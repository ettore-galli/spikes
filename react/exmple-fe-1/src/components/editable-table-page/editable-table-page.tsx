
import React from 'react';
import EditableTable from '../editable-table/editable-table';

const EditableTablePage: React.FC = () => {

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

    return (
        <>
            <div><h1>Editable Table</h1></div>
            <div><EditableTable columns={columns} /></div>
        </>
    );
};

export default EditableTablePage;