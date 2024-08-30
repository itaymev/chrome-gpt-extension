// content.js

chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    if (request.action === "scanPage") {
        const pageDetails = {
            url: window.location.href,
            backgroundColor: window.getComputedStyle(document.body, null).getPropertyValue('background-color'),
            title: document.title,
            textContent: document.body.innerText,
            links: Array.from(document.querySelectorAll('a')).map(link => link.href) || [],
            images: Array.from(document.querySelectorAll('img')).map(img => img.src) || [],
            metaTags: Array.from(document.querySelectorAll('meta')).map(meta => ({
                name: meta.getAttribute('name'),
                content: meta.getAttribute('content')
            })) || [],
            headings: Array.from(document.querySelectorAll('h1, h2, h3, h4, h5, h6')).map(heading => ({
                tag: heading.tagName,
                text: heading.innerText
            })) || [],
            forms: Array.from(document.querySelectorAll('form')).map(form => ({
                action: form.action,
                method: form.method,
                inputs: Array.from(form.querySelectorAll('input, textarea, select')).map(input => ({
                    type: input.type,
                    name: input.name,
                    value: input.value
                }))
            })) || [],
            scripts: Array.from(document.querySelectorAll('script')).map(script => script.src) || [],
            stylesheets: Array.from(document.querySelectorAll('link[rel="stylesheet"]')).map(link => link.href) || [],
            structuredData: Array.from(document.querySelectorAll('script[type="application/ld+json"]')).map(script => script.innerText) || [],
            media: {
                audio: Array.from(document.querySelectorAll('audio')).map(audio => audio.src) || [],
                video: Array.from(document.querySelectorAll('video')).map(video => video.src) || []
            },
            navigation: Array.from(document.querySelectorAll('nav a')).map(nav => ({
                text: nav.innerText,
                href: nav.href
            })) || [],
            tables: Array.from(document.querySelectorAll('table')).map(table => ({
                headers: Array.from(table.querySelectorAll('th')).map(th => th.innerText) || [],
                rows: Array.from(table.querySelectorAll('tr')).map(tr => Array.from(tr.querySelectorAll('td')).map(td => td.innerText)) || []
            })) || [],
            comments: Array.from(document.querySelectorAll('.comment, .review')).map(comment => comment.innerText) || []
        };
        sendResponse(pageDetails);
    }
});