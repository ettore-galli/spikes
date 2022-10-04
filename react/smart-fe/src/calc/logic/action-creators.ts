
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