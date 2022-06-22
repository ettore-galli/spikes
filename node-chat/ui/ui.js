console.log("Javascript module loaded")


const ENDPOINTS = {
    "messages": "http://localhost:3000/messages",
    "message": "http://localhost:3000/message"
}

function getOwnIdentity() {
    return "myself";
}

function getMessages(putMessages) {
    fetch(ENDPOINTS["messages"])
        .then(response => response.json())
        .then(messages => putMessages(messages));

}

function renderMessages(messages) {
    return messages.map(m => `<h4>${m.name}</h4><h5>${m.message}</h5>`).reduce((full, current) => full + current, "");
}

function displayMessages(hostDiv) {
    getMessages(ms => { document.getElementById(hostDiv).innerHTML = renderMessages(ms) })
}

function renderPage() {
    displayMessages("messages");
}

function pageInit() {
    document.getElementById("send").addEventListener("click", _ => { sendMessage(document.getElementById("message").value) });
    renderPage();
}

function buildMessage(text) {
    return { "message": text, "name": getOwnIdentity() }
}

function sendMessage(text) {
    fetch(ENDPOINTS["message"],
        {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(buildMessage(text))
        })
        .then(_ => renderPage());
}



document.addEventListener("DOMContentLoaded", pageInit);



