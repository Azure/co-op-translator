<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "bd4704f50c55da7d572b691484aa0b30",
  "translation_date": "2025-10-15T03:04:06+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "it"
}
-->
# Contribuire a Co-op Translator

Questo progetto accoglie con piacere contributi e suggerimenti. La maggior parte dei contributi richiede che tu accetti un Contributor License Agreement (CLA) che dichiari di avere il diritto di concederci l’uso del tuo contributo. Per maggiori dettagli, visita https://cla.opensource.microsoft.com.

Quando invii una pull request, un bot CLA determinerà automaticamente se devi fornire un CLA e aggiornerà la PR di conseguenza (ad esempio, con un controllo di stato o un commento). Segui semplicemente le istruzioni fornite dal bot. Dovrai farlo solo una volta per tutti i repository che usano il nostro CLA.

## Configurazione dell’ambiente di sviluppo

Per configurare l’ambiente di sviluppo di questo progetto, consigliamo di usare Poetry per la gestione delle dipendenze. Usiamo `pyproject.toml` per gestire le dipendenze del progetto, quindi per installarle dovresti usare Poetry.

### Creare un ambiente virtuale

#### Usando pip

```bash
python -m venv .venv
```

#### Usando Poetry

```bash
poetry init
```

### Attivare l’ambiente virtuale

#### Per entrambi, pip e Poetry

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

### Installazione del pacchetto e delle dipendenze necessarie

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

2. Copia nella cartella di test alcuni file markdown e immagini che vuoi tradurre. Ad esempio:
    ```bash
    cp /path/to/your/docs/*.md test_docs/
    cp /path/to/your/images/*.png test_docs/
    ```

3. Installa il pacchetto localmente:
    ```bash
    pip install -e .
    ```

4. Esegui Co-op Translator sui tuoi documenti di test:
    ```bash
    python -m co_op_translator --language-codes ko --root-dir test_docs
    ```

5. Controlla i file tradotti in `test_docs/translations` e `test_docs/translated_images` per verificare:
   - La qualità della traduzione
   - Che i commenti dei metadati siano corretti
   - Che la struttura originale del markdown sia preservata
   - Che link e immagini funzionino correttamente

Questo test manuale aiuta a garantire che le tue modifiche funzionino bene in scenari reali.

### Variabili d’ambiente

1. Crea un file `.env` nella directory principale copiando il file `.env.template` fornito.
1. Compila le variabili d’ambiente come indicato.

> [!TIP]
>
> ### Opzioni aggiuntive per l’ambiente di sviluppo
>
> Oltre a eseguire il progetto in locale, puoi anche usare GitHub Codespaces o i Dev Containers di VS Code per un’alternativa nella configurazione dell’ambiente di sviluppo.
>
> #### GitHub Codespaces
>
> Puoi eseguire questi esempi virtualmente usando GitHub Codespaces senza bisogno di ulteriori configurazioni.
>
> Il pulsante aprirà una versione web di VS Code nel tuo browser:
>
> 1. Apri il template (potrebbe richiedere alcuni minuti):
>
>     [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/azure/co-op-translator)
>
> #### Esecuzione locale con VS Code Dev Containers
>
> ⚠️ Questa opzione funziona solo se Docker Desktop ha almeno 16 GB di RAM allocati. Se hai meno di 16 GB di RAM, puoi provare l’opzione [GitHub Codespaces](../..) o [configurare tutto in locale](../..).
>
> Un’opzione correlata sono i Dev Containers di VS Code, che apriranno il progetto nel tuo VS Code locale usando l’estensione [Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers):
>
> 1. Avvia Docker Desktop (installalo se non è già installato)
> 2. Apri il progetto:
>
>    [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator)


### Stile del codice

