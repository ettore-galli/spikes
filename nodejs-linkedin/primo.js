const path = require("path");

const message = "Hello, world!"
console.log(message.slice(4));
console.log(__dirname);
console.log(__filename);

console.log(`file = ${path.basename(__filename)}`);


for (let key in global) {
    console.log(key)
}

console.log("-----------------------")


console.log(process.argv);


function getParam(flag) {
    const indexFlag = process.argv.indexOf(flag);
    return indexFlag < 0 ? null : process.argv[indexFlag + 1];

}

for (let flag of ["nome", "cognome"]) {
    const flagKey = `--${flag}`;
    const message = `${flag} --> ${getParam(flagKey)}`;
    console.log(message);
}

process.stdin.on("data", (x) => { console.log(x.toString().trim()) });

