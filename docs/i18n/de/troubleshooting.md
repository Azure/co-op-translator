# Fehlerbehebung

Use this page when a translation run succeeds unexpectedly, fails during configuration, or produces output that needs review.

## Erste Schritte

1. Run a focused command first, such as `translate -l "ko" -md`.
2. Add `-d` for console debug logs.
3. Add `-s` to save debug logs under `<root-dir>/logs/`.
4. Run `co-op-review` after translation to check freshness, structure, and local links.

```bash
translate -l "ko" -md -d -s
co-op-review -l "ko"
```

## Konfigurationsfehler

### Kein Sprachmodell-Anbieter

Fehler:

```text
No language model configuration found.
```

Behebung:

- Konfigurieren Sie Azure OpenAI oder OpenAI.
- Überprüfen Sie, dass die Variablen in der Umgebung vorhanden sind, in der der Befehl ausgeführt wird.
- Für lokale Nutzung legen Sie sie in `.env` im Projektstamm ab.

Siehe [Konfiguration](configuration.md).

### Bildübersetzung ohne Azure AI Vision

Fehler:

```text
Image translation requested but Azure AI Service is not configured.
```

Behebung:

- Fügen Sie `AZURE_AI_SERVICE_API_KEY` hinzu.
- Fügen Sie `AZURE_AI_SERVICE_ENDPOINT` hinzu.
- Oder führen Sie einen reinen Textbefehl aus, z. B. `translate -l "ko" -md`.

### Ungültiger Schlüssel oder Endpunkt

Symptome können `401`, maskierte Berechtigungsfehler oder Zugriffsfehler auf den Endpunkt umfassen.

Behebung:

- Bestätigen Sie, dass der Schlüssel zur gleichen Azure-Ressource wie der Endpunkt gehört.
- Bestätigen Sie, dass die Ressource Vision unterstützt, wenn Sie `-img` verwenden.
- Bestätigen Sie, dass der Bereitstellungsname von Azure OpenAI und die API-Version mit Ihrer Bereitstellung übereinstimmen.
- Führen Sie mit Debug-Protokollen aus: `translate -l "ko" -md -d -s`.

## Keine Dateien wurden übersetzt

Häufige Ursachen:

- Die ausgewählten Flags passen nicht zu Ihren Dateien.
- Bereits übersetzte Dateien sind vorhanden.
- Quelldateien befinden sich in ausgeschlossenen Verzeichnissen.
- Der Befehl wird vom falschen Projektstamm ausgeführt.

Prüfungen:

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -nb --dry-run
translate -l "ko" -img --dry-run
```

Verwenden Sie `--root-dir`, wenn der Befehl außerhalb des Projektstamms ausgeführt wird.

## Unerwartetes Link-Verhalten

Das Umschreiben von Links hängt von den ausgewählten Inhaltstypen ab:

- `-nb` enthalten: Notebook-Links können auf übersetzte Notebooks verweisen.
- `-nb` ausgeschlossen: Notebook-Links können weiterhin auf die Quell-Notebooks zeigen.
- `-img` enthalten: Bildlinks können auf übersetzte Bilder verweisen.
- `-img` ausgeschlossen: Bildlinks können weiterhin auf die Quellbilder zeigen.

Führen Sie eine vollständige Inhaltsübersetzung durch, wenn alle internen Links bevorzugt auf die übersetzten Ausgaben verweisen sollen:

```bash
translate -l "ko" -md -nb -img
```

Führen Sie nach der Übersetzung eine Link-Überprüfung durch:

```bash
co-op-review -l "ko"
```

## Probleme bei der Markdown-Darstellung

Wenn übersetztes Markdown falsch gerendert wird:

- Prüfen Sie, dass das Frontmatter mit `---` beginnt und endet.
- Prüfen Sie, dass die Anzahl der Code-Fences zwischen Quell- und Übersetzungsdateien übereinstimmt.
- Führen Sie `co-op-review` aus, um häufige Strukturprobleme zu erkennen.
- Übersetzen Sie die betroffene Datei erneut, wenn die Ausgabe beschädigt wurde.

```bash
co-op-review -l "ko" --format github
```

## GitHub Action ausgeführt, aber kein Pull Request erstellt

Wenn `peter-evans/create-pull-request` meldet, dass der Branch nicht vor dem Basisbranch liegt, hat der Workflow keine Dateien zum Committen gefunden.

Mögliche Ursachen:

- Der Übersetzungslauf hat keine Änderungen erzeugt.
- `.gitignore` schließt `translations/`, `translated_images/` oder übersetzte Notebooks aus.
- `add-paths` stimmt nicht mit den erzeugten Ausgabeverzeichnissen überein.
- Der Übersetzungsschritt wurde vorzeitig beendet.

Lösungen:

1. Bestätigen Sie, dass erzeugte Dateien in `translations/` oder `translated_images/` existieren.
2. Bestätigen Sie, dass `.gitignore` die erzeugten Ausgaben nicht ignoriert.
3. Verwenden Sie passende `add-paths`:

   ```yaml
   with:
     add-paths: |
       translations/
       translated_images/
   ```

4. Fügen Sie vorübergehend Debug-Flags zum translate-Befehl hinzu:

   ```bash
   translate -l "ko" -md -d -s
   ```

5. Bestätigen Sie, dass die Workflow-Berechtigungen Folgendes umfassen:

   ```yaml
   permissions:
     contents: write
     pull-requests: write
   ```

## Übersetzungsqualität

Maschinelle Übersetzungen müssen möglicherweise von Menschen überprüft werden. Verwenden Sie `evaluate` nur, wenn Sie experimentelle Qualitätsbewertungen und Workflows zur Reparatur bei geringer Zuverlässigkeit wünschen.

!!! warning "Experimental"
    `evaluate` kann regelbasierte und LLM-basierte Prüfungen verwenden; sein Bewertungsmodell und das Verhalten bei Metadaten können sich ändern. Verwenden Sie es nicht in obligatorischen CI-Gates, es sei denn, Ihr Workflow ist auf Änderungen vorbereitet.

Für deterministische CI-Prüfungen verwenden Sie stattdessen `co-op-review`.