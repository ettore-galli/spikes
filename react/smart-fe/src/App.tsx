import React, { useReducer } from 'react';

import './App.css';
import Calc from './calc/calc';
import { calcReducer, calcReducerInitialState } from './calc/calc_reducer';

function App() {

  const [state, dispatch] = useReducer(calcReducer, calcReducerInitialState);

  return (
    <div className="App">
      <header className="App-header">
        <Calc state={state} dispatch={dispatch} />
      </header>
    </div>
  );
}

export default App;
