import logo from './logo.svg';
import './App.css';
import { useEffect, useState } from 'react';

function App() {

  const [light, setLight] = useState(0);

  const backgrounds = ["#000", "#888", "#fff"];

  function setDark() {
    setLight(0);
  }

  function setDim() {
    setLight(1);
  }

  function setBright() {
    setLight(2);
  }

  const [size, setSize] = useState("small");
  const sizes = { "small": 100, "medium": 200, "large": 300 };

  useEffect(() => {
    console.log(`LIGHT: ${light}`)
  }, [light])

  useEffect(() => {
    console.log(`SIZE: ${size}`)
  }, [size])

  useEffect(() => {
    console.log(`L/S: ${light} / ${size}`)
  }, [size, light])

  return (
    <div className="App">
      <header className="App-header" style={{ backgroundColor: backgrounds[light] }} >
        <img src={logo} className="App-logo" alt="logo" width={sizes[size]} />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>

        <button name="dark" onClick={setDark}>Dark</button>
        <button name="dim" onClick={setDim}>Dim</button>
        <button name="bright" onClick={setBright}>Bright</button>
        <br />
        <button name="small" onClick={() => setSize("small")}>Small</button>
        <button name="medium" onClick={() => setSize("medium")}>Medium</button>
        <button name="big" onClick={() => setSize("large")}>Large</button>

        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React2222
        </a>
      </header>
    </div>
  );
}

export default App;
