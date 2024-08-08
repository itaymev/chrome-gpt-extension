from flask import Flask, request, jsonify
from flask_cors import CORS
from OpenAIConnector import OpenAIConnector

app = Flask(__name__)
CORS(app)
connector = OpenAIConnector()

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    prompt = data.get('prompt')
    system_msg = data.get('system_msg', 'You are a helpful assistant. Your responses must be as concise and short as possible. You must only respond in plain text')
    response = connector.run_prompt(prompt, system_msg)

    return jsonify(response)

@app.route('/scan', methods=['POST'])
def scan():
    data = request.json
    url = data.get('url')
    backgroundColor = data.get('backgroundColor')
    title = data.get('title')
    textContent = data.get('textContent')

    # Return a response
    return jsonify(url, backgroundColor, title, textContent)

if __name__ == '__main__':
    app.run(port=5000)