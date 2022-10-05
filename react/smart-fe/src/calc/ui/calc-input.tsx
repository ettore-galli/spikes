interface CalcInputProps {
    state: any,
    calcEvents: any // TODO: Avoid any

}

function CalcInput(props: CalcInputProps) {

    const { calcEvents } = props;

    const setNewValue = (e: any) => {
        calcEvents.doSetInputItem(e.target.value);
    }

    return (
        <>
            <input key={"new"} value={props.state.inputItem} onChange={setNewValue} />
        </>
    );
}

export default CalcInput;
