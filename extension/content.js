// content.js
console.log("Content script loaded");

chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    console.log("Message received in content script", request);
    if (request.action === "scanPage") {
      const pageDetails = {
        url: window.location.href,
        backgroundColor: window.getComputedStyle(document.body).backgroundColor,
        title: document.title,
        textContent: document.body.innerText
      };
      sendResponse(pageDetails);
    }
  });
  