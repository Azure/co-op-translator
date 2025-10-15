<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "20943a46b11c6d74814f41a817a6db4c",
  "translation_date": "2025-10-15T02:13:34+00:00",
  "source_file": "getting_started/command-line-guide/translator-your-project.md",
  "language_code": "de"
}
-->
# Übersetzen Sie Ihr Projekt mit dem Co-op Translator

Der **Co-op Translator** ist ein Kommandozeilen-Tool (CLI), mit dem Sie Markdown- und Bilddateien in Ihrem Projekt in mehrere Sprachen übersetzen können. In diesem Abschnitt erfahren Sie, wie Sie das Tool verwenden, welche CLI-Optionen es gibt und erhalten Beispiele für verschiedene Anwendungsfälle.

> [!NOTE]
> Eine vollständige Liste aller Befehle und deren ausführliche Beschreibung finden Sie in der [Befehlsreferenz](./command-reference.md).

---

## Beispiel-Szenarien und Befehle

Hier sind einige typische Anwendungsfälle für den **Co-op Translator** mit den passenden Befehlen.

### 1. Grundlegende Übersetzung (Einzelne Sprache)

Um Ihr gesamtes Projekt (Markdown-Dateien und Bilder) in eine einzelne Sprache, z. B. Koreanisch, zu übersetzen, verwenden Sie folgenden Befehl:

```bash
translate -l "ko"
```

Dieser Befehl übersetzt alle Markdown- und Bilddateien ins Koreanische und fügt neue Übersetzungen hinzu, ohne bestehende zu löschen.

