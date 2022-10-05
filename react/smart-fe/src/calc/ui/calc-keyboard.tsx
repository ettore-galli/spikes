interface KeyboardProps {
    calcEvents: any // TODO: Avoid any
}

function CalcKeyboard(props: KeyboardProps) {

    const { calcEvents } = props;

    return (
        <>
            <input type="button" value="ENTER" onClick={calcEvents.doCalcEnter} />
            <input type="button" value="DROP" onClick={calcEvents.doCalcDrop} />
            <input type="button" value="[+]" onClick={calcEvents.doCalcSum} />
            <input type="button" value="[-]" onClick={calcEvents.doCalcSub} />
            <input type="button" value="[*]" onClick={calcEvents.doCalcMul} />
            <input type="button" value="[/]" onClick={calcEvents.doCalcDiv} />
        </>
    );
}

export default CalcKeyboard;
