<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d95d7ec0097c5569ac16dd42840787a2",
  "translation_date": "2025-06-12T09:24:43+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "de"
}
-->
# Beitrag zum Co-op Translator

Dieses Projekt freut sich über Beiträge und Vorschläge. Die meisten Beiträge erfordern, dass Sie einer Contributor License Agreement (CLA) zustimmen, die bestätigt, dass Sie das Recht haben und tatsächlich gewähren, dass wir Ihre Beiträge verwenden dürfen. Weitere Informationen finden Sie unter https://cla.opensource.microsoft.com.

Wenn Sie eine Pull-Anfrage einreichen, prüft ein CLA-Bot automatisch, ob Sie eine CLA vorlegen müssen, und versieht die PR entsprechend (z. B. Statusprüfung, Kommentar). Folgen Sie einfach den Anweisungen des Bots. Dies müssen Sie nur einmal für alle Repositories mit unserer CLA tun.

## Einrichtung der Entwicklungsumgebung

Für die Einrichtung der Entwicklungsumgebung dieses Projekts empfehlen wir die Verwendung von Poetry zur Verwaltung der Abhängigkeiten. Wir verwenden `pyproject.toml` zur Verwaltung der Projektabhängigkeiten, daher sollten Sie Poetry verwenden, um die Abhängigkeiten zu installieren.

### Virtuelle Umgebung erstellen

#### Mit pip

```bash
python -m venv .venv
```

#### Mit Poetry

```bash
poetry init
```

### Aktivieren der virtuellen Umgebung

#### Für pip und Poetry

- Windows:

    ```bash
    .venv\Scripts\activate.bat
    ```

- Mac/Linux:

    ```bash
    source .venv/bin/activate
    ```

#### Mit Poetry

```bash
poetry shell
```

### Installation des Pakets und der benötigten Pakete

#### Mit Poetry (aus pyproject.toml)

```bash
poetry install
```

### Manuelles Testen

Bevor Sie eine PR einreichen, ist es wichtig, die Übersetzungsfunktion mit echter Dokumentation zu testen:

1. Erstellen Sie ein Testverzeichnis im Stammverzeichnis:
    ```bash
    mkdir test_docs
    ```

2. Kopieren Sie einige Markdown-Dokumentationen und Bilder, die Sie übersetzen möchten, in das Testverzeichnis. Zum Beispiel:
    ```bash
    cp /path/to/your/docs/*.md test_docs/
    cp /path/to/your/images/*.png test_docs/
    ```

3. Installieren Sie das Paket lokal:
    ```bash
    pip install -e .
    ```

4. Führen Sie Co-op Translator auf Ihren Testdokumenten aus:
    ```bash
    python -m co_op_translator --language-codes ko --root-dir test_docs
    ```

5. Überprüfen Sie die übersetzten Dateien im Verzeichnis `test_docs/translations` and `test_docs/translated_images` to verify:
   - The translation quality
   - The metadata comments are correct
   - The original markdown structure is preserved
   - Links and images are working properly

This manual testing helps ensure that your changes work well in real-world scenarios.

### Environment variables

1. Create an `.env` file in the root directory by copying the provided `.env.template`.
1. Füllen Sie die Umgebungsvariablen entsprechend der Anleitung aus.

> [!TIP]
>
> ### Zusätzliche Optionen für die Entwicklungsumgebung
>
> Zusätzlich zur lokalen Ausführung des Projekts können Sie auch GitHub Codespaces oder VS Code Dev Containers als alternative Entwicklungsumgebungen nutzen.
>
> #### GitHub Codespaces
>
> Sie können diese Beispiele virtuell mit GitHub Codespaces ausführen, ohne zusätzliche Einstellungen oder Konfigurationen.
>
> Der Button öffnet eine webbasierte VS Code-Instanz in Ihrem Browser:
>
> 1. Öffnen Sie die Vorlage (dies kann einige Minuten dauern):
>
>     [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/azure/co-op-translator)
>
> #### Lokale Ausführung mit VS Code Dev Containers
>
> ⚠️ Diese Option funktioniert nur, wenn Docker Desktop mindestens 16 GB RAM zugewiesen sind. Wenn Sie weniger als 16 GB RAM haben, können Sie die [GitHub Codespaces-Option](../..) nutzen oder die lokale Einrichtung vornehmen ([siehe oben](../..)).
>
> Eine verwandte Option sind VS Code Dev Containers, mit denen das Projekt in Ihrem lokalen VS Code unter Verwendung der [Dev Containers-Erweiterung](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) geöffnet wird:
>
> 1. Starten Sie Docker Desktop (installieren Sie es, falls noch nicht geschehen)
> 2. Öffnen Sie das Projekt:
>
>    [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator)


