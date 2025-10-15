<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3fd2055f97f093b6fe102ea24df4458b",
  "translation_date": "2025-10-15T04:19:37+00:00",
  "source_file": "AGENTS.md",
  "language_code": "de"
}
-->
# AGENTS.md

## Projektübersicht

Co‑op Translator ist ein Python-Kommandozeilentool und ein GitHub Actions Workflow, das Markdown-Dateien, Jupyter-Notebooks und Bildtexte in mehrere Sprachen übersetzt. Die Ausgaben werden in sprachspezifischen Ordnern organisiert und die Übersetzungen bleiben mit dem Quellinhalt synchronisiert. Das Projekt ist als von Poetry verwaltete Bibliothek mit CLI-Einstiegspunkten strukturiert.

### Architekturüberblick

- CLI-Einstiegspunkte (`translate`, `migrate-links`, `evaluate`) rufen eine einheitliche CLI auf, die an Übersetzungs-, Link-Migrations- und Evaluationsprozesse weiterleitet.
- Der Konfigurationslader liest `.env` und erkennt automatisch den LLM-Anbieter (Azure OpenAI oder OpenAI) sowie, falls gewünscht, den Vision-Anbieter (Azure AI Service) für die Texterkennung in Bildern.
- Der Übersetzungskern verarbeitet Markdown und Notebooks; die Vision-Pipeline extrahiert Text aus Bildern, wenn `-img` verwendet wird.
- Ausgaben werden unter `translations/<lang>/` für Text und `translated_images/` für Bilder organisiert, wobei die Originalstruktur erhalten bleibt.

### Wichtige Technologien und Frameworks

- Python 3.10–3.12, Poetry für das Packaging
- CLI: `click`
- LLM/AI SDKs: Azure OpenAI, OpenAI
- Vision: Azure AI Service (Computer Vision)
- HTTP und Daten: `httpx`, `pydantic`
- Bildverarbeitung: `pillow`, `opencv-python`, `matplotlib`
- Tooling: `pytest`, `black`, `ruff`

## Setup-Befehle

### Voraussetzungen

- Python 3.10–3.12
- Azure-Abonnement (optional, für Azure AI Services)
- Internetzugang für LLM/Vision-APIs (z. B. Azure OpenAI/OpenAI, Azure AI Vision)

### Option A: Poetry (empfohlen)

```bash
# From repository root
pip install poetry
poetry install

# Run any command via Poetry
poetry run translate --help
```

### Option B: pip/venv

```bash
# Create & activate virtual environment
python -m venv .venv
# Windows
.venv\\Scripts\\activate
# Linux/macOS
# source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# (Optional) Editable install for local development
pip install -e .
```

## Nutzung für Endanwender

### Docker (veröffentlichtes Image)

```bash
# Pull public image from GHCR
docker pull ghcr.io/azure/co-op-translator:latest

# Run with current folder mounted and .env provided (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "fr es" -md

# PowerShell
docker run --rm -it --env-file .env -v ${PWD}:/work ghcr.io/azure/co-op-translator:latest -l "fr es" -md
```

Hinweise:
- Der Standard-Entrypoint ist `translate`. Für die Link-Migration mit `--entrypoint migrate-links` überschreiben.
- Stelle sicher, dass die Sichtbarkeit des GHCR-Pakets auf Öffentlich steht, damit anonyme Pulls möglich sind.

### CLI (pip)

```bash
pip install co-op-translator
translate -l "fr es" -md
```

### Umgebungs-Konfiguration

Lege eine `.env`-Datei im Wurzelverzeichnis des Repositories an und trage die Zugangsdaten/Endpoints für dein gewähltes Sprachmodell und (optional) den Vision-Service ein. Für anbieter-spezifische Einrichtung siehe `getting_started/set-up-azure-ai.md`.

### Erforderliche Umgebungsvariablen

Mindestens ein LLM-Anbieter muss konfiguriert sein. Für die Bildübersetzung muss zusätzlich Azure AI Service eingerichtet werden.

- Azure OpenAI (Textübersetzung):
  - `AZURE_OPENAI_API_KEY`
  - `AZURE_OPENAI_ENDPOINT`
  - `AZURE_OPENAI_MODEL_NAME`
  - `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME`
  - `AZURE_OPENAI_API_VERSION`

