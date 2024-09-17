import './App.css';


import Home from './pages/Home';
import About from './pages/About';
import Contact from './pages/Contact';

import { BrowserRouter, Routes, Route, Link } from 'react-router-dom';

function App() {
  return <div>
    <BrowserRouter>
      <header><h1>App</h1></header>
      <hr />
      <nav>
        <Link to="/">Home</Link>
        <Link to="/about">About</Link>
        <Link to="/contact">Contact</Link>
      </nav>
      <hr />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<About />} />
        <Route path="/contact" element={<Contact />} />
      </Routes>
      <hr />
      <footer><small>Copyright {new Date().getFullYear()}</small></footer>
    </BrowserRouter>
  </div>
}

export default App;
