import React from 'react';
import logo from './logo.svg';
import './App.css';

// import 'semantic-ui-css/semantic.min.css'

import HeaderExampleIconProp from './components/header/header'
import ButtonExampleAnimated from './components/button/buttonx'

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <HeaderExampleIconProp ></HeaderExampleIconProp>
        <ButtonExampleAnimated />
      </header>
    </div>
  );
}

export default App;
