# API Python

L'API Python pubblica stabile è esportata da `co_op_translator.api`. La maggior parte delle integrazioni usa uno di questi flussi di lavoro:

| Scenario | Usalo quando | API principali |
| --- | --- | --- |
| Translate individual files or documents | La tua applicazione legge il contenuto sorgente, chiama Co-op Translator per la traduzione e decide dove salvare il risultato. | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Prepara contenuti per la traduzione host-agent | Il tuo host MCP o modello dell'applicazione tradurrà i chunk, mentre Co-op Translator gestisce il chunking e la ricostruzione. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Translate an entire repository | Vuoi che l'API Python si comporti come la CLI e gestisca la scoperta, i percorsi di output, i metadati, la pulizia e le scritture. | `run_translation` |

La maggior parte dei moduli di basso livello sotto `core`, `config`, `review` e `utils` sono dettagli di implementazione utilizzati da questi punti di ingresso dell'API.

I client MCP usano la stessa API pubblica tramite il [MCP Server](mcp.md). Usa questa pagina quando chiami Python direttamente, e la guida MCP quando esponi Co-op Translator a un agente o a un editor. Se stai decidendo tra CLI, API Python e MCP, inizia con [Scegli il tuo flusso di lavoro](workflows.md).

## Flusso iniziale dell'API

Inizia qui se stai chiamando Co-op Translator da codice Python:

1. Configura un provider LLM come descritto in [Configurazione](configuration.md), a meno che tu non stia solo preparando chunk Markdown o di notebook per la traduzione da parte di un host-agent.
2. Decidi se la tua applicazione gestisce l'I/O dei file.
3. Usa le API di contenuto quando la tua applicazione legge e scrive file individuali.
4. Usa `run_translation` quando Co-op Translator deve elaborare un repository come la CLI.
5. Usa `run_review` dopo la traduzione se hai bisogno di controlli deterministici nell'automazione.

| Goal | API to start with |
| --- | --- |
| Traduci una stringa o un file Markdown | `translate_markdown_content` |
| Translate one notebook payload | `translate_notebook_content` |
| Translate one image | `translate_image_content` |
| Consenti a un host agent di tradurre i chunk di Markdown o dei notebook | `start_markdown_agent_translation` o `start_notebook_agent_translation` |
| Riscrivi i link tradotti dopo aver scelto un percorso di output | `rewrite_markdown_paths` o `rewrite_notebook_paths` |
| Translate a full repository | `run_translation` |
| Review translated output | `run_review` |

## Scenario 1: Tradurre file o documenti individuali

Usa questo flusso di lavoro quando hai già un file, un buffer dell'editor, un payload di notebook, una richiesta MCP o un input di pipeline personalizzato. Il tuo codice gestisce l'I/O dei file:

1. Leggi il contenuto sorgente.
2. Chiama un'API di traduzione del contenuto.
3. Eventualmente chiama un'API di riscrittura dei percorsi se il contenuto tradotto verrà scritto in una cartella di traduzione del progetto.
4. Salva o restituisci il risultato dalla tua applicazione.

Le API di traduzione del contenuto non eseguono la scoperta del progetto, non scrivono metadati, non aggiungono disclaimer e non riscrivono i link automaticamente.

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

Se il Markdown tradotto non vivrà in una struttura di progetto di Co-op Translator, salta `rewrite_markdown_paths` e salva direttamente la stringa tradotta.

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

`translate_notebook_content` traduce le celle Markdown e preserva le celle non-Markdown. La riscrittura dei percorsi si applica solo alle celle Markdown.

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

`translate_image_content` legge l'immagine sorgente e restituisce un `PIL.Image.Image` renderizzato. Non scrive metadati dell'immagine tradotta.

## Scenario 2: Tradurre un intero repository

Usa questo flusso di lavoro quando vuoi che l'API Python si comporti come la CLI `translate`. `run_translation` scopre i file supportati, traduce i tipi di contenuto selezionati, riscrive i percorsi, scrive i file di output, aggiorna i metadati ed esegue attività di manutenzione della traduzione come la pulizia.

`run_translation` è il punto di ingresso preferito per l'orchestrazione del progetto. `translate_project` è esportato come alias di compatibilità con lo stesso comportamento.

Traduci i file Markdown nel repository corrente in coreano e giapponese:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    markdown=True,
)
```

Traduci solo i notebook da una root del progetto specifica:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="fr",
    root_dir="./my-course",
    notebook=True,
)
```

