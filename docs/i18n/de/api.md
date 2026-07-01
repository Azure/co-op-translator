# Python API

Die stabile öffentliche Python-API wird aus `co_op_translator.api` exportiert. Die meisten Integrationen verwenden einen der folgenden Workflows:

| Scenario | Use this when | Main APIs |
| --- | --- | --- |
| Translate individual files or documents | Your application reads source content, calls Co-op Translator for translation, and decides where to save the result. | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Prepare content for host-agent translation | Your MCP host or application model will translate chunks, while Co-op Translator handles chunking and reconstruction. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Translate an entire repository | You want the Python API to behave like the CLI and handle discovery, output paths, metadata, cleanup, and writes. | `run_translation` |

Die meisten niedrigeren Module unter `core`, `config`, `review` und `utils` sind Implementierungsdetails, die von diesen API-Einstiegspunkten verwendet werden.

MCP-Clients verwenden dieselbe öffentliche API über den [MCP Server](mcp.md). Verwenden Sie diese Seite, wenn Sie Python direkt aufrufen, und den MCP-Leitfaden, wenn Sie Co-op Translator einem Agenten oder Editor bereitstellen. Wenn Sie zwischen CLI, Python-API und MCP entscheiden, beginnen Sie mit [Wählen Sie Ihren Workflow](workflows.md).

## First-Time API Flow

Beginnen Sie hier, wenn Sie Co-op Translator aus Python-Code aufrufen:

1. Konfigurieren Sie einen LLM-Anbieter wie in [Configuration](configuration.md) beschrieben, es sei denn, Sie bereiten nur Markdown- oder Notebook-Chunks für die Übersetzung durch einen Host-Agenten vor.
2. Entscheiden Sie, ob Ihre Anwendung die Datei-Ein-/Ausgabe übernimmt.
3. Verwenden Sie Content-APIs, wenn Ihre Anwendung einzelne Dateien liest und schreibt.
4. Verwenden Sie `run_translation`, wenn Co-op Translator ein Repository wie die CLI verarbeiten soll.
5. Verwenden Sie `run_review` nach der Übersetzung, wenn Sie deterministische Prüfungen in der Automatisierung benötigen.

| Goal | API to start with |
| --- | --- |
| Translate one Markdown string or file | `translate_markdown_content` |
| Translate one notebook payload | `translate_notebook_content` |
| Translate one image | `translate_image_content` |
| Let a host agent translate Markdown or notebook chunks | `start_markdown_agent_translation` or `start_notebook_agent_translation` |
| Rewrite translated links after choosing an output path | `rewrite_markdown_paths` or `rewrite_notebook_paths` |
| Translate a full repository | `run_translation` |
| Review translated output | `run_review` |

## Scenario 1: Translate Individual Files or Documents

Verwenden Sie diesen Workflow, wenn Sie bereits eine Datei, einen Editor-Puffer, eine Notebook-Nutzlast, eine MCP-Anfrage oder eine benutzerdefinierte Pipeline-Eingabe haben. Ihr Code übernimmt die Datei-Ein-/Ausgabe:

1. Lesen Sie den Quellinhalt.
2. Rufen Sie eine Content-Übersetzungs-API auf.
3. Rufen Sie optional eine Pfad-Umschreibungs-API auf, wenn der übersetzte Inhalt in einen Projekt-Übersetzungsordner geschrieben werden soll.
4. Speichern oder geben Sie das Ergebnis aus Ihrer Anwendung zurück.

Die Content-Übersetzungs-APIs führen keine Projekterkennung durch, schreiben keine Metadaten, fügen keine Haftungsausschlüsse hinzu und schreiben Links nicht automatisch um.

### Markdown File

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

Wenn das übersetzte Markdown nicht in einem Co-op Translator Projektlayout liegen wird, überspringen Sie `rewrite_markdown_paths` und speichern Sie die übersetzte Zeichenkette direkt.

### Notebook File

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

`translate_notebook_content` übersetzt Markdown-Zellen und erhält Nicht-Markdown-Zellen. Die Pfadumschreibung wird nur auf Markdown-Zellen angewendet.

### Image File

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

`translate_image_content` liest das Quellbild und gibt ein gerendertes `PIL.Image.Image` zurück. Es schreibt keine übersetzten Bildmetadaten.

## Scenario 2: Translate an Entire Repository

