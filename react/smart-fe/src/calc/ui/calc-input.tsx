import { createCalcEvents } from '../logic/events';

interface Props {
    state: any,
    dispatch: any

}

function CalcInput(props: Props) {

    const calcEvents = createCalcEvents(props.dispatch);

    return (
        <>
            <input key={"new"} value={props.state.inputItem} onChange={calcEvents.setNewValue} />
        </>
    );
}

export default CalcInput;