Anteprima del volume di traduzione senza scrivere file:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="es de",
    root_dir="./my-course",
    markdown=True,
    dry_run=True,
)
```

Registra eventi di progresso strutturati per un'integrazione:

```python
from co_op_translator.api import TranslationEvent, run_translation


def on_event(event: TranslationEvent) -> None:
    payload = event.to_dict()
    # Archivia il payload nella tabella job-event o trasmettilo in streaming alla tua interfaccia utente.


run_translation(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
    progress_callback=on_event,
)
```

Gli eventi usano lo schema versionato `co-op.translation.event.v1`. Le integrazioni dovrebbero
fare affidamento su campi stabili come `type` e `stage_key`, non sul testo rivolto all'utente
della console o su `stage_label`.

Traduci più root di contenuto in una sola chiamata:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    root_dirs=["./docs", "./labs"],
)
```

Scrivi le traduzioni in gruppi di output espliciti:

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

Usa un placeholder per lingua quando ogni lingua dovrebbe contenere una sottodirectory annidata:

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

Se nessuno di `markdown`, `notebook` o `images` è impostato, l'API traduce tutti i tipi supportati: Markdown, notebook e immagini.

### Conservare le modifiche umane accettate con un provider di stato di traduzione

Per impostazione predefinita, Co-op Translator mantiene il comportamento esistente a livello di file: quando un
sorgente Markdown è obsoleta, l'intero file tradotto viene rigenerato. Le integrazioni ospitate
possono opzionalmente passare un `TranslationStateProvider` per preservare le modifiche umane
nelle porzioni di origine che non sono cambiate.

Il provider fornisce l'ultima coppia sorgente/target accettata e registra ogni nuovo
candidato. L'accettazione rimane responsabilità dell'integrazione—per esempio,
dopo che una pull request di traduzione è stata unita:

```python
from pathlib import Path

from co_op_translator.api import (
    TranslationBaseline,
    TranslationUpdate,
    run_translation,
)


class DatabaseTranslationState:
    def load_baseline(
        self,
        *,
        source_path: Path,
        translation_path: Path,
        language_code: str,
    ) -> TranslationBaseline | None:
        row = load_accepted_translation(
            source_path=source_path,
            translation_path=translation_path,
            language_code=language_code,
        )
        if row is None:
            return None
        return TranslationBaseline(
            source_text=row.source_text,
            target_text=row.target_text,
            revision=row.accepted_revision,
        )

    def record_candidate(
        self,
        *,
        source_path: Path,
        translation_path: Path,
        language_code: str,
        source_text: str,
        target_text: str,
        update: TranslationUpdate,
    ) -> None:
        save_translation_candidate(
            source_path=source_path,
            translation_path=translation_path,
            language_code=language_code,
            source_text=source_text,
            target_text=target_text,
            mode=update.mode,
            fallback_reason=update.fallback_reason,
        )


run_translation(
    language_codes="ko",
    root_dir="./course",
    markdown=True,
    translation_state_provider=DatabaseTranslationState(),
)
```

Per i file Markdown con una baseline accettata valida, Co-op Translator allinea
i blocchi Markdown di livello superiore. I blocchi sorgente invariati riutilizzano gli attuali blocchi tradotti
inclusi gli interventi manuali; i blocchi sorgente modificati o aggiunti vengono inviati
per la traduzione; i blocchi sorgente eliminati vengono rimossi. Se l'allineamento è ambiguo,
la struttura target è cambiata, una traduzione di blocco è invalida o non è disponibile una baseline,
Co-op Translator ricorre in modo sicuro al percorso esistente di traduzione dell'intero file.



segment translation memory. Si applica attualmente alla traduzione di progetti Markdown.
Il comportamento per notebook e immagini non cambia. Passare `update=True`
richiede comunque la rigenerazione completa.

Se uno o più file non possono essere tradotti, `run_translation` solleva un
`RuntimeError` dopo che il flusso di lavoro del progetto termina invece di riportare un
run riuscito con output mancante. Le integrazioni dovrebbero considerarlo come un lavoro fallito
e mantenere lo stato di traduzione accettato precedente.

## Revisionare l'output tradotto

`run_review` esegue controlli deterministici sulla traduzione senza credenziali LLM o Vision.

