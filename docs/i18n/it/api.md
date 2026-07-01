# API Python

L'API Python pubblica e stabile è esportata da `co_op_translator.api`. La maggior parte delle integrazioni usa uno di questi flussi di lavoro:

| Scenario | Usalo quando | API principali |
| --- | --- | --- |
| Translate individual files or documents | La tua applicazione legge il contenuto sorgente, chiama Co-op Translator per la traduzione e decide dove salvare il risultato. | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Prepare content for host-agent translation | Il tuo host MCP o il modello dell'applicazione tradurrà i frammenti, mentre Co-op Translator gestisce il frazionamento e la ricostruzione. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Translate an entire repository | Vuoi che l'API Python si comporti come la CLI e gestisca la scoperta, i percorsi di output, i metadati, la pulizia e le scritture. | `run_translation` |

La maggior parte dei moduli a basso livello sotto `core`, `config`, `review` e `utils` sono dettagli di implementazione utilizzati da questi punti di ingresso dell'API.

I client MCP usano la stessa API pubblica tramite il [Server MCP](mcp.md). Usa questa pagina quando chiami Python direttamente, e la guida MCP quando esponi Co-op Translator a un agente o editor. Se stai decidendo tra CLI, API Python e MCP, inizia con [Scegli il flusso di lavoro](workflows.md).

## Flusso iniziale per l'API

Inizia qui se chiami Co-op Translator dal codice Python:

1. Configura un provider LLM come descritto in [Configurazione](configuration.md), a meno che tu non stia solo preparando frammenti di Markdown o notebook per la traduzione da parte dell'host-agent.
2. Decidi se la tua applicazione gestisce l'I/O dei file.
3. Usa le API di contenuto quando la tua applicazione legge e scrive file individuali.
4. Usa `run_translation` quando Co-op Translator deve processare un repository come la CLI.
5. Usa `run_review` dopo la traduzione se hai bisogno di controlli deterministici nell'automazione.

| Obiettivo | API da cui iniziare |
| --- | --- |
| Translate one Markdown string or file | `translate_markdown_content` |
| Translate one notebook payload | `translate_notebook_content` |
| Translate one image | `translate_image_content` |
| Let a host agent translate Markdown or notebook chunks | `start_markdown_agent_translation` or `start_notebook_agent_translation` |
| Rewrite translated links after choosing an output path | `rewrite_markdown_paths` or `rewrite_notebook_paths` |
| Translate a full repository | `run_translation` |
| Review translated output | `run_review` |

## Scenario 1: Translate Individual Files or Documents

Usa questo flusso di lavoro quando hai già un file, un buffer dell'editor, un payload di notebook, una richiesta MCP o un input di pipeline personalizzato. Il tuo codice si occupa dell'I/O dei file:

1. Leggi il contenuto sorgente.
2. Chiama un'API di traduzione del contenuto.
3. Facoltativamente chiama un'API di riscrittura dei percorsi se il contenuto tradotto verrà scritto in una cartella di traduzione del progetto.
4. Salva o restituisci il risultato dalla tua applicazione.

Le API di traduzione del contenuto non eseguono la scoperta del progetto, non scrivono metadati, non aggiungono avvisi e non riscrivono i link automaticamente.

### File Markdown

```python
import asyncio
from pathlib import Path

from co_op_translator.api import (
    rewrite_markdown_paths,
    translate_markdown_content,
)


async def main() -> None:
    source_path = Path("docs/guide.md")
    target_path = Path("translations/ko/docs/guide.md")

    translated = await translate_markdown_content(
        source_path.read_text(encoding="utf-8"),
        "ko",
        {"source_path": source_path},
    )

    rewritten = rewrite_markdown_paths(
        translated,
        source_path=source_path,
        target_path=target_path,
        policy={
            "language_code": "ko",
            "root_dir": ".",
            "translations_dir": "translations",
            "translated_images_dir": "translated_images",
            "translation_types": ["markdown", "images"],
        },
    )

    target_path.parent.mkdir(parents=True, exist_ok=True)
    target_path.write_text(rewritten, encoding="utf-8")


asyncio.run(main())
```

Se il Markdown tradotto non risiederà in una struttura di progetto Co-op Translator, salta `rewrite_markdown_paths` e salva direttamente la stringa tradotta.

### File Notebook

