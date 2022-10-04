type StackFunction = ((a: any, b: any) => any) | ((a: any) => any);

export const performOnStack = (stack: any[], performer: StackFunction): any[] => {

    if (stack.length > 1) {
        try {
            const sliced = stack.slice(-2);
            const [a, b] = sliced;
            return [...sliced, performer(parseFloat(a), parseFloat(b))]
        } catch (e) {
            return [...stack, String(e)]
        }

    }

    return stack;
}