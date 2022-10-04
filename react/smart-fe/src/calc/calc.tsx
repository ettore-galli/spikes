import { doCalcEnter, doCalcDrop, doSetInputItem, doCalcSum, doCalcSub, doCalcMul, doCalcDiv } from './calc_reducer';

interface Props {
    state: any,
    dispatch: any
}

function Calc(props: Props) {

    const setNewValue = (e: any) => {
        props.dispatch(doSetInputItem(e.target.value))
    }

    const enter = () => {
        props.dispatch(doCalcEnter())
    }

    const drop = () => {
        props.dispatch(doCalcDrop())
    }

    const stackSum = () => {
        props.dispatch(doCalcSum())
    }

    const stackSub = () => {
        props.dispatch(doCalcSub())
    }

    const stackMul = () => {
        props.dispatch(doCalcMul())
    }

    const stackDiv = () => {
        props.dispatch(doCalcDiv())
    }

    return (
        <>
            {
                props.state.stack.map((item: any, index: number) => {
                    return <input key={index} value={item} readOnly={true} />
                })
            }
            <hr />
            <input key={"new"} value={props.state.inputItem} onChange={setNewValue} />
            <hr />
            <input type="button" value="ENTER" onClick={enter} />
            <input type="button" value="DROP" onClick={drop} />
            <input type="button" value="[+]" onClick={stackSum} />
            <input type="button" value="[-]" onClick={stackSub} />
            <input type="button" value="[*]" onClick={stackMul} />
            <input type="button" value="[/]" onClick={stackDiv} />
        </>

    );
}

export default Calc;
