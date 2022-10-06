import { useReducer } from 'react';

import { bindActionCreators } from './reducer-utils/reducer-utils';

import * as rpnLogic from './rpn-logic';

import Calc from './ui/calc';

function CalcMain() {

  const [state, dispatch] = useReducer(rpnLogic.calcReducer, rpnLogic.calcReducerInitialState);
  const calcEvents = bindActionCreators(rpnLogic.rpnActioncreators, dispatch);

  return <Calc state={state} dispatch={dispatch} calcEvents={calcEvents} />;

}

export default CalcMain;