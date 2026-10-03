# MCP Server

Co-op Translator enthält einen Model Context Protocol-Server für Agents, Editoren und MCP-kompatible Clients.

Für die standardmäßige lokale Einrichtung behalten Benutzer keinen separaten Server manuell am Laufen. Sie konfigurieren ihren MCP-Client, und der Client startet `co-op-translator-mcp` automatisch über `stdio`, wenn er Co-op Translator-Tools benötigt.

Wenn Sie sich zwischen CLI, Python-API und MCP entscheiden, beginnen Sie mit [Choose Your Workflow](workflows.md).

Verwenden Sie MCP, wenn ein Agent oder Editor Co-op Translator direkt aufrufen sollte:

| User goal | MCP tools |
| --- | --- |
| Ein Markdown-Dokument, ein Notebook oder ein Bild übersetzen | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content` |
| Markdown- oder Notebook-Inhalte mit dem Host-Agent-Modell übersetzen | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Übersetzte Markdown- oder Notebook-Links nach Auswahl des Ausgabepfads umschreiben | `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Ein vollständiges Repository wie mit dem CLI übersetzen | `run_translation`, `translate_project` |
| Übersetzte Ausgabe ohne LLM-Anmeldeinformationen überprüfen | `run_review` |
| Inspect capabilities and environment status | `get_api_overview`, `list_supported_languages`, `get_configuration_status` |

Der MCP-Server kapselt dieselbe öffentliche Python-API, die in [Python API](api.md) dokumentiert ist. Tools, die Provider verwenden, nutzen dieselben konfigurierten Provider wie die CLI und die Python-API. Agent-unterstützte Tools bereiten Chunks für den MCP-Host-Agenten zur Übersetzung vor und verwenden dann Co-op Translator, um das finale Markdown oder Notebook wiederherzustellen.

## Schritt 1: Co-op Translator installieren und konfigurieren

Installieren Sie Co-op Translator in der Python-Umgebung, die Ihr MCP-Client verwenden wird:

```bash
pip install co-op-translator
```

Für die lokale Entwicklung aus diesem Repository installieren Sie das Paket im Editable-Modus:

```bash
pip install -e .
```

Wählen Sie den Übersetzungsmodus, den Ihr MCP-Client verwenden wird:

| Mode | Use this for | Credentials |
| --- | --- | --- |
| Anbieter-gestützt | Der Co-op Translator ruft `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, oder `run_translation` auf. | Die Übersetzung erfordert Azure OpenAI, OpenAI oder Anthropic. Die Bildübersetzung erfordert außerdem Azure AI Vision. |
| Agent-gestützt | Der MCP-Host-Agent übersetzt Chunks, die von `start_markdown_agent_translation` oder `start_notebook_agent_translation` zurückgegeben werden. | Für Markdown- oder Notebook-Chunks sind keine Anmeldeinformationen für den Co-op Translator LLM-Anbieter erforderlich. Die Bildübersetzung wird im agentgestützten Modus noch nicht unterstützt. |

Wenn Sie mit Markdown- oder Notebook-Übersetzung innerhalb eines Agents wie Codex oder Claude Code beginnen, starten Sie mit dem agent-unterstützten Modus. Verwenden Sie den provider-gestützten Modus, wenn Co-op Translator selbst Ihre konfigurierten Provider aufrufen soll, wenn Sie Bilder übersetzen oder wenn Sie repositoryweite Übersetzungen wie mit der CLI durchführen.

Konfigurieren Sie einen Provider für provider-gestützte Workflows:

```bash
# Azure OpenAI
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"

# Oder OpenAI
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"

# Oder Anthropic
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

Provider-gestützte Bildübersetzung benötigt zusätzlich:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

!!! note
    Der Agent-gestützte Modus deckt derzeit Markdown- und Notebook-Markdown-Zellen ab. Die Bildübersetzung verwendet weiterhin die anbietergestützte Bildpipeline und erfordert Azure AI Vision für OCR und layoutbewusste Darstellung.

## Schritt 2: Ihren MCP-Client konfigurieren

Für die normale lokale `stdio`-Konfiguration fügen Sie Co-op Translator Ihrer MCP-Client-Konfiguration hinzu. Der Client startet und stoppt den Prozess automatisch.

Installierte Paketkonfiguration:

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

Nach dem Ändern der MCP-Client-Konfiguration starten oder laden Sie den Client neu, damit er den neuen Server entdecken kann.

## Schritt 3: Den Server im Client überprüfen

Bitten Sie den MCP-Client, verfügbare Tools aufzulisten, oder rufen Sie zuerst einen der schreibgeschützten Helfer auf:

