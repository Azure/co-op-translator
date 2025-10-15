<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "bd4704f50c55da7d572b691484aa0b30",
  "translation_date": "2025-10-15T02:11:57+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "de"
}
-->
# Beitrag zu Co-op Translator

Dieses Projekt freut sich über Beiträge und Vorschläge. Die meisten Beiträge erfordern, dass du eine Contributor License Agreement (CLA) akzeptierst, in der du bestätigst, dass du das Recht hast, uns die Nutzungsrechte an deinem Beitrag zu gewähren. Weitere Informationen findest du unter https://cla.opensource.microsoft.com.

Wenn du einen Pull Request einreichst, prüft ein CLA-Bot automatisch, ob du eine CLA abgeben musst, und kennzeichnet den PR entsprechend (z. B. Statusprüfung, Kommentar). Folge einfach den Anweisungen des Bots. Dies musst du nur einmal für alle Repositories tun, die unsere CLA verwenden.

## Entwicklungsumgebung einrichten

Um die Entwicklungsumgebung für dieses Projekt einzurichten, empfehlen wir die Verwendung von Poetry zur Verwaltung der Abhängigkeiten. Wir nutzen `pyproject.toml` zur Verwaltung der Projektabhängigkeiten. Daher solltest du für die Installation von Abhängigkeiten Poetry verwenden.

### Erstellen einer virtuellen Umgebung

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

### Installation des Pakets und der benötigten Abhängigkeiten

#### Mit Poetry (aus pyproject.toml)

```bash
poetry install
```

### Manuelles Testen

Bevor du einen PR einreichst, ist es wichtig, die Übersetzungsfunktion mit echter Dokumentation zu testen:

1. Erstelle ein Testverzeichnis im Hauptverzeichnis:
    ```bash
    mkdir test_docs
    ```

2. Kopiere einige Markdown-Dokumentationen und Bilder, die du übersetzen möchtest, in das Testverzeichnis. Zum Beispiel:
    ```bash
    cp /path/to/your/docs/*.md test_docs/
    cp /path/to/your/images/*.png test_docs/
    ```

3. Installiere das Paket lokal:
    ```bash
    pip install -e .
    ```

4. Führe Co-op Translator auf deinen Testdokumenten aus:
    ```bash
    python -m co_op_translator --language-codes ko --root-dir test_docs
    ```

5. Überprüfe die übersetzten Dateien in `test_docs/translations` und `test_docs/translated_images`, um sicherzustellen:
   - Die Übersetzungsqualität stimmt
   - Die Metadaten-Kommentare korrekt sind
   - Die ursprüngliche Markdown-Struktur erhalten bleibt
   - Links und Bilder richtig funktionieren

Dieses manuelle Testen hilft sicherzustellen, dass deine Änderungen auch in realen Szenarien funktionieren.

### Umgebungsvariablen

1. Erstelle eine `.env`-Datei im Hauptverzeichnis, indem du die bereitgestellte `.env.template`-Datei kopierst.
1. Fülle die Umgebungsvariablen wie angegeben aus.

> [!TIP]
>
> ### Weitere Optionen für die Entwicklungsumgebung
>
> Neben dem lokalen Ausführen des Projekts kannst du auch GitHub Codespaces oder VS Code Dev Containers als alternative Entwicklungsumgebung nutzen.
>
> #### GitHub Codespaces
>
> Du kannst diese Beispiele virtuell mit GitHub Codespaces ausführen, ohne zusätzliche Einstellungen oder Installationen.
>
> Der Button öffnet eine webbasierte VS Code-Instanz in deinem Browser:
>
> 1. Öffne die Vorlage (dies kann einige Minuten dauern):
>
>     [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/azure/co-op-translator)
>
> #### Lokal mit VS Code Dev Containers ausführen
>
> ⚠️ Diese Option funktioniert nur, wenn deinem Docker Desktop mindestens 16 GB RAM zugewiesen sind. Wenn du weniger als 16 GB RAM hast, kannst du die [GitHub Codespaces-Option](../..) ausprobieren oder [es lokal einrichten](../..).
>
> Eine verwandte Option sind VS Code Dev Containers, mit denen du das Projekt in deinem lokalen VS Code mit der [Dev Containers-Erweiterung](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) öffnen kannst:
>
> 1. Starte Docker Desktop (installiere es, falls noch nicht geschehen)
> 2. Öffne das Projekt:
>
>    [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator)


