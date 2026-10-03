# Configuration

Co-op Translator nécessite un fournisseur de modèle de langue. La traduction d'images nécessite en outre Azure AI Vision.

La configuration est lue à partir des variables d'environnement. Pour les projets locaux, placez-les dans un fichier `.env` à la racine du projet.

Pour la configuration des ressources Azure, voir [Configuration Azure AI](azure-ai-setup.md).

## Configuration du runtime local

Utilisez un environnement virtuel avant d'exécuter l'interface en ligne de commande (CLI) localement. Co-op Translator prend en charge Python 3.11 à 3.14.

Pour l'utilisation normale de la CLI, installez le package publié dans un environnement virtuel :

### Windows (PowerShell)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install co-op-translator
translate --help
```

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install co-op-translator
translate --help
```

### Développement du dépôt

Pour le développement du dépôt, installez les dépendances depuis la racine du projet :

```bash
poetry install
poetry run translate --help
```

Une fois la CLI disponible, configurez un fournisseur de modèle de langue dans `.env`.

## Sélection du fournisseur

L'outil détecte automatiquement les fournisseurs dans cet ordre :

1. Azure OpenAI
2. OpenAI
3. Anthropic

La traduction nécessite des identifiants pour le fournisseur, sauf pour les aperçus tels que `translate -l "ko" -md --dry-run`. `migrate-links`, `co-op-review`, et `run_review` sont des opérations de maintenance déterministes et ne nécessitent pas d'identifiants de fournisseur.

## Backend du client de modèle

À partir de Co-op Translator 0.22.0, Azure OpenAI, OpenAI et Anthropic utilisent par défaut Microsoft Agent Framework. Aucun paramètre de backend n'est requis pour une utilisation normale.

Semantic Kernel reste disponible temporairement pour des raisons de compatibilité. Pour le sélectionner explicitement, définissez :

```bash
CO_OP_TRANSLATOR_MODEL_CLIENT="semantic-kernel"
```

L'utilisation de Semantic Kernel génère un avertissement de dépréciation. Le package prévoit de déplacer Semantic Kernel en dépendance optionnelle dans la version 0.23.0 et de retirer l'intégration dans la version 0.24.0, sous réserve des résultats de compatibilité et des retours des utilisateurs. Anthropic requiert `agent-framework` ; sélectionner explicitement `semantic-kernel` avec Anthropic échoue avec une erreur de configuration. Les valeurs invalides échouent lors de l'initialisation du traducteur utilisant un fournisseur au lieu de retomber silencieusement. Suivez le déploiement et signalez les blocages dans [le ticket GitHub #543](https://github.com/Azure/co-op-translator/issues/543).

## Azure OpenAI

Utilisez Azure OpenAI lorsque votre modèle est déployé dans Azure AI Foundry ou Azure OpenAI Service.

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

La vérification de connectivité utilise l'endpoint, la clé API, la version de l'API et le nom du déploiement avant le début de la traduction.

## OpenAI

Utilisez OpenAI lorsque vous appelez directement l'API OpenAI.

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

`OPENAI_CHAT_MODEL_ID` est requis car le traducteur a besoin d'un modèle de chat explicite pour les appels API.

Laissez `OPENAI_ORG_ID` et `OPENAI_BASE_URL` non définis pour la configuration par défaut. Ajoutez un ID d'organisation uniquement si votre compte en a besoin, ou une URL de base uniquement lorsque vous utilisez un endpoint personnalisé. Ne copiez pas les valeurs d'exemple pour les paramètres optionnels.

## Anthropic Claude

Utilisez Anthropic lorsque vous appelez directement l'API Claude. Créez une [clé API Anthropic](https://platform.claude.com/docs/en/get-started) et choisissez un [ID de modèle Claude](https://platform.claude.com/docs/en/about-claude/models/model-ids-and-versions) pris en charge.

```bash
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

`ANTHROPIC_API_KEY` et `ANTHROPIC_MODEL` sont requis. Vous n'avez pas besoin de définir `CO_OP_TRANSLATOR_MODEL_CLIENT` ; Agent Framework est le backend par défaut.

Laissez `ANTHROPIC_BASE_URL` non défini pour l'API Anthropic. Définissez-le seulement si vous utilisez un endpoint personnalisé.

`ANTHROPIC_MAX_TOKENS` est défini par défaut sur `8192`, ce qui laisse de la marge pour des scripts riches en tokens comme Meitei Mayek. Diminuez-le si votre modèle ou l'endpoint compatible Anthropic limite la sortie en dessous de cette valeur.

## Azure AI Vision

La traduction d'images nécessite Azure AI Vision afin que l'outil puisse extraire le texte des images avant que le modèle de langue configuré ne le traduise. Anthropic peut traduire le texte extrait comme Azure OpenAI ou OpenAI.

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

Si la traduction d'images est sélectionnée avec `-img`, `images=True`, ou sans filtre de type de contenu, l'outil valide la configuration de Vision avant le début de la traduction.

## Plusieurs jeux d'identifiants

La couche de configuration prend en charge plusieurs jeux d'identifiants en suffixant les variables avec le même index :

```bash
AZURE_OPENAI_API_KEY_1="..."
AZURE_OPENAI_ENDPOINT_1="https://<resource-1>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME_1="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME_1="<deployment-1>"
AZURE_OPENAI_API_VERSION_1="2024-12-01-preview"

AZURE_OPENAI_API_KEY_2="..."
AZURE_OPENAI_ENDPOINT_2="https://<resource-2>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME_2="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME_2="<deployment-2>"
AZURE_OPENAI_API_VERSION_2="2024-12-01-preview"
```

Chaque jeu doit être complet. La vérification de santé sélectionne un jeu fonctionnel avant que la traduction ne se poursuive.

OpenAI et Anthropic prennent en charge la même convention de suffixe. Gardez chaque variable d'un jeu d'identifiants sur le même suffixe, y compris les valeurs optionnelles telles que `OPENAI_BASE_URL_1` ou `ANTHROPIC_BASE_URL_1`.

## Exigences des commandes

| Commande ou API | LLM requis | Vision requise | Remarques |
| --- | --- | --- | --- |
| `translate -md` | Oui | Non | Traduit uniquement le Markdown. |
| `translate -nb` | Oui | Non | Traduit uniquement les notebooks. |
| `translate -img` | Oui | Oui | Traduit uniquement les images. |
| `translate` sans drapeaux de type | Oui | Oui | Le mode par défaut inclut le Markdown, les notebooks et les images. |
| `evaluate` | Oui | Non | Utilise l'évaluation LLM sauf si `--fast` est sélectionné. |
| `migrate-links` | Non | Non | Effectue la migration locale des liens sans appels au fournisseur. |
| `co-op-review` | Non | Non | Exécute des vérifications déterministes de la structure de traduction, de la fraîcheur, du Markdown, des notebooks et des liens locaux. |
| `run_translation(markdown=True)` | Oui | Non | Traduction Markdown programmatique. |
| `run_translation(images=True)` | Oui | Oui | Traduction d'images programmatique. |
| `run_review(...)` | Non | Non | Revue déterministe programmatique. |

## Répertoires de sortie

Sortie de traduction de texte par défaut :

```text
translations/<language-code>/<source-relative-path>
```

Sortie d'images traduites par défaut :

```text
translated_images/<language-code>/<source-relative-path>
```

L'API Python peut remplacer ces répertoires avec `translations_dir` et `image_dir`.