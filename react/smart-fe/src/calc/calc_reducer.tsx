export const calcReducerInitialState = { stack: [1, 2, 3], inputItem: "" };

export function calcReducer(state: any, action: { type: string, payload: any }) {
    switch (action.type) {
        case 'enter':
            return { ...state, stack: [...state.stack, state.inputItem] };
        case 'drop':
            return { ...state, stack: [...state.stack.slice(0, -1)] };
        case 'set-input-item':
            return { ...state, inputItem: action.payload.item };
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