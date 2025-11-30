<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "822238e4451d04bb152cebb1be6f13c2",
  "translation_date": "2025-11-30T09:49:46+00:00",
  "source_file": "getting_started/command-reference.md",
  "language_code": "de"
}
-->
# Befehlsreferenz

Die **Co-op Translator** CLI bietet verschiedene Optionen, um den Übersetzungsprozess anzupassen:

Befehl                                       | Beschreibung
----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"                 | Übersetzt dein Projekt in die angegebenen Sprachen. Beispiel: translate -l "es fr de" übersetzt ins Spanische, Französische und Deutsche. Verwende translate -l "all", um in alle unterstützten Sprachen zu übersetzen.
translate -l "language_codes" -u              | Aktualisiert Übersetzungen, indem bestehende gelöscht und neu erstellt werden. Achtung: Dies löscht alle aktuellen Übersetzungen für die angegebenen Sprachen.
translate -l "language_codes" -img            | Übersetzt nur Bilddateien.
translate -l "language_codes" -md             | Übersetzt nur Markdown-Dateien.
translate -l "language_codes" -nb             | Übersetzt nur Jupyter-Notebook-Dateien (.ipynb).
translate -l "language_codes" --fix           | Übersetzt Dateien mit niedrigen Vertrauenswerten basierend auf vorherigen Bewertungsergebnissen neu.
translate -l "language_codes" -d              | Aktiviert den Debug-Modus für detaillierte Protokollierung.
translate -l "language_codes" --save-logs, -s | Speichert DEBUG-Level-Protokolle in Dateien unter <root_dir>/logs/ (Konsole bleibt durch -d gesteuert)
translate -l "language_codes" -r "root_dir"   | Gibt das Stammverzeichnis des Projekts an
translate -l "language_codes" -f              | Verwendet den Schnellmodus für Bildübersetzungen (bis zu 3x schnelleres Plotten bei leichtem Qualitäts- und Ausrichtungsverlust).
translate -l "language_codes" -y              | Bestätigt alle Eingabeaufforderungen automatisch (praktisch für CI/CD-Pipelines)
translate -l "language_codes" --add-disclaimer/--no-disclaimer | Aktiviert oder deaktiviert das Hinzufügen eines Hinweises zur maschinellen Übersetzung in übersetzte Markdown-Dateien und Notebooks (Standard: aktiviert).
translate -l "language_codes" --help          | Zeigt Hilfedetails innerhalb der CLI mit verfügbaren Befehlen an
evaluate -l "language_code"                  | Bewertet die Übersetzungsqualität für eine bestimmte Sprache und liefert Vertrauenswerte
evaluate -l "language_code" -c 0.8           | Bewertet Übersetzungen mit einem benutzerdefinierten Vertrauensschwellenwert
evaluate -l "language_code" -f               | Schneller Bewertungsmodus (nur regelbasiert, kein LLM)
evaluate -l "language_code" -D               | Tiefer Bewertungsmodus (nur LLM-basiert, gründlicher aber langsamer)
evaluate -l "language_code" --save-logs, -s  | Speichert DEBUG-Level-Protokolle in Dateien unter <root_dir>/logs/
migrate-links -l "language_codes"             | Verarbeitet übersetzte Markdown-Dateien neu, um Links zu Notebooks (.ipynb) zu aktualisieren. Bevorzugt übersetzte Notebooks, falls vorhanden; andernfalls kann auf Original-Notebooks zurückgegriffen werden.
migrate-links -l "language_codes" -r          | Gibt das Projektstammverzeichnis an (Standard: aktuelles Verzeichnis).
migrate-links -l "language_codes" --dry-run   | Zeigt an, welche Dateien sich ändern würden, ohne Änderungen zu schreiben.
migrate-links -l "language_codes" --no-fallback-to-original | Schreibt Links zu Original-Notebooks nicht um, wenn übersetzte Gegenstücke fehlen (aktualisiert nur, wenn Übersetzung existiert).
migrate-links -l "language_codes" -d          | Aktiviert den Debug-Modus für detaillierte Protokollierung.
migrate-links -l "language_codes" --save-logs, -s | Speichert DEBUG-Level-Protokolle in Dateien unter <root_dir>/logs/
migrate-links -l "all" -y                      | Verarbeitet alle Sprachen und bestätigt Warnhinweise automatisch.

