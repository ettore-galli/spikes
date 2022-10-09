import { testData } from "./example-1-test-data";

export interface Item {
    key: string;
    name: string;
    age: number;
    address: string;
}

const SERVER="localhost:8000"

// export const getTableData = (): Promise<Item[]> => {
//     return new Promise<Item[]>(
//         (resolve, _) => {
//             setTimeout(() => resolve(testData), 1000);
//         }
//     );
// }


export const getTableData = (): Promise<Item[]> => {
    return new Promise<Item[]>(
        (resolve, _) => {
            setTimeout(() => resolve(testData), 1000);
        }
    );
}

// const saveTableData = (_: Item[]): Promise<OperationResult> => {
//     return new Promise(
//         (resolve, _) => { resolve({ success: true, message: "" }) }
//     )
// }

