
interface Props {
    state: any,
    dispatch: any

}

function CalcDisplay(props: Props) {
    return (
        <>
            {
                props.state.stack.map((item: any, index: number) => {
                    return <input key={index} value={item} readOnly={true} />
                })
            }
        </>
    );
}

export default CalcDisplay;
