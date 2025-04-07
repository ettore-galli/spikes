# CLEANUP ANDROID

## 1 ---------------------------------------------------------------------------------

Ecco un metodo dettagliato per liberare spazio su un telefono Android **senza root** utilizzando **ADB (Android Debug Bridge)**:

---

### **Prerequisiti**

1. **Abilita Debug USB** sul telefono:
   - Vai in *Impostazioni > Informazioni sul telefono* e clicca più volte su *Numero build* per sbloccare le *Opzioni sviluppatore*.
   - Abilita *Debug USB* nelle opzioni sviluppatore.
2. Installa **ADB sul PC**:
   - Scarica [Android SDK Platform Tools](https://developer.android.com/studio/releases/platform-tools) per il tuo sistema operativo.
   - Estrai i file e apri una finestra del terminale nella cartella.

---

### **Passaggi per liberare spazio**

#### **1. Connetti il dispositivo e verifica la connessione ADB**

```bash
adb devices
```

Se vedi il tuo dispositivo nella lista, la connessione è riuscita.

#### **2. Accedi alla shell ADB**

```bash
adb shell
```

#### **3. Analizza lo spazio occupato**

Visualizza la memoria disponibile:

```bash
df -h
```

Cerca le partizioni (es. `/data`, `/sdcard`) per identificare dove lo spazio è esaurito.

#### **4. Elimina file temporanei e cache (senza root)**

- **Cache delle app** (sicuro, non richiede root):

  ```bash
  pm trim-caches 9999999999999999
  ```

  Questo comando pulisce la cache di *tutte* le app.

- **Cancella dati di app specifiche** (se conosci il nome del pacchetto):

  ```bash
  pm clear <nome.pacchetto.app>
  ```

  Esempio per Facebook: `pm clear com.facebook.katana`.

#### **5. Pulisci la cartella Download e file obsoleti**

- Per elencare file grandi nella memoria interna:

  ```bash
  find /sdcard/ -type f -exec du -h {} + | sort -rh | head -n 20
  ```

  (Sostituisci `/sdcard/` con `/storage/emulated/0/` se necessario).

- Per cancellare file (es. vecchi APK, log):

  ```bash
  rm -rf /sdcard/Download/*.apk
  rm -rf /sdcard/DCIM/.thumbnails/*
  ```

#### **6. Gestisci file di grandi dimensioni nelle app**

Alcune app (es. WhatsApp, Telegram) accumulano file multimediali. Usa:

```bash
rm -rf /sdcard/WhatsApp/Media/*.tmp
rm -rf /sdcard/Telegram/Telegram Video/*
```

#### **7. Disinstalla app preinstallate (se supportato)**

Alcuni produttori permettono la disinstallazione senza root:

```bash
pm uninstall --user 0 <nome.pacchetto.app>
```

Esempio per un'app bloatware di Samsung:

```bash
pm uninstall --user 0 com.samsung.android.app.notes
```

> **Nota**: Le app torneranno dopo un reset di fabbrica.

---

### **Alternative senza ADB**

Se ADB è troppo tecnico:

1. Usa l'app **Files by Google** (pulizia automatica di cache e file duplicati).
2. Collegati al PC e cancella manualmente i file nella cartella del telefono.

---

### **Avvertenze**

- Non eliminare cartelle di sistema (`/system`, `/data/data/`) senza root: potresti causare crash.
- Fai un backup prima di cancellare dati importanti.

Con questi passaggi dovresti liberare diversi GB senza root! 🚀

## 2 ---------------------------------------------------------------------------------

Ecco un metodo **senza root** per liberare spazio su Android via ADB, con focus su:  

### **1. Pulizia generale ad ampio raggio**  

#### **A. Cancellare cache di tutte le app**  

```bash
adb shell pm trim-caches 999999999999999
```  

*(Pulisce la cache di sistema e delle app senza eliminare dati personalizzati.)*  

#### **B. Eliminare file temporanei e cache manuale**  

```bash
adb shell rm -rf /sdcard/Download/*
adb shell rm -rf /sdcard/Android/data/*/cache/*
adb shell rm -rf /sdcard/.thumbnails/*
```  

*(Cancella download, cache app, e thumbnail. Sostituisci `/sdcard/` con il percorso della memoria interna se diverso.)*  

#### **C. Forzare la pulizia della memoria interna**  

```bash
adb shell cmd device_config put storage_native_boot enable_gc true
adb shell sm gc
```  

*(Attiva la garbage collection di Android per liberare spazio inattivo.)*  

---

### **2. Individuare le app a maggior consumo di spazio**  

#### **A. Lista app ordinate per dimensione (APK + dati)**  

```bash
adb shell dumpsys package stats | grep -E "Package:|codeSize=|dataSize=" | awk '/Package:/ {app=$2} /codeSize=|dataSize=/ {print app, $0}' | sort -k5 -nr
```  

*(Mostra pacchetto, dimensione APK (`codeSize`), e dati utente (`dataSize`) in ordine decrescente.)*  

#### **B. Controllare occupazione in `/sdcard/Android/data`**  

```bash
adb shell du -h /sdcard/Android/data/ | sort -hr | head -n 20
```  

*(Elenco delle 20 cartelle più pesanti nella memoria interna, dove molte app salvano file.)*  

#### **C. Trova file grandi nella memoria interna**  

```bash
adb shell find /sdcard/ -type f -exec du -h {} + | sort -hr | head -n 30
```  

*(Cerca i 30 file più grandi in `/sdcard/`, utile per trovare video/dump inutilizzati.)*  

---

### **3. Individuare dove si concentra l’occupazione**  

#### **A. Analisi per cartelle principali**  

```bash
adb shell du -h /sdcard/ | sort -hr | head -n 15
```  

*(Mostra le cartelle più pesanti in `/sdcard/`, es. `DCIM`, `WhatsApp`, `Telegram`.)*  

#### **B. Focus su `/Android/data` e `/obb`**  

```bash
adb shell du -h /sdcard/Android/data /sdcard/Android/obb | grep -E "G|M" | sort -hr
```  

*(Filtra solo cartelle con occupazione in GB/MB.)*  

#### **C. Verifica spazio totale disponibile**  

```bash
adb shell df -h /sdcard/
```  

*(Mostra spazio libero/occupato nella memoria interna.)*  

---

### **Bonus: Pulizia mirata senza root**  

- **Disinstallare app bloatware (senza root)**:  

  ```bash
  adb shell pm uninstall --user 0 com.facebook.appmanager
  ```  

  *(Sostituisci con il nome pacchetto dell’app da rimuovere. Funziona per molte app preinstallate.)*  

- **Eliminare backup obsoleti**:  

  ```bash
  adb shell rm -rf /sdcard/*.bak /sdcard/*.tmp
  ```  

---

### **Note importanti:**  

- **Nessun dato perso**: I comandi `rm` cancellano file permanentemente. Usa `ls` prima per verificare (es. `adb shell ls /sdcard/Download/`).  
- **Alternative grafiche**: Se hai accesso al dispositivo, app come **DiskUsage** aiutano a visualizzare lo spazio in modo intuitivo.  
- **Limitazioni**: Senza root, non puoi eliminare dati in `/data/data/<app>` o cache di sistema profonda.  

Se vuoi un report dettagliato dell’occupazione, esegui:  

```bash
adb shell dumpsys diskstats > storage_analysis.txt
```  

Poi analizzalo sul PC. 🚀