```json
{
  "tool": "get_api_overview",
  "arguments": {}
}
```

Nützliche erste Prüfungen:

| Tool | What to check |
| --- | --- |
| `get_api_overview` | Bestätigt, dass der Server erreichbar ist und zeigt verfügbare Workflows. |
| `list_supported_languages` | Bestätigt, dass gepackte Sprachdaten geladen werden können. |
| `get_configuration_status` | Bestätigt die Verfügbarkeit von LLM- und Vision-Providern, ohne geheime Werte offenzulegen. |

## Schritt 4: Einen Arbeitsablauf wählen

### Einzelne Dateien oder Dokumente übersetzen

Verwenden Sie provider-gestützte Content-Tools, wenn der MCP-Client bereits Dokumenteninhalt oder einen Bildpfad hat und Co-op Translator die konfigurierten Übersetzungs-Provider aufrufen soll.

Für Markdown:

1. Rufen Sie `translate_markdown_content` mit `document`, `language_code` und optional `source_path` auf.
2. Wenn das übersetzte Ergebnis in ein Co-op Translator-Ausgabelayout geschrieben werden soll, rufen Sie `rewrite_markdown_paths` auf.
3. Lassen Sie den Client den finalen `content` schreiben oder zurückgeben.

Für Notebooks:

1. Rufen Sie `translate_notebook_content` mit dem Notebook-JSON und `language_code` auf.
2. Rufen Sie `rewrite_notebook_paths` auf, wenn übersetzte Notebook-Links für einen Zielpfad angepasst werden müssen.
3. Schreiben oder geben Sie das finale Notebook-JSON zurück.

Für Bilder:

1. Rufen Sie `translate_image_content` mit `image_path`, `language_code` und optional `root_dir` oder `fast_mode` auf.
2. Lesen Sie das zurückgegebene `data_base64` und `mime_type`.
3. Wenn `output_path` angegeben ist, wird das übersetzte Bild auch an diesem Pfad gespeichert.

Die Content-Tools führen keine Projekterkennung, Metadatenaktualisierungen, Haftungsausschlüsse oder automatische Pfadumschreibungen durch. Wenn Sie möchten, dass der Host-Agent Markdown- oder Notebook-Chunks ohne Co-op Translator-LLM-Provider-Anmeldeinformationen übersetzt, verwenden Sie den untenstehenden agent-unterstützten Workflow.

### Mit dem Host-Agent-Modell übersetzen

Verwenden Sie agent-unterstützte Tools, wenn Sie möchten, dass der MCP-Host-Agent, z. B. ein Coding-Assistent, den übersetzten Text erzeugt, anstatt einen LLM-Provider für Co-op Translator zu konfigurieren.

In einem chatbasierten MCP-Client müssen Sie normalerweise kein Tool-JSON selbst schreiben. Bitten Sie den Agenten, den agent-unterstützten Workflow zu verwenden:

```text
Translate this Markdown file to Korean with Co-op Translator MCP.
Use agent-assisted mode: call start_markdown_agent_translation, translate the returned chunks with your own model, then call finish_markdown_agent_translation.
Keep Markdown formatting, code blocks, and links intact.
```

Für Notebooks verwenden Sie dasselbe Muster:

```text
Translate this notebook to Korean with Co-op Translator MCP.
Use start_notebook_agent_translation, translate the returned Markdown-cell chunks with your own model, then call finish_notebook_agent_translation.
Preserve code cells, outputs, and notebook metadata.
```

Wenn Ihr MCP-Client Server-Prompts unterstützt, verwenden Sie `agent_assisted_markdown_translation_prompt`, damit der Client dieselben Workflow-Anweisungen lädt.

Für Markdown:

1. Rufen Sie `start_markdown_agent_translation` mit `document`, `language_code` und optional `source_path` auf.
2. Übersetzen Sie jedes zurückgegebene Chunk im Host-Agenten, indem Sie dem Chunk-`prompt` folgen.
3. Rufen Sie `finish_markdown_agent_translation` mit dem ursprünglichen `job` und den übersetzten Chunks unter Verwendung von `chunk_id` und `translated_text` auf.
4. Wenn der Inhalt in einen übersetzten Zielpfad geschrieben werden soll, rufen Sie `rewrite_markdown_paths` auf.

Für Notebooks:

1. Rufen Sie `start_notebook_agent_translation` mit dem Notebook-JSON und `language_code` auf.
2. Übersetzen Sie jedes zurückgegebene Chunk im Host-Agenten.
3. Rufen Sie `finish_notebook_agent_translation` mit dem ursprünglichen `job` und den übersetzten Chunks auf.
4. Rufen Sie `rewrite_notebook_paths` auf, wenn übersetzte Notebook-Links an Zielpfade angepasst werden müssen.

