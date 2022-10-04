import React, { useReducer, useContext } from 'react';


import { CounterDispatch } from './main'

export function Buttons() {
    const dispatch = useContext(CounterDispatch)

    return (
        <>
            <button onClick={() => dispatch({ type: 'decrement' })}>-</button>
            <button onClick={() => dispatch({ type: 'increment' })}>+</button>
        </>
    );
}
