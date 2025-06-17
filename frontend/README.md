# Frontend Boilerplate (Vite + TypeScript + JSX senza React + Jest)

## Avvio sviluppo

```sh
npm run dev
```
Avvia il server di sviluppo con hot reload.

## Build artefatto per deploy

```sh
npm run build
```
Il risultato sarà nella cartella `dist/`.

## Esecuzione test unitari

```sh
npm test
```
Esegue i test con Jest.

## Note
- La sintassi JSX è abilitata senza React (vedi configurazione `tsconfig.json` e `vite.config.ts`).
- I test sono scritti in TypeScript e gestiti tramite Jest.
- Per modificare la sintassi JSX, vedi la sezione "jsx" in `tsconfig.json` e la configurazione Vite.
