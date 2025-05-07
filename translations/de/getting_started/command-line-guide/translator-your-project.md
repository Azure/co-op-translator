<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "33db54f4f3ca9f0321be05374b591f2b",
  "translation_date": "2025-05-06T17:59:52+00:00",
  "source_file": "getting_started/command-line-guide/translator-your-project.md",
  "language_code": "de"
}
-->
# Übersetze dein Projekt mit Co-op Translator

Der **Co-op Translator** ist ein Kommandozeilen-Tool (CLI), das dir dabei hilft, Markdown- und Bilddateien in deinem Projekt in mehrere Sprachen zu übersetzen. In diesem Abschnitt wird erklärt, wie du das Tool benutzt, welche CLI-Optionen es gibt und es werden Beispiele für verschiedene Anwendungsfälle gezeigt.

> [!NOTE]
> Für eine vollständige Liste der Befehle und deren ausführliche Beschreibung siehe die [Command reference](./command-reference.md).

---

## Beispiel-Szenarien und Befehle

Hier sind einige häufige Anwendungsfälle für den **Co-op Translator** mit den passenden Befehlen.

### 1. Grundübersetzung (eine Sprache)

Um dein gesamtes Projekt (Markdown-Dateien und Bilder) in eine einzelne Sprache wie Koreanisch zu übersetzen, verwende folgenden Befehl:

```bash
translate -l "ko"
```

Dieser Befehl übersetzt alle Markdown- und Bilddateien ins Koreanische, ohne bestehende Übersetzungen zu löschen, sondern ergänzt sie.

