<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3fd2055f97f093b6fe102ea24df4458b",
  "translation_date": "2025-10-15T04:18:57+00:00",
  "source_file": "AGENTS.md",
  "language_code": "fr"
}
-->
# AGENTS.md

## Présentation du projet

Co‑op Translator est un outil en ligne de commande Python et un workflow GitHub Actions qui traduit des fichiers Markdown, des notebooks Jupyter et du texte d’images dans plusieurs langues. Il organise les sorties dans des dossiers spécifiques à chaque langue et maintient la synchronisation des traductions avec le contenu source. Le projet est structuré comme une bibliothèque gérée par Poetry avec des points d’entrée CLI.

### Vue d’ensemble de l’architecture

- Les points d’entrée CLI (`translate`, `migrate-links`, `evaluate`) appellent une CLI unifiée qui répartit vers les flux de traduction, de migration de liens et d’évaluation.
- Le chargeur de configuration lit le fichier `.env` et détecte automatiquement le fournisseur LLM (Azure OpenAI ou OpenAI) et, si demandé, le fournisseur de vision (Azure AI Service) pour l’extraction de texte d’image.
- Le cœur de la traduction gère les fichiers Markdown et les notebooks ; le pipeline de vision extrait le texte des images lorsque l’option `-img` est utilisée.
- Les sorties sont organisées dans `translations/<lang>/` pour le texte et `translated_images/` pour les images, en préservant la structure originale.

### Technologies et frameworks principaux

- Python 3.10–3.12, Poetry pour le packaging
- CLI : `click`
- SDK LLM/IA : Azure OpenAI, OpenAI
- Vision : Azure AI Service (Computer Vision)
- HTTP et données : `httpx`, `pydantic`
- Imagerie : `pillow`, `opencv-python`, `matplotlib`
- Outils : `pytest`, `black`, `ruff`

## Commandes d’installation

### Prérequis

- Python 3.10–3.12
- Abonnement Azure (optionnel, pour les services Azure AI)
- Accès Internet pour les API LLM/Vision (ex. Azure OpenAI/OpenAI, Azure AI Vision)

### Option A : Poetry (recommandé)

```bash
# From repository root
pip install poetry
poetry install

# Run any command via Poetry
poetry run translate --help
```

### Option B : pip/venv

```bash
# Create & activate virtual environment
python -m venv .venv
# Windows
.venv\\Scripts\\activate
# Linux/macOS
# source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# (Optional) Editable install for local development
pip install -e .
```

## Utilisation pour l’utilisateur final

### Docker (image publiée)

```bash
# Pull public image from GHCR
docker pull ghcr.io/azure/co-op-translator:latest

# Run with current folder mounted and .env provided (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "fr es" -md

# PowerShell
docker run --rm -it --env-file .env -v ${PWD}:/work ghcr.io/azure/co-op-translator:latest -l "fr es" -md
```

Remarques :
- Le point d’entrée par défaut est `translate`. Remplacez-le par `--entrypoint migrate-links` pour la migration des liens.
- Assurez-vous que la visibilité du package GHCR est Publique pour les téléchargements anonymes.

### CLI (pip)

```bash
pip install co-op-translator
translate -l "fr es" -md
```

### Configuration de l’environnement

Créez un fichier `.env` à la racine du dépôt et fournissez les identifiants/points de terminaison pour le modèle de langue choisi et (optionnellement) le service de vision. Pour la configuration spécifique au fournisseur, consultez `getting_started/set-up-azure-ai.md`.

### Variables d’environnement requises

Au moins un fournisseur LLM doit être configuré. Pour la traduction d’images, Azure AI Service doit aussi être configuré.

- Azure OpenAI (traduction de texte) :
  - `AZURE_OPENAI_API_KEY`
  - `AZURE_OPENAI_ENDPOINT`
  - `AZURE_OPENAI_MODEL_NAME`
  - `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME`
  - `AZURE_OPENAI_API_VERSION`

