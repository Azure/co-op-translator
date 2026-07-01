# CLI-Referenz

Co-op Translator installiert diese Befehlszeilen-Einstiegspunkte:

- `translate`
- `evaluate`
- `migrate-links`
- `co-op-review`
- `co-op-translator-mcp`

Die Befehle `translate`, `evaluate`, `migrate-links` und `co-op-review` werden über `co_op_translator.__main__` weitergeleitet, das die Implementierung des Befehls basierend auf dem aufgerufenen Skriptnamen auswählt. Der MCP-Server verwendet `co_op_translator.mcp.server` direkt.

Wenn Sie zwischen CLI, Python-API und MCP entscheiden, beginnen Sie mit [Wählen Sie Ihren Workflow](workflows.md).

## Erster CLI-Ablauf

Beginnen Sie hier, wenn Sie Co-op Translator vom Terminal aus verwenden:

1. Konfigurieren Sie einen LLM-Anbieter wie in [Configuration](configuration.md) beschrieben.
2. Wählen Sie den Inhaltstyp, den Sie übersetzen möchten.
3. Führen Sie zuerst einen fokussierten Befehl aus, z. B. nur Markdown-Übersetzung.
4. Verwenden Sie `--dry-run` vor umfangreichen Repository-Änderungen.
5. Verwenden Sie `co-op-review` nach der Übersetzung, um Struktur und Aktualität zu prüfen.

| Ziel | Empfohlener Startbefehl |
| --- | --- |
| Translate Markdown documents | `translate -l "ko" -md` |
| Translate notebooks | `translate -l "ko" -nb` |
| Translate image text | `translate -l "ko" -img` |
| Preview work without writing files | `translate -l "ko" -md --dry-run` |
| Review existing translations | `co-op-review -l "ko"` |
| Update notebook and Markdown links | `migrate-links -l "ko" --dry-run` |
| Expose tools to an MCP client | Configure the [MCP-Server](mcp.md) instead of running CLI commands directly. |

## translate

Translate Markdown files, notebooks, and image text into one or more target languages.

```bash
translate -l "ko ja fr"
```

### Häufige Beispiele

Translate only Markdown:

```bash
translate -l "de" -md
```

Translate only notebooks:

```bash
translate -l "zh-CN" -nb
```

Translate Markdown and images:

```bash
translate -l "pt-BR" -md -img
```

Update existing translations by deleting and recreating them:

```bash
translate -l "ko" -u
```

Run without interactive prompts:

```bash
translate -l "ko ja" -md -y
```

Save logs:

```bash
translate -l "ko" -s
```

### Optionen

| Option | Erforderlich | Beschreibung |
| --- | --- | --- |
| `-l`, `--language-codes` | Ja | Leerzeichen-getrennte Sprachcodes, z. B. `"es fr de"`, oder `"all"`. |
| `-r`, `--root-dir` | Nein | Projektstamm. Standardmäßig das aktuelle Verzeichnis. |
| `-u`, `--update` | Nein | Löscht vorhandene Übersetzungen für ausgewählte Sprachen und erstellt sie neu. |
| `-img`, `--images` | Nein | Übersetzt nur Bilddateien. |
| `-md`, `--markdown` | Nein | Übersetzt nur Markdown-Dateien. |
| `-nb`, `--notebook` | Nein | Übersetzt nur Jupyter-Notebook-Dateien. |
| `-d`, `--debug` | Nein | Aktiviert Debug-Logging in der Konsole. |
| `-s`, `--save-logs` | Nein | Speichert DEBUG-Level-Logs unter `<root-dir>/logs/`. |
| `-x`, `--fix` | Nein | Übersetzt erneut Markdown-Dateien mit niedriger Konfidenz basierend auf früheren Bewertungsergebnissen. |
| `-c`, `--min-confidence` | Nein | Konfidenz-Schwelle für `--fix`. Standardwert ist `0.7`. |
| `--add-disclaimer`, `--no-disclaimer` | Nein | Haftungsausschluss für maschinelle Übersetzungen hinzufügen oder unterdrücken. In der CLI standardmäßig aktiviert. |
| `-f`, `--fast` | Nein | Veralteter schneller Bildmodus. |
| `-y`, `--yes` | Nein | Bestätigungen automatisch annehmen, nützlich in CI. |
| `--repo-url` | Nein | Repository-URL, die in der README-Sprachentabelle für Sparse-Checkout-Hinweise verwendet wird. |
| `--migrate-language-folders` | Nein | Benennt veraltete Alias-Ordner, wie `cn` oder `tw`, in kanonische BCP 47-Ordner um. |
| `--dry-run` | Nein | Vorschau der Migration von Sprachordnern und Übersetzungsschätzungen ohne Schreibvorgänge. |

