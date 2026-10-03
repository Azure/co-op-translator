# Python-API

Die stabile öffentliche Python-API wird aus `co_op_translator.api` exportiert. Die meisten Integrationen verwenden einen der folgenden Arbeitsabläufe:

| Szenario | Verwenden Sie dies, wenn | Haupt-APIs |
| --- | --- | --- |
| Einzelne Dateien oder Dokumente übersetzen | Ihre Anwendung liest die Quelldaten, ruft Co-op Translator zur Übersetzung auf und entscheidet, wo das Ergebnis gespeichert wird. | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Inhalte für die Übersetzung durch einen Host-Agenten vorbereiten | Ihr MCP-Host oder Anwendungsmodell übersetzt die Chunks, während Co-op Translator das Chunking und die Rekonstruktion übernimmt. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Ein gesamtes Repository übersetzen | Sie möchten, dass die Python-API sich wie das CLI verhält und Erkennung, Ausgabe-Pfade, Metadaten, Bereinigung und Schreibvorgänge übernimmt. | `run_translation` |

Die meisten tiefer gelegenen Module unter `core`, `config`, `review` und `utils` sind Implementierungsdetails, die von diesen API-Einstiegspunkten verwendet werden.

MCP-Clients verwenden die gleiche öffentliche API über den [MCP-Server](mcp.md). Verwenden Sie diese Seite, wenn Sie Python direkt aufrufen, und den MCP-Leitfaden, wenn Sie Co-op Translator einem Agenten oder Editor zur Verfügung stellen. Wenn Sie sich zwischen CLI, Python-API und MCP entscheiden, beginnen Sie mit [Wählen Sie Ihren Arbeitsablauf](workflows.md).

## Erster API-Ablauf

Beginnen Sie hier, wenn Sie Co-op Translator aus Python-Code aufrufen:

1. Konfigurieren Sie einen LLM-Anbieter wie in [Configuration](configuration.md) beschrieben, es sei denn, Sie bereiten nur Markdown- oder Notebook-Chunks für die Übersetzung durch einen Host-Agenten vor.
2. Entscheiden Sie, ob Ihre Anwendung die Datei-Ein-/Ausgabe verwaltet.
3. Verwenden Sie Content-APIs, wenn Ihre Anwendung einzelne Dateien liest und schreibt.
4. Verwenden Sie `run_translation`, wenn Co-op Translator ein Repository wie das CLI verarbeiten soll.
5. Verwenden Sie `run_review` nach der Übersetzung, wenn Sie deterministische Prüfungen in der Automatisierung benötigen.

| Ziel | API zum Starten |
| --- | --- |
| Eine Markdown-Zeichenfolge oder -Datei übersetzen | `translate_markdown_content` |
| Eine Notebook-Nutzlast übersetzen | `translate_notebook_content` |
| Ein Bild übersetzen | `translate_image_content` |
| Einem Host-Agenten die Übersetzung von Markdown- oder Notebook-Chunks überlassen | `start_markdown_agent_translation` oder `start_notebook_agent_translation` |
| Übersetzte Links nach Auswahl eines Ausgabe-Pfads umschreiben | `rewrite_markdown_paths` oder `rewrite_notebook_paths` |
| Ein komplettes Repository übersetzen | `run_translation` |
| Übersetzte Ausgabe überprüfen | `run_review` |

## Szenario 1: Einzelne Dateien oder Dokumente übersetzen

Verwenden Sie diesen Ablauf, wenn Sie bereits eine Datei, einen Editor-Puffer, eine Notebook-Nutzlast, eine MCP-Anfrage oder eine benutzerdefinierte Pipeline-Eingabe haben. Ihr Code ist für die Datei-Ein-/Ausgabe verantwortlich:

1. Lesen Sie den Quellinhalt.
2. Rufen Sie eine Content-Übersetzungs-API auf.
3. Optional: Rufen Sie eine Pfad-Umschreibungs-API auf, wenn der übersetzte Inhalt in einen Projekt-Übersetzungsordner geschrieben wird.
4. Speichern oder geben Sie das Ergebnis aus Ihrer Anwendung zurück.

