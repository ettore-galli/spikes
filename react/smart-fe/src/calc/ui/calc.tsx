import { createCalcEvents } from '../rpn-logic/events';

import CalcDisplay from './calc-display';
import CalcInput from './calc-input';
import CalcKeyboard from './calc-keyboard';

interface Props {
    state: any,
    dispatch: any
}

function Calc(props: Props) {

    const calcEvents = createCalcEvents(props.dispatch);

    return (
        <>
            {/* <CalcDisplay {...props} /> */}
            <CalcDisplay state={props.state} />
            <hr />
            <CalcInput calcEvents={calcEvents} state={props.state} />
            <hr />
            <CalcKeyboard calcEvents={calcEvents} />
        </>
    );
}

export default Calc;
