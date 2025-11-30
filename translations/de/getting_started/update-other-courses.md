<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "93a7150216aa3c2d191135358fa6dd21",
  "translation_date": "2025-11-30T13:35:34+00:00",
  "source_file": "getting_started/update-other-courses.md",
  "language_code": "de"
}
-->
# Aktualisiere den Abschnitt „Andere Kurse“ (Microsoft Beginners Repositories)

Diese Anleitung erklärt, wie man den Abschnitt „Andere Kurse“ mit Co-op Translator automatisch synchronisiert und wie man die globale Vorlage für alle Repositories aktualisiert.

- Gilt für: Nur Microsoft Beginners Repositories
- Funktioniert mit: Co-op Translator CLI und GitHub Actions
- Vorlagenquelle: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## Schnellstart: Auto-Sync im Repository aktivieren

Füge die folgenden Marker um den Abschnitt „Andere Kurse“ in deinem README ein. Co-op Translator ersetzt bei jedem Lauf alles zwischen diesen Markern.

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

Jedes Mal, wenn Co-op Translator ausgeführt wird – entweder über die CLI (z. B. `translate -l "<language codes>"`) oder GitHub Actions – aktualisiert es automatisch den Abschnitt „Andere Kurse“, der von diesen Markern umschlossen ist.

> [!NOTE]
> Wenn du bereits eine Liste hast, umschließe sie einfach mit denselben Markern. Der nächste Lauf ersetzt sie durch den neuesten standardisierten Inhalt.

---

## So änderst du den globalen Inhalt

Wenn du den standardisierten Inhalt aktualisieren möchtest, der in allen Beginners Repositories angezeigt wird:

1. Bearbeite die Vorlage: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)
2. Erstelle einen Pull Request mit deinen Änderungen im Co-op Translator Repository
3. Nach dem Merge des PR wird die Co-op Translator Version aktualisiert
4. Beim nächsten Lauf von Co-op Translator (CLI oder GitHub Action) in einem Ziel-Repository wird der aktualisierte Abschnitt automatisch synchronisiert

So wird eine einzige, verlässliche Quelle für den Inhalt „Andere Kurse“ in allen Beginners Repositories sichergestellt.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, können automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten. Das Originaldokument in seiner Ursprungssprache ist als maßgebliche Quelle zu betrachten. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->