!!! note "Beta"
    `run_review` è un'API beta di revisione deterministica. Non chiama i provider di modelli né scrive file, ma gli schemi di controlli e issue possono evolvere.

```python
from co_op_translator.api import run_review

run_review(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
)
```

Dopo una traduzione solo del README, usa lo stesso ambito per la revisione:

```python
run_review(language_codes="ko", root_dir="./my-course", readme_only=True)
```

`readme_only=True` esamina solo `README.md` sotto ogni root di origine configurato,
inclusi `groups` personalizzati e le directory di output. Altri documenti e README
annidati sono esclusi. Un README sorgente mancante genera `ValueError`; controlli di traduzione falliti
generano `RuntimeError`.

Revisiona solo i file cambiati rispetto a un riferimento base e stampa output in stile GitHub:

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

## Esempi API da copiare e incollare

Traduci contenuto Markdown senza scrivere file:

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

Traduci e riscrivi i link Markdown:

```python
import asyncio

from co_op_translator.api import rewrite_markdown_paths, translate_markdown_content


async def main() -> None:
    translated = await translate_markdown_content(
        "[Setup](../setup.md)\n\n![Hero](images/hero.png)",
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

Traduci un repository da Python:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    root_dir="./course",
    markdown=True,
    yes=True,
)
```

Traduci più root:

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

Preserva i termini del glossario:

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
    TranslationBaseline,
    TranslationStateProvider,
    TranslationUpdate,
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

::: co_op_translator.api.TranslationBaseline

::: co_op_translator.api.TranslationStateProvider

::: co_op_translator.api.TranslationUpdate

::: co_op_translator.api.run_translation

::: co_op_translator.api.translate_project

::: co_op_translator.api.run_review

## API di traduzione del contenuto

Le API di traduzione del contenuto sono pensate per integrazioni che hanno già il contenuto in memoria, come un'estensione per editor, uno strumento MCP, un processore di notebook o una pipeline personalizzata.

| Funzione | Input | Output | I/O file | Note |
| --- | --- | --- | --- | --- |
| `translate_markdown_content` | Markdown `str` | Markdown `str` | No | Asincrono. Traduce solo contenuto Markdown. Non riscrive i link, non scrive metadati né aggiunge disclaimer. |
| `translate_notebook_content` | Notebook JSON `str` o `dict` | Notebook JSON `str` | No | Asincrono. Traduce le celle Markdown e preserva le celle non-Markdown. Non riscrive i link, non scrive metadati né aggiunge disclaimer. |
| `translate_image_content` | Percorso dell'immagine | `PIL.Image.Image` | Legge solo l'immagine sorgente | Sincrono. Estrae e traduce il testo dell'immagine, quindi restituisce un'immagine renderizzata. Non salva metadati dell'immagine tradotta. |

`translate_markdown_content` e `translate_notebook_content` accettano un opzionale `source_path` tramite le loro opzioni. Il percorso viene passato come contesto al traduttore; i chiamanti restano responsabili di qualsiasi riscrittura di percorsi specifica del progetto dopo la traduzione.

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

Le API assistite da agente non chiamano il provider LLM configurato da Co-op Translator. Preparano chunk Markdown o di notebook per la traduzione da parte di un host agent, quindi ricostruiscono il contenuto finale dai chunk tradotti.

| Funzione | Scopo |
| --- | --- |
| `start_markdown_agent_translation` | Restituisce un job Markdown autonomo con chunk, prompt e stato di ricostruzione. |
| `finish_markdown_agent_translation` | Ricostruisce Markdown da un job e dai chunk tradotti dall'host-agent. |
| `start_notebook_agent_translation` | Restituisce un job di notebook con chunk delle celle Markdown per la traduzione da parte dell'host-agent. |
| `finish_notebook_agent_translation` | Ricostruisce il JSON del notebook preservando le celle di codice, gli output e i metadati. |

Questo flusso è principalmente pensato per host MCP. Se hai bisogno di traduzione di repository in produzione con Co-op Translator che gestisce le chiamate ai provider, usa `translate_markdown_content`, `translate_notebook_content` o `run_translation`.

## API di riscrittura dei percorsi

Le API di riscrittura dei percorsi non eseguono traduzioni. Aggiornano link e percorsi nel frontmatter dopo che i chiamanti conoscono il percorso sorgente, il percorso target tradotto e la struttura del progetto.

