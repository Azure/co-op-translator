<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0788d7ebe4876c9be89132f48e09b26d",
  "translation_date": "2025-05-06T17:50:25+00:00",
  "source_file": "getting_started/troubleshooting.md",
  "language_code": "de"
}
-->
# Microsoft Co-op Translator Troubleshooting Guide


## Übersicht
Der Microsoft Co-Op Translator ist ein leistungsstarkes Tool, um Markdown-Dokumente nahtlos zu übersetzen. Diese Anleitung hilft Ihnen dabei, häufige Probleme bei der Nutzung des Tools zu beheben.

## Häufige Probleme und Lösungen

### 1. Markdown-Tag-Problem
**Problem:** Das übersetzte Markdown-Dokument enthält oben ein `markdown`-Tag, das Darstellungsprobleme verursacht.

**Lösung:** Um das Problem zu beheben, löschen Sie einfach das `markdown`-Tag am Anfang der Datei. Dadurch wird das Markdown-Dokument korrekt dargestellt.

**Schritte:**
1. Öffnen Sie die übersetzte Markdown-Datei (`.md`).
2. Suchen Sie das `markdown`-Tag am Anfang des Dokuments.
3. Löschen Sie das `markdown`-Tag.
4. Speichern Sie die Änderungen an der Datei.
5. Öffnen Sie die Datei erneut, um sicherzustellen, dass sie korrekt dargestellt wird.

### 2. Problem mit URLs eingebetteter Bilder
**Problem:** Die URLs der eingebetteten Bilder stimmen nicht mit der Sprachlokalisierung überein, was zu falschen oder fehlenden Bildern führt.

**Lösung:** Überprüfen Sie die URLs der eingebetteten Bilder und stellen Sie sicher, dass sie der Sprachlokalisierung entsprechen. Alle Bilder befinden sich im `translated_images`-Ordner, jedes Bild hat einen Sprachlokalisierungs-Tag im Dateinamen.

**Schritte:**
1. Öffnen Sie das übersetzte Markdown-Dokument.
2. Identifizieren Sie die eingebetteten Bilder und deren URLs.
3. Überprüfen Sie, ob die Sprachlokalisierung im Bilddateinamen mit der Sprache des Dokuments übereinstimmt.
4. Aktualisieren Sie die URLs bei Bedarf.
5. Speichern Sie die Änderungen und öffnen Sie das Dokument erneut, um zu bestätigen, dass die Bilder korrekt dargestellt werden.

### 3. Übersetzungsgenauigkeit
**Problem:** Der übersetzte Inhalt ist nicht genau oder benötigt weitere Bearbeitung.

**Lösung:** Überprüfen Sie das übersetzte Dokument und nehmen Sie notwendige Änderungen vor, um Genauigkeit und Lesbarkeit zu verbessern.

**Schritte:**
1. Öffnen Sie das übersetzte Dokument.
2. Prüfen Sie den Inhalt sorgfältig.
3. Nehmen Sie erforderliche Änderungen vor, um die Übersetzungsgenauigkeit zu verbessern.
4. Speichern Sie die Änderungen.

### 4. Formatierungsprobleme der Datei
**Problem:** Die Formatierung des übersetzten Dokuments ist fehlerhaft. Dies kann bei Tabellen auftreten, hier wird zusätzlicher ``` are added.

**Solution:** Adjust the formatting of the document to match the original structure. Simply deleting the ``` helfen, die Tabellenprobleme zu beheben.

**Schritte:**
1. Öffnen Sie das übersetzte Dokument.
2. Vergleichen Sie es mit dem Originaldokument, um Formatierungsprobleme zu erkennen.
3. Passen Sie die Formatierung an, damit sie mit dem Originaldokument übereinstimmt.
4. Speichern Sie die Änderungen.

**Haftungsausschluss**:  
Dieses Dokument wurde mithilfe des KI-Übersetzungsdienstes [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ausgangssprache gilt als maßgebliche Quelle. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die durch die Nutzung dieser Übersetzung entstehen.