- OpenAI (Alternative für Textübersetzung):
  - `OPENAI_API_KEY`
  - `OPENAI_ORG_ID` (optional)
  - `OPENAI_CHAT_MODEL_ID` (erforderlich bei Nutzung des OpenAI-Anbieters)
  - `OPENAI_BASE_URL` (optional; Standard: `https://api.openai.com/v1`)

- Azure AI Service für Texterkennung in Bildern (erforderlich bei Nutzung von `-img`):
  - `AZURE_AI_SERVICE_API_KEY` (bevorzugt) oder veraltet `AZURE_SUBSCRIPTION_KEY`
  - `AZURE_AI_SERVICE_ENDPOINT`

Beispiel für einen `.env`-Ausschnitt:

```bash
# Azure AI Service (for image translation)
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<your-ai-service>.cognitiveservices.azure.com/"

# Azure OpenAI (primary option)
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<your-azure-openai>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<your-deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"

# OpenAI (alternative option)
OPENAI_API_KEY="..."
OPENAI_ORG_ID="..."            # optional
OPENAI_CHAT_MODEL_ID="gpt-4o"   # required when using OpenAI
OPENAI_BASE_URL="https://api.openai.com/v1" # optional
```

Hinweise:

- Das Tool erkennt den verfügbaren LLM-Anbieter automatisch; konfiguriere entweder Azure OpenAI oder OpenAI.
- Für die Bildübersetzung werden sowohl `AZURE_AI_SERVICE_API_KEY` als auch `AZURE_AI_SERVICE_ENDPOINT` benötigt.
- Die CLI gibt eine klare Fehlermeldung aus, wenn erforderliche Variablen fehlen.

## Entwicklungs-Workflow

- Der Quellcode befindet sich unter `src/co_op_translator`, Tests unter `tests/`.
- Primäre CLIs (über Entry Points installiert):

```bash
# Translate content to one or more languages (space‑separated codes)
translate -l "fr es de"

# Restrict by content type
translate -l "ja" -md            # only Markdown
translate -l "ko" -nb            # only notebooks
translate -l "zh" -md -img       # Markdown + images

# Update links in previously translated notebooks/Markdown
migrate-links -l "all" -y
```

Weitere Nutzungsdokumentation findest du unter `getting_started/`.

## Testanleitung

Führe Tests aus dem Wurzelverzeichnis des Repositories aus. Einige Tests benötigen API-Zugangsdaten; überspringe diese bei Bedarf.

```bash
# Run full test suite
pytest

# Skip tests that require live API keys
pytest -m "not api_key_required"

# Run a subset
pytest tests/co_op_translator -k "name_substring"
```

Optionale Coverage (benötigt `coverage`):

```bash
coverage run -m pytest -m "not api_key_required"
coverage html  # outputs to ./htmlcov
```

## Richtlinien für den Code-Stil

- Formatter: Black (konfiguriert in `pyproject.toml`, Zeilenlänge 88)
- Linter: Ruff (konfiguriert in `pyproject.toml`, Zeilenlänge 120)
- Typüberprüfung: mypy (Konfiguration vorhanden; bei Installation aktivieren)

Befehle:

```bash
# Via Poetry
poetry run black .
poetry run ruff check .
poetry run ruff check . --fix   # safe auto‑fixes

# Or with global tools
black .
ruff check .
```

Organisiere Python-Quellen unter `src/`, Tests unter `tests/`, und bevorzuge explizite Importe innerhalb des Paket-Namespace (`co_op_translator.*`).

## Build und Deployment

Build-Artefakte werden unter `dist/` veröffentlicht.

```bash
# Build (Poetry)
poetry build

# Local install of the built wheel
pip install dist/*.whl
```

Automatisierung über GitHub Actions wird unterstützt; siehe:

- `getting_started/github-actions-guide/github-actions-guide-public.md`
- `getting_started/github-actions-guide/github-actions-guide-org.md`

### Container-Image (GHCR)

- Offizielles Image: `ghcr.io/azure/co-op-translator:<tag>`
- Tags: `latest` (auf main), semantische Tags wie `vX.Y.Z` und ein `sha`-Tag
- Multi-Arch: `linux/amd64, linux/arm64` werden via Buildx unterstützt
- Dockerfile-Muster: Baue Abhängigkeits-Wheels im Builder (mit `build-essential` und `python3-dev`) und installiere sie im Runtime-Container aus dem lokalen Wheelhouse (`pip install --no-index --find-links=/wheels`)
- Workflow: `.github/workflows/docker-publish.yml` baut und pusht zu GHCR

