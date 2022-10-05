interface KeyboardProps {
    calcEvents: any // TODO: Avoid any
}

function CalcKeyboard(props: KeyboardProps) {


    const { calcEvents } = props;

    return (
        <>
            <input type="button" value="ENTER" onClick={calcEvents.enter} />
            <input type="button" value="DROP" onClick={calcEvents.drop} />
            <input type="button" value="[+]" onClick={calcEvents.stackSum} />
            <input type="button" value="[-]" onClick={calcEvents.stackSub} />
            <input type="button" value="[*]" onClick={calcEvents.stackMul} />
            <input type="button" value="[/]" onClick={calcEvents.stackDiv} />
        </>
    );
}

export default CalcKeyboard;
