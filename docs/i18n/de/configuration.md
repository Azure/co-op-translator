# Konfiguration

Co-op Translator benötigt einen Anbieter für Sprachmodelle. Die Bildübersetzung erfordert zudem Azure AI Vision.

Die Konfiguration wird aus Umgebungsvariablen gelesen. Für lokale Projekte legen Sie diese in einer `.env`-Datei im Projektstamm ab.

Für die Einrichtung von Azure-Ressourcen siehe [Azure AI Einrichtung](azure-ai-setup.md).

## Lokale Laufzeitkonfiguration

Verwenden Sie vor dem lokalen Ausführen der CLI eine virtuelle Umgebung. Co-op Translator unterstützt Python 3.10 bis 3.12.

Für die normale CLI-Nutzung installieren Sie das veröffentlichte Paket in einer virtuellen Umgebung:

=== "Windows"

    ```powershell
    python -m venv .venv
    .venv\Scripts\activate
    pip install co-op-translator
    translate --help
    ```

=== "macOS / Linux"

    ```bash
    python -m venv .venv
    source .venv/bin/activate
    pip install co-op-translator
    translate --help
    ```

Für die Entwicklung am Repository installieren Sie stattdessen die Abhängigkeiten vom Projektstamm aus:

```bash
poetry install
poetry run translate --help
```

Nachdem die CLI verfügbar ist, konfigurieren Sie einen Anbieter für Sprachmodelle in der `.env`.

## Auswahl des Anbieters

Das Tool erkennt Anbieter automatisch in folgender Reihenfolge:

1. Azure OpenAI
2. OpenAI

Wenn keiner der Anbieter konfiguriert ist, schlagen `translate`, `evaluate`, `migrate-links` und `run_translation` bei den Konfigurationsprüfungen fehl. `co-op-review` und `run_review` sind deterministische Wartungsprüfungen und benötigen keine Anbieterdaten.

## Azure OpenAI

Verwenden Sie Azure OpenAI, wenn Ihr Modell in Azure AI Foundry oder dem Azure OpenAI Service bereitgestellt ist.

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Die Konnektivitätsprüfung verwendet den Endpunkt, den API-Schlüssel, die API-Version und den Bereitstellungsnamen, bevor die Übersetzung beginnt.

## OpenAI

Verwenden Sie OpenAI, wenn Sie die OpenAI-API direkt aufrufen.

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
OPENAI_ORG_ID="..."          # optional
OPENAI_BASE_URL="..."        # optional
```

`OPENAI_CHAT_MODEL_ID` ist erforderlich, da der Translator ein explizites Chatmodell für API-Aufrufe benötigt.

## Azure AI Vision

Die Bildübersetzung erfordert Azure AI Vision, damit das Tool Text aus Bildern extrahieren kann, bevor er übersetzt wird.

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

Wenn die Bildübersetzung mit `-img`, `images=True` oder ohne Content-Type-Filter ausgewählt ist, validiert das Tool die Vision-Konfiguration, bevor die Übersetzung beginnt.

## Mehrere Anmeldeinformationssätze

Die Konfigurationsschicht unterstützt mehrere Anmeldeinformationssätze, indem Variablen mit demselben Index suffixiert werden:

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

Jeder Satz muss vollständig sein. Die Gesundheitsprüfung wählt vor dem Fortfahren der Übersetzung einen funktionierenden Satz aus.

## Befehlsanforderungen

| Befehl oder API | LLM erforderlich | Vision erforderlich | Hinweise |
| --- | --- | --- | --- |
| `translate -md` | Ja | Nein | Übersetzt nur Markdown. |
| `translate -nb` | Ja | Nein | Übersetzt nur Notebooks. |
| `translate -img` | Ja | Ja | Übersetzt nur Bilder. |
| `translate` with no type flags | Ja | Ja | Im Standardmodus sind Markdown, Notebooks und Bilder enthalten. |
| `evaluate` | Ja | Nein | Verwendet LLM-Evaluierung, sofern nicht `--fast` ausgewählt ist. |
| `migrate-links` | Ja | Nein | Führt Link-Migration durch, führt aber weiterhin gemeinsame Konfigurationsprüfungen aus. |
| `co-op-review` | Nein | Nein | Führt deterministische Prüfungen zu Übersetzungsstruktur, Aktualität, Markdown, Notebook und lokalen Links aus. |
| `run_translation(markdown=True)` | Ja | Nein | Programmgesteuerte Markdown-Übersetzung. |
| `run_translation(images=True)` | Ja | Ja | Programmgesteuerte Bildübersetzung. |
| `run_review(...)` | Nein | Nein | Programmgesteuerte deterministische Überprüfung. |

## Ausgabeverzeichnisse

Standardausgabe für Textübersetzungen:

```text
translations/<language-code>/<source-relative-path>
```

Standardausgabe für übersetzte Bilder:

```text
translated_images/<language-code>/<source-relative-path>
```

Die Python-API kann diese Verzeichnisse mit `translations_dir` und `image_dir` überschreiben.