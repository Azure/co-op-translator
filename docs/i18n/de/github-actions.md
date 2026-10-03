# GitHub Actions

Verwenden Sie GitHub Actions, wenn Sie möchten, dass ein Repository geänderte Dokumentation automatisch übersetzt und einen Pull Request mit den erzeugten Ergebnissen öffnet.

Beginnen Sie mit der Standardkonfiguration `GITHUB_TOKEN`, auch für Organisations-Repositories, wenn die Richtlinie dies zulässt. Siehe [GitHub-App-Einrichtung](#github-app-setup), wenn Ihre Organisation eine App-Identität verlangt oder Sie automatische nachgelagerte Workflow-Ausführungen benötigen.

**Menschliche Bearbeitungen:** diese Workflows übersetzen geänderte Quelldateien vollständig neu und können Formulierungen in ihren Übersetzungen überschreiben. Prüfen Sie jeden PR vor dem Zusammenführen. Die Erhaltung akzeptierter Änderungen auf Markdown-Blockebene erfordert eine benutzerdefinierte Integration mit dem [Python API translation state provider](api.md#preserve-accepted-human-edits-with-a-translation-state-provider).

## Ihr erster README-Übersetzungs-PR

Beginnen Sie mit einer Root-`README.md` und einer Zielsprache. Dieser Workflow übersetzt nur Markdown, daher wird Azure AI Vision nicht benötigt.

1. Kopieren Sie [translate-readme.yml](../../assets/workflows/translate-readme.yml) ([Vorlage auf GitHub anzeigen](https://github.com/Azure/co-op-translator/blob/main/docs/assets/workflows/translate-readme.yml)) nach `.github/workflows/translate-readme.yml` in das Repository, das Sie übersetzen möchten, und committen Sie es in den Standardbranch dieses Repositories. Die Vorlage verwendet die Root-Action in `Azure/co-op-translator@main`, die die CLI aus dem gleichen source ref installiert. Sperren Sie auf einen überprüften Commit für reproduzierbare Ausführungen.
2. Öffnen Sie **Actions > Translate README > Run workflow**, wählen Sie eine Sprache und lassen Sie **Preview only** aktiviert. Überprüfen Sie die Token-Schätzung im Vorschau-Schritt. Die Vorschau ruft keine Modellanbieter auf, schreibt keine Übersetzungen und erstellt keinen PR.
3. Fügen Sie die Secrets für einen [Textanbieter](#prerequisites) hinzu, und aktivieren Sie **GitHub Actions erlauben, Pull Requests zu erstellen und zu genehmigen** unter **Einstellungen > Aktionen > Allgemein**. Die Vorlage fordert `contents: write` und `pull-requests: write` für ihren Job an; Sie müssen die Standardberechtigungen nicht für jeden Workflow ändern. Wenn die Organisationsrichtlinie diese Berechtigungen oder diese Einstellung blockiert, fragen Sie einen Administrator nach einer genehmigten [GitHub App](#github-app-setup).
4. Führen Sie den Workflow erneut mit deaktiviertem **Preview only** aus. Er zeigt eine Vorschau, übersetzt, führt `co-op-review --readme-only` aus und erstellt oder aktualisiert einen Übersetzungs-PR erst, nachdem Übersetzung und Review erfolgreich waren. Die Workflow-Zusammenfassung verlinkt auf den PR.
5. Überprüfen Sie die Formulierungen und Dateiänderungen im PR und führen Sie ihn zusammen, wenn Sie bereit sind. Der Workflow führt den PR nicht automatisch zusammen.

Der PR enthält nur `translations/<language>/README.md` und seine Sprach-Metadatendatei. Das Quell-README bleibt unverändert, und Links zu anderen Dokumenten verweisen weiterhin auf die Quelldokumente. Der PR-Text listet geänderte Dateien und Ergebnisse der strukturellen Überprüfung auf. Wenn Übersetzung oder Review fehlschlägt, prüfen Sie die Workflow-Zusammenfassung und die Logs des fehlgeschlagenen Schritts; es wird kein PR erstellt. Wenn es keine Änderungen gibt, ist kein neuer PR erforderlich.

**Hinweis zu Organisation und CI:** Eine GitHub-App ist optional, keine Voraussetzung für Organisationsbesitz. Mit `GITHUB_TOKEN` erfordern Pull-Request-Workflows zum Öffnen, Aktualisieren oder Wiederöffnen eines PR, dass ein Benutzer mit Schreibzugriff **Approve workflows to run** auswählt. Push-Workflows werden durch dieses Token nicht ausgelöst. Für unbeaufsichtigte nachgelagerte CI siehe [GitHub-App-Einrichtung](#github-app-setup) und GitHubs [Regeln zum Auslösen von Workflows](https://docs.github.com/en/actions/how-tos/writing-workflows/choosing-when-your-workflow-runs/triggering-a-workflow).

## Voraussetzungen

Bevor Sie den Workflow erstellen, konfigurieren Sie die AI-Service-Secrets, die Ihr Übersetzungslauf benötigt.

Für die Textübersetzung wird ein Sprachmodellanbieter benötigt:

- Azure OpenAI: `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_MODEL_NAME`, `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME`, `AZURE_OPENAI_API_VERSION`
- OpenAI: `OPENAI_API_KEY`, `OPENAI_CHAT_MODEL_ID`, plus optional `OPENAI_ORG_ID` and `OPENAI_BASE_URL`
- Anthropic: `ANTHROPIC_API_KEY`, `ANTHROPIC_MODEL`, plus optional `ANTHROPIC_BASE_URL`

Für die Bildübersetzung wird zusätzlich Azure AI Vision benötigt:

- `AZURE_AI_SERVICE_API_KEY`
- `AZURE_AI_SERVICE_ENDPOINT`

Siehe [Konfiguration](configuration.md) und [Azure AI-Einrichtung](azure-ai-setup.md) für Details zur lokalen Konfiguration.

## Standardeinrichtung

Nachdem Sie den README-Workflow ausprobiert haben, verwenden Sie diese Einrichtung, um die Markdown-Dateien eines Repositories in mehrere Sprachen zu übersetzen. Sie führt eine Markdown-Überprüfung durch, bevor ein PR geöffnet wird, und benötigt kein Azure AI Vision.

### Schritt 1: Repository-Secrets hinzufügen

Öffnen Sie in Ihrem Ziel-Repository **Settings** > **Secrets and variables** > **Actions**, und fügen Sie dann die Provider-Secrets hinzu, die Ihr Workflow verwendet.

![Actions-Secrets auswählen](../../assets/github-actions/select-setting-action.png)

### Schritt 2: Workflow-Berechtigungen aktivieren

Öffnen Sie **Settings** > **Actions** > **General**.

Unter **Workflow permissions**:

1. Aktivieren Sie **GitHub Actions erlauben, Pull Requests zu erstellen und zu genehmigen**.
2. Speichern Sie die Einstellung.

Der untenstehende Job fordert ausdrücklich `contents: write` und `pull-requests: write` an. Lassen Sie die Standard-Workflow-Berechtigungen des Repositories unverändert. Wenn die Organisationsrichtlinie die PR-Erstellung blockiert, fragen Sie einen Administrator nach einer genehmigten [GitHub App](#github-app-setup).

### Schritt 3: Den Workflow hinzufügen

Erstellen Sie `.github/workflows/co-op-translator.yml`:

```yaml
name: Co-op Translator

on:
  push:
    branches:
      - main

jobs:
  co-op-translator:
    runs-on: ubuntu-latest
    env:
      TARGET_LANGUAGES: "es fr de"

    permissions:
      contents: write
      pull-requests: write

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Set up Python
        uses: actions/setup-python@v7
        with:
          python-version: "3.11"

      - name: Install Co-op Translator
        run: |
          python -m pip install --upgrade pip
          pip install co-op-translator

      - name: Run Co-op Translator
        env:
          PYTHONIOENCODING: utf-8
          AZURE_OPENAI_API_KEY: ${{ secrets.AZURE_OPENAI_API_KEY }}
          AZURE_OPENAI_ENDPOINT: ${{ secrets.AZURE_OPENAI_ENDPOINT }}
          AZURE_OPENAI_MODEL_NAME: ${{ secrets.AZURE_OPENAI_MODEL_NAME }}
          AZURE_OPENAI_CHAT_DEPLOYMENT_NAME: ${{ secrets.AZURE_OPENAI_CHAT_DEPLOYMENT_NAME }}
          AZURE_OPENAI_API_VERSION: ${{ secrets.AZURE_OPENAI_API_VERSION }}
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
          OPENAI_ORG_ID: ${{ secrets.OPENAI_ORG_ID }}
          OPENAI_CHAT_MODEL_ID: ${{ secrets.OPENAI_CHAT_MODEL_ID }}
          OPENAI_BASE_URL: ${{ secrets.OPENAI_BASE_URL }}
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
          ANTHROPIC_MODEL: ${{ secrets.ANTHROPIC_MODEL }}
          ANTHROPIC_BASE_URL: ${{ secrets.ANTHROPIC_BASE_URL }}
        run: |
          translate -l "$TARGET_LANGUAGES" -md -y

      - name: Review Markdown translations
        run: |
          python - <<'PY'
          import os
          from co_op_translator.api import run_review

          run_review(
              language_codes=os.environ["TARGET_LANGUAGES"].split(),
              markdown=True,
              notebook=False,
              output_format="github",
          )
          PY

      - name: Create Pull Request with translations
        uses: peter-evans/create-pull-request@v5
        with:
          token: ${{ secrets.GITHUB_TOKEN }}
          commit-message: "Update translations via Co-op Translator"
          title: "Update translations via Co-op Translator"
          body: |
            This PR updates translations for recent changes to the main branch.
            Markdown structure, freshness, and local links were reviewed.
            Review translation wording before merging.

            Generated by Co-op Translator.
          branch: update-translations
          base: main
          labels: translation, automated-pr
          delete-branch: true
          add-paths: |
            translations/
```

Ändern Sie `TARGET_LANGUAGES` auf die Sprachen, die Ihr Projekt benötigt. Die Überprüfung verwendet die Python-API, um nur Markdown zu prüfen, und stimmt mit dem Übersetzungsschritt überein. Ein Übersetzungs- oder Review-Fehler stoppt den Job vor der PR-Erstellung. Der Workflow führt den PR nicht automatisch zusammen. Für große Repositories fügen Sie einen `paths:`-Filter unter `on.push` hinzu, sodass der Workflow nur ausgeführt wird, wenn sich die Dokumentation ändert.

### Optional: Notebooks und Bilder

Für Notebooks fügen Sie `-nb` zum Übersetzungsbefehl hinzu und setzen `notebook=True` im Review-Schritt. Für Bildtext konfigurieren Sie die beiden [Azure AI Vision-Secrets](#prerequisites), übergeben sie im `env` des Übersetzungsschritts, fügen `-img` zum Befehl hinzu und ergänzen `translated_images/` in den `add-paths` des PR-Schritts. Prüfen Sie übersetzte Bilder visuell; die deterministische Überprüfung zertifiziert weder Bildtext noch linguistische Genauigkeit.

## GitHub-App-Einrichtung

Verwenden Sie eine genehmigte GitHub-App, wenn Ihre Organisation eine App-Identität verlangt oder wenn der generierte PR nachgelagerte CI ohne den `GITHUB_TOKEN`-Freigabeschritt auslösen muss. Eine App umgeht nicht die Organisationsrichtlinie; Administratoren kontrollieren weiterhin deren Installation und Berechtigungen.

### Schritt 1: Erstellen oder Installieren einer GitHub-App

Verwenden Sie eine vorhandene von der Organisation bereitgestellte App, falls verfügbar, oder erstellen Sie eine mit Lese-/Schreibzugriff auf **Contents** und **Pull requests**. Installieren Sie sie auf dem Ziel-Repository mit ggf. erforderlicher organisatorischer Genehmigung.

Notieren Sie:

- App-ID
- Inhalt des privaten Schlüssels

Speichern Sie diese als Repository-Secrets:

- `GH_APP_ID`
- `GH_APP_PRIVATE_KEY`

### Schritt 2: Ein App-Token erstellen

Fügen Sie diesen Schritt direkt vor dem vorhandenen Pull-Request-Schritt hinzu. Verwenden Sie für die README-Vorlage dieselbe Erfolgsbedingung, damit Vorschauen und fehlgeschlagene Übersetzungen kein App-Token anfordern:

```yaml
      - name: Authenticate GitHub App
        id: generate_token
        if: ${{ !inputs.preview && steps.translate.outcome == 'success' && steps.review.outcome == 'success' }}
        uses: actions/create-github-app-token@v2
        with:
          app-id: ${{ secrets.GH_APP_ID }}
          private-key: ${{ secrets.GH_APP_PRIVATE_KEY }}
          permission-contents: write
          permission-pull-requests: write
```

Ändern Sie dann nur den `token`-Input des bestehenden Pull-Request-Schritts auf `${{ steps.generate_token.outputs.token }}`. Behalten Sie dessen Erfolgsbedingung, Branch, PR-Text und `add-paths` unverändert. Das Token ist standardmäßig auf das aktuelle Repository beschränkt. Wenn Sie die Standardeinrichtung anstelle der README-Vorlage anpassen, lassen Sie das obenstehende `if` weg: Dieser Workflow verwendet die Standard-Erfolgsbedingung, sodass Token-Erstellung und PR-Erstellung nur nach erfolgreicher Übersetzung und Review ausgeführt werden.

Siehe die offizielle [create-github-app-token Action](https://github.com/actions/create-github-app-token/tree/v2) für Installation und Token-Berechtigungen.

## Runner-Limits

GitHub-gehostete Runner haben eine maximale Job-Dauer. Große Repositories oder viele Zielsprachen können dieses Limit überschreiten.

Für große Übersetzungs-Workloads:

- Übersetzen Sie pro Lauf weniger Sprachen.
- Verwenden Sie Inhalts-Flags wie `-md`, `-nb` oder `-img`.
- Verwenden Sie einen selbstgehosteten Runner, wenn Repository-Größe oder Modelllatenz gehostete Runner unzuverlässig machen.

## Überprüfung in CI

Verwenden Sie `co-op-review`, wenn ein Pull Request generierte Übersetzungen validieren soll, ohne LLM- oder Vision-Anbieter aufzurufen.

```yaml
      - name: Review translated outputs
        run: |
          co-op-review --changed-from "origin/${{ github.base_ref }}" --format github
```

`co-op-review` ist ein Beta-Befehl für deterministische Überprüfungen. Seine Checks und das Ausgabe-Schema können sich weiterentwickeln, aber er ist so konzipiert, dass er für CI sicher ist, weil er keine Dateien schreibt oder Modellanbieter aufruft.