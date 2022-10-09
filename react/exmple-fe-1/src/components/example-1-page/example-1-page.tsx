import React from 'react';
import { OperationResult } from '../common/common';
import EditableTable, { TableRowItem } from '../editable-table';

import { getTableData, saveTableData } from './example-1-data-provider';

const Example1Page: React.FC = () => {

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

    const save = (data: TableRowItem[]): Promise<OperationResult> => {
        return saveTableData(data.map(item => ({ key: item.key, name: item.name, age: item.age, address: item.address })));
    }

    return (
        <>
            <div><h1>Editable Table esempio 1</h1></div>
            <div><EditableTable
                columns={columns}
                loadDataCallback={getTableData}
                saveDataCallback={save}
            /></div>
        </>
    );
};

export default Example1Page;