import { createCalcEvents } from './logic/events';

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
            <CalcDisplay {...props} />
            <hr />
            <CalcInput {...props} />
            <hr />
            <CalcKeyboard {...props} />
        </>
    );
}

export default Calc;
