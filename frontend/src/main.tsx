import ReactDOM from 'react-dom/client';


import './style.css'
import typescriptLogo from './typescript.svg'
import viteLogo from '/vite.svg'
import { setupCounter } from './counter.ts'

const appContent = (<div>
  <a href={"https://vite.dev"} target="_blank">
    <img src={viteLogo} className={"logo"} alt={"Vite logo"} />
  </a>
  <a href="https://www.typescriptlang.org/" target="_blank">
    <img src={typescriptLogo} className="logo vanilla" alt="TypeScript logo" />
  </a>
  <h1>Vite + TypeScript</h1>
  <div className="card">
    <button id="counter" type="button">XXX</button>
  </div>
  <p className="read-the-docs">
    Click on the Vite and TypeScript logos to learn more
  </p>
</div>);

const root = ReactDOM.createRoot(document.getElementById('app')!);
root.render(appContent);

// document.querySelector<HTMLDivElement>('#app')!.innerHTML = `
//   <div>
//     <a href="https://vite.dev" target="_blank">
//       <img src="${viteLogo}" class="logo" alt="Vite logo" />
//     </a>
//     <a href="https://www.typescriptlang.org/" target="_blank">
//       <img src="${typescriptLogo}" class="logo vanilla" alt="TypeScript logo" />
//     </a>
//     <h1>Vite + TypeScript</h1>
//     <div class="card">
//       <button id="counter" type="button"></button>
//     </div>
//     <p class="read-the-docs">
//       Click on the Vite and TypeScript logos to learn more
//     </p>
//   </div>
// `

setupCounter(document.querySelector<HTMLButtonElement>('#counter')!)