Die Content-Übersetzungs-APIs führen keine Projekterkennung durch, schreiben keine Metadaten, fügen keine Haftungsausschlüsse hinzu und schreiben Links nicht automatisch um.

### Markdown-Datei

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

Wenn das übersetzte Markdown nicht in einem Co-op Translator-Projektlayout enthalten sein wird, überspringen Sie `rewrite_markdown_paths` und speichern Sie die übersetzte Zeichenfolge direkt.

### Notebook-Datei

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

`translate_notebook_content` übersetzt Markdown-Zellen und bewahrt Nicht-Markdown-Zellen. Pfadumschreibungen werden nur auf Markdown-Zellen angewendet.

### Bilddatei

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

## Szenario 2: Ein gesamtes Repository übersetzen

Verwenden Sie diesen Ablauf, wenn die Python-API wie das `translate`-CLI agieren soll. `run_translation` entdeckt unterstützte Dateien, übersetzt ausgewählte Inhaltstypen, schreibt Pfade um, schreibt Ausgabedateien, aktualisiert Metadaten und führt Übersetzungswartungsaufgaben wie Bereinigung durch.

`run_translation` ist der bevorzugte Einstiegspunkt zur Projektorchestrierung. `translate_project` wird als Kompatibilitätsalias mit dem gleichen Verhalten exportiert.

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

Vorschau des Übersetzungsumfangs ohne Dateien zu schreiben:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="es de",
    root_dir="./my-course",
    markdown=True,
    dry_run=True,
)
```

Zeichnen Sie strukturierte Fortschrittsereignisse für eine Integration auf:

```python
from co_op_translator.api import TranslationEvent, run_translation


def on_event(event: TranslationEvent) -> None:
    payload = event.to_dict()
    # Speichere die Nutzlast in deiner Job-Event-Tabelle oder sende sie an deine UI.


run_translation(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
    progress_callback=on_event,
)
```

Ereignisse verwenden das versionierte Schema `co-op.translation.event.v1`. Integrationen sollten
sich auf stabile Felder wie `type` und `stage_key` stützen und nicht auf benutzerorientierte
Konsolentext oder `stage_label`.

Mehrere Inhaltsstämme in einem Aufruf übersetzen:

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

### Akzeptierte menschliche Bearbeitungen mit einem TranslationStateProvider beibehalten

Standardmäßig behält Co-op Translator sein bestehendes Verhalten auf Datei-Ebene bei: wenn eine
Markdown-Quelle veraltet ist, wird die gesamte übersetzte Datei neu generiert. Gehostete
Integrationen können optional einen `TranslationStateProvider` übergeben, um menschliche
Bearbeitungen in Quellblöcken zu bewahren, die sich nicht geändert haben.

Der Provider liefert das zuletzt akzeptierte Quell-/Ziel-Paar und protokolliert jeden neuen
Kandidaten. Die Annahme bleibt in der Verantwortung der Integration – zum Beispiel,
nachdem ein Übersetzungs-Pull-Request gemerged wurde:

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

Für Markdown-Dateien mit einer gültigen akzeptierten Baseline stimmt Co-op Translator
top-level Markdown-Blöcke ab. Unveränderte Quellblöcke verwenden wieder die aktuellen übersetzten
Blöcke, einschließlich von Personen vorgenommener Bearbeitungen; geänderte oder hinzugefügte Quellblöcke werden zur Übersetzung gesendet
zur Übersetzung; gelöschte Quellblöcke werden entfernt. Wenn die Zuordnung mehrdeutig ist,
die Zielstruktur sich geändert hat, eine Blockübersetzung ungültig ist oder keine Baseline
verfügbar ist, fällt Co-op Translator sicher auf den bestehenden vollständigen Datei-
Übersetzungspfad zurück.

Diese API speichert den Übersetzungszustand von Dokumenten, nicht eine dokumentübergreifende Phrase- oder
Segment-Übersetzungs-Memory. Derzeit gilt sie für Markdown-Projektübersetzungen.
Verhalten für Notebooks und Bilder bleibt unverändert. Das Setzen von `update=True`
fordert weiterhin eine vollständige Neugenerierung an.

Wenn eine oder mehrere Dateien nicht übersetzt werden können, löst `run_translation` einen
`RuntimeError` aus, nachdem der Projektworkflow abgeschlossen ist, anstatt einen
erfolgreichen Lauf mit fehlender Ausgabe zu melden. Integrationen sollten dies als fehlgeschlagene
Aufgabe behandeln und den zuvor akzeptierten Übersetzungszustand beibehalten.

## Übersetzte Ausgabe überprüfen

`run_review` führt deterministische Übersetzungsprüfungen ohne LLM- oder Vision-Anmeldeinformationen durch.

!!! note "Beta"
    `run_review` ist eine Beta-Version einer deterministischen Review-API. Sie ruft keine Modellanbieter auf und schreibt keine Dateien, aber Prüfungen und Issue-Schemata können sich weiterentwickeln.

```python
from co_op_translator.api import run_review

