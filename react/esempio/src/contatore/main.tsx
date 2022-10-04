import React, { useReducer, useContext } from 'react';

import { Counter } from './counter';

const initialState = { count: 0 };

export const CounterDispatch = React.createContext<any | null>(null);

function reducer(state: { count: number; }, action: { type: any; }) {
    switch (action.type) {
        case 'increment':
            return { count: state.count + 1 };
        case 'decrement':
            return { count: state.count - 1 };
        default:
            throw new Error();
    }
}


export function Main() {
    const [state, dispatch] = useReducer(reducer, initialState);
    return (
        <CounterDispatch.Provider value={dispatch}>
            <Counter state={state} />
        </CounterDispatch.Provider>
    );
}
