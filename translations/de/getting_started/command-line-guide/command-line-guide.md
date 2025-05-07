<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d8eec418d6325416b9fab19a2dfcbf41",
  "translation_date": "2025-05-06T17:52:26+00:00",
  "source_file": "getting_started/command-line-guide/command-line-guide.md",
  "language_code": "de"
}
-->
# Verwendung der Co-op Translator Befehlszeilenschnittstelle (CLI)

## Voraussetzungen

- **Python 3.10 oder höher**: Erforderlich zum Ausführen des Co-op Translators.
- **Ressource für Sprachmodelle**:  
  - **Azure OpenAI** oder andere LLMs. Details finden Sie in den [supported models and services](../../../../README.md).
- **Ressource für Computer Vision** (optional):  
  - Für die Bildübersetzung. Ist diese nicht verfügbar, arbeitet der Translator im [Markdown-only mode](../markdown-only-mode.md).  
  - **Azure Computer Vision**

### Erste Einrichtung

Bevor Sie beginnen, stellen Sie sicher, dass Sie die folgenden Ressourcen eingerichtet haben:

- [Set up Azure OpenAI](../set-up-resources/set-up-azure-openai.md)  
- [Set up Azure Computer Vision](../set-up-resources/set-up-azure-computer-vision.md) (optional)

## Inhaltsverzeichnis

1. [Erstellen einer '.env'-Datei im Stammverzeichnis](./create-env-file.md)  
   - Fügen Sie die erforderlichen Schlüssel für den gewählten Sprachmodell-Dienst hinzu.  
   - Wenn Azure Computer Vision-Schlüssel ausgelassen oder `-md` angegeben sind, arbeitet der Translator im Markdown-only mode.  
3. [Installation des Co-op Translator Pakets](./install-package.md)  
4. [Übersetzen Ihres Projekts mit Co-op Translator](./translator-your-project.md)

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir auf Genauigkeit achten, bitten wir zu beachten, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache ist als maßgebliche Quelle zu betrachten. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die durch die Nutzung dieser Übersetzung entstehen.