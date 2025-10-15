<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a6cddf5e9648ef0bba0de7eb07e74cf1",
  "translation_date": "2025-10-15T02:12:43+00:00",
  "source_file": "getting_started/command-reference.md",
  "language_code": "de"
}
-->
# Befehlsreferenz

Die **Co-op Translator** CLI bietet verschiedene Optionen, um den Übersetzungsprozess anzupassen:

Befehl                                        | Beschreibung
----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"                 | Übersetzt Ihr Projekt in die angegebenen Sprachen. Beispiel: translate -l "es fr de" übersetzt ins Spanische, Französische und Deutsche. Mit translate -l "all" wird in alle unterstützten Sprachen übersetzt.
translate -l "language_codes" -u              | Aktualisiert Übersetzungen, indem bestehende gelöscht und neu erstellt werden. Achtung: Dadurch werden alle aktuellen Übersetzungen für die angegebenen Sprachen gelöscht.
translate -l "language_codes" -img            | Übersetzt nur Bilddateien.
translate -l "language_codes" -md             | Übersetzt nur Markdown-Dateien.
translate -l "language_codes" -nb             | Übersetzt nur Jupyter Notebook-Dateien (.ipynb).
translate -l "language_codes" --fix           | Übersetzt Dateien mit niedrigen Vertrauenswerten basierend auf vorherigen Bewertungsergebnissen erneut.
translate -l "language_codes" -d              | Aktiviert den Debug-Modus für detaillierte Protokollierung.
translate -l "language_codes" --save-logs, -s | Speichert DEBUG-Protokolle als Dateien unter <root_dir>/logs/ (Konsolenausgabe bleibt durch -d gesteuert)
translate -l "language_codes" -r "root_dir"   | Gibt das Stammverzeichnis des Projekts an
translate -l "language_codes" -f              | Nutzt den Schnellmodus für Bildübersetzungen (bis zu 3x schnelleres Plotten bei leichtem Qualitäts- und Ausrichtungsverlust).
translate -l "language_codes" -y              | Bestätigt alle Abfragen automatisch (nützlich für CI/CD-Pipelines)
translate -l "language_codes" --help          | Hilfe-Details innerhalb der CLI mit verfügbaren Befehlen
evaluate -l "language_code"                  | Bewertet die Übersetzungsqualität für eine bestimmte Sprache und gibt Vertrauenswertungen aus
evaluate -l "language_code" -c 0.8           | Bewertet Übersetzungen mit individuellem Vertrauensschwellenwert
evaluate -l "language_code" -f               | Schneller Bewertungsmodus (nur regelbasiert, kein LLM)
evaluate -l "language_code" -D               | Tiefer Bewertungsmodus (nur LLM-basiert, gründlicher aber langsamer)
evaluate -l "language_code" --save-logs, -s  | Speichert DEBUG-Protokolle als Dateien unter <root_dir>/logs/
migrate-links -l "language_codes"             | Überarbeitet übersetzte Markdown-Dateien, um Links zu Notebooks (.ipynb) zu aktualisieren. Bevorzugt übersetzte Notebooks, wenn verfügbar; andernfalls kann auf die Originale zurückgegriffen werden.
migrate-links -l "language_codes" -r          | Gibt das Projekt-Stammverzeichnis an (Standard: aktuelles Verzeichnis).
migrate-links -l "language_codes" --dry-run   | Zeigt an, welche Dateien geändert würden, ohne Änderungen zu speichern.
migrate-links -l "language_codes" --no-fallback-to-original | Links zu Original-Notebooks werden nicht umgeschrieben, wenn übersetzte Versionen fehlen (nur aktualisieren, wenn Übersetzung existiert).
migrate-links -l "language_codes" -d          | Aktiviert den Debug-Modus für detaillierte Protokollierung.
migrate-links -l "language_codes" --save-logs, -s | Speichert DEBUG-Protokolle als Dateien unter <root_dir>/logs/
migrate-links -l "all" -y                      | Verarbeitet alle Sprachen und bestätigt die Warnmeldung automatisch.

## Anwendungsbeispiele

  1. Standardverhalten (neue Übersetzungen hinzufügen, ohne bestehende zu löschen):   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. Nur neue koreanische Bildübersetzungen hinzufügen (bestehende Übersetzungen bleiben erhalten):    translate -l "ko" -img

  3. Alle koreanischen Übersetzungen aktualisieren (Achtung: Löscht alle bestehenden koreanischen Übersetzungen vor der Neuübersetzung):    translate -l "ko" -u

  4. Nur koreanische Bilder aktualisieren (Achtung: Löscht alle bestehenden koreanischen Bilder vor der Neuübersetzung):    translate -l "ko" -img -u

  5. Neue Markdown-Übersetzungen für Koreanisch hinzufügen, ohne andere Übersetzungen zu beeinflussen:    translate -l "ko" -md

  6. Übersetzungen mit niedrigem Vertrauenswert basierend auf vorherigen Bewertungen korrigieren: translate -l "ko" --fix

  7. Übersetzungen mit niedrigem Vertrauenswert nur für bestimmte Dateien (Markdown) korrigieren: translate -l "ko" --fix -md

  8. Übersetzungen mit niedrigem Vertrauenswert nur für bestimmte Dateien (Bilder) korrigieren: translate -l "ko" --fix -img

  9. Schnellmodus für Bildübersetzungen verwenden:    translate -l "ko" -img -f

  10. Übersetzungen mit niedrigem Vertrauenswert und individuellem Schwellenwert korrigieren: translate -l "ko" --fix -c 0.8

  11. Beispiel für Debug-Modus: - translate -l "ko" -d: Aktiviert Debug-Protokollierung.
  12. Protokolle in Dateien speichern: translate -l "ko" -s
  13. DEBUG in Konsole und Datei: translate -l "ko" -d -s

  14. Notebook-Links für koreanische Übersetzungen migrieren (Links zu übersetzten Notebooks aktualisieren, wenn verfügbar):    migrate-links -l "ko"

  15. Links migrieren mit Dry-Run (keine Dateischreibungen):    migrate-links -l "ko" --dry-run

  16. Links nur aktualisieren, wenn übersetzte Notebooks existieren (kein Rückgriff auf Originale):    migrate-links -l "ko" --no-fallback-to-original

  17. Alle Sprachen mit Bestätigungsabfrage verarbeiten:    migrate-links -l "all"

  18. Alle Sprachen automatisch bestätigen und verarbeiten:    migrate-links -l "all" -y
  19. Protokolle für migrate-links in Dateien speichern:    migrate-links -l "ko ja" -s

### Bewertungsbeispiele

> [!WARNING]  
> **Beta-Funktion**: Die Bewertungsfunktion befindet sich derzeit in der Beta-Phase. Diese Funktion wurde eingeführt, um übersetzte Dokumente zu bewerten. Die Bewertungsmethoden und die genaue Umsetzung werden noch entwickelt und können sich ändern.

  1. Koreanische Übersetzungen bewerten: evaluate -l "ko"

  2. Bewertung mit individuellem Vertrauensschwellenwert: evaluate -l "ko" -c 0.8

  3. Schnelle Bewertung (nur regelbasiert): evaluate -l "ko" -f

  4. Tiefe Bewertung (nur LLM-basiert): evaluate -l "ko" -D

---

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ausgangssprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.