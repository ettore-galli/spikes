
# LISP SETUP

## Configurazione dell'Ambiente di Sviluppo Common Lisp

Ecco come puoi impostare il tuo ambiente:

### 1\. Immagine Docker per Common Lisp

Per un ambiente minimale, useremo un'immagine Docker che include un'implementazione Common Lisp come **SBCL (Steel Bank Common Lisp)**, che è molto popolare e performante.

#### Dockerfile

Crea un file chiamato `Dockerfile` (senza estensione) nella tua directory di progetto con il seguente contenuto:

```dockerfile
# Usa un'immagine base Ubuntu leggera
FROM ubuntu:22.04

# Aggiorna i pacchetti e installa SBCL e Git (utile per clonare progetti in futuro)
RUN apt-get update && \
    apt-get install -y sbcl git && \
    rm -rf /var/lib/apt/lists/*

# Imposta SBCL come comando predefinito quando il container viene avviato senza argomenti
CMD ["sbcl"]
```

**Spiegazione:**

* `FROM ubuntu:22.04`: Inizia da un'immagine Ubuntu 22.04, una base solida e relativamente leggera.
* `RUN apt-get update && apt-get install -y sbcl git && rm -rf /var/lib/apt/lists/*`: Questo comando aggiorna l'elenco dei pacchetti, installa **SBCL** (l'interprete Common Lisp) e **Git** (per il controllo versione, utile per scaricare librerie in futuro) e poi pulisce la cache dei pacchetti per ridurre la dimensione dell'immagine.
* `CMD ["sbcl"]`: Imposta `sbcl` come comando predefinito. Quando avvii il container senza specificare un comando, si avvierà direttamente la REPL (Read-Eval-Print Loop) di SBCL.

#### Costruire e Avviare il Container

1. **Naviga** nella directory dove hai salvato il `Dockerfile`.

2. **Costruisci l'immagine** (solo la prima volta o quando modifichi il Dockerfile):

    ```bash
    docker build -t common-lisp-env .
    ```

    Questo comando costruisce un'immagine Docker e la tagga con il nome `common-lisp-env`. Il `.` alla fine indica che il Dockerfile si trova nella directory corrente.

3. **Avvia il container** e accedi alla REPL di SBCL:

    ```bash
    docker run -it common-lisp-env
    docker run -p 4005:4005 -it common-lisp-env
    ```

      * `-it` ti permette di interagire con il container (modalità interattiva e pseudo-TTY).

Ora dovresti trovarti nella REPL di SBCL, pronta per eseguire codice Lisp:

```lisp
* (+ 1 2)
3
* (print "Ciao Common Lisp!")
"Ciao Common Lisp!"
"Ciao Common Lisp!"
*
```

-----

### 2\. Plugin VS Code per Common Lisp

nc -zv 127.0.0.1 4005

ALive
```json
{
    // Host del server SLIME/SWANK
    "alive.lsp.remote.host": "127.0.0.1",

    // Porta del server SLIME/SWANK
    "alive.lsp.remote.port": 4005,

    // Usa solo la connessione remota, non locale
    "alive.lsp.remote.enabled": true,

    // Non serve comando di avvio, il server è già attivo
    "alive.lsp.startCommand": [],

    // (Opzionale) Timeout per la connessione
    "alive.lsp.remote.timeout": 10000
}
```

Per un'esperienza di sviluppo ottimale in VS Code, il plugin più consigliato e funzionale è **Common Lisp (LispWorks)**, che integra il supporto per **SLIME (Superior Lisp Interaction Mode for Emacs)** o **Sly (una sua evoluzione)**.

1. **Apri VS Code.**
2. Vai alla sezione **Estensioni** (Ctrl+Shift+X o Cmd+Shift+X).
3. Cerca "Common Lisp" e installa l'estensione **"Common Lisp (LispWorks)"** di LispWorks Ltd.

**Configurazione minima in VS Code:**

Dopo aver installato l'estensione, avrai bisogno di dirgli come connettersi al tuo server Lisp (che sarà in esecuzione nel container Docker).

Nel tuo workspace di VS Code, crea una directory `.vscode` e all'interno un file `settings.json` con il seguente contenuto:

