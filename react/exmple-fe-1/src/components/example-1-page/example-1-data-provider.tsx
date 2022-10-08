import { testData } from "./example- 1-test-data";

export interface Item {
    key: string;
    name: string;
    age: number;
    address: string;
}

export const getTableData = () => {
    return new Promise<Item[]>(
        (resolve, _) => {
            setTimeout(() => resolve(testData), 1000);
        }
    );
}