run_review(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
)
```

Nach einer reinen README-Übersetzung verwenden Sie denselben Umfang für die Prüfung:

```python
run_review(language_codes="ko", root_dir="./my-course", readme_only=True)
```

`readme_only=True` überprüft nur `README.md` unter jedem konfigurierten Quell-Stamm,
einschließlich benutzerdefinierter `groups` und Ausgabeordner. Andere Dokumente und verschachtelte
READMEs sind ausgeschlossen. Ein fehlendes Quell-README löst `ValueError` aus; fehlgeschlagene
Übersetzungsprüfungen lösen `RuntimeError` aus.

Überprüfen Sie nur Dateien, die gegenüber einem Basis-Ref geändert wurden, und geben Sie GitHub-flavored-Ausgabe aus:

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

## Copy-Paste API-Beispiele

Markdown-Inhalte übersetzen ohne Dateischreibvorgänge:

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

Markdown-Links übersetzen und umschreiben:

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

Ein Repository mit Python übersetzen:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    root_dir="./course",
    markdown=True,
    yes=True,
)
```

Mehrere Stämme übersetzen:

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

Glossarbegriffe bewahren:

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

## Öffentliche Einstiegspunkte

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

## Content-Übersetzungs-APIs

Content-Übersetzungs-APIs sind für Integrationen gedacht, die Inhalte bereits im Speicher haben, wie z. B. eine Editor-Erweiterung, ein MCP-Tool, ein Notebook-Prozessor oder eine benutzerdefinierte Pipeline.

| Funktion | Eingabe | Ausgabe | Datei-E/A | Hinweise |
| --- | --- | --- | --- | --- |
| `translate_markdown_content` | Markdown `str` | Markdown `str` | Nein | Asynchron. Übersetzt nur Markdown-Inhalte. Es schreibt keine Links um, schreibt keine Metadaten und fügt keine Haftungsausschlüsse hinzu. |
| `translate_notebook_content` | Notebook JSON `str` oder `dict` | Notebook JSON `str` | Nein | Asynchron. Übersetzt Markdown-Zellen und bewahrt Nicht-Markdown-Zellen. Es schreibt keine Links um, schreibt keine Metadaten und fügt keine Haftungsausschlüsse hinzu. |
| `translate_image_content` | Bildpfad | `PIL.Image.Image` | Liest nur das Quellbild | Synchron. Extrahiert und übersetzt Bildtext und gibt dann ein gerendertes Bild zurück. Es speichert keine übersetzten Bildmetadaten. |

`translate_markdown_content` und `translate_notebook_content` akzeptieren optional über ihre Optionen einen `source_path`. Der Pfad wird dem Translator als Kontext übergeben; die Aufrufer sind weiterhin verantwortlich für projektspezifische Pfadumschreibungen nach der Übersetzung.

```python
from co_op_translator.api import MarkdownTranslationOptions, translate_markdown_content

translated = await translate_markdown_content(
    document,
    "ko",
    MarkdownTranslationOptions(source_path="docs/guide.md"),
)
```

Die gleichen Optionen können auch als Dictionaries übergeben werden:

```python
translated = await translate_markdown_content(
    document,
    "ko",
    {"source_path": "docs/guide.md"},
)
```

## Agent-Unterstützte Übersetzungs-APIs

Agent-unterstützte APIs rufen den konfigurierten LLM-Anbieter von Co-op Translator nicht auf. Sie bereiten Markdown- oder Notebook-Chunks für einen Host-Agenten zur Übersetzung vor und rekonstruieren dann den finalen Inhalt aus den übersetzten Chunks.

