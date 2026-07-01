# MCP-Server

Co-op Translator enthält einen Model Context Protocol-Server für Agenten, Editoren und MCP-kompatible Clients.

Für die Standard-Lokaleinrichtung behalten Benutzer keinen separaten Server manuell geöffnet. Sie konfigurieren ihren MCP-Client, und der Client startet `co-op-translator-mcp` automatisch über `stdio`, wenn er Co-op Translator-Tools benötigt.

Wenn Sie sich zwischen CLI, Python-API und MCP entscheiden, beginnen Sie mit [Wählen Sie Ihren Arbeitsablauf](workflows.md).

Verwenden Sie MCP, wenn ein Agent oder Editor Co-op Translator direkt aufrufen soll:

| Benutzerziel | MCP-Tools |
| --- | --- |
| Ein Markdown-Dokument, ein Notebook oder ein Bild übersetzen | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content` |
| Markdown- oder Notebook-Inhalte mit dem Host-Agentenmodell übersetzen | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Übersetzte Markdown- oder Notebook-Links nach Auswahl des Ausgabepfads umschreiben | `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Ein komplettes Repository wie die CLI übersetzen | `run_translation`, `translate_project` |
| Übersetzte Ausgabe ohne LLM-Zugangsdaten prüfen | `run_review` |
| Funktionen und Umgebungsstatus prüfen | `get_api_overview`, `list_supported_languages`, `get_configuration_status` |

Der MCP-Server kapselt dieselbe öffentliche Python-API, die in [Python API](api.md) dokumentiert ist. Provider-gestützte Tools verwenden dieselben konfigurierten Provider wie die CLI und die Python-API. Agent-unterstützte Tools bereiten Chunks für den MCP-Host-Agenten zur Übersetzung vor und verwenden dann Co-op Translator, um das endgültige Markdown oder Notebook zu rekonstruieren.

## Schritt 1: Co-op Translator installieren und konfigurieren

Installieren Sie Co-op Translator in der Python-Umgebung, die Ihr MCP-Client verwenden wird:

```bash
pip install co-op-translator
```

Für die lokale Entwicklung aus diesem Repository installieren Sie das Paket im Editiermodus:

```bash
pip install -e .
```

Wählen Sie den Übersetzungsmodus, den Ihr MCP-Client verwenden soll:

| Modus | Verwenden für | Anmeldedaten |
| --- | --- | --- |
| Provider-gestützt | Co-op Translator ruft `translate_markdown_content`, `translate_notebook_content`, `translate_image_content` oder `run_translation` auf. | Markdown- und Notebook-Übersetzung erfordern Azure OpenAI oder OpenAI. Bildübersetzung erfordert außerdem Azure AI Vision. |
| Agent-unterstützt | Der MCP-Host-Agent übersetzt Chunks, die von `start_markdown_agent_translation` oder `start_notebook_agent_translation` zurückgegeben werden. | Für Markdown- oder Notebook-Chunks sind keine Co-op Translator LLM-Provider-Anmeldedaten erforderlich. Bildübersetzung wird im agent-unterstützten Modus noch nicht abgedeckt. |

Wenn Sie mit der Markdown- oder Notebook-Übersetzung innerhalb eines Agenten wie Codex oder Claude Code beginnen, starten Sie mit dem agent-unterstützten Modus. Verwenden Sie den provider-gestützten Modus, wenn Co-op Translator selbst Ihre konfigurierten Provider aufrufen soll, wenn Sie Bilder übersetzen oder wenn Sie repositoryweite Übersetzungen wie mit der CLI ausführen.

Konfigurieren Sie Provider-Anmeldedaten nur für provider-gestützte Workflows:

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Provider-gestützte Bildübersetzung benötigt zusätzlich:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

!!! note
    Der agent-unterstützte Modus deckt derzeit Markdown und Markdown-Zellen in Notebooks ab. Die Bildübersetzung verwendet weiterhin die provider-gestützte Bildpipeline und erfordert Azure AI Vision für OCR und layoutsensible Darstellung.

