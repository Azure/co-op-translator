<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "758ca1c5ae0d32c52d2dd59132dcfbf0",
  "translation_date": "2025-11-30T09:47:46+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "de"
}
-->
# Beitrag zu Co-op Translator

Dieses Projekt freut sich über Beiträge und Vorschläge. Die meisten Beiträge erfordern, dass Sie einer Contributor License Agreement (CLA) zustimmen, die bestätigt, dass Sie das Recht haben und tatsächlich die Rechte einräumen, Ihre Beiträge zu verwenden. Details finden Sie unter https://cla.opensource.microsoft.com.

Wenn Sie eine Pull-Anfrage einreichen, prüft ein CLA-Bot automatisch, ob Sie eine CLA bereitstellen müssen, und versieht die PR entsprechend (z. B. Statusprüfung, Kommentar). Folgen Sie einfach den Anweisungen des Bots. Dies müssen Sie nur einmal für alle Repositories mit unserer CLA tun.

## Einrichtung der Entwicklungsumgebung

Für die Einrichtung der Entwicklungsumgebung dieses Projekts empfehlen wir Poetry zur Verwaltung der Abhängigkeiten. Wir verwenden `pyproject.toml` zur Verwaltung der Projektabhängigkeiten, daher sollten Sie zum Installieren der Abhängigkeiten Poetry verwenden.

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

### Installation des Pakets und der benötigten Pakete

#### Mit Poetry (aus pyproject.toml)

```bash
poetry install
```

### Manuelles Testen

Bevor Sie eine PR einreichen, ist es wichtig, die Übersetzungsfunktionalität mit echter Dokumentation zu testen:

1. Erstellen Sie im Stammverzeichnis ein Testverzeichnis:
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

5. Überprüfen Sie die übersetzten Dateien in `test_docs/translations` und `test_docs/translated_images`, um sicherzustellen:
   - Die Übersetzungsqualität
   - Die Metadaten-Kommentare sind korrekt
   - Die ursprüngliche Markdown-Struktur bleibt erhalten
   - Links und Bilder funktionieren einwandfrei

Dieses manuelle Testen hilft sicherzustellen, dass Ihre Änderungen in realen Szenarien gut funktionieren.

### Umgebungsvariablen

1. Erstellen Sie eine `.env`-Datei im Stammverzeichnis, indem Sie die bereitgestellte `.env.template` kopieren.
1. Füllen Sie die Umgebungsvariablen entsprechend der Anleitung aus.

> [!TIP]
>
> ### Weitere Optionen für die Entwicklungsumgebung
>
> Neben dem lokalen Ausführen des Projekts können Sie auch GitHub Codespaces oder VS Code Dev Containers als alternative Entwicklungsumgebungen nutzen.
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
> #### Lokales Ausführen mit VS Code Dev Containers
>
> ⚠️ Diese Option funktioniert nur, wenn Docker Desktop mindestens 16 GB RAM zugewiesen ist. Wenn Sie weniger als 16 GB RAM haben, können Sie die [GitHub Codespaces-Option](../..) nutzen oder die lokale Einrichtung vornehmen.
>
> Eine verwandte Option sind VS Code Dev Containers, die das Projekt in Ihrem lokalen VS Code mit der [Dev Containers-Erweiterung](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) öffnen:
>
> 1. Starten Sie Docker Desktop (installieren Sie es, falls noch nicht geschehen)
> 2. Öffnen Sie das Projekt:
>
>    [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator)


### Code-Stil