```json
{
    "lisp.connections": [
        {
            "name": "Docker SBCL",
            "host": "localhost",
            "port": 4005, // Questa è la porta predefinita per SLIME, la mapperemo da Docker
            "remoteDir": "/app", // Directory remota dove si troverà il tuo codice nel container
            "initCommands": [
                "(ql:quickload :swank)" // Carica Swank, il server di connessione per SLIME/Sly
            ]
        }
    ],
    "lisp.enableREPL": true,
    "lisp.enableLiveEval": true
}
```

-----

### 3\. Workflow di Sviluppo Minimo

Ecco il flusso di lavoro di base:

1. **Avvia il tuo Container Docker con Mappatura Porte e Volumi:**

    Per permettere a VS Code di connettersi al server Lisp nel container e di sincronizzare il codice, devi mappare una porta e un volume.

    Apri il tuo terminale e nella directory del tuo progetto esegui:

    ```bash
    docker run -it -p 4005:4005 -v "$(pwd):/app" --name lisp-dev common-lisp-env
    ```

      * `-p 4005:4005`: Mappa la porta 4005 del tuo host alla porta 4005 del container. È su questa porta che il server SLIME/Sly si metterà in ascolto.
      * `-v "$(pwd):/app"`: Mappa la directory corrente del tuo computer (`$(pwd)` su Linux/macOS, `%cd%` su Windows PowerShell) alla directory `/app` all'interno del container. Questo ti permette di modificare i file in VS Code sul tuo computer e di far sì che queste modifiche siano visibili nel container, e viceversa.
      * `--name lisp-dev`: Assegna un nome al container, utile per fermarlo o riavviarlo facilmente.

    Una volta avviato il container, nella sua REPL, dovrai caricare il server Swank/Sly. Poiché lo abbiamo messo in `initCommands` nel `settings.json` di VS Code, l'estensione dovrebbe tentare di farlo automaticamente quando si connette. Tuttavia, se vuoi farlo manualmente, puoi digitare:

    ```lisp
    * (ql:quickload :swank)
    * (swank:create-server :port 4005 :dont-close t)
    ```

    *Nota*: `ql:quickload` presuppone che Quicklisp sia installato. Se la tua immagine base non lo include, dovrai installarlo. Per questo setup minimale, ci affidiamo al fatto che il plugin VS Code lo gestirà al meglio o che potresti aggiungerlo al Dockerfile in seguito se necessario.

2. **Connetti VS Code al Container Lisp:**

      * In VS Code, apri un file `.lisp` (ad esempio, `main.lisp` nella tua directory di progetto).
      * L'estensione Common Lisp dovrebbe rilevare la configurazione in `settings.json`.
      * Premi `Ctrl+Alt+C` `Ctrl+Alt+C` (o `Cmd+Alt+C` `Cmd+Alt+C` su Mac) per connetterti alla REPL. Se tutto è configurato correttamente, vedrai una REPL integrata apparire nel terminale di VS Code.

3. **Scrivere e Valutare Codice:**

      * Scrivi il tuo codice Lisp nel file `.lisp`.
      * **Per valutare un'espressione:** posiziona il cursore sull'espressione e premi `Ctrl+X Ctrl+E` (o `Cmd+X Cmd+E`). Il risultato apparirà nella REPL.
      * **Per caricare l'intero file:** `Ctrl+C Ctrl+K` (o `Cmd+C Cmd+K`).
      * Interagisci direttamente con la REPL di Lisp integrata per testare le funzioni o esplorare.

-----

### Prossimi Passi per l'Espansione Futura

Questo setup ti darà una base solida. Ecco alcune idee per espanderlo in futuro:

* **Quicklisp:** Un gestore di librerie per Common Lisp. Puoi aggiungerlo al tuo `Dockerfile` per installarlo automaticamente. È quasi indispensabile per progetti reali.
* **Struttura del Progetto:** Impara a organizzare i tuoi progetti Lisp usando **ASDF (Another System Definition Facility)**, il sistema di build standard de facto.
* **Debugging:** Esplora le funzionalità di debugging offerte da SLIME/Sly tramite il plugin VS Code.
* **Altri Editor:** Se decidi di passare a Emacs, SLIME è nativo di Emacs e offre un'esperienza di sviluppo Common Lisp molto ricca.

Questo ambiente minimalista ti permetterà di concentrarti sull'apprendimento di Common Lisp senza dover affrontare complessità di configurazione iniziali. Divertiti a programmare in Lisp\!

Hai altre domande su come affinare questo setup o su come iniziare con Common Lisp?
