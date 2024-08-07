
const _MESSAGES = [
    "Message 1",
    "Message 2",
    "Message 3"
];

const MESSAGES = _MESSAGES;

function getMessages() {

    return new Promise((resolve, reject) => {
        const messages = MESSAGES;
        if (messages.length > 0) {
            resolve(messages);
        } else {
            reject("No messages found")
        }

    })

}

function displayMessages(messages) {
    const SEP = "----------------------------------------------------------------------"
    console.log(SEP);
    messages.forEach(message => {
        console.log(`- ${message}`)
    });
    console.log(SEP);
}


function displayError(error) {
    console.log(`ERROR: ${error} !`);
}

function main() {
    getMessages().then(displayMessages).catch(displayError);
}

async function async_main() {
    const messages = await getMessages();
    await displayMessages(messages);
}

async_main();