| Funzione | Ambito | Note |
| --- | --- | --- |
| `rewrite_markdown_paths` | Corpo Markdown e frontmatter | Riscrive i link Markdown e i campi di percorso del frontmatter supportati per un target tradotto. |
| `rewrite_notebook_paths` | Celle Markdown nel JSON del notebook | Applica la riscrittura dei percorsi Markdown a ogni cella Markdown e lascia invariate le celle non-Markdown. |

L'argomento `policy` può essere un dizionario con questi campi:

| Campo | Obbligatorio | Scopo |
| --- | --- | --- |
| `language_code` | Sì | Codice lingua di destinazione, come `"ko"` o `"pt-BR"`. |
| `root_dir` | No | Root del progetto sorgente. Predefinito `"."`. |
| `translations_dir` | No | Directory di output per la traduzione del testo. Predefinita `translations` sotto `root_dir`. |
| `translated_images_dir` | No | Directory di output per le immagini tradotte. Predefinita `translated_images` sotto `root_dir`. |
| `translation_types` | No | Tipi di traduzione abilitati. Predefiniti Markdown, notebook e immagini. |
| `lang_subdir` | No | Sottodirectory opzionale sotto ogni cartella della lingua. |

## Parametri di traduzione del progetto

| Parametro | Tipo | Predefinito | Scopo |
| --- | --- | --- | --- |
| `language_codes` | `str` | Richiesto | Codici lingua di destinazione separati da spazi, come `"ko ja fr"`, o `"all"`. I codici alias sono normalizzati ai valori canonical BCP 47. |
| `root_dir` | `str` | `"."` | Root del progetto per un singolo target di traduzione. Ignorato quando `root_dirs` o `groups` sono forniti. |
| `update` | `bool` | `False` | Elimina e ricrea le traduzioni esistenti per le lingue selezionate. |
| `images` | `bool` | `False` | Include la traduzione delle immagini. Richiede la configurazione di Azure AI Vision. |
| `markdown` | `bool` | `False` | Include la traduzione Markdown. |
| `notebook` | `bool` | `False` | Include la traduzione dei notebook Jupyter. |
| `debug` | `bool` | `False` | Abilita il logging di debug. |
| `save_logs` | `bool` | `False` | Salva i file di log a livello DEBUG nella directory `logs/` della root. |
| `yes` | `bool` | `True` | Confermare automaticamente i prompt per l'uso programmatico e CI. |
| `add_disclaimer` | `bool` | `False` | Aggiungere avvisi di traduzione automatica ai Markdown e ai notebook tradotti. |
| `translations_dir` | `str \| None` | `None` | Directory di output personalizzata per le traduzioni di testo. I percorsi relativi vengono risolti rispetto a ciascuna root. |
| `image_dir` | `str \| None` | `None` | Directory di output personalizzata per le immagini tradotte. I percorsi relativi vengono risolti rispetto a ciascuna root. |
| `root_dirs` | `Iterable[str] \| None` | `None` | Più root che condividono le stesse impostazioni di output. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | Coppie esplicite `(root_dir, translations_dir)`. Ha precedenza su `root_dirs`. |
| `repo_url` | `str \| None` | `None` | URL del repository usato per generare la guida per la tabella delle lingue nel README. |
| `glossaries` | `Iterable[str] \| None` | `None` | Termini del glossario da preservare durante la traduzione. I duplicati e i termini vuoti vengono normalizzati. |
| `dry_run` | `bool` | `False` | Stimare il volume di traduzione e visualizzare in anteprima il comportamento di migrazione senza scrivere file. |
| `translation_state_provider` | `TranslationStateProvider \| None` | `None` | Adapter opzionale per la persistenza della baseline accettata e dei candidati per aggiornamenti incrementali dei Markdown. Ometterlo preserva il comportamento esistente a file intero. |

## Parametri di revisione

`run_review` rispecchia intenzionalmente la firma di `run_translation` dove possibile in modo che l'automazione possa passare tra i flussi di lavoro di traduzione e revisione con un branching minimo.

