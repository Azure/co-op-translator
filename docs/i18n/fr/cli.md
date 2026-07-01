# Référence CLI

Co-op Translator installe ces points d'entrée en ligne de commande :

- `translate`
- `evaluate`
- `migrate-links`
- `co-op-review`
- `co-op-translator-mcp`

Les commandes `translate`, `evaluate`, `migrate-links` et `co-op-review` sont dispatchées via `co_op_translator.__main__`, qui sélectionne l'implémentation de la commande en fonction du nom du script invoqué. Le serveur MCP utilise `co_op_translator.mcp.server` directement.

Si vous hésitez entre l'interface CLI, l'API Python et le MCP, commencez par [Choose Your Workflow](workflows.md).

## First-Time CLI Flow

Commencez ici si vous utilisez Co-op Translator depuis un terminal :

1. Configurez un fournisseur LLM comme décrit dans [Configuration](configuration.md).
2. Choisissez le type de contenu que vous souhaitez traduire.
3. Exécutez d'abord une commande ciblée, par exemple une traduction uniquement Markdown.
4. Utilisez `--dry-run` avant des modifications importantes du dépôt.
5. Utilisez `co-op-review` après la traduction pour vérifier la structure et la fraîcheur.

| Objectif | Commande pour commencer |
| --- | --- |
| Translate Markdown documents | `translate -l "ko" -md` |
| Translate notebooks | `translate -l "ko" -nb` |
| Translate image text | `translate -l "ko" -img` |
| Preview work without writing files | `translate -l "ko" -md --dry-run` |
| Review existing translations | `co-op-review -l "ko"` |
| Update notebook and Markdown links | `migrate-links -l "ko" --dry-run` |
| Expose tools to an MCP client | Configure the [MCP Server](mcp.md) instead of running CLI commands directly. |

## translate

Traduire des fichiers Markdown, des notebooks et du texte d'images vers une ou plusieurs langues cibles.

```bash
translate -l "ko ja fr"
```

### Exemples courants

Traduire uniquement le Markdown :

```bash
translate -l "de" -md
```

Traduire uniquement les notebooks :

```bash
translate -l "zh-CN" -nb
```

Traduire Markdown et images :

```bash
translate -l "pt-BR" -md -img
```

Mettre à jour les traductions existantes en les supprimant et en les recréant :

```bash
translate -l "ko" -u
```

Exécuter sans invites interactives :

```bash
translate -l "ko ja" -md -y
```

Enregistrer les logs :

```bash
translate -l "ko" -s
```

### Options

| Option | Requis | Description |
| --- | --- | --- |
| `-l`, `--language-codes` | Yes | Codes de langue séparés par des espaces, par exemple `"es fr de"`, ou `"all"`. |
| `-r`, `--root-dir` | No | Racine du projet. Par défaut le répertoire courant. |
| `-u`, `--update` | No | Supprime les traductions existantes pour les langues sélectionnées et les recrée. |
| `-img`, `--images` | No | Traduire uniquement les fichiers image. |
| `-md`, `--markdown` | No | Traduire uniquement les fichiers Markdown. |
| `-nb`, `--notebook` | No | Traduire uniquement les fichiers Jupyter notebook. |
| `-d`, `--debug` | No | Activer les logs de débogage dans la console. |
| `-s`, `--save-logs` | No | Enregistrer les logs de niveau DEBUG sous `<root-dir>/logs/`. |
| `-x`, `--fix` | No | Retraduire les fichiers Markdown à faible confiance en fonction des résultats d'évaluation précédents. |
| `-c`, `--min-confidence` | No | Seuil de confiance pour `--fix`. Par défaut `0.7`. |
| `--add-disclaimer`, `--no-disclaimer` | No | Ajouter ou supprimer les mentions indiquant une traduction automatique. Activé par défaut dans la CLI. |
| `-f`, `--fast` | No | Mode image rapide obsolète. |
| `-y`, `--yes` | No | Confirmer automatiquement les invites, utile en CI. |
| `--repo-url` | No | URL du dépôt utilisée dans le conseil sparse-checkout du tableau des langues du README. |
| `--migrate-language-folders` | No | Renommer les dossiers d'alias hérités, tels que `cn` ou `tw`, en dossiers canoniques BCP 47. |
| `--dry-run` | No | Prévisualiser la migration des dossiers de langue et les estimations de traduction sans écrire de fichiers. |

Si aucun indicateur de type n'est fourni, `translate` traite le Markdown, les notebooks et les images. La traduction d'images nécessite la configuration Azure AI Vision.

## evaluate

Évaluer la qualité des Markdown traduits pour une langue.

!!! warning "Experimental"
    `evaluate` is experimental. It can use rule-based and LLM-based quality checks, writes evaluation results into translation metadata, and its scoring model and metadata behavior may change.

```bash
evaluate -l "ko"
```

### Exemples courants

Utiliser un seuil de faible confiance plus strict :

```bash
evaluate -l "es" -c 0.8
```

Exécuter uniquement des contrôles basés sur des règles :

```bash
evaluate -l "fr" -f
```

Exécuter uniquement des contrôles basés sur des LLM :

```bash
evaluate -l "ja" -D
```

### Options

| Option | Requis | Description |
| --- | --- | --- |
| `-l`, `--language-code` | Yes | Code de langue unique à évaluer. Les codes d'alias sont normalisés. |
| `-r`, `--root-dir` | No | Racine du projet. Par défaut le répertoire courant. |
| `-c`, `--min-confidence` | No | Seuil utilisé pour lister les traductions à faible confiance. Par défaut `0.7`. |
| `-d`, `--debug` | No | Activer les logs de débogage. |
| `-s`, `--save-logs` | No | Enregistrer les logs de niveau DEBUG sous `<root-dir>/logs/`. |
| `-f`, `--fast` | No | Évaluation basée uniquement sur des règles. |
| `-D`, `--deep` | No | Évaluation basée uniquement sur des LLM. |

