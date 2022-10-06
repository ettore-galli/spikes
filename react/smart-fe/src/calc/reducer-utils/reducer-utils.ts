export const bindActionCreators = (actionCreators: { [key: string]: ((...args: any) => Object) }, dispatch: ((action: any) => void)) => {
    return Object.keys(actionCreators).reduce((prv, cur) => {
        return {
            ...prv, [cur]: ((...args: any) => {
                return dispatch(actionCreators[cur](...args));
            })
        }
    }, {});
}

