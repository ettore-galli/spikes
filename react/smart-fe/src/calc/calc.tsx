import { createCalcEvents } from './logic/events';

interface Props {
    state: any,
    dispatch: any

}

function Calc(props: Props) {

    const calcEvents = createCalcEvents(props.dispatch);

    return (
        <>
            {
                props.state.stack.map((item: any, index: number) => {
                    return <input key={index} value={item} readOnly={true} />
                })
            }
            <hr />
            <input key={"new"} value={props.state.inputItem} onChange={calcEvents.setNewValue} />
            <hr />
            <input type="button" value="ENTER" onClick={calcEvents.enter} />
            <input type="button" value="DROP" onClick={calcEvents.drop} />
            <input type="button" value="[+]" onClick={calcEvents.stackSum} />
            <input type="button" value="[-]" onClick={calcEvents.stackSub} />
            <input type="button" value="[*]" onClick={calcEvents.stackMul} />
            <input type="button" value="[/]" onClick={calcEvents.stackDiv} />
        </>

    );
}

export default Calc;
