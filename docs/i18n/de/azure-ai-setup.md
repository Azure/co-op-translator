# Azure AI Einrichtung

Verwenden Sie diese Anleitung, wenn Sie Azure OpenAI für Textübersetzungen und Azure AI Vision für die Extraktion von Text aus Bildern konfigurieren möchten.

## Voraussetzungen

- Ein Azure-Abonnement.
- Berechtigung zum Erstellen oder Verwenden von Azure AI-Ressourcen und Modellbereitstellungen.
- Ein Projekt in Azure AI Foundry oder ein gleichwertiger Zugriff auf Azure OpenAI- und Azure AI Vision-Ressourcen.

## Erstellen eines Azure AI-Projekts

1. Öffnen Sie [Azure AI Foundry](https://ai.azure.com).
2. Erstellen Sie ein Projekt oder wählen Sie eines aus.
3. Erstellen oder wählen Sie einen AI-Hub für das Projekt aus.
4. Öffnen Sie nach der Erstellung die Projektübersicht.

## Bereitstellen eines Azure OpenAI-Modells

1. Öffnen Sie im Projekt **Modelle + Endpunkte**.
2. Wählen Sie **Modell bereitstellen**.
3. Wählen Sie ein GPT-Modell wie `gpt-4o`.
4. Stellen Sie das Modell bereit.
5. Notieren Sie den Endpunkt, den Bereitstellungsnamen, den Modellnamen, den API-Schlüssel und die API-Version.

!!! note
    Die Azure OpenAI API-Version ist unabhängig von der Modellversion, die in Azure AI Foundry angezeigt wird. Wählen Sie eine für Ihre Bereitstellung unterstützte API-Version.

## Azure AI Vision konfigurieren

Die Bildübersetzung verwendet Azure AI Vision, um Text aus Quellbildern zu extrahieren, bevor der Text übersetzt wird.

Finden Sie in Ihrem Azure AI-Projekt den Azure AI Services-Schlüssel und den Endpunkt.

![Azure AI-Dienstinformationen finden](../../assets/find-azure-ai-info.png)

Notieren:

- Azure AI Service-Endpunkt
- Azure AI Service API-Schlüssel

## Umgebungsvariablen

Fügen Sie die Anmeldeinformationen Ihrer `.env`-Datei oder den CI-Geheimnissen hinzu.

```bash
# Azure AI Vision, erforderlich für die Bildübersetzung
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"

# Azure OpenAI, erforderlich für die Textübersetzung
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Co-op Translator unterstützt außerdem optionale Fallback-Anmeldeinformationssätze. Duplizieren Sie einen vollständigen Anbieter-Satz mit Suffixen wie `_1` oder `_2`; alle Variablen in einem Fallback-Satz müssen dasselbe Suffix haben.

```bash
AZURE_OPENAI_API_KEY_1="..."
AZURE_OPENAI_ENDPOINT_1="https://<resource-1>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME_1="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME_1="<deployment-1>"
AZURE_OPENAI_API_VERSION_1="2024-12-01-preview"
```

## Nächste Schritte

- Kehren Sie zu [Konfiguration](configuration.md) zurück, um lokale oder CI-Umgebungsvariablen einzurichten.
- Verwenden Sie die [CLI-Referenz](cli.md) für Übersetzungsbefehle.
- Verwenden Sie [GitHub Actions](github-actions.md), um Übersetzungs-Pull Requests zu automatisieren.