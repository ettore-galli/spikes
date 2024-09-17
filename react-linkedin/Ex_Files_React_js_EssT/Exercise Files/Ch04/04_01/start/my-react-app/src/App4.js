import './App.css';
import { useState, useEffect } from 'react';

function App() {



  const useVal = (initialValue) => {
    const [val, setVal] = useState(initialValue);
    return [val, e => { setVal(e.target.value) }, (descr, hex) => {
      const upperized = descr.split("#")[0].toUpperCase() + " " + hex;

      return upperized;
    }]
  }

  const [data, setData] = useState({});
  const [colorName, setColorName, transformDescr] = useVal("");
  const [colorHex, setColorHex] = useVal("#8855ee");


  const submit = e => {
    e.preventDefault();
    console.log({ cn: colorName, cc: colorHex })
  }

  const getGithubUrl = (user) => {
    return `https://api.github.com/users/${user}`;
  }

  const fetchGithubUserData = (user, dataConsumer, errorNotifier, loadNotifier) => {
    console.log("fetchGithubUserData")

    loadNotifier(true);
    
    fetch(getGithubUrl(user))
      .then((data) => data.json())
      .then((data) => {
        console.log("DATA", data)
        loadNotifier(false);
        dataConsumer(data);
      })
     .catch(errorNotifier);
  }

  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const buildResponse = (rjson) => <div>
    <span>{rjson.login}</span>
    <span>{rjson.bio}</span>
  </div>;

  const buildLoadResponse = () => <div>
    <span style={{ color: "green" }}>Loading...</span>
  </div>;

  const buildErrorResponse = (error) => <div>
    <span style={{ color: "red" }}>{error}</span>
  </div>;


  useEffect(
    () => {
      fetchGithubUserData(
        "ettore-galli",
        setData,
        setError,
        setLoading
      )
    }, []
  )

  const ApiData = () => {
    if (loading) {
      return buildLoadResponse();
    }
    if (error) {
      return buildErrorResponse(error);
    }
    return buildResponse(data)

  }

  return (
    <div className="App">
      <header className="App-header">
        <h1>REACT</h1>
      </header>
      <section className="App-body">
        <div className="App-data">
          <ApiData />
        </div>
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


      </section>

    </div>
  );
}

export default App;
