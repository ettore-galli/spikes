import { testData } from "./example-2-test-data";

export interface Item {
    key: string;
    name: string;
    phone: string;
}

export const getTableData = () => {
    return new Promise<Item[]>(
        (resolve, _) => {
            setTimeout(() => resolve(testData), 1000);
        }
    );
}