### Code-Stil

Wir verwenden [Black](https://github.com/psf/black) als Python-Code-Formatter, um einen einheitlichen Code-Stil im Projekt sicherzustellen. Black ist ein kompromissloser Code-Formatter, der Python-Code automatisch so formatiert, dass er dem Black-Code-Stil entspricht.

#### Konfiguration

Die Black-Konfiguration ist in unserer `pyproject.toml` festgelegt:

```toml
[tool.black]
line-length = 88
target-version = ['py310']
include = '\.pyi?$'
```

#### Installation von Black

Sie können Black entweder mit Poetry (empfohlen) oder pip installieren:

##### Mit Poetry

Black wird automatisch installiert, wenn Sie die Entwicklungsumgebung einrichten:
```bash
poetry install
```

##### Mit pip

Wenn Sie pip verwenden, können Sie Black direkt installieren:
```bash
pip install black
```

#### Verwendung von Black

##### Mit Poetry

1. Formatieren Sie alle Python-Dateien im Projekt:
    ```bash
    poetry run black .
    ```

2. Formatieren Sie eine bestimmte Datei oder ein Verzeichnis:
    ```bash
    poetry run black path/to/file_or_directory
    ```

##### Mit pip

1. Formatieren Sie alle Python-Dateien im Projekt:
    ```bash
    black .
    ```

2. Formatieren Sie eine bestimmte Datei oder ein Verzeichnis:
    ```bash
    black path/to/file_or_directory
    ```

> [!TIP]
> Wir empfehlen, Ihren Editor so einzurichten, dass er den Code beim Speichern automatisch mit Black formatiert. Die meisten modernen Editoren unterstützen dies über Erweiterungen oder Plugins.

## Ausführen von Co-op Translator

Um Co-op Translator mit Poetry in Ihrer Umgebung auszuführen, gehen Sie wie folgt vor:

1. Navigieren Sie in das Verzeichnis, in dem Sie Übersetzungstests durchführen möchten, oder erstellen Sie einen temporären Ordner für Testzwecke.

2. Führen Sie folgenden Befehl aus. Der Schalter `-l ko` with the language code you wish to translate into. The `-d` aktiviert den Debug-Modus.

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> [!NOTE]
> Stellen Sie sicher, dass Ihre Poetry-Umgebung aktiviert ist (poetry shell), bevor Sie den Befehl ausführen.

## Maintainer

### Commit-Nachricht und Merge-Strategie

Um Konsistenz und Klarheit in der Commit-Historie unseres Projekts sicherzustellen, verwenden wir ein bestimmtes Format für Commit-Nachrichten **für die abschließende Commit-Nachricht** bei Verwendung der **Squash and Merge**-Strategie.

Wenn eine Pull-Anfrage (PR) gemerged wird, werden die einzelnen Commits zu einem einzigen Commit zusammengefasst. Die abschließende Commit-Nachricht sollte folgendem Format entsprechen, um eine saubere und einheitliche Historie zu gewährleisten.

#### Format der Commit-Nachricht (für squash and merge)

Wir verwenden das folgende Format für Commit-Nachrichten:

```bash
<type>: <description> (#<PR number>)
```

- **type**: Gibt die Kategorie des Commits an. Folgende Typen verwenden wir:
  - `Docs`: For documentation updates.
  - `Build`: For changes related to the build system or dependencies, including updates to configuration files, CI workflows, or the Dockerfile.
  - `Core`: For modifications to the project's core functionality or features, particularly those involving files in the `src/co_op_translator/core` directory.

- **description**: A concise summary of the change.
- **PR number**: The number of the pull request associated with the commit.

**Examples**:

- `Docs: Update installation instructions for clarity (#50)`
- `Core: Improve handling of image translation (#60)`

> [!NOTE]
> Currently, the **`Docs`**, **`Core`**, and **`Build`** prefixes are automatically added to PR titles based on the labels applied to the modified source code. As long as the correct label is applied, you typically don't need to manually update the PR title. You just need to verify that everything is correct and the prefix has been generated appropriately.

#### Merge strategy

We use **Squash and Merge** as our default strategy for pull requests. This strategy ensures that commit messages follow our format, even if individual commits don't.

**Reasons**:

- A clean, linear project history.
- Consistency in commit messages.
- Reduced noise from minor commits (e.g., "fix typo").

When merging, ensure the final commit message follows the commit message format described above.

**Example of Squash and Merge**
If a PR contains the following commits:

- `fix typo`
- `update README`
- `adjust formatting`

They should be squashed into:
`Docs: Improve documentation clarity and formatting (#65)`

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache ist als maßgebliche Quelle zu betrachten. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die durch die Verwendung dieser Übersetzung entstehen.