## Schritt 2: Konfigurieren Sie Ihren MCP-Client

Für die normale lokale `stdio`-Einrichtung fügen Sie Co-op Translator Ihrer MCP-Client-Konfiguration hinzu. Der Client startet und beendet den Prozess automatisch.

Konfiguration für installiertes Paket:

```json
{
  "mcpServers": {
    "co-op-translator": {
      "command": "co-op-translator-mcp",
      "args": []
    }
  }
}
```

Source-Checkout-Konfiguration unter Windows:

```json
{
  "mcpServers": {
    "co-op-translator": {
      "command": "C:\\Users\\you\\dev\\co-op-translator\\.venv\\Scripts\\python.exe",
      "args": ["-m", "co_op_translator.mcp.server"],
      "cwd": "C:\\Users\\you\\dev\\co-op-translator"
    }
  }
}
```

Source-Checkout-Konfiguration unter macOS oder Linux:

```json
{
  "mcpServers": {
    "co-op-translator": {
      "command": "/Users/you/dev/co-op-translator/.venv/bin/python",
      "args": ["-m", "co_op_translator.mcp.server"],
      "cwd": "/Users/you/dev/co-op-translator"
    }
  }
}
```

Nachdem Sie die MCP-Client-Konfiguration geändert haben, starten oder laden Sie den Client neu, damit er den neuen Server entdecken kann.

## Schritt 3: Server im Client prüfen

Lassen Sie den MCP-Client die verfügbaren Tools auflisten oder rufen Sie zuerst einen der schreibgeschützten Helfer auf:

```json
{
  "tool": "get_api_overview",
  "arguments": {}
}
```

Nützliche erste Prüfungen:

| Tool | Was zu prüfen ist |
| --- | --- |
| `get_api_overview` | Bestätigt, dass der Server erreichbar ist und zeigt verfügbare Workflows. |
| `list_supported_languages` | Bestätigt, dass paketierte Sprachdaten geladen werden können. |
| `get_configuration_status` | Bestätigt LLM- und Vision-Provider-Verfügbarkeit, ohne geheime Werte offenzulegen. |

## Schritt 4: Wählen Sie einen Workflow

### Einzelne Dateien oder Dokumente übersetzen

Verwenden Sie provider-gestützte Content-Tools, wenn der MCP-Client bereits Dokumentinhalt oder einen Bildpfad hat und Co-op Translator die konfigurierten Übersetzungsprovider aufrufen soll.

Für Markdown:

1. Rufen Sie `translate_markdown_content` mit `document`, `language_code` und optional `source_path` auf.
2. Wenn das übersetzte Ergebnis in ein Co-op Translator-Ausgabelayout geschrieben werden soll, rufen Sie `rewrite_markdown_paths` auf.
3. Lassen Sie den Client den finalen `content` schreiben oder zurückgeben.

Für Notebooks:

1. Rufen Sie `translate_notebook_content` mit Notebook-JSON und `language_code` auf.
2. Rufen Sie `rewrite_notebook_paths` auf, wenn übersetzte Notebook-Links für einen Zielpfad angepasst werden müssen.
3. Schreiben oder geben Sie das finale Notebook-JSON zurück.

Für Bilder:

1. Rufen Sie `translate_image_content` mit `image_path`, `language_code` und optional `root_dir` oder `fast_mode` auf.
2. Lesen Sie das zurückgegebene `data_base64` und `mime_type`.
3. Wenn `output_path` angegeben ist, wird das übersetzte Bild auch an diesem Pfad gespeichert.

Die Content-Tools führen keine Projekterkennung, Metadatenaktualisierungen, Haftungsausschlüsse oder automatisches Pfadumschreiben durch. Wenn Sie möchten, dass der Host-Agent Markdown- oder Notebook-Chunks ohne Co-op Translator LLM-Provider-Anmeldedaten übersetzt, verwenden Sie den unten beschriebenen agent-unterstützten Workflow.

