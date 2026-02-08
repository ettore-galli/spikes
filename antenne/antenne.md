## ANTENNE

Ettore, questa è una domanda splendida — e molto più comune tra gli autodidatti seri di quanto sembri. Hai già le basi giuste (propagazione, impedenza, linee di trasmissione), quindi quello che ti serve non è un corso generico, ma **una roadmap strutturata** che ti porti dal modello fisico dell’antenna alla capacità di calcolare impedenza e resistenza di radiazione di un radiatore filare.

I risultati della ricerca che ho fatto mostrano materiale utile ma sparso:  

Quindi ti costruisco una roadmap coerente che usa questi riferimenti come punti d’appoggio.

### 📘 Roadmap completa per capire davvero le antenne filari

#### 1️⃣ **Partire dal modello elementare: il dipolo corto**

È il “mattone” concettuale di tutte le antenne filari.

Obiettivi:

Risorse:

Concetti chiave:

#### 2️⃣ **Passare al dipolo reale: distribuzione sinusoidale della corrente**

Qui inizi a vedere antenne “vere”, con lunghezza confrontabile con λ.

Obiettivi:

Risorse:

Concetti chiave:

#### 3️⃣ **Impedenza di ingresso: parte reale e parte immaginaria**

Una volta capito come si irradia, serve capire come si alimenta.

Obiettivi:

- parte reale = resistenza di radiazione + perdite ohmiche;
- parte immaginaria = energia immagazzinata (reattanza).

Risorse:

Concetti chiave:

#### 4️⃣ **Antenne verticali (Marconiane) e piano di massa**

Dopo il dipolo, il passo naturale è capire la versione “tagliata a metà”.

Obiettivi:

Concetti chiave:

#### 5️⃣ **Antenne end‑fed e matching**

Ora puoi capire antenne come EFHW, 1/2 onda verticali senza radiali, ecc.

Obiettivi:

Concetti chiave:

#### 6️⃣ **Calcolo pratico: come si ottengono \(R_r\) e \(Z_{in}\)**

A questo punto puoi iniziare a calcolare davvero.

##### 🔹 Resistenza di radiazione

Derivata da:
\[
R_r = \frac{2P_{irr}}{I_0^2}
\]
dove \(P_{irr}\) si ottiene integrando il campo lontano.

##### 🔹 Impedenza di ingresso

\[
Z_{in} = R_r + R_{loss} + jX
\]
dove \(X\) deriva dall’energia immagazzinata nei campi vicino all’antenna.

##### 🔹 Strumenti utili

Certo Ettore — ti riscrivo la sezione **Risorse consigliate** in un formato *copiabile* con link espliciti, mantenendo la stessa struttura a livelli.  
I link che seguono provengono dai risultati della ricerca che ho effettuato.

---

# 📚 Risorse consigliate (con link copiabili)

## **Livello 1 – Fondamentale**

- **Dipolo di Hertz e antenne elementari**  
  (Cerca “dipolo di Hertz pdf” o “antenne filari appunti universitari” — non ci sono link stabili e affidabili da citare)

- **Dispense introduttive ITIS/Universitarie sulle antenne filari**  
  (Anche qui i link variano molto; meglio cercare “dispense antenne filari pdf”)

---

## **Livello 2 – Intermedio**

- **IN3ECI – Efficienza e resistenza di radiazione**  
  (Documento molto diffuso tra i radioamatori, ma non presente nei risultati della ricerca; si trova facilmente cercando “IN3ECI efficienza antenna pdf”)

- **Antenna Theory – Balanis (3ª o 4ª edizione)**  
  - Companion site ufficiale (Wiley):  
    <https://bcs.wiley.com/he-bcs/Books?action=index&bcsId=11764&itemId=1118642066>  

  - PDF della 3ª edizione (Università dell’Illinois):  
    <https://jontalle.web.engr.illinois.edu/TEACH/BOOKS/Balanis-AntennaTheoryAnalysis_Design3rdEd.05.pdf>  

  - Copia su Internet Archive:  
    <https://ia800501.us.archive.org/30/items/AntennaTheoryAnalysisAndDesign3rdEd/Antenna%20Theory%20Analysis%20and%20Design%203rd%20ed.pdf>  

  - Scheda Google Books (anteprima):  
    <https://books.google.com/books/about/Antenna_Theory.html?id=u-xbCwAAQBAJ>  

  - Edizione 1982 su Internet Archive:  
    <https://archive.org/details/antennatheoryana0000bala>  

---

## **Livello 3 – Avanzato**

- **Field and Wave Electromagnetics – Cheng**  
  (Non è apparso nei risultati della ricerca; si trova cercando “Cheng Field and Wave pdf”)

- **Antenna Theory and Design – Stutzman & Thiele**  
  (Anche questo non è apparso nei risultati; cerca “Stutzman Thiele antenna pdf”)

- **Manuale NEC2 + software 4NEC2**  
  (Cerca “NEC2 manual pdf” e “4NEC2 download”)

---

Se vuoi, posso anche prepararti una versione *ancora più operativa* con:  

- link diretti a capitoli specifici (es. dipolo, monopolo, impedenza);  
- una lista di esercizi progressivi;  
- un percorso guidato per usare NEC2 e verificare i calcoli analitici.


---
…or create a new repository on the command line
echo "# pcb-design-work" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/ettore-galli/pcb-design-work.git
git push -u origin main

…or push an existing repository from the command line
git remote add origin https://github.com/ettore-galli/pcb-design-work.git
git branch -M main
git push -u origin main