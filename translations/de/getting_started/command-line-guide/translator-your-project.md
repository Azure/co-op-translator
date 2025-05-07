<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d238206c3503631e32774716d11d1868",
  "translation_date": "2025-05-07T14:07:08+00:00",
  "source_file": "getting_started/command-line-guide/translator-your-project.md",
  "language_code": "de"
}
-->
# Übersetze dein Projekt mit Co-op Translator

Der **Co-op Translator** ist ein Kommandozeilen-Tool (CLI), das dir dabei hilft, Markdown- und Bilddateien in deinem Projekt in mehrere Sprachen zu übersetzen. Dieser Abschnitt erklärt, wie du das Tool benutzt, stellt die verschiedenen CLI-Optionen vor und gibt Beispiele für unterschiedliche Anwendungsfälle.

> [!NOTE]
> Für eine vollständige Liste der Befehle und deren ausführliche Beschreibung, siehe die [Command reference](./command-reference.md).

---

## Beispiel-Szenarien und Befehle

Hier sind einige gängige Anwendungsfälle für den **Co-op Translator** zusammen mit den passenden Befehlen.

### 1. Grundlegende Übersetzung (eine Sprache)

Um dein gesamtes Projekt (Markdown-Dateien und Bilder) in eine einzelne Sprache, wie Koreanisch, zu übersetzen, verwende folgenden Befehl:

```bash
translate -l "ko"
```

Dieser Befehl übersetzt alle Markdown- und Bilddateien ins Koreanische und fügt neue Übersetzungen hinzu, ohne bestehende zu löschen.