Usiamo [Black](https://github.com/psf/black) come formattatore di codice Python per mantenere uno stile coerente in tutto il progetto. Black è un formattatore che riformatta automaticamente il codice Python secondo lo stile Black.

#### Configurazione

La configurazione di Black è specificata nel nostro `pyproject.toml`:

```toml
[tool.black]
line-length = 88
target-version = ['py310']
include = '\.pyi?$'
```

#### Installazione di Black

Puoi installare Black usando Poetry (consigliato) o pip:

##### Usando Poetry

Black viene installato automaticamente quando configuri l’ambiente di sviluppo:
```bash
poetry install
```

##### Usando pip

Se usi pip, puoi installare Black direttamente:
```bash
pip install black
```

#### Utilizzo di Black

##### Con Poetry

1. Formattta tutti i file Python del progetto:
    ```bash
    poetry run black .
    ```

2. Formattta un file o una cartella specifica:
    ```bash
    poetry run black path/to/file_or_directory
    ```

##### Con pip

1. Formattta tutti i file Python del progetto:
    ```bash
    black .
    ```

2. Formattta un file o una cartella specifica:
    ```bash
    black path/to/file_or_directory
    ```

> [!TIP]
> Ti consigliamo di configurare il tuo editor per formattare automaticamente il codice con Black al salvataggio. La maggior parte degli editor moderni lo supporta tramite estensioni o plugin.

## Esecuzione di Co-op Translator

Per eseguire Co-op Translator usando Poetry nel tuo ambiente, segui questi passaggi:

1. Vai nella cartella dove vuoi eseguire i test di traduzione o crea una cartella temporanea per i test.

2. Esegui il seguente comando. Sostituisci `-l ko` con il codice della lingua in cui vuoi tradurre. Il flag `-d` attiva la modalità debug.

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> [!NOTE]
> Assicurati che l’ambiente Poetry sia attivato (poetry shell) prima di eseguire il comando.

## Contribuire una nuova lingua

Accogliamo con piacere contributi che aggiungono il supporto a nuove lingue. Prima di aprire una PR, completa i passaggi seguenti per facilitare la revisione.

1. Aggiungi la lingua alla mappatura dei font
   - Modifica `src/co_op_translator/fonts/font_language_mappings.yml`
   - Aggiungi una voce con:
     - `code`: codice lingua in stile ISO (es. `vi`)
     - `name`: nome visualizzato comprensibile
     - `font`: un font presente in `src/co_op_translator/fonts/` che supporta lo script
     - `rtl`: `true` se la lingua è da destra a sinistra, altrimenti `false`

2. Includi i file dei font necessari (se servono)
   - Se serve un nuovo font, verifica che la licenza sia compatibile con la distribuzione open source
   - Aggiungi il file del font in `src/co_op_translator/fonts/`

3. Verifica locale
   - Esegui traduzioni su un piccolo campione (Markdown, immagini e notebook se necessario)
   - Verifica che l’output sia visualizzato correttamente, inclusi font e layout RTL se applicabile

4. Aggiorna la documentazione
   - Assicurati che la lingua compaia in `getting_started/supported-languages.md`
   - Non sono necessarie modifiche a `README_languages_template.md`; viene generato automaticamente dalla lista delle lingue supportate

5. Apri una PR
   - Descrivi la lingua aggiunta e qualsiasi considerazione su font/licenza
   - Allega screenshot degli output renderizzati se possibile

Esempio di voce YAML:

```yaml
new_lang(code):
  name: "New Language"
  font: "NotoSans-Medium.ttf"
  rtl: false
```


## Maintainer

### Messaggio di commit e strategia di merge

Per garantire coerenza e chiarezza nella cronologia dei commit del progetto, seguiamo un formato specifico **per il messaggio di commit finale** quando usiamo la strategia **Squash and Merge**.

Quando una pull request (PR) viene unita, i singoli commit vengono uniti in un unico commit. Il messaggio di commit finale deve seguire il formato qui sotto per mantenere una cronologia pulita e coerente.

#### Formato del messaggio di commit (per squash and merge)

Usiamo il seguente formato per i messaggi di commit:

```bash
<type>: <description> (#<PR number>)
```

- **type**: Specifica la categoria del commit. Usiamo i seguenti tipi:
  - `Docs`: Per aggiornamenti alla documentazione.
  - `Build`: Per modifiche al sistema di build o alle dipendenze, inclusi aggiornamenti a file di configurazione, workflow CI o Dockerfile.
  - `Core`: Per modifiche alle funzionalità principali del progetto, in particolare ai file nella cartella `src/co_op_translator/core`.

- **description**: Un breve riassunto della modifica.
- **PR number**: Il numero della pull request associata al commit.

**Esempi**:

- `Docs: Aggiorna le istruzioni di installazione per maggiore chiarezza (#50)`
- `Core: Migliora la gestione della traduzione delle immagini (#60)`

> [!NOTE]
> Attualmente, i prefissi **`Docs`**, **`Core`** e **`Build`** vengono aggiunti automaticamente ai titoli delle PR in base alle etichette applicate al codice modificato. Finché l’etichetta corretta è applicata, di solito non è necessario aggiornare manualmente il titolo della PR. Devi solo verificare che tutto sia corretto e che il prefisso sia stato generato correttamente.

#### Strategia di merge

Usiamo **Squash and Merge** come strategia predefinita per le pull request. Questa strategia garantisce che i messaggi di commit seguano il nostro formato, anche se i singoli commit non lo fanno.

**Motivi**:

- Una cronologia del progetto pulita e lineare.
- Coerenza nei messaggi di commit.
- Meno rumore da commit minori (es. "fix typo").

Quando unisci, assicurati che il messaggio di commit finale segua il formato descritto sopra.

**Esempio di Squash and Merge**
Se una PR contiene i seguenti commit:

- `fix typo`
- `update README`
- `adjust formatting`

Devono essere uniti in:
`Docs: Migliora la chiarezza e la formattazione della documentazione (#65)`

---

**Disclaimer**:
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per garantire l’accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale umana. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall’uso di questa traduzione.