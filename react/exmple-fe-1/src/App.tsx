import React from 'react';
import 'antd/dist/antd.min.css';
import './App.css';

import { BrowserRouter, Routes, Route } from "react-router-dom";

import Example1Page from './components/example-1-page/example-1-page';
import Example2Page from './components/example-2-page/example-2-page';

function App() {
  return (
    <div className='App'>
      <Example1Page />

      <BrowserRouter>
      <Routes>
        <Route path="/" >
          <Route path="example-1" element={<Example1Page />} />
          <Route path="example-2" element={<Example2Page />} />
        </Route>
      </Routes>
    </BrowserRouter>
    </div>
  )
}

export default App;