> [!TIP]
>
> Möchtest du wissen, welche Sprachcodes im **Co-op Translator** verfügbar sind? Sieh dir den Abschnitt [Supported Languages](https://github.com/Azure/co-op-translator#supported-languages) im Repository an.

#### Beispiel im Phi-3 CookBook

Im **Phi-3 CookBook** habe ich folgende Methode verwendet, um die koreanische Übersetzung für die vorhandenen Markdown-Dateien und Bilder hinzuzufügen.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko"
Translating images: 100%|███████████████████████████████████████████████████| 276/276 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 153/153 [1:43:07<00:00, 241.31s/it]
```

### 2. Übersetzung in mehrere Sprachen

Um dein Projekt in mehrere Sprachen (z. B. Spanisch, Französisch und Deutsch) zu übersetzen, benutze diesen Befehl:

```bash
translate -l "es fr de"
```

Dieser Befehl übersetzt das Projekt in Spanisch, Französisch und Deutsch und fügt neue Übersetzungen hinzu, ohne bestehende zu überschreiben.

#### Beispiel im Phi-3 CookBook

Im **Phi-3 CookBook** habe ich nach dem Abrufen der neuesten Änderungen folgende Methode verwendet, um neu hinzugefügte Markdown-Dateien und Bilder zu übersetzen.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko ja zh tw es fr" -a
Translating images: 100%|███████████████████████████████████████████████████| 273/273 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 6/6 [24:07<00:00, 241.31s/it]
```

> [!NOTE]
> Obwohl es generell empfohlen wird, jeweils nur eine Sprache zu übersetzen, kann es in Situationen wie dieser, in denen bestimmte Änderungen hinzugefügt werden müssen, effizient sein, mehrere Sprachen gleichzeitig zu übersetzen.

### 3. Übersetzungen aktualisieren (löscht bestehende Übersetzungen)

Um bestehende Übersetzungen zu aktualisieren (also die aktuellen Übersetzungen zu löschen und durch neue zu ersetzen), verwende die Option `-u`. Dadurch werden alle vorhandenen Übersetzungen für die angegebenen Sprachen gelöscht und neu übersetzt.

```bash
translate -l "ko" -u
```

Warnung: Dieser Befehl fordert dich zur Bestätigung auf, bevor die bestehenden Übersetzungen gelöscht werden.

#### Beispiel im Phi-3 CookBook

Im **Phi-3 CookBook** habe ich folgende Methode genutzt, um alle spanisch übersetzten Dateien zu aktualisieren. Ich empfehle diese Methode, wenn es umfangreiche Änderungen am Originalinhalt über mehrere Markdown-Dokumente gibt. Sind nur wenige übersetzte Markdown-Dateien zu aktualisieren, ist es effizienter, diese gezielt manuell zu löschen und anschließend die Methode `-a` zum Hinzufügen der aktualisierten Übersetzungen zu verwenden.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "es" -u
Warning: The update command will delete all existing translations for 'es' and re-translate everything.
Do you want to continue? Type 'yes' to proceed: yes
Proceeding with update...
Translating images: 100%|████████████████████████████████████████████| 150/150 [43:46<00:00, 15.55s/it]
Translating markdown files: 100%|███████████████████████████████████| 95/95 [1:40:27<00:00, 125.62s/it]
```

### 5. Nur Bilder übersetzen

Um nur die Bilddateien in deinem Projekt zu übersetzen, verwende die Option `-img`:

```bash
translate -l "ko" -img
```

Dieser Befehl übersetzt nur die Bilder ins Koreanische, ohne die Markdown-Dateien zu verändern.

### 6. Nur Markdown-Dateien übersetzen

Um ausschließlich die Markdown-Dateien in deinem Projekt zu übersetzen, nutze die Option `-md`:

```bash
translate -l "ko" -md
```

### 7. Nach Fehlern in übersetzten Dateien suchen

Wenn du übersetzte Dateien auf Fehler überprüfen und bei Bedarf die Übersetzung erneut versuchen möchtest, verwende die Option `-chk`:

```bash
translate -l "ko" -chk
```

Dieser Befehl durchsucht die übersetzten Markdown-Dateien und versucht, fehlerhafte Dateien erneut zu übersetzen.

#### Beispiel im Phi-3 CookBook

Im **Phi-3 CookBook** habe ich folgende Methode verwendet, um Übersetzungsfehler in den koreanischen Dateien zu prüfen und automatisch eine erneute Übersetzung für Dateien mit erkannten Problemen auszulösen.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko" -chk 
Checking translated files for errors in ko...
Checking files for ko: 100%|██████████████████████████████████████████████████| 95/95 [00:01<00:00, 65.47file/s]
Retrying vsc-extension-quickstart.md for ko:   0%|                                     | 0/17 [00:00<?, ?file/s] 
```

Diese Option prüft auf Übersetzungsfehler. Aktuell wird eine Datei als fehlerhaft markiert, wenn der Unterschied bei Zeilenumbrüchen zwischen Original- und Übersetzungsdatei mehr als sechs beträgt. Ich plane, dieses Kriterium zukünftig flexibler zu gestalten.

Diese Methode ist beispielsweise nützlich, um fehlende Textabschnitte oder beschädigte Übersetzungen zu erkennen und für diese Dateien automatisch eine erneute Übersetzung zu veranlassen.

Falls du jedoch bereits weißt, welche Dateien problematisch sind, ist es effizienter, diese Dateien manuell zu löschen und die Option `-a` option to re-translate them.

### 8. Debug Mode

To enable detailed logging for troubleshooting, use the `-d` zu verwenden:

```bash
translate -l "ko" -d
```

Dieser Befehl führt die Übersetzung im Debug-Modus aus und liefert zusätzliche Protokollinformationen, die bei der Fehlersuche helfen können.

#### Beispiel im Phi-3 CookBook

Im **Phi-3 CookBook** trat ein Problem auf, bei dem Übersetzungen mit vielen Links in Markdown-Dateien Formatierungsfehler verursachten, wie z. B. fehlerhafte Übersetzungen und ignorierte Zeilenumbrüche. Um das Problem zu diagnostizieren, habe ich die Option `-d` verwendet, um zu sehen, wie der Übersetzungsprozess abläuft.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "ko" -d
DEBUG:openai._base_client:Request options: {'method': 'post', 'url': '/chat/completions', 'headers': {'api-key': 'af04e0bea45747d8a7b8c131c1971044'}, 'files': None, 'json_data': {'messages': [{'role': 'user', 'content': "Translate the following text to ko. NEVER ADD ANY EXTRA CONTENT OUTSIDE THE TRANSLATION. TRANSLATE ONLY WHAT IS GIVEN TO YOU.. MAINTAIN MARKDOWN FORMAT\n\n# Phi-3 Cookbook: Hands-On Examples with Microsoft's Phi-3 Models [![Open and use the samples in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phi-3cookbook) [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%
...
```

### 9. Alle Sprachen übersetzen

Wenn du das Projekt in alle unterstützten Sprachen übersetzen möchtest, benutze das Schlüsselwort all.

> [!WARNING]
> Die gleichzeitige Übersetzung aller Sprachen kann je nach Projektgröße viel Zeit in Anspruch nehmen. Zum Beispiel dauerte die Übersetzung des **Phi-3 CookBook** ins Spanische etwa 2 Stunden. Angesichts des Umfangs ist es für eine einzelne Person nicht praktikabel, 20 Sprachen zu bearbeiten. Es wird empfohlen, die Arbeit auf mehrere Mitwirkende aufzuteilen, die jeweils ein oder zwei Sprachen verwalten und die Übersetzungen schrittweise aktualisieren.

```bash
translate -l "all"
```

Dieser Befehl übersetzt das Projekt in alle verfügbaren Sprachen. Wenn du fortfährst, kann die Übersetzung je nach Projektgröße erheblich Zeit in Anspruch nehmen.

> [!TIP]
>
> ### Manuelles Löschen übersetzter Dateien (optional)
> Übersetzte Dateien werden jetzt automatisch erkannt und bereinigt, wenn eine Quelldatei aktualisiert wird.
>
> Möchtest du jedoch eine Übersetzung manuell aktualisieren – zum Beispiel eine bestimmte Datei neu übersetzen oder das Systemverhalten überschreiben – kannst du den folgenden Befehl verwenden, um alle Versionen der Datei in den Sprachordnern zu löschen.
>
> ### Unter Windows:
> 1. **Mit der Eingabeaufforderung**:
>    - Öffne die Eingabeaufforderung.
>    - Navigiere mit dem `cd`-Befehl in den Ordner, in dem sich die Dateien befinden.
>    - Verwende folgenden Befehl zum Löschen der Dateien:
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
>      Ersetze `"C:\YourPath"` entsprechend.
>
>    - Der Befehl `cd` zusammen mit `find` sucht nach Dateien mit dem Namen `filename`:
>      ```bash
>     find . -type f -name "*filename*" -delete
>     ```
>    - Ersetze `filename` entsprechend.
>
>    - Verwende den Befehl `translate -l`, um die neuesten Dateiänderungen zu aktualisieren.

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir auf Genauigkeit achten, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Originalsprache ist als maßgebliche Quelle zu betrachten. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.