```python
import asyncio
from pathlib import Path

from co_op_translator.api import (
    rewrite_notebook_paths,
    translate_notebook_content,
)


async def main() -> None:
    source_path = Path("docs/tutorial.ipynb")
    target_path = Path("translations/ja/docs/tutorial.ipynb")

    translated_json = await translate_notebook_content(
        source_path.read_text(encoding="utf-8"),
        "ja",
        {"source_path": source_path},
    )

    rewritten_json = rewrite_notebook_paths(
        translated_json,
        source_path=source_path,
        target_path=target_path,
        policy={
            "language_code": "ja",
            "root_dir": ".",
            "translations_dir": "translations",
            "translated_images_dir": "translated_images",
            "translation_types": ["notebook", "images"],
        },
    )

    target_path.parent.mkdir(parents=True, exist_ok=True)
    target_path.write_text(rewritten_json, encoding="utf-8")


asyncio.run(main())
```

`translate_notebook_content` traduce le celle Markdown e preserva le celle non Markdown. La riscrittura dei percorsi viene applicata solo alle celle Markdown.

### File immagine

```python
from pathlib import Path

from co_op_translator.api import translate_image_content

source_path = Path("docs/images/hero.png")
target_path = Path("translated_images/fr/hero.png")

translated_image = translate_image_content(
    source_path,
    "fr",
    {
        "root_dir": ".",
        "fast_mode": False,
    },
)

target_path.parent.mkdir(parents=True, exist_ok=True)
translated_image.save(target_path)
```

`translate_image_content` legge l'immagine sorgente e restituisce un `PIL.Image.Image` renderizzato. Non scrive i metadati dell'immagine tradotta.

## Scenario 2: Translate an Entire Repository

Usa questo flusso di lavoro quando vuoi che l'API Python si comporti come la CLI `translate`. `run_translation` scopre i file supportati, traduce i tipi di contenuto selezionati, riscrive i percorsi, scrive i file di output, aggiorna i metadati ed esegue attività di manutenzione della traduzione come la pulizia.

`run_translation` è il punto di ingresso preferito per l'orchestrazione del progetto. `translate_project` è esportato come alias di compatibilità con lo stesso comportamento.

Translate Markdown files in the current repository into Korean and Japanese:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    markdown=True,
)
```

Translate only notebooks from a specific project root:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="fr",
    root_dir="./my-course",
    notebook=True,
)
```

Preview translation volume without writing files:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="es de",
    root_dir="./my-course",
    markdown=True,
    dry_run=True,
)
```

Translate multiple content roots in one call:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    root_dirs=["./docs", "./labs"],
)
```

Write translations into explicit output groups:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ja",
    markdown=True,
    groups=[
        ("./course-a", "./localized/course-a"),
        ("./course-b", "./localized/course-b"),
    ],
)
```

Use a per-language placeholder when each language should contain a nested subdirectory:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    groups=[
        ("./course", "./translations/<lang>/course"),
    ],
)
```

If none of `markdown`, `notebook`, or `images` are set, the API translates all supported types: Markdown, notebooks, and images.

## Revisione dell'output tradotto

`run_review` esegue controlli di traduzione deterministici senza credenziali LLM o Vision.

!!! note "Beta"
    `run_review` è un'API beta di revisione deterministica. Non chiama provider di modelli né scrive file, ma gli schemi dei controlli e dei problemi potrebbero evolvere.

```python
from co_op_translator.api import run_review

run_review(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
)
```

Review only files changed against a base ref and print GitHub-flavored output:

```python
from co_op_translator.api import run_review

run_review(
    language_codes="ko",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
    changed_from="origin/main",
    output_format="github",
)
```

## Esempi di API da copiare e incollare

Translate Markdown content without file writes:

```python
import asyncio

from co_op_translator.api import translate_markdown_content


async def main() -> None:
    translated = await translate_markdown_content(
        "# Hello\n\nWelcome to the course.",
        "ko",
    )
    print(translated)


asyncio.run(main())
```

Translate and rewrite Markdown links:

```python
import asyncio

from co_op_translator.api import rewrite_markdown_paths, translate_markdown_content


async def main() -> None:
    translated = await translate_markdown_content(
        "[Setup](../setup.md)\n\n![Hero](../../images/hero.png)",
        "ko",
        {"source_path": "docs/guide.md"},
    )
    rewritten = rewrite_markdown_paths(
        translated,
        source_path="docs/guide.md",
        target_path="translations/ko/docs/guide.md",
        policy={
            "language_code": "ko",
            "root_dir": ".",
            "translations_dir": "translations",
            "translated_images_dir": "translated_images",
            "translation_types": ["markdown", "images"],
        },
    )
    print(rewritten)


asyncio.run(main())
```

