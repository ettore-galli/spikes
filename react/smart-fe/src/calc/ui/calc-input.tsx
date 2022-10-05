interface CalcInputProps {
    state: any,
    calcEvents: any // TODO: Evoid any

}

function CalcInput(props: CalcInputProps) {


    const { calcEvents } = props;

    return (
        <>
            <input key={"new"} value={props.state.inputItem} onChange={calcEvents.setNewValue} />
        </>
    );
}

export default CalcInput;
