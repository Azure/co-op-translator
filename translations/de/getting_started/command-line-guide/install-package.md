<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "510827ad22a2031a50838919c3594828",
  "translation_date": "2025-10-15T02:13:28+00:00",
  "source_file": "getting_started/command-line-guide/install-package.md",
  "language_code": "de"
}
-->
# Installiere das Co-op Translator Paket

Der **Co-op Translator** ist ein Kommandozeilen-Tool (CLI), das dir hilft, alle Markdown-Dateien und Bilder in deinem Projekt in mehrere Sprachen zu übersetzen. In dieser Anleitung erfährst du, wie du den Translator konfigurierst und für verschiedene Anwendungsfälle nutzt.

### Erstelle eine virtuelle Umgebung

Du kannst eine virtuelle Umgebung entweder mit `pip` oder `Poetry` erstellen. Gib einen der folgenden Befehle in deinem Terminal ein.

#### Mit pip

```bash
python -m venv .venv
```

#### Mit Poetry

```bash
poetry init
```

### Aktiviere die virtuelle Umgebung

Nachdem du die virtuelle Umgebung erstellt hast, musst du sie aktivieren. Die Schritte unterscheiden sich je nach Betriebssystem. Gib den folgenden Befehl in deinem Terminal ein.

#### Für pip und Poetry

- Windows:

    ```bash
    .venv\Scripts\activate
    ```

- Mac/Linux:

    ```bash
    source .venv/bin/activate
    ```

#### Mit Poetry

1. Wenn du die Umgebung mit Poetry erstellt hast, gib den folgenden Befehl in deinem Terminal ein, um sie zu aktivieren.

    ```bash
    poetry shell
    ```

### Installation des Pakets und der benötigten Abhängigkeiten

Sobald deine virtuelle Umgebung eingerichtet und aktiviert ist, installierst du die notwendigen Abhängigkeiten.

### Schnelle Installation

Installiere den Co-Op Translator mit pip

```
pip install co-op-translator
```
Oder 

Installiere mit Poetry
```
poetry add co-op-translator
```

#### Mit pip (über requirements.txt), wenn du dieses Repo klonst

> [!NOTE]
> Bitte mache dies NICHT, wenn du den Co-op Translator über die schnelle Installation installierst.

1. Wenn du pip verwendest, gib den folgenden Befehl in deinem Terminal ein. Damit werden automatisch die benötigten Pakete aus der Datei `requirements.txt` installiert:

    ```bash
    pip install -r requirements.txt
    ```

#### Mit Poetry (über pyproject.toml)

1. Wenn du Poetry verwendest, gib den folgenden Befehl in deinem Terminal ein. Damit werden automatisch die benötigten Pakete aus der Datei `pyproject.toml` installiert:

    ```bash
    poetry install
    ```

---

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ausgangssprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.