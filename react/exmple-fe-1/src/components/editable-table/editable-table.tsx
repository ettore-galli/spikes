import React, { useState, useEffect } from 'react';

import { Button } from 'antd';

import EditableTableComponent, { TableRowItem } from './parts/editable-table-component';
import { OperationResult } from '../common/common';


interface EditableTableProps {
    columns: { [field: string]: any }[]
    loadDataCallback: () => Promise<TableRowItem[]>
    saveDataCallback: ((data: TableRowItem[]) => Promise<OperationResult>)
}

const initialData: TableRowItem[] = [];

const EditableTable: React.FC<EditableTableProps> = (props: EditableTableProps) => {

    const [data, setData] = useState(initialData);
    const [reloadData, setReloadData]: [boolean, ((reloadData: boolean) => void)] = useState(true);

    useEffect(
        () => {
            if (reloadData) {
                props.loadDataCallback().then(
                    (data) => {
                        setData(data)
                        setReloadData(false)
                    }
                )
            }
        }
    )

    const setDataCallback = (data: TableRowItem[]): OperationResult => {
        setData(data)
        return { success: true, message: "OK" }
    }

    const onSaveCommand = () => {
        props.saveDataCallback(data)
        setReloadData(true)
    }

    const onCancelCommand = () => {
        setReloadData(true)
    }

    return (
        <div>
            <EditableTableComponent
                columns={props.columns}
                setDataCallback={setDataCallback}
                data={data}
            />
            <Button type="primary" onClick={onSaveCommand}>Save</Button>
            <Button type="primary" onClick={onCancelCommand}>Cancel</Button>
        </div>
    );
};

export default EditableTable;