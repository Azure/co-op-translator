# Mitwirken an sprachlichen Verbesserungen

Ihr Sprachwissen kann dabei helfen, Co-op Translator zu verbessern. Beginnen Sie mit einem Beispiel, einem Vorschlag zur Korrektur und einer Erklärung über das [Formular für Übersetzungsfeedback](https://github.com/Azure/co-op-translator/issues/new?template=translation_feedback.yml). Sie müssen keinen Code schreiben oder für einen Modelldurchlauf bezahlen.

## Von einem Bericht zur gemeinsamen Verbesserung

1. Ein Beitragender liefert einen Quellenauszug, dessen Übersetzung und Kontext.
2. Ein Sprachprüfer prüft Bedeutung, Natürlichkeit und ob der Vorschlag von einem bestimmten Gebietsschema oder Kurs abhängt.
3. Ein Maintainer entscheidet, ob die Korrektur in den Quellkurs, in eine gemeinsame Sprachanweisung, in die Terminologiekonfiguration oder in den Übersetzungscode gehört.
4. Für eine gemeinsame Regel vergleicht ein Maintainer die Ausgaben vor und nach der Änderung am gemeldeten Beispiel und an unzusammenhängenden Beispielen. Beitragende können diese Ausgaben prüfen, ohne das Tool selbst auszuführen.
5. Der resultierende PR verlinkt den Bericht und nennt die Personen, die Beispiele und Reviews geliefert haben. Bereitstellung oder Neugenerierung in den konsumierenden Repositories ist ein separater Schritt.

Ein Bericht ändert nicht automatisch Prompts oder regeneriert Kursübersetzungen. Kursspezifische Korrekturen sollten mit dem Kurs-Repository verbunden bleiben. Gehen Sie nicht davon aus, dass eine manuelle Änderung eine spätere erneute Übersetzung überdauert; bestätigen Sie das Verhalten für diesen Arbeitsablauf.

## Bestehendes Beispiel: Japanische Markdown-Links

Die [Japanische Anweisungsdatei](https://github.com/Azure/co-op-translator/blob/main/src/co_op_translator/templates/language/ja.md) weist das Modell an, den Linktext zu übersetzen und gleichzeitig die Markdown-Syntax und das Linkziel beizubehalten. Zum Beispiel darf ein als `[text](URL)` geschriebener Link nicht zu `「text」（URL）` werden.

Dies ist ein fokussiertes Beispiel für eine Sprachregel, gestützt durch eine Illustration von korrekter und inkorrekter Ausgabe. Es ist kein Beleg dafür, dass Prompt-Anweisungen allein korrektes Markdown garantieren.

Der [Markdown-Prompt-Builder](https://github.com/Azure/co-op-translator/blob/main/src/co_op_translator/utils/markdown/prompts.py) lädt `templates/language/<language_code>.md` unter Verwendung eines kleingeschriebenen, getrimmten Sprachcodes. Wenn keine Datei existiert, verwendet er die allgemeinen Anweisungen. Dies beschreibt den Pfad des Markdown-Prompts; gehen Sie nicht davon aus, dass jedes Bild oder ein anderer Übersetzungspfad dieselben Anweisungen verwendet.

Die [Prompt-Tests](https://github.com/Azure/co-op-translator/blob/main/tests/co_op_translator/utils/markdown/test_prompts.py) prüfen, dass die japanischen Anweisungen enthalten sind. Das überprüft die Zusammenstellung der Prompts, nicht die Übersetzungsqualität.

## Was gehört in eine Sprachregel?

Schlagen Sie eine enge, wiederholbare Korrektur mit einem Quellbeispiel, dem erwarteten Verhalten und einem Gegenbeispiel vor, in dem die Regel nicht angewendet werden darf. Bewahren Sie Bedeutung, Platzhalter, Code, URLs und die Dokumentstruktur. Vermeiden Sie es, die Stilpräferenz einer Person oder die Terminologie eines Kurses in eine universelle Regel zu verwandeln.

Die aktuelle [Glossar-Implementierung](https://github.com/Azure/co-op-translator/blob/main/src/co_op_translator/glossary.py) schützt Begriffe vor Übersetzung. Sie ist kein Terminologie-Wörterbuch von Quelle zu Ziel. Besprechen Sie neues Terminologie-Verhalten, bevor Sie es Beitragenden versprechen.

## Community-Beispiel: Ein Bericht über einen japanischen Produktnamen

In [Bericht #527](https://github.com/Azure/co-op-translator/issues/527) identifizierte @hyoshioka0128 eine japanische Übersetzung, die den Produktnamen `Co-op Translator` in `Co-op 翻訳` änderte. Der Bericht enthielt einen Link zum betroffenen Dokument und einen Screenshot, wodurch das Problem leicht zu lokalisieren war.

Der Beitragende verlinkte außerdem einen [zugehörigen Kurs-PR](https://github.com/microsoft/AZD-for-beginners/pull/109). In der Diskussion des Issues erkannte der Maintainer den Bericht an und schlug vor, zu untersuchen, warum der Name geändert wurde, einschließlich Terminologieschutz, Glossarverhalten und dem Übersetzungspfad.

Dies zeigt, wie ein kleiner Bericht eine Untersuchung unterstützen kann, die über eine einzelne Formulierungsänderung hinausgeht. Es ist kein verifiziertes Vorher/Nachher-Ergebnis oder ein Beleg dafür, dass die oben genannten japanischen Markdown-Link-Anweisungen dieses Produktnamensproblem behoben haben.

Sie können auf die gleiche Weise beitragen: Teilen Sie den Originaltext, die aktuelle Übersetzung, den vorgeschlagenen Korrekturvorschlag und warum es wichtig ist. Fügen Sie bei Bedarf einen Dokumentlink oder Screenshot hinzu. Sie müssen die Ursache nicht diagnostizieren oder einen Prompt schreiben, bevor Sie es melden.

## Validierung vor der Übernahme einer Regel

Verwenden Sie für Basis- und Kandidatenläufe dieselben Quellproben, Übersetzerrevision, Anbieter/Modell und Generierungseinstellungen und ändern Sie nur die vorgeschlagene Anweisung. Zeichnen Sie die tatsächliche Prompt-Änderung und die Ausgaben auf; wiederholen Sie Beispiele bei Bedarf, um einen konsistenten Effekt von Ausgabevariabilität zu unterscheiden. Schließen Sie den gemeldeten Fehler, kontrastierende Kontexte und Beispiele ein, die bereits korrekt übersetzt werden.

| Beispiel | Quelle/Kontext | Basis-Ausgabe | Kandidaten-Ausgabe | Bewertung des Reviewers |
| --- | --- | --- | --- | --- |
| Gemeldeter Fehler | Zu sammeln | Nicht ausgeführt | Nicht ausgeführt | Ausstehend |
| Gegenbeispiel | Zu sammeln | Nicht ausgeführt | Nicht ausgeführt | Ausstehend |
| Unbetroffenes Beispiel | Zu sammeln | Nicht ausgeführt | Nicht ausgeführt | Ausstehend |

Prüfen Sie strukturelle Invarianten getrennt von linguistischen Beurteilungen. Ein erfolgreicher Prompt-Lade-Test ist keine Qualitätsbewertung, und ein exakt erwarteter Satz ist nicht die einzige gültige Übersetzung. Wenn Kontext, Modellläufe oder Sprachprüfung fehlen, halten Sie den Vorschlag ausstehend, anstatt zu behaupten, das Problem sei behoben.