Agent-unterstützte Tools rufen den konfigurierten LLM-Provider von Co-op Translator nicht auf. Der Host-Agent ist verantwortlich für die Übersetzung der zurückgegebenen Chunks. Co-op Translator kümmert sich um Markdown-Chunking, Platzhalter-Erhaltung, Frontmatter-Wiederherstellung, Ersatz von Notebook-Zellen und Nachübersetzungs-Normalisierung.

### Ein gesamtes Repository übersetzen

Verwenden Sie `run_translation`, wenn der Benutzer möchte, dass Co-op Translator wie das `translate`-CLI arbeitet.

Die Repository-Übersetzung verwendet standardmäßig `dry_run=true`, damit ein Agent den Umfang vor Dateiänderungen prüfen kann:

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "dry_run": true
}
```

Das `run_translation`-Ergebnis enthält ein `events`-Array mit versionierten
`co-op.translation.event.v1`-Fortschrittsereignissen. MCP-Clients sollten Felder wie
`type`, `stage_key`, `completed`, `total` und `current_path` verwenden, anstatt
erfassten Konsolentext zu parsen. Geben Sie `json_events_path` an, um diese Ereignisse
zusätzlich in eine NDJSON-Datei zu schreiben.

Um Schreibvorgänge zu ermöglichen, muss der Aufrufer sowohl `dry_run=false` als auch `confirm_write=true` setzen:

```json
{
  "language_codes": "ko",
  "root_dir": ".",
  "markdown": true,
  "dry_run": false,
  "confirm_write": true
}
```

`translate_project` wird als Kompatibilitätsalias für `run_translation` bereitgestellt.

### Übersetzte Ausgabe überprüfen

Verwenden Sie `run_review` für deterministische Prüfungen, die keine LLM- oder Vision-Anmeldeinformationen erfordern:

!!! note "Beta"
    MCP stellt die Beta-API `run_review` bereit. Sie ist sicher für schreibgeschützte Review-Workflows, aber Review-Prüfungen und Issue-Schemata können sich weiterentwickeln.

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "notebook": true
}
```

Das Ergebnis enthält erfasste Textausgabe und eine strukturierte Review-Zusammenfassung, wenn verfügbar.

## Manuelle Serverläufe

Manuelle Ausführungen dienen hauptsächlich zum Debugging oder für Transports, die sich wie lang laufende Server verhalten.

Debuggen Sie den Standard-stdio-Server:

```bash
co-op-translator-mcp
```

Aus einem Source-Checkout ausführen:

```bash
python -m co_op_translator.mcp.server
```

Einen lang laufenden HTTP- oder SSE-Server ausführen:

```bash
co-op-translator-mcp --transport streamable-http
co-op-translator-mcp --transport sse
```

Für lokale Editor- und Agent-Integrationen bevorzugen Sie die vom Client verwaltete `stdio`-Konfiguration in Schritt 2.

## Tools

| Tool | Purpose | Writes files |
| --- | --- | --- |
| `translate_markdown_content` | Translate a Markdown string. | No |
| `translate_notebook_content` | Markdown-Zellen im Notebook-JSON übersetzen. | Nein |
| `translate_image_content` | Text in einem Bild übersetzen und Base64-Bilddaten zurückgeben. | Optional, nur wenn `output_path` angegeben ist |
| `start_markdown_agent_translation` | Markdown-Chunks für den Host-Agent vorbereiten, damit dieser sie ohne Anmeldeinformationen für den Co-op Translator LLM-Anbieter übersetzt. | Nein |
| `finish_markdown_agent_translation` | Markdown aus vom Host-Agenten übersetzten Abschnitten rekonstruieren. | Nein |
| `start_notebook_agent_translation` | Markdown-Zellen eines Notebooks für den Host-Agent vorbereiten, damit dieser sie übersetzt. | Nein |
| `finish_notebook_agent_translation` | Notebook-JSON aus vom Host-Agenten übersetzten Abschnitten rekonstruieren. | Nein |
| `rewrite_markdown_paths` | Markdown-Inhalt und Frontmatter-Pfade für ein übersetztes Ziel umschreiben. | Nein |
| `rewrite_notebook_paths` | Pfade in den Markdown-Zellen des Notebooks umschreiben. | Nein |
| `run_translation` | Projektweite Übersetzung wie mit dem CLI ausführen. | Ja, wenn `dry_run=false` und `confirm_write=true` |
| `translate_project` | Compatibility alias for `run_translation`. | Yes when `dry_run=false` and `confirm_write=true` |
| `run_review` | Run deterministic review checks. | No |
| `get_configuration_status` | Konfigurierte LLM- und Vision-Anbieter melden, ohne Geheimnisse offenzulegen. | Nein |
| `list_supported_languages` | List supported target language codes. | No |
| `get_api_overview` | Verfügbare MCP-Workflows und -Tools beschreiben. | Nein |

