<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "758ca1c5ae0d32c52d2dd59132dcfbf0",
  "translation_date": "2025-11-30T10:58:17+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "it"
}
-->
# Contribuire a Co-op Translator

Questo progetto accoglie contributi e suggerimenti. La maggior parte dei contributi richiede di accettare un
Contributor License Agreement (CLA) che dichiara che hai il diritto e effettivamente concedi a noi
i diritti di utilizzare il tuo contributo. Per dettagli, visita https://cla.opensource.microsoft.com.

Quando invii una pull request, un bot CLA determinerà automaticamente se devi fornire
un CLA e decorerà la PR di conseguenza (ad esempio, controllo di stato, commento). Segui semplicemente le istruzioni
fornite dal bot. Dovrai farlo solo una volta per tutti i repository che usano il nostro CLA.

## Configurazione dell'ambiente di sviluppo

Per configurare l'ambiente di sviluppo per questo progetto, consigliamo di usare Poetry per la gestione delle dipendenze. Usiamo `pyproject.toml` per gestire le dipendenze del progetto, quindi per installare le dipendenze dovresti usare Poetry.

### Creare un ambiente virtuale

#### Usando pip

```bash
python -m venv .venv
```

#### Usando Poetry

```bash
poetry init
```

### Attivare l'ambiente virtuale

#### Per pip e Poetry

- Windows:

    ```bash
    .venv\Scripts\activate.bat
    ```

- Mac/Linux:

    ```bash
    source .venv/bin/activate
    ```

#### Usando Poetry

```bash
poetry shell
```

### Installare il pacchetto e i pacchetti richiesti

#### Usando Poetry (da pyproject.toml)

```bash
poetry install
```

### Test manuale

Prima di inviare una PR, è importante testare la funzionalità di traduzione con documentazione reale:

1. Crea una cartella di test nella directory principale:
    ```bash
    mkdir test_docs
    ```

2. Copia nella cartella di test alcuni documenti markdown e immagini che vuoi tradurre. Per esempio:
    ```bash
    cp /path/to/your/docs/*.md test_docs/
    cp /path/to/your/images/*.png test_docs/
    ```

3. Installa il pacchetto localmente:
    ```bash
    pip install -e .
    ```

4. Esegui Co-op Translator sui documenti di test:
    ```bash
    python -m co_op_translator --language-codes ko --root-dir test_docs
    ```

5. Controlla i file tradotti in `test_docs/translations` e `test_docs/translated_images` per verificare:
   - La qualità della traduzione
   - Che i commenti dei metadati siano corretti
   - Che la struttura originale del markdown sia preservata
   - Che link e immagini funzionino correttamente

Questo test manuale aiuta a garantire che le tue modifiche funzionino bene in scenari reali.

### Variabili d'ambiente

1. Crea un file `.env` nella directory principale copiando il file `.env.template` fornito.
1. Compila le variabili d'ambiente come indicato.

> [!TIP]
>
> ### Opzioni aggiuntive per l'ambiente di sviluppo
>
> Oltre a eseguire il progetto localmente, puoi anche usare GitHub Codespaces o VS Code Dev Containers come alternative per la configurazione dell'ambiente di sviluppo.
>
> #### GitHub Codespaces
>
> Puoi eseguire questi esempi virtualmente usando GitHub Codespaces senza necessità di ulteriori impostazioni.
>
> Il pulsante aprirà un'istanza web di VS Code nel tuo browser:
>
> 1. Apri il template (potrebbe richiedere alcuni minuti):
>
>     [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/azure/co-op-translator)
>
> #### Esecuzione locale con VS Code Dev Containers
>
> ⚠️ Questa opzione funziona solo se Docker Desktop ha almeno 16 GB di RAM allocati. Se hai meno di 16 GB, puoi provare l'[opzione GitHub Codespaces](../..) o [configurare localmente](../..).
>
> Un'opzione correlata è VS Code Dev Containers, che apre il progetto nel tuo VS Code locale usando l'[estensione Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers):
>
> 1. Avvia Docker Desktop (installalo se non è già presente)
> 2. Apri il progetto:
>
>    [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator)


