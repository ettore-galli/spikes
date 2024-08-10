import * as readline from 'readline';

function processAnswer(readLine, answer) {
    console.log(`. ${answer}`);
    readLine.close();
}

function main() {
    const readLine = readline.createInterface(
        {
            input: process.stdin,
            output: process.stdout
        }
    );

    readLine.question(">>>", processAnswer.bind(null, readLine))
}

main();