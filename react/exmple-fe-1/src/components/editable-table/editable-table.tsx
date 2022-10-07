
import { Form, Input, InputNumber, Popconfirm, Table, Typography } from 'antd';
import React, { useEffect, useState } from 'react';

import { getTableData } from './data-provider';

interface TableRowItem {
    key: string
    [field: string]: any
}


interface EditableCellProps extends React.HTMLAttributes<HTMLElement> {
    editing: boolean;
    dataIndex: string;
    title: any;
    inputType: 'number' | 'text';
    record: TableRowItem;
    index: number;
    children: React.ReactNode;
}

const EditableCell: React.FC<EditableCellProps> = ({
    editing,
    dataIndex,
    title,
    inputType,
    record,
    index,
    children,
    ...restProps
}) => {

    const inputNode = inputType === 'number' ? <InputNumber /> : <Input />;

    return (
        <td {...restProps}>
            {editing ? (
                <Form.Item
                    name={dataIndex}
                    style={{ margin: 0 }}
                    rules={[
                        {
                            required: true,
                            message: `Please Input ${title}!`,
                        },
                    ]}
                >
                    {inputNode}
                </Form.Item>
            ) : (
                children
            )}
        </td>
    );
};


interface EditableTableProps {
    columns: { [field: string]: any }[]
}

const EditableTable: React.FC<EditableTableProps> = (props: EditableTableProps) => {

    const initialData: TableRowItem[] = [];
    const [form] = Form.useForm();
    const [data, setData] = useState(initialData);
    const [editingKey, setEditingKey] = useState('');

    useEffect(
        () => {
            console.log("Try load data")
            getTableData().then(
                (data: TableRowItem[]) => {
                    console.log(data);
                    setData(data)
                }
            )
        }
    )

    const isEditing = (record: TableRowItem) => record.key === editingKey;

    const blankEditingRecord = props.columns.reduce((prv, cur) => ({ ...prv, [cur.dataIndex]: '' }), {});

    const edit = (record: Partial<TableRowItem> & { key: React.Key }) => {
        form.setFieldsValue({ ...blankEditingRecord, ...record });
        setEditingKey(record.key);
    };

    const cancel = () => {
        setEditingKey('');
    };

    const save = async (key: React.Key) => {
        try {
            const row = (await form.validateFields()) as TableRowItem;
            const newData = [...data];
            const index = newData.findIndex(item => key === item.key);
            if (index > -1) {
                const item = newData[index];
                newData.splice(index, 1, {
                    ...item,
                    ...row,
                });
                setData(newData);
                setEditingKey('');
            } else {
                newData.push(row);
                setData(newData);
                setEditingKey('');
            }
        } catch (errInfo) {
            console.log('Validate Failed:', errInfo);
        }
    };


    const operationColumn = [
        {
            title: 'operation',
            dataIndex: 'operation',
            render: (_: any, record: TableRowItem) => {
                const editable = isEditing(record);
                return editable ? (
                    <span>
                        <Typography.Link onClick={() => save(record.key)} style={{ marginRight: 8 }}>
                            Save
                        </Typography.Link>
                        <Popconfirm title="Sure to cancel?" onConfirm={cancel}>
                            <a>Cancel</a>
                        </Popconfirm>
                    </span>
                ) : (
                    <Typography.Link disabled={editingKey !== ''} onClick={() => edit(record)}>
                        Edit
                    </Typography.Link>
                );
            },
        },
    ];

    const columns = [...props.columns, ...operationColumn];

    const mergedColumns = columns.map(col => {
        if (!col.editable) {
            return col;
        }
        return {
            ...col,
            onCell: (record: TableRowItem) => ({
                record,
                inputType: col.inputType,
                dataIndex: col.dataIndex,
                title: col.title,
                editing: isEditing(record),
            }),
        };
    });

    return (
        <Form form={form} component={false}>
            <Table
                components={{
                    body: {
                        cell: EditableCell,
                    },
                }}
                bordered
                dataSource={data}
                columns={mergedColumns}
                rowClassName="editable-row"
                pagination={{
                    onChange: cancel,
                }}
            />
        </Form>
    );
};

export default EditableTable;