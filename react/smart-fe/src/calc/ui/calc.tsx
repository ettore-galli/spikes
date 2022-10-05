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

    const calcEvents = bindActionCreators(rpnActioncreators, props.dispatch);

    return (
        <>
            <CalcDisplay state={props.state} />
            <hr />
            <CalcInput calcEvents={calcEvents} state={props.state} />
            <hr />
            <CalcKeyboard calcEvents={calcEvents} />
        </>
    );
}

export default Calc;