## Sicherheitshinweise

- Bewahre API-Keys und Endpoints in `.env` oder im Secrets-Store deiner CI auf; niemals Secrets committen.
- Für die Bildübersetzung werden Azure AI Vision Keys/Endpoints benötigt; andernfalls `-img` weglassen.
- Prüfe Anbieter-Kontingente/Ratenlimits bei großen Übersetzungsaufträgen.

## Richtlinien für Pull Requests

### Vor dem Einreichen

1. **Teste deine Änderungen:**
   - Führe betroffene Notebooks vollständig aus
   - Überprüfe, dass alle Zellen fehlerfrei laufen
   - Prüfe, ob die Ausgaben sinnvoll sind

2. **Dokumentations-Updates:**
   - Aktualisiere `README.md` bei neuen Konzepten
   - Füge Kommentare in Notebooks für komplexen Code hinzu
   - Stelle sicher, dass Markdown-Zellen den Zweck erklären

3. **Dateiänderungen:**
   - Keine `.env`-Dateien committen (verwende `.env.example`)
   - Committe nicht `venv/` oder `__pycache__/`-Verzeichnisse
   - Notebook-Ausgaben beibehalten, wenn sie Konzepte demonstrieren
   - Temporäre Dateien und Backup-Notebooks (`*-backup.ipynb`) entfernen

4. **Stil und Formatierung:**
   - Halte dich an die Stil- und Formatierungsrichtlinien
   - Führe `poetry run black .` und `poetry run ruff check .` aus, um Stil- und Formatierungsfehler zu prüfen

5. **Tests und CLI-Hilfe ergänzen/aktualisieren:**
   - Füge Tests hinzu oder aktualisiere sie bei Verhaltensänderungen
   - Halte die CLI-Hilfe konsistent zu den Änderungen


### Commit-Nachricht und Merge-Strategie

Wir verwenden standardmäßig Squash and Merge. Die finale Squash-Commit-Nachricht sollte folgendem Muster entsprechen:

```bash
<type>: <description> (#<PR number>)
```

Erlaubte Typen:
- `Docs` — Dokumentations-Updates
- `Build` — Build-System, Abhängigkeiten, Konfiguration/CI
- `Core` — Kernfunktionalität und Features (z. B. `src/co_op_translator/core`)

Beispiele:
- `Docs: Update installation instructions for clarity (#50)`
- `Core: Improve handling of image translation (#60)`

Hinweise:
- PR-Titel werden oft automatisch anhand von Labels vorangestellt; prüfe, ob das generierte Präfix korrekt ist.

### PR-Titelformat

Verwende klare, prägnante Titel. Bevorzuge die gleiche Struktur wie für den finalen Squash-Commit:
- `Docs: Update installation instructions for clarity`
- `Core: Improve handling of image translation`

## Debugging und Fehlerbehebung

- Häufige Probleme und Lösungen: `getting_started/troubleshooting.md`
- Unterstützte Sprachen und Hinweise (inklusive Schriftarten/bekannte Probleme): `getting_started/supported-languages.md`
- Bei Link-Problemen in Notebooks erneut ausführen: `migrate-links -l "all" -y`

## Hinweise für Agents

- Bevorzuge Poetry für reproduzierbare Umgebungen; andernfalls `requirements.txt` verwenden.
- Beim Aufruf von CLIs in CI die benötigten Secrets über Umgebungsvariablen oder `.env`-Injection bereitstellen.
- Für Monorepo-Nutzer: Dieses Repository fungiert als eigenständiges Paket; keine Koordination mit Sub-Packages erforderlich.

- Multi-Arch-Hinweis: Behalte `linux/arm64` bei, wenn ARM-Nutzer (Apple Silicon/ARM-Server) Zielgruppe sind; andernfalls reicht `linux/amd64` für Einfachheit.
- Verweise Nutzer auf den Docker Quick Start in `README.md`, wenn Container bevorzugt werden; sowohl Bash- als auch PowerShell-Varianten angeben, da sich die Anführungszeichen unterscheiden.

---

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ausgangssprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die durch die Nutzung dieser Übersetzung entstehen.