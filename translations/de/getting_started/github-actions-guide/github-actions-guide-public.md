<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a52587a512e667f70d92db853d3c61d5",
  "translation_date": "2025-06-12T19:21:28+00:00",
  "source_file": "getting_started/github-actions-guide/github-actions-guide-public.md",
  "language_code": "de"
}
-->
# Verwendung der Co-op Translator GitHub Action (Öffentliche Einrichtung)

**Zielgruppe:** Diese Anleitung richtet sich an Nutzer in den meisten öffentlichen oder privaten Repositories, bei denen die Standard-GitHub Actions-Berechtigungen ausreichen. Sie verwendet das integrierte `GITHUB_TOKEN`.

Automatisieren Sie mühelos die Übersetzung der Dokumentation Ihres Repositories mit der Co-op Translator GitHub Action. Diese Anleitung zeigt Ihnen, wie Sie die Action so einrichten, dass bei Änderungen an Ihren Quell-Markdown-Dateien oder Bildern automatisch Pull Requests mit aktualisierten Übersetzungen erstellt werden.

> [!IMPORTANT]
>
> **Die richtige Anleitung wählen:**
>
> Diese Anleitung beschreibt die **einfachere Einrichtung mit dem Standard-`GITHUB_TOKEN`**. Dies ist die empfohlene Methode für die meisten Nutzer, da keine Verwaltung sensibler GitHub App Private Keys erforderlich ist.
>

## Voraussetzungen

Bevor Sie die GitHub Action konfigurieren, stellen Sie sicher, dass Sie die erforderlichen Zugangsdaten für den KI-Dienst bereit haben.

**1. Erforderlich: Zugangsdaten für KI-Sprachmodelle**  
Sie benötigen Zugangsdaten für mindestens ein unterstütztes Sprachmodell:

- **Azure OpenAI**: Benötigt Endpoint, API-Schlüssel, Modell-/Deployment-Namen, API-Version.  
- **OpenAI**: Benötigt API-Schlüssel, (Optional: Organisations-ID, Basis-URL, Modell-ID).  
- Details finden Sie unter [Supported Models and Services](../../../../README.md).

**2. Optional: Zugangsdaten für KI Vision (für Bildübersetzung)**

- Nur erforderlich, wenn Sie Text in Bildern übersetzen möchten.  
- **Azure AI Vision**: Benötigt Endpoint und Subscription Key.  
- Falls nicht angegeben, läuft die Action im [Markdown-only-Modus](../markdown-only-mode.md).

## Einrichtung und Konfiguration

Folgen Sie diesen Schritten, um die Co-op Translator GitHub Action in Ihrem Repository mit dem Standard-`GITHUB_TOKEN` zu konfigurieren.

### Schritt 1: Authentifizierung verstehen (mit `GITHUB_TOKEN`)

Dieser Workflow verwendet das integrierte `GITHUB_TOKEN`, das von GitHub Actions bereitgestellt wird. Dieses Token gewährt dem Workflow automatisch die Berechtigungen, mit Ihrem Repository zu interagieren, basierend auf den in **Schritt 3** konfigurierten Einstellungen.

### Schritt 2: Repository-Geheimnisse konfigurieren

Sie müssen nur Ihre **Zugangsdaten für KI-Dienste** als verschlüsselte Geheimnisse in den Repository-Einstellungen hinzufügen.

1.  Navigieren Sie zu Ihrem Ziel-GitHub-Repository.  
2.  Gehen Sie zu **Settings** > **Secrets and variables** > **Actions**.  
3.  Klicken Sie unter **Repository secrets** auf **New repository secret** und fügen Sie für jeden benötigten KI-Dienst das entsprechende Geheimnis hinzu.

    ![Select setting action](../../../../translated_images/select-setting-action.32e2394813d09dc148494f34daea40724f24ff406de889f26cbbbf05f98ed621.de.png) *(Bildreferenz: Zeigt, wo Geheimnisse hinzugefügt werden)*

**Erforderliche KI-Dienst-Geheimnisse (Fügen Sie ALLE hinzu, die gemäß Ihren Voraussetzungen zutreffen):**

| Geheimnisname                     | Beschreibung                            | Wertquelle                      |
| :-------------------------------- | :------------------------------------- | :------------------------------ |
| `AZURE_SUBSCRIPTION_KEY`          | Schlüssel für Azure AI Service (Computer Vision) | Ihre Azure AI Foundry            |
| `AZURE_AI_SERVICE_ENDPOINT`         | Endpoint für Azure AI Service (Computer Vision) | Ihre Azure AI Foundry            |
| `AZURE_OPENAI_API_KEY`            | Schlüssel für Azure OpenAI Service            | Ihre Azure AI Foundry            |
| `AZURE_OPENAI_ENDPOINT`           | Endpoint für Azure OpenAI Service             | Ihre Azure AI Foundry            |
| `AZURE_OPENAI_MODEL_NAME`         | Ihr Azure OpenAI Modellname                     | Ihre Azure AI Foundry            |
| `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` | Ihr Azure OpenAI Deployment-Name                 | Ihre Azure AI Foundry            |
| `AZURE_OPENAI_API_VERSION`        | API-Version für Azure OpenAI                    | Ihre Azure AI Foundry            |
| `OPENAI_API_KEY`                  | API-Schlüssel für OpenAI                      | Ihre OpenAI Plattform            |
| `OPENAI_ORG_ID`                   | OpenAI Organisations-ID (Optional)            | Ihre OpenAI Plattform            |
| `OPENAI_CHAT_MODEL_ID`            | Spezifische OpenAI Modell-ID (Optional)         | Ihre OpenAI Plattform            |
| `OPENAI_BASE_URL`                 | Benutzerdefinierte OpenAI API Basis-URL (Optional) | Ihre OpenAI Plattform            |

