export const calcReducerInitialState = { stack: [1, 2, 3], inputItem: "" };

type StackFunction = ((a: any, b: any) => any) | ((a: any) => any);
const performOnStack = (stack: any[], performer: StackFunction): any[] => {

    if (stack.length > 1) {
        try {
            const sliced = stack.slice(-2);
            const [a, b] = sliced;
            return [...sliced, performer(a, b)]
        } catch (e) {
            return [...stack, String(e)]
        }

    }

    return stack;
}

export function calcReducer(state: any, action: { type: string, payload: any }) {
    switch (action.type) {
        case 'enter':
            return { ...state, stack: [...state.stack, state.inputItem] };
        case 'drop':
            return { ...state, stack: [...state.stack.slice(0, -1)] };
        case 'set-input-item':
            return { ...state, inputItem: action.payload.item };
        case 'sum':
            return { ...state, stack: performOnStack(state.stack, (a, b) => a + b) };
        case 'sub':
            return { ...state, stack: performOnStack(state.stack, (a, b) => a - b) };
        case 'mul':
            return { ...state, stack: performOnStack(state.stack, (a, b) => a * b) };
        case 'div':
            return { ...state, stack: performOnStack(state.stack, (a, b) => a / b) };
        default:
            throw new Error();
    }
}

export function doSetInputItem(item: any): { type: string, payload: any } {
    return { type: "set-input-item", payload: { item } };
}

export function doCalcEnter(): { type: string } {
    return { type: "enter" };
}

export function doCalcDrop(): { type: string } {
    return { type: "drop" };
}

export function doCalcSum(): { type: string } {
    return { type: "sum" };
}

export function doCalcSub(): { type: string } {
    return { type: "sub" };
}

export function doCalcMul(): { type: string } {
    return { type: "mul" };
}

export function doCalcDiv(): { type: string } {
    return { type: "div" };
}