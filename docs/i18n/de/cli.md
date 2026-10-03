# CLI-Referenz

Co-op Translator installiert diese Kommandozeilen-Entrypoints:

- `translate`
- `evaluate`
- `migrate-links`
- `co-op-review`
- `co-op-translator-mcp`

Die `translate`, `evaluate`, `migrate-links` und `co-op-review` Befehle werden über `co_op_translator.__main__` weitergeleitet, das die Befehlsimplementierung basierend auf dem aufgerufenen Skriptnamen auswählt. Der MCP-Server verwendet `co_op_translator.mcp.server` direkt.

Wenn Sie sich zwischen CLI, Python-API und MCP entscheiden, beginnen Sie mit [Wählen Sie Ihren Arbeitsablauf](workflows.md).

## Konsolenausgabe

Interaktive Terminals verwenden Rich-Formatierung für Kopfzeile, Fortschritt und Zusammenfassungen. CI- und nicht-interaktive Ausgaben fallen automatisch auf Klartext zurück.

Setzen Sie `CO_OP_TRANSLATOR_OUTPUT_STYLE=plain`, um Klartextausgabe zu erzwingen, oder `CO_OP_TRANSLATOR_OUTPUT_STYLE=rich`, um Rich-Ausgabe zu erzwingen. Setzen Sie `CO_OP_TRANSLATOR_NO_PROGRESS=1`, um Live-Fortschrittsbalken zu unterdrücken und dennoch Zusammenfassungen beizubehalten.

Verwenden Sie `translate --json-events progress.ndjson`, wenn ein anderes System maschinenlesbaren Fortschritt benötigt. Die CLI rendert weiterhin menschenlesbare Ausgaben, während die NDJSON-Datei versionierte `co-op.translation.event.v1`-Ereignisse mit stabilen Feldern wie `type`, `stage_key`, `completed`, `total` und
`current_path` erhält.




## Erstmaliger CLI-Ablauf

Beginnen Sie hier, wenn Sie Co-op Translator von einem Terminal aus verwenden:

1. Konfigurieren Sie einen LLM-Anbieter wie in [Configuration](configuration.md) beschrieben.
2. Wählen Sie den Inhaltstyp, den Sie übersetzen möchten.
3. Führen Sie zuerst einen fokussierten Befehl aus, z. B. nur Markdown-Übersetzung.
4. Verwenden Sie `--dry-run` vor größeren Repository-Änderungen.
5. Verwenden Sie `co-op-review` nach der Übersetzung, um Struktur und Aktualität zu prüfen.

| Ziel | Befehl zum Einstieg |
| --- | --- |
| Translate Markdown documents | `translate -l "ko" -md` |
| Translate notebooks | `translate -l "ko" -nb` |
| Translate image text | `translate -l "ko" -img` |
| Preview work without writing files | `translate -l "ko" -md --dry-run` |
| Review existing translations | `co-op-review -l "ko"` |
| Update notebook and Markdown links | `migrate-links -l "ko" --dry-run` |
| Expose tools to an MCP client | Konfigurieren Sie stattdessen den [MCP-Server](mcp.md), anstatt CLI-Befehle direkt auszuführen. |

## translate

Übersetzt Markdown-Dateien, Notebooks und Bildtext in eine oder mehrere Zielsprachen.

```bash
translate -l "ko ja fr"
```

### Häufige Beispiele

Nur Markdown übersetzen:

```bash
translate -l "de" -md
```

Nur Notebooks übersetzen:

```bash
translate -l "zh-CN" -nb
```

Markdown und Bilder übersetzen:

```bash
translate -l "pt-BR" -md -img
```

Bestehende Übersetzungen durch Löschen und Neuerstellung aktualisieren:

```bash
translate -l "ko" -u
```

Ohne interaktive Eingabeaufforderungen ausführen:

```bash
translate -l "ko ja" -md -y
```

Protokolle speichern:

```bash
translate -l "ko" -s
```

Strukturierte Fortschrittsereignisse schreiben:

```bash
translate -l "ko ja" -md --json-events progress.ndjson
```

### Optionen

| Option | Erforderlich | Beschreibung |
| --- | --- | --- |
| `-l`, `--language-codes` | Ja | Durch Leerzeichen getrennte Sprachcodes, z. B. `"es fr de"`, oder `"all"`. |
| `-r`, `--root-dir` | Nein | Projektstamm. Standard: das aktuelle Verzeichnis. |
| `-u`, `--update` | Nein | Löscht vorhandene Übersetzungen für ausgewählte Sprachen und erstellt sie neu. |
| `-img`, `--images` | Nein | Übersetzt nur Bilddateien. |
| `-md`, `--markdown` | Nein | Übersetzt nur Markdown-Dateien. |
| `-nb`, `--notebook` | Nein | Übersetzt nur Jupyter-Notebook-Dateien. |
| `-d`, `--debug` | Nein | Aktiviert Debug-Logging in der Konsole. |
| `-s`, `--save-logs` | Nein | Speichert DEBUG-Level-Logs unter `<root-dir>/logs/`. |
| `--json-events` | Nein | Schreibt maschinenlesbare Übersetzungs-Fortschrittsevents als NDJSON. |
| `-x`, `--fix` | Nein | Übersetzt Markdown-Dateien mit niedriger Zuverlässigkeit basierend auf vorherigen Bewertungsergebnissen neu. |
| `-c`, `--min-confidence` | Nein | Vertrauensschwelle für `--fix`. Standard: `0.7`. |
| `--add-disclaimer`, `--no-disclaimer` | Nein | Maschinelle Übersetzungs-Hinweise hinzufügen oder unterdrücken. In der CLI standardmäßig aktiviert. |
| `-f`, `--fast` | Nein | Veralteter schneller Bildmodus. |
| `-y`, `--yes` | Nein | Bestätigungen automatisch ausführen, nützlich in CI. |
| `--repo-url` | Nein | Repository-URL, die in der README-Sprachentabelle für Sparse-Checkout-Empfehlungen verwendet wird. |
| `--migrate-language-folders` | Nein | Benennt veraltete Alias-Ordner wie `cn` oder `tw` in kanonische BCP 47-Ordner um. |
| `--dry-run` | Nein | Vorschau der Migration von Sprachordnern und Übersetzungsschätzungen, ohne Dateien zu schreiben. |

Wenn kein Typ-Flag angegeben ist, verarbeitet `translate` Markdown, Notebooks und Bilder. Die Bildübersetzung erfordert die Konfiguration von Azure AI Vision.

## evaluate

Bewertet die Qualität übersetzter Markdown-Dateien für eine Sprache.

!!! warning "Experimentell"
    `evaluate` ist experimentell. Es kann regelbasierte und LLM-basierte Qualitätsprüfungen verwenden, schreibt Bewertungsergebnisse in die Übersetzungsmetadaten, und sein Bewertungsmodell sowie das Verhalten der Metadaten können sich ändern.

```bash
evaluate -l "ko"
```

### Häufige Beispiele

Verwenden Sie einen strengeren Schwellenwert für niedrige Vertrauenswerte:

```bash
evaluate -l "es" -c 0.8
```

Nur regelbasierte Prüfungen ausführen:

```bash
evaluate -l "fr" -f
```

Nur LLM-basierte Prüfungen ausführen:

```bash
evaluate -l "ja" -D
```

### Optionen