| Parametro | Tipo | Predefinito | Scopo |
| --- | --- | --- | --- |
| `language_codes` | `str \| Iterable[str]` | `"all"` | Cartelle delle lingue target da revisionare. Sono accettate stringhe separate da spazi e iterabili. `"all"` rivede ogni lingua di traduzione rilevata. |
| `root_dir` | `str` | `"."` | Root del progetto per un singolo obiettivo di revisione. Ignorato quando `root_dirs` o `groups` sono forniti. |
| `markdown` | `bool` | `False` | Includere file sorgente Markdown e MDX. |
| `notebook` | `bool` | `False` | Includere file sorgente dei notebook Jupyter. |
| `images` | `bool` | `False` | Riservato per parità con le opzioni di traduzione. I riferimenti ai link delle immagini vengono verificati dal Markdown. |
| `translations_dir` | `str \| None` | `None` | Directory di output personalizzata per le traduzioni di testo. I percorsi relativi vengono risolti rispetto a ciascuna root. |
| `root_dirs` | `Iterable[str] \| None` | `None` | Più root che condividono le stesse impostazioni di output. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | Coppie esplicite `(root_dir, translations_dir)`. Ha precedenza su `root_dirs`. |
| `changed_from` | `str \| None` | `None` | Ref Git usato per limitare la revisione ai file sorgente modificati. |
| `readme_only` | `bool` | `False` | Revisionare solo `README.md` sotto ogni source root. Un README sorgente mancante genera `ValueError`. |
| `output_format` | `str` | `"text"` | Formato di output della revisione. I valori supportati sono `"text"` e `"github"`. |
| `fail_on_warnings` | `bool` | `False` | Trattare gli avvisi come fallimenti oltre agli errori. |
| `debug` | `bool` | `False` | Abilitare il logging di debug. |
| `save_logs` | `bool` | `False` | Salvare file di log a livello DEBUG nella directory root `logs/`. |

Se nessuno tra `markdown`, `notebook` o `images` è impostato, l'API rivede Markdown, notebook e riferimenti ai link delle immagini dove applicabile. La revisione non chiama un provider LLM e non richiede chiavi API.

## Requisiti di configurazione

Le API di traduzione basate su provider richiedono la configurazione del provider prima di tradurre:

- La traduzione di Markdown e notebook richiede un provider LLM. Configurare Azure OpenAI, OpenAI o Anthropic.
- La traduzione delle immagini richiede Azure AI Vision oltre al provider LLM.
- `run_translation` esegue controlli di connettività leggeri prima dell'inizio della traduzione del progetto.
- Le API assistite da agent `start_*_agent_translation` e `finish_*_agent_translation` non chiamano i provider LLM di Co-op Translator. L'applicazione host o l'agente MCP traduce i chunk preparati.
- `rewrite_markdown_paths`, `rewrite_notebook_paths` e `run_review` sono deterministici e non richiedono credenziali del provider.

Variabili Azure OpenAI richieste:

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Variabili OpenAI richieste:

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

Variabili Anthropic richieste:

