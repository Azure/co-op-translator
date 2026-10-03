# GitHub Actions

Utilisez GitHub Actions lorsque vous souhaitez qu’un dépôt traduise automatiquement la documentation modifiée et ouvre une pull request avec les résultats générés.

Commencez par la configuration standard `GITHUB_TOKEN`, y compris pour les dépôts d’organisation lorsque la politique le permet. Voir [GitHub App Setup](#github-app-setup) lorsque votre organisation exige une identité d’App ou que vous avez besoin d’exécutions automatiques de workflows en aval.

**Modifications humaines :** ces workflows retraduisent entièrement les fichiers source modifiés et peuvent écraser la formulation modifiée dans leurs traductions. Examinez chaque PR avant de fusionner. La préservation au niveau des blocs Markdown des modifications acceptées nécessite une intégration personnalisée avec le [fournisseur d'état de traduction de l'API Python](api.md#preserve-accepted-human-edits-with-a-translation-state-provider).

## Votre première PR de traduction du README

Commencez par un `README.md` racine et une langue cible. Ce workflow traduit uniquement le Markdown, donc Azure AI Vision n'est pas requis.

1. Copiez [translate-readme.yml](../../assets/workflows/translate-readme.yml) ([voir le modèle sur GitHub](https://github.com/Azure/co-op-translator/blob/main/docs/assets/workflows/translate-readme.yml)) dans `.github/workflows/translate-readme.yml` dans le dépôt que vous voulez traduire, et validez-le sur la branche par défaut de ce dépôt. Le modèle utilise l'Action racine `Azure/co-op-translator@main`, qui installe l'interface en ligne de commande depuis la même référence source. Épinglez un commit révisé pour des exécutions reproductibles.
2. Ouvrez **Actions > Translate README > Run workflow**, choisissez une langue et laissez **Preview only** coché. Vérifiez l'estimation de tokens à l'étape d'aperçu. L'aperçu n'appelle pas les fournisseurs de modèles, n'écrit pas les traductions et ne crée pas de PR.
3. Ajoutez les secrets pour un [fournisseur de texte](#prerequisites), et activez **Autoriser GitHub Actions à créer et approuver des pull requests** dans **Paramètres > Actions > Général**. Le modèle demande `contents: write` et `pull-requests: write` pour son job ; vous n'avez pas besoin de modifier les permissions par défaut pour chaque workflow. Si la politique de l'organisation bloque ces permissions ou ce réglage, demandez à un administrateur à propos d'une [GitHub App](#github-app-setup) approuvée.
4. Exécutez de nouveau le workflow avec **Preview only** décoché. Il effectue l'aperçu, traduit, lance `co-op-review --readme-only`, et crée ou met à jour une PR de traduction uniquement après réussite de la traduction et de la revue. Le résumé du workflow contient un lien vers la PR.
5. Vérifiez la formulation et les modifications de fichiers dans la PR, puis fusionnez quand vous êtes prêt. Le workflow ne fusionne pas automatiquement.

La PR contient uniquement `translations/<language>/README.md` et son fichier de métadonnées de langue. Le README source reste inchangé, et les liens vers d'autres documents continuent de pointer vers les documents source. Le corps de la PR liste les fichiers modifiés et les résultats de la revue structurelle. Si la traduction ou la revue échoue, inspectez le résumé du workflow et les logs des étapes échouées ; aucune PR n'est créée. S'il n'y a pas de changements, aucune nouvelle PR n'est nécessaire.

**Note organisation et CI :** Une GitHub App est optionnelle, pas une exigence liée à la propriété de l'organisation. Avec `GITHUB_TOKEN`, les workflows de pull request pour ouvrir, mettre à jour ou rouvrir une PR nécessitent qu’un utilisateur ayant un accès en écriture sélectionne **Approve workflows to run**. Les workflows de push ne sont pas déclenchés par ce token. Pour du CI en aval sans intervention, voir [GitHub App Setup](#github-app-setup) et les [règles de déclenchement des workflows](https://docs.github.com/en/actions/how-tos/writing-workflows/choosing-when-your-workflow-runs/triggering-a-workflow) de GitHub.

## Prérequis

Avant de créer le workflow, configurez les secrets du service IA dont votre exécution de traduction a besoin.

La traduction de texte nécessite un fournisseur de modèle de langue :

- Azure OpenAI: `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_MODEL_NAME`, `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME`, `AZURE_OPENAI_API_VERSION`
- OpenAI: `OPENAI_API_KEY`, `OPENAI_CHAT_MODEL_ID`, plus optional `OPENAI_ORG_ID` et `OPENAI_BASE_URL`
- Anthropic: `ANTHROPIC_API_KEY`, `ANTHROPIC_MODEL`, plus optional `ANTHROPIC_BASE_URL`

La traduction d'images nécessite en outre Azure AI Vision :

- `AZURE_AI_SERVICE_API_KEY`
- `AZURE_AI_SERVICE_ENDPOINT`

Voir [Configuration](configuration.md) et [Azure AI Setup](azure-ai-setup.md) pour les détails de configuration locale.

## Configuration standard

Après avoir essayé le workflow README, utilisez cette configuration pour traduire les fichiers Markdown d'un dépôt en plusieurs langues. Il exécute une revue Markdown avant d'ouvrir une PR et ne nécessite pas Azure AI Vision.

### Étape 1 : Ajouter les secrets du dépôt

Dans le dépôt cible, ouvrez **Settings** > **Secrets and variables** > **Actions**, puis ajoutez les secrets des fournisseurs que votre workflow utilisera.

![Sélectionner les secrets Actions](../../assets/github-actions/select-setting-action.png)

### Étape 2 : Activer les permissions du workflow

Ouvrez **Settings** > **Actions** > **General**.

Sous **Workflow permissions** :

1. Activez **Autoriser GitHub Actions à créer et approuver des pull requests**.
2. Enregistrez le réglage.

Le job ci-dessous demande explicitement `contents: write` et `pull-requests: write`. Gardez les permissions par défaut du workflow du dépôt inchangées. Si la politique de l'organisation bloque la création de PR, demandez à un administrateur au sujet d'une [GitHub App](#github-app-setup) approuvée.

### Étape 3 : Ajouter le workflow

Créez `.github/workflows/co-op-translator.yml` :

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

Changez `TARGET_LANGUAGES` pour les langues dont votre projet a besoin. La revue utilise l'API Python pour vérifier uniquement le Markdown, en accord avec l'étape de traduction. Une erreur de traduction ou de revue arrête le job avant la création de la PR. Le workflow ne fusionne pas la PR automatiquement. Pour les grands dépôts, ajoutez un filtre `paths:` sous `on.push` afin que le workflow ne s'exécute que lorsque la documentation change.

### Optionnel : notebooks et images

Pour les notebooks, ajoutez `-nb` à la commande de traduction et définissez `notebook=True` dans l'étape de revue. Pour le texte des images, configurez les deux [Azure AI Vision secrets](#prerequisites), transmettez-les dans `env` de l'étape de traduction, ajoutez `-img` à la commande et ajoutez `translated_images/` à `add-paths` de l'étape PR. Vérifiez visuellement les images traduites ; la revue déterministe ne certifie pas le texte des images ni l'exactitude linguistique.

## Configuration de GitHub App

Utilisez une GitHub App approuvée lorsque votre organisation exige une identité d'App, ou lorsque la PR générée doit déclencher du CI en aval sans l'étape d'approbation `GITHUB_TOKEN`. Une App ne contourne pas la politique de l'organisation ; les administrateurs contrôlent toujours son installation et ses permissions.

### Étape 1 : Créer ou installer une GitHub App

Utilisez une App fournie par l'organisation si disponible, ou créez-en une avec un accès lecture/écriture à **Contents** et **Pull requests**. Installez-la sur le dépôt cible avec toute approbation organisationnelle requise.

Notez :

- ID de l'App
- Contenu de la clé privée

Stockez-les comme secrets du dépôt :

- `GH_APP_ID`
- `GH_APP_PRIVATE_KEY`

### Étape 2 : Générer un token d'App

Ajoutez cette étape immédiatement avant l'étape de pull request existante. Pour le modèle README, utilisez la même condition de succès afin que les aperçus et les traductions échouées ne demandent pas de token d'App :

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

Changez ensuite uniquement l'entrée `token` de l'étape de pull request existante en `${{ steps.generate_token.outputs.token }}`. Gardez sa condition de succès, sa branche, le corps de la PR et `add-paths` inchangés. Le token est limité au dépôt courant par défaut. Lors de l'adaptation de la configuration standard plutôt que du modèle README, omettez le `if` ci‑dessus : ce workflow utilise la condition de succès par défaut, donc la création du token et la création de la PR s'exécutent uniquement après la réussite de la traduction et de la revue.

Voir l'[Action create-github-app-token](https://github.com/actions/create-github-app-token/tree/v2) officielle pour l'installation et les permissions du token.

## Limites des runners

Les runners hébergés par GitHub ont une durée maximale par job. Les grands dépôts ou de nombreuses langues cibles peuvent dépasser cette limite.

Pour les charges de traduction importantes :

- Traduisez moins de langues par exécution.
- Utilisez des indicateurs de contenu tels que `-md`, `-nb` ou `-img`.
- Utilisez un runner auto‑hébergé lorsque la taille du dépôt ou la latence du modèle rend les runners hébergés peu fiables.

## Revue dans le CI

Utilisez `co-op-review` lorsqu'une pull request doit valider les traductions générées sans appeler les fournisseurs LLM ou Vision.

```yaml
      - name: Review translated outputs
        run: |
          co-op-review --changed-from "origin/${{ github.base_ref }}" --format github
```

`co-op-review` est une commande de revue déterministe en version bêta. Ses vérifications et le schéma de sortie peuvent évoluer, mais elle est conçue pour être sûre pour le CI car elle n'écrit pas de fichiers ni n'appelle de fournisseurs de modèles.