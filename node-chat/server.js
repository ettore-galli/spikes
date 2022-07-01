const express = require("express");
const bodyParser = require("body-parser");
const path = require('node:path');

const app = express();
const http = require('http').Server(app);
const io = require('socket.io')(http)

let messages = [
    { "message": "Message 1", "name": "gino" },

];

app.use(express.static(path.join(__dirname, "ui")));
app.use(bodyParser.json());

app.get('/messages', (_, res) => { res.send(messages) });

app.post('/message', (req, res) => {
    console.log(req.body);
    messages.push(req.body);
    res.sendStatus(200)
});

const ioConnectionHandler = (socket) => {
    console.log(`Connected to ${socket.address}`)
}

io.on("connection", ioConnectionHandler)
const server = http.listen(3000, () => { console.log(`Started on port ${server.address().port}`) });

