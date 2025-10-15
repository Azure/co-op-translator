<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "527ca4d0a8d3f51087ec3317279e36ee",
  "translation_date": "2025-10-15T02:09:22+00:00",
  "source_file": "getting_started/github-actions-guide/github-actions-guide-public.md",
  "language_code": "fr"
}
-->
# Utiliser l’action GitHub Co-op Translator (Configuration publique)

**Public visé :** Ce guide s’adresse aux utilisateurs de la plupart des dépôts publics ou privés où les autorisations standard des GitHub Actions suffisent. Il utilise le `GITHUB_TOKEN` intégré.

Automatisez la traduction de la documentation de votre dépôt en toute simplicité grâce à l’action GitHub Co-op Translator. Ce guide vous explique comment configurer l’action pour créer automatiquement des pull requests avec les traductions mises à jour dès que vos fichiers Markdown source ou vos images sont modifiés.

> [!IMPORTANT]
>
> **Choisir le bon guide :**
>
> Ce guide détaille la **configuration la plus simple utilisant le `GITHUB_TOKEN` standard**. C’est la méthode recommandée pour la majorité des utilisateurs, car elle ne nécessite pas de gérer des clés privées sensibles d’application GitHub.
>

## Prérequis

Avant de configurer l’action GitHub, assurez-vous de disposer des identifiants nécessaires pour le service d’IA.

**1. Obligatoire : Identifiants du modèle de langue IA**
Vous devez disposer des identifiants pour au moins un modèle de langue pris en charge :

- **Azure OpenAI** : Nécessite un endpoint, une clé API, des noms de modèle/déploiement, une version d’API.
- **OpenAI** : Nécessite une clé API, (optionnel : ID d’organisation, URL de base, ID de modèle).
- Consultez [Modèles et services pris en charge](../../../../README.md) pour plus de détails.

**2. Optionnel : Identifiants IA Vision (pour la traduction d’images)**

- Nécessaire uniquement si vous souhaitez traduire le texte contenu dans des images.
- **Azure AI Vision** : Nécessite un endpoint et une clé d’abonnement.
- Si vous ne les fournissez pas, l’action fonctionnera en [mode Markdown uniquement](../markdown-only-mode.md).

## Configuration

Suivez ces étapes pour configurer l’action GitHub Co-op Translator dans votre dépôt en utilisant le `GITHUB_TOKEN` standard.

### Étape 1 : Comprendre l’authentification (Utilisation du `GITHUB_TOKEN`)

Ce workflow utilise le `GITHUB_TOKEN` intégré fourni par GitHub Actions. Ce jeton donne automatiquement les autorisations nécessaires au workflow pour interagir avec votre dépôt selon les paramètres configurés à l’**étape 3**.

### Étape 2 : Configurer les secrets du dépôt

Vous devez simplement ajouter vos **identifiants de service IA** comme secrets chiffrés dans les paramètres de votre dépôt.

1.  Rendez-vous sur le dépôt GitHub concerné.
2.  Allez dans **Settings** > **Secrets and variables** > **Actions**.
3.  Sous **Repository secrets**, cliquez sur **New repository secret** pour chaque secret de service IA requis listé ci-dessous.

    <img src="../../../../translated_images/select-setting-action.3b95c915d60311592ca51ecb91b3a7bbe0ae45438a2ee872c1520dc90b677780.fr.png" alt="Sélectionner l’action de paramétrage"> *(Référence image : montre où ajouter les secrets)*

**Secrets de service IA requis (Ajoutez TOUS ceux qui correspondent à vos prérequis) :**

