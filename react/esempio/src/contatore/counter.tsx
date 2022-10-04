import React, { useReducer, useContext } from 'react';

import { Buttons } from './buttons';


import { CounterDispatch } from './main'
// export const CounterDispatch = React.createContext<any | null>(null);

// function reducer(state: { count: number; }, action: { type: any; }) {
//     switch (action.type) {
//         case 'increment':
//             return { count: state.count + 1 };
//         case 'decrement':
//             return { count: state.count - 1 };
//         default:
//             throw new Error();
//     }
// }
const initialState = { count: 0 };

export function Counter(props: { state: { count: any; } }) {
    // const [state, dispatch] = useReducer(reducer, initialState);

    const dispatch = useContext(CounterDispatch);
    return (
        <>
            Count: {props.state.count}
            <button onClick={() => dispatch({ type: 'decrement' })}>-</button>
            <button onClick={() => dispatch({ type: 'increment' })}>+</button>
            <Buttons></Buttons>
        </>
    );
}