| Funktion | Zweck |
| --- | --- |
| `start_markdown_agent_translation` | Gibt einen eigenständigen Markdown-Job mit Chunks, Prompts und Rekonstruktionszustand zurück. |
| `finish_markdown_agent_translation` | Rekonstruiert Markdown aus einem Job und vom Host-Agenten übersetzten Chunks. |
| `start_notebook_agent_translation` | Gibt einen Notebook-Job mit Markdown-Zellen-Chunks für die Übersetzung durch einen Host-Agenten zurück. |
| `finish_notebook_agent_translation` | Rekonstruiert Notebook-JSON und bewahrt dabei Code-Zellen, Outputs und Metadaten. |

Dieser Ablauf ist hauptsächlich für MCP-Hosts vorgesehen. Wenn Sie Produktions-Repository-Übersetzungen benötigen, bei denen Co-op Translator die Provideraufrufe verwaltet, verwenden Sie `translate_markdown_content`, `translate_notebook_content` oder `run_translation`.

## Pfad-Umschreibungs-APIs

Pfad-Umschreibungs-APIs führen keine Übersetzung durch. Sie aktualisieren Links und Frontmatter-Pfade, nachdem die Aufrufer den Quellpfad, den übersetzten Zielpfad und das Projektlayout kennen.

| Funktion | Geltungsbereich | Hinweise |
| --- | --- | --- |
| `rewrite_markdown_paths` | Markdown-Inhalt und Frontmatter | Schreibt Markdown-Links und unterstützte Frontmatter-Pfadfelder für ein übersetztes Ziel um. |
| `rewrite_notebook_paths` | Markdown-Zellen im Notebook-JSON | Wendet die Markdown-Pfadumschreibung auf jede Markdown-Zelle an und lässt Nicht-Markdown-Zellen unverändert. |

Das `policy`-Argument kann ein Dictionary mit diesen Feldern sein:

| Feld | Erforderlich | Zweck |
| --- | --- | --- |
| `language_code` | Ja | Ziel-Sprachcode, z. B. `"ko"` oder `"pt-BR"`. |
| `root_dir` | Nein | Projektstamm des Quells. Standard ist `"."`. |
| `translations_dir` | Nein | Ausgabeverzeichnis für Textübersetzungen. Standardmäßig `translations` unter `root_dir`. |
| `translated_images_dir` | Nein | Ausgabeverzeichnis für übersetzte Bilder. Standardmäßig `translated_images` unter `root_dir`. |
| `translation_types` | Nein | Aktivierte Übersetzungstypen. Standardmäßig Markdown, Notebooks und Bilder. |
| `lang_subdir` | Nein | Optionales Unterverzeichnis unter jedem Sprachordner. |

## Projekt-Übersetzungs-Parameter

