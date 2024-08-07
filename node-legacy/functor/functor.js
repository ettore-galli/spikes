// zero :: () -> Number
function fZero() {
    console.log('Starting with nothing');
    // Definitely not launching a nuclear strike here.
    // But this function is still impure.
    return 0;
}


// Effect :: Function -> Effect
function Effect(f) {
    return {
        introspect() {
            console.log(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>");
            console.log(`f=${f}`)
            console.log("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<");
        },
        map(g) {
            return Effect(x => g(f(x)));
        },
        runEffects(x) {
            return f(x);
        }
    }
}

Effect.of = (value) => Effect(() => value);

console.log("------------------------------------------------------------------------")

const zero = Effect(fZero);
zero.introspect();

const increment = x => x + 1; // Just a regular function.

const one = zero.map(increment);
one.introspect();

one.runEffects();


console.log("------------------------------------------------------------------------")

MY_DATA = {
    "a": "lasdkaòlskdaòlskd",
    "b": "bxcbzmxcbzxbcznm",
    "c": "ldskaskdsdòaskd"
}

const getSomeDataDirty = (key) => MY_DATA[key];
const getSomeData = (key) => Effect.of(getSomeDataDirty(key));

const processData = (data) => `<<<< ${data} >>>>`;

const putDataDirty = (data) => {
    console.log(data);
    console.log("---");
}

const putData = (data) => Effect.of(putDataDirty(data))

const key = Effect.of("b");
// const process = key.map(getSomeData).runEffects().map(putData);
const process = key.map(getSomeData).runEffects().map(processData).map(putData);

process.runEffects() 