
import React, { useState, useEffect } from 'react';
import EditableTable, { TableRowItem, RowSaveResult } from '../editable-table/editable-table';
import { Item } from './example-1-data-provider';

import { getTableData } from './example-1-data-provider';

const initialData: Item[] = [];

const Example1Page: React.FC = () => {

    const [data, setData] = useState(initialData);

    const columns: { [field: string]: any }[] = [
        {
            title: 'Name',
            dataIndex: 'name',
            width: '25%',
            editable: true,
            inputType: 'text'
        },
        {
            title: 'Age',
            dataIndex: 'age',
            width: '15%',
            editable: true,
            inputType: 'number'
        },
        {
            title: 'Address',
            dataIndex: 'address',
            width: '40%',
            editable: true,
            inputType: 'text'
        },
    ];

    useEffect(
        () => {
            getTableData().then(
                (data) => {
                    setData(data)
                }
            )
        }
    )

    const setDataCallback = (data: TableRowItem[]): RowSaveResult => {
        console.log("Saving data...")
        return { success: true, message: "OK" }
    }

    return (
        <>
            <div><h1>Editable Table</h1></div>
            <div><EditableTable columns={columns} setDataCallback={setDataCallback} data={data} /></div>
        </>
    );
};

export default Example1Page;