Verwenden Sie diesen Workflow, wenn Sie möchten, dass die Python-API sich wie das `translate`-CLI verhält. `run_translation` entdeckt unterstützte Dateien, übersetzt ausgewählte Inhaltstypen, schreibt Pfade um, schreibt Ausgabedateien, aktualisiert Metadaten und führt Übersetzungs-Wartungsaufgaben wie Bereinigung durch.

`run_translation` ist der bevorzugte Einstiegspunkt zur Projektorchestrierung. `translate_project` wird als Kompatibilitäts-Alias mit demselben Verhalten exportiert.

Übersetzen Sie Markdown-Dateien im aktuellen Repository ins Koreanische und Japanische:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    markdown=True,
)
```

Übersetzen Sie nur Notebooks aus einem bestimmten Projektstamm:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="fr",
    root_dir="./my-course",
    notebook=True,
)
```

Vorschau des Übersetzungsvolumens ohne Dateien zu schreiben:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="es de",
    root_dir="./my-course",
    markdown=True,
    dry_run=True,
)
```

Übersetzen Sie mehrere Inhaltsstämme in einem Aufruf:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    root_dirs=["./docs", "./labs"],
)
```

Schreiben Sie Übersetzungen in explizite Ausgabengruppen:

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

Verwenden Sie einen sprachspezifischen Platzhalter, wenn jede Sprache ein verschachteltes Unterverzeichnis enthalten soll:

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

Wenn keines von `markdown`, `notebook` oder `images` gesetzt ist, übersetzt die API alle unterstützten Typen: Markdown, Notebooks und Bilder.

## Review Translated Output

`run_review` führt deterministische Übersetzungsprüfungen ohne LLM- oder Vision-Zugangsdaten aus.

!!! note "Beta"
    `run_review` ist eine Beta-API für deterministische Reviews. Sie ruft keine Modellanbieter auf und schreibt keine Dateien, aber Prüfungen und Issue-Schemata können sich weiterentwickeln.

```python
from co_op_translator.api import run_review

run_review(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
)
```

Überprüfen Sie nur Dateien, die gegenüber einem Basis-Ref geändert wurden, und drucken Sie GitHub-kompatible Ausgabe:

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

## Copy-Paste API Examples

Übersetzen Sie Markdown-Inhalt ohne Datei-Schreibvorgänge:

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

Übersetzen und überschreiben Sie Markdown-Links:

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

Übersetzen Sie ein Repository aus Python:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    root_dir="./course",
    markdown=True,
    yes=True,
)
```

Übersetzen Sie mehrere Stämme:

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

Behalten Sie Glossarbegriffe bei:

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

## Public Entry Points

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

## Content Translation APIs

Content-Übersetzungs-APIs sind für Integrationen gedacht, die Inhalte bereits im Speicher haben, wie eine Editor-Erweiterung, ein MCP-Tool, ein Notebook-Prozessor oder eine benutzerdefinierte Pipeline.

| Function | Input | Output | File I/O | Notes |
| --- | --- | --- | --- | --- |
| `translate_markdown_content` | Markdown `str` | Markdown `str` | No | Async. Translates Markdown content only. It does not rewrite links, write metadata, or append disclaimers. |
| `translate_notebook_content` | Notebook JSON `str` or `dict` | Notebook JSON `str` | No | Async. Translates Markdown cells and preserves non-Markdown cells. It does not rewrite links, write metadata, or append disclaimers. |
| `translate_image_content` | Image path | `PIL.Image.Image` | Reads source image only | Synchronous. Extracts and translates image text, then returns a rendered image. It does not save translated image metadata. |

`translate_markdown_content` und `translate_notebook_content` akzeptieren einen optionalen `source_path` über ihre Optionen. Der Pfad wird als Kontext an den Übersetzer übergeben; Aufrufer sind weiterhin für projektspezifische Pfadumschreibungen nach der Übersetzung verantwortlich.

```python
from co_op_translator.api import MarkdownTranslationOptions, translate_markdown_content