```bash
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

`ANTHROPIC_BASE_URL` and `ANTHROPIC_MAX_TOKENS` sono opzionali. Microsoft Agent Framework è il client modello predefinito per tutti i provider a partire da Co-op Translator 0.22.0. Semantic Kernel può ancora essere selezionato temporaneamente con `CO_OP_TRANSLATOR_MODEL_CLIENT="semantic-kernel"`, ma così facendo genera un avviso di deprecazione; vedi [configurazione](configuration.md#model-client-backend) per il piano di rimozione graduale.

Variabili Azure AI Vision richieste per la traduzione delle immagini:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

`run_review` è deterministico e non richiede configurazione LLM o Azure AI Vision.

## Note sul comportamento

- Le API di traduzione dei contenuti mantengono la traduzione separata dalla riscrittura dei percorsi del progetto. Chiamare esplicitamente `rewrite_markdown_paths` o `rewrite_notebook_paths` quando il contenuto tradotto necessita di adeguare i link relativi al progetto per una destinazione target.
- Le API di orchestrazione del progetto aggiungono comportamenti di progetto attorno alla traduzione dei contenuti, inclusi la scoperta dei file, le scritture, la riscrittura dei percorsi, i metadati, la pulizia e gli avvisi opzionali.
- `run_translation` stampa riepiloghi di avanzamento e stime attraverso lo stesso reporter basato su Rich usato dalla CLI. L'output non interattivo passa a testo semplice.
- `dry_run=True` calcola le stime usando aggiornamenti virtuali del README, ma non scrive il README né i file di traduzione.
- Le `groups` vengono processate sequenzialmente. Una singola stima aggregata viene stampata prima dell'inizio del lavoro.
- Quando è selezionata la traduzione delle immagini, la mancanza di configurazione Vision genera un errore prima dell'avvio della traduzione.
- Le cartelle di lingua esistenti basate su alias vengono rilevate e possono essere migrate a nomi di cartelle di lingua canonici come parte dell'esecuzione.
- `run_review` fallisce in caso di file tradotti mancanti, metadati di traduzione mancanti o obsoleti, frontmatter/fence di codice Markdown malformati e JSON di notebook tradotti non valido.
- `run_review` segnala come avvisi i target locali di link Markdown e immagini mancanti per impostazione predefinita.

## Percorso di chiamata interno

L'API delega alla stessa implementazione core usata dalla CLI:

Traduzione:

1. `co_op_translator.api.translation.translate_markdown_content`, `translate_notebook_content`, o `translate_image_content` per la traduzione in memoria.
2. `co_op_translator.api.translation.rewrite_markdown_paths` o `rewrite_notebook_paths` per il post-processing esplicito dei percorsi.
3. `co_op_translator.api.translation.run_translation` per l'orchestrazione completa del progetto.
4. `co_op_translator.config.Config`, `LLMConfig` e `VisionConfig`.
5. `co_op_translator.core.project.ProjectTranslator`.
6. `co_op_translator.core.project.TranslationManager`.
7. Mixin di traduzione del progetto focalizzati su Markdown, notebook e immagini.
8. Traduttori di Markdown, notebook, testo e immagini sotto `co_op_translator.core`.

Revisione:

1. `co_op_translator.api.review.run_review`
2. `co_op_translator.review.targets.build_review_targets`
3. `co_op_translator.review.runner.ReviewRunner`
4. Controlli deterministici sotto `co_op_translator.review.checks`

Le seguenti classi sono utili per i manutentori, ma non sono esportate come API stabile a livello di pacchetto.

| Classe | Modulo | Responsabilità |
| --- | --- | --- |
| `ProjectTranslator` | `co_op_translator.core.project.project_translator` | Coordina la traduzione a livello di progetto, la gestione delle directory, la normalizzazione dei metadati per lingua e la delega ai traduttori di Markdown, notebook e immagini. |
| `TranslationManager` | `co_op_translator.core.project.translation` | Esegue il lavoro asincrono di elaborazione dei file per Markdown, notebook, immagini, rilevamento di obsolescenza e aggiornamenti dei metadati di traduzione. |
| `ProjectMarkdownTranslationMixin` | `co_op_translator.core.project.translation.project_markdown_translation` | Orchestra la lettura dei file Markdown, la traduzione dei contenuti, la riscrittura dei percorsi, i metadati, gli avvisi e le scritture. |
| `ProjectNotebookTranslationMixin` | `co_op_translator.core.project.translation.project_notebook_translation` | Orchestra la lettura dei file notebook, la traduzione delle celle Markdown, la riscrittura dei percorsi, i metadati, gli avvisi e le scritture. |
| `ProjectImageTranslationMixin` | `co_op_translator.core.project.translation.project_image_translation` | Orchestra la scoperta delle immagini sorgente, la traduzione delle immagini, i percorsi di output, i metadati e le scritture. |
| `ProjectEvaluator` | `co_op_translator.core.project.project_evaluator` | Trova coppie di Markdown tradotte, valuta la qualità della traduzione e legge i metadati di confidenza per i flussi di lavoro di riparazione a bassa confidenza. |
| `ReviewRunner` | `co_op_translator.review.runner` | Coordina i controlli di revisione deterministici tra i file sorgente, le lingue target e le root di traduzione configurate. |
| `ReviewTarget` | `co_op_translator.review.targets` | Descrive una source root e la directory di output della traduzione rivista per quella root. |
| `LanguageFolderMigrator` | `co_op_translator.core.project.language_migrator` | Rileva cartelle di lingua alias legacy e prepara piani di migrazione a cartelle canoniche BCP 47. |
| `Config` | `co_op_translator.config.base_config` | Carica i file `.env` e verifica se i provider LLM richiesti e i provider Vision opzionali sono configurati. |
| `LLMConfig` | `co_op_translator.config.llm_config.config` | Rileva automaticamente Azure OpenAI, OpenAI o Anthropic, convalida le variabili d'ambiente richieste ed esegue controlli di connettività del provider. |
| `VisionConfig` | `co_op_translator.config.vision_config.config` | Rileva la configurazione Azure AI Vision ed esegue controlli di connettività per la traduzione delle immagini. |