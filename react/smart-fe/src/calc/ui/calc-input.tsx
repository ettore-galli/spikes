// import { createCalcEvents } from '../logic/events';

interface CalcInputProps {
    state: any,
    calcEvents: any // TODO: Evoid any

}

function CalcInput(props: CalcInputProps) {

    // const calcEvents = createCalcEvents(props.dispatch);

    const {calcEvents} = props;

    return (
        <>
            <input key={"new"} value={props.state.inputItem} onChange={calcEvents.setNewValue} />
        </>
    );
}

export default CalcInput;
