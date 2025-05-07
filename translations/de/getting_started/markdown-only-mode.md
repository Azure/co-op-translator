<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9b1b247a8d0f1736459e0e9ede0d9c92",
  "translation_date": "2025-05-06T17:43:53+00:00",
  "source_file": "getting_started/markdown-only-mode.md",
  "language_code": "de"
}
-->
# Verwendung des Markdown-Only-Modus

## Einführung
Der Markdown-Only-Modus ist darauf ausgelegt, nur den Markdown-Inhalt Ihres Projekts zu übersetzen. Dieser Modus überspringt den Bildübersetzungsprozess und konzentriert sich ausschließlich auf den Textinhalt, was ihn ideal für Situationen macht, in denen keine Bildübersetzung erforderlich ist oder die nötigen Umgebungsvariablen für Computer Vision nicht gesetzt sind.

## Wann verwenden
- Wenn die Computer Vision-bezogenen Umgebungsvariablen nicht konfiguriert sind.
- Wenn Sie nur den Textinhalt übersetzen möchten, ohne Bildverknüpfungen zu aktualisieren.
- Wenn dies vom Benutzer explizit über die `-md` Kommandozeilenoption angegeben wird.

## Wie aktivieren
Um den Markdown-Only-Modus zu aktivieren, verwenden Sie die `-md` Option in Ihrem Befehl. Zum Beispiel:
```
translate -l "ko" -md
```

Oder wenn die Computer Vision-bezogenen Umgebungsvariablen nicht konfiguriert sind. Das Ausführen von `translate -l "ko"` wechselt automatisch in den Markdown-Only-Modus.

```
translate -l "ko"
```

Dieser Befehl übersetzt den Markdown-Inhalt ins Koreanische und aktualisiert Bildverknüpfungen auf ihre ursprünglichen Pfade, anstatt sie auf übersetzte Bildpfade zu ändern.

## Verhalten
Im Markdown-Only-Modus:
- Wird der Bildübersetzungsschritt übersprungen.
- Bleiben Bildverknüpfungen im Markdown unverändert und zeigen auf ihre ursprünglichen Pfade.

## Beispiele
### Vorher
```markdown
![Image](../../../getting_started/translated/path/to/image.png)
```
### Nach Verwendung des Markdown-Only-Modus
```markdown
![Image](../../../getting_started/original/path/to/image.png)
```

## Fehlerbehebung
- Stellen Sie sicher, dass die `-md` Option korrekt im Befehl angegeben ist.
- Überprüfen Sie, dass keine Computer Vision-Umgebungsvariablen den Prozess stören.

## Fazit
Der Markdown-Only-Modus bietet eine einfache Möglichkeit, Textinhalte zu übersetzen, ohne Bildverknüpfungen zu verändern. Er ist besonders nützlich, wenn keine Bildübersetzung erforderlich ist oder wenn in Umgebungen ohne Computer Vision gearbeitet wird.

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache ist als maßgebliche Quelle zu betrachten. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die durch die Nutzung dieser Übersetzung entstehen.