
import React, { useRef, useState } from 'react';
import EditableTable from '../editable-table/editable-table';

const EditableTablePage: React.FC = () => {

    return (
        <>
            <div><h1>Editable Table</h1></div>
            <div><EditableTable /></div>
        </>
    );
};

export default EditableTablePage;