<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b6d85d887d2664539a438dae5d0dfa50",
  "translation_date": "2025-06-12T18:30:59+00:00",
  "source_file": "getting_started/command-line-guide/install-package.md",
  "language_code": "de"
}
-->
# Installation des Co-op Translator Pakets

Der **Co-op Translator** ist ein Kommandozeilen-Tool (CLI), das Ihnen dabei hilft, alle Markdown-Dateien und Bilder in Ihrem Projekt in mehrere Sprachen zu übersetzen. Dieses Tutorial führt Sie durch die Konfiguration des Translators und die verschiedenen Anwendungsfälle.

### Erstellen einer virtuellen Umgebung

Sie können eine virtuelle Umgebung entweder mit `pip` oder `Poetry` erstellen. Geben Sie einen der folgenden Befehle in Ihrem Terminal ein.

#### Verwendung von pip

```bash
python -m venv .venv
```

#### Verwendung von Poetry

```bash
poetry init
```

### Aktivieren der virtuellen Umgebung

Nachdem Sie die virtuelle Umgebung erstellt haben, müssen Sie sie aktivieren. Die Schritte unterscheiden sich je nach Betriebssystem. Geben Sie den folgenden Befehl in Ihrem Terminal ein.

#### Für pip und Poetry

- Windows:

    ```bash
    .venv\Scripts\activate
    ```

- Mac/Linux:

    ```bash
    source .venv/bin/activate
    ```

#### Verwendung von Poetry

1. Wenn Sie die Umgebung mit Poetry erstellt haben, geben Sie den folgenden Befehl in Ihrem Terminal ein, um sie zu aktivieren.

    ```bash
    poetry shell
    ```

### Installation des Pakets und der erforderlichen Abhängigkeiten

Sobald Ihre virtuelle Umgebung eingerichtet und aktiviert ist, besteht der nächste Schritt darin, die notwendigen Abhängigkeiten zu installieren.

### Schnelle Installation

Installation des Co-Op Translators via pip

```
pip install co-op-translator
```
Oder 

Installation via Poetry

```
poetry add co-op-translator
```

#### Verwendung von pip (aus requirements.txt), falls Sie dieses Repository klonen

![NOTE] Bitte tun Sie dies NICHT, wenn Sie den Co-op Translator über die Schnellinstallation installieren.

1. Wenn Sie pip verwenden, geben Sie den folgenden Befehl in Ihrem Terminal ein. Dadurch werden automatisch die erforderlichen Pakete installiert, die in der Datei `requirements.txt` angegeben sind:

    ```bash
    pip install -r requirements.txt
    ```

#### Verwendung von Poetry (aus pyproject.toml)

1. Wenn Sie Poetry verwenden, geben Sie den folgenden Befehl in Ihrem Terminal ein. Dadurch werden automatisch die erforderlichen Pakete installiert, die in der Datei `pyproject.toml` angegeben sind:

    ```bash
    poetry install
    ```

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir auf Genauigkeit achten, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache gilt als maßgebliche Quelle. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die durch die Nutzung dieser Übersetzung entstehen.