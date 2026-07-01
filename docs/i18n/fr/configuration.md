# Configuration

Co-op Translator nécessite un fournisseur de modèle linguistique. La traduction d'images nécessite en outre Azure AI Vision.

La configuration est lue depuis des variables d'environnement. Pour les projets locaux, placez-les dans un fichier `.env` à la racine du projet.

Pour la configuration des ressources Azure, voir [Azure AI Setup](azure-ai-setup.md).

## Configuration d'exécution locale

Utilisez un environnement virtuel avant d'exécuter l'interface en ligne de commande localement. Co-op Translator prend en charge Python 3.10 à 3.12.

Pour une utilisation normale de la CLI, installez le paquet publié dans un environnement virtuel :

=== "Windows"

    ```powershell
    python -m venv .venv
    .venv\Scripts\activate
    pip install co-op-translator
    translate --help
    ```

=== "macOS / Linux"

    ```bash
    python -m venv .venv
    source .venv/bin/activate
    pip install co-op-translator
    translate --help
    ```

Pour le développement du dépôt, installez plutôt les dépendances depuis la racine du projet :

```bash
poetry install
poetry run translate --help
```

Une fois la CLI disponible, configurez un fournisseur de modèle linguistique dans `.env`.

## Sélection du fournisseur

L'outil détecte automatiquement les fournisseurs dans cet ordre :

1. Azure OpenAI
2. OpenAI

Si aucun fournisseur n'est configuré, `translate`, `evaluate`, `migrate-links` et `run_translation` échouent lors des vérifications de configuration. `co-op-review` et `run_review` sont des vérifications de maintenance déterministes et ne requièrent pas d'identifiants de fournisseur.

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
OPENAI_ORG_ID="..."          # facultatif
OPENAI_BASE_URL="..."        # facultatif
```

`OPENAI_CHAT_MODEL_ID` est requis parce que le traducteur a besoin d'un modèle de chat explicite pour les appels API.

## Azure AI Vision

La traduction d'images nécessite Azure AI Vision afin que l'outil puisse extraire le texte des images avant de le traduire.

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

Si la traduction d'images est sélectionnée avec `-img`, `images=True`, ou sans filtre de type de contenu, l'outil valide la configuration Vision avant le début de la traduction.

## Plusieurs jeux d'identifiants

La couche de configuration prend en charge plusieurs jeux d'identifiants en suffixant les variables avec le même indice :

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

Chaque jeu doit être complet. La vérification de santé sélectionne un jeu fonctionnel avant que la traduction ne continue.

## Exigences par commande

| Commande ou API | LLM requis | Vision requise | Remarques |
| --- | --- | --- | --- |
| `translate -md` | Oui | Non | Traduit uniquement le Markdown. |
| `translate -nb` | Oui | Non | Traduit uniquement les notebooks. |
| `translate -img` | Oui | Oui | Traduit uniquement les images. |
| `translate` with no type flags | Oui | Oui | Le mode par défaut inclut Markdown, notebooks et images. |
| `evaluate` | Oui | Non | Utilise l'évaluation LLM sauf si `--fast` est sélectionné. |
| `migrate-links` | Oui | Non | Effectue la migration des liens, mais exécute toujours les vérifications de configuration partagées. |
| `co-op-review` | Non | Non | Exécute des vérifications déterministes de la structure de traduction, de la fraîcheur, du Markdown, des notebooks et des liens locaux. |
| `run_translation(markdown=True)` | Oui | Non | Traduction Markdown programmatique. |
| `run_translation(images=True)` | Oui | Oui | Traduction d'images programmatique. |
| `run_review(...)` | Non | Non | Vérification déterministe programmatique. |

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