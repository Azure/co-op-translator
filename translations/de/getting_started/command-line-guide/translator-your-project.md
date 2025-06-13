<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d238206c3503631e32774716d11d1868",
  "translation_date": "2025-06-12T18:39:50+00:00",
  "source_file": "getting_started/command-line-guide/translator-your-project.md",
  "language_code": "de"
}
-->
# Übersetze dein Projekt mit Co-op Translator

Der **Co-op Translator** ist ein Kommandozeilen-Tool (CLI), das dir hilft, Markdown- und Bilddateien in deinem Projekt in mehrere Sprachen zu übersetzen. Dieser Abschnitt erklärt, wie du das Tool benutzt, stellt die verschiedenen CLI-Optionen vor und gibt Beispiele für unterschiedliche Anwendungsfälle.

> [!NOTE]
> Für eine vollständige Liste der Befehle und deren ausführliche Beschreibungen, siehe bitte die [Command reference](./command-reference.md).

---

## Beispiel-Szenarien und Befehle

Hier sind einige gängige Anwendungsfälle für den **Co-op Translator** mit den passenden Befehlen.

### 1. Grundlegende Übersetzung (Eine Sprache)

Um dein gesamtes Projekt (Markdown-Dateien und Bilder) in eine einzelne Sprache, z. B. Koreanisch, zu übersetzen, verwende den folgenden Befehl:

```bash
translate -l "ko"
```

Dieser Befehl übersetzt alle Markdown- und Bilddateien ins Koreanische und fügt neue Übersetzungen hinzu, ohne vorhandene zu löschen.

