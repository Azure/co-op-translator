# Maintainer-Leitfaden

This page summarizes how the API, CLI, and documentation site are wired together.

## Öffentliche API-Grenze

The stable Python API is exported from:

```python
co_op_translator.api
```

Die öffentliche API ist in Hilfsfunktionen zur Inhaltsübersetzung, Pfadumschreibung, Projektorchestrierung und Überprüfung gegliedert:

```python
from co_op_translator.api import (
    ImageTranslationOptions,
    MarkdownTranslationOptions,
    NotebookTranslationOptions,
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

Beim Hinzufügen neuer öffentlicher APIs aktualisieren Sie:

- `src/co_op_translator/api/__init__.py`
- `docs/api.md`
- relevante API-Tests unter `tests/co_op_translator/`, wie `test_api.py` oder `test_review_api.py`

Vermeiden Sie es, niedrigere `core`-Module als stabile API zu dokumentieren, es sei denn, das Projekt beabsichtigt, sie direkt zu unterstützen.

## CLI entry points

Das Paket definiert diese Poetry-Skripte:

```toml
[tool.poetry.scripts]
translate = "co_op_translator.__main__:main"
evaluate = "co_op_translator.__main__:main"
migrate-links = "co_op_translator.__main__:main"
co-op-review = "co_op_translator.__main__:main"
co-op-translator-mcp = "co_op_translator.mcp.server:main"
```

`src/co_op_translator/__main__.py` leitet anhand des Skriptnamens weiter:

- `translate` ruft `co_op_translator.cli.translate.translate_command` auf
- `evaluate` ruft `co_op_translator.cli.evaluate.evaluate_command` auf
- `migrate-links` ruft `co_op_translator.cli.migrate_links.migrate_links_command` auf
- `co-op-review` ruft `co_op_translator.cli.review.review_command` auf

`co-op-translator-mcp` umgeht `__main__.py` und ruft `co_op_translator.mcp.server:main` direkt auf.

Beim Hinzufügen oder Ändern von CLI-Optionen aktualisieren Sie:

- den relevanten `src/co_op_translator/cli/*.py`-Befehl
- `docs/cli.md`
- CLI-bezogene Tests, falls sich das Verhalten ändert

## MCP server

Der MCP-Server ist implementiert in:

```python
co_op_translator.mcp.server
```

Der Server verwendet bewusst die öffentliche Python-API, statt niedrigere `core`-Module direkt aufzurufen. Bewahren Sie diese Grenze, damit MCP-Clients, Python-Aufrufer und die CLI dasselbe Verhalten haben.

Beim Hinzufügen oder Ändern von MCP-Tools aktualisieren Sie:

- `src/co_op_translator/mcp/server.py`
- `tests/co_op_translator/test_mcp_server.py`
- `docs/mcp.md`
- `docs/api.md`, falls sich die öffentliche API-Oberfläche ändert

Repository-Übersetzungswerkzeuge sind über MCP modellaufrufbar und können viele Dateien schreiben. Behalten Sie `dry_run=True` als Standard bei und verlangen Sie `confirm_write=True`, bevor Projektübersetzungen ohne Dry-Run geschrieben werden.

## Translation flow

Der übergeordnete Projektübersetzungsablauf ist:

1. CLI-Argumente oder API-Parameter parsen.
2. LLM-Konfiguration mit `LLMConfig` validieren.
3. Azure AI Vision validieren, wenn Bildübersetzung ausgewählt ist.
4. Sprachcodes normalisieren.
5. Veraltete Sprachordner-Aliase erkennen.
6. Übersetzungsvolumen schätzen.
7. README-Sprach-/Kursabschnitte bei Bedarf aktualisieren.
8. Projektübersetzung an `ProjectTranslator` delegieren.
9. `ProjectTranslator` delegiert die Datei-Verarbeitung an `TranslationManager`.

Der `TranslationManager` setzt sich aus fokussierten Dateityp-Mixins zusammen:

- `ProjectMarkdownTranslationMixin` verarbeitet das Lesen von Markdown-Dateien, Inhaltsübersetzung, Pfadumschreibung, Metadaten, Haftungsausschlüsse und Schreibvorgänge.
- `ProjectNotebookTranslationMixin` verarbeitet das Lesen von Notebook-Dateien, Übersetzung von Markdown-Zellen, Pfadumschreibung, Metadaten, Haftungsausschlüsse und Schreibvorgänge.
- `ProjectImageTranslationMixin` verarbeitet die Bildfindung, Textextraktion/-übersetzung, das Schreiben gerenderter Bilder und Metadaten.

Die niedrigeren Inhalts-APIs überspringen den Projekt-Workflow:

1. `translate_markdown_content` und `translate_notebook_content` übersetzen nur Inhalte im Speicher.
2. `translate_image_content` übersetzt Text in einem einzelnen Bild und gibt ein gerendetes Bildobjekt zurück.
3. `rewrite_markdown_paths` und `rewrite_notebook_paths` sind explizite Post-Processing-Helfer. Sie führen keine Übersetzung und keine Projekt-Schreibvorgänge durch.

## Review flow

Der deterministische Review-Ablauf ist:

1. CLI-Argumente oder API-Parameter parsen.
2. Angeforderte Sprachcodes normalisieren.
3. Ein oder mehrere Review-Ziele aus `root_dir`, `root_dirs` oder `groups` erstellen.
4. Optional Quelldateien mit `--changed-from` begrenzen.
5. Deterministische Prüfungen für Struktur, Übersetzungsaktualität, Markdown-Integrität und lokale Link-/Bildpfade durchführen.
6. Entweder Textausgabe oder GitHub-flavored Markdown ausgeben.
7. Mit einem Fehler beenden, wenn Review-Fehler gefunden werden.

Der Review-Ablauf benötigt keine API-Schlüssel und sollte weiterhin für Pull-Request-CI geeignet sein. Der Pull-Request-Workflow schreibt bei jedem Lauf eine Prüfungszusammenfassung und postet nur dann einen PR-Kommentar, wenn `co-op-review` fehlschlägt.

## Documentation site

Die Dokumentationsseite wird konfiguriert durch:

```text
mkdocs.yml
requirements-docs.txt
docs/
```

Das `docs/`-Verzeichnis ist die kanonische Dokumentationsquelle. Fügen Sie keine neuen Endbenutzeranleitungen außerhalb dieses Verzeichnisses hinzu, es sei denn, das Projekt führt absichtlich eine weitere veröffentlichte Dokumentationsoberfläche ein.

Lokal bauen:

```bash
python -m pip install -r requirements-docs.txt
python -m mkdocs build --strict
```

Lokal vorschauen:

```bash
python -m mkdocs serve
```

Die generierte Seite wird nach `site/` geschrieben, welches von git ignoriert wird.

## GitHub Pages workflow

`.github/workflows/docs.yml` baut die Seite bei Pull Requests und stellt sie bei Pushes auf `main` bereit.

Der Workflow installiert:

```bash
pip install -r requirements-docs.txt
```

Der Docs-Workflow installiert nur die Dokumentations-Toolchain. `mkdocs.yml` verweist `mkdocstrings` auf `src/`, sodass öffentliche API-Seiten aus dem Quellbaum gerendert werden können, ohne das vollständige Runtime-Abhängigkeits-Set zu installieren. Wenn zukünftige API-Dokumentationen das Importieren optionaler Runtime-Provider während des Builds erfordern, aktualisieren Sie sowohl `.github/workflows/docs.yml` als auch diesen Leitfaden zusammen.

## Docs quality bar

Bevor Sie Änderungen an der Dokumentation zusammenführen, führen Sie aus:

```bash
python -m mkdocs build --strict
git diff --check
```

Verwenden Sie strikte Builds, damit defekte Links, ungültige Navigationseinträge und API-Rendering-Probleme frühzeitig fehlschlagen.