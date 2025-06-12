<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b38d8f042530a4bc872def7cb2c141cd",
  "translation_date": "2025-06-12T11:22:54+00:00",
  "source_file": "getting_started/command-reference.md",
  "language_code": "de"
}
-->
# Befehlsreferenz  
Die **Co-op Translator** CLI bietet verschiedene Optionen, um den Übersetzungsprozess anzupassen:

Befehl                                       | Beschreibung  
---------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------  
translate -l "language_codes"                 | Übersetzt Ihr Projekt in die angegebenen Sprachen. Beispiel: translate -l "es fr de" übersetzt ins Spanische, Französische und Deutsche. Verwenden Sie translate -l "all", um in alle unterstützten Sprachen zu übersetzen.  
translate -l "language_codes" -u              | Aktualisiert Übersetzungen, indem vorhandene gelöscht und neu erstellt werden. Warnung: Dies löscht alle aktuellen Übersetzungen für die angegebenen Sprachen.  
translate -l "language_codes" -img            | Übersetzt nur Bilddateien.  
translate -l "language_codes" -md             | Übersetzt nur Markdown-Dateien.  
translate -l "language_codes" -chk            | Prüft übersetzte Dateien auf Fehler und versucht bei Bedarf die Übersetzung erneut.  
translate -l "language_codes" -d              | Aktiviert den Debug-Modus für detaillierte Protokollierung.  
translate -l "language_codes" -r "root_dir"   | Gibt das Stammverzeichnis des Projekts an.  
translate -l "language_codes" -f              | Verwendet den Schnellmodus für Bildübersetzungen (bis zu 3x schnelleres Rendern bei leichtem Qualitäts- und Ausrichtungsverlust).  
translate -l "language_codes" -y              | Bestätigt automatisch alle Eingabeaufforderungen (praktisch für CI/CD-Pipelines).  
translate -l "language_codes" --help          | Zeigt Hilfedetails innerhalb der CLI mit verfügbaren Befehlen an.  

### Anwendungsbeispiele:

  1. Standardverhalten (neue Übersetzungen hinzufügen, ohne bestehende zu löschen):   translate -l "ko"    translate -l "es fr de" -r "./my_project"  

  2. Nur neue koreanische Bildübersetzungen hinzufügen (vorhandene Übersetzungen werden nicht gelöscht):    translate -l "ko" -img  

  3. Alle koreanischen Übersetzungen aktualisieren (Warnung: Löscht alle vorhandenen koreanischen Übersetzungen vor der Neuübersetzung):    translate -l "ko" -u  

  4. Nur koreanische Bilder aktualisieren (Warnung: Löscht alle vorhandenen koreanischen Bilder vor der Neuübersetzung):    translate -l "ko" -img -u  

  5. Neue Markdown-Übersetzungen für Koreanisch hinzufügen, ohne andere Übersetzungen zu beeinflussen:    translate -l "ko" -md  

  6. Übersetzte Dateien auf Fehler prüfen und Übersetzungen bei Bedarf erneut versuchen: translate -l "ko" -chk  

  7. Übersetzte Dateien auf Fehler prüfen und Übersetzungen erneut versuchen (nur Markdown): translate -l "ko" -chk -md  

  8. Übersetzte Dateien auf Fehler prüfen und Übersetzungen erneut versuchen (nur Bilder): translate -l "ko" -chk -img  

  9. Schnellmodus für Bildübersetzung verwenden:    translate -l "ko" -img -f  

  10. Beispiel für den Debug-Modus: - translate -l "ko" -d: Debug-Protokollierung aktivieren.

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache ist als maßgebliche Quelle zu betrachten. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die durch die Verwendung dieser Übersetzung entstehen.