import os, httpx
from openai import AzureOpenAI

DEFAULT_DEPLOYMENT_NAME = "gpt-4o"

class OpenAIConnector:
    def __init__(self, deployment_name = None) -> None:
        if deployment_name is None:
            deployment_name = DEFAULT_DEPLOYMENT_NAME
        
        self.deployment_name = deployment_name
        # print("INFO - %s: using deployment: %s"%(__file__, deployment_name,))

        self.client = AzureOpenAI(
                        api_version = "2024-02-01", # This is the latest version as of 8/8/2024
                        api_key = self.get_ai_key(),
                        base_url = self.get_ai_endpoint(),
                        default_headers={"Ocp-Apim-Subscription-Key" :self.get_ai_key()},
                        http_client=httpx.Client(verify=False)
                    )
    
    def run_prompt(self, prompt, system_msg):
        full_prompt = [
            {"role": "system", "content": system_msg},
            {"role": "user", "content": prompt}
        ]

        completion = self.client.chat.completions.create(
            model=self.deployment_name,
            messages=full_prompt, 
            max_tokens = 4096
        )

        # print(f"INFO - {__file__}: Prompt tokens: {completion.usage.prompt_tokens}")
        # print(f"INFO - {__file__}: Completion tokens: {completion.usage.completion_tokens}")
        # print(f"INFO - {__file__}: GPT finish reason: {completion.choices[0].finish_reason}")
    
        gpt_response = completion.choices[0].message.content

        return gpt_response

    def get_ai_key(self) -> str:
        if "OPENAI_KEY" in os.environ:
            # print("INFO - %s: Found OPENAI_KEY environment variable."%(__file__,))
            return os.environ["OPENAI_KEY"]
        elif "openai_key" in os.environ:
            # print("INFO - %s: Found OPENAI_KEY environment variable."%(__file__,))
            return os.environ["openai_key"]
        else:
            raise Exception("ERROR - %s: OpenAI key not found in environment variables"%(__file__,))
        
    def get_ai_endpoint(self) -> str:
        if "OPENAI_ENDPOINT" in os.environ:
            # print("INFO - %s: Found OPENAI_ENDPOINT environment variable."%(__file__,))
            return os.environ["OPENAI_ENDPOINT"]
        elif "openai_endpoint" in os.environ:
            # print("INFO - %s: Found OPENAI_ENDPOINT environment variable."%(__file__,))
            return os.environ["openai_endpoint"]
        else:
            raise Exception("ERROR - %s: OpenAI endpoint not found in environment variables"%(__file__,))