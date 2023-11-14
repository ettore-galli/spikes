---
marp: true
style: |
    section, pre {
        background-color: #f0fff0;
    }

    h1, h2, h3, h4, h5, h6{
        text-align: center;
        color: #006600;
    }

    .centrato {
        text-align: center;
    }

    th {
        background-color: #f0fff0;
        color: #006600;
    }

    td {
        background-color: #f0fff0;
        color: #006600;
    }
---

# DESIGN PATTERNS

---

## Corso ENG: DP

* Design patterns GoF
* Cenni ai design principles

---

## Presentazione: Oggi

* Breve illustrazione della struttura del corso
  * Cenni ai design principles
  * Illustrazione di **un** dp esemplificativo

---

## Presentazione: Next step

Da organizzare e definire per incontro/i successivo/i

* Lab interattivo su altri DP da scegliere in
  base a feedback e interesse
* Varie ed eventuali a richiesta

---

## Introduzione

* Soluzioni a problemi comuni e ricorrenti
* Frutto di esperienza e processo induttivo
* Standardizzazione
* Generalità / astrazione
* Primo anno citato di storia: 1977 (-> induzione + esperienza)

---

## Introduzione (continua...)

_Un pattern descrive il nucleo di una soluzione relativa un problema che compare
frequentemente in un dato contesto_

_Il modello della soluzione deve essere strutturato in modo che
“si possa usare tale soluzione un milione di volte, senza mai farlo allo stesso modo”_

Christopher Alexander (architetto)

---

## Macro categorie di pattern

Le principali categorie di pattern sw sono:

* Architetturali (es. client server, MVC)
* Progettuali ("via di mezzo", i "nostri")
* Idiomi (basso livello, legati al linguaggio, es. il Singleton)

---

## Classificazione dei pattern

<style scoped>
table {
    display: table;
    width: 100%;
    font-size: 18px;
}

</style>

| Creazionali            | Strutturali           |Comportamentali         |
| ---                    | ---                   |---                     |
| Factory method         | Adapter               |Interpreter             |
| Abstract Factory       | Bridge                |Template Method         |
| Builder                | Composite             |Chain of Responsability |
| Prototype              | Decorator             |Command                 |
| Singleton              | Facade                |Iterator                |
|                        | Flyweigh              |Mediator                |
|                        | Proxy                 |Memento                 |
|                        |                       |Observer                |
|                        |                       |State                   |
|                        |                       |Strategy                |
|                        |                       |Visitor                 |

---

## Frequenza d'uso dei pattern

<style scoped>
img {
    display: block;
    margin: 0 auto;
}
</style>

![height:500px](./images/frequenza-uso-pattern.png)

---

## Scelta dei pattern presentati

Utilizzati due criteri:

* Popolarità
    In base alla classifica di frequenza d'uso

* Uso effettivo
    Cioè che più probabilmente si implementa nel normale
    nel normale lavoro di tutti i giorni (es. template method)
    a differenza di altri (es. Observer) che più facilmente si
    trovano già implementati in librerie e framework

---

## Gli altri

A richiesta in "Puntate" successive...

---

## Leitmotiv

Nei pattern (creazionali in primis, ma tutti) si notano
due fondamentali linee guida:

* Chiamate polimorfiche di metodi
* Utilizzo degli oggetti attraverso le loro interfacce

---

## Pattern creazionali

* Delega della creazione delgli oggetti
* Disaccoppiamento

---

## Factory / struttura

Si vuole creare un'interfaccia per la creazione di oggetti il
cui tipo non è noto a priori, ma la sua interfaccia lo è.

<style scoped>
img {
    display: block;
    margin: 0 auto;
}
</style>

![height:350px](./images/factory-struttura.png)

---

## Factory / Esempio

Un convertitore di gradi Celsius Fahrenheit può prendere
l'input o da file, o da terminale

Si vuole razionalizzare l'istanziazione della classe che preleva l'input

Utile quando non si conosce a runtime la tipologia di oggetto da creare

---

## Abstract Factory / Struttura

Abstract Factory serve per creare famiglie di
oggetti consistenti tra loro

<style scoped>
img {
    display: block;
    margin: 0 auto;
}
</style>

![height:350px](./images/factory-struttura.png)

---

## Abstract Factory / Esempio

Si vuole costruire gli elementi "grafici" di una
home page multilingue, costituita da un messaggio
di benvenuto ed una bandiera.

Si vuole garantire che il "set" bandiera / messaggio
sia coerente

Si sceglie una "dimensione" che gestirà gli artfetti dello stesso
tipo a lei coerenti.

---

## Builder / Struttura

Lo scopo del builder è incapsulare la costruzione di un oggetto complesso

<style scoped>
img {
    display: block;
    margin: 0 auto;
}
</style>

![height:350px](./images/builder-struttura.png)

---

## Builder / Esempio

Costruire una classe Logger composta di un formatter e di
uno "scrittore" di output.

Secondo il formatter o il tipo do output scelto, si hanno diversi tipi
di logger, che vanno costruiti a step.

---

## Bridge / Struttura

Lo scopo del bridge è disaccoppiare più astrazioni
da più implementazioni concrete.

E' utile quando negli oggetti si individuano più "dimensioni"

---

## Bridge / Esempio

<style scoped>
img {
    display: inline-block;
    margin: 50px;
}
</style>

![w:450](./images/bridge-esempio-1.jpg) ![w:450](./images/bridge-esempio-2.png)

---

## Bridge / Schema standard

<style scoped>
img {
    display: block;
    margin: 0 auto;
}
</style>

![height:350px](./images/bridge-struttura.png)

---

## Bridge / Esempio (continua)

Si vuole realizzare un visualizatore di figure, che può visualizzare
semplici figure in due modalità:

* Figura semplice (una sola)
* Figura ripetuta (tra copie)

Il rendering, inoltre, deve poter avvenire sia un modo grafico che testuale

---

## Chain Of responsibility / Schema

<style scoped>
img {
    display: block;
    margin: 0 auto;
}
</style>

Lo scopo del Chain of Responiibility è quello di
fornire un serie di handler di una stessa richiesta in sequenza,
non sapendo in anticipo quale evaderà la richiesta.

![height:350px](./images/chain-struttura-1.png)

---

## Chain Of responsibility / Struttura

<style scoped>
img {
    display: block;
    margin: 0 auto;
}
</style>

![height:350px](./images/chain-struttura-2.png)

---

## Chain Of responsibility / Esempio

Elevamento a potenza

(demo)

* Per piccoli numeri e esponente intero, si procede per moltiplicazioni ripetute
* Per numeri intermedi si usa usa math.pow
* Per grandi numeri si effettua un arrotondamento intero con l'operatore **
