import React from 'react';

import { doCalcEnter, doCalcDrop, doSetInputItem } from './calc_reducer';

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

    return (
        <>  {props.state.stack}
            {props.state.inputItem}
            {
                props.state.stack.map((item: any, index: number) => {
                    return <input key={index} value={item} readOnly={true} />
                })
            }
            <input key={"new"} value={props.state.inputItem} onChange={setNewValue} />
            <input type="button" value="ENTER" onClick={enter} />
            <input type="button" value="DROP" onClick={drop} />
        </>

    );
}

export default Calc;
