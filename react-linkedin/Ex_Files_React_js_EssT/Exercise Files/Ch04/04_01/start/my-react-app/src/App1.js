import logo from './logo.svg';
import './App.css';
import { useRef } from 'react';

function App() {

  const colorName = useRef();
  const colorHex = useRef();
  const submit = e => {
    e.preventDefault();
    const cn = colorName.current.value;
    const cc = colorHex.current.value;

    console.log({ cn, cc })
  }
  return (
    <div className="App">
      <header className="App-header" style={{ backgroundColor: "#999" }} >

        <form onSubmit={submit}>
          <input type="text" placeholder='nome' ref={colorName} />
          <input type="color" ref={colorHex} />
          <button name="add">add</button>
        </form>


      </header>
    </div>
  );
}

export default App;
