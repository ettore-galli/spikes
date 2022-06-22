const fs = require("fs");

fs.readFile("./files/dati.json", 'utf-8', (_, data) => { console.log(data) })

fs.readdir("./files", (_, data) => { console.log(data) });

fs.writeFile("./files/output.json", JSON.stringify({ "test": 123 }), _ => { /* handle error */ });