import React from 'react';
import logo from './logo.svg';
import './App.css';

const App: React.FC = () => {
  const aaa: string = "cicci";
  const bbb: number = 3.14159;
  const ccc: number[] = [2.71828, 3.14159];
  const tupla: [number, string] = [2.71828, "3.14159"];

  interface ValueDisplayer {
    value: number | string | object
  }

  const Valore: React.FC<ValueDisplayer> = ({ value }) => {
    return <div>
      <hr />
      <p>Valore: {JSON.stringify(value)}</p>
      <p>Tipo: {typeof value}</p>
    </div>
  };

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>{typeof Valore}</p>
        <Valore value={aaa} ></Valore>
        <Valore value={bbb} ></Valore>
        <Valore value={ccc} ></Valore>
        <Valore value={tupla} ></Valore>
      </header>
    </div>
  );
}

export default App;