> [!TIP]
>
> Möchtest du wissen, welche Sprachcodes im **Co-op Translator** verfügbar sind? Sieh dir den Abschnitt [Supported Languages](https://github.com/Azure/co-op-translator#supported-languages) im Repository an.

#### Beispiel im Phi-3 CookBook

Im **Phi-3 CookBook** habe ich die folgende Methode verwendet, um die koreanische Übersetzung für bestehende Markdown-Dateien und Bilder hinzuzufügen.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko"
Translating images: 100%|███████████████████████████████████████████████████| 276/276 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 153/153 [1:43:07<00:00, 241.31s/it]
```

### 2. Übersetzung in mehrere Sprachen

Um dein Projekt in mehrere Sprachen (z.B. Spanisch, Französisch und Deutsch) zu übersetzen, verwende diesen Befehl:

```bash
translate -l "es fr de"
```

Dieser Befehl übersetzt das Projekt in Spanisch, Französisch und Deutsch, ohne bestehende Übersetzungen zu überschreiben, sondern ergänzt sie.

#### Beispiel im Phi-3 CookBook

Im **Phi-3 CookBook** habe ich nach dem Aktualisieren auf die neuesten Änderungen die folgende Methode genutzt, um neu hinzugefügte Markdown-Dateien und Bilder zu übersetzen.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko ja zh tw es fr" -a
Translating images: 100%|███████████████████████████████████████████████████| 273/273 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 6/6 [24:07<00:00, 241.31s/it]
```

> [!NOTE]
> Obwohl es generell empfohlen wird, jeweils eine Sprache zu übersetzen, kann es in Fällen wie diesem, wo bestimmte Änderungen ergänzt werden müssen, effizienter sein, mehrere Sprachen gleichzeitig zu übersetzen.

### 3. Angabe des Stammverzeichnisses

Standardmäßig verwendet der Translator das aktuelle Arbeitsverzeichnis. Wenn sich dein Projekt woanders befindet, gib das Stammverzeichnis mit der Option -r an:

```bash
translate -l "es fr de" -r "./my_project"
```

Dieser Befehl übersetzt die Dateien in `./my_project` into Spanish, French, and German.

### 4. Updating Translations (Deletes Existing Translations)

To update existing translations (i.e., delete the current translations and replace them with new ones), use the `-u` Option. Dadurch werden alle bestehenden Übersetzungen für die angegebenen Sprachen gelöscht und neu übersetzt.

```bash
translate -l "ko" -u
```

Warnung: Dieser Befehl fragt vor dem Löschen der bestehenden Übersetzungen nach einer Bestätigung.

#### Beispiel im Phi-3 CookBook

Im **Phi-3 CookBook** habe ich die folgende Methode genutzt, um alle spanischen Übersetzungen zu aktualisieren. Ich empfehle diese Methode, wenn es größere Änderungen im Originaltext über mehrere Markdown-Dateien hinweg gibt. Bei nur wenigen zu aktualisierenden Übersetzungen ist es effizienter, die entsprechenden Dateien manuell zu löschen und dann die `-a` Methode zu verwenden, um die aktualisierten Übersetzungen hinzuzufügen.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "es" -u
Warning: The update command will delete all existing translations for 'es' and re-translate everything.
Do you want to continue? Type 'yes' to proceed: yes
Proceeding with update...
Translating images: 100%|████████████████████████████████████████████| 150/150 [43:46<00:00, 15.55s/it]
Translating markdown files: 100%|███████████████████████████████████| 95/95 [1:40:27<00:00, 125.62s/it]
```

### 6. Nur Bilder übersetzen

Um nur die Bilddateien in deinem Projekt zu übersetzen, benutze die Option `-img`:

```bash
translate -l "ko" -img
```

Dieser Befehl übersetzt nur die Bilder ins Koreanische, ohne die Markdown-Dateien zu beeinflussen.

### 7. Nur Markdown-Dateien übersetzen

Um nur die Markdown-Dateien in deinem Projekt zu übersetzen, benutze die Option `-md`:

```bash
translate -l "ko" -md
```

### 8. Überprüfung auf Fehler in übersetzten Dateien

Wenn du übersetzte Dateien auf Fehler prüfen und bei Bedarf die Übersetzung wiederholen möchtest, benutze die Option `-chk`:

```bash
translate -l "ko" -chk
```

Dieser Befehl durchsucht die übersetzten Markdown-Dateien und versucht bei fehlerhaften Dateien die Übersetzung erneut.

#### Beispiel im Phi-3 CookBook

Im **Phi-3 CookBook** habe ich die folgende Methode verwendet, um die koreanischen Dateien auf Übersetzungsfehler zu prüfen und fehlerhafte Dateien automatisch erneut zu übersetzen.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko" -chk 
Checking translated files for errors in ko...
Checking files for ko: 100%|██████████████████████████████████████████████████| 95/95 [00:01<00:00, 65.47file/s]
Retrying vsc-extension-quickstart.md for ko:   0%|                                     | 0/17 [00:00<?, ?file/s] 
```

Diese Option überprüft auf Übersetzungsfehler. Derzeit wird eine Datei als fehlerhaft markiert, wenn die Anzahl der Zeilenumbrüche zwischen Original und Übersetzung um mehr als sechs abweicht. Ich plane, dieses Kriterium künftig flexibler zu gestalten.

Diese Methode ist zum Beispiel nützlich, um fehlende Abschnitte oder beschädigte Übersetzungen zu erkennen, und übersetzt diese Dateien automatisch neu.

Wenn du jedoch bereits weißt, welche Dateien Probleme bereiten, ist es effizienter, diese Dateien manuell zu löschen und dann die `-a` option to re-translate them.

### 9. Debug Mode

To enable detailed logging for troubleshooting, use the `-d` Option zu verwenden:

```bash
translate -l "ko" -d
```

Dieser Befehl führt die Übersetzung im Debug-Modus aus und liefert zusätzliche Protokollinformationen, die bei der Fehlersuche helfen können.

#### Beispiel im Phi-3 CookBook

Im **Phi-3 CookBook** hatte ich ein Problem, bei dem Übersetzungen mit vielen Links in Markdown-Dateien zu Formatierungsfehlern führten, wie z.B. kaputte Übersetzungen und ignorierte Zeilenumbrüche. Um das Problem zu diagnostizieren, habe ich die `-d` Option verwendet, um den Übersetzungsprozess genauer zu beobachten.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "ko" -d
DEBUG:openai._base_client:Request options: {'method': 'post', 'url': '/chat/completions', 'headers': {'api-key': 'af04e0bea45747d8a7b8c131c1971044'}, 'files': None, 'json_data': {'messages': [{'role': 'user', 'content': "Translate the following text to ko. NEVER ADD ANY EXTRA CONTENT OUTSIDE THE TRANSLATION. TRANSLATE ONLY WHAT IS GIVEN TO YOU.. MAINTAIN MARKDOWN FORMAT\n\n# Phi-3 Cookbook: Hands-On Examples with Microsoft's Phi-3 Models [![Open and use the samples in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phi-3cookbook) [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%
...
```

### 10. Übersetzung in alle Sprachen

Wenn du das Projekt in alle unterstützten Sprachen übersetzen möchtest, verwende das Schlüsselwort all.

> [!WARNING]
> Die Übersetzung aller Sprachen auf einmal kann je nach Projektgröße sehr viel Zeit in Anspruch nehmen. Zum Beispiel dauerte die Übersetzung des **Phi-3 CookBook** ins Spanische etwa 2 Stunden. Aufgrund des Umfangs ist es nicht praktikabel, dass eine Person 20 Sprachen alleine bearbeitet. Es wird empfohlen, die Arbeit auf mehrere Mitwirkende aufzuteilen, die jeweils eine oder zwei Sprachen betreuen und die Übersetzungen schrittweise aktualisieren.

```bash
translate -l "all"
```

Dieser Befehl übersetzt das Projekt in alle verfügbaren Sprachen. Je nach Projektgröße kann die Übersetzung sehr viel Zeit in Anspruch nehmen.

> [!TIP]
>
> ### Löschen von Dateien, die aktualisiert werden müssen  
> Um Dateien zu aktualisieren, die kürzlich in einem Pull Request geändert wurden, ist der erste Schritt, alle bestehenden Versionen der jeweiligen Datei in den verschiedenen Sprachübersetzungsordnern zu löschen. Das kannst du gesammelt mit folgendem Befehl tun, der alle Dateien mit einem bestimmten Namen in den Übersetzungsordnern entfernt.
>
> ### Unter Windows:
> 1. **Mit der Eingabeaufforderung**:
>    - Öffne die Eingabeaufforderung.
>    - Navigiere mit `cd` zu dem Ordner, in dem sich die Dateien befinden.
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
>      Ersetze `"C:\YourPath"` with the folder path and `filename` with the specific name.
>
> ### On macOS/Linux:
> 1. **Using Terminal**:
>   - Open Terminal.
>   - Navigate to the directory with `cd`.
>   - Use the `find` Befehl:
>     ```bash
>     find . -type f -name "*filename*" -delete
>     ```
>     Ersetze `filename` with the specific name.
>
> Always double-check the files before deleting to avoid accidental loss. 
>
> Once you have deleted the files which need to be replace simply rerun your `translate -l` Befehl, um die neuesten Änderungen der Dateien zu aktualisieren.

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir auf Genauigkeit achten, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die durch die Nutzung dieser Übersetzung entstehen.