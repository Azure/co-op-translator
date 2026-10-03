# Guida per i manutentori

Questa pagina riassume come sono collegati l'API, la CLI e il sito della documentazione.

## Confine dell'API pubblica

L'API Python stabile è esportata da:

```python
co_op_translator.api
```

L'API pubblica è organizzata in helper per la traduzione dei contenuti, helper per la riscrittura dei percorsi, orchestrazione del progetto e revisione:

```python
from co_op_translator.api import (
    ImageTranslationOptions,
    MarkdownTranslationOptions,
    NotebookTranslationOptions,
    TranslationBaseline,
    TranslationStateProvider,
    TranslationUpdate,
    run_review,
    run_translation,
    rewrite_markdown_paths,
    rewrite_notebook_paths,
    translate_image_content,
    translate_markdown_content,
    translate_notebook_content,
    translate_project,
)
```

`TranslationStateProvider` è il confine di persistenza per le integrazioni ospitate.
Deve mantenere i candidati generati separati dalle baseline accettate in modo che una
traduzione non unita non possa diventare la fonte della verità.

Quando si aggiungono nuove API pubbliche, aggiornare:

- `src/co_op_translator/api/__init__.py`
- `docs/api.md`
- test API rilevanti in `tests/co_op_translator/`, come `test_api.py` o `test_review_api.py`

Evitare di documentare i moduli `core` di basso livello come API stabili a meno che il progetto non intenda supportarli direttamente.

## Punti di ingresso della CLI

Il pacchetto definisce questi script di Poetry:

```toml
[tool.poetry.scripts]
translate = "co_op_translator.__main__:main"
evaluate = "co_op_translator.__main__:main"
migrate-links = "co_op_translator.__main__:main"
co-op-review = "co_op_translator.__main__:main"
co-op-translator-mcp = "co_op_translator.mcp.server:main"
```

`src/co_op_translator/__main__.py` esegue il dispatch in base al nome dello script:

- `translate` chiama `co_op_translator.cli.translate.translate_command`
- `evaluate` chiama `co_op_translator.cli.evaluate.evaluate_command`
- `migrate-links` chiama `co_op_translator.cli.migrate_links.migrate_links_command`
- `co-op-review` chiama `co_op_translator.cli.review.review_command`

`co-op-translator-mcp` aggira `__main__.py` e chiama `co_op_translator.mcp.server:main` direttamente.

Quando si aggiungono o si modificano le opzioni della CLI, aggiornare:

- il comando rilevante in `src/co_op_translator/cli/*.py`
- `docs/cli.md`
- test relativi alla CLI, se il comportamento cambia

## MCP server

Il server MCP è implementato in:

```python
co_op_translator.mcp.server
```

Il server avvolge intenzionalmente l'API Python pubblica invece di chiamare i moduli `core` di basso livello. Mantenere questo confine intatto in modo che i client MCP, i chiamanti Python e la CLI condividano lo stesso comportamento.

Quando si aggiungono o si modificano strumenti MCP, aggiornare:

- `src/co_op_translator/mcp/server.py`
- `tests/co_op_translator/test_mcp_server.py`
- `docs/mcp.md`
- `docs/api.md` se la superficie dell'API pubblica cambia

Gli strumenti di traduzione del repository sono chiamabili tramite modello attraverso MCP e possono scrivere molti file. Mantenere `dry_run=True` come impostazione predefinita e richiedere `confirm_write=True` prima della traduzione di un progetto non in dry-run.

## Flusso di traduzione

Il flusso di traduzione del progetto ad alto livello è:

1. Analizzare gli argomenti della CLI o i parametri dell'API.
2. Validare la configurazione LLM con `LLMConfig`.
3. Validare Azure AI Vision quando è selezionata la traduzione delle immagini.
4. Normalizzare i codici delle lingue.
5. Rilevare alias legacy delle cartelle delle lingue.
6. Stimare il volume di traduzione.
7. Aggiornare le sezioni di lingua/corso del README quando applicabile.
8. Delegare la traduzione del progetto a `ProjectTranslator`.
9. `ProjectTranslator` delega l'elaborazione dei file a `TranslationManager`.

`TranslationManager` è composto da mixin focalizzati per tipo di file:

- `ProjectMarkdownTranslationMixin` gestisce la lettura di file Markdown, la traduzione dei contenuti, la riscrittura dei percorsi, i metadati, le avvertenze e le operazioni di scrittura.
- `ProjectNotebookTranslationMixin` gestisce la lettura di file notebook, la traduzione delle celle Markdown, la riscrittura dei percorsi, i metadati, le avvertenze e le operazioni di scrittura.
- `ProjectImageTranslationMixin` gestisce la scoperta delle immagini, l'estrazione/traduzione del testo, la scrittura delle immagini renderizzate e i metadati.

Le API di contenuto di livello inferiore saltano il flusso di lavoro del progetto:

1. `translate_markdown_content` e `translate_notebook_content` traducono solo contenuti in memoria.
2. `translate_image_content` traduce il testo in una singola immagine e restituisce un oggetto immagine renderizzato.
3. `rewrite_markdown_paths` e `rewrite_notebook_paths` sono helper espliciti di post-elaborazione. Non eseguono traduzioni né scritture sul progetto.

## Flusso di revisione

Il flusso di revisione deterministico è:

1. Analizzare gli argomenti della CLI o i parametri dell'API.
2. Normalizzare i codici lingua richiesti.
3. Costruire uno o più obiettivi di revisione da `root_dir`, `root_dirs` o `groups`.
4. Facoltativamente limitare i file sorgente con `--changed-from`.
5. Eseguire controlli deterministici per struttura, freschezza delle traduzioni, integrità del Markdown e percorsi di link/immagini locali.
6. Stampare l'output come testo o come Markdown in stile GitHub.
7. Terminare con un errore quando vengono trovati errori di revisione.

Il flusso di revisione non richiede chiavi API e rimane disponibile per controlli locali o CI dei consumatori con opt-in. Questo repository non esegue `co-op-review` automaticamente su ogni pull request.

## Sito della documentazione

Il sito di documentazione è configurato da:

```text
mkdocs.yml
requirements-docs.txt
docs/
```

La directory `docs/` è la fonte canonica della documentazione. Non aggiungere nuove guide per l'utente finale al di fuori di questa directory a meno che il progetto non introduca intenzionalmente un'altra superficie di documentazione pubblicata.

Costruire localmente:

```bash
python -m pip install -r requirements-docs.txt
python -m mkdocs build --strict
```

Anteprima locale:

```bash
python -m mkdocs serve
```

Il sito generato viene scritto in `site/`, che è ignorato da git.

## Flusso di lavoro GitHub Pages

`.github/workflows/docs.yml` costruisce il sito sulle pull request e lo distribuisce quando si esegue il push su `main`.

Il workflow installa:

```bash
pip install -r requirements-docs.txt
```

Il workflow dei docs installa solo la toolchain di documentazione. `mkdocs.yml` punta `mkdocstrings` a `src/` in modo che le pagine dell'API pubblica possano essere renderizzate dal tree dei sorgenti senza installare l'intero set di dipendenze di runtime. Se le future documentazioni API richiedono l'importazione di provider di runtime opzionali durante la build, aggiornare sia `.github/workflows/docs.yml` che questa guida insieme.

## Standard di qualità della documentazione

Prima di unire le modifiche alla documentazione, eseguire:

```bash
python -m mkdocs build --strict
git diff --check
```

Usare build rigorose in modo che i link rotti, le voci di navigazione non valide e i problemi di rendering delle API vengano individuati precocemente.