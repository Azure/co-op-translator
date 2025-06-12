<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d95d7ec0097c5569ac16dd42840787a2",
  "translation_date": "2025-06-12T09:33:27+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "it"
}
-->
# Contribuire a Co-op Translator

Questo progetto accoglie contributi e suggerimenti. La maggior parte dei contributi richiede di accettare un Contributor License Agreement (CLA) che dichiara che hai il diritto e effettivamente concedi a noi i diritti di utilizzare il tuo contributo. Per i dettagli, visita https://cla.opensource.microsoft.com.

Quando invii una pull request, un bot CLA determinerà automaticamente se devi fornire un CLA e decorerà la PR di conseguenza (ad esempio, controllo stato, commento). Segui semplicemente le istruzioni fornite dal bot. Dovrai farlo una sola volta per tutti i repository che usano il nostro CLA.

## Configurazione dell’ambiente di sviluppo

Per configurare l’ambiente di sviluppo di questo progetto, consigliamo di usare Poetry per la gestione delle dipendenze. Usiamo `pyproject.toml` per gestire le dipendenze di progetto, quindi per installarle devi usare Poetry.

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

### Installazione del pacchetto e delle dipendenze richieste

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

4. Esegui Co-op Translator sui tuoi documenti di test:
    ```bash
    python -m co_op_translator --language-codes ko --root-dir test_docs
    ```

5. Controlla i file tradotti in `test_docs/translations` and `test_docs/translated_images` to verify:
   - The translation quality
   - The metadata comments are correct
   - The original markdown structure is preserved
   - Links and images are working properly

This manual testing helps ensure that your changes work well in real-world scenarios.

### Environment variables

1. Create an `.env` file in the root directory by copying the provided `.env.template`.
1. Compila le variabili d’ambiente come indicato.

> [!TIP]
>
> ### Opzioni aggiuntive per l’ambiente di sviluppo
>
> Oltre a eseguire il progetto localmente, puoi anche usare GitHub Codespaces o VS Code Dev Containers come ambienti di sviluppo alternativi.
>
> #### GitHub Codespaces
>
> Puoi eseguire questi esempi virtualmente usando GitHub Codespaces senza necessità di configurazioni aggiuntive.
>
> Il pulsante aprirà un’istanza web di VS Code nel tuo browser:
>
> 1. Apri il template (potrebbero volerci alcuni minuti):
>
>     [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/azure/co-op-translator)
>
> #### Esecuzione locale con VS Code Dev Containers
>
> ⚠️ Questa opzione funziona solo se Docker Desktop ha almeno 16 GB di RAM assegnati. Se hai meno di 16 GB di RAM, puoi provare l’opzione [GitHub Codespaces](../..) o [configurare l’ambiente localmente](../..).
>
> Un’opzione correlata è VS Code Dev Containers, che apre il progetto nella tua VS Code locale usando l’estensione [Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers):
>
> 1. Avvia Docker Desktop (installalo se non è già presente)
> 2. Apri il progetto:
>
>    [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator)


### Stile del codice

Usiamo [Black](https://github.com/psf/black) come formatter per mantenere uno stile di codice coerente in tutto il progetto. Black è un formatter rigoroso che riformatta automaticamente il codice Python per aderire allo stile Black.

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
> Ti consigliamo di configurare il tuo editor per formattare automaticamente il codice con Black al salvataggio. La maggior parte degli editor moderni supporta questa funzione tramite estensioni o plugin.

## Esecuzione di Co-op Translator

Per eseguire Co-op Translator usando Poetry nel tuo ambiente, segui questi passaggi:

1. Spostati nella cartella dove vuoi fare i test di traduzione o crea una cartella temporanea per i test.

2. Esegui il comando seguente. Il flag `-l ko` with the language code you wish to translate into. The `-d` indica la modalità debug.

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> [!NOTE]
> Assicurati che l’ambiente Poetry sia attivato (poetry shell) prima di eseguire il comando.

## Maintainer

### Messaggio di commit e strategia di merge

Per garantire coerenza e chiarezza nella cronologia dei commit del progetto, seguiamo un formato specifico per il messaggio di commit **finale** quando usiamo la strategia **Squash and Merge**.

Quando una pull request (PR) viene unita, i singoli commit vengono compressi in un unico commit. Il messaggio finale deve seguire il formato qui sotto per mantenere una cronologia pulita e coerente.

#### Formato del messaggio di commit (per squash and merge)

Usiamo il seguente formato per i messaggi di commit:

```bash
<type>: <description> (#<PR number>)
```

- **type**: Specifica la categoria del commit. Usiamo i seguenti tipi:
  - `Docs`: For documentation updates.
  - `Build`: For changes related to the build system or dependencies, including updates to configuration files, CI workflows, or the Dockerfile.
  - `Core`: For modifications to the project's core functionality or features, particularly those involving files in the `src/co_op_translator/core` directory.

- **description**: A concise summary of the change.
- **PR number**: The number of the pull request associated with the commit.

**Examples**:

- `Docs: Update installation instructions for clarity (#50)`
- `Core: Improve handling of image translation (#60)`

> [!NOTE]
> Currently, the **`Docs`**, **`Core`**, and **`Build`** prefixes are automatically added to PR titles based on the labels applied to the modified source code. As long as the correct label is applied, you typically don't need to manually update the PR title. You just need to verify that everything is correct and the prefix has been generated appropriately.

#### Merge strategy

We use **Squash and Merge** as our default strategy for pull requests. This strategy ensures that commit messages follow our format, even if individual commits don't.

**Reasons**:

- A clean, linear project history.
- Consistency in commit messages.
- Reduced noise from minor commits (e.g., "fix typo").

When merging, ensure the final commit message follows the commit message format described above.

**Example of Squash and Merge**
If a PR contains the following commits:

- `fix typo`
- `update README`
- `adjust formatting`

They should be squashed into:
`Docs: Improve documentation clarity and formatting (#65)`

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica AI [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per garantire accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda la traduzione professionale umana. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall’uso di questa traduzione.