> [!TIP]
>
> Möchtest du wissen, welche Sprachcodes im **Co-op Translator** verfügbar sind? Schau dir den Abschnitt [Supported Languages](https://github.com/Azure/co-op-translator#supported-languages) im Repository an.

#### Beispiel im Phi-3 CookBook

Im **Phi-3 CookBook** habe ich die folgende Methode verwendet, um die koreanische Übersetzung für die bestehenden Markdown-Dateien und Bilder hinzuzufügen.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko"
Translating images: 100%|███████████████████████████████████████████████████| 276/276 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 153/153 [1:43:07<00:00, 241.31s/it]
```

### 2. Übersetzung in mehrere Sprachen

Um dein Projekt in mehrere Sprachen zu übersetzen (z. B. Spanisch, Französisch und Deutsch), verwende diesen Befehl:

```bash
translate -l "es fr de"
```

Dieser Befehl übersetzt das Projekt in Spanisch, Französisch und Deutsch und fügt neue Übersetzungen hinzu, ohne bestehende zu überschreiben.

#### Beispiel im Phi-3 CookBook

Im **Phi-3 CookBook** habe ich nach dem Einholen der neuesten Änderungen, um die aktuellsten Commits zu berücksichtigen, die folgende Methode genutzt, um neu hinzugefügte Markdown-Dateien und Bilder zu übersetzen.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko ja zh tw es fr" -a
Translating images: 100%|███████████████████████████████████████████████████| 273/273 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 6/6 [24:07<00:00, 241.31s/it]
```

> [!NOTE]
> Obwohl es generell empfohlen wird, jeweils nur eine Sprache zu übersetzen, kann es in Situationen wie dieser, bei der bestimmte Änderungen hinzugefügt werden müssen, effizient sein, mehrere Sprachen gleichzeitig zu übersetzen.

### 3. Übersetzungen aktualisieren (löscht bestehende Übersetzungen)

Um bestehende Übersetzungen zu aktualisieren (d.h. die aktuellen Übersetzungen zu löschen und durch neue zu ersetzen), benutze die Option `-u`. Dadurch werden alle bestehenden Übersetzungen für die angegebenen Sprachen gelöscht und neu übersetzt.

```bash
translate -l "ko" -u
```

Warnung: Dieser Befehl fordert dich vor dem Löschen der bestehenden Übersetzungen zur Bestätigung auf.

#### Beispiel im Phi-3 CookBook

Im **Phi-3 CookBook** habe ich die folgende Methode verwendet, um alle übersetzten Dateien auf Spanisch zu aktualisieren. Ich empfehle diese Methode, wenn es größere Änderungen am Originalinhalt in mehreren Markdown-Dokumenten gibt. Sind nur wenige übersetzte Markdown-Dateien zu aktualisieren, ist es effizienter, diese Dateien manuell zu löschen und anschließend die `-a` Methode zu verwenden, um die aktualisierten Übersetzungen hinzuzufügen.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "es" -u
Warning: The update command will delete all existing translations for 'es' and re-translate everything.
Do you want to continue? Type 'yes' to proceed: yes
Proceeding with update...
Translating images: 100%|████████████████████████████████████████████| 150/150 [43:46<00:00, 15.55s/it]
Translating markdown files: 100%|███████████████████████████████████| 95/95 [1:40:27<00:00, 125.62s/it]
```

### 5. Nur Bilder übersetzen

Um nur die Bilddateien in deinem Projekt zu übersetzen, benutze die Option `-img`:

```bash
translate -l "ko" -img
```

Dieser Befehl übersetzt nur die Bilder ins Koreanische, ohne die Markdown-Dateien zu beeinflussen.

### 6. Nur Markdown-Dateien übersetzen

Um nur die Markdown-Dateien in deinem Projekt zu übersetzen, benutze die Option `-md`:

```bash
translate -l "ko" -md
```

### 7. Überprüfung auf Fehler in übersetzten Dateien

Wenn du übersetzte Dateien auf Fehler überprüfen und die Übersetzung bei Bedarf erneut ausführen möchtest, benutze die Option `-chk`:

```bash
translate -l "ko" -chk
```

Dieser Befehl durchsucht die übersetzten Markdown-Dateien und versucht, fehlerhafte Dateien erneut zu übersetzen.

#### Beispiel im Phi-3 CookBook

Im **Phi-3 CookBook** habe ich die folgende Methode verwendet, um Übersetzungsfehler in den koreanischen Dateien zu überprüfen und automatisch für Dateien mit Problemen die Übersetzung erneut zu starten.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko" -chk 
Checking translated files for errors in ko...
Checking files for ko: 100%|██████████████████████████████████████████████████| 95/95 [00:01<00:00, 65.47file/s]
Retrying vsc-extension-quickstart.md for ko:   0%|                                     | 0/17 [00:00<?, ?file/s] 
```

Diese Option prüft auf Übersetzungsfehler. Aktuell wird eine Datei als fehlerhaft markiert, wenn der Unterschied bei Zeilenumbrüchen zwischen Original und Übersetzung mehr als sechs beträgt. Ich plane, dieses Kriterium zukünftig flexibler zu gestalten.

Diese Methode ist z.B. nützlich, um fehlende Abschnitte oder beschädigte Übersetzungen zu erkennen, und startet für diese Dateien automatisch die erneute Übersetzung.

Wenn du jedoch bereits weißt, welche Dateien problematisch sind, ist es effizienter, diese manuell zu löschen und dann die Option `-a` option to re-translate them.

### 8. Debug Mode

To enable detailed logging for troubleshooting, use the `-d` zu verwenden:

```bash
translate -l "ko" -d
```

Dieser Befehl führt die Übersetzung im Debug-Modus aus und liefert zusätzliche Protokollinformationen, die bei der Fehlersuche helfen.

#### Beispiel im Phi-3 CookBook

Im **Phi-3 CookBook** bin ich auf ein Problem gestoßen, bei dem Übersetzungen mit vielen Links in Markdown-Dateien Formatierungsfehler verursachten, wie z. B. fehlerhafte Übersetzungen und ignorierte Zeilenumbrüche. Um das Problem zu analysieren, habe ich die Option `-d` genutzt, um den Übersetzungsprozess genauer zu beobachten.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "ko" -d
DEBUG:openai._base_client:Request options: {'method': 'post', 'url': '/chat/completions', 'headers': {'api-key': 'af04e0bea45747d8a7b8c131c1971044'}, 'files': None, 'json_data': {'messages': [{'role': 'user', 'content': "Translate the following text to ko. NEVER ADD ANY EXTRA CONTENT OUTSIDE THE TRANSLATION. TRANSLATE ONLY WHAT IS GIVEN TO YOU.. MAINTAIN MARKDOWN FORMAT\n\n# Phi-3 Cookbook: Hands-On Examples with Microsoft's Phi-3 Models [![Open and use the samples in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phi-3cookbook) [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%
...
```

### 9. Alle Sprachen übersetzen

Wenn du das Projekt in alle unterstützten Sprachen übersetzen möchtest, verwende das Schlüsselwort all.

> [!WARNING]
> Die Übersetzung aller Sprachen auf einmal kann je nach Projektgröße sehr viel Zeit in Anspruch nehmen. Zum Beispiel hat die Übersetzung des **Phi-3 CookBook** ins Spanische etwa 2 Stunden gedauert. Angesichts des Umfangs ist es nicht praktikabel, dass eine Person 20 Sprachen alleine bearbeitet. Es empfiehlt sich, die Arbeit auf mehrere Mitwirkende aufzuteilen, die jeweils ein oder zwei Sprachen betreuen und die Übersetzungen schrittweise aktualisieren.

```bash
translate -l "all"
```

Dieser Befehl übersetzt das Projekt in alle verfügbaren Sprachen. Wenn du fortfährst, kann die Übersetzung je nach Größe des Projekts viel Zeit benötigen.

> [!TIP]
>
> ### Manuelles Löschen übersetzter Dateien (optional)
> Übersetzte Dateien werden jetzt automatisch erkannt und bereinigt, wenn eine Quelldatei aktualisiert wird.
>
> Möchtest du jedoch eine Übersetzung manuell aktualisieren – zum Beispiel eine bestimmte Datei neu machen oder das Systemverhalten überschreiben – kannst du den folgenden Befehl verwenden, um alle Versionen der Datei in den Sprachordnern zu löschen.
>
> ### Unter Windows:
> 1. **Mit der Eingabeaufforderung**:
>    - Öffne die Eingabeaufforderung.
>    - Navigiere mit dem `cd`-Befehl in den Ordner, in dem sich die Dateien befinden.
>    - Verwende den folgenden Befehl, um Dateien zu löschen:
>      ```
>      del /s *filename*
>      ```
>      Die Option `/s` durchsucht auch Unterverzeichnisse.
>
> 2. **Mit PowerShell**:
>    - Öffne PowerShell.
>    - Führe diesen Befehl aus:
>      ```powershell
>      Get-ChildItem -Path "C:\YourPath" -Filter "*filename*" -Recurse | Remove-Item -Force
>      ```
>      Ersetze `"C:\YourPath"` durch den Pfad zu deinem Ordner.
>
> 3. **Mit `cd` und `find`**:
>    ```bash
>     find . -type f -name "*filename*" -delete
>     ```
>
> 4. **Zum Aktualisieren der neuesten Dateiänderungen**:
>    Verwende den Befehl `filename` with the specific name.
>
> Always double-check the files before deleting to avoid accidental loss. 
>
> Once you have deleted the files which need to be replace simply rerun your `translate -l`.

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die durch die Verwendung dieser Übersetzung entstehen.