Wir verwenden [Black](https://github.com/psf/black) als Python-Code-Formatter, um einen einheitlichen Code-Stil im Projekt sicherzustellen. Black ist ein kompromissloser Formatter, der Python-Code automatisch so formatiert, dass er dem Black-Stil entspricht.

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

## Co-op Translator ausführen

Um Co-op Translator mit Poetry in Ihrer Umgebung auszuführen, gehen Sie wie folgt vor:

1. Navigieren Sie in das Verzeichnis, in dem Sie Übersetzungstests durchführen möchten, oder erstellen Sie einen temporären Ordner für Tests.

2. Führen Sie den folgenden Befehl aus. Ersetzen Sie `-l ko` durch den Sprachcode, in den Sie übersetzen möchten. Das `-d`-Flag aktiviert den Debug-Modus.

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> [!NOTE]
> Stellen Sie sicher, dass Ihre Poetry-Umgebung aktiviert ist (poetry shell), bevor Sie den Befehl ausführen.

## Neue Sprache beitragen

Wir freuen uns über Beiträge, die Unterstützung für neue Sprachen hinzufügen. Bitte führen Sie vor dem Öffnen einer PR die folgenden Schritte durch, um eine reibungslose Überprüfung zu gewährleisten.

1. Fügen Sie die Sprache zur Schriftartenzuordnung hinzu
   - Bearbeiten Sie `src/co_op_translator/fonts/font_language_mappings.yml`
   - Fügen Sie einen Eintrag mit folgenden Angaben hinzu:
     - `code`: ISO-ähnlicher Sprachcode (z. B. `vi`)
     - `name`: Benutzerfreundlicher Anzeigename
     - `font`: Eine Schriftart aus `src/co_op_translator/fonts/`, die das Schriftsystem unterstützt
     - `rtl`: `true`, wenn von rechts nach links, sonst `false`

2. Fügen Sie erforderliche Schriftdateien hinzu (falls nötig)
   - Wenn eine neue Schriftart benötigt wird, prüfen Sie die Lizenzkompatibilität für Open-Source-Verteilung
   - Fügen Sie die Schriftdatei zu `src/co_op_translator/fonts/` hinzu

3. Lokale Überprüfung
   - Führen Sie Übersetzungen für eine kleine Probe durch (Markdown, Bilder und Notebooks, je nach Bedarf)
   - Überprüfen Sie, ob die Ausgabe korrekt dargestellt wird, einschließlich Schriftarten und ggf. RTL-Layout

4. Dokumentation aktualisieren
   - Stellen Sie sicher, dass die Sprache in `getting_started/supported-languages.md` erscheint
   - Änderungen an `getting_started/README_languages_template.md` sind nicht erforderlich; diese Datei wird aus der unterstützten Liste generiert

5. Öffnen Sie eine PR
   - Beschreiben Sie die hinzugefügte Sprache und eventuelle Schrift-/Lizenzüberlegungen
   - Fügen Sie wenn möglich Screenshots der gerenderten Ausgabe bei

Beispiel für einen YAML-Eintrag:

```yaml
new_lang(code):
  name: "New Language"
  font: "NotoSans-Medium.ttf"
  rtl: false
```

### Neue Sprache testen

Sie können die neue Sprache mit folgendem Befehl testen:

```bash
# Erstellen und aktivieren Sie eine virtuelle Umgebung
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
# Installieren Sie das Entwicklungspaket
pip install -e .
# Führen Sie die Übersetzung aus
translate -l "new_lang"
```

## Maintainer

### Commit-Nachricht und Merge-Strategie

Um Konsistenz und Klarheit im Commit-Verlauf unseres Projekts zu gewährleisten, verwenden wir ein bestimmtes Format für Commit-Nachrichten **für die finale Commit-Nachricht** beim Einsatz der **Squash and Merge**-Strategie.

Wenn eine Pull-Anfrage (PR) gemerged wird, werden die einzelnen Commits zu einem einzigen Commit zusammengefasst. Die finale Commit-Nachricht sollte dem untenstehenden Format folgen, um eine saubere und konsistente Historie zu gewährleisten.

#### Format der Commit-Nachricht (für Squash and Merge)

Wir verwenden folgendes Format für Commit-Nachrichten:

```bash
<type>: <description> (#<PR-Nummer>)
```

- **type**: Gibt die Kategorie des Commits an. Wir verwenden folgende Typen:
  - `Docs`: Für Dokumentationsänderungen.
  - `Build`: Für Änderungen am Build-System oder Abhängigkeiten, einschließlich Updates an Konfigurationsdateien, CI-Workflows oder Dockerfile.
  - `Core`: Für Änderungen an der Kernfunktionalität oder Features des Projekts, insbesondere Dateien im Verzeichnis `src/co_op_translator/core`.

- **description**: Eine kurze Zusammenfassung der Änderung.
- **PR-Nummer**: Die Nummer der zugehörigen Pull-Anfrage.

**Beispiele**:

- `Docs: Installationsanleitung für bessere Verständlichkeit aktualisiert (#50)`
- `Core: Verbesserung der Bildübersetzungsbehandlung (#60)`

> [!NOTE]
> Derzeit werden die Präfixe **`Docs`**, **`Core`** und **`Build`** automatisch basierend auf den Labels, die auf den geänderten Quellcode angewendet werden, zu PR-Titeln hinzugefügt. Solange das korrekte Label gesetzt ist, müssen Sie den PR-Titel normalerweise nicht manuell anpassen. Prüfen Sie nur, ob alles korrekt ist und der Präfix entsprechend generiert wurde.

#### Merge-Strategie

Wir verwenden **Squash and Merge** als Standardstrategie für Pull-Anfragen. Diese Strategie stellt sicher, dass Commit-Nachrichten unserem Format entsprechen, auch wenn einzelne Commits dies nicht tun.

**Gründe**:

- Eine saubere, lineare Projekt-Historie.
- Konsistenz bei Commit-Nachrichten.
- Weniger Rauschen durch kleine Commits (z. B. "Tippfehler korrigiert").

Beim Mergen stellen Sie sicher, dass die finale Commit-Nachricht dem oben beschriebenen Format entspricht.

**Beispiel für Squash and Merge**  
Wenn eine PR folgende Commits enthält:

- `fix typo`  
- `update README`  
- `adjust formatting`

sollten diese zu folgendem Commit zusammengefasst werden:  
`Docs: Verbesserung der Dokumentationsklarheit und Formatierung (#65)`

### Release-Prozess

Dieser Abschnitt beschreibt den einfachsten Weg für Maintainer, eine neue Version von Co-op Translator zu veröffentlichen.

#### 1. Version in `pyproject.toml` erhöhen

1. Bestimmen Sie die nächste Versionsnummer (wir folgen Semantic Versioning: `MAJOR.MINOR.PATCH`).
2. Bearbeiten Sie `pyproject.toml` und aktualisieren Sie das Feld `version` unter `[tool.poetry]`.
3. Öffnen Sie eine dedizierte Pull-Anfrage, die nur die Version (und ggf. automatisch aktualisierte Lock-/Metadaten-Dateien) ändert.
4. Nach der Überprüfung verwenden Sie **Squash and Merge** und stellen sicher, dass die finale Commit-Nachricht dem oben beschriebenen Format entspricht.

#### 2. GitHub Release erstellen

1. Gehen Sie zur GitHub-Repository-Seite und öffnen Sie **Releases** → **Draft a new release**.
2. Erstellen Sie einen neuen Tag (z. B. `v0.13.0`) vom `main`-Branch.
3. Setzen Sie den Release-Titel auf dieselbe Version (z. B. `v0.13.0`).
4. Klicken Sie auf **Generate release notes**, um das Changelog automatisch zu füllen.
5. Optional können Sie den Text bearbeiten (z. B. um neu unterstützte Sprachen oder wichtige Änderungen hervorzuheben).
6. Veröffentlichen Sie den Release.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache ist als maßgebliche Quelle zu betrachten. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->