Translate a repository from Python:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    root_dir="./course",
    markdown=True,
    yes=True,
)
```

Translate multiple roots:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    root_dirs=[
        "./docs",
        "./labs",
    ],
)
```

Preserve glossary terms:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="fr",
    markdown=True,
    glossaries=[
        "Co-op Translator",
        "Azure AI Foundry",
        "GitHub Actions",
    ],
)
```

## Punti di ingresso pubblici

```python
from co_op_translator.api import (
    ImageTranslationOptions,
    MarkdownTranslationOptions,
    NotebookTranslationOptions,
    finish_markdown_agent_translation,
    finish_notebook_agent_translation,
    run_review,
    run_translation,
    rewrite_markdown_paths,
    rewrite_notebook_paths,
    start_markdown_agent_translation,
    start_notebook_agent_translation,
    translate_image_content,
    translate_markdown_content,
    translate_notebook_content,
    translate_project,
)
```

::: co_op_translator.api.translate_markdown_content

::: co_op_translator.api.translate_notebook_content

::: co_op_translator.api.translate_image_content

::: co_op_translator.api.start_markdown_agent_translation

::: co_op_translator.api.finish_markdown_agent_translation

::: co_op_translator.api.start_notebook_agent_translation

::: co_op_translator.api.finish_notebook_agent_translation

::: co_op_translator.api.rewrite_markdown_paths

::: co_op_translator.api.rewrite_notebook_paths

::: co_op_translator.api.MarkdownTranslationOptions

::: co_op_translator.api.NotebookTranslationOptions

::: co_op_translator.api.ImageTranslationOptions

::: co_op_translator.api.run_translation

::: co_op_translator.api.translate_project

::: co_op_translator.api.run_review

## API di traduzione del contenuto

Le API di traduzione del contenuto sono destinate a integrazioni che hanno già il contenuto in memoria, come un'estensione dell'editor, uno strumento MCP, un processore di notebook o una pipeline personalizzata.

| Funzione | Input | Output | I/O file | Note |
| --- | --- | --- | --- | --- |
| `translate_markdown_content` | Markdown `str` | Markdown `str` | No | Async. Traduce solo contenuto Markdown. Non riscrive link, non scrive metadati e non aggiunge avvisi. |
| `translate_notebook_content` | Notebook JSON `str` or `dict` | Notebook JSON `str` | No | Async. Traduce le celle Markdown e preserva le celle non Markdown. Non riscrive link, non scrive metadati e non aggiunge avvisi. |
| `translate_image_content` | Image path | `PIL.Image.Image` | Reads source image only | Sincrono. Estrae e traduce il testo dell'immagine, poi restituisce un'immagine renderizzata. Non salva i metadati dell'immagine tradotta. |

`translate_markdown_content` e `translate_notebook_content` accettano un opzionale `source_path` tramite le loro opzioni. Il percorso viene passato come contesto al traduttore; i chiamanti rimangono responsabili di qualsiasi riscrittura dei percorsi specifica del progetto dopo la traduzione.

```python
from co_op_translator.api import MarkdownTranslationOptions, translate_markdown_content

