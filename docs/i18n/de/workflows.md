# Wählen Sie Ihren Workflow

Co-op Translator kann auf drei Arten verwendet werden: die CLI, die Python-API und der MCP-Server. Sie teilen sich dieselben Übersetzungsfunktionen, aber jede passt zu einem anderen Workflow.

Verwenden Sie diese Seite, wenn Sie entscheiden, wo Sie anfangen sollen.

**Wenn Sie Übersetzungen per Hand bearbeiten:** Die standardmäßigen CLI- und Actions-Workflows übersetzen geänderte Quelldateien vollständig neu, sodass Ihre Formulierungen in diesen Dateien überschrieben werden können. Prüfen Sie den Diff, bevor Sie ein Update annehmen. Zur Bewahrung der Blockstruktur akzeptierter Markdown-Änderungen verwenden Sie den optionalen [Python API translation state provider](api.md#preserve-accepted-human-edits-with-a-translation-state-provider).

## Schnelle Entscheidung

| Wenn Sie ... | Verwenden | Hier starten |
| --- | --- | --- |
| Ein Repository vom Terminal aus übersetzen oder überprüfen | CLI | [CLI Reference](cli.md) |
| Übersetzung zu einem Python-Skript, Service, Notebook oder CI-Job hinzufügen | Python API | [Python API](api.md) |
| Lassen Sie einen Agenten, Editor oder MCP-kompatiblen Client Inhalte für Sie übersetzen | MCP Server | [MCP Server](mcp.md) |
| Ein Markdown-Dokument, Notebook oder Bild übersetzen, das Ihre Anwendung bereits geladen hat | Python API oder MCP Server | [Python API](api.md) oder [MCP Server](mcp.md) |
| Ein ganzes Repository mit standardmäßigen Ausgabeordnern und Metadaten übersetzen | CLI oder `run_translation` | [CLI Reference](cli.md) oder [Python API](api.md) |

## Verwenden Sie die CLI, wenn

Wählen Sie die CLI, wenn eine Person oder ein CI-Job die Repository-Übersetzung von einer Shell aus steuert.

Die CLI ist der direkteste Weg, wenn Sie möchten, dass Co-op Translator Projektdateien entdeckt, übersetzte Ausgaben erstellt, das Projektlayout beibehält, Metadaten aktualisiert und Review-Befehle ausführt.

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -md -nb
co-op-review -l "ko"
migrate-links -l "ko" --dry-run
```

Dieses Beispiel übersetzt Markdown und Notebooks. Fügen Sie `-img` nur hinzu, nachdem Sie [Azure AI Vision](configuration.md#azure-ai-vision) konfiguriert haben. Für einen ersten Lauf nur mit Markdown folgen Sie [Your first translation](first-translation.md).

Gute Anwendungsfälle:

- Sie übersetzen ein Repository von Ihrem Terminal aus.
- Sie möchten einen wiederholbaren Befehl für CI- oder Release-Workflows.
- Sie möchten integrierte Projekterkennung, Ausgabepfade, Metadaten, Bereinigung und Review.
- Sie bevorzugen eine Befehlsoberfläche gegenüber dem Schreiben von Python-Code.

## Verwenden Sie die Python-API, wenn

Wählen Sie die Python-API, wenn Ihr eigener Code den Workflow steuern soll.

Die API ist nützlich für Anwendungen, Automatisierungsskripte, Notebooks, Services und benutzerdefinierte Pipelines. Sie erlaubt es, niedrigstufige Inhaltsübersetzungs-APIs für einzelne Dateien aufzurufen oder dieselbe repositoryweite Orchestrierung auszuführen, die auch die CLI verwendet.

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
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    notebook=True,
    images=False,
    dry_run=True,
)
```

Gute Anwendungsfälle:

- Ihre Anwendung liest bereits Dateien, Puffer, Notebooks oder Bildbytes.
- Sie benötigen benutzerdefinierte Validierung, Speicherung, Logging, Wiederholungen oder Genehmigungsabläufe.
- Sie möchten ein Dokument, Notebook oder Bild übersetzen, ohne ein ganzes Repository zu verarbeiten.
- Sie möchten eine Repository-Übersetzung, aber über Python-Automation statt über einen Shell-Befehl.

## Verwenden Sie den MCP-Server, wenn

Wählen Sie den MCP-Server, wenn ein Agent, Editor oder ein MCP-kompatibler Client Co-op Translator-Tools aufrufen soll.

In der normalen lokalen Konfiguration hält der Benutzer den Server nicht manuell am Laufen. Der MCP-Client startet `co-op-translator-mcp` über `stdio`, wenn er die Tools benötigt.

Beispielhafte Benutzeranfragen, die ein Agent bearbeiten könnte:

- "Übersetze diese Markdown-Datei ins Koreanische und behalte die Links korrekt bei."
- "Übersetzen Sie diese Markdown-Datei ins Koreanische mit dem agentenunterstützten MCP-Workflow und verwenden Sie dabei Ihr eigenes Modell für die übersetzten Abschnitte."
- "Übersetzen Sie dieses Notebook ins Koreanische, bewahren Sie die Codezellen und verwenden Sie Co-op Translator MCP, um das Notebook zu rekonstruieren."
- "Übersetzen Sie den Text in diesem Bild ins Japanische und speichern Sie das Ergebnis."
- "Führen Sie eine Trockenübersetzung eines Repositories ins Spanische durch und sagen Sie mir, was sich ändern würde."
- "Prüfen Sie, ob die koreanische Übersetzung aktuell ist."

Für Markdown und Notebooks kann MCP in zwei Modi arbeiten:

| Modus | Verwenden wenn | Hauptwerkzeuge |
| --- | --- | --- |
| Agent-unterstützt | Der MCP-Host-Agent sollte Abschnitte mit seinem eigenen Modell übersetzen, ohne Zugangsdaten für den LLM-Anbieter von Co-op Translator. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Provider-gestützt | Co-op Translator sollte Azure OpenAI, OpenAI oder Anthropic direkt aufrufen. | `translate_markdown_content`, `translate_notebook_content` |

MCP provider-gestützte Markdown-Tool-Aufrufform:

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

MCP Image-Tool-Aufrufform:

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

Repository-Übersetzung wird standardmäßig über MCP als Trockenlauf ausgeführt:

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

Gute Anwendungsfälle:

- Sie möchten Workflows für Übersetzungen in natürlicher Sprache innerhalb eines Agents oder Editors.
- Sie möchten Markdown- oder Notebook-Übersetzungen, bei denen das Host-Agent-Modell vorbereitete Abschnitte übersetzt.
- Sie möchten, dass der Agent ausgewählte Inhalte übersetzt, anstatt ein ganzes Repository.
- Sie möchten einen Genehmigungsschritt vor repositoryweiten Schreibvorgängen.
- Sie möchten eine Schnittstelle, die Werkzeuge für Markdown, Notebooks, Bilder, Review und Pfadumschreibung bereitstellt.

## Wie sie zusammenpassen

Die CLI ist die beste Voreinstellung für Menschen, die Repositories übersetzen. Die Python-API ist am besten, wenn Ihr Code den Workflow steuert. Der MCP-Server ist am besten, wenn ein Agent oder Editor den Workflow steuert.

Alle drei Wege verwenden dieselbe öffentliche Co-op Translator-API, sodass Sie mit der CLI beginnen, später mit Python automatisieren und dieselben Fähigkeiten für MCP-Clients bereitstellen können, wenn Sie agentengesteuerte Workflows benötigen.