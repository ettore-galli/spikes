import React, { useState, useEffect } from 'react';

// ----- utility

export const getNextCounterNumber = (previous: number): Promise<number> => {
    const INC: number = 1;
    return new Promise((resolve, reject) => { resolve(previous + INC) })
}

// ----- hook

const useCounter = (initial: number): [number, (() => void)] => {
    const [hCounter, setHCounter] = useState(initial);

    const inc = (): void => {
        getNextCounterNumber(hCounter)
            .then(newCounterValue => { setHCounter(newCounterValue) })
    }

    return [hCounter, inc]
}


const Contatore: React.FC = () => {

    // senza hook
    const [counter, setCounter] = useState(1); 
    const increment = () => {
        getNextCounterNumber(counter).then(newCounterValue => { setCounter(newCounterValue) });
    }

    // custom hook
    const [cnt, incVal] = useCounter(0)


    return (
        <>
            <div><h1>Contatore</h1></div>

            <hr />

            <p>Senza hook</p>

            <div>
                {counter}
                <input type={"button"} value={"+"} onClick={increment}></input>
            </div>

            <hr />

            <p>Con Custom Hook</p>

            <div>
                {cnt}
                <input type={"button"} value={"+"} onClick={incVal}></input>
            </div>
        </>
    );
};

export default Contatore;