import { testData } from "./test-data";
import { Item } from './common';

export const getTableData = () => {
    return new Promise<Item[]>(
        (resolve, _) => {
            setTimeout(() => resolve(testData), 1000);
        }
    );
}