
import { Form, Input, InputNumber, Popconfirm, Table, Typography } from 'antd';
import React, { useState } from 'react';


const NO_EDITING_KEY = '';

interface EditableTableComponentProps {
    columns: { [field: string]: any }[]
    setDataCallback: ((data: TableRowItem[]) => RowSaveResult)
    data: TableRowItem[]
}

export interface RowSaveResult {
    success: boolean
    message: string
}

export interface TableRowItem {
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

const EditableTableComponent: React.FC<EditableTableComponentProps> = (props: EditableTableComponentProps) => {

    const [form] = Form.useForm();
    const [editingKey, setEditingKey] = useState(NO_EDITING_KEY);

    const blankEditingRecord = props.columns.reduce((prv, cur) => ({ ...prv, [cur.dataIndex]: '' }), {});

    const isEditing = (record: TableRowItem) => record.key === editingKey;

    const edit = (record: Partial<TableRowItem> & { key: React.Key }) => {
        form.setFieldsValue({ ...blankEditingRecord, ...record });
        setEditingKey(record.key);
    };

    const cancel = () => {
        setEditingKey(NO_EDITING_KEY);
    };

    const save = async (key: React.Key) => {
        try {

            const row = (await form.validateFields()) as TableRowItem;
            const newData = [...props.data];
            const index = newData.findIndex(item => key === item.key);

            if (index > -1) {
                const item = newData[index];
                newData.splice(index, 1, {
                    ...item,
                    ...row,
                });
                console.log("New data post edit: ", row)
                !!props.setDataCallback && props.setDataCallback(newData);
                setEditingKey(NO_EDITING_KEY);
            } else {
                newData.push(row);
                !!props.setDataCallback && props.setDataCallback(newData);
                setEditingKey(NO_EDITING_KEY);
            }
        } catch (errInfo) {
            console.log('Validate Failed:', errInfo);
        }
    };

    const operationColumn = [
        {
            title: '',
            dataIndex: '',
            render: (_: any, record: TableRowItem) => {
                const editable = isEditing(record);
                return editable ? (
                    <span>
                        <Typography.Link onClick={() => save(record.key)} style={{ marginRight: 8 }}>
                            Save
                        </Typography.Link>
                        <Popconfirm title="Sure to cancel?" onConfirm={cancel}>
                            <a href="/#">Cancel</a>
                        </Popconfirm>
                    </span>
                ) : (
                    <Typography.Link disabled={editingKey !== NO_EDITING_KEY} onClick={() => edit(record)}>
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
                dataSource={props.data}
                columns={mergedColumns}
                rowClassName="editable-row"
                pagination={{
                    onChange: cancel,
                }}
            />
        </Form>
    );
};

export default EditableTableComponent;