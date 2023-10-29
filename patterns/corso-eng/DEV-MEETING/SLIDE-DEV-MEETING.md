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

## Introduzione

* Soluzioni a problemi comuni e ricorrenti
* Frutto di esperienza e processo induttivo
* Standardizzazione
* Generalità / astrazione
* Primo anno citato di atoria: 1977 (-> induzione + esperienza)

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

## Factory / struttura

Si vuole creare un'interfaccia per la creazione di oggetti
in una superclasse, ma permettere alle sottoclassi di
alterare il tipo di oggetti creati

<style scoped>
img {
    display: block;
    margin: 0 auto;
}
</style>

![height:350px](./images/factory-struttura.png)

---

## Factory / esempio

Un convertitore di gradi Celsius Fahrenheit può prendere
l'input o da file, o da terminale

Si vuole razionalizzare l'istanziazione della classe che preleva l'input

