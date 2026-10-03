# Fehlerbehebung

Verwenden Sie diese Seite, wenn ein Übersetzungslauf unerwartet erfolgreich ist, während der Konfiguration fehlschlägt oder Ausgaben erzeugt, die überprüft werden müssen.

## Erste Schritte

1. Führen Sie zuerst einen gezielten Befehl aus, z. B. `translate -l "ko" -md`.
2. Fügen Sie `-d` für Debug-Logs in der Konsole hinzu.
3. Fügen Sie `-s` hinzu, um Debug-Logs unter `<root-dir>/logs/` zu speichern.
4. Führen Sie `co-op-review` nach der Übersetzung aus, um Aktualität, Struktur und lokale Links zu prüfen.

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

Lösung:

- Konfigurieren Sie Azure OpenAI, OpenAI oder Anthropic.
- Überprüfen Sie, ob die Variablen in der Umgebung vorhanden sind, in der der Befehl ausgeführt wird.
- Für lokale Nutzung legen Sie sie in `.env` im Projektstamm ab.

Siehe [Konfiguration](configuration.md).

### Bildübersetzung ohne Azure AI Vision

Fehler:

```text
Image translation requested but Azure AI Service is not configured.
```

Lösung:

- Fügen Sie `AZURE_AI_SERVICE_API_KEY` hinzu.
- Fügen Sie `AZURE_AI_SERVICE_ENDPOINT` hinzu.
- Oder führen Sie einen textbasierten Befehl wie `translate -l "ko" -md` aus.

### Ungültiger Schlüssel oder Endpunkt

Symptome können `401`, geschwärzte Berechtigungsfehler oder Endpunktzugriffsfehler umfassen.

Lösung:

- Bestätigen Sie, dass der Schlüssel zur selben Azure-Ressource wie der Endpunkt gehört.
- Bestätigen Sie, dass die Ressource Vision unterstützt, wenn `-img` verwendet wird.
- Bestätigen Sie, dass der Azure OpenAI-Bereitstellungsname und die API-Version mit Ihrer Bereitstellung übereinstimmen.
- Führen Sie mit Debug-Logs aus: `translate -l "ko" -md -d -s`.

## Keine Dateien wurden übersetzt

Häufige Ursachen:

- Die gewählten Flags passen nicht zu Ihren Dateien.
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

## Unerwartetes Linkverhalten

Das Umschreiben von Links hängt von den ausgewählten Inhaltstypen ab:

- `-nb` eingeschlossen: Notebook-Links können auf übersetzte Notebooks verweisen.
- `-nb` ausgeschlossen: Notebook-Links können weiterhin auf Quell-Notebooks zeigen.
- `-img` eingeschlossen: Bildlinks können auf übersetzte Bilder verweisen.
- `-img` ausgeschlossen: Bildlinks können weiterhin auf Quellbilder zeigen.

Führen Sie eine vollständige Inhaltsübersetzung durch, wenn alle internen Links übersetzte Ausgaben bevorzugen sollen:

```bash
translate -l "ko" -md -nb -img
```

Führen Sie nach der Übersetzung eine Link-Überprüfung durch:

```bash
co-op-review -l "ko"
```

## Probleme beim Markdown-Rendering

Wenn übersetztes Markdown falsch gerendert wird:

- Prüfen Sie, ob Frontmatter mit `---` beginnt und endet.
- Prüfen Sie, ob die Anzahl der Code-Fences zwischen Quell- und Übersetzungsdateien übereinstimmt.
- Führen Sie `co-op-review` aus, um häufige Strukturprobleme zu finden.
- Übersetzen Sie die spezifische Datei erneut, wenn die Ausgabe beschädigt wurde.

```bash
co-op-review -l "ko" --format github
```

## GitHub Action ausgeführt, aber kein Pull Request wurde erstellt

Wenn `peter-evans/create-pull-request` meldet, dass der Branch nicht vor dem Basis-Branch liegt, hat der Workflow keine Dateien zum Committen gefunden.

Wahrscheinliche Ursachen:

- Der Übersetzungslauf hat keine Änderungen erzeugt.
- `.gitignore` schließt `translations/`, `translated_images/` oder übersetzte Notebooks aus.
- `add-paths` stimmt nicht mit den generierten Ausgabeverzeichnissen überein.
- Der Übersetzungsschritt wurde vorzeitig beendet.

Lösungen:

1. Bestätigen Sie, dass generierte Dateien in `translations/` oder `translated_images/` vorhanden sind.
2. Stellen Sie sicher, dass `.gitignore` generierte Ausgaben nicht ignoriert.
3. Verwenden Sie passende `add-paths`:

   ```yaml
   with:
     add-paths: |
       translations/
       translated_images/
   ```

4. Fügen Sie dem translate-Befehl vorübergehend Debug-Flags hinzu:

   ```bash
   translate -l "ko" -md -d -s
   ```

5. Bestätigen Sie, dass die Workflow-Berechtigungen enthalten:

   ```yaml
   permissions:
     contents: write
     pull-requests: write
   ```

## Übersetzungsqualität

Maschinelle Übersetzungen benötigen möglicherweise eine menschliche Überprüfung. Verwenden Sie `evaluate` nur, wenn Sie experimentelle Qualitätsbewertungen und Reparatur-Workflows bei geringer Vertrauenswürdigkeit wünschen.

!!! warning "Experimentell"
    `evaluate` kann regelbasierte und LLM-basierte Prüfungen verwenden, und sein Bewertungsmodell sowie das Metadatenverhalten können sich ändern. Schließen Sie es aus den erforderlichen CI-Gates aus, es sei denn, Ihr Workflow ist auf Änderungen vorbereitet.

Für deterministische CI-Prüfungen verwenden Sie stattdessen `co-op-review`.