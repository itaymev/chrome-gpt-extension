from flask import Flask, request, jsonify
from flask_cors import CORS
from OpenAIConnector import OpenAIConnector

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
connector = OpenAIConnector()

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    prompt = data.get('prompt')
    system_msg = data.get('system_msg', 'You are a helpful assistant. You must only respond in plain text')
    response = connector.run_prompt(prompt, system_msg)

    print(response)
    return jsonify(response)

if __name__ == '__main__':
    app.run(port=5000)