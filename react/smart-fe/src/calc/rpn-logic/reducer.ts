import { performOnStack } from './rpn-logic-utils';

const BLANK: string = "";
export const calcReducerInitialState = { stack: [], inputItem: BLANK };

export function calcReducer(state: any, action: { type: string, payload: any }) {
    switch (action.type) {
        case 'enter':
            return { ...state, stack: [...state.stack, state.inputItem], inputItem: BLANK };
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

