import React from 'react';

import { OperationResult } from '../common/common';

import EditableTable, { TableRowItem } from '../editable-table';

import { getTableData } from './example-2-data-provider';

const Example2Page: React.FC = () => {

    const columns: { [field: string]: any }[] = [
        {
            title: 'Name',
            dataIndex: 'name',
            width: '60%',
            editable: true,
            inputType: 'text'
        },
        {
            title: 'Phone',
            dataIndex: 'phone',
            width: '40%',
            editable: true,
            inputType: 'text'
        },
    ];

    const saveTableData = (_: TableRowItem[]): Promise<OperationResult> => {
        return new Promise(
            (resolve, _) => { resolve({ success: true, message: "" }) }
        )
    }

    return (
        <>
            <div><h1>Editable Table Esempio 2</h1></div>
            <div><EditableTable
                columns={columns}
                loadDataCallback={getTableData}
                saveDataCallback={saveTableData}
            /></div>
        </>
    );
};

export default Example2Page;