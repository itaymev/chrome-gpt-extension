import os, httpx
from openai import AzureOpenAI

DEFAULT_DEPLOYMENT_NAME = "gpt-4o"

class OpenAIConnector:
    def __init__(self, deployment_name = None) -> None:
        if deployment_name is None:
            deployment_name = DEFAULT_DEPLOYMENT_NAME
            # print("INFO - %s: using default deployment: %s"%(__file__, deployment_name,))
        self.deployment_name = deployment_name

        self.client = AzureOpenAI(
                        api_version = "2023-07-01-preview",
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

        # print(f"Prompt tokens: {completion.usage.prompt_tokens}")
        # print(f"Completion tokens: {completion.usage.completion_tokens}")
        # print(f"GPT finish reason: {completion.choices[0].finish_reason}")
    
        gpt_response = completion.choices[0].message.content

        return gpt_response

    def get_ai_key(self) -> str:
        if "OPENAI_KEY" in os.environ:
            return os.environ["OPENAI_KEY"]
        elif "openai_key" in os.environ:
            return os.environ["openai_key"]
        else:
            raise Exception("OpenAI key not found in environment variables")
        
    def get_ai_endpoint(self) -> str:
        if "OPENAI_ENDPOINT" in os.environ:
            return os.environ["OPENAI_ENDPOINT"]
        elif "openai_endpoint" in os.environ:
            return os.environ["openai_endpoint"]
        else:
            raise Exception("OpenAI endpoint not found in environment variables")