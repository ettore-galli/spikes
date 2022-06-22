const express = require("express");
const bodyParser = require("body-parser");
const path = require('node:path');

const app = express();

let messages = [
    { "message": "Message 1", "name": "gino" },
 
];

app.use(express.static(path.join(__dirname, "ui")));
app.use(bodyParser.json());

app.get('/messages', (req, res) => { res.send(messages) });

app.post('/message', (req, res) => {
    console.log(req.body);
    messages.push(req.body);
    res.sendStatus(200)
});

const server = app.listen(3000, () => { console.log(`Started on port ${server.address().port}`) });

