# Wählen Sie Ihren Workflow

Co-op Translator kann auf drei Arten verwendet werden: die CLI, die Python-API und der MCP-Server. Sie haben die gleichen Übersetzungsfunktionen, aber jede passt zu einem anderen Workflow.

Verwenden Sie diese Seite, wenn Sie entscheiden, wo Sie anfangen sollen.

## Schnelle Entscheidung

| Wenn Sie ... | Verwenden | Hier starten |
| --- | --- | --- |
| Ein Repository vom Terminal aus übersetzen oder überprüfen | CLI | [CLI-Referenz](cli.md) |
| Übersetzung zu einem Python-Skript, -Dienst, -Notebook oder CI-Job hinzufügen | Python-API | [Python-API](api.md) |
| Einen Agenten, Editor oder MCP-kompatiblen Client Inhalte für Sie übersetzen lassen | MCP-Server | [MCP-Server](mcp.md) |
| Ein Markdown-Dokument, Notebook oder Bild übersetzen, das Ihre App bereits geladen hat | Python-API oder MCP-Server | [Python-API](api.md) oder [MCP-Server](mcp.md) |
| Ein komplettes Repository mit standardmäßigen Ausgabeordnern und Metadaten übersetzen | CLI oder `run_translation` | [CLI-Referenz](cli.md) oder [Python-API](api.md) |

## Verwenden Sie die CLI, wenn

Wählen Sie die CLI, wenn eine Person oder ein CI-Job die Repository-Übersetzung über eine Shell steuert.

Die CLI ist der direkteste Weg, wenn Sie möchten, dass Co-op Translator Projektdateien erkennt, übersetzte Ausgaben erstellt, das Projektlayout beibehält, Metadaten aktualisiert und Review-Befehle ausführt.

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -md -nb -img
co-op-review -l "ko" -md -nb
migrate-links -l "ko" --dry-run
```

Passt gut für:

- Sie übersetzen ein Repository von Ihrem Terminal aus.
- Sie möchten einen wiederholbaren Befehl für CI- oder Release-Workflows.
- Sie möchten eingebaute Projekterkennung, Ausgabewege, Metadaten, Bereinigung und Review.
- Sie bevorzugen eine Befehlsoberfläche gegenüber dem Schreiben von Python-Code.

## Verwenden Sie die Python-API, wenn

Wählen Sie die Python-API, wenn Ihr eigener Code den Workflow steuern soll.

Die API ist nützlich für Anwendungen, Automatisierungsskripte, Notebooks, Dienste und benutzerdefinierte Pipelines. Sie ermöglicht das Aufrufen von Low-Level-Inhaltsübersetzungs-APIs für einzelne Dateien oder das Ausführen derselben Repository-orchestrierung, die von der CLI verwendet wird.

Ein Markdown-Dokument übersetzen und entscheiden, wo es gespeichert werden soll:

```python
import asyncio
from pathlib import Path

from co_op_translator.api import rewrite_markdown_paths, translate_markdown_content


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
    )

    target_path.parent.mkdir(parents=True, exist_ok=True)
    target_path.write_text(rewritten, encoding="utf-8")


asyncio.run(main())
```

Führen Sie eine Repository-Übersetzung aus Python aus:

```python
import asyncio

from co_op_translator.api import run_translation


async def main() -> None:
    await run_translation(
        language_codes=["ko"],
        translate_markdown=True,
        translate_notebooks=True,
        translate_images=False,
        dry_run=True,
    )


