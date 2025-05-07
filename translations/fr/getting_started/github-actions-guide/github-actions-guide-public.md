<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "87bf95d45e684475ef1e67d8dae5f6eb",
  "translation_date": "2025-05-06T18:11:18+00:00",
  "source_file": "getting_started/github-actions-guide/github-actions-guide-public.md",
  "language_code": "fr"
}
-->
# Utilisation de l’action GitHub Co-op Translator (Configuration publique)

**Public visé :** Ce guide s’adresse aux utilisateurs de la plupart des dépôts publics ou privés où les permissions standard de GitHub Actions sont suffisantes. Il utilise le `GITHUB_TOKEN` intégré.

Automatisez facilement la traduction de la documentation de votre dépôt grâce à l’action GitHub Co-op Translator. Ce guide vous explique comment configurer l’action pour créer automatiquement des pull requests avec des traductions mises à jour dès que vos fichiers Markdown sources ou images changent.

> [!IMPORTANT]
>
> **Choisir le bon guide :**
>
> Ce guide décrit la **configuration la plus simple avec le `GITHUB_TOKEN` standard**. C’est la méthode recommandée pour la plupart des utilisateurs car elle ne nécessite pas de gérer des clés privées sensibles d’application GitHub.
>

## Prérequis

Avant de configurer l’action GitHub, assurez-vous de disposer des identifiants nécessaires pour les services d’IA.

**1. Obligatoire : Identifiants du modèle de langue IA**  
Vous devez avoir des identifiants pour au moins un modèle de langue supporté :

- **Azure OpenAI** : nécessite Endpoint, clé API, noms du modèle/déploiement, version de l’API.  
- **OpenAI** : nécessite clé API, (optionnel : ID organisation, URL de base, ID modèle).  
- Consultez [Modèles et services supportés](../../../../README.md) pour plus de détails.  
- Guide d’installation : [Configurer Azure OpenAI](../set-up-resources/set-up-azure-openai.md).

**2. Optionnel : Identifiants Computer Vision (pour la traduction d’images)**

- Nécessaire uniquement si vous devez traduire du texte dans des images.  
- **Azure Computer Vision** : nécessite Endpoint et clé d’abonnement.  
- Si non fournis, l’action utilisera par défaut le [mode Markdown uniquement](../markdown-only-mode.md).  
- Guide d’installation : [Configurer Azure Computer Vision](../set-up-resources/set-up-azure-computer-vision.md).

## Configuration et installation

Suivez ces étapes pour configurer l’action GitHub Co-op Translator dans votre dépôt en utilisant le `GITHUB_TOKEN` standard.

### Étape 1 : Comprendre l’authentification (utilisation du `GITHUB_TOKEN`)

Ce workflow utilise le `GITHUB_TOKEN` intégré fourni par GitHub Actions. Ce jeton donne automatiquement les permissions nécessaires au workflow pour interagir avec votre dépôt selon les réglages définis à l’**Étape 3**.

### Étape 2 : Configurer les secrets du dépôt

Vous devez uniquement ajouter vos **identifiants des services IA** en tant que secrets chiffrés dans les paramètres de votre dépôt.

1.  Accédez au dépôt GitHub cible.  
2.  Allez dans **Settings** > **Secrets and variables** > **Actions**.  
3.  Sous **Repository secrets**, cliquez sur **New repository secret** pour chaque secret requis listé ci-dessous.

    ![Select setting action](../../../../getting_started/github-actions-guide/imgs/select-setting-action.png) *(Référence image : montre où ajouter les secrets)*

**Secrets requis pour les services IA (ajoutez TOUS ceux qui s’appliquent selon vos prérequis) :**

| Nom du secret                      | Description                                | Source de la valeur              |
| :-------------------------------- | :---------------------------------------- | :------------------------------ |
| `AZURE_SUBSCRIPTION_KEY`            | Clé pour Azure AI Service (Computer Vision)  | Votre instance Azure AI          |
| `AZURE_AI_SERVICE_ENDPOINT`         | Endpoint pour Azure AI Service (Computer Vision) | Votre instance Azure AI          |
| `AZURE_OPENAI_API_KEY`              | Clé pour le service Azure OpenAI           | Votre instance Azure AI          |
| `AZURE_OPENAI_ENDPOINT`             | Endpoint pour le service Azure OpenAI      | Votre instance Azure AI          |
| `AZURE_OPENAI_MODEL_NAME`           | Nom du modèle Azure OpenAI                   | Votre instance Azure AI          |
| `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` | Nom du déploiement Azure OpenAI              | Votre instance Azure AI          |
| `AZURE_OPENAI_API_VERSION`          | Version API pour Azure OpenAI                | Votre instance Azure AI          |
| `OPENAI_API_KEY`                    | Clé API pour OpenAI                         | Votre plateforme OpenAI          |
| `OPENAI_ORG_ID`                     | ID organisation OpenAI (optionnel)          | Votre plateforme OpenAI          |
| `OPENAI_CHAT_MODEL_ID`              | ID modèle OpenAI spécifique (optionnel)      | Votre plateforme OpenAI          |
| `OPENAI_BASE_URL`                   | URL de base API OpenAI personnalisée (optionnel) | Votre plateforme OpenAI          |

