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
    system_msg = data.get('system_msg', "You are a helpful assistant and you will be given page details about the user's active tab when prompted. You must only respond in plain text.")
    page_details = data.get('pageDetails', {})

    # Combine prompt with page details
    full_prompt = f"{prompt}\n\nPage Details:\nURL: {page_details.get('url')}\nTitle: {page_details.get('title')}\nBackground Color: {page_details.get('backgroundColor')}\nText Content: {page_details.get('textContent')}\nLinks: {page_details.get('links')}\nImages: {page_details.get('images')}"

    response = connector.run_prompt(full_prompt, system_msg)

    return jsonify(response)

if __name__ == '__main__':
    app.run(port=5000)