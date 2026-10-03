# Maintainer-Leitfaden

Diese Seite fasst zusammen, wie API, CLI und die Dokumentationsseite miteinander verknüpft sind.

## Öffentliche API-Grenze

Die stabile Python-API wird exportiert aus:

```python
co_op_translator.api
```

Die öffentliche API ist in Helfer für Inhaltsübersetzung, Helfer für Pfadumschreibung, Projektorchestrierung und Überprüfung organisiert:

```python
from co_op_translator.api import (
    ImageTranslationOptions,
    MarkdownTranslationOptions,
    NotebookTranslationOptions,
    TranslationBaseline,
    TranslationStateProvider,
    TranslationUpdate,
    run_review,
    run_translation,
    rewrite_markdown_paths,
    rewrite_notebook_paths,
    translate_image_content,
    translate_markdown_content,
    translate_notebook_content,
    translate_project,
)
```

`TranslationStateProvider` ist die Persistenz-Grenze für gehostete Integrationen.
Es muss generierte Kandidaten von akzeptierten Baselines getrennt halten, damit eine
nicht zusammengeführte Übersetzung nicht zur Quelle der Wahrheit wird.

Beim Hinzufügen neuer öffentlicher APIs aktualisieren:

- `src/co_op_translator/api/__init__.py`
- `docs/api.md`
- relevante API-Tests unter `tests/co_op_translator/`, wie z. B. `test_api.py` oder `test_review_api.py`

Vermeide es, niedrigere `core`-Module als stabile API zu dokumentieren, sofern das Projekt nicht beabsichtigt, diese direkt zu unterstützen.

## CLI-Einstiegspunkte

Das Paket definiert diese Poetry-Skripte:

```toml
[tool.poetry.scripts]
translate = "co_op_translator.__main__:main"
evaluate = "co_op_translator.__main__:main"
migrate-links = "co_op_translator.__main__:main"
co-op-review = "co_op_translator.__main__:main"
co-op-translator-mcp = "co_op_translator.mcp.server:main"
```

`src/co_op_translator/__main__.py` leitet nach Skriptnamen weiter:

- `translate` ruft `co_op_translator.cli.translate.translate_command` auf
- `evaluate` ruft `co_op_translator.cli.evaluate.evaluate_command` auf
- `migrate-links` ruft `co_op_translator.cli.migrate_links.migrate_links_command` auf
- `co-op-review` ruft `co_op_translator.cli.review.review_command` auf

`co-op-translator-mcp` umgeht `__main__.py` und ruft `co_op_translator.mcp.server:main` direkt auf.

Beim Hinzufügen oder Ändern von CLI-Optionen aktualisieren:

- den relevanten `src/co_op_translator/cli/*.py`-Befehl
- `docs/cli.md`
- CLI-bezogene Tests, falls sich das Verhalten ändert

## MCP-Server

Der MCP-Server ist implementiert in:

```python
co_op_translator.mcp.server
```

Der Server kapselt bewusst die öffentliche Python-API, anstatt niedrigere `core`-Module direkt aufzurufen. Diese Grenze sollte beibehalten werden, damit MCP-Clients, Python-Aufrufer und die CLI dasselbe Verhalten teilen.

Beim Hinzufügen oder Ändern von MCP-Tools aktualisieren:

- `src/co_op_translator/mcp/server.py`
- `tests/co_op_translator/test_mcp_server.py`
- `docs/mcp.md`
- `docs/api.md`, wenn sich die öffentliche API-Oberfläche ändert

Die Repository-Übersetzungswerkzeuge sind über MCP modellaufrufbar und können viele Dateien schreiben. Behalte `dry_run=True` als Standard bei und verlange `confirm_write=True`, bevor eine nicht im Dry-Run durchgeführte Projektübersetzung erfolgt.

## Übersetzungsablauf

Der übergeordnete Ablauf der Projektübersetzung ist:

1. CLI-Argumente oder API-Parameter parsen.
2. LLM-Konfiguration mit `LLMConfig` validieren.
3. Azure AI Vision validieren, wenn Bildübersetzung ausgewählt ist.
4. Sprachcodes normalisieren.
5. Legacy-Aliase für Sprachordner erkennen.
6. Übersetzungsvolumen schätzen.
7. README-Sprach-/Kursabschnitte bei Bedarf aktualisieren.
8. Projektübersetzung an `ProjectTranslator` delegieren.
9. `ProjectTranslator` delegiert die Dateiverarbeitung an `TranslationManager`.

