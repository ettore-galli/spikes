import { useReducer } from 'react';

import Calc from './ui/calc';

import { calcReducer, calcReducerInitialState } from './rpn-logic/reducer';
// import * as rpnActioncreators from './rpn-logic/action-creators';
// import { bindActionCreators } from './reducer-utils/reducer-utils';

function CalcMain() {

  // console.log(bindActionCreators(rpnActioncreators));

  const [state, dispatch] = useReducer(calcReducer, calcReducerInitialState);

  return <Calc state={state} dispatch={dispatch} />;

}

export default CalcMain;