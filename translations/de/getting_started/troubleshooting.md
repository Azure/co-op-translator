<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6e626bef5ed78a1cc55b0dbf44f01d47",
  "translation_date": "2025-10-15T02:13:10+00:00",
  "source_file": "getting_started/troubleshooting.md",
  "language_code": "de"
}
-->
# Microsoft Co-op Translator Fehlerbehebungsleitfaden

## Überblick
Der Microsoft Co-Op Translator ist ein leistungsstarkes Tool, um Markdown-Dokumente nahtlos zu übersetzen. Dieser Leitfaden hilft Ihnen, häufige Probleme bei der Nutzung des Tools zu beheben.

## Häufige Probleme und Lösungen

### 1. Markdown-Tag-Problem
**Problem:** Das übersetzte Markdown-Dokument enthält einen `markdown`-Tag am Anfang, was zu Darstellungsproblemen führt.

**Lösung:** Entfernen Sie einfach den `markdown`-Tag am Anfang der Datei. Dadurch wird das Markdown-Dokument korrekt angezeigt.

**Schritte:**
1. Öffnen Sie die übersetzte Markdown-Datei (`.md`).
2. Suchen Sie den `markdown`-Tag am Anfang des Dokuments.
3. Löschen Sie den `markdown`-Tag.
4. Speichern Sie die Änderungen.
5. Öffnen Sie die Datei erneut, um sicherzustellen, dass sie korrekt angezeigt wird.

### 2. Problem mit Bild-URLs
**Problem:** Die URLs der eingebetteten Bilder stimmen nicht mit der Sprachversion überein, was zu falschen oder fehlenden Bildern führt.

**Lösung:** Überprüfen Sie die URLs der eingebetteten Bilder und stellen Sie sicher, dass sie zur Sprachversion passen. Alle Bilder befinden sich im Ordner `translated_images`, jedes Bild hat einen Sprach-Tag im Dateinamen.

**Schritte:**
1. Öffnen Sie das übersetzte Markdown-Dokument.
2. Suchen Sie die eingebetteten Bilder und deren URLs.
3. Prüfen Sie, ob der Sprach-Tag im Bilddateinamen zur Sprache des Dokuments passt.
4. Aktualisieren Sie die URLs falls nötig.
5. Speichern Sie die Änderungen und öffnen Sie das Dokument erneut, um zu prüfen, ob die Bilder korrekt angezeigt werden.

### 3. Übersetzungsgenauigkeit
**Problem:** Der übersetzte Inhalt ist ungenau oder muss weiter bearbeitet werden.

**Lösung:** Überprüfen Sie das übersetzte Dokument und nehmen Sie die nötigen Anpassungen vor, um die Genauigkeit und Lesbarkeit zu verbessern.

**Schritte:**
1. Öffnen Sie das übersetzte Dokument.
2. Prüfen Sie den Inhalt sorgfältig.
3. Nehmen Sie die nötigen Korrekturen vor.
4. Speichern Sie die Änderungen.

## 4. Berechtigungsfehler Redacted oder 404

Wenn Bilder oder Text nicht in die richtige Sprache übersetzt werden und Sie im -d Debug-Modus einen 401-Fehler erhalten, handelt es sich um einen klassischen Authentifizierungsfehler – entweder ist der Schlüssel ungültig, abgelaufen oder nicht mit der Region des Endpunkts verknüpft.

