import { useReducer } from 'react';

import Calc from './ui/calc';
import { calcReducer, calcReducerInitialState } from './logic/reducer';

function CalcMain() {

  const [state, dispatch] = useReducer(calcReducer, calcReducerInitialState);

  return <Calc state={state} dispatch={dispatch} />;

}

export default CalcMain;