<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9b1b247a8d0f1736459e0e9ede0d9c92",
  "translation_date": "2025-06-12T11:36:01+00:00",
  "source_file": "getting_started/markdown-only-mode.md",
  "language_code": "de"
}
-->
# Verwendung des Nur-Markdown-Modus

## Einführung
Der Nur-Markdown-Modus ist darauf ausgelegt, nur den Markdown-Inhalt Ihres Projekts zu übersetzen. Dieser Modus überspringt den Bildübersetzungsprozess und konzentriert sich ausschließlich auf den Textinhalt, was ihn ideal für Szenarien macht, in denen keine Bildübersetzung erforderlich ist oder die notwendigen Umgebungsvariablen für Computer Vision nicht gesetzt sind.

## Wann verwenden
- Wenn die Umgebungsvariablen für Computer Vision nicht konfiguriert sind.
- Wenn Sie nur den Textinhalt übersetzen möchten, ohne Bildverknüpfungen zu aktualisieren.
- Wenn dies vom Benutzer explizit über die `-md` Kommandozeilenoption angegeben wird.

## Wie aktivieren
Um den Nur-Markdown-Modus zu aktivieren, verwenden Sie die `-md` Option in Ihrem Befehl. Zum Beispiel:
```
translate -l "ko" -md
```

Oder wenn die Umgebungsvariablen für Computer Vision nicht konfiguriert sind. Das Ausführen von `translate -l "ko"` schaltet automatisch in den Nur-Markdown-Modus.

```
translate -l "ko"
```

Dieser Befehl übersetzt den Markdown-Inhalt ins Koreanische und aktualisiert Bildverknüpfungen zu ihren Originalpfaden, anstatt sie in Pfade für übersetzte Bilder zu ändern.

## Verhalten
Im Nur-Markdown-Modus:
- Überspringt der Übersetzungsprozess den Schritt der Bildübersetzung.
- Bleiben Bildverknüpfungen im Markdown unverändert und zeigen auf ihre Originalpfade.

## Beispiele
### Vorher
```markdown
![Image](../../../translated_images/image.aa98bae4d78871bb3b23ac9f938ff86539da4cd6fb4c52dafedc4665135c3d61.de.png)
```
### Nach Verwendung des Nur-Markdown-Modus
```markdown
![Image](../../../translated_images/image.fc8708ffe1e1ca12c38822b1a382726da4b232025d1daa8a50ab75c8635d0c4a.de.png)
```

## Fehlerbehebung
- Stellen Sie sicher, dass die `-md` Option korrekt im Befehl angegeben ist.
- Überprüfen Sie, dass keine Umgebungsvariablen für Computer Vision den Prozess stören.

## Fazit
Der Nur-Markdown-Modus bietet eine einfache Möglichkeit, Textinhalte zu übersetzen, ohne Bildverknüpfungen zu verändern. Er ist besonders nützlich, wenn keine Bildübersetzung erforderlich ist oder wenn in Umgebungen ohne Computer Vision gearbeitet wird.

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache ist als maßgebliche Quelle zu betrachten. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.