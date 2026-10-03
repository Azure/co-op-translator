# Konfiguration

Co-op Translator erfordert einen Sprachmodell-Anbieter. Bildübersetzung erfordert zusätzlich Azure AI Vision.

Die Konfiguration wird aus Umgebungsvariablen gelesen. Für lokale Projekte legen Sie diese in einer `.env`-Datei im Projektstamm ab.

Zur Einrichtung von Azure-Ressourcen siehe [Azure AI-Einrichtung](azure-ai-setup.md).

## Lokale Laufzeitkonfiguration

Verwenden Sie vor dem lokalen Ausführen der CLI eine virtuelle Umgebung. Co-op Translator unterstützt Python 3.11 bis 3.14.

Für die normale CLI-Nutzung installieren Sie das veröffentlichte Paket innerhalb einer virtuellen Umgebung:

### Windows (PowerShell)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install co-op-translator
translate --help
```

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install co-op-translator
translate --help
```

### Entwicklung im Repository

Für die Entwicklung im Repository installieren Sie stattdessen die Abhängigkeiten aus dem Projektstamm:

```bash
poetry install
poetry run translate --help
```

Nachdem die CLI verfügbar ist, konfigurieren Sie einen Sprachmodell-Anbieter in `.env`.

## Anbieterauswahl

Das Tool erkennt Anbieter automatisch in dieser Reihenfolge:

1. Azure OpenAI
2. OpenAI
3. Anthropic

Für Übersetzungen sind Anbieterdaten erforderlich, ausgenommen Vorschauen wie `translate -l "ko" -md --dry-run`. `migrate-links`, `co-op-review` und `run_review` sind deterministische Wartungsoperationen und benötigen keine Anbieterdaten.

## Modell-Client-Backend

Ab Co-op Translator 0.22.0 verwenden Azure OpenAI, OpenAI und Anthropic standardmäßig das Microsoft Agent Framework. Für die normale Nutzung ist keine Backend-Einstellung erforderlich.

Semantic Kernel bleibt vorübergehend aus Kompatibilitätsgründen verfügbar. Um es explizit auszuwählen, setzen Sie:

```bash
CO_OP_TRANSLATOR_MODEL_CLIENT="semantic-kernel"
```

