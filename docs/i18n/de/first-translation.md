# Übersetzen, bearbeiten und prüfen eines kleinen Projekts

Beginnen Sie mit zwei kurzen Markdown-Dateien und einer Zielsprache. Sie sehen, wo Übersetzungen geschrieben werden, was passiert, wenn die Quelle sich ändert, und wie Sie das Ergebnis überprüfen.

## Aufgezeichnete Ergebnisse

Das Beispiel wurde am 19. September 2026 mit Co-op Translator 0.21.0 und Azure OpenAI (`gpt-5-mini`) ausgeführt. Die unveränderten CLI-Befehle wurden über Clicks `CliRunner` aufgerufen, wobei das erstellte Wheel und die vorhandenen Python-Abhängigkeiten verwendet wurden.

| Schritt | Ergebnis |
| --- | --- |
| Vorschau | Exit 0; keine Modellübersetzung angefordert |
| Initial translation | Exit 0; 27.36 seconds |
| Erste Überprüfung | Exit 0 |
| README bearbeiten und prüfen | Exit 1; veraltete Übersetzung erkannt |
| Übersetzung aktualisieren | Exit 0; 22.17 seconds |
| Überprüfung nach Update | Exit 0; keine Fehler oder Warnungen |
| Unveränderter Leitfaden | Identische Bytes vor und nach README-Aktualisierung |
| Erneut ausführen | Exit 0; identische Hashes für alle Übersetzungsdateien |

Dies sind Messungen einzelner Durchläufe, keine Leistungsversprechen. Die Einrichtungszeit ist ausgeschlossen; die Abrechnung durch den Anbieter wurde nicht gemessen. Ein unveränderter Durchlauf kann dennoch eine Anbieter-Gesundheitsprüfung durchführen.

Untersuchen Sie die [erste Übersetzung](../../assets/demo/before.txt), [aktualisierte Übersetzung](../../assets/demo/after.txt), [vollständigen Übersetzungsdiff](../../assets/demo/update.diff), [veraltete Überprüfung](../../assets/demo/review-stale.txt), [abschließende Überprüfung](../../assets/demo/review-after.txt) und die [Ausführungsdetails](../../assets/demo/results.json). Die Übersetzung der gesamten Datei kann andere Formulierungen verändern, wie der erfasste Diff zeigt. Beide Textartefakte behalten den generierten Haftungsausschluss.

Menschliche Überprüfung bleibt wichtig: die erfasste Aktualisierung verwendet `[사용 가이드](guide.md)을`; das koreanische Partikel sollte `[사용 가이드](guide.md)를` sein. Die Textartefakte belassen diese Ausgabe unverändert, statt eine vom Modell bearbeitete Übersetzung zu präsentieren. Die strukturelle Überprüfung besteht trotz dieses Formulierungsproblems.

## 1. Einen kleinen Ordner vorbereiten

