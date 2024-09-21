import './App.css';
import { useState } from 'react';

function App() {

  const [colorName, setColorName] = useState("");
  const [colorHex, setColorHex] = useState("#8855ee");

  const submit = e => {
    e.preventDefault();


    console.log({ cn: colorName, cc: colorHex })
  }
  
  return (
    <div className="App">
      <header className="App-header" style={{ backgroundColor: "#000000" }} >

        <form onSubmit={submit}>

          <input
            type="text"
            value={colorName}
            onChange={e => setColorName(e.target.value)}
            placeholder='nome' />

          <input
            type="color"
            onChange={e =>setColorHex(e.target.value)}
            value={colorHex}
          />

          <button name="add">add</button>
        </form>


      </header>
    </div>
  );
}

export default App;
