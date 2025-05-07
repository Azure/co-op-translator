<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "66029e3b67a3eb980ab8740367e91283",
  "translation_date": "2025-05-07T14:07:01+00:00",
  "source_file": "getting_started/command-line-guide/create-env-file.md",
  "language_code": "de"
}
-->
# Erstellen Sie die Datei *.env* im Stammverzeichnis

In diesem Tutorial zeigen wir Ihnen, wie Sie Ihre Umgebungsvariablen für Azure-Dienste mit einer *.env*-Datei einrichten. Umgebungsvariablen ermöglichen es Ihnen, sensible Zugangsdaten wie API-Schlüssel sicher zu verwalten, ohne sie fest im Code zu verankern.

> [!IMPORTANT]
> - Es muss nur ein Sprachmodell-Dienst (Azure OpenAI oder OpenAI) konfiguriert werden. Füllen Sie die Umgebungsvariablen für den von Ihnen bevorzugten Dienst aus. Wenn Umgebungsvariablen für mehrere Sprachmodelle gesetzt sind, wählt der Co-op Translator eines nach Priorität aus.
> - Wenn die Umgebungsvariablen für Computer Vision nicht gesetzt sind, wechselt der Translator automatisch in den [Markdown-only-Modus](./markdown-only-mode.md).

> [!NOTE]
> Diese Anleitung konzentriert sich hauptsächlich auf Azure-Dienste, aber Sie können jedes unterstützte Sprachmodell aus der [Liste der unterstützten Modelle und Dienste](../README.md#-supported-models-and-services) wählen.

## Erstellen der *.env*-Datei

Erstellen Sie im Stammverzeichnis Ihres Projekts eine Datei mit dem Namen *.env*. In dieser Datei werden alle Ihre Umgebungsvariablen in einem einfachen Format gespeichert.

> [!WARNING]
> Vermeiden Sie es, Ihre *.env*-Datei in Versionsverwaltungssysteme wie Git einzuchecken. Fügen Sie *.env* zu Ihrer .gitignore-Datei hinzu, um versehentliche Commits zu verhindern.

1. Navigieren Sie zum Stammverzeichnis Ihres Projekts.

1. Erstellen Sie eine *.env*-Datei im Stammverzeichnis Ihres Projekts.

1. Öffnen Sie die *.env*-Datei und fügen Sie die folgende Vorlage ein:

    ```plaintext
    # Azure Credentials
    AZURE_AI_SERVICE_API_KEY="your_azure_ai_service_api_key"
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

> [!NOTE]
> Wenn Sie Ihre API-Schlüssel und Endpunkte suchen, können Sie die Anleitung in [set-up-azure-ai.md](../set-up-azure-ai.md) nutzen.

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.