- OpenAI (alternative pour la traduction de texte) :
  - `OPENAI_API_KEY`
  - `OPENAI_ORG_ID` (optionnel)
  - `OPENAI_CHAT_MODEL_ID` (requis avec le fournisseur OpenAI)
  - `OPENAI_BASE_URL` (optionnel ; par défaut `https://api.openai.com/v1`)

- Azure AI Service pour l’extraction de texte d’image (requis avec `-img`) :
  - `AZURE_AI_SERVICE_API_KEY` (préféré) ou l’ancien `AZURE_SUBSCRIPTION_KEY`
  - `AZURE_AI_SERVICE_ENDPOINT`

Exemple d’extrait `.env` :

```bash
# Azure AI Service (for image translation)
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<your-ai-service>.cognitiveservices.azure.com/"

# Azure OpenAI (primary option)
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<your-azure-openai>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<your-deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"

# OpenAI (alternative option)
OPENAI_API_KEY="..."
OPENAI_ORG_ID="..."            # optional
OPENAI_CHAT_MODEL_ID="gpt-4o"   # required when using OpenAI
OPENAI_BASE_URL="https://api.openai.com/v1" # optional
```

Remarques :

- L’outil détecte automatiquement le fournisseur LLM disponible ; configurez soit Azure OpenAI soit OpenAI.
- La traduction d’images nécessite à la fois `AZURE_AI_SERVICE_API_KEY` et `AZURE_AI_SERVICE_ENDPOINT`.
- La CLI affichera une erreur claire si des variables requises sont manquantes.

## Workflow de développement

- Le code source se trouve dans `src/co_op_translator` ; les tests dans `tests/`.
- CLIs principaux (installés via les points d’entrée) :

```bash
# Translate content to one or more languages (space‑separated codes)
translate -l "fr es de"

# Restrict by content type
translate -l "ja" -md            # only Markdown
translate -l "ko" -nb            # only notebooks
translate -l "zh" -md -img       # Markdown + images

# Update links in previously translated notebooks/Markdown
migrate-links -l "all" -y
```

Consultez la documentation d’utilisation supplémentaire dans `getting_started/`.

## Instructions de test

Lancez les tests depuis la racine du dépôt. Certains tests peuvent nécessiter des identifiants API ; ignorez-les si besoin.

```bash
# Run full test suite
pytest

# Skip tests that require live API keys
pytest -m "not api_key_required"

# Run a subset
pytest tests/co_op_translator -k "name_substring"
```

Couverture optionnelle (nécessite `coverage`) :

```bash
coverage run -m pytest -m "not api_key_required"
coverage html  # outputs to ./htmlcov
```

## Règles de style de code

- Formateur : Black (configuré dans `pyproject.toml`, longueur de ligne 88)
- Linter : Ruff (configuré dans `pyproject.toml`, longueur de ligne 120)
- Vérification des types : mypy (configuration présente ; activez si installé)

Commandes :

```bash
# Via Poetry
poetry run black .
poetry run ruff check .
poetry run ruff check . --fix   # safe auto‑fixes

# Or with global tools
black .
ruff check .
```

Organisez les sources Python sous `src/`, les tests sous `tests/`, et privilégiez les imports explicites dans l’espace de noms du package (`co_op_translator.*`).

## Construction et déploiement

Les artefacts de build sont publiés dans `dist/`.

```bash
# Build (Poetry)
poetry build

# Local install of the built wheel
pip install dist/*.whl
```

L’automatisation via GitHub Actions est prise en charge ; voir :

- `getting_started/github-actions-guide/github-actions-guide-public.md`
- `getting_started/github-actions-guide/github-actions-guide-org.md`

### Image de conteneur (GHCR)

- Image officielle : `ghcr.io/azure/co-op-translator:<tag>`
- Tags : `latest` (sur main), tags sémantiques comme `vX.Y.Z`, et un tag `sha`
- Multi-arch : `linux/amd64, linux/arm64` pris en charge via Buildx
- Modèle Dockerfile : construction des wheels de dépendances dans le builder (avec `build-essential` et `python3-dev`) et installation depuis le wheelhouse local en runtime (`pip install --no-index --find-links=/wheels`)
- Workflow : `.github/workflows/docker-publish.yml` construit et pousse vers GHCR

## Considérations de sécurité