> [!TIP]
>
> Sie möchten wissen, welche Sprachcodes im **Co-op Translator** verfügbar sind? Schauen Sie im Abschnitt [Supported Languages](https://github.com/Azure/co-op-translator#supported-languages) im Repository nach.

#### Beispiel im Phi-3 CookBook

Im **Phi-3 CookBook** habe ich folgende Methode verwendet, um die koreanische Übersetzung für die vorhandenen Markdown-Dateien und Bilder hinzuzufügen.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko"
Translating images: 100%|███████████████████████████████████████████████████| 276/276 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 153/153 [1:43:07<00:00, 241.31s/it]
```

### 2. Übersetzung in mehrere Sprachen

Um Ihr Projekt in mehrere Sprachen (z. B. Spanisch, Französisch und Deutsch) zu übersetzen, verwenden Sie diesen Befehl:

```bash
translate -l "es fr de"
```

Dieser Befehl übersetzt das Projekt in Spanisch, Französisch und Deutsch und fügt neue Übersetzungen hinzu, ohne bestehende zu überschreiben.

#### Beispiel im Phi-3 CookBook

Im **Phi-3 CookBook** habe ich nach dem Aktualisieren auf die neuesten Änderungen folgende Methode verwendet, um neu hinzugefügte Markdown-Dateien und Bilder zu übersetzen.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko ja zh tw es fr" -a
Translating images: 100%|███████████████████████████████████████████████████| 273/273 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 6/6 [24:07<00:00, 241.31s/it]
```

> [!NOTE]
> Es wird generell empfohlen, jeweils nur eine Sprache zu übersetzen. In Fällen wie diesem, in denen gezielte Änderungen hinzugefügt werden müssen, kann die Übersetzung mehrerer Sprachen gleichzeitig jedoch effizient sein.

### 3. Übersetzungen aktualisieren (Löscht bestehende Übersetzungen)

Um bestehende Übersetzungen zu aktualisieren (d. h. die aktuellen Übersetzungen zu löschen und durch neue zu ersetzen), verwenden Sie die Option `-u`. Dadurch werden alle vorhandenen Übersetzungen für die angegebenen Sprachen gelöscht und neu übersetzt.

```bash
translate -l "ko" -u
```

Achtung: Dieser Befehl fordert Sie vor dem Löschen der bestehenden Übersetzungen zur Bestätigung auf.

#### Beispiel im Phi-3 CookBook

Im **Phi-3 CookBook** habe ich folgende Methode verwendet, um alle übersetzten Dateien auf Spanisch zu aktualisieren. Ich empfehle diese Methode, wenn es größere Änderungen am Originalinhalt in mehreren Markdown-Dokumenten gibt. Wenn nur wenige übersetzte Markdown-Dateien aktualisiert werden müssen, ist es effizienter, diese gezielt zu löschen und dann mit der `-a` Methode die aktualisierten Übersetzungen hinzuzufügen.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "es" -u
Warning: The update command will delete all existing translations for 'es' and re-translate everything.
Do you want to continue? Type 'yes' to proceed: yes
Proceeding with update...
Translating images: 100%|████████████████████████████████████████████| 150/150 [43:46<00:00, 15.55s/it]
Translating markdown files: 100%|███████████████████████████████████| 95/95 [1:40:27<00:00, 125.62s/it]
```

### 5. Nur Bilder übersetzen

Um nur die Bilddateien in Ihrem Projekt zu übersetzen, verwenden Sie die Option `-img`:

```bash
translate -l "ko" -img
```

Dieser Befehl übersetzt ausschließlich die Bilder ins Koreanische, ohne die Markdown-Dateien zu verändern.

### 6. Nur Markdown-Dateien übersetzen

Um nur die Markdown-Dateien in Ihrem Projekt zu übersetzen, verwenden Sie die Option `-md`:

```bash
translate -l "ko" -md
```

#### Beispiel im Phi-3 CookBook

Im **Phi-3 CookBook** habe ich folgende Methode verwendet, um Übersetzungsfehler in den koreanischen Dateien zu prüfen und die Übersetzung für fehlerhafte Dateien automatisch erneut auszuführen.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko" -chk 
Checking translated files for errors in ko...
Checking files for ko: 100%|██████████████████████████████████████████████████| 95/95 [00:01<00:00, 65.47file/s]
Retrying vsc-extension-quickstart.md for ko:   0%|                                     | 0/17 [00:00<?, ?file/s] 
```

Diese Option prüft auf Übersetzungsfehler. Aktuell wird eine Datei als fehlerhaft markiert, wenn die Anzahl der Zeilenumbrüche im Original und in der Übersetzung um mehr als sechs abweicht. Ich plane, dieses Kriterium künftig flexibler zu gestalten.

Diese Methode ist zum Beispiel hilfreich, um fehlende Abschnitte oder beschädigte Übersetzungen zu erkennen und die Übersetzung für diese Dateien automatisch zu wiederholen.

Wenn Sie jedoch bereits wissen, welche Dateien problematisch sind, ist es effizienter, diese gezielt zu löschen und mit der `-a` Option erneut zu übersetzen.

### 8. Debug-Modus

Um detaillierte Protokolle zur Fehlerbehebung zu erhalten, verwenden Sie die Option `-d`:

```bash
translate -l "ko" -d
```

Dieser Befehl führt die Übersetzung im Debug-Modus aus und liefert zusätzliche Protokollinformationen, die bei der Fehlersuche helfen können.

#### Beispiel im Phi-3 CookBook

Im **Phi-3 CookBook** bin ich auf ein Problem gestoßen, bei dem Übersetzungen mit vielen Links in Markdown-Dateien zu Formatierungsfehlern führten, z. B. zu fehlerhaften Übersetzungen und ignorierten Zeilenumbrüchen. Um das Problem zu analysieren, habe ich die Option `-d` verwendet, um den Ablauf der Übersetzung zu beobachten.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "ko" -d
DEBUG:openai._base_client:Request options: {'method': 'post', 'url': '/chat/completions', 'headers': {'api-key': 'af04e0bea45747d8a7b8c131c1971044'}, 'files': None, 'json_data': {'messages': [{'role': 'user', 'content': "Translate the following text to ko. NEVER ADD ANY EXTRA CONTENT OUTSIDE THE TRANSLATION. TRANSLATE ONLY WHAT IS GIVEN TO YOU.. MAINTAIN MARKDOWN FORMAT\n\n# Phi-3 Cookbook: Hands-On Examples with Microsoft's Phi-3 Models [![Open and use the samples in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phi-3cookbook) [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%
...
```

### 9. Übersetzung in alle Sprachen

Wenn Sie das Projekt in alle unterstützten Sprachen übersetzen möchten, verwenden Sie das Schlüsselwort all.

> [!WARNING]
> Die Übersetzung in alle Sprachen kann je nach Projektgröße sehr viel Zeit in Anspruch nehmen. Zum Beispiel hat die Übersetzung des **Phi-3 CookBook** ins Spanische etwa 2 Stunden gedauert. Bei diesem Umfang ist es nicht praktikabel, dass eine Person 20 Sprachen übernimmt. Es empfiehlt sich, die Arbeit auf mehrere Mitwirkende aufzuteilen, sodass jeder ein oder zwei Sprachen betreut und die Übersetzungen schrittweise aktualisiert werden.

```bash
translate -l "all"
```

Dieser Befehl übersetzt das Projekt in alle verfügbaren Sprachen. Je nach Größe des Projekts kann die Übersetzung viel Zeit in Anspruch nehmen.

> [!TIP]
>
> ### Manuelles Löschen von übersetzten Dateien (optional)
> Übersetzte Dateien werden jetzt automatisch erkannt und bereinigt, wenn eine Quelldatei aktualisiert wird.
>
> Wenn Sie jedoch eine Übersetzung manuell aktualisieren möchten – z. B. um eine bestimmte Datei neu zu übersetzen oder das Systemverhalten zu überschreiben – können Sie mit folgendem Befehl alle Versionen der Datei in den Sprachordnern löschen.
>
> ### Unter Windows:
> 1. **Mit der Eingabeaufforderung**:
>    - Öffnen Sie die Eingabeaufforderung.
>    - Navigieren Sie mit dem Befehl `cd` in den Ordner, in dem sich die Dateien befinden.
>    - Verwenden Sie folgenden Befehl zum Löschen:
>      ```
>      del /s *filename*
>      ```
>      Ersetzen Sie `filename` durch den entsprechenden Teil des Dateinamens. Die Option `/s` durchsucht auch Unterordner.
>
> 2. **Mit PowerShell**:
>    - Öffnen Sie PowerShell.
>    - Führen Sie diesen Befehl aus:
>      ```powershell
>      Get-ChildItem -Path "C:\YourPath" -Filter "*filename*" -Recurse | Remove-Item -Force
>      ```
>      Ersetzen Sie `"C:\YourPath"` durch den Ordnerpfad und `filename` durch den entsprechenden Namen.
>
> ### Unter macOS/Linux:
> 1. **Mit dem Terminal**:
>   - Öffnen Sie das Terminal.
>   - Navigieren Sie mit `cd` in das Verzeichnis.
>   - Verwenden Sie den Befehl `find`:
>     ```bash
>     find . -type f -name "*filename*" -delete
>     ```
>     Ersetzen Sie `filename` durch den entsprechenden Namen.
>
> Überprüfen Sie die Dateien immer sorgfältig, bevor Sie sie löschen, um versehentlichen Datenverlust zu vermeiden.
>
> Nachdem Sie die zu ersetzenden Dateien gelöscht haben, führen Sie einfach erneut Ihren `translate -l` Befehl aus, um die neuesten Änderungen zu aktualisieren.

---

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ausgangssprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.