## Resources

| Resource URI | Purpose |
| --- | --- |
| `co-op://api` | JSON-Übersicht der Workflows und Tools. |
| `co-op://supported-languages` | JSON-Liste der unterstützten Sprachcodes. |
| `co-op://configuration` | JSON-Zusammenfassung der Provider-Verfügbarkeit ohne Geheimnisse. |

## Prompts

| Prompt | Purpose |
| --- | --- |
| `translate_markdown_document_prompt` | Einen MCP-Client durch die Inhaltsübersetzung und optionales Umschreiben von Pfaden führen. |
| `agent_assisted_markdown_translation_prompt` | Einen MCP-Client durch die Host-Agent-gestützte Markdown-Übersetzung führen, ohne Anmeldeinformationen für den Co-op Translator LLM-Anbieter. |
| `translate_repository_prompt` | Einen MCP-Client durch eine Repository-Übersetzung führen, die zuerst einen Dry-Run durchführt. |

## Beispiele zum Kopieren und Einfügen

Translate Markdown content:

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

Rewrite translated Markdown links:

```json
{
  "tool": "rewrite_markdown_paths",
  "arguments": {
    "content": "[Setup](../setup.md)\n\n![Hero](images/hero.png)",
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

Markdown mit dem Host-Agenten-Modell übersetzen:

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

Nachdem der Host-Agent jeden zurückgegebenen Chunk übersetzt hat, beende den Job mit dem vollständigen `job`-Objekt, das von `start_markdown_agent_translation` zurückgegeben wurde:

```text
tool: finish_markdown_agent_translation
arguments:
  job: <the full job object returned by start_markdown_agent_translation>
  translated_chunks:
    - chunk_id: body:1
      translated_text: "# 안녕하세요\n\n시작하려면 `pip install`을 사용하세요."
```

Preview repository translation:

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

## Troubleshooting

| Problem | What to try |
| --- | --- |
| Der MCP-Client kann `co-op-translator-mcp` nicht finden. | Verwenden Sie den absoluten Pfad zur Python-Executable und die `["-m", "co_op_translator.mcp.server"]`-Source-Checkout-Konfiguration. |
| Der Server ist aufgelistet, aber die Übersetzung schlägt fehl. | Rufen Sie `get_configuration_status` auf und bestätigen Sie, dass ein LLM-Anbieter verfügbar ist. |
| Sie möchten Markdown- oder Notebook-Übersetzung ohne Anbieter-Anmeldeinformationen. | Verwenden Sie `start_markdown_agent_translation` / `finish_markdown_agent_translation` oder die Notebook-Entsprechungen, damit der Host-Agent die Chunks übersetzt. |
| Die Bildübersetzung schlägt fehl. | Stellen Sie sicher, dass die Azure AI Vision-Variablen gesetzt sind, und rufen Sie `get_configuration_status` auf. |
| Die Repository-Übersetzung schreibt keine Dateien. | Setzen Sie `dry_run=false` und `confirm_write=true` nur nach ausdrücklicher Zustimmung des Benutzers. |
| Änderungen an der Client-Konfiguration erscheinen nicht. | Starten oder laden Sie den MCP-Client neu. |

## Sicherheitshinweise

- MCP-Toolaufrufe werden von der Host-Anwendung modellgesteuert, daher ist die Repository-Übersetzung standardmäßig ein Dry-Run.
- Eine vollständige Repository-Übersetzung kann viele Dateien erstellen, aktualisieren oder entfernen. Fordern Sie eine ausdrückliche Benutzerbestätigung an, bevor Sie `confirm_write=true` setzen.
- Das Konfigurationsstatus-Tool gibt niemals API-Schlüssel, Endpunkte oder andere geheime Werte zurück.
- Die Bildübersetzung liefert Base64-Bilddaten zurück. Große Bilder können große Tool-Antworten erzeugen.
- Agent-gestützte Tools geben Quell-Chunks und Prompts an den MCP-Host zurück. Verwenden Sie sie nur mit Inhalten, die der Benutzer bereit ist, an dieses Host-Agent-Modell zu senden.