- Gardez les clés API et points de terminaison dans `.env` ou dans le store de secrets de votre CI ; ne jamais commettre de secrets.
- Pour la traduction d’images, les clés/points de terminaison Azure AI Vision sont requis ; sinon, omettez `-img`.
- Vérifiez les quotas/limites du fournisseur lors de gros lots de traduction.

## Règles pour les Pull Requests

### Avant de soumettre

1. **Testez vos modifications :**
   - Exécutez complètement les notebooks concernés
   - Vérifiez que toutes les cellules s’exécutent sans erreur
   - Contrôlez que les sorties sont appropriées

2. **Mises à jour de la documentation :**
   - Mettez à jour le `README.md` si vous ajoutez de nouveaux concepts
   - Ajoutez des commentaires dans les notebooks pour le code complexe
   - Assurez-vous que les cellules markdown expliquent le but

3. **Modifications de fichiers :**
   - Évitez de commettre des fichiers `.env` (utilisez `.env.example`)
   - Ne commettez pas les dossiers `venv/` ou `__pycache__/`
   - Gardez les sorties des notebooks lorsqu’elles illustrent des concepts
   - Supprimez les fichiers temporaires et les notebooks de sauvegarde (`*-backup.ipynb`)

4. **Style et formatage :**
   - Respectez les règles de style et de formatage
   - Lancez `poetry run black .` et `poetry run ruff check .` pour vérifier le style et le formatage

5. **Ajoutez/actualisez les tests et l’aide CLI :**
   - Ajoutez ou mettez à jour les tests lors de changements de comportement
   - Gardez l’aide CLI cohérente avec les modifications


### Format du message de commit et stratégie de fusion

Nous utilisons Squash and Merge par défaut. Le message du commit final doit suivre :

```bash
<type>: <description> (#<PR number>)
```

Types autorisés :
- `Docs` — mises à jour de la documentation
- `Build` — système de build, dépendances, configuration/CI
- `Core` — fonctionnalités et cœur du projet (ex. `src/co_op_translator/core`)

Exemples :
- `Docs: Mise à jour des instructions d’installation pour plus de clarté (#50)`
- `Core: Amélioration de la gestion de la traduction d’images (#60)`

Remarques :
- Les titres de PR sont souvent auto-préfixés selon les labels ; vérifiez que le préfixe généré est correct.

### Format du titre de la PR

Utilisez des titres clairs et concis. Privilégiez la même structure que le message de squash final :
- `Docs: Mise à jour des instructions d’installation pour plus de clarté`
- `Core: Amélioration de la gestion de la traduction d’images`

## Débogage et dépannage

- Problèmes courants et solutions : `getting_started/troubleshooting.md`
- Langues prises en charge et remarques (polices/problèmes connus) : `getting_started/supported-languages.md`
- Pour les problèmes de liens dans les notebooks, relancez : `migrate-links -l "all" -y`

## Notes pour les agents

- Privilégiez Poetry pour des environnements reproductibles ; sinon utilisez `requirements.txt`.
- Lors de l’appel des CLIs en CI, fournissez les secrets requis via les variables d’environnement ou l’injection `.env`.
- Pour les consommateurs en monorepo, ce dépôt fonctionne comme un package autonome ; aucune coordination de sous-package n’est nécessaire.

- Conseils multi-arch : gardez `linux/arm64` si les utilisateurs ARM (Apple Silicon/serveurs ARM) sont visés ; sinon, `linux/amd64` seul est acceptable pour simplifier.
- Orientez les utilisateurs vers le Docker Quick Start dans le `README.md` s’ils préfèrent l’utilisation en conteneur ; incluez les variantes Bash et PowerShell à cause des différences de guillemets.

---

**Avertissement** :
Ce document a été traduit à l’aide du service de traduction IA [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d’assurer l’exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des imprécisions. Le document original dans sa langue d’origine doit être considéré comme la source faisant autorité. Pour les informations critiques, il est recommandé de recourir à une traduction humaine professionnelle. Nous déclinons toute responsabilité en cas de malentendus ou d’interprétations erronées résultant de l’utilisation de cette traduction.