| Parameter | Typ | Standard | Zweck |
| --- | --- | --- | --- |
| `language_codes` | `str` | Erforderlich | durch Leerzeichen getrennte Zielsprachen-Codes, z. B. `"ko ja fr"`, oder `"all"`. Alias-Codes werden auf kanonische BCP 47-Werte normalisiert. |
| `root_dir` | `str` | `"."` | Projektstamm für ein einzelnes Übersetzungsziel. Wird ignoriert, wenn `root_dirs` oder `groups` angegeben sind. |
| `update` | `bool` | `False` | Bestehende Übersetzungen für die ausgewählten Sprachen löschen und neu erstellen. |
| `images` | `bool` | `False` | Bildübersetzung einschließen. Erfordert Azure AI Vision-Konfiguration. |
| `markdown` | `bool` | `False` | Markdown-Übersetzung einschließen. |
| `notebook` | `bool` | `False` | Jupyter-Notebook-Übersetzung einschließen. |
| `debug` | `bool` | `False` | Debug-Logging aktivieren. |
| `save_logs` | `bool` | `False` | DEBUG-Level-Protokolldateien im Stammverzeichnis `logs/` speichern. |
| `yes` | `bool` | `True` | Eingabeaufforderungen für programmgesteuerte und CI-Nutzung automatisch bestätigen. |
| `add_disclaimer` | `bool` | `False` | Maschinenübersetzungs-Hinweise zu übersetzten Markdown-Dateien und Notebooks hinzufügen. |
| `translations_dir` | `str \| None` | `None` | Benutzerdefiniertes Ausgabeverzeichnis für Textübersetzungen. Relative Pfade werden relativ zu jedem Stammverzeichnis aufgelöst. |
| `image_dir` | `str \| None` | `None` | Benutzerdefiniertes Ausgabeverzeichnis für übersetzte Bilder. Relative Pfade werden relativ zu jedem Stammverzeichnis aufgelöst. |
| `root_dirs` | `Iterable[str] \| None` | `None` | Mehrere Stammverzeichnisse, die dieselben Ausgabeeinstellungen teilen. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | Explizite `(root_dir, translations_dir)`-Paare. Hat Vorrang vor `root_dirs`. |
| `repo_url` | `str \| None` | `None` | Repository-URL, die beim Erstellen der README-Sprachentabelle verwendet wird. |
| `glossaries` | `Iterable[str] \| None` | `None` | Glossarbegriffe, die während der Übersetzung erhalten bleiben sollen. Duplikate und leere Begriffe werden normalisiert. |
| `dry_run` | `bool` | `False` | Schätzt das Übersetzungsvolumen und zeigt das Migrationsverhalten an, ohne Dateien zu schreiben. |
| `translation_state_provider` | `TranslationStateProvider \| None` | `None` | Optionaler Adapter zur Persistenz von akzeptierter Basis und Kandidaten für inkrementelle Markdown-Aktualisierungen. Wenn weggelassen, bleibt das bestehende Verhalten mit vollständigen Dateien erhalten. |

## Überprüfungsparameter

`run_review` spiegelt absichtlich die Signatur von `run_translation` so weit wie möglich wider, damit Automatisierungen mit minimalen Verzweigungen zwischen Übersetzungs- und Prüf-Workflows wechseln können.

| Parameter | Typ | Standard | Zweck |
| --- | --- | --- | --- |
| `language_codes` | `str \| Iterable[str]` | `"all"` | Zu überprüfende Zielsprachordner. Leerzeichen-getrennte Strings und Iterables werden akzeptiert. `"all"` überprüft jede entdeckte Übersetzungssprache. |
| `root_dir` | `str` | `"."` | Projekt-Stammverzeichnis für ein einzelnes Prüfungsziel. Wird ignoriert, wenn `root_dirs` oder `groups` angegeben sind. |
| `markdown` | `bool` | `False` | Markdown- und MDX-Quelldateien einschließen. |
| `notebook` | `bool` | `False` | Jupyter-Notebook-Quelldateien einschließen. |
| `images` | `bool` | `False` | Reserviert zur Parität mit den Übersetzungsoptionen. Link-Referenzen zu Bildern werden aus Markdown geprüft. |
| `translations_dir` | `str \| None` | `None` | Benutzerdefiniertes Ausgabeverzeichnis für Textübersetzungen. Relative Pfade werden relativ zu jedem Stammverzeichnis aufgelöst. |
| `root_dirs` | `Iterable[str] \| None` | `None` | Mehrere Stammverzeichnisse, die dieselben Ausgabeeinstellungen teilen. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | Explizite `(root_dir, translations_dir)`-Paare. Hat Vorrang vor `root_dirs`. |
| `changed_from` | `str \| None` | `None` | Git-Ref, der verwendet wird, um die Überprüfung auf geänderte Quelldateien zu beschränken. |
| `readme_only` | `bool` | `False` | Prüft nur `README.md` unter jedem Quell-Stammverzeichnis. Ein fehlendes Quell-README löst `ValueError` aus. |
| `output_format` | `str` | `"text"` | Ausgabeformat der Überprüfung. Unterstützte Werte sind `"text"` und `"github"`. |
| `fail_on_warnings` | `bool` | `False` | Warnungen zusätzlich zu Fehlern als Fehler behandeln. |
| `debug` | `bool` | `False` | Debug-Logging aktivieren. |
| `save_logs` | `bool` | `False` | DEBUG-Level-Protokolldateien im `logs/`-Verzeichnis des Stammverzeichnisses speichern. |