Die Verwendung von Semantic Kernel erzeugt eine Abkündigungswarnung. Es ist geplant, Semantic Kernel in Version 0.23.0 als optionale Abhängigkeit auszulagern und die Integration in 0.24.0 zu entfernen, vorbehaltlich der Kompatibilitätsergebnisse und des Nutzerfeedbacks. Anthropic benötigt `agent-framework`; die explizite Auswahl von `semantic-kernel` mit Anthropic schlägt mit einem Konfigurationsfehler fehl. Ungültige Werte führen während der Initialisierung des provider-gestützten Translators zu einem Fehler, anstatt stillschweigend auf eine andere Option zurückzufallen. Verfolgen Sie die Einführung und melden Sie Blocker in [GitHub-Issue #543](https://github.com/Azure/co-op-translator/issues/543).

## Azure OpenAI

Verwenden Sie Azure OpenAI, wenn Ihr Modell in Azure AI Foundry oder im Azure OpenAI Service bereitgestellt ist.

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Die Konnektivitätsprüfung verwendet den Endpunkt, den API-Schlüssel, die API-Version und den Deployment-Namen, bevor die Übersetzung beginnt.

## OpenAI

Verwenden Sie OpenAI, wenn Sie die OpenAI-API direkt aufrufen.

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

`OPENAI_CHAT_MODEL_ID` ist erforderlich, da der Translator ein explizites Chatmodell für API-Aufrufe benötigt.

Lassen Sie `OPENAI_ORG_ID` und `OPENAI_BASE_URL` für die Standardkonfiguration ungesetzt. Fügen Sie eine Organisations-ID nur hinzu, wenn Ihr Konto eine benötigt, oder eine Basis-URL nur bei Verwendung eines benutzerdefinierten Endpunkts. Kopieren Sie keine Platzhalterwerte für optionale Einstellungen.

## Anthropic Claude

Verwenden Sie Anthropic, wenn Sie die Claude-API direkt aufrufen. Erstellen Sie einen [Anthropic-API-Schlüssel](https://platform.claude.com/docs/en/get-started) und wählen Sie eine unterstützte [Claude-Modell-ID](https://platform.claude.com/docs/en/about-claude/models/model-ids-and-versions).

```bash
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

`ANTHROPIC_API_KEY` und `ANTHROPIC_MODEL` sind erforderlich. Sie müssen `CO_OP_TRANSLATOR_MODEL_CLIENT` nicht setzen; Agent Framework ist das Standard-Backend.

Lassen Sie `ANTHROPIC_BASE_URL` für die Anthropic-API ungesetzt. Setzen Sie es nur bei Verwendung eines benutzerdefinierten Endpunkts.

`ANTHROPIC_MAX_TOKENS` hat standardmäßig den Wert `8192`, was Platz für tokendichte Schriftsysteme wie Meitei Mayek lässt. Verringern Sie ihn, wenn Ihr Modell oder ein Anthropic-kompatibler Endpunkt die Ausgabe darunter begrenzt.

## Azure AI Vision

Die Bildübersetzung erfordert Azure AI Vision, damit das Tool Text aus Bildern extrahieren kann, bevor das konfigurierte Sprachmodell ihn übersetzt. Anthropic kann den extrahierten Text genauso übersetzen wie Azure OpenAI oder OpenAI.

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

Wenn die Bildübersetzung mit `-img`, `images=True` oder ohne Inhaltstypfilter ausgewählt wird, validiert das Tool die Vision-Konfiguration, bevor die Übersetzung beginnt.

## Mehrere Anmeldedatensätze

Die Konfigurationsschicht unterstützt mehrere Anmeldedatensätze, indem Variablen mit demselben Index versehen werden:

```bash
AZURE_OPENAI_API_KEY_1="..."
AZURE_OPENAI_ENDPOINT_1="https://<resource-1>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME_1="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME_1="<deployment-1>"
AZURE_OPENAI_API_VERSION_1="2024-12-01-preview"

AZURE_OPENAI_API_KEY_2="..."
AZURE_OPENAI_ENDPOINT_2="https://<resource-2>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME_2="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME_2="<deployment-2>"
AZURE_OPENAI_API_VERSION_2="2024-12-01-preview"
```

Jedes Set muss vollständig sein. Die Gesundheitsprüfung wählt ein funktionierendes Set aus, bevor die Übersetzung fortfährt.

OpenAI und Anthropic unterstützen dieselbe Suffix-Konvention. Bewahren Sie jede Variable eines Anmeldedatensatzes mit demselben Suffix auf, einschließlich optionaler Werte wie `OPENAI_BASE_URL_1` oder `ANTHROPIC_BASE_URL_1`.

## Befehlsanforderungen

| Befehl oder API | LLM erforderlich | Vision erforderlich | Hinweise |
| --- | --- | --- | --- |
| `translate -md` | Ja | Nein | Übersetzt nur Markdown. |
| `translate -nb` | Ja | Nein | Übersetzt nur Notebooks. |
| `translate -img` | Ja | Ja | Übersetzt nur Bilder. |
| `translate` ohne Typ-Flags | Ja | Ja | Der Standardmodus umfasst Markdown, Notebooks und Bilder. |
| `evaluate` | Ja | Nein | Verwendet LLM-Auswertung, sofern nicht `--fast` gewählt wurde. |
| `migrate-links` | Nein | Nein | Führt lokale Link-Migration ohne Provider-Aufrufe durch. |
| `co-op-review` | Nein | Nein | Führt deterministische Prüfungen der Übersetzungsstruktur, der Aktualität, von Markdown, Notebooks und lokalen Links durch. |
| `run_translation(markdown=True)` | Ja | Nein | Programmgesteuerte Markdown-Übersetzung. |
| `run_translation(images=True)` | Ja | Ja | Programmgesteuerte Bildübersetzung. |
| `run_review(...)` | Nein | Nein | Programmgesteuerte deterministische Prüfung. |

## Ausgabeverzeichnisse

Standardausgabe für Textübersetzungen:

```text
translations/<language-code>/<source-relative-path>
```

Standardausgabe für übersetzte Bilder:

```text
translated_images/<language-code>/<source-relative-path>
```

Die Python-API kann diese Verzeichnisse mit `translations_dir` und `image_dir` überschreiben。