Wenn kein Typ-Flag angegeben wird, verarbeitet `translate` Markdown, Notebooks und Bilder. Die Bildübersetzung erfordert eine Azure AI Vision-Konfiguration.

## evaluate

Evaluate translated Markdown quality for one language.

!!! warning "Experimental"
    `evaluate` is experimental. It can use rule-based and LLM-based quality checks, writes evaluation results into translation metadata, and its scoring model and metadata behavior may change.

```bash
evaluate -l "ko"
```

### Häufige Beispiele

Use a stricter low-confidence threshold:

```bash
evaluate -l "es" -c 0.8
```

Run rule-based checks only:

```bash
evaluate -l "fr" -f
```

Run LLM-based checks only:

```bash
evaluate -l "ja" -D
```

### Optionen

| Option | Erforderlich | Beschreibung |
| --- | --- | --- |
| `-l`, `--language-code` | Ja | Einzelner Sprachcode zur Bewertung. Alias-Codes werden normalisiert. |
| `-r`, `--root-dir` | Nein | Projektstamm. Standardmäßig das aktuelle Verzeichnis. |
| `-c`, `--min-confidence` | Nein | Schwelle, die beim Auflisten von Übersetzungen mit niedriger Konfidenz verwendet wird. Standardwert `0.7`. |
| `-d`, `--debug` | Nein | Debug-Logging aktivieren. |
| `-s`, `--save-logs` | Nein | Speichert DEBUG-Level-Logs unter `<root-dir>/logs/`. |
| `-f`, `--fast` | Nein | Nur regelbasierte Auswertung. |
| `-D`, `--deep` | Nein | Nur LLM-basierte Auswertung. |

Standardmäßig verwendet `evaluate` sowohl regelbasierte als auch LLM-basierte Auswertungen. Ergebnisse werden in die Übersetzungs-Metadaten geschrieben und in der Konsole zusammengefasst.

## co-op-review

Run deterministic translation maintenance checks without API credentials.

!!! note "Beta"
    `co-op-review` is a beta deterministic review command. It does not call model providers or write files, but its checks and issue output schema may evolve.

```bash
co-op-review -l "ko"
```

### Häufige Beispiele

Review Korean and Japanese translations from the current directory:

```bash
co-op-review -l "ko ja"
```

Review a specific project root:

```bash
co-op-review -l "fr" -r ./my-course
```

Review only source files changed against a base ref:

```bash
co-op-review -l "ko" --changed-from origin/main
```

Print GitHub-flavored Markdown output for CI summaries:

```bash
co-op-review -l "ko ja" --changed-from origin/main --format github
```

### Optionen

| Option | Erforderlich | Beschreibung |
| --- | --- | --- |
| `-l`, `--language-code` | Nein | Sprachcode zur Überprüfung. Kann mehrfach übergeben oder als Leerzeichen-getrennter Wert angegeben werden. Standardmäßig alle entdeckten Übersetzungssprachen. |
| `-r`, `--root-dir` | Nein | Projektstamm. Standardmäßig das aktuelle Verzeichnis. |
| `--changed-from` | Nein | Git-Ref, der verwendet wird, um die Überprüfung auf geänderte Quelldateien zu beschränken. |
| `--format` | Nein | Ausgabeformat: `text` oder `github`. Standard ist `text`. |