translated = await translate_markdown_content(
    document,
    "ko",
    MarkdownTranslationOptions(source_path="docs/guide.md"),
)
```

Le stesse opzioni possono essere passate come dizionari:

```python
translated = await translate_markdown_content(
    document,
    "ko",
    {"source_path": "docs/guide.md"},
)
```

## API di traduzione assistita da agente

Le API assistite da agente non chiamano Azure OpenAI o OpenAI da Co-op Translator. Preparano frammenti di Markdown o notebook per la traduzione da parte dell'host agent, quindi ricostruiscono il contenuto finale dai frammenti tradotti.

| Funzione | Scopo |
| --- | --- |
| `start_markdown_agent_translation` | Restituisce un lavoro Markdown autonomo con frammenti, prompt e stato di ricostruzione. |
| `finish_markdown_agent_translation` | Ricostruisce Markdown da un lavoro e dai frammenti tradotti dall'host-agent. |
| `start_notebook_agent_translation` | Restituisce un lavoro notebook con frammenti di celle Markdown per la traduzione da parte dell'host-agent. |
| `finish_notebook_agent_translation` | Ricostruisce il JSON del notebook preservando le celle di codice, le output e i metadati. |

Questo flusso di lavoro è destinato principalmente agli host MCP. Se hai bisogno di traduzione di repository in produzione con Co-op Translator che gestisce le chiamate ai provider, usa `translate_markdown_content`, `translate_notebook_content` o `run_translation`.

## API per la riscrittura dei percorsi

Le API per la riscrittura dei percorsi non eseguono traduzioni. Aggiornano i link e i percorsi del frontmatter dopo che i chiamanti conoscono il percorso sorgente, il percorso di destinazione tradotto e la struttura del progetto.

| Funzione | Ambito | Note |
| --- | --- | --- |
| `rewrite_markdown_paths` | Corpo Markdown e frontmatter | Riscrive i link Markdown e i campi di percorso del frontmatter supportati per una destinazione tradotta. |
| `rewrite_notebook_paths` | Celle Markdown nel JSON del notebook | Applica la riscrittura dei percorsi Markdown a ogni cella Markdown e lascia invariate le celle non Markdown. |

L'argomento `policy` può essere un dizionario con questi campi:

| Campo | Obbligatorio | Scopo |
| --- | --- | --- |
| `language_code` | Yes | Codice lingua di destinazione, come `"ko"` o `"pt-BR"`. |
| `root_dir` | No | Radice del progetto sorgente. Predefinito a `"."`. |
| `translations_dir` | No | Directory di output per le traduzioni testuali. Predefinita `translations` sotto `root_dir`. |
| `translated_images_dir` | No | Directory di output per le immagini tradotte. Predefinita `translated_images` sotto `root_dir`. |
| `translation_types` | No | Tipi di traduzione abilitati. Predefinito a Markdown, notebook e immagini. |
| `lang_subdir` | No | Sottodirectory opzionale sotto ogni cartella di lingua. |

## Parametri di traduzione del progetto

| Parametro | Tipo | Predefinito | Scopo |
| --- | --- | --- | --- |
| `language_codes` | `str` | Required | Codici lingua di destinazione separati da spazi, come `"ko ja fr"`, oppure `"all"`. I codici alias sono normalizzati ai valori canonici BCP 47. |
| `root_dir` | `str` | `"."` | Radice del progetto per un singolo target di traduzione. Ignorato quando `root_dirs` o `groups` sono forniti. |
| `update` | `bool` | `False` | Elimina e ricrea le traduzioni esistenti per le lingue selezionate. |
| `images` | `bool` | `False` | Includi la traduzione delle immagini. Richiede la configurazione di Azure AI Vision. |
| `markdown` | `bool` | `False` | Includi la traduzione di Markdown. |
| `notebook` | `bool` | `False` | Includi la traduzione di notebook Jupyter. |
| `debug` | `bool` | `False` | Abilita il logging di debug. |
| `save_logs` | `bool` | `False` | Salva file di log di livello DEBUG sotto la directory root `logs/`. |
| `yes` | `bool` | `True` | Conferma automaticamente i prompt per l'uso programmatico e in CI. |
| `add_disclaimer` | `bool` | `False` | Aggiungi disclaimer di traduzione automatica a Markdown e notebook tradotti. |
| `translations_dir` | `str \| None` | `None` | Directory di output personalizzata per le traduzioni di testo. I percorsi relativi si risolvono rispetto a ciascuna root. |
| `image_dir` | `str \| None` | `None` | Directory di output personalizzata per le immagini tradotte. I percorsi relativi si risolvono rispetto a ciascuna root. |
| `root_dirs` | `Iterable[str] \| None` | `None` | Più root che condividono le stesse impostazioni di output. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | Coppie esplicite `(root_dir, translations_dir)`. Ha precedenza su `root_dirs`. |
| `repo_url` | `str \| None` | `None` | URL del repository usato per il rendering della tabella delle lingue nel README. |
| `glossaries` | `Iterable[str] \| None` | `None` | Termini di glossario da preservare durante la traduzione. I duplicati e i termini vuoti vengono normalizzati. |
| `dry_run` | `bool` | `False` | Stima il volume di traduzione e anteprima il comportamento della migrazione senza scrivere file. |

## Parametri di revisione

`run_review` rispecchia intenzionalmente la firma di `run_translation` dove possibile in modo che l'automazione possa passare tra i flussi di lavoro di traduzione e revisione con una ramificazione minima.

| Parametro | Tipo | Predefinito | Scopo |
| --- | --- | --- | --- |
| `language_codes` | `str \| Iterable[str]` | `"all"` | Cartelle lingua di destinazione da revisionare. Sono accettate stringhe separate da spazi e iterabili. `"all"` revisiona tutte le lingue di traduzione scoperte. |
| `root_dir` | `str` | `"."` | Radice del progetto per un singolo target di revisione. Ignorato quando `root_dirs` o `groups` sono forniti. |
| `markdown` | `bool` | `False` | Includi file sorgente Markdown e MDX. |
| `notebook` | `bool` | `False` | Includi file sorgente Jupyter notebook. |
| `images` | `bool` | `False` | Riservato per parità con le opzioni di traduzione. I riferimenti ai link delle immagini vengono controllati dal Markdown. |
| `translations_dir` | `str \| None` | `None` | Directory di output per le traduzioni di testo personalizzate. I percorsi relativi vengono risolti rispetto a ciascuna root. |
| `root_dirs` | `Iterable[str] \| None` | `None` | Più root che condividono le stesse impostazioni di output. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | Coppie esplicite `(root_dir, translations_dir)`. Ha precedenza su `root_dirs`. |
| `changed_from` | `str \| None` | `None` | Riferimento Git utilizzato per limitare la revisione ai file sorgente modificati. |
| `output_format` | `str` | `"text"` | Formato di output della revisione. Valori supportati: `"text"` e `"github"`. |
| `fail_on_warnings` | `bool` | `False` | Tratta gli avvertimenti come fallimenti oltre agli errori. |
| `debug` | `bool` | `False` | Abilita il logging di debug. |
| `save_logs` | `bool` | `False` | Salva i file di log a livello DEBUG nella directory root `logs/`. |

If none of `markdown`, `notebook`, or `images` are set, the API reviews Markdown, notebooks, and image link references where applicable. Review does not call an LLM provider and does not require API keys.

## Requisiti di configurazione

Le API di traduzione che richiedono provider necessitano della configurazione del provider prima di tradurre:

- La traduzione di Markdown e notebook richiede un provider LLM. Configurare Azure OpenAI o OpenAI.
- La traduzione delle immagini richiede Azure AI Vision oltre al provider LLM.
- `run_translation` esegue controlli di connettività leggeri prima che inizi la traduzione del progetto.
- Le API assistite da agenti `start_*_agent_translation` e `finish_*_agent_translation` non chiamano i provider LLM di Co-op Translator. L'applicazione host o l'agente MCP traduce i chunk preparati.
- `rewrite_markdown_paths`, `rewrite_notebook_paths`, and `run_review` sono deterministici e non richiedono credenziali del provider.

Variabili richieste per Azure OpenAI:

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Variabili richieste per OpenAI:

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

Variabili richieste per Azure AI Vision per la traduzione delle immagini:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

`run_review` è deterministico e non richiede la configurazione di Azure OpenAI, OpenAI o Azure AI Vision.

## Note sul comportamento

- Le API di traduzione dei contenuti separano la traduzione dalla riscrittura dei percorsi del progetto. Chiamare esplicitamente `rewrite_markdown_paths` o `rewrite_notebook_paths` quando il contenuto tradotto necessita che i link relativi al progetto siano adeguati per una destinazione specifica.
- Le API di orchestrazione del progetto aggiungono comportamenti di progetto attorno alla traduzione dei contenuti, inclusi rilevamento dei file, scritture, riscrittura dei percorsi, metadati, pulizia e disclaimer opzionali.
- `run_translation` stampa riepiloghi di avanzamento e stime tramite Click, corrispondenti all'esperienza utente CLI.
- `dry_run=True` calcola le stime usando aggiornamenti virtuali del README, ma non scrive il README né i file di traduzione.
- `groups` vengono processati sequenzialmente. Viene stampata una singola stima aggregata prima dell'inizio dei lavori.
- Quando è selezionata la traduzione delle immagini, la mancanza della configurazione Vision genera un errore prima dell'avvio della traduzione.
- Le cartelle di lingua esistenti basate su alias vengono rilevate e possono essere migrate a nomi di cartelle di lingua canonici come parte dell'esecuzione.
- `run_review` fallisce in caso di file tradotti mancanti, metadati di traduzione mancanti o obsoleti, frontmatter/recinzioni di codice Markdown malformati e JSON di notebook tradotti non valido.
- `run_review` segnala come avvertimenti, per impostazione predefinita, i target locali di link Markdown e immagini mancanti.

## Percorso di chiamata interno

L'API delega alla stessa implementazione core utilizzata dalla CLI:

Traduzione:

1. `co_op_translator.api.translation.translate_markdown_content`, `translate_notebook_content`, or `translate_image_content` per la traduzione in memoria.
2. `co_op_translator.api.translation.rewrite_markdown_paths` or `rewrite_notebook_paths` per il post-processing esplicito dei percorsi.
3. `co_op_translator.api.translation.run_translation` per l'orchestrazione completa del progetto.
4. `co_op_translator.config.Config`, `LLMConfig`, and `VisionConfig`.
5. `co_op_translator.core.project.ProjectTranslator`.
6. `co_op_translator.core.project.TranslationManager`.
7. Mixin di traduzione del progetto focalizzati per Markdown, notebook e immagini.
8. Traduttori di Markdown, notebook, testo e immagini sotto `co_op_translator.core`.

Revisione:

1. `co_op_translator.api.review.run_review`
2. `co_op_translator.review.targets.build_review_targets`
3. `co_op_translator.review.runner.ReviewRunner`
4. Controlli deterministici sotto `co_op_translator.review.checks`

Le seguenti classi sono utili per i manutentori, ma non sono esportate come API stabile a livello di package.

| Classe | Modulo | Responsabilità |
| --- | --- | --- |
| `ProjectTranslator` | `co_op_translator.core.project.project_translator` | Coordina la traduzione a livello di progetto, la gestione delle directory, la normalizzazione dei metadati per lingua e la delega ai traduttori per Markdown, notebook e immagini. |
| `TranslationManager` | `co_op_translator.core.project.translation` | Esegue il lavoro di elaborazione file asincrona per Markdown, notebook, immagini, rilevamento di contenuti obsoleti e aggiornamenti dei metadati di traduzione. |
| `ProjectMarkdownTranslationMixin` | `co_op_translator.core.project.translation.project_markdown_translation` | Orchestra la lettura dei file Markdown, la traduzione dei contenuti, la riscrittura dei percorsi, i metadati, i disclaimer e le scritture. |
| `ProjectNotebookTranslationMixin` | `co_op_translator.core.project.translation.project_notebook_translation` | Orchestra la lettura dei file notebook, la traduzione delle celle Markdown, la riscrittura dei percorsi, i metadati, i disclaimer e le scritture. |
| `ProjectImageTranslationMixin` | `co_op_translator.core.project.translation.project_image_translation` | Orchestra la scoperta delle immagini sorgente, la traduzione delle immagini, i percorsi di output, i metadati e le scritture. |
| `ProjectEvaluator` | `co_op_translator.core.project.project_evaluator` | Trova coppie Markdown tradotte, valuta la qualità della traduzione e legge i metadati di confidenza per workflow di riparazione a bassa confidenza. |
| `ReviewRunner` | `co_op_translator.review.runner` | Coordina controlli deterministici di revisione su file sorgente, lingue target e root di traduzione configurate. |
| `ReviewTarget` | `co_op_translator.review.targets` | Descrive una root sorgente e la directory di output di traduzione rivista per quella root. |
| `LanguageFolderMigrator` | `co_op_translator.core.project.language_migrator` | Rileva cartelle di lingua legacy basate su alias e prepara piani di migrazione verso nomi canonici di cartelle BCP 47. |
| `Config` | `co_op_translator.config.base_config` | Carica file `.env` e verifica se i provider LLM richiesti e, opzionalmente, Vision sono configurati. |
| `LLMConfig` | `co_op_translator.config.llm_config.config` | Rileva automaticamente Azure OpenAI o OpenAI, valida le variabili d'ambiente richieste ed esegue controlli di connettività del provider. |
| `VisionConfig` | `co_op_translator.config.vision_config.config` | Rileva la configurazione di Azure AI Vision ed esegue controlli di connettività per la traduzione delle immagini. |