asyncio.run(main())
```

Passt gut für:

- Ihre Anwendung liest bereits Dateien, Buffer, Notebooks oder Bildbytes.
- Sie benötigen benutzerdefinierte Validierung, Speicherung, Protokollierung, Wiederholungen oder Genehmigungsabläufe.
- Sie möchten ein Dokument, Notebook oder Bild übersetzen, ohne ein ganzes Repository zu verarbeiten.
- Sie möchten Repository-Übersetzung, aber aus Python-Automation statt eines Shell-Befehls.

## Verwenden Sie den MCP-Server, wenn

Wählen Sie den MCP-Server, wenn ein Agent, Editor oder MCP-kompatibler Client die Co-op Translator-Tools aufrufen soll.

In der normalen lokalen Konfiguration hält der Benutzer den Server nicht manuell am Laufen. Der MCP-Client startet `co-op-translator-mcp` über `stdio`, wenn er die Tools benötigt.

Beispiele für Benutzeranfragen, die ein Agent bearbeiten könnte:

- "Übersetze diese Markdown-Datei ins Koreanische und behalte die Links korrekt bei."
- "Übersetze diese Markdown-Datei ins Koreanische mit dem agentenunterstützten MCP-Workflow, unter Verwendung eines eigenen Modells für die übersetzten Abschnitte."
- "Übersetze dieses Notebook ins Koreanische, bewahre Codezellen und verwende Co-op Translator MCP, um das Notebook zu rekonstruieren."
- "Übersetze den Text in diesem Bild ins Japanische und speichere das Ergebnis."
- "Führe eine Trockenausführung einer Repository-Übersetzung ins Spanische durch und sag mir, was sich ändern würde."
- "Prüfe, ob die koreanische Übersetzung auf dem neuesten Stand ist."

Für Markdown und Notebooks kann MCP in zwei Modi arbeiten:

| Modus | Verwenden, wenn | Hauptwerkzeuge |
| --- | --- | --- |
| Agent-unterstützt | Der MCP-Host-Agent sollte Abschnitte mit seinem eigenen Modell übersetzen, ohne Zugangsdaten für einen LLM-Anbieter von Co-op Translator. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Provider-gestützt | Co-op Translator sollte Azure OpenAI oder OpenAI direkt aufrufen. | `translate_markdown_content`, `translate_notebook_content` |

MCP provider-gestützter Markdown-Toolaufruf-Shape:

```json
{
  "tool": "translate_markdown_content",
  "arguments": {
    "document": "# Setup\n\nInstall Co-op Translator first.",
    "language_code": "ko",
    "options": {
      "source_path": "docs/setup.md"
    }
  }
}
```

MCP Bild-Toolaufruf-Shape:

```json
{
  "tool": "translate_image_content",
  "arguments": {
    "image_path": "assets/architecture.png",
    "language_code": "ko",
    "output_path": "translated_images/ko/assets/architecture.png"
  }
}
```

Repository-Übersetzung wird standardmäßig über MCP als Trockendurchlauf ausgeführt:

```json
{
  "tool": "run_translation",
  "arguments": {
    "language_codes": ["ko"],
    "translate_markdown": true,
    "translate_notebooks": true,
    "translate_images": false,
    "dry_run": true
  }
}
```

Passt gut für:

- Sie möchten natürlichsprachige Übersetzungsworkflows in einem Agenten oder Editor.
- Sie möchten Markdown- oder Notebook-Übersetzung, bei der das Host-Agent-Modell vorbereitete Abschnitte übersetzt.
- Sie möchten, dass der Agent ausgewählte Inhalte statt eines gesamten Repositories übersetzt.
- Sie möchten einen Genehmigungsschritt vor repositoryweiten Schreibvorgängen.
- Sie möchten eine Schnittstelle, die Markdown-, Notebook-, Bild-, Review- und Pfad-Umschreibungswerkzeuge bereitstellt.

## Wie sie zusammenpassen

Die CLI ist die beste Standardeinstellung für Menschen, die Repositories übersetzen. Die Python-API ist am besten, wenn Ihr Code den Workflow besitzt. Der MCP-Server ist am besten, wenn ein Agent oder Editor den Workflow besitzt.

Alle drei Pfade verwenden die gleiche öffentliche Co-op Translator-API, sodass Sie mit der CLI beginnen, später mit Python automatisieren und dieselben Funktionen für MCP-Clients bereitstellen können, wenn Sie agentengesteuerte Workflows benötigen.