### Étape 3 : Configurer les permissions du workflow

L’action GitHub a besoin des permissions accordées via le `GITHUB_TOKEN` pour récupérer le code et créer des pull requests.

1.  Dans votre dépôt, allez dans **Settings** > **Actions** > **General**.  
2.  Descendez jusqu’à la section **Workflow permissions**.  
3.  Sélectionnez **Read and write permissions**. Cela donne au `GITHUB_TOKEN` les permissions `contents: write` et `pull-requests: write` nécessaires pour ce workflow.  
4.  Vérifiez que la case **Allow GitHub Actions to create and approve pull requests** est cochée.  
5.  Cliquez sur **Save**.

![Permission setting](../../../../getting_started/github-actions-guide/imgs/permission-setting.png)

### Étape 4 : Créer le fichier de workflow

Enfin, créez le fichier YAML qui définit le workflow automatisé utilisant le `GITHUB_TOKEN`.

1.  À la racine de votre dépôt, créez le répertoire `.github/workflows/` s’il n’existe pas.  
2.  Dans `.github/workflows/`, créez un fichier nommé `co-op-translator.yml`.  
3.  Collez le contenu suivant dans `co-op-translator.yml`.

```yaml
name: Co-op Translator

on:
  push:
    branches:
      - main

jobs:
  co-op-translator:
    runs-on: ubuntu-latest

    permissions:
      contents: write
      pull-requests: write

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      - name: Install Co-op Translator
        run: |
          python -m pip install --upgrade pip
          pip install co-op-translator

      - name: Run Co-op Translator
        env:
          PYTHONIOENCODING: utf-8
          # === AI Service Credentials ===
          AZURE_SUBSCRIPTION_KEY: ${{ secrets.AZURE_SUBSCRIPTION_KEY }}
          AZURE_AI_SERVICE_ENDPOINT: ${{ secrets.AZURE_AI_SERVICE_ENDPOINT }}
          AZURE_OPENAI_API_KEY: ${{ secrets.AZURE_OPENAI_API_KEY }}
          AZURE_OPENAI_ENDPOINT: ${{ secrets.AZURE_OPENAI_ENDPOINT }}
          AZURE_OPENAI_MODEL_NAME: ${{ secrets.AZURE_OPENAI_MODEL_NAME }}
          AZURE_OPENAI_CHAT_DEPLOYMENT_NAME: ${{ secrets.AZURE_OPENAI_CHAT_DEPLOYMENT_NAME }}
          AZURE_OPENAI_API_VERSION: ${{ secrets.AZURE_OPENAI_API_VERSION }}
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
          OPENAI_ORG_ID: ${{ secrets.OPENAI_ORG_ID }}
          OPENAI_CHAT_MODEL_ID: ${{ secrets.OPENAI_CHAT_MODEL_ID }}
          OPENAI_BASE_URL: ${{ secrets.OPENAI_BASE_URL }}
        run: |
          # =====================================================================
          # IMPORTANT: Set your target languages here (REQUIRED CONFIGURATION)
          # =====================================================================
          # Example: Translate to Spanish, French, German. Add -y to auto-confirm.
          translate -l "es fr de" -y  # <--- MODIFY THIS LINE with your desired languages

      - name: Create Pull Request with translations
        uses: peter-evans/create-pull-request@v5
        with:
          token: ${{ secrets.GITHUB_TOKEN }}
          commit-message: "🌐 Update translations via Co-op Translator"
          title: "🌐 Update translations via Co-op Translator"
          body: |
            This PR updates translations for recent changes to the main branch.

            ### 📋 Changes included
            - Translated contents are available in the `translations/` directory
            - Translated images are available in the `translated_images/` directory

            ---
            🌐 Automatically generated by the [Co-op Translator](https://github.com/Azure/co-op-translator) GitHub Action.
          branch: update-translations
          base: main
          labels: translation, automated-pr
          delete-branch: true
          add-paths: |
            translations/
            translated_images/
```  
4.  **Personnalisez le workflow :**  
  - **[!IMPORTANT] Langues cibles :** dans l’étape `Run Co-op Translator` step, you **MUST review and modify the list of language codes** within the `translate -l "..." -y` command to match your project's requirements. The example list (`ar de es...`) needs to be replaced or adjusted.
  - **Trigger (`on:`):** The current trigger runs on every push to `main`. For large repositories, consider adding a `paths:` filter (see commented example in the YAML) to run the workflow only when relevant files (e.g., source documentation) change, saving runner minutes.
  - **PR Details:** Customize the `commit-message`, `title`, `body`, `branch` name, and `labels` in the `Create Pull Request` si nécessaire.

**Avertissement** :  
Ce document a été traduit à l’aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçons d’assurer l’exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d’origine doit être considéré comme la source faisant foi. Pour les informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous ne saurions être tenus responsables des malentendus ou des mauvaises interprétations résultant de l’utilisation de cette traduction.