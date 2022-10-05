
interface CalcDisplayProps {
    state: any,
}

function CalcDisplay(props: CalcDisplayProps) {
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
