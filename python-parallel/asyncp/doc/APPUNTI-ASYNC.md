# APPUNTI ASYNC

## Link

<https://docs.python.org/3/library/asyncio.html>

## Concetti AI

In python qual è la differenza a livello di sistema/implementazione tra il multithreading e asyncio? in particolare nel multithreading come avvine ela distribuzione del lavoro tra un thread e l'altro?

In Python, **multithreading** e **asyncio** sono due approcci diversi per gestire operazioni concorrenti, con differenze significative a livello di implementazione e comportamento del sistema.

---

## **1. Differenze principali tra Multithreading e Asyncio**

### **Multithreading**

- **Implementazione**: Utilizza thread del sistema operativo (gestiti dal kernel).
- **GIL (Global Interpreter Lock)**: In Python, il GIL permette solo un thread alla volta di eseguire bytecode Python, anche su CPU multicore. Questo limita il parallelismo per codice CPU-bound.
- **I/O-bound tasks**: Utile per operazioni I/O-bound (es. richieste di rete, lettura/scrittura su disco), perché i thread possono rilasciare il GIL mentre aspettano.
- **Overhead**: Ogni thread ha un overhead di memoria e tempo di creazione non trascurabile.
- **Preemption**: Il sistema operativo gestisce lo scheduling dei thread, interrompendoli e riprendendoli in modo non deterministico.

### **Asyncio**

- **Implementazione**: Basato su **event loop** a singolo thread, con cooperative multitasking.
- **No GIL limitation**: Non essendo basato su thread, non è limitato dal GIL (ma gira su un singolo thread).
- **I/O-bound tasks**: Ideale per I/O ad alta concorrenza (es. migliaia di connessioni di rete), perché le coroutine cedono il controllo esplicitamente (`await`).
- **Basso overhead**: Le coroutine sono molto più leggere dei thread.
- **No preemption**: Le coroutine devono cedere volontariamente il controllo (`await`), altrimenti bloccano l'event loop.

---

## **2. Come funziona la distribuzione del lavoro nel Multithreading?**

In Python, il multithreading è gestito dal sistema operativo, non dall'interprete Python. Ecco come avviene la distribuzione del lavoro:

1. **Thread Scheduling**:
   - Lo **scheduler del sistema operativo** decide quando un thread viene eseguito, sospeso o ripreso.
   - Non c'è garanzia sull'ordine di esecuzione (non deterministico).
   - Su CPU multicore, i thread possono essere eseguiti in parallelo, ma il GIL limita l'esecuzione concorrente del codice Python.

2. **Context Switching**:
   - Quando un thread esegue un'operazione I/O (es. una richiesta HTTP), rilascia il GIL e va in attesa.
   - Un altro thread può acquisire il GIL ed eseguire codice Python.
   - Questo permette una pseudo-concorrenza in scenari I/O-bound.

3. **Problemi comuni**:
   - **Race condition**: Se più thread accedono a risorse condivise senza lock.
   - **Starvation**: Alcuni thread potrebbero non ottenere abbastanza tempo di esecuzione.
   - **GIL contention**: Troppi thread possono causare overhead a causa del GIL.

---

## **3. Esempio Pratico**

### **Multithreading (con `threading`)**

```python
import threading
import time

def task(name):
    print(f"Thread {name} started")
    time.sleep(2)  # Simula I/O
    print(f"Thread {name} finished")

threads = []
for i in range(3):
    t = threading.Thread(target=task, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
```

- I thread vengono gestiti dal sistema operativo.
- L'ordine di esecuzione non è garantito.

### **Asyncio**

```python
import asyncio

async def task(name):
    print(f"Coroutine {name} started")
    await asyncio.sleep(2)  # Simula I/O
    print(f"Coroutine {name} finished")

async def main():
    await asyncio.gather(task(1), task(2), task(3))

asyncio.run(main())
```

- Tutto gira in un singolo thread.
- Le coroutine cedono il controllo solo su `await`.

---

## **4. Quando usare uno o l'altro?**

| **Criterio**       | **Multithreading** | **Asyncio** |
|---------------------|-------------------|-------------|
| **I/O-bound**       | ✅ Sì (ma con overhead) | ✅ Ideale (basso overhead) |
| **CPU-bound**       | ❌ No (GIL) | ❌ No (single-thread) |
| **Controllo fine**  | ❌ Gestito dall'OS | ✅ Sì (cooperative) |
| **Scalabilità**     | ❌ Limitata (overhead thread) | ✅ Alta (migliaia di coroutine) |

- **Usa `multithreading`** se hai operazioni I/O bloccanti e vuoi un approccio semplice.
- **Usa `asyncio`** se hai molto I/O ad alta concorrenza (es. server web, scraper).
- **Per CPU-bound**, usa `multiprocessing` per aggirare il GIL.

Spero che questa spiegazione ti sia utile! Se hai dubbi, chiedimi pure. 🚀