| Option | Erforderlich | Beschreibung |
| --- | --- | --- |
| `-l`, `--language-code` | Ja | Einzelner Sprachcode zur Bewertung. Alias-Codes werden normalisiert. |
| `-r`, `--root-dir` | Nein | Projektstamm. Standard: das aktuelle Verzeichnis. |
| `-c`, `--min-confidence` | Nein | Schwellenwert, der beim Auflisten von Übersetzungen mit niedriger Vertrauenswürdigkeit verwendet wird. Standard: `0.7`. |
| `-d`, `--debug` | Nein | Aktiviert Debug-Logging. |
| `-s`, `--save-logs` | Nein | Speichert DEBUG-Level-Logs unter `<root-dir>/logs/`. |
| `-f`, `--fast` | Nein | Nur regelbasierte Bewertung. |
| `-D`, `--deep` | Nein | Nur LLM-basierte Bewertung. |

Standardmäßig verwendet `evaluate` sowohl regelbasierte als auch LLM-basierte Bewertung. Ergebnisse werden in Übersetzungsmetadaten geschrieben und in der Konsole zusammengefasst.

## co-op-review

Führen Sie deterministische Wartungsprüfungen für Übersetzungen ohne API-Anmeldeinformationen durch.

!!! note "Beta"
    `co-op-review` ist ein Beta-Befehl für deterministische Überprüfungen. Er ruft keine Modellanbieter auf und schreibt keine Dateien, aber seine Prüfungen und das Schema der Ausgabe möglicher Probleme können sich weiterentwickeln.

```bash
co-op-review -l "ko"
```

### Häufige Beispiele

Überprüfen Sie koreanische und japanische Übersetzungen aus dem aktuellen Verzeichnis:

```bash
co-op-review -l "ko ja"
```

Ein bestimmtes Projekt-Stammverzeichnis überprüfen:

```bash
co-op-review -l "fr" -r ./my-course
```

Nur das README nach einer reinen README-Übersetzung überprüfen:

```bash
translate -l "ko" --readme-only -y
co-op-review -l "ko" --readme-only --format github
```

`--readme-only` ignoriert andere Dokumente und verschachtelte READMEs. Es schlägt fehl, wenn die Stamm-`README.md` fehlt. In Kombination mit `--changed-from` überprüft es das README nur, wenn diese Quelldatei geändert wurde. Eine README-only-Übersetzung belässt das Quell-README unverändert, einschließlich etwaiger shared-section-Markierungen.




Nur Quell-Dateien überprüfen, die gegenüber einem Basis-Ref geändert wurden:

```bash
co-op-review -l "ko" --changed-from origin/main
```

GitHub-flavored Markdown-Ausgabe für CI-Zusammenfassungen ausgeben:

```bash
co-op-review -l "ko ja" --changed-from origin/main --format github
```

### Optionen

| Option | Erforderlich | Beschreibung |
| --- | --- | --- |
| `-l`, `--language-code` | Nein | Sprachcode zur Überprüfung. Kann mehrfach übergeben oder als durch Leerzeichen getrennter Wert angegeben werden. Standardmäßig alle entdeckten Übersetzungssprachen. |
| `-r`, `--root-dir` | Nein | Projektstamm. Standard: das aktuelle Verzeichnis. |
| `--changed-from` | Nein | Git-Ref, mit dem die Überprüfung auf geänderte Quelldateien begrenzt wird. |
| `--readme-only` | Nein | Überprüft nur die Root-`README.md`-Übersetzung. |
| `--format` | Nein | Ausgabeformat: `text` oder `github`. Standard: `text`. |

`co-op-review` prüft derzeit auf fehlende übersetzte Dateien, fehlende oder veraltete Übersetzungs-Metadaten, Integrität von Markdown-Frontmatter und Code-Fences, ungültiges übersetztes Notebook-JSON und fehlende lokale Markdown- oder Bild-Linkziele. Fehlende Links sind standardmäßig Warnungen; strukturelle und Aktualitätsprobleme führen zum Fehlschlag des Befehls.

## co-op-translator-mcp

Starten Sie den Co-op Translator MCP-Server für Agents, Editoren und MCP-kompatible Clients.

```bash
co-op-translator-mcp
```

