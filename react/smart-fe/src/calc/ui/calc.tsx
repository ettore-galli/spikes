import { useEffect } from 'react';

import CalcDisplay from './calc-display';
import CalcInput from './calc-input';
import CalcKeyboard from './calc-keyboard';

interface Props {
    state: any,
    dispatch: any
    calcEvents: any
}

const Calc: React.FC<Props> = (props: Props) => {

    useEffect(() => {
        document.title = 'Esempio applicazione React';
    });

    return (
        <>
            <CalcDisplay state={props.state} />
            <hr />
            <CalcInput calcEvents={props.calcEvents} state={props.state} />
            <hr />
            <CalcKeyboard calcEvents={props.calcEvents} />
        </>
    );
}

export default Calc;
