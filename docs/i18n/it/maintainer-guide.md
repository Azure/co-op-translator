# Guida per i manutentori

Questa pagina riassume come sono collegati tra loro l'API, la CLI e il sito di documentazione.

## Confine dell'API pubblica

L'API Python stabile è esportata da:

```python
co_op_translator.api
```

L'API pubblica è organizzata in helper per la traduzione dei contenuti, helper per la riscrittura dei percorsi, orchestrazione dei progetti e revisione:

```python
from co_op_translator.api import (
    ImageTranslationOptions,
    MarkdownTranslationOptions,
    NotebookTranslationOptions,
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

Quando si aggiungono nuove API pubbliche, aggiornare:

- `src/co_op_translator/api/__init__.py`
- `docs/api.md`
- relevant API tests under `tests/co_op_translator/`, such as `test_api.py` or `test_review_api.py`

Evitare di documentare i moduli di livello inferiore `core` come API stabili a meno che il progetto non intenda supportarli direttamente.

## Punti di ingresso CLI

Il pacchetto definisce questi script Poetry:

```toml
[tool.poetry.scripts]
translate = "co_op_translator.__main__:main"
evaluate = "co_op_translator.__main__:main"
migrate-links = "co_op_translator.__main__:main"
co-op-review = "co_op_translator.__main__:main"
co-op-translator-mcp = "co_op_translator.mcp.server:main"
```

`src/co_op_translator/__main__.py` instrada in base al nome dello script:

- `translate` chiama `co_op_translator.cli.translate.translate_command`
- `evaluate` chiama `co_op_translator.cli.evaluate.evaluate_command`
- `migrate-links` chiama `co_op_translator.cli.migrate_links.migrate_links_command`
- `co-op-review` chiama `co_op_translator.cli.review.review_command`

`co-op-translator-mcp` aggira `__main__.py` e chiama direttamente `co_op_translator.mcp.server:main`.

Quando si aggiungono o modificano le opzioni della CLI, aggiornare:

- the relevant `src/co_op_translator/cli/*.py` command
- `docs/cli.md`
- i test relativi alla CLI, se il comportamento cambia

## Server MCP

Il server MCP è implementato in:

```python
co_op_translator.mcp.server
```

Il server avvolge intenzionalmente l'API Python pubblica piuttosto che chiamare i moduli di livello inferiore `core`. Mantieni questo confine intatto in modo che i client MCP, i chiamanti Python e la CLI condividano lo stesso comportamento.

Quando si aggiungono o modificano gli strumenti MCP, aggiornare:

- `src/co_op_translator/mcp/server.py`
- `tests/co_op_translator/test_mcp_server.py`
- `docs/mcp.md`
- `docs/api.md` if the public API surface changes

Gli strumenti di traduzione del repository sono invocabili tramite modello attraverso MCP e possono scrivere molti file. Mantieni `dry_run=True` come valore predefinito e richiedi `confirm_write=True` prima di una traduzione del progetto non in modalità dry-run.

## Flusso di traduzione

Il flusso di traduzione del progetto ad alto livello è:

1. Analizza gli argomenti della CLI o i parametri dell'API.
2. Valida la configurazione LLM con `LLMConfig`.
3. Valida Azure AI Vision quando è selezionata la traduzione delle immagini.
4. Normalizza i codici lingua.
5. Rileva alias di cartelle lingua legacy.
6. Stima il volume di traduzione.
7. Aggiorna le sezioni lingua/corso del README quando applicabile.
8. Delega la traduzione del progetto a `ProjectTranslator`.
9. `ProjectTranslator` delega l'elaborazione dei file a `TranslationManager`.

`TranslationManager` è composto da mixin focalizzati per tipo di file:

- `ProjectMarkdownTranslationMixin` gestisce la lettura dei file Markdown, la traduzione dei contenuti, la riscrittura dei percorsi, i metadati, le avvertenze e le scritture.
- `ProjectNotebookTranslationMixin` gestisce la lettura dei file notebook, la traduzione delle celle Markdown, la riscrittura dei percorsi, i metadati, le avvertenze e le scritture.
- `ProjectImageTranslationMixin` gestisce la scoperta delle immagini, l'estrazione/traduzione del testo, la scrittura di immagini renderizzate e i metadati.

Le API di contenuto di livello inferiore saltano il flusso di lavoro del progetto:

1. `translate_markdown_content` and `translate_notebook_content` translate in-memory content only.
2. `translate_image_content` translates text in a single image and returns a rendered image object.
3. `rewrite_markdown_paths` and `rewrite_notebook_paths` are explicit post-processing helpers. They perform no translation and no project writes.

## Flusso di revisione

Il flusso di revisione deterministico è:

1. Analizza gli argomenti della CLI o i parametri dell'API.
2. Normalizza i codici lingua richiesti.
3. Costruisci uno o più target di revisione da `root_dir`, `root_dirs` o `groups`.
4. Facoltativamente limita i file sorgente con `--changed-from`.
5. Esegui controlli deterministici per struttura, freschezza della traduzione, integrità del Markdown e percorsi di link/immagini locali.
6. Stampa output di testo o Markdown in stile GitHub.
7. Termina con un errore quando vengono trovati errori di revisione.

Il flusso di revisione non richiede chiavi API e dovrebbe rimanere adatto per la CI delle pull request. Il workflow delle pull request scrive un riepilogo dei controlli ad ogni esecuzione e pubblica un commento sulla PR solo quando `co-op-review` fallisce.

## Sito della documentazione

Il sito della documentazione è configurato da:

```text
mkdocs.yml
requirements-docs.txt
docs/
```

La directory `docs/` è la fonte canonica della documentazione. Non aggiungere nuove guide per l'utente finale al di fuori di questa directory a meno che il progetto non introduca intenzionalmente un'altra superficie di documentazione pubblicata.

Build locally:

```bash
python -m pip install -r requirements-docs.txt
python -m mkdocs build --strict
```

Preview locally:

```bash
python -m mkdocs serve
```

Il sito generato viene scritto in `site/`, che è ignorata da git.

## Workflow di GitHub Pages

`.github/workflows/docs.yml` compila il sito sulle pull request e lo distribuisce sui push verso `main`.

Il workflow installa:

```bash
pip install -r requirements-docs.txt
```

Il workflow della documentazione installa solo la toolchain della documentazione. `mkdocs.yml` indirizza `mkdocstrings` verso `src/` in modo che le pagine dell'API pubblica possano essere generate dall'albero dei sorgenti senza installare l'intero insieme di dipendenze di runtime. Se le future documentazioni dell'API richiedono l'importazione di provider di runtime opzionali durante la build, aggiorna sia `.github/workflows/docs.yml` sia questa guida insieme.

## Standard di qualità della documentazione

Prima di unire le modifiche alla documentazione, esegui:

```bash
python -m mkdocs build --strict
git diff --check
```

Usa build rigorose in modo che link rotti, voci di navigazione invalide e problemi di rendering delle API falliscano presto.