`TranslationManager` setzt sich aus fokussierten Dateityp-Mixins zusammen:

- `ProjectMarkdownTranslationMixin` kümmert sich um das Lesen von Markdown-Dateien, Inhaltsübersetzung, Pfadumschreibung, Metadaten, Haftungsausschlüsse und Schreibvorgänge.
- `ProjectNotebookTranslationMixin` kümmert sich um das Lesen von Notebook-Dateien, Übersetzung von Markdown-Zellen, Pfadumschreibung, Metadaten, Haftungsausschlüsse und Schreibvorgänge.
- `ProjectImageTranslationMixin` kümmert sich um die Bildentdeckung, Textextraktion/-übersetzung, das Schreiben gerenderter Bilder und Metadaten.

Die tieferliegenden Content-APIs überspringen den Projekt-Workflow:

1. `translate_markdown_content` und `translate_notebook_content` übersetzen nur In-Memory-Inhalte.
2. `translate_image_content` übersetzt Text in einem einzelnen Bild und gibt ein gerendertes Bildobjekt zurück.
3. `rewrite_markdown_paths` und `rewrite_notebook_paths` sind explizite Post-Processing-Helfer. Sie führen keine Übersetzung und keine Projekt-Schreibvorgänge durch.

## Review-Ablauf

Der deterministische Review-Ablauf ist:

1. CLI-Argumente oder API-Parameter parsen.
2. Angeforderte Sprachcodes normalisieren.
3. Einen oder mehrere Review-Ziele aus `root_dir`, `root_dirs` oder `groups` erstellen.
4. Optional Quelldateien mit `--changed-from` begrenzen.
5. Deterministische Prüfungen für Struktur, Übersetzungsaktualität, Markdown-Integrität und lokale Link-/Bildpfade ausführen.
6. Entweder Textausgabe oder GitHub-flavored Markdown ausgeben.
7. Bei gefundenen Review-Fehlern mit einem Fehlerstatus beenden.

Der Review-Ablauf benötigt keine API-Schlüssel und steht für lokale Prüfungen oder optionales Consumer-CI zur Verfügung. Dieses Repository führt `co-op-review` nicht automatisch bei jedem Pull Request aus.

## Dokumentationsseite

Die Dokumentationsseite wird konfiguriert durch:

```text
mkdocs.yml
requirements-docs.txt
docs/
```

Das Verzeichnis `docs/` ist die kanonische Dokumentationsquelle. Füge keine neuen Endanwender-Anleitungen außerhalb dieses Verzeichnisses hinzu, es sei denn, das Projekt führt absichtlich eine weitere veröffentlichte Dokumentationsoberfläche ein.

Build lokal:

```bash
python -m pip install -r requirements-docs.txt
python -m mkdocs build --strict
```

Preview lokal:

```bash
python -m mkdocs serve
```

Die generierte Seite wird nach `site/` geschrieben, das von git ignoriert wird.

## GitHub Pages-Workflow

`.github/workflows/docs.yml` baut die Seite bei Pull Requests und stellt sie bei Pushes auf `main` bereit.

Der Workflow installiert:

```bash
pip install -r requirements-docs.txt
```

Der Docs-Workflow installiert nur die Dokumentations-Toolchain. `mkdocs.yml` zeigt `mkdocstrings` auf `src/`, sodass öffentliche API-Seiten aus dem Quellbaum gerendert werden können, ohne das vollständige Laufzeitabhängigkeiten-Set zu installieren. Falls zukünftige API-Dokus das Importieren optionaler Laufzeitanbieter während des Builds erfordern, aktualisiere sowohl `.github/workflows/docs.yml` als auch diesen Leitfaden zusammen.

## Qualitätsstandard der Dokumentation

Vor dem Zusammenführen von Dokumentationsänderungen ausführen:

```bash
python -m mkdocs build --strict
git diff --check
```

Verwende strikte Builds, damit kaputte Links, ungültige Navigationseinträge und Probleme beim API-Rendering frühzeitig fehlschlagen.