`co-op-review` überprüft derzeit auf fehlende übersetzte Dateien, fehlende oder veraltete Übersetzungs-Metadaten, Integrität von Markdown-Frontmatter und Code-Fences, ungültiges übersetztes Notebook-JSON und fehlende lokale Markdown- oder Bild-Linkziele. Fehlende Links sind standardmäßig Warnungen; strukturelle und Aktualitätsprobleme führen zum Scheitern des Befehls.

## co-op-translator-mcp

Run the Co-op Translator MCP server for agents, editors, and MCP-compatible clients.

```bash
co-op-translator-mcp
```

The default transport is `stdio`. See the [MCP-Server](mcp.md) guide for client configuration, tools, resources, and safety notes.

### Optionen

| Option | Erforderlich | Beschreibung |
| --- | --- | --- |
| `--transport` | Nein | MCP-Transport: `stdio`, `streamable-http`, oder `sse`. Standard ist `stdio`. |

## migrate-links

Reprocess translated Markdown files and update notebook links so they point to translated notebooks when available.

```bash
migrate-links -l "ko ja"
```

### Häufige Beispiele

Preview link updates:

```bash
migrate-links -l "ko" --dry-run
```

Process all supported languages without confirmation:

```bash
migrate-links -l "all" -y
```

Only rewrite links when translated notebooks exist:

```bash
migrate-links -l "ko" --no-fallback-to-original
```

### Optionen

| Option | Erforderlich | Beschreibung |
| --- | --- | --- |
| `-l`, `--language-codes` | Ja | Leerzeichen-getrennte Sprachcodes, oder `"all"`. |
| `-r`, `--root-dir` | Nein | Projektstamm. Standardmäßig das aktuelle Verzeichnis. |
| `--image-dir` | Nein | Verzeichnis der übersetzten Bilder relativ zum Projektstamm. Standard ist `translated_images`. |
| `--dry-run` | Nein | Zeigt Dateien an, die sich ändern würden, ohne Aktualisierungen zu schreiben. |
| `--fallback-to-original`, `--no-fallback-to-original` | Nein | Original-Notebook-Links verwenden, wenn übersetzte Notebooks fehlen. Standardmäßig aktiviert. |
| `-d`, `--debug` | Nein | Debug-Logging aktivieren. |
| `-s`, `--save-logs` | Nein | Speichert DEBUG-Level-Logs unter `<root-dir>/logs/`. |
| `-y`, `--yes` | Nein | Bestätigungen automatisch annehmen beim Verarbeiten aller Sprachen. |

## Umgebung

Alle Befehle benötigen einen konfigurierten LLM-Anbieter:

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
```

Image translation additionally requires Azure AI Vision:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

## Ausgabe-Layout

Textübersetzungen werden abgelegt unter:

```text
translations/<language-code>/<original-path>
```

Ausgabe der übersetzten Bilder wird abgelegt unter:

```text
translated_images/<language-code>/<original-path>
```

For example, translating `README.md` and `docs/setup.md` into Korean produces:

```text
translations/ko/README.md
translations/ko/docs/setup.md
```

## Copy-Paste-CLI-Beispiele

Translate Markdown into three languages:

```bash
translate -l "ko ja fr" -md
```

Translate notebooks only:

```bash
translate -l "zh-CN" -nb
```

Translate images only:

```bash
translate -l "pt-BR" -img
```

Preview Markdown translation without writing files:

```bash
translate -l "de es" -md --dry-run
```

Repair low-confidence Markdown translations:

```bash
evaluate -l "ko" -c 0.8
translate -l "ko" --fix -c 0.8 -md
```

Run CI-friendly Markdown translation:

```bash
translate -l "ko ja" -md -y -s
```

Review translated output:

```bash
co-op-review -l "ko ja"
```

Preview link migration:

```bash
migrate-links -l "ko" --dry-run
```