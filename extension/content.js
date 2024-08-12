// content.js

chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    if (request.action === "scanPage") {
        const pageDetails = {
            url: window.location.href,
            backgroundColor: window.getComputedStyle(document.body, null).getPropertyValue('background-color'),
            title: document.title,
            textContent: document.body.innerText,
            links: Array.from(document.querySelectorAll('a')).map(link => link.href),
            images: Array.from(document.querySelectorAll('img')).map(img => img.src)
        };
        sendResponse(pageDetails);
    }
});