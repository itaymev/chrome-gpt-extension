// Send button
document.getElementById('send').addEventListener('click', async () => {
    const message = document.getElementById('textarea').value;
    const chatContainer = document.getElementById('chat-container');

    // User message
    const userMessageDiv = document.createElement('div');
    userMessageDiv.className = 'message user-message';
    userMessageDiv.innerText = message;
    chatContainer.appendChild(userMessageDiv);

    // Clear textbox
    document.getElementById('textarea').value = '';

    // Loading message
    const loadingDiv = document.createElement('div');
    loadingDiv.className = 'message loading-message';
    loadingDiv.innerText = 'Loading...';
    chatContainer.appendChild(loadingDiv);

    try {
        const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
        chrome.scripting.executeScript(
            {
                target: { tabId: tab.id },
                files: ['content.js']
            },
            async () => {
                chrome.tabs.sendMessage(tab.id, { action: "scanPage" }, async (pageDetails) => {
                    if (chrome.runtime.lastError) {
                        chatContainer.removeChild(loadingDiv);
                        const errorMessageDiv = document.createElement('div');
                        errorMessageDiv.className = 'message error-message';
                        errorMessageDiv.innerHTML = `<div class="response">Error: ${chrome.runtime.lastError.message}</div>`;
                        chatContainer.appendChild(errorMessageDiv);
                        return;
                    }

                    if (!pageDetails || Object.keys(pageDetails).length === 0) {
                        chatContainer.removeChild(loadingDiv);
                        const errorMessageDiv = document.createElement('div');
                        errorMessageDiv.className = 'message error-message';
                        errorMessageDiv.innerHTML = `<div class="response">Error: No page details received.</div>`;
                        chatContainer.appendChild(errorMessageDiv);
                        return;
                    }

                    const { url, backgroundColor, title, textContent, links, images } = pageDetails;

                    const response = await fetch('http://localhost:5000/chat', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json'
                        },
                        body: JSON.stringify({
                            prompt: message + "\n\n\nThe following is webpage information about the user's Active Tab:\n" + url + backgroundColor + title + textContent + links + images,
                            system_msg: "You are a helpful assistant and you will be given page details about the user's active tab when prompted. You must only respond in plain text.",
                        })
                    });

                    const data = await response.json();
                    chatContainer.removeChild(loadingDiv);

                    // Response message
                    const responseMessageDiv = document.createElement('div');
                    responseMessageDiv.className = 'message response-message';
                    responseMessageDiv.innerHTML = `<div class="response">${data}</div>`;
                    chatContainer.appendChild(responseMessageDiv);
                });
            }
        );
    } catch (error) {
        chatContainer.removeChild(loadingDiv);

        // Error message
        const errorMessageDiv = document.createElement('div');
        errorMessageDiv.className = 'message error-message';
        errorMessageDiv.innerHTML = `<div class="response">Error: ${error.message}</div>`;
        chatContainer.appendChild(errorMessageDiv);
    }

    chatContainer.scrollTop = chatContainer.scrollHeight;
});

// Enter key binded to send button
document.getElementById('textarea').addEventListener('keydown', (event) => {
  if (event.key === 'Enter') {
      event.preventDefault();
      document.getElementById('send').click();
  }
});