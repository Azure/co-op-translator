<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0788d7ebe4876c9be89132f48e09b26d",
  "translation_date": "2025-06-12T12:22:07+00:00",
  "source_file": "getting_started/troubleshooting.md",
  "language_code": "de"
}
-->
# Microsoft Co-op Translator Fehlerbehebungsanleitung


## Übersicht
Der Microsoft Co-Op Translator ist ein leistungsstarkes Werkzeug, um Markdown-Dokumente nahtlos zu übersetzen. Diese Anleitung hilft Ihnen dabei, häufig auftretende Probleme bei der Nutzung des Tools zu beheben.

## Häufige Probleme und Lösungen

### 1. Markdown-Tag-Problem
**Problem:** Das übersetzte Markdown-Dokument enthält oben ein `markdown`-Tag, das Darstellungsprobleme verursacht.

**Lösung:** Um das Problem zu beheben, löschen Sie einfach das `markdown`-Tag am Anfang der Datei. Dadurch wird das Markdown-Dokument korrekt dargestellt.

**Schritte:**
1. Öffnen Sie die übersetzte Markdown-Datei (`.md`).
2. Suchen Sie das `markdown`-Tag am Anfang des Dokuments.
3. Löschen Sie das `markdown`-Tag.
4. Speichern Sie die Änderungen in der Datei.
5. Öffnen Sie die Datei erneut, um sicherzustellen, dass sie korrekt dargestellt wird.

### 2. Problem mit URLs eingebetteter Bilder
**Problem:** Die URLs der eingebetteten Bilder stimmen nicht mit der Sprachversion überein, was zu falschen oder fehlenden Bildern führt.

**Lösung:** Überprüfen Sie die URL der eingebetteten Bilder und stellen Sie sicher, dass sie mit der Sprachversion übereinstimmen. Alle Bilder befinden sich im `translated_images`-Ordner, wobei jedes Bild einen Sprachversionstag im Dateinamen trägt.

**Schritte:**
1. Öffnen Sie das übersetzte Markdown-Dokument.
2. Identifizieren Sie die eingebetteten Bilder und deren URLs.
3. Überprüfen Sie, ob die Sprachversion im Bilddateinamen mit der Sprache des Dokuments übereinstimmt.
4. Aktualisieren Sie die URLs bei Bedarf.
5. Speichern Sie die Änderungen und öffnen Sie das Dokument erneut, um zu bestätigen, dass die Bilder korrekt dargestellt werden.

### 3. Übersetzungsgenauigkeit
**Problem:** Der übersetzte Inhalt ist nicht genau oder erfordert weitere Überarbeitungen.

**Lösung:** Überprüfen Sie das übersetzte Dokument und nehmen Sie erforderliche Änderungen vor, um Genauigkeit und Lesbarkeit zu verbessern.

**Schritte:**
1. Öffnen Sie das übersetzte Dokument.
2. Lesen Sie den Inhalt sorgfältig durch.
3. Nehmen Sie notwendige Änderungen vor, um die Übersetzungsgenauigkeit zu verbessern.
4. Speichern Sie die Änderungen.

### 4. Probleme mit der Dateiformatierung
**Problem:** Die Formatierung des übersetzten Dokuments ist fehlerhaft. Dies kann bei Tabellen auftreten, hier wird zusätzlich ``` are added.

**Solution:** Adjust the formatting of the document to match the original structure. Simply deleting the ``` die Tabellenprobleme beheben.

**Schritte:**
1. Öffnen Sie das übersetzte Dokument.
2. Vergleichen Sie es mit dem Originaldokument, um Formatierungsprobleme zu erkennen.
3. Passen Sie die Formatierung an, damit sie mit dem Original übereinstimmt.
4. Speichern Sie die Änderungen.

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir auf Genauigkeit achten, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache gilt als maßgebliche Quelle. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die durch die Nutzung dieser Übersetzung entstehen.