### Stile del codice

Usiamo [Black](https://github.com/psf/black) come formattatore di codice Python per mantenere uno stile coerente in tutto il progetto. Black è un formattatore di codice rigoroso che riformatta automaticamente il codice Python per conformarsi allo stile Black.

#### Configurazione

La configurazione di Black è specificata nel nostro `pyproject.toml`:

```toml
[tool.black]
line-length = 88
target-version = ['py310']
include = '\.pyi?$'
```

#### Installare Black

Puoi installare Black usando Poetry (consigliato) o pip:

##### Usando Poetry

Black viene installato automaticamente quando configuri l'ambiente di sviluppo:
```bash
poetry install
```

##### Usando pip

Se usi pip, puoi installare Black direttamente:
```bash
pip install black
```

#### Usare Black

##### Con Poetry

1. Formattta tutti i file Python nel progetto:
    ```bash
    poetry run black .
    ```

2. Formattta un file o una cartella specifica:
    ```bash
    poetry run black path/to/file_or_directory
    ```

##### Con pip

1. Formattta tutti i file Python nel progetto:
    ```bash
    black .
    ```

2. Formattta un file o una cartella specifica:
    ```bash
    black path/to/file_or_directory
    ```

> [!TIP]
> Consigliamo di configurare il tuo editor per formattare automaticamente il codice con Black al salvataggio. La maggior parte degli editor moderni supporta questa funzione tramite estensioni o plugin.

## Eseguire Co-op Translator

Per eseguire Co-op Translator usando Poetry nel tuo ambiente, segui questi passaggi:

1. Vai nella cartella dove vuoi fare i test di traduzione o crea una cartella temporanea per i test.

2. Esegui il comando seguente. Sostituisci `-l ko` con il codice della lingua in cui vuoi tradurre. Il flag `-d` indica la modalità debug.

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> [!NOTE]
> Assicurati che l'ambiente Poetry sia attivato (poetry shell) prima di eseguire il comando.

## Contribuire con una nuova lingua

Accogliamo contributi che aggiungono supporto per nuove lingue. Prima di aprire una PR, completa i passaggi seguenti per garantire una revisione fluida.

1. Aggiungi la lingua alla mappatura dei font
   - Modifica `src/co_op_translator/fonts/font_language_mappings.yml`
   - Aggiungi una voce con:
     - `code`: codice lingua in stile ISO (es. `vi`)
     - `name`: nome leggibile per l'utente
     - `font`: un font incluso in `src/co_op_translator/fonts/` che supporta lo script
     - `rtl`: `true` se la lingua è da destra a sinistra, altrimenti `false`

2. Includi i file font necessari (se richiesti)
   - Se serve un nuovo font, verifica la compatibilità della licenza per la distribuzione open source
   - Aggiungi il file font in `src/co_op_translator/fonts/`

3. Verifica locale
   - Esegui traduzioni su un piccolo campione (Markdown, immagini e notebook se applicabile)
   - Verifica che l'output venga renderizzato correttamente, inclusi font e layout RTL se presenti

4. Aggiorna la documentazione
   - Assicurati che la lingua appaia in `getting_started/supported-languages.md`
   - Non è necessario modificare `getting_started/README_languages_template.md`; viene generato dalla lista supportata

5. Apri una PR
   - Descrivi la lingua aggiunta e eventuali considerazioni su font/licenze
   - Allega screenshot degli output renderizzati se possibile

Esempio di voce YAML:

```yaml
new_lang(code):
  name: "New Language"
  font: "NotoSans-Medium.ttf"
  rtl: false
```

### Testare la nuova lingua

Puoi testare la nuova lingua eseguendo il comando seguente:

```bash
# Crea e attiva un ambiente virtuale
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
# Installa il pacchetto di sviluppo
pip install -e .
# Esegui la traduzione
translate -l "new_lang"
```

## Maintainer

### Messaggi di commit e strategia di merge

Per garantire coerenza e chiarezza nella cronologia dei commit del progetto, seguiamo un formato specifico per il messaggio di commit **del commit finale** quando usiamo la strategia **Squash and Merge**.

Quando una pull request (PR) viene unita, i singoli commit vengono compressi in un unico commit. Il messaggio finale deve seguire il formato indicato per mantenere una cronologia pulita e coerente.

#### Formato del messaggio di commit (per squash and merge)

Usiamo il seguente formato per i messaggi di commit:

```bash
<type>: <description> (#<numero PR>)
```

- **type**: specifica la categoria del commit. Usiamo i seguenti tipi:
  - `Docs`: per aggiornamenti alla documentazione.
  - `Build`: per modifiche relative al sistema di build o dipendenze, inclusi aggiornamenti a file di configurazione, workflow CI o Dockerfile.
  - `Core`: per modifiche alla funzionalità o caratteristiche principali del progetto, in particolare per file nella cartella `src/co_op_translator/core`.

- **description**: un riassunto conciso della modifica.
- **PR number**: il numero della pull request associata al commit.

**Esempi**:

- `Docs: Aggiorna istruzioni di installazione per maggiore chiarezza (#50)`
- `Core: Migliora gestione della traduzione delle immagini (#60)`

> [!NOTE]
> Attualmente, i prefissi **`Docs`**, **`Core`** e **`Build`** vengono aggiunti automaticamente ai titoli delle PR in base alle etichette applicate al codice sorgente modificato. Finché l'etichetta corretta è applicata, di solito non è necessario aggiornare manualmente il titolo della PR. Basta verificare che tutto sia corretto e che il prefisso sia stato generato correttamente.

#### Strategia di merge

Usiamo **Squash and Merge** come strategia predefinita per le pull request. Questa strategia garantisce che i messaggi di commit seguano il nostro formato, anche se i singoli commit non lo fanno.

**Motivi**:

- Una cronologia del progetto pulita e lineare.
- Coerenza nei messaggi di commit.
- Riduzione del rumore da commit minori (es. "fix typo").

Quando unisci, assicurati che il messaggio del commit finale segua il formato descritto sopra.

**Esempio di Squash and Merge**
Se una PR contiene i seguenti commit:

- `fix typo`
- `update README`
- `adjust formatting`

Dovrebbero essere compressi in:
`Docs: Migliora chiarezza e formattazione della documentazione (#65)`

### Processo di rilascio

Questa sezione descrive il modo più semplice per i maintainer di pubblicare una nuova release di Co-op Translator.

#### 1. Aggiornare la versione in `pyproject.toml`

1. Decidi il prossimo numero di versione (seguiamo semantic versioning: `MAJOR.MINOR.PATCH`).
2. Modifica `pyproject.toml` aggiornando il campo `version` sotto `[tool.poetry]`.
3. Apri una pull request dedicata che modifica solo la versione (e eventuali file di lock o metadati aggiornati automaticamente, se presenti).
4. Dopo la revisione, usa **Squash and Merge** e assicurati che il messaggio finale segua il formato descritto sopra.

#### 2. Creare una Release su GitHub

1. Vai alla pagina del repository GitHub e apri **Releases** → **Draft a new release**.
2. Crea un nuovo tag (ad esempio, `v0.13.0`) dal branch `main`.
3. Imposta il titolo della release con la stessa versione (ad esempio, `v0.13.0`).
4. Clicca su **Generate release notes** per auto-compilare il changelog.
5. Modifica eventualmente il testo (ad esempio, per evidenziare nuove lingue supportate o cambiamenti importanti).
6. Pubblica la release.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per garantire l’accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un traduttore umano. Non ci assumiamo alcuna responsabilità per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->