### Mit dem Host-Agentenmodell übersetzen

Verwenden Sie agent-unterstützte Tools, wenn Sie möchten, dass der MCP-Host-Agent, beispielsweise ein Coding-Assistent, den übersetzten Text erzeugt, anstatt Azure OpenAI oder OpenAI für Co-op Translator zu konfigurieren.

In einem Chat-basierten MCP-Client müssen Sie normalerweise nicht selbst Tool-JSON schreiben. Bitten Sie den Agenten, den agent-unterstützten Workflow zu verwenden:

```text
Translate this Markdown file to Korean with Co-op Translator MCP.
Use agent-assisted mode: call start_markdown_agent_translation, translate the returned chunks with your own model, then call finish_markdown_agent_translation.
Keep Markdown formatting, code blocks, and links intact.
```

Für Notebooks verwenden Sie das gleiche Muster:

```text
Translate this notebook to Korean with Co-op Translator MCP.
Use start_notebook_agent_translation, translate the returned Markdown-cell chunks with your own model, then call finish_notebook_agent_translation.
Preserve code cells, outputs, and notebook metadata.
```

Wenn Ihr MCP-Client Server-Prompts unterstützt, verwenden Sie `agent_assisted_markdown_translation_prompt`, damit der Client dieselben Workflow-Anweisungen lädt.

Für Markdown:

1. Rufen Sie `start_markdown_agent_translation` mit `document`, `language_code` und optional `source_path` auf.
2. Übersetzen Sie jeden zurückgegebenen Chunk im Host-Agenten, indem Sie der Chunk-`prompt` folgen.
3. Rufen Sie `finish_markdown_agent_translation` mit dem ursprünglichen `job` und den übersetzten Chunks unter Verwendung von `chunk_id` und `translated_text` auf.
4. Wenn der Inhalt in einen übersetzten Zielpfad geschrieben werden soll, rufen Sie `rewrite_markdown_paths` auf.

Für Notebooks:

1. Rufen Sie `start_notebook_agent_translation` mit Notebook-JSON und `language_code` auf.
2. Übersetzen Sie jeden zurückgegebenen Chunk im Host-Agenten.
3. Rufen Sie `finish_notebook_agent_translation` mit dem ursprünglichen `job` und den übersetzten Chunks auf.
4. Rufen Sie `rewrite_notebook_paths` auf, wenn übersetzte Notebook-Links für einen Zielpfad angepasst werden müssen.

Agent-unterstützte Tools rufen Azure OpenAI oder OpenAI von Co-op Translator nicht auf. Der Host-Agent ist verantwortlich für die Übersetzung der zurückgegebenen Chunks. Co-op Translator übernimmt das Chunking von Markdown, die Erhaltung von Platzhaltern, die Rekonstruktion von Frontmatter, das Ersetzen von Notebook-Zellen und die Nachbearbeitungs-Normalisierung.

### Ein komplettes Repository übersetzen

Verwenden Sie `run_translation`, wenn der Benutzer möchte, dass Co-op Translator wie die CLI arbeitet.

Die Repository-Übersetzung hat standardmäßig `dry_run=true`, damit ein Agent den Umfang vor Dateiänderungen prüfen kann:

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "dry_run": true
}
```

Um Schreibvorgänge zuzulassen, muss der Aufrufer sowohl `dry_run=false` als auch `confirm_write=true` setzen:

```json
{
  "language_codes": "ko",
  "root_dir": ".",
  "markdown": true,
  "dry_run": false,
  "confirm_write": true
}
```

`translate_project` wird als Kompatibilitätsalias für `run_translation` angeboten.

### Übersetzte Ausgabe überprüfen

Verwenden Sie `run_review` für deterministische Prüfungen, die keine LLM- oder Vision-Anmeldedaten erfordern:

!!! note "Beta"
    MCP stellt die Beta-API `run_review` bereit. Sie ist für schreibgeschützte Review-Workflows sicher, aber Prüfungen und Issue-Schemas können sich weiterentwickeln.

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "notebook": true
}
```