Par défaut, `evaluate` utilise à la fois l'évaluation basée sur des règles et celle basée sur des LLM. Les résultats sont écrits dans les métadonnées de traduction et résumés dans la console.

## co-op-review

Exécuter des vérifications déterministes de maintenance de traduction sans informations d'identification API.

!!! note "Beta"
    `co-op-review` is a beta deterministic review command. It does not call model providers or write files, but its checks and issue output schema may evolve.

```bash
co-op-review -l "ko"
```

### Exemples courants

Vérifier les traductions coréennes et japonaises depuis le répertoire courant :

```bash
co-op-review -l "ko ja"
```

Vérifier une racine de projet spécifique :

```bash
co-op-review -l "fr" -r ./my-course
```

Vérifier uniquement les fichiers source modifiés par rapport à une référence de base :

```bash
co-op-review -l "ko" --changed-from origin/main
```

Afficher la sortie au format Markdown GitHub-flavored pour des résumés CI :

```bash
co-op-review -l "ko ja" --changed-from origin/main --format github
```

### Options

| Option | Requis | Description |
| --- | --- | --- |
| `-l`, `--language-code` | No | Code de langue à examiner. Peut être passé plusieurs fois ou en tant que valeur séparée par des espaces. Par défaut, toutes les langues de traduction découvertes. |
| `-r`, `--root-dir` | No | Racine du projet. Par défaut le répertoire courant. |
| `--changed-from` | No | Référence Git utilisée pour limiter la revue aux fichiers source modifiés. |
| `--format` | No | Format de sortie : `text` ou `github`. Par défaut `text`. |

`co-op-review` vérifie actuellement les fichiers traduits manquants, les métadonnées de traduction manquantes ou obsolètes, l'intégrité du frontmatter Markdown et des blocs de code, le JSON invalide des notebooks traduits et les cibles locales de liens Markdown ou image manquantes. Les liens manquants sont des avertissements par défaut ; les problèmes de structure et de fraîcheur font échouer la commande.

## co-op-translator-mcp

Exécuter le serveur MCP de Co-op Translator pour les agents, éditeurs et clients compatibles MCP.

```bash
co-op-translator-mcp
```

Le transport par défaut est `stdio`. Consultez le guide [MCP Server](mcp.md) pour la configuration des clients, les outils, les ressources et les notes de sécurité.

### Options

| Option | Requis | Description |
| --- | --- | --- |
| `--transport` | No | Transport MCP : `stdio`, `streamable-http`, ou `sse`. Par défaut `stdio`. |

## migrate-links

Reprocesser les fichiers Markdown traduits et mettre à jour les liens des notebooks afin qu'ils pointent vers les notebooks traduits lorsque ceux-ci sont disponibles.

```bash
migrate-links -l "ko ja"
```

### Exemples courants

Prévisualiser les mises à jour des liens :

```bash
migrate-links -l "ko" --dry-run
```

Traiter toutes les langues prises en charge sans confirmation :

```bash
migrate-links -l "all" -y
```

Réécrire les liens uniquement lorsque des notebooks traduits existent :

```bash
migrate-links -l "ko" --no-fallback-to-original
```

### Options

| Option | Requis | Description |
| --- | --- | --- |
| `-l`, `--language-codes` | Yes | Codes de langue séparés par des espaces, ou `"all"`. |
| `-r`, `--root-dir` | No | Racine du projet. Par défaut le répertoire courant. |
| `--image-dir` | No | Répertoire des images traduites relatif à la racine. Par défaut `translated_images`. |
| `--dry-run` | No | Afficher les fichiers qui changeraient sans écrire de mises à jour. |
| `--fallback-to-original`, `--no-fallback-to-original` | No | Utiliser les liens de notebook originaux lorsque les notebooks traduits sont manquants. Activé par défaut. |
| `-d`, `--debug` | No | Activer les logs de débogage. |
| `-s`, `--save-logs` | No | Enregistrer les logs de niveau DEBUG sous `<root-dir>/logs/`. |
| `-y`, `--yes` | No | Confirmer automatiquement les invites lors du traitement de toutes les langues. |

## Environment

Toutes les commandes nécessitent un fournisseur LLM configuré :

```bash
# Azure OpenAI
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"

# Ou OpenAI
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

La traduction d'images nécessite en outre Azure AI Vision :

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

## Output layout

Les traductions textuelles sont écrites sous :

```text
translations/<language-code>/<original-path>
```

Les images traduites sont écrites sous :

```text
translated_images/<language-code>/<original-path>
```

Par exemple, traduire `README.md` et `docs/setup.md` en coréen produit :

```text
translations/ko/README.md
translations/ko/docs/setup.md
```

## Copy-Paste CLI Examples

Traduire le Markdown en trois langues :

```bash
translate -l "ko ja fr" -md
```

Traduire uniquement les notebooks :

```bash
translate -l "zh-CN" -nb
```

Traduire uniquement les images :

```bash
translate -l "pt-BR" -img
```

Aperçu de la traduction Markdown sans écrire de fichiers :

```bash
translate -l "de es" -md --dry-run
```

Réparer les traductions Markdown à faible confiance :

```bash
evaluate -l "ko" -c 0.8
translate -l "ko" --fix -c 0.8 -md
```

Exécution de la traduction Markdown adaptée à la CI :

```bash
translate -l "ko ja" -md -y -s
```

Vérifier la sortie traduite :

```bash
co-op-review -l "ko ja"
```

Aperçu de la migration des liens :

```bash
migrate-links -l "ko" --dry-run
```