Wenn weder `markdown`, `notebook` noch `images` gesetzt sind, überprüft die API Markdown, Notebooks und Bildlink-Verweise, sofern zutreffend. Die Überprüfung ruft keinen LLM-Provider auf und erfordert keine API-Schlüssel.

## Konfigurationsanforderungen

Anbieterbasierte Übersetzungs-APIs erfordern eine Anbieter-Konfiguration vor der Übersetzung:

- Für Markdown- und Notebook-Übersetzungen ist ein LLM-Anbieter erforderlich. Konfigurieren Sie Azure OpenAI, OpenAI oder Anthropic.
- Bildübersetzung erfordert zusätzlich zum LLM-Anbieter Azure AI Vision.
- `run_translation` führt vor Beginn der Projektübersetzung leichte Konnektivitätsprüfungen durch.
- Agent-unterstützte `start_*_agent_translation`- und `finish_*_agent_translation`-APIs rufen keine Co-op Translator LLM-Provider auf. Die Host-Anwendung oder der MCP-Agent übersetzt die vorbereiteten Chunks.
- `rewrite_markdown_paths`, `rewrite_notebook_paths` und `run_review` sind deterministisch und benötigen keine Anbieter-Zugangsdaten.

Erforderliche Azure OpenAI-Variablen:

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Erforderliche OpenAI-Variablen:

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

Erforderliche Anthropic-Variablen:

```bash
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

`ANTHROPIC_BASE_URL` und `ANTHROPIC_MAX_TOKENS` sind optional. Microsoft Agent Framework ist ab Co-op Translator 0.22.0 der Standardmodell-Client für alle Anbieter. Semantic Kernel kann weiterhin vorübergehend mit `CO_OP_TRANSLATOR_MODEL_CLIENT="semantic-kernel"` ausgewählt werden, aber dies gibt eine Deprecation-Warnung aus; siehe [Konfiguration](configuration.md#model-client-backend) für den gestaffelten Entfernungsplan.

Erforderliche Azure AI Vision-Variablen für die Bildübersetzung:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

`run_review` ist deterministisch und erfordert keine LLM- oder Azure AI Vision-Konfiguration.

## Verhaltenshinweise

- Inhaltsübersetzungs-APIs trennen Übersetzung vom Umschreiben von Projektpfaden. Rufen Sie `rewrite_markdown_paths` oder `rewrite_notebook_paths` explizit auf, wenn übersetzter Inhalt projekt-relative Links für ein Ziel anpassen muss.
- Projektorchestrierungs-APIs fügen Projektverhalten rund um die Inhaltsübersetzung hinzu, einschließlich Dateierkennung, Schreibvorgängen, Pfadumschreibung, Metadaten, Bereinigung und optionalen Haftungsausschlüssen.
- `run_translation` gibt Fortschritts- und Schätzungszusammenfassungen über denselben Rich-basierten Reporter aus, der auch vom CLI verwendet wird. Nicht-interaktive Ausgaben fallen auf einfachen Text zurück.
- `dry_run=True` berechnet Schätzungen mithilfe virtueller README-Aktualisierungen, schreibt jedoch weder die README noch Übersetzungsdateien.
- `groups` werden nacheinander verarbeitet. Eine einzige aggregierte Schätzung wird vor Arbeitsbeginn ausgegeben.
- Wenn die Bildübersetzung ausgewählt ist, führt eine fehlende Vision-Konfiguration vor Beginn der Übersetzung zu einem Fehler.
- Bestehende aliasbasierte Sprachordner werden erkannt und können im Rahmen des Laufs auf kanonische Sprachordnernamen migriert werden.
- `run_review` schlägt fehl bei fehlenden übersetzten Dateien, fehlenden oder veralteten Übersetzungsmetadaten, fehlerhaftem Markdown-Frontmatter/Code-Fences und ungültigem übersetztem Notebook-JSON.
- `run_review` meldet fehlende lokale Markdown- und Bild-Link-Ziele standardmäßig als Warnungen.

## Interner Aufrufpfad

Die API delegiert an dieselbe Kernimplementierung, die vom CLI verwendet wird:

Übersetzung:

1. `co_op_translator.api.translation.translate_markdown_content`, `translate_notebook_content`, or `translate_image_content` für In-Memory-Übersetzung.
2. `co_op_translator.api.translation.rewrite_markdown_paths` or `rewrite_notebook_paths` für explizite Nachbearbeitung von Pfaden.
3. `co_op_translator.api.translation.run_translation` für vollständige Projektorchestrierung.
4. `co_op_translator.config.Config`, `LLMConfig`, and `VisionConfig`.
5. `co_op_translator.core.project.ProjectTranslator`.
6. `co_op_translator.core.project.TranslationManager`.
7. Fokussierte Projekt-Übersetzungs-Mixins für Markdown, Notebooks und Bilder.
8. Markdown-, Notebook-, Text- und Bildübersetzer unter `co_op_translator.core`.

Überprüfung:

1. `co_op_translator.api.review.run_review`
2. `co_op_translator.review.targets.build_review_targets`
3. `co_op_translator.review.runner.ReviewRunner`
4. Deterministische Prüfungen unter `co_op_translator.review.checks`

Die folgenden Klassen sind für Maintainer nützlich, werden jedoch nicht als paketweite stabile API exportiert.

| Klasse | Modul | Verantwortung |
| --- | --- | --- |
| `ProjectTranslator` | `co_op_translator.core.project.project_translator` | Koordiniert Übersetzungen auf Projektebene, Verzeichnisverwaltung, sprachbezogene Metadaten-Normalisierung und die Delegation an Markdown-, Notebook- und Bildübersetzer. |
| `TranslationManager` | `co_op_translator.core.project.translation` | Führt die asynchronen Datei-Verarbeitungsarbeiten für Markdown, Notebooks, Bilder, Erkennung veralteter Dateien und Aktualisierungen der Übersetzungsmetadaten durch. |
| `ProjectMarkdownTranslationMixin` | `co_op_translator.core.project.translation.project_markdown_translation` | Orchestriert das Lesen von Markdown-Dateien, Inhaltsübersetzung, Pfadumschreibung, Metadaten, Haftungsausschlüsse und Schreibvorgänge. |
| `ProjectNotebookTranslationMixin` | `co_op_translator.core.project.translation.project_notebook_translation` | Orchestriert das Lesen von Notebook-Dateien, Übersetzung von Markdown-Zellen, Pfadumschreibung, Metadaten, Haftungsausschlüsse und Schreibvorgänge. |
| `ProjectImageTranslationMixin` | `co_op_translator.core.project.translation.project_image_translation` | Orchestriert die Erkennung von Quellbildern, Bildübersetzung, Ausgabepfade, Metadaten und Schreibvorgänge. |
| `ProjectEvaluator` | `co_op_translator.core.project.project_evaluator` | Findet übersetzte Markdown-Paare, bewertet die Übersetzungsqualität und liest Konfidenz-Metadaten für Reparatur-Workflows bei geringer Konfidenz. |
| `ReviewRunner` | `co_op_translator.review.runner` | Koordiniert deterministische Prüfungen über Quelldateien, Zielsprachen und konfigurierte Übersetzungs-Stammverzeichnisse. |
| `ReviewTarget` | `co_op_translator.review.targets` | Beschreibt ein Quell-Stammverzeichnis und das Übersetzungs-Ausgabeverzeichnis, das für dieses Stammverzeichnis geprüft wird. |
| `LanguageFolderMigrator` | `co_op_translator.core.project.language_migrator` | Erkennt alte Alias-Sprachordner und bereitet Migrationspläne zu kanonischen BCP 47-Ordnernamen vor. |
| `Config` | `co_op_translator.config.base_config` | Lädt `.env`-Dateien und prüft, ob erforderliche LLM- und optionale Vision-Anbieter konfiguriert sind. |
| `LLMConfig` | `co_op_translator.config.llm_config.config` | Erkennt automatisch Azure OpenAI, OpenAI oder Anthropic, validiert erforderliche Umgebungsvariablen und führt Konnektivitätsprüfungen für Anbieter durch. |
| `VisionConfig` | `co_op_translator.config.vision_config.config` | Erkennt Azure AI Vision-Konfiguration und führt Konnektivitätsprüfungen für die Bildübersetzung durch. |