Das Ergebnis enthält erfasste Textausgabe und eine strukturierte Review-Zusammenfassung, wenn verfügbar.

## Manuelle Serverausführungen

Manuelle Ausführungen dienen hauptsächlich zum Debugging oder für Transports, die sich wie lang laufende Server verhalten.

Debuggen Sie den Standard-stdio-Server:

```bash
co-op-translator-mcp
```

Aus einem Source-Checkout ausführen:

```bash
python -m co_op_translator.mcp.server
```

Einen lang lebenden HTTP- oder SSE-Server ausführen:

```bash
co-op-translator-mcp --transport streamable-http
co-op-translator-mcp --transport sse
```

Für lokale Editor- und Agent-Integrationen bevorzugen Sie die clientverwaltete `stdio`-Konfiguration in Schritt 2.

## Werkzeuge

| Tool | Zweck | Schreibt Dateien |
| --- | --- | --- |
| `translate_markdown_content` | Einen Markdown-String übersetzen. | No |
| `translate_notebook_content` | Markdown-Zellen in Notebook-JSON übersetzen. | No |
| `translate_image_content` | Text in einem Bild übersetzen und base64-Bilddaten zurückgeben. | Optional, nur wenn `output_path` angegeben ist |
| `start_markdown_agent_translation` | Markdown-Chunks für den Host-Agenten vorbereiten, damit diese ohne Co-op Translator LLM-Anmeldedaten übersetzt werden. | No |
| `finish_markdown_agent_translation` | Markdown aus den vom Host-Agenten übersetzten Chunks rekonstruieren. | No |
| `start_notebook_agent_translation` | Notebook-Markdown-Zell-Chunks für den Host-Agenten vorbereiten. | No |
| `finish_notebook_agent_translation` | Notebook-JSON aus den vom Host-Agenten übersetzten Chunks rekonstruieren. | No |
| `rewrite_markdown_paths` | Markdown-Body- und Frontmatter-Pfade für ein übersetztes Ziel umschreiben. | No |
| `rewrite_notebook_paths` | Pfade innerhalb von Notebook-Markdown-Zellen umschreiben. | No |
| `run_translation` | Projektweite Übersetzung wie die CLI ausführen. | Yes when `dry_run=false` and `confirm_write=true` |
| `translate_project` | Kompatibilitätsalias für `run_translation`. | Yes when `dry_run=false` and `confirm_write=true` |
| `run_review` | Deterministische Review-Prüfungen durchführen. | No |
| `get_configuration_status` | Konfigurierte LLM- und Vision-Provider melden, ohne Geheimnisse offenzulegen. | No |
| `list_supported_languages` | Unterstützte Zielsprachen-Codes auflisten. | No |
| `get_api_overview` | Verfügbare MCP-Workflows und Tools beschreiben. | No |

## Ressourcen

| Ressourcen-URI | Zweck |
| --- | --- |
| `co-op://api` | JSON-Übersicht über Workflows und Tools. |
| `co-op://supported-languages` | JSON-Liste unterstützter Sprachcodes. |
| `co-op://configuration` | JSON-Zusammenfassung der Provider-Verfügbarkeit ohne Geheimnisse. |

## Prompts

| Prompt | Zweck |
| --- | --- |
| `translate_markdown_document_prompt` | Einen MCP-Client durch die Inhaltsübersetzung sowie optionales Pfadumschreiben führen. |
| `agent_assisted_markdown_translation_prompt` | Einen MCP-Client durch die Host-Agenten-Markdown-Übersetzung führen, ohne Co-op Translator LLM-Provider-Anmeldedaten. |
| `translate_repository_prompt` | Einen MCP-Client durch eine repository-weite Übersetzung führen, die zuerst einen Dry-Run macht. |

## Copy-Paste-Beispiele

Markdown-Inhalt übersetzen:

```json
{
  "tool": "translate_markdown_content",
  "arguments": {
    "document": "# Hello\n\nWelcome to the course.",
    "language_code": "ko",
    "source_path": "docs/guide.md"
  }
}
```

Übersetzte Markdown-Links umschreiben:

```json
{
  "tool": "rewrite_markdown_paths",
  "arguments": {
    "content": "[Setup](../setup.md)\n\n![Hero](../../images/hero.png)",
    "source_path": "docs/guide.md",
    "target_path": "translations/ko/docs/guide.md",
    "policy": {
      "language_code": "ko",
      "root_dir": ".",
      "translations_dir": "translations",
      "translated_images_dir": "translated_images",
      "translation_types": ["markdown", "images"]
    }
  }
}
```

Markdown mit dem Host-Agentenmodell übersetzen:

```json
{
  "tool": "start_markdown_agent_translation",
  "arguments": {
    "document": "# Hello\n\nUse `pip install` to get started.",
    "language_code": "ko",
    "source_path": "docs/guide.md"
  }
}
```

Nachdem der Host-Agent jeden zurückgegebenen Chunk übersetzt hat, beenden Sie den Auftrag mit dem vollständigen `job`-Objekt, das von `start_markdown_agent_translation` zurückgegeben wurde:

```text
tool: finish_markdown_agent_translation
arguments:
  job: <the full job object returned by start_markdown_agent_translation>
  translated_chunks:
    - chunk_id: body:1
      translated_text: "# 안녕하세요\n\n시작하려면 `pip install`을 사용하세요."
```

Vorschau der Repository-Übersetzung:

```json
{
  "tool": "run_translation",
  "arguments": {
    "language_codes": "ko",
    "root_dir": ".",
    "markdown": true,
    "dry_run": true
  }
}
```

## Fehlerbehebung

| Problem | Was zu versuchen ist |
| --- | --- |
| Der MCP-Client kann `co-op-translator-mcp` nicht finden. | Verwenden Sie den absoluten Python-Ausführungs-Pfad und die Source-Checkout-Konfiguration `["-m", "co_op_translator.mcp.server"]`. |
| Der Server wird aufgelistet, aber die Übersetzung schlägt fehl. | Rufen Sie `get_configuration_status` auf und bestätigen Sie, dass ein LLM-Provider verfügbar ist. |
| Sie möchten Markdown- oder Notebook-Übersetzung ohne Azure OpenAI/OpenAI-Schlüssel. | Verwenden Sie `start_markdown_agent_translation` / `finish_markdown_agent_translation` oder die Notebook-Äquivalente, damit der Host-Agent die Chunks übersetzt. |
| Bildübersetzung schlägt fehl. | Bestätigen Sie, dass die Azure AI Vision-Variablen gesetzt sind, und rufen Sie `get_configuration_status` auf. |
| Repository-Übersetzung schreibt keine Dateien. | Setzen Sie `dry_run=false` und `confirm_write=true` nur nach ausdrücklicher Benutzerfreigabe. |
| Änderungen an der Client-Konfiguration erscheinen nicht. | Starten oder laden Sie den MCP-Client neu. |

## Sicherheitshinweise

- MCP-Tool-Aufrufe werden von der Host-Anwendung modellgesteuert, daher erfolgt die Repository-Übersetzung standardmäßig als Dry-Run.
- Eine vollständige Repository-Übersetzung kann viele Dateien erstellen, aktualisieren oder löschen. Fordern Sie eine ausdrückliche Benutzerfreigabe an, bevor Sie `confirm_write=true` setzen.
- Das Tool für den Konfigurationsstatus gibt niemals API-Schlüssel, Endpunkte oder andere geheime Werte zurück.
- Die Bildübersetzung liefert base64-Bilddaten. Große Bilder können große Tool-Antworten erzeugen.
- Agent-unterstützte Tools liefern Quell-Chunks und Prompts an den MCP-Host. Verwenden Sie sie nur mit Inhalten, die der Benutzer dem Host-Agentenmodell gegenüber freigeben möchte.