## Anwendungsbeispiele

  1. Standardverhalten (fügt neue Übersetzungen hinzu, ohne bestehende zu löschen):   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. Fügt nur neue koreanische Bildübersetzungen hinzu (bestehende Übersetzungen werden nicht gelöscht):    translate -l "ko" -img

  3. Aktualisiert alle koreanischen Übersetzungen (Achtung: Dies löscht alle bestehenden koreanischen Übersetzungen vor der Neuübersetzung):    translate -l "ko" -u

  4. Aktualisiert nur koreanische Bilder (Achtung: Dies löscht alle bestehenden koreanischen Bilder vor der Neuübersetzung):    translate -l "ko" -img -u

  5. Fügt neue Markdown-Übersetzungen für Koreanisch hinzu, ohne andere Übersetzungen zu beeinflussen:    translate -l "ko" -md

  6. Korrigiert Übersetzungen mit niedrigem Vertrauenswert basierend auf vorherigen Bewertungsergebnissen: translate -l "ko" --fix

  7. Korrigiert Übersetzungen mit niedrigem Vertrauenswert nur für bestimmte Dateien (Markdown): translate -l "ko" --fix -md

  8. Korrigiert Übersetzungen mit niedrigem Vertrauenswert nur für bestimmte Dateien (Bilder): translate -l "ko" --fix -img

  9. Verwendet den Schnellmodus für Bildübersetzungen:    translate -l "ko" -img -f

  10. Korrigiert Übersetzungen mit niedrigem Vertrauenswert mit benutzerdefiniertem Schwellenwert: translate -l "ko" --fix -c 0.8

  11. Beispiel für Debug-Modus: - translate -l "ko" -d: Aktiviert Debug-Protokollierung.
  12. Protokolle in Dateien speichern: translate -l "ko" -s
  13. DEBUG in Konsole und Datei: translate -l "ko" -d -s
  14. Übersetzen ohne maschinelle Übersetzungshinweise in den Ausgaben: translate -l "ko" --no-disclaimer

  15. Migriert Notebook-Links für koreanische Übersetzungen (aktualisiert Links zu übersetzten Notebooks, wenn verfügbar):    migrate-links -l "ko"

  15. Migriert Links mit Trockenlauf (keine Dateiänderungen):    migrate-links -l "ko" --dry-run

  16. Aktualisiert Links nur, wenn übersetzte Notebooks existieren (kein Rückfall auf Originale):    migrate-links -l "ko" --no-fallback-to-original

  17. Verarbeitet alle Sprachen mit Bestätigungsaufforderung:    migrate-links -l "all"

  18. Verarbeitet alle Sprachen und bestätigt automatisch:    migrate-links -l "all" -y
  19. Protokolle für migrate-links in Dateien speichern:    migrate-links -l "ko ja" -s

### Bewertungsbeispiele

> [!WARNING]  
> **Beta-Funktion**: Die Bewertungsfunktion befindet sich derzeit in der Beta-Phase. Diese Funktion wurde veröffentlicht, um übersetzte Dokumente zu bewerten, und die Bewertungsmethoden sowie die detaillierte Implementierung sind noch in Entwicklung und können sich ändern.

  1. Koreanische Übersetzungen bewerten: evaluate -l "ko"

  2. Bewertung mit benutzerdefiniertem Vertrauensschwellenwert: evaluate -l "ko" -c 0.8

  3. Schnelle Bewertung (nur regelbasiert): evaluate -l "ko" -f

  4. Tiefe Bewertung (nur LLM-basiert): evaluate -l "ko" -D

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache ist als maßgebliche Quelle zu betrachten. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->