Der Standardtransport ist `stdio`. Siehe die Anleitung zum [MCP-Server](mcp.md) für Client-Konfiguration, Tools, Ressourcen und Sicherheitshinweise.

### Optionen

| Option | Erforderlich | Beschreibung |
| --- | --- | --- |
| `--transport` | Nein | MCP-Transport: `stdio`, `streamable-http` oder `sse`. Standard: `stdio`. |

## migrate-links

Verarbeitet übersetzte Markdown-Dateien erneut und aktualisiert Notebook-Links, sodass sie bei Verfügbarkeit auf übersetzte Notebooks verweisen.

```bash
migrate-links -l "ko ja"
```

### Häufige Beispiele

Vorschau der Link-Updates:

```bash
migrate-links -l "ko" --dry-run
```

Alle unterstützten Sprachen ohne Bestätigung verarbeiten:

```bash
migrate-links -l "all" -y
```

Links nur umschreiben, wenn übersetzte Notebooks vorhanden sind:

```bash
migrate-links -l "ko" --no-fallback-to-original
```

### Optionen

| Option | Erforderlich | Beschreibung |
| --- | --- | --- |
| `-l`, `--language-codes` | Ja | Durch Leerzeichen getrennte Sprachcodes oder `"all"`. |
| `-r`, `--root-dir` | Nein | Projektstamm. Standard: das aktuelle Verzeichnis. |
| `--image-dir` | Nein | Verzeichnis für übersetzte Bilder relativ zum Root. Standard: `translated_images`. |
| `--dry-run` | Nein | Zeigt Dateien, die sich ändern würden, ohne Aktualisierungen zu schreiben. |
| `--fallback-to-original`, `--no-fallback-to-original` | Nein | Verwendet Original-Notebook-Links, wenn übersetzte Notebooks fehlen. Standardmäßig aktiviert. |
| `-d`, `--debug` | Nein | Aktiviert Debug-Logging. |
| `-s`, `--save-logs` | Nein | Speichert DEBUG-Level-Logs unter `<root-dir>/logs/`. |
| `-y`, `--yes` | Nein | Bestätigungen automatisch ausführen, wenn alle Sprachen verarbeitet werden. |

## Umgebung

Wenn ein Befehl Anbieteranmeldeinformationen erfordert, konfigurieren Sie eines dieser Anbieter-Sets. `translate --dry-run` und `co-op-review` benötigen keine Anbieteranmeldeinformationen:

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

Die Bildübersetzung erfordert zusätzlich Azure AI Vision:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

## Ausgabe-Layout

Textübersetzungen werden unter folgendem Pfad geschrieben:

```text
translations/<language-code>/<original-path>
```

Die Ausgabe übersetzter Bilder wird unter folgendem Pfad geschrieben:

```text
translated_images/<language-code>/<original-path>
```

Beispielsweise erzeugt die Übersetzung von `README.md` und `docs/setup.md` ins Koreanische:

```text
translations/ko/README.md
translations/ko/docs/setup.md
```

## Copy-Paste-CLI-Beispiele

Markdown in drei Sprachen übersetzen:

```bash
translate -l "ko ja fr" -md
```

Nur Notebooks übersetzen:

```bash
translate -l "zh-CN" -nb
```

Nur Bilder übersetzen:

```bash
translate -l "pt-BR" -img
```

Vorschau der Markdown-Übersetzung ohne Dateien zu schreiben:

```bash
translate -l "de es" -md --dry-run
```

Niedrig-konfidente Markdown-Übersetzungen reparieren:

```bash
evaluate -l "ko" -c 0.8
translate -l "ko" --fix -c 0.8 -md
```

CI-freundliche Markdown-Übersetzung ausführen:

```bash
translate -l "ko ja" -md -y -s
```

Übersetzte Ausgabe überprüfen:

```bash
co-op-review -l "ko ja"
```

Vorschau der Link-Migration:

```bash
migrate-links -l "ko" --dry-run
```