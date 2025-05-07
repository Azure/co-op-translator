<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b6d85d887d2664539a438dae5d0dfa50",
  "translation_date": "2025-05-06T17:56:38+00:00",
  "source_file": "getting_started/command-line-guide/install-package.md",
  "language_code": "de"
}
-->
# Installation des Co-op Translator Pakets

Der **Co-op Translator** ist ein Kommandozeilen-Tool (CLI), das Ihnen dabei hilft, alle Markdown-Dateien und Bilder in Ihrem Projekt in mehrere Sprachen zu übersetzen. Dieses Tutorial führt Sie durch die Konfiguration des Translators und dessen Anwendung für verschiedene Anwendungsfälle.

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

### Installation des Pakets und der benötigten Abhängigkeiten

Sobald Ihre virtuelle Umgebung eingerichtet und aktiviert ist, ist der nächste Schritt die Installation der erforderlichen Abhängigkeiten.

### Schnelle Installation

Installation des Co-Op Translators über pip

```
pip install co-op-translator
```  
Oder  

Installation über Poetry  
```
poetry add co-op-translator
```

#### Verwendung von pip (aus requirements.txt), falls Sie dieses Repo klonen

![NOTE] Bitte tun Sie dies NICHT, wenn Sie den Co-op Translator über die schnelle Installation installieren.

1. Wenn Sie pip verwenden, geben Sie den folgenden Befehl in Ihrem Terminal ein. Dadurch werden automatisch die erforderlichen Pakete installiert, die in der `requirements.txt` Datei angegeben sind:

    ```bash
    pip install -r requirements.txt
    ```

#### Verwendung von Poetry (aus pyproject.toml)

1. Wenn Sie Poetry verwenden, geben Sie den folgenden Befehl in Ihrem Terminal ein. Dadurch werden automatisch die erforderlichen Pakete installiert, die in der `pyproject.toml` Datei angegeben sind:

    ```bash
    poetry install
    ```

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache ist als maßgebliche Quelle zu betrachten. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.