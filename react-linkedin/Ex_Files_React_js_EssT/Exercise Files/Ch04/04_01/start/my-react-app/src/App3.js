import './App.css';
import { useState } from 'react';

function App() {



  const useVal = (initialValue) => {
    const [val, setVal] = useState(initialValue);
    return [val, e => { setVal(e.target.value) }, (descr, hex) => {
      const upperized = descr.split("#")[0].toUpperCase() + " " + hex;

      return upperized;
    }]
  }


  const [colorName, setColorName, transformDescr] = useVal("");
  const [colorHex, setColorHex] = useVal("#8855ee");


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
            onChange={setColorName}
            placeholder='nome' />

          <input
            type="color"
            onChange={setColorHex}
            value={colorHex}
          />

          <p>{transformDescr(colorName, colorHex)}</p>

          <button name="add">add</button>
        </form>


      </header>
    </div>
  );
}

export default App;