| Nom du secret                         | Description                                   | Source de la valeur                |
| :------------------------------------- | :-------------------------------------------- | :--------------------------------- |
| `AZURE_AI_SERVICE_API_KEY`             | Clé pour Azure AI Service (Computer Vision)   | Votre Azure AI Foundry             |
| `AZURE_AI_SERVICE_ENDPOINT`            | Endpoint pour Azure AI Service (Computer Vision) | Votre Azure AI Foundry         |
| `AZURE_OPENAI_API_KEY`                 | Clé pour le service Azure OpenAI              | Votre Azure AI Foundry             |
| `AZURE_OPENAI_ENDPOINT`                | Endpoint pour le service Azure OpenAI         | Votre Azure AI Foundry             |
| `AZURE_OPENAI_MODEL_NAME`              | Nom de votre modèle Azure OpenAI              | Votre Azure AI Foundry             |
| `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME`    | Nom de votre déploiement Azure OpenAI         | Votre Azure AI Foundry             |
| `AZURE_OPENAI_API_VERSION`             | Version d’API pour Azure OpenAI               | Votre Azure AI Foundry             |
| `OPENAI_API_KEY`                       | Clé API pour OpenAI                           | Votre plateforme OpenAI            |
| `OPENAI_ORG_ID`                        | ID d’organisation OpenAI (optionnel)          | Votre plateforme OpenAI            |
| `OPENAI_CHAT_MODEL_ID`                 | ID de modèle OpenAI spécifique (optionnel)    | Votre plateforme OpenAI            |
| `OPENAI_BASE_URL`                      | URL de base API OpenAI personnalisée (optionnel) | Votre plateforme OpenAI        |

### Étape 3 : Configurer les autorisations du workflow

L’action GitHub a besoin d’autorisations via le `GITHUB_TOKEN` pour cloner le code et créer des pull requests.

1.  Dans votre dépôt, allez dans **Settings** > **Actions** > **General**.
2.  Descendez jusqu’à la section **Workflow permissions**.
3.  Sélectionnez **Read and write permissions**. Cela donne au `GITHUB_TOKEN` les autorisations nécessaires `contents: write` et `pull-requests: write` pour ce workflow.
4.  Vérifiez que la case **Allow GitHub Actions to create and approve pull requests** est **cochée**.
5.  Cliquez sur **Save**.

<img src="../../../../translated_images/permission-setting.ae2f02748b0579e7dc3633f14dad67005b533ea8f69890818857de058089a7f5.fr.png" alt="Paramétrage des autorisations">

### Étape 4 : Créer le fichier de workflow

Enfin, créez le fichier YAML qui définit le workflow automatisé utilisant le `GITHUB_TOKEN`.

1.  À la racine de votre dépôt, créez le dossier `.github/workflows/` s’il n’existe pas.
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
          AZURE_AI_SERVICE_API_KEY: ${{ secrets.AZURE_AI_SERVICE_API_KEY }}
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
4.  **Personnaliser le workflow :**
  - **[!IMPORTANT] Langues cibles :** Dans l’étape `Run Co-op Translator`, vous **DEVEZ vérifier et modifier la liste des codes de langue** dans la commande `translate -l "..." -y` pour qu’elle corresponde aux besoins de votre projet. La liste d’exemple (`ar de es...`) doit être remplacée ou ajustée.
  - **Déclencheur (`on:`) :** Le déclencheur actuel lance le workflow à chaque push sur `main`. Pour les gros dépôts, pensez à ajouter un filtre `paths:` (voir l’exemple commenté dans le YAML) pour n’exécuter le workflow que lorsque les fichiers pertinents (ex : documentation source) changent, afin d’économiser les minutes du runner.
  - **Détails du PR :** Personnalisez le `commit-message`, le `title`, le `body`, le nom de la `branch` et les `labels` dans l’étape `Create Pull Request` si besoin.

## Exécution du workflow

> [!WARNING]  
> **Limite de temps des runners hébergés par GitHub :**  
> Les runners hébergés par GitHub comme `ubuntu-latest` ont une **durée d’exécution maximale de 6 heures**.  
> Pour les dépôts de documentation volumineux, si le processus de traduction dépasse 6 heures, le workflow sera automatiquement interrompu.  
> Pour éviter cela, pensez à :  
> - Utiliser un **runner auto-hébergé** (pas de limite de temps)  
> - Réduire le nombre de langues cibles par exécution

Une fois le fichier `co-op-translator.yml` fusionné dans votre branche principale (ou celle spécifiée dans le déclencheur `on:`), le workflow s’exécutera automatiquement à chaque fois que des modifications seront poussées sur cette branche (et correspondent au filtre `paths`, si configuré).

---

**Avertissement** :  
Ce document a été traduit à l’aide du service de traduction IA [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d’assurer l’exactitude, veuillez noter que les traductions automatisées peuvent comporter des erreurs ou des imprécisions. Le document original dans sa langue d’origine doit être considéré comme la source faisant autorité. Pour les informations critiques, il est recommandé de recourir à une traduction humaine professionnelle. Nous déclinons toute responsabilité en cas de malentendus ou d’interprétations erronées résultant de l’utilisation de cette traduction.