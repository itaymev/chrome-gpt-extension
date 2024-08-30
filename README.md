# Chrome Chat Extension

## Description

The Chrome Chat Extension allows users to interact with OpenAI's ChatGPT directly from their browser. The extension scans the current webpage and sends relevant information to the ChatGPT model, which then provides responses based on the page content and user input.

## Features

- Scans the current webpage for various elements like links, images, meta tags, headings, forms, scripts, stylesheets, structured data, media, navigation, tables, and comments.
- Sends the scanned page details along with user input to a backend server that interacts with OpenAI's ChatGPT.
- Displays the response from ChatGPT in the extension's popup interface.

## Requirements

- Python 3.7+
- Flask
- Flask-CORS
- httpx
- OpenAI SDK
- Google Chrome Browser

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/chrome-chat-extension.git
    cd chrome-chat-extension
    ```

2. Install the required Python packages:
    ```sh
    pip install -r requirements.txt
    ```

3. Set up environment variables for OpenAI:
    ```sh
    export OPENAI_KEY=your_openai_key
    export OPENAI_ENDPOINT=your_openai_endpoint
    ```

4. Run the Flask server:
    ```sh
    python server.py
    ```

5. Load the extension in Chrome:
    - Open Chrome and go to `chrome://extensions/`.
    - Enable "Developer mode" by toggling the switch in the top right corner.
    - Click "Load unpacked" and select the directory where you cloned the repository.

## File Descriptions

### `content.js`

This file contains the content script that scans the current webpage for various elements and collects details such as links, images, meta tags, headings, forms, scripts, stylesheets, structured data, media, navigation, tables, and comments. It sends these details to the background script when a message with the action "scanPage" is received.

### `background.js`

This file contains the background script that listens for messages from the popup script and executes the content script on the active tab to collect page details.

### `manifest.json`

This file defines the extension's metadata, permissions, and the scripts to be loaded. It specifies the content script to be injected into all webpages and the background script to be used as a service worker.

### `popup.html`

This file defines the HTML structure of the extension's popup interface. It includes a text area for user input, a send button, and a container to display chat messages.

### `style.css`

This file contains the CSS styles for the popup interface, including the layout and appearance of the chat container, text area, and buttons.

### `popup.js`

This file contains the JavaScript logic for the popup interface. It handles user interactions, such as sending messages, displaying loading indicators, and showing responses from the server. It also sends a message to the background script to execute the content script and collect page details.

### `OpenAIConnector.py`

This file contains the `OpenAIConnector` class, which interacts with the OpenAI API. It initializes the OpenAI client, sends prompts to the API, and retrieves responses.

### `server.py`

This file contains the Flask server that handles incoming requests from the extension. It receives the user input and page details, sends them to the OpenAI API via the `OpenAIConnector`, and returns the response to the extension.

## Usage

1. Open the Chrome browser and navigate to any webpage.
2. Click on the Chrome Chat Extension icon in the toolbar to open the popup interface.
3. Type your message in the text area and click "Send".
4. The extension will scan the current webpage, send the details along with your message to the backend server, and display the response from ChatGPT in the popup interface.