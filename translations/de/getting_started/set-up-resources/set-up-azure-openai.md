<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "10d8cb07ad0d2ee6705439d4e382ecc9",
  "translation_date": "2025-05-06T18:15:27+00:00",
  "source_file": "getting_started/set-up-resources/set-up-azure-openai.md",
  "language_code": "de"
}
-->
# Azure OpenAI für die Sprachübersetzung einrichten

## Erstellen einer Azure OpenAI-Ressource in Azure AI Foundry

Um Azure OpenAI in Azure AI Foundry einzurichten, befolgen Sie diese Schritte:

### Erstellen eines Hubs

1. Melden Sie sich im [Azure AI Foundry-Portal](https://ai.azure.com) an: Stellen Sie sicher, dass Sie mit Ihrem Azure-Konto angemeldet sind.

2. Navigieren Sie zum Management Center: Wählen Sie auf der Startseite im linken Menü „Management Center“ aus.

3. Erstellen Sie einen neuen Hub: Klicken Sie auf „+ New hub“ und geben Sie die erforderlichen Details wie Subscription, Resource Group und Hub Name ein. Wir empfehlen, den Hub in East US bereitzustellen, da diese Region Cognitive Vision und GPT-Modelle unterstützt.

4. Überprüfen und erstellen: Prüfen Sie die Angaben und klicken Sie auf „Create“, um Ihren Hub einzurichten.

### Erstellen eines Projekts

1. Gehen Sie zur Startseite: Falls Sie nicht bereits dort sind, wählen Sie oben links „Azure AI Foundry“, um zur Startseite zu gelangen.

2. Erstellen Sie ein Projekt: Klicken Sie auf „+ Create project“ und geben Sie einen Namen für Ihr Projekt ein.

3. Wählen Sie einen Hub aus: Wenn Sie mehrere Hubs haben, wählen Sie den gewünschten aus. Wenn Sie einen neuen Hub erstellen möchten, können Sie dies in diesem Schritt tun.

4. Konfigurieren Sie das Projekt: Folgen Sie den Anweisungen, um Ihr Projekt nach Ihren Bedürfnissen einzurichten.

5. Erstellen Sie das Projekt: Klicken Sie auf „Create“, um die Einrichtung abzuschließen.

### Bereitstellen eines Modells und Endpunkts für OpenAI-Modelle

1. Melden Sie sich im [Azure AI Foundry-Portal](https://ai.azure.com) an: Stellen Sie sicher, dass Sie mit dem Azure-Abonnement angemeldet sind, das Ihre Azure OpenAI Service-Ressource enthält.

2. Navigieren Sie zu Models and Endpoint: Finden Sie auf der Startseite von Azure AI Foundry die Kachel mit „“ und wählen Sie „Let's go.“ oder „Model and Endpoints“ im linken Menü aus.

3. Falls Sie noch kein GPT-Modell bereitgestellt haben, wählen Sie „deploy model“: Wählen Sie ein GPT-Modell aus, wir empfehlen GPT-4o, GPT-4o-mini oder o3-mini.

4. Greifen Sie auf Ihre Ressourcen zu: Sie sollten Ihre vorhandenen Azure OpenAI Service-Ressourcen sehen. Wenn Sie mehrere Ressourcen haben, verwenden Sie den Selektor, um die gewünschte auszuwählen.

Für detailliertere Anweisungen können Sie die offizielle Azure AI Foundry-Dokumentation konsultieren.

[How to Create a project](https://learn.microsoft.com/azure/ai-studio/how-to/create-project)

[How to Create resources](https://learn.microsoft.com/azure/ai-studio/how-to/create-azure-ai-resource)

[How to use OpenAI Model in AI Foundry](https://learn.microsoft.com/azure/ai-studio/ai-services/how-to/connect-azure-openai)

[OpenAI Services in Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/azure-openai-in-ai-studio)

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir auf Genauigkeit achten, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Originalsprache ist als maßgebliche Quelle zu betrachten. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die durch die Verwendung dieser Übersetzung entstehen.