### Schritt 3: Workflow-Berechtigungen konfigurieren

Die GitHub Action benötigt Berechtigungen, die über das `GITHUB_TOKEN` gewährt werden, um Code auszuchecken und Pull Requests zu erstellen.

1.  Gehen Sie in Ihrem Repository zu **Settings** > **Actions** > **General**.  
2.  Scrollen Sie zum Abschnitt **Workflow permissions**.  
3.  Wählen Sie **Read and write permissions** aus. Damit erhält das `GITHUB_TOKEN` die notwendigen `contents: write` und `pull-requests: write` Berechtigungen für diesen Workflow.  
4.  Stellen Sie sicher, dass das Kontrollkästchen **Allow GitHub Actions to create and approve pull requests** aktiviert ist.  
5.  Klicken Sie auf **Save**.

![Permission setting](../../../../translated_images/permission-setting.cb1f57fdb5194f0743b1f6932f221e404ae2928ee88d77f1de39aba46fbf774a.de.png)

### Schritt 4: Workflow-Datei erstellen

Erstellen Sie abschließend die YAML-Datei, die den automatisierten Workflow mit `GITHUB_TOKEN` definiert.

1.  Erstellen Sie im Stammverzeichnis Ihres Repositories den Ordner `.github/workflows/`, falls dieser noch nicht existiert.  
2.  Erstellen Sie innerhalb von `.github/workflows/` eine Datei mit dem Namen `co-op-translator.yml`.  
3.  Fügen Sie den folgenden Inhalt in `co-op-translator.yml` ein.

```yaml
name: Co-op Translator

on:
  push:
    branches:
      - main

jobs:
  co-op-translator:
    runs-on: ubuntu-latest

    permissions:
      contents: write
      pull-requests: write

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      - name: Install Co-op Translator
        run: |
          python -m pip install --upgrade pip
          pip install co-op-translator

      - name: Run Co-op Translator
        env:
          PYTHONIOENCODING: utf-8
          # === AI Service Credentials ===
          AZURE_SUBSCRIPTION_KEY: ${{ secrets.AZURE_SUBSCRIPTION_KEY }}
          AZURE_AI_SERVICE_ENDPOINT: ${{ secrets.AZURE_AI_SERVICE_ENDPOINT }}
          AZURE_OPENAI_API_KEY: ${{ secrets.AZURE_OPENAI_API_KEY }}
          AZURE_OPENAI_ENDPOINT: ${{ secrets.AZURE_OPENAI_ENDPOINT }}
          AZURE_OPENAI_MODEL_NAME: ${{ secrets.AZURE_OPENAI_MODEL_NAME }}
          AZURE_OPENAI_CHAT_DEPLOYMENT_NAME: ${{ secrets.AZURE_OPENAI_CHAT_DEPLOYMENT_NAME }}
          AZURE_OPENAI_API_VERSION: ${{ secrets.AZURE_OPENAI_API_VERSION }}
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
          OPENAI_ORG_ID: ${{ secrets.OPENAI_ORG_ID }}
          OPENAI_CHAT_MODEL_ID: ${{ secrets.OPENAI_CHAT_MODEL_ID }}
          OPENAI_BASE_URL: ${{ secrets.OPENAI_BASE_URL }}
        run: |
          # =====================================================================
          # IMPORTANT: Set your target languages here (REQUIRED CONFIGURATION)
          # =====================================================================
          # Example: Translate to Spanish, French, German. Add -y to auto-confirm.
          translate -l "es fr de" -y  # <--- MODIFY THIS LINE with your desired languages

      - name: Create Pull Request with translations
        uses: peter-evans/create-pull-request@v5
        with:
          token: ${{ secrets.GITHUB_TOKEN }}
          commit-message: "🌐 Update translations via Co-op Translator"
          title: "🌐 Update translations via Co-op Translator"
          body: |
            This PR updates translations for recent changes to the main branch.

            ### 📋 Changes included
            - Translated contents are available in the `translations/` directory
            - Translated images are available in the `translated_images/` directory

            ---
            🌐 Automatically generated by the [Co-op Translator](https://github.com/Azure/co-op-translator) GitHub Action.
          branch: update-translations
          base: main
          labels: translation, automated-pr
          delete-branch: true
          add-paths: |
            translations/
            translated_images/
```  
4.  **Workflow anpassen:**  
  - **[!IMPORTANT] Zielsprachen:** Passen Sie bei Bedarf im Schritt `Run Co-op Translator` step, you **MUST review and modify the list of language codes** within the `translate -l "..." -y` command to match your project's requirements. The example list (`ar de es...`) needs to be replaced or adjusted.
  - **Trigger (`on:`):** The current trigger runs on every push to `main`. For large repositories, consider adding a `paths:` filter (see commented example in the YAML) to run the workflow only when relevant files (e.g., source documentation) change, saving runner minutes.
  - **PR Details:** Customize the `commit-message`, `title`, `body`, `branch` name, and `labels` in the `Create Pull Request` die Sprachliste an.

**Haftungsausschluss**:  
Dieses Dokument wurde mithilfe des KI-Übersetzungsdienstes [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir auf Genauigkeit achten, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache ist als maßgebliche Quelle zu betrachten. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.