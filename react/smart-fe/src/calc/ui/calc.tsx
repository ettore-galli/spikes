import { createCalcEvents } from '../rpn-logic/events';

import CalcDisplay from './calc-display';
import CalcInput from './calc-input';
import CalcKeyboard from './calc-keyboard';

import * as rpnActioncreators from '../rpn-logic/action-creators';
import { bindActionCreators } from '../reducer-utils/reducer-utils';

interface Props {
    state: any,
    dispatch: any
}

function Calc(props: Props) {

    const calcEvents = createCalcEvents(props.dispatch);

    // console.log(bindActionCreators(rpnActioncreators));

    const calcEvents2 = bindActionCreators(rpnActioncreators, props.dispatch);

    console.log(calcEvents)
    console.log(calcEvents2)

    return (
        <>
            {/* <CalcDisplay {...props} /> */}
            <CalcDisplay state={props.state} />
            <hr />
            <CalcInput calcEvents={calcEvents} state={props.state} />
            <hr />
            <CalcKeyboard calcEvents={calcEvents} calcEvents2={calcEvents2}/>
        </>
    );
}

export default Calc;
