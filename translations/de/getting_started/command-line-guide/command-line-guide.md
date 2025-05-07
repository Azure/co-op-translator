<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a5eb9b53c81804f04bc9456160e79940",
  "translation_date": "2025-05-07T14:06:55+00:00",
  "source_file": "getting_started/command-line-guide/command-line-guide.md",
  "language_code": "de"
}
-->
# Verwendung der Co-op Translator Befehlszeilenschnittstelle (CLI)

## Voraussetzungen

- **Python 3.10 oder höher**: Erforderlich für die Ausführung des Co-op Translators.
- **Language Model Resource**:  
  - **Azure OpenAI** oder andere LLMs. Details sind in den [supported models and services](../../../../README.md) zu finden.
- **Computer Vision Resource** (optional):  
  - Für die Bildübersetzung. Ist diese nicht verfügbar, wechselt der Translator in den [Markdown-only mode](../markdown-only-mode.md).  
  - **Azure Computer Vision**

## Inhaltsverzeichnis

1. [Erstellen einer '.env'-Datei im Stammverzeichnis](./create-env-file.md)  
   - Fügen Sie die erforderlichen Schlüssel für den gewählten Language Model Service hinzu.  
   - Wenn die Azure Computer Vision Schlüssel weggelassen werden oder `-md` angegeben ist, arbeitet der Translator im Markdown-only mode.  
1. [Installation des Co-op translator Pakets](./install-package.md)  
1. [Übersetzen Ihres Projekts mit Co-op Translator](./translator-your-project.md)

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.