translated = await translate_markdown_content(
    document,
    "ko",
    MarkdownTranslationOptions(source_path="docs/guide.md"),
)
```

Die gleichen Optionen können als Dictionaries übergeben werden:

```python
translated = await translate_markdown_content(
    document,
    "ko",
    {"source_path": "docs/guide.md"},
)
```

## Agent-Assisted Translation APIs

Agent-unterstützte APIs rufen Azure OpenAI oder OpenAI nicht aus Co-op Translator auf. Sie bereiten Markdown- oder Notebook-Chunks für einen Host-Agenten zur Übersetzung vor und rekonstruieren dann den finalen Inhalt aus den übersetzten Chunks.

| Function | Purpose |
| --- | --- |
| `start_markdown_agent_translation` | Return a self-contained Markdown job with chunks, prompts, and reconstruction state. |
| `finish_markdown_agent_translation` | Reconstruct Markdown from a job and host-agent translated chunks. |
| `start_notebook_agent_translation` | Return a notebook job with Markdown-cell chunks for host-agent translation. |
| `finish_notebook_agent_translation` | Reconstruct notebook JSON while preserving code cells, outputs, and metadata. |

Dieser Workflow ist hauptsächlich für MCP-Hosts vorgesehen. Wenn Sie eine Produktions-Repository-Übersetzung benötigen, bei der Co-op Translator die Anbieteraufrufe verwaltet, verwenden Sie `translate_markdown_content`, `translate_notebook_content` oder `run_translation`.

## Path Rewriting APIs

Pfad-Umschreibungs-APIs führen keine Übersetzung durch. Sie aktualisieren Links und Frontmatter-Pfade, nachdem Aufrufer den Quellpfad, den übersetzten Zielpfad und das Projektlayout kennen.

| Function | Scope | Notes |
| --- | --- | --- |
| `rewrite_markdown_paths` | Markdown body and frontmatter | Rewrites Markdown links and supported frontmatter path fields for a translated target. |
| `rewrite_notebook_paths` | Markdown cells in notebook JSON | Applies Markdown path rewriting to each Markdown cell and leaves non-Markdown cells unchanged. |

Das `policy`-Argument kann ein Dictionary mit diesen Feldern sein:

| Field | Required | Purpose |
| --- | --- | --- |
| `language_code` | Yes | Target language code, such as `"ko"` or `"pt-BR"`. |
| `root_dir` | No | Source project root. Defaults to `"."`. |
| `translations_dir` | No | Text translation output directory. Defaults to `translations` under `root_dir`. |
| `translated_images_dir` | No | Translated image output directory. Defaults to `translated_images` under `root_dir`. |
| `translation_types` | No | Enabled translation types. Defaults to Markdown, notebooks, and images. |
| `lang_subdir` | No | Optional subdirectory under each language folder. |

## Project Translation Parameters

| Parameter | Type | Default | Purpose |
| --- | --- | --- | --- |
| `language_codes` | `str` | Required | Space-separated target language codes, such as `"ko ja fr"`, or `"all"`. Alias codes are normalized to canonical BCP 47 values. |
| `root_dir` | `str` | `"."` | Project root for a single translation target. Ignored when `root_dirs` or `groups` are supplied. |
| `update` | `bool` | `False` | Delete and recreate existing translations for the selected languages. |
| `images` | `bool` | `False` | Include image translation. Requires Azure AI Vision configuration. |
| `markdown` | `bool` | `False` | Include Markdown translation. |
| `notebook` | `bool` | `False` | Include Jupyter notebook translation. |
| `debug` | `bool` | `False` | Enable debug logging. |
| `save_logs` | `bool` | `False` | Save DEBUG-level log files under the root `logs/` directory. |
| `yes` | `bool` | `True` | Auto-confirm prompts for programmatic and CI usage. |
| `add_disclaimer` | `bool` | `False` | Add machine translation disclaimers to translated Markdown and notebooks. |
| `translations_dir` | `str \| None` | `None` | Custom text translation output directory. Relative paths resolve against each root. |
| `image_dir` | `str \| None` | `None` | Custom translated image output directory. Relative paths resolve against each root. |
| `root_dirs` | `Iterable[str] \| None` | `None` | Multiple roots that share the same output settings. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | Explicit `(root_dir, translations_dir)` pairs. Takes precedence over `root_dirs`. |
| `repo_url` | `str \| None` | `None` | Repository URL used when rendering README language table guidance. |
| `glossaries` | `Iterable[str] \| None` | `None` | Glossary terms to preserve during translation. Duplicates and blank terms are normalized. |
| `dry_run` | `bool` | `False` | Estimate translation volume and preview migration behavior without writing files. |

## Review Parameters

`run_review` spiegelt absichtlich das `run_translation`-Signaturbild, wo möglich, damit die Automatisierung mit minimalen Verzweigungen zwischen Übersetzungs- und Review-Workflows wechseln kann.

| Parameter | Type | Default | Purpose |
| --- | --- | --- | --- |
| `language_codes` | `str \| Iterable[str]` | `"all"` | Target language folders to review. Space-separated strings and iterables are accepted. `"all"` reviews every discovered translation language. |
| `root_dir` | `str` | `"."` | Project root for a single review target. Ignored when `root_dirs` or `groups` are supplied. |
| `markdown` | `bool` | `False` | Include Markdown and MDX source files. |
| `notebook` | `bool` | `False` | Include Jupyter notebook source files. |
| `images` | `bool` | `False` | Reserved for parity with translation options. Link references to images are checked from Markdown. |
| `translations_dir` | `str \| None` | `None` | Benutzerdefiniertes Ausgabeverzeichnis für Textübersetzungen. Relative Pfade werden gegenüber jedem Stammverzeichnis aufgelöst. |
| `root_dirs` | `Iterable[str] \| None` | `None` | Mehrere Stammverzeichnisse, die dieselben Ausgabeeinstellungen teilen. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | Explizite `(root_dir, translations_dir)`-Paare. Haben Vorrang vor `root_dirs`. |
| `changed_from` | `str \| None` | `None` | Git-Ref, die verwendet wird, um die Prüfung auf geänderte Quelldateien zu beschränken. |
| `output_format` | `str` | `"text"` | Ausgabeformat der Überprüfung. Unterstützte Werte sind `"text"` und `"github"`. |
| `fail_on_warnings` | `bool` | `False` | Behandle Warnungen zusätzlich zu Fehlern als Fehlschläge. |
| `debug` | `bool` | `False` | Debug-Logging aktivieren. |
| `save_logs` | `bool` | `False` | Speichert Protokolldateien auf DEBUG-Ebene im Stammverzeichnis `logs/`. |

If none of `markdown`, `notebook`, or `images` are set, the API reviews Markdown, notebooks, and image link references where applicable. Review does not call an LLM provider and does not require API keys.

## Konfigurationsanforderungen

Von Providern unterstützte Übersetzungs‑APIs erfordern vor der Übersetzung eine Provider‑Konfiguration:

- Markdown and notebook translation require an LLM provider. Configure either Azure OpenAI or OpenAI.
- Image translation requires Azure AI Vision in addition to the LLM provider.
- `run_translation` runs lightweight connectivity checks before project translation begins.
- Agent-assisted `start_*_agent_translation` and `finish_*_agent_translation` APIs do not call Co-op Translator LLM providers. The host application or MCP agent translates the prepared chunks.
- `rewrite_markdown_paths`, `rewrite_notebook_paths`, and `run_review` are deterministic and do not require provider credentials.

Required Azure OpenAI variables:

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Required OpenAI variables:

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

Required Azure AI Vision variables for image translation:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

`run_review` is deterministic and does not require Azure OpenAI, OpenAI, or Azure AI Vision configuration.

## Verhaltenshinweise

- Die Content-Übersetzungs-APIs trennen Übersetzung und Pfadumschreibung im Projekt. Rufen Sie `rewrite_markdown_paths` oder `rewrite_notebook_paths` explizit auf, wenn übersetzter Inhalt projektrelative Links an einen Zielort anpassen muss.
- Projektorchestrierungs-APIs fügen rund um die Inhaltsübersetzung projektbezogenes Verhalten hinzu, einschließlich Dateierkennung, Schreibvorgängen, Pfadumschreibung, Metadaten, Bereinigung und optionalen Haftungsausschlüssen.
- `run_translation` gibt Fortschritt und Schätzungszusammenfassungen über Click aus und entspricht so der CLI-Nutzererfahrung.
- `dry_run=True` berechnet Schätzungen mithilfe virtueller README-Aktualisierungen, schreibt aber weder das README noch die Übersetzungsdateien.
- `groups` werden nacheinander verarbeitet. Eine einzige aggregierte Schätzung wird ausgegeben, bevor die Arbeit beginnt.
- Wenn die Bildübersetzung ausgewählt ist, führt fehlende Vision-Konfiguration vor Übersetzungsbeginn zu einem Fehler.
- Bestehende aliasbasierte Sprachordner werden erkannt und können im Rahmen des Laufs auf kanonische Sprachordnernamen migriert werden.
- `run_review` schlägt fehl bei fehlenden übersetzten Dateien, fehlenden oder veralteten Übersetzungsmetadaten, fehlerhaftem Markdown-Frontmatter/Code-Fences und ungültigem übersetztem Notebook-JSON.
- `run_review` meldet standardmäßig fehlende lokale Markdown- und Bild-Link-Ziele als Warnungen.

## Interner Aufrufpfad

Die API delegiert an dieselbe Kernimplementierung, die auch von der CLI verwendet wird:

Translation:

1. `co_op_translator.api.translation.translate_markdown_content`, `translate_notebook_content`, or `translate_image_content` for in-memory translation.
2. `co_op_translator.api.translation.rewrite_markdown_paths` or `rewrite_notebook_paths` for explicit path post-processing.
3. `co_op_translator.api.translation.run_translation` for full project orchestration.
4. `co_op_translator.config.Config`, `LLMConfig`, and `VisionConfig`.
5. `co_op_translator.core.project.ProjectTranslator`.
6. `co_op_translator.core.project.TranslationManager`.
7. Focused project translation mixins for Markdown, notebooks, and images.
8. Markdown, notebook, text, and image translators under `co_op_translator.core`.

Review:

1. `co_op_translator.api.review.run_review`
2. `co_op_translator.review.targets.build_review_targets`
3. `co_op_translator.review.runner.ReviewRunner`
4. Deterministic checks under `co_op_translator.review.checks`

The following classes are useful for maintainers, but are not exported as the package-level stable API.

| Klasse | Modul | Aufgabe |
| --- | --- | --- |
| `ProjectTranslator` | `co_op_translator.core.project.project_translator` | Koordiniert Übersetzungen auf Projektebene, Verzeichnisverwaltung, sprachspezifische Metadaten-Normalisierung und Delegation an Markdown-, Notebook- und Bildübersetzer. |
| `TranslationManager` | `co_op_translator.core.project.translation` | Führt die asynchrone Dateiverarbeitung für Markdown, Notebooks, Bilder, Stalerkennung und Aktualisierungen der Übersetzungsmetadaten durch. |
| `ProjectMarkdownTranslationMixin` | `co_op_translator.core.project.translation.project_markdown_translation` | Orchestriert das Lesen von Markdown-Dateien, Inhaltsübersetzung, Pfadumschreibung, Metadaten, Haftungsausschlüsse und Schreibvorgänge. |
| `ProjectNotebookTranslationMixin` | `co_op_translator.core.project.translation.project_notebook_translation` | Orchestriert das Lesen von Notebook-Dateien, Übersetzung von Markdown-Zellen, Pfadumschreibung, Metadaten, Haftungsausschlüsse und Schreibvorgänge. |
| `ProjectImageTranslationMixin` | `co_op_translator.core.project.translation.project_image_translation` | Orchestriert die Ermittlung von Quellbildern, Bildübersetzung, Ausgabepfade, Metadaten und Schreibvorgänge. |
| `ProjectEvaluator` | `co_op_translator.core.project.project_evaluator` | Findet übersetzte Markdown-Paare, bewertet die Übersetzungsqualität und liest Konfidenzmetadaten für Reparatur-Workflows bei niedriger Konfidenz. |
| `ReviewRunner` | `co_op_translator.review.runner` | Koordiniert deterministische Überprüfungen über Quelldateien, Zielsprachen und konfigurierte Übersetzungsstammverzeichnisse. |
| `ReviewTarget` | `co_op_translator.review.targets` | Beschreibt ein Quell-Stammverzeichnis und das für dieses Stammverzeichnis geprüfte Übersetzungs-Ausgabeverzeichnis. |
| `LanguageFolderMigrator` | `co_op_translator.core.project.language_migrator` | Erkennt veraltete Alias-Sprachordner und bereitet Migrationspläne zu kanonischen BCP 47-Ordnern vor. |
| `Config` | `co_op_translator.config.base_config` | Lädt `.env`-Dateien und prüft, ob die erforderlichen LLM- und optionalen Vision-Anbieter konfiguriert sind. |
| `LLMConfig` | `co_op_translator.config.llm_config.config` | Erkennt automatisch Azure OpenAI oder OpenAI, validiert erforderliche Umgebungsvariablen und führt Konnektivitätsprüfungen für Provider durch. |
| `VisionConfig` | `co_op_translator.config.vision_config.config` | Erkennt die Azure AI Vision-Konfiguration und führt Konnektivitätsprüfungen für die Bildübersetzung durch. |