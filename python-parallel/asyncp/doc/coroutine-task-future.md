# Coroutine, Task e Future

In python async quali sono le differenze e i tipici casi d'uso di Coroutine, Task e Future?

---

In Python's `asyncio`, **Coroutine**, **Task**, e **Future** sono concetti fondamentali per la programmazione asincrona, ma hanno ruoli distinti. Ecco una spiegazione chiara delle differenze e dei casi d'uso tipici:

---

### 1. **Coroutine**

- **Cos'è**:  
  Una funzione definita con `async def` che può essere sospesa (`await`) durante l'esecuzione. Non viene eseguita automaticamente: devi esplicitamente "guidarla" con un event loop.  

  ```python
  async def my_coroutine():
      await asyncio.sleep(1)
      return "Done"
  ```

- **Casi d'uso**:  
  - Definire operazioni asincrone (es. chiamate HTTP, I/O su file, query a database).  
  - Spezzare operazioni lunghe in passaggi sospendibili (`await`).  

- **Attenzione**:  
  Una coroutine **non è eseguita** finché non viene "awaitata" o trasformata in un `Task`.

---

### 2. **Future**

- **Cos'è**:  
  Un **contenitore** per un risultato che sarà disponibile in futuro. È un oggetto di basso livello usato internamente da `asyncio` per rappresentare operazioni asincrone.  

  ```python
  future = asyncio.Future()
  future.set_result("Done")  # Imposta manualmente un risultato
  ```

- **Casi d'uso**:  
  - Interfaccia per callback-based code (es. integrare librerie non-async).  
  - Costruire meccanismi personalizzati (es. adattatori per socket o event loop esterni).  

- **Attenzione**:  
  Di solito non si usano direttamente, ma tramite `Task` o `asyncio` high-level API.

---

### 3. **Task**

- **Cos'è**:  
  Una **sottoclasse di `Future`** che avvia e gestisce l'esecuzione di una coroutine nell'event loop.  

  ```python
  task = asyncio.create_task(my_coroutine())  # Avvia la coroutine in background
  ```

- **Casi d'uso**:  
  - Eseguire coroutine **in concorrenza** (es. fare più richieste HTTP parallele).  
  - Monitorare o cancellare operazioni avviate (`task.cancel()`).  

- **Attenzione**:  
  Un `Task` è creato con `asyncio.create_task()` o `loop.create_task()` e viene schedulato immediatamente.

---

### **Differenze Chiave**

| Concetto      | Descrizione | Quando si usa |  
|--------------|------------|--------------|  
| **Coroutine** | Funzione async (`async def`) | Operazioni asincrone singole (es. `await func()`). |  
| **Task**     | Coroutine in esecuzione nell'event loop | Parallelismo (es. `gather()`, `create_task()`). |  
| **Future**   | Promessa di un risultato futuro | Low-level (di solito gestito da `asyncio`). |  

---

### **Esempio Pratico**

```python
import asyncio

async def fetch_data():
    print("Fetching data...")
    await asyncio.sleep(2)
    return "Data"

async def main():
    # Coroutine (non parte finché non awaitata)
    coro = fetch_data()  

    # Task (parte immediatamente in background)
    task = asyncio.create_task(fetch_data())  

    # Future (usato internamente da asyncio)
    future = asyncio.Future()
    future.set_result("Manual Future")

    print(await coro)  # "Data" dopo 2 secondi
    print(await task)  # "Data" dopo 2 secondi (in parallelo se ci sono più task)
    print(await future)  # "Manual Future" immediato

asyncio.run(main())
```

---

### **Riassunto**

- **Coroutine**: Definisci *cosa* fare in modo asincrono.  
- **Task**: Esegui coroutine *in parallelo*.  
- **Future**: Meccanismo low-level per *risultati futuri* (usato da `Task`).  

Se vuoi approfondire un aspetto specifico, chiedimi pure! 🚀