Führen Sie den Co-op Translator mit dem [-d debug switch](https://github.com/Azure/co-op-translator/blob/main/getting_started/command-reference.md) aus, um die Ursache zu ermitteln.

- **Fehlermeldung:** `Access denied due to invalid subscription key or wrong API endpoint.`
- **Mögliche Ursachen:**
  - Der Abonnement-Schlüssel wurde im Request entfernt oder ist falsch.
  - Der AI Services Key oder Subscription Key gehört zu einer anderen Azure-Ressource (z. B. Translator oder OpenAI) statt zu einer **Azure AI Vision**-Ressource.

 **Ressourcentyp**
  - Gehen Sie zum [Azure Portal](https://portal.azure.com) oder [Azure AI Foundry](https://ai.azure.com) und stellen Sie sicher, dass die Ressource vom Typ `Azure AI services` → `Vision` ist.
  - Überprüfen Sie die Schlüssel und stellen Sie sicher, dass der richtige Schlüssel verwendet wird.

## 5. Konfigurationsfehler (neues Fehlerhandling)

Mit dem neuen selektiven Übersetzungssystem gibt der Co-op Translator jetzt explizite Fehlermeldungen aus, wenn erforderliche Dienste nicht konfiguriert sind.

### 5.1. Azure AI Service nicht für Bildübersetzung konfiguriert

**Problem:** Sie haben die Bildübersetzung angefordert (`-img`-Flag), aber Azure AI Service ist nicht richtig konfiguriert.

**Fehlermeldung:**
```
Error: Image translation requested but Azure AI Service is not configured.
Please add AZURE_AI_SERVICE_API_KEY and AZURE_AI_SERVICE_ENDPOINT to your .env file.
Check Azure AI Service availability and configuration.
```

**Lösung:**
1. **Option 1:** Azure AI Service konfigurieren
   - Fügen Sie `AZURE_AI_SERVICE_API_KEY` zu Ihrer `.env`-Datei hinzu
   - Fügen Sie `AZURE_AI_SERVICE_ENDPOINT` zu Ihrer `.env`-Datei hinzu
   - Prüfen Sie, ob der Service erreichbar ist

2. **Option 2:** Bildübersetzungsanfrage entfernen
   ```bash
   # Instead of: translate -l "ko" -img
   # Use: translate -l "ko" -md
   ```

### 5.2. Fehlende erforderliche Konfiguration

**Problem:** Wichtige LLM-Konfiguration fehlt.

**Fehlermeldung:**
```
Error: No language model configuration found.
Please configure either Azure OpenAI or OpenAI in your .env file.
```

**Lösung:**
1. Prüfen Sie, ob Ihre `.env`-Datei mindestens eine der folgenden LLM-Konfigurationen enthält:
   - **Azure OpenAI:** `AZURE_OPENAI_API_KEY` und `AZURE_OPENAI_ENDPOINT`
   - **OpenAI:** `OPENAI_API_KEY`
   
   Sie benötigen entweder Azure OpenAI ODER OpenAI konfiguriert, nicht beide.

### 5.3. Verwirrung bei selektiver Übersetzung

**Problem:** Es wurden keine Dateien übersetzt, obwohl der Befehl erfolgreich war.

**Mögliche Ursachen:**
- Falsche Dateityp-Flags (`-md`, `-img`, `-nb`)
- Keine passenden Dateien im Projekt
- Falsche Verzeichnisstruktur

**Lösung:**
1. **Debug-Modus verwenden**, um zu sehen, was passiert:
   ```bash
   translate -l "ko" -md -d
   ```

2. **Dateitypen im Projekt prüfen:**
   ```bash
   # For markdown files
   find . -name "*.md" -not -path "./translations/*"
   
   # For notebooks
   find . -name "*.ipynb" -not -path "./translations/*"
   
   # For images
   find . -name "*.png" -o -name "*.jpg" -o -name "*.jpeg" -not -path "./translations/*"
   ```

3. **Flag-Kombinationen überprüfen:**
   ```bash
   # Translate everything (default)
   translate -l "ko"
   
   # Translate specific types
   translate -l "ko" -md -img
   ```

## 6. Migration vom alten System

### 6.1. Markdown-Only-Modus veraltet

**Problem:** Befehle, die sich auf den automatischen Markdown-Only-Fallback verlassen haben, funktionieren nicht mehr wie erwartet.

**Altes Verhalten:**
```bash
# This used to automatically switch to markdown-only mode
translate -l "ko"  # (when Azure AI Vision was not configured)
```

**Neues Verhalten:**
```bash
# This now produces an error if image translation is requested but not configured
translate -l "ko" -img
```

**Lösung:**
- **Seien Sie explizit**, was Sie übersetzen möchten:
  ```bash
  translate -l "ko" -md        # Only markdown
  translate -l "ko" -md -img   # Markdown and images
  translate -l "ko"            # Everything (if all services configured)
  ```

### 6.2. Unerwartetes Link-Verhalten

**Problem:** Links in übersetzten Dateien zeigen auf unerwartete Orte.

**Ursache:** Die dynamische Linkverarbeitung ändert sich je nach ausgewähltem Dateityp.

**Lösung:**
1. **Verstehen Sie das neue Link-Verhalten:**
   - `-nb` enthalten: Notebook-Links zeigen auf übersetzte Versionen
   - `-nb` nicht enthalten: Notebook-Links zeigen auf Originaldateien
   - `-img` enthalten: Bild-Links zeigen auf übersetzte Versionen
   - `-img` nicht enthalten: Bild-Links zeigen auf Originaldateien

2. **Wählen Sie die richtige Kombination** für Ihren Anwendungsfall:
   ```bash
   # All internal links point to translated versions
   translate -l "ko" -md -img -nb
   
   # Only markdown translated, other links point to originals
   translate -l "ko" -md
   ```

## 7. GitHub Action lief, aber es wurde kein Pull Request (PR) erstellt

**Symptom:** Die Workflow-Logs für `peter-evans/create-pull-request` zeigen:

> Branch 'update-translations' is not ahead of base 'main' and will not be created

**Wahrscheinliche Ursachen:**
- **Keine Änderungen erkannt:** Der Übersetzungsschritt hat keine Unterschiede erzeugt (Repo ist bereits aktuell).
- **Ignorierte Ausgaben:** `.gitignore` schließt Dateien aus, die Sie eigentlich committen möchten (z. B. `*.ipynb`, `translations/`, `translated_images/`).
- **add-paths stimmen nicht überein:** Die Pfade, die der Action übergeben wurden, stimmen nicht mit den tatsächlichen Ausgabepfaden überein.
- **Workflow-Logik/Bedingungen:** Der Übersetzungsschritt wurde vorzeitig beendet oder hat in unerwartete Verzeichnisse geschrieben.

**So beheben / prüfen Sie das:**
1. **Ausgaben prüfen:** Nach der Übersetzung sollten neue/geänderte Dateien in `translations/` und/oder `translated_images/` im Workspace liegen.
   - Wenn Notebooks übersetzt werden, prüfen Sie, ob `.ipynb`-Dateien tatsächlich unter `translations/<lang>/...` geschrieben wurden.
2. **`.gitignore` prüfen:** Ignorieren Sie keine generierten Ausgaben. Stellen Sie sicher, dass Sie NICHT ignorieren:
   - `translations/`
   - `translated_images/`
   - `*.ipynb` (bei Notebook-Übersetzung)
3. **add-paths stimmen mit Ausgaben überein:** Verwenden Sie einen mehrzeiligen Wert und fügen Sie beide Ordner hinzu, falls nötig:
   ```yaml
   with:
     add-paths: |
       translations/
       translated_images/
   ```
4. **PR zum Debuggen erzwingen:** Erlauben Sie vorübergehend leere Commits, um zu prüfen, ob alles korrekt verdrahtet ist:
   ```yaml
   with:
     commit-empty: true
   ```
5. **Mit Debug ausführen:** Fügen Sie `-d` zum Übersetzungsbefehl hinzu, um zu sehen, welche Dateien gefunden und geschrieben wurden.
6. **Berechtigungen (GITHUB_TOKEN):** Stellen Sie sicher, dass der Workflow Schreibrechte für Commits und PRs hat:
   ```yaml
   permissions:
     contents: write
     pull-requests: write
   ```


## Schnelle Debug-Checkliste

Wenn Sie Übersetzungsprobleme beheben:

1. **Debug-Modus verwenden:** Fügen Sie das `-d`-Flag hinzu, um detaillierte Logs zu sehen
2. **Flags prüfen:** Stellen Sie sicher, dass `-md`, `-img`, `-nb` zu Ihrer Absicht passen
3. **Konfiguration prüfen:** Überprüfen Sie, ob Ihre `.env`-Datei die nötigen Schlüssel enthält
4. **Schrittweise testen:** Starten Sie mit nur `-md`, fügen Sie dann weitere Typen hinzu
5. **Dateistruktur prüfen:** Stellen Sie sicher, dass die Quelldateien existieren und zugänglich sind

Weitere Informationen zu verfügbaren Befehlen und Flags finden Sie in der [Befehlsreferenz](./command-reference.md).

---

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ausgangssprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die durch die Nutzung dieser Übersetzung entstehen.