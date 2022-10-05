interface KeyboardProps {
    calcEvents: any // TODO: Avoid any
    calcEvents2: any // TODO: Avoid any
}

function CalcKeyboard(props: KeyboardProps) {


    const { calcEvents, calcEvents2 } = props;

    return (
        <>
            <input type="button" value="ENTER" onClick={calcEvents2.doCalcEnter} />
            <input type="button" value="DROP" onClick={calcEvents.drop} />
            <input type="button" value="[+]" onClick={calcEvents.stackSum} />
            <input type="button" value="[-]" onClick={calcEvents.stackSub} />
            <input type="button" value="[*]" onClick={calcEvents.stackMul} />
            <input type="button" value="[/]" onClick={calcEvents.stackDiv} />
        </>
    );
}

export default CalcKeyboard;