### Code-Stil

Wir verwenden [Black](https://github.com/psf/black) als Python-Code-Formatter, um einen einheitlichen Code-Stil im gesamten Projekt zu gewährleisten. Black ist ein kompromissloser Code-Formatter, der Python-Code automatisch an den Black-Code-Stil anpasst.

#### Konfiguration

Die Black-Konfiguration ist in unserer `pyproject.toml` festgelegt:

```toml
[tool.black]
line-length = 88
target-version = ['py310']
include = '\.pyi?$'
```

#### Black installieren

Du kannst Black entweder mit Poetry (empfohlen) oder pip installieren:

##### Mit Poetry

Black wird automatisch installiert, wenn du die Entwicklungsumgebung einrichtest:
```bash
poetry install
```

##### Mit pip

Wenn du pip verwendest, kannst du Black direkt installieren:
```bash
pip install black
```

#### Black verwenden

##### Mit Poetry

1. Formatiere alle Python-Dateien im Projekt:
    ```bash
    poetry run black .
    ```

2. Formatiere eine bestimmte Datei oder ein Verzeichnis:
    ```bash
    poetry run black path/to/file_or_directory
    ```

##### Mit pip

1. Formatiere alle Python-Dateien im Projekt:
    ```bash
    black .
    ```

2. Formatiere eine bestimmte Datei oder ein Verzeichnis:
    ```bash
    black path/to/file_or_directory
    ```

> [!TIP]
> Wir empfehlen, deinen Editor so einzurichten, dass der Code beim Speichern automatisch mit Black formatiert wird. Die meisten modernen Editoren unterstützen dies über Erweiterungen oder Plugins.

## Co-op Translator ausführen

Um Co-op Translator mit Poetry in deiner Umgebung auszuführen, folge diesen Schritten:

1. Wechsle in das Verzeichnis, in dem du Übersetzungstests durchführen möchtest, oder erstelle einen temporären Ordner zu Testzwecken.

2. Führe den folgenden Befehl aus. Ersetze `-l ko` durch den Sprachcode, in den du übersetzen möchtest. Das `-d`-Flag aktiviert den Debug-Modus.

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> [!NOTE]
> Stelle sicher, dass deine Poetry-Umgebung aktiviert ist (poetry shell), bevor du den Befehl ausführst.

## Eine neue Sprache beitragen

Wir freuen uns über Beiträge, die neue Sprachen unterstützen. Bitte führe vor dem Öffnen eines PRs die folgenden Schritte durch, um eine reibungslose Überprüfung zu gewährleisten.

1. Sprache zur Schriftarten-Zuordnung hinzufügen
   - Bearbeite `src/co_op_translator/fonts/font_language_mappings.yml`
   - Füge einen Eintrag hinzu mit:
     - `code`: ISO-ähnlicher Sprachcode (z. B. `vi`)
     - `name`: Benutzerfreundlicher Anzeigename
     - `font`: Eine Schriftart aus `src/co_op_translator/fonts/`, die das Schriftsystem unterstützt
     - `rtl`: `true` bei Rechts-nach-Links-Schrift, sonst `false`

2. Benötigte Schriftdateien einbinden (falls erforderlich)
   - Wenn eine neue Schriftart benötigt wird, prüfe die Lizenz auf Kompatibilität mit Open Source
   - Füge die Schriftdatei zu `src/co_op_translator/fonts/` hinzu

3. Lokale Überprüfung
   - Führe Übersetzungen für eine kleine Probe durch (Markdown, Bilder und Notebooks, falls zutreffend)
   - Überprüfe, ob die Ausgabe korrekt dargestellt wird, einschließlich Schriftarten und ggf. RTL-Layout

4. Dokumentation aktualisieren
   - Stelle sicher, dass die Sprache in `getting_started/supported-languages.md` aufgeführt ist
   - Änderungen an `README_languages_template.md` sind nicht erforderlich; diese Datei wird aus der unterstützten Liste generiert

5. PR eröffnen
   - Beschreibe die hinzugefügte Sprache und ggf. Schrift-/Lizenzüberlegungen
   - Füge nach Möglichkeit Screenshots der gerenderten Ausgaben bei

Beispiel für einen YAML-Eintrag:

```yaml
new_lang(code):
  name: "New Language"
  font: "NotoSans-Medium.ttf"
  rtl: false
```


## Maintainer

### Commit-Nachricht und Merge-Strategie

Um Konsistenz und Klarheit in der Commit-Historie unseres Projekts zu gewährleisten, folgen wir einem bestimmten Format für Commit-Nachrichten **für die finale Commit-Nachricht** bei Verwendung der **Squash and Merge**-Strategie.

Wenn ein Pull Request (PR) gemergt wird, werden die einzelnen Commits zu einem einzigen Commit zusammengefasst. Die finale Commit-Nachricht sollte dem untenstehenden Format folgen, um eine saubere und konsistente Historie zu erhalten.

#### Format der Commit-Nachricht (für Squash and Merge)

Wir verwenden folgendes Format für Commit-Nachrichten:

```bash
<type>: <description> (#<PR number>)
```

- **type**: Gibt die Kategorie des Commits an. Wir verwenden folgende Typen:
  - `Docs`: Für Aktualisierungen der Dokumentation.
  - `Build`: Für Änderungen am Build-System oder an Abhängigkeiten, einschließlich Updates an Konfigurationsdateien, CI-Workflows oder der Dockerfile.
  - `Core`: Für Änderungen an der Kernfunktionalität des Projekts, insbesondere an Dateien im Verzeichnis `src/co_op_translator/core`.

- **description**: Eine kurze Zusammenfassung der Änderung.
- **PR number**: Die Nummer des Pull Requests, der mit dem Commit verknüpft ist.

**Beispiele**:

- `Docs: Update installation instructions for clarity (#50)`
- `Core: Improve handling of image translation (#60)`

> [!NOTE]
> Aktuell werden die Präfixe **`Docs`**, **`Core`** und **`Build`** automatisch zu PR-Titeln hinzugefügt, basierend auf den Labels, die dem geänderten Quellcode zugewiesen sind. Solange das richtige Label gesetzt ist, musst du den PR-Titel normalerweise nicht manuell anpassen. Du solltest nur überprüfen, ob alles korrekt ist und das Präfix richtig generiert wurde.

#### Merge-Strategie

Wir verwenden **Squash and Merge** als Standardstrategie für Pull Requests. Diese Strategie stellt sicher, dass Commit-Nachrichten unserem Format entsprechen, auch wenn einzelne Commits dies nicht tun.

**Gründe**:

- Eine saubere, lineare Projekt-Historie.
- Konsistenz bei Commit-Nachrichten.
- Weniger "Rauschen" durch kleinere Commits (z. B. "fix typo").

Beim Mergen stelle sicher, dass die finale Commit-Nachricht dem oben beschriebenen Format entspricht.

**Beispiel für Squash and Merge**
Wenn ein PR folgende Commits enthält:

- `fix typo`
- `update README`
- `adjust formatting`

Sollten sie zusammengefasst werden zu:
`Docs: Improve documentation clarity and formatting (#65)`

---

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ausgangssprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die durch die Nutzung dieser Übersetzung entstehen.