Verwenden Sie Python 3.11–3.14 und das [Einrichten einer virtuellen Umgebung](configuration.md#local-runtime-setup). Installieren Sie die für dieses Beispiel verwendete Version:

```bash
python -m pip install co-op-translator==0.21.0
mkdir translation-demo
cd translation-demo
git init
```

Laden Sie [README.txt](../../assets/demo/README.txt) und [guide.txt](../../assets/demo/guide.txt) in diesen Ordner herunter und speichern Sie sie als `README.md` und `guide.md`. Es sind kleine fiktive Projektdokumente; keine Anwendungsinstallation ist erforderlich.

Das README enthält einen Codeblock und einen Link zu `guide.md`. Sein letzter Satz lautet:

```text
Notes are saved locally.
```

Behalten Sie nur diese beiden Quelldokumente in diesem Ordner. Alle folgenden Befehle werden innerhalb von `translation-demo` ausgeführt und funktionieren in Bash und PowerShell.

## 2. Vorschau ohne Anmeldeinformationen

```bash
translate -l "ko" -md --dry-run
```

Die Vorschau schätzt die Übersetzungsarbeit, ohne ein Modell aufzurufen oder Übersetzungen zu schreiben. Token-Schätzungen sind kein Abrechnungsangebot. Der erste Lauf sollte beide Markdown-Dateien als neue Arbeit identifizieren.

## 3. Anbieter wählen und übersetzen

Konfigurieren Sie einen Anbieter mit dem [Konfigurationsleitfaden](configuration.md): Azure OpenAI, OpenAI oder Anthropic. Textübersetzungen mit OpenAI und Anthropic erfordern kein Azure-Konto. Bilddienste sind für dieses Beispiel nicht erforderlich.

Wenn Sie eine lokale `.env`-Datei verwenden, fügen Sie `.env` zur `.gitignore` dieses Ordners hinzu. Übersetzungsaufrufe verwenden Ihr Anbieter-Konto und können Kosten verursachen.

```bash
translate -l "ko" -md
co-op-review -l "ko"
```

Öffnen Sie `translations/ko/README.md` und `translations/ko/guide.md`. Überprüfen Sie die koreanische Wortwahl, den Codeblock und den Link vom übersetzten README zum übersetzten Guide. Die Wortwahl der Ausgabe variiert je nach Modell.

`co-op-review` überprüft Aktualität, Struktur und lokale Links. Ein bestandenes Ergebnis bestätigt nicht die sprachliche Genauigkeit. Beheben Sie alle gemeldeten Fehler, bevor Sie fortfahren.

Dokumentieren Sie die erfolgreiche Basisversion mit Git (konfigurieren Sie bei Bedarf zuerst Ihre Git-Identität):

```bash
git add README.md guide.md translations
git commit -m "Record initial Korean translation"
```

## 4. Die Quelle ändern

Ersetzen Sie in `README.md` `Notes are saved locally.` durch:

```text
Notes are saved locally as Markdown files.
```

Lassen Sie `guide.md` unverändert. Führen Sie dann aus:

```bash
co-op-review -l "ko"
translate -l "ko" -md --dry-run
```

Die Überprüfung sollte melden, dass die README-Übersetzung veraltet ist und mit einem Fehler beendet werden. Dies ist der erwartete Zwischenzustand. Die Vorschau sollte Arbeit für das geänderte README identifizieren.

## 5. Aktualisieren und den Diff überprüfen

```bash
translate -l "ko" -md
git diff -- README.md translations/ko/README.md
git diff -- translations/ko/guide.md
co-op-review -l "ko"
```

Untersuchen Sie den echten Diff: Die Standard-CLI übersetzt die geänderte Datei erneut, sodass das Modell auch andere Formulierungen in dieser Datei überarbeiten kann. Der unveränderte Leitfaden sollte keinen Diff aufweisen. Die Überprüfung sollte README nicht mehr als veraltet melden; untersuchen Sie stattdessen alle anderen Befunde, anstatt sie zu ignorieren.

Die blockweise Erhaltung menschlicher Markdown-Änderungen erfordert einen optionalen Übersetzungszustandsanbieter in der [Python API](api.md). Dieser ist durch diese CLI-Befehle nicht aktiviert.

## 6. Erneut ausführen ohne Änderungen

Committen Sie die aktualisierte Quelle und Übersetzung:

```bash
git add README.md translations
git commit -m "Update Korean translation after source edit"
translate -l "ko" -md
git diff --exit-code -- translations
```

Mit aktuellen Übersetzungen und unveränderter Konfiguration überspringt der Übersetzer die Dateien. Der letzte Git-Befehl sollte keinen Diff erzeugen und erfolgreich beenden.

## Nächste Schritte

- [Nur ein README übersetzen und einen Pull Request öffnen](github-actions.md#your-first-readme-translation-pr).
- [CLI, Python-API oder MCP wählen](workflows.md).
- [Ein Übersetzungsproblem melden ohne zu programmieren](https://github.com/Azure/co-op-translator/issues/new?template=translation_feedback.yml).