<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "53c99ea0ead7a3500149d4bb96be5811",
  "translation_date": "2025-05-06T17:54:31+00:00",
  "source_file": "getting_started/command-line-guide/create-env-file.md",
  "language_code": "de"
}
-->
# Erstellen Sie die Datei *.env* im Stammverzeichnis

In diesem Tutorial zeigen wir Ihnen, wie Sie Ihre Umgebungsvariablen für Azure-Dienste mithilfe einer *.env*-Datei einrichten. Umgebungsvariablen ermöglichen es Ihnen, sensible Zugangsdaten wie API-Schlüssel sicher zu verwalten, ohne sie direkt im Code zu hinterlegen.

> [!IMPORTANT]
> - Es muss nur ein Sprachmodell-Dienst (Azure OpenAI oder OpenAI) konfiguriert werden. Füllen Sie die Umgebungsvariablen für den bevorzugten Dienst aus. Wenn Umgebungsvariablen für mehrere Sprachmodelle gesetzt sind, wählt der Co-op Translator eines basierend auf der Priorität aus.
> - Wenn keine Umgebungsvariablen für Computer Vision gesetzt sind, wechselt der Translator automatisch in den [Markdown-only-Modus](./markdown-only-mode.md).

> [!NOTE]
> Diese Anleitung konzentriert sich hauptsächlich auf Azure-Dienste, aber Sie können auch jedes unterstützte Sprachmodell aus der [Liste der unterstützten Modelle und Dienste](../README.md#-supported-models-and-services) auswählen.

## Erstellen der Datei *.env*

Erstellen Sie im Stammverzeichnis Ihres Projekts eine Datei namens *.env*. In dieser Datei werden alle Ihre Umgebungsvariablen in einem einfachen Format gespeichert.

> [!WARNING]
> Die Datei *.env* darf nicht in Versionskontrollsysteme wie Git eingecheckt werden. Fügen Sie *.env* Ihrer .gitignore-Datei hinzu, um versehentliche Commits zu vermeiden.

1. Navigieren Sie zum Stammverzeichnis Ihres Projekts.

1. Erstellen Sie im Stammverzeichnis Ihres Projekts eine Datei namens *.env*.

    ![Erstellen der Datei *.env*.](../../../../imgs/create-env.png)

1. Öffnen Sie die Datei *.env* und fügen Sie die folgende Vorlage ein:

    ```plaintext
    # Azure Credentials
    AZURE_SUBSCRIPTION_KEY="your_azure_AIServices_api_key"
    AZURE_AI_SERVICE_ENDPOINT="https://your_azure_ai_service_endpoint"

    # Azure OpenAI Credentials
    AZURE_OPENAI_API_KEY="your_azure_openai_api_key"
    AZURE_OPENAI_ENDPOINT="https://your_azure_openai_endpoint"
    AZURE_OPENAI_MODEL_NAME="your_model_name"
    AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="your_deployment_name"
    AZURE_OPENAI_API_VERSION="your_api_version"

    # OpenAI Credentials
    OPENAI_API_KEY="your_openai_api_key"
    OPENAI_ORG_ID="your_openai_org_id"
    OPENAI_CHAT_MODEL_ID="your_chat_model_id(ex. gpt-4o)"
    OPENAI_BASE_URL="https://api.openai.com/v1 (If you don't have a custom base URL, you can delete this lin, then it will use the default base URL)"
    ```

## Sammeln Sie Ihre Azure-Zugangsdaten

Sie benötigen folgende Azure-Zugangsdaten, um die Umgebung zu konfigurieren:

Alle Details finden Sie auf der Projektübersichtsseite in [AI Foundry](https://ai.azure.com/build/overview)

![Foundry-Übersicht](../../../../imgs/foundry-overview.png)


### Für Azure AI Service:

    - Azure Subscription Key: Ihr API-Schlüssel für Azure AI Services, mit dem Sie auf die Azure AI-Dienste zugreifen können.
    - Azure AI Service Endpoint: Die Endpunkt-URL für Ihren spezifischen Azure AI-Dienst.

### Für Azure OpenAI Service:

    - Azure OpenAI API Key: Der API-Schlüssel zum Zugriff auf Azure OpenAI-Dienste.
    - Azure OpenAI Endpoint: Die Endpunkt-URL für Ihren Azure OpenAI-Dienst.


1. Kopieren Sie Ihren AI Services-Schlüssel und Endpoint und fügen Sie diese in die *.env*-Datei ein.
2. Kopieren Sie Ihren Azure OpenAI API-Schlüssel und Endpoint und fügen Sie diese in die *.env*-Datei ein.

### Modelldetails

Wählen Sie Modell und Endpunkte im linken Menü aus

![FoundryModels](../../../../imgs/gpt-models.png)

Wählen Sie nun das Modell aus, das Sie verwenden möchten, um die Modelldetails zu erhalten

![Modelldetails](../../../../imgs/model-deployment-name.png)

Für die *.env*-Datei benötigen wir folgende Angaben

    - Azure OpenAI Model Name: Der Name des Modells, mit dem Sie interagieren werden.
    - Azure OpenAI Name: Der Name Ihrer Bereitstellung für Azure OpenAI-Modelle.
    - Azure OpenAI API Version: Die Version der Azure OpenAI API, die Sie verwenden (zu finden am Ende der URL).

Um diese Details zu erhalten, wählen Sie die Modellbereitstellung aus

![FoundryModelinfo](../../../../imgs/foundry-model-info.png)

### Azure-Umgebungsvariablen hinzufügen

3. Kopieren Sie Ihren Azure OpenAI **Name** und die Modell-**Version** und fügen Sie diese in die *.env*-Datei ein.
4. Speichern Sie die *.env*-Datei.
5. Nun können Sie auf diese Umgebungsvariablen zugreifen, um **Co-op Translator** mit Ihren Azure-Diensten zu verwenden.

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache ist als maßgebliche Quelle zu betrachten. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.