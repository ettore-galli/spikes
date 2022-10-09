import { OperationResult } from "../common/common";

export interface Item {
    key: string;
    name: string;
    age: number;
    address: string;
}

const SERVER = "http://localhost:8000"


export const getTableData = (): Promise<Item[]> => {
    const get_url = `${SERVER}/items`;
    return fetch(get_url).then((response) => response.json()).then((response) => response.map((record: any) => ({ key: record.id, name: record.name, age: record.age, address: record.address })));
}

export const saveTableData = (data: Item[]): Promise<OperationResult> => {
    const url = `${SERVER}/items/bulk`;

    const postData = data.map((record: any) => ({ id: record.key, name: record.name, age: record.age, address: record.address }));

    return fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        },
        body: JSON.stringify(postData)
    }).then(() => ({ success: true, message: "OK" }));

}

