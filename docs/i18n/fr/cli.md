# Référence CLI

Co-op Translator installe ces points d'entrée en ligne de commande :

- `translate`
- `evaluate`
- `migrate-links`
- `co-op-review`
- `co-op-translator-mcp`

Les commandes `translate`, `evaluate`, `migrate-links` et `co-op-review` transmettent via `co_op_translator.__main__`, qui sélectionne l'implémentation de la commande en fonction du nom du script invoqué. Le serveur MCP utilise directement `co_op_translator.mcp.server`.

Si vous hésitez entre l'interface CLI, l'API Python et MCP, commencez par [Choisir votre flux de travail](workflows.md).

## Sortie de la console

Les terminaux interactifs utilisent le formatage Rich pour l'en-tête de commande, la progression et les synthèses. Les sorties CI et non interactives reviennent automatiquement au texte brut.

Définissez `CO_OP_TRANSLATOR_OUTPUT_STYLE=plain` pour forcer la sortie en texte brut, ou `CO_OP_TRANSLATOR_OUTPUT_STYLE=rich` pour forcer la sortie Rich. Définissez `CO_OP_TRANSLATOR_NO_PROGRESS=1` pour conserver les synthèses tout en supprimant les barres de progression en direct.

Utilisez `translate --json-events progress.ndjson` lorsqu'un autre système a besoin
d'une progression lisible par machine. La CLI continue d'afficher une sortie destinée aux humains, tandis que
le fichier NDJSON reçoit des événements versionnés `co-op.translation.event.v1` avec
des champs stables tels que `type`, `stage_key`, `completed`, `total` et
`current_path`.

## Flux de première utilisation de la CLI

Commencez ici si vous utilisez Co-op Translator depuis un terminal :

1. Configurez un fournisseur LLM comme décrit dans [Configuration](configuration.md).
2. Choisissez le type de contenu que vous souhaitez traduire.
3. Exécutez d'abord une commande ciblée, par exemple la traduction uniquement de Markdown.
4. Utilisez `--dry-run` avant des modifications importantes du dépôt.
5. Utilisez `co-op-review` après la traduction pour vérifier la structure et la fraîcheur.

| Objectif | Commande pour commencer |
| --- | --- |
| Traduire des documents Markdown | `translate -l "ko" -md` |
| Traduire des notebooks | `translate -l "ko" -nb` |
| Traduire le texte des images | `translate -l "ko" -img` |
| Prévisualiser le travail sans écrire de fichiers | `translate -l "ko" -md --dry-run` |
| Vérifier les traductions existantes | `co-op-review -l "ko"` |
| Mettre à jour les liens des notebooks et Markdown | `migrate-links -l "ko" --dry-run` |
| Exposer des outils à un client MCP | Configurez le [Serveur MCP](mcp.md) au lieu d'exécuter les commandes CLI directement. |

## translate

Traduire des fichiers Markdown, des notebooks et le texte des images vers une ou plusieurs langues cibles.

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

Enregistrer les journaux :

```bash
translate -l "ko" -s
```

Écrire des événements de progression structurés :

```bash
translate -l "ko ja" -md --json-events progress.ndjson
```

### Options

| Option | Requis | Description |
| --- | --- | --- |
| `-l`, `--language-codes` | Oui | Codes de langue séparés par des espaces, tels que `"es fr de"`, ou `"all"`. |
| `-r`, `--root-dir` | Non | Racine du projet. Par défaut le répertoire courant. |
| `-u`, `--update` | Non | Supprime les traductions existantes pour les langues sélectionnées et les recrée. |
| `-img`, `--images` | Non | Traduire uniquement les fichiers image. |
| `-md`, `--markdown` | Non | Traduire uniquement les fichiers Markdown. |
| `-nb`, `--notebook` | Non | Traduire uniquement les fichiers Jupyter notebook. |
| `-d`, `--debug` | Non | Activer la journalisation de débogage dans la console. |
| `-s`, `--save-logs` | Non | Enregistrer les journaux de niveau DEBUG sous `<root-dir>/logs/`. |
| `--json-events` | Non | Écrire des événements de progression de traduction lisibles par machine au format NDJSON. |
| `-x`, `--fix` | Non | Retraduire les fichiers Markdown à faible confiance en se basant sur les résultats d'évaluations précédentes. |
| `-c`, `--min-confidence` | Non | Seuil de confiance pour `--fix`. Par défaut `0.7`. |
| `--add-disclaimer`, `--no-disclaimer` | Non | Ajouter ou supprimer les mentions d'avertissement de traduction automatique. Activé par défaut dans la CLI. |
| `-f`, `--fast` | Non | Mode image rapide obsolète. |
| `-y`, `--yes` | Non | Confirmer automatiquement les invites, utile en CI. |
| `--repo-url` | Non | URL du dépôt utilisée dans le conseil de sparse-checkout du tableau des langues du README. |
| `--migrate-language-folders` | Non | Renommer les dossiers d'alias legacy, tels que `cn` ou `tw`, vers les dossiers canoniques BCP 47. |
| `--dry-run` | Non | Prévisualiser la migration des dossiers de langue et les estimations de traduction sans écrire de fichiers. |

Si aucun indicateur de type n'est fourni, `translate` traite le Markdown, les notebooks et les images. La traduction d'images nécessite une configuration Azure AI Vision.

## evaluate

Évaluer la qualité des traductions Markdown pour une langue.

!!! warning "Expérimental"
    `evaluate` est expérimental. Il peut utiliser des contrôles de qualité basés sur des règles et sur des LLM, écrit les résultats d'évaluation dans les métadonnées de traduction, et son modèle de notation et le comportement des métadonnées peuvent évoluer.

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
| `-l`, `--language-code` | Oui | Code de langue unique à évaluer. Les codes alias sont normalisés. |
| `-r`, `--root-dir` | Non | Racine du projet. Par défaut le répertoire courant. |
| `-c`, `--min-confidence` | Non | Seuil utilisé lors de la liste des traductions à faible confiance. Par défaut `0.7`. |
| `-d`, `--debug` | Non | Activer la journalisation de débogage. |
| `-s`, `--save-logs` | Non | Enregistrer les journaux de niveau DEBUG sous `<root-dir>/logs/`. |
| `-f`, `--fast` | Non | Évaluation basée uniquement sur des règles. |
| `-D`, `--deep` | Non | Évaluation basée uniquement sur des LLM. |

Par défaut, `evaluate` utilise à la fois l'évaluation basée sur des règles et sur des LLM. Les résultats sont écrits dans les métadonnées de traduction et résumés dans la console.

## co-op-review

Exécutez des vérifications déterministes de maintenance de traduction sans identifiants d'API.

!!! note "Bêta"
    `co-op-review` est une commande de revue déterministe en bêta. Elle n'appelle pas de fournisseurs de modèles ni n'écrit de fichiers, mais ses contrôles et son schéma de sortie des problèmes peuvent évoluer.

```bash
co-op-review -l "ko"
```

### Exemples courants

Vérifier les traductions coréenne et japonaise depuis le répertoire courant :

```bash
co-op-review -l "ko ja"
```

Vérifier une racine de projet spécifique :

```bash
co-op-review -l "fr" -r ./my-course
```

Vérifier uniquement le README après une traduction uniquement du README :

```bash
translate -l "ko" --readme-only -y
co-op-review -l "ko" --readme-only --format github
```

`--readme-only` ignore les autres documents et les README imbriqués. Il échoue si le README racine
`README.md` est manquant. Combiné avec `--changed-from`, il n'examine que le README
lorsque ce fichier source a changé. La traduction README-only laisse le README source
inchangé, y compris tous les marqueurs de section partagée.

Vérifier uniquement les fichiers source modifiés par rapport à une référence de base :

```bash
co-op-review -l "ko" --changed-from origin/main
```

Afficher une sortie Markdown au format GitHub pour les résumés CI :

```bash
co-op-review -l "ko ja" --changed-from origin/main --format github
```

### Options

| Option | Requis | Description |
| --- | --- | --- |
| `-l`, `--language-code` | Non | Code de langue à vérifier. Peut être passé plusieurs fois ou comme valeur séparée par des espaces. Par défaut, toutes les langues de traduction découvertes. |
| `-r`, `--root-dir` | Non | Racine du projet. Par défaut le répertoire courant. |
| `--changed-from` | Non | Référence Git utilisée pour limiter la revue aux fichiers source modifiés. |
| `--readme-only` | Non | Vérifier uniquement la traduction du `README.md` racine. |
| `--format` | Non | Format de sortie : `text` ou `github`. Par défaut `text`. |

`co-op-review` vérifie actuellement les fichiers traduits manquants, les métadonnées de traduction manquantes ou obsolètes, l'intégrité du frontmatter Markdown et des balises de code, le JSON de notebook traduit invalide, et les cibles de liens Markdown ou image locales manquantes. Les liens manquants sont des avertissements par défaut ; les problèmes de structure et de fraîcheur entraînent l'échec de la commande.

## co-op-translator-mcp

Exécutez le serveur MCP de Co-op Translator pour les agents, éditeurs et clients compatibles MCP.

```bash
co-op-translator-mcp
```

Le transport par défaut est `stdio`. Consultez le guide [Serveur MCP](mcp.md) pour la configuration des clients, les outils, les ressources et les notes de sécurité.

### Options

| Option | Requis | Description |
| --- | --- | --- |
| `--transport` | Non | Transport MCP: `stdio`, `streamable-http`, ou `sse`. Par défaut `stdio`. |

## migrate-links

Retraiter les fichiers Markdown traduits et mettre à jour les liens des notebooks afin qu'ils pointent vers des notebooks traduits lorsque ceux-ci sont disponibles.

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

Ne réécrire les liens que lorsque des notebooks traduits existent :

```bash
migrate-links -l "ko" --no-fallback-to-original
```

### Options

| Option | Requis | Description |
| --- | --- | --- |
| `-l`, `--language-codes` | Oui | Codes de langue séparés par des espaces, ou `"all"`. |
| `-r`, `--root-dir` | Non | Racine du projet. Par défaut le répertoire courant. |
| `--image-dir` | Non | Répertoire des images traduites relatif à la racine. Par défaut `translated_images`. |
| `--dry-run` | Non | Afficher les fichiers qui changeraient sans écrire de mises à jour. |
| `--fallback-to-original`, `--no-fallback-to-original` | Non | Utiliser les liens de notebook originaux lorsque les notebooks traduits sont manquants. Activé par défaut. |
| `-d`, `--debug` | Non | Activer la journalisation de débogage. |
| `-s`, `--save-logs` | Non | Enregistrer les journaux de niveau DEBUG sous `<root-dir>/logs/`. |
| `-y`, `--yes` | Non | Confirmer automatiquement les invites lors du traitement de toutes les langues. |

## Environnement

Lorsqu'une commande nécessite des identifiants de fournisseur, configurez un de ces ensembles de fournisseurs. `translate --dry-run` et `co-op-review` ne nécessitent pas d'identifiants de fournisseur :

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

# Ou Anthropic
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

La traduction d'images nécessite en outre Azure AI Vision :

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

## Disposition de la sortie

Les traductions textuelles sont écrites sous :

```text
translations/<language-code>/<original-path>
```

La sortie des images traduites est écrite sous :

```text
translated_images/<language-code>/<original-path>
```

Par exemple, la traduction de `README.md` et `docs/setup.md` en coréen produit :

```text
translations/ko/README.md
translations/ko/docs/setup.md
```

## Exemples CLI à copier-coller

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

Prévisualiser la traduction Markdown sans écrire de fichiers :

```bash
translate -l "de es" -md --dry-run
```

Réparer les traductions Markdown à faible confiance :

```bash
evaluate -l "ko" -c 0.8
translate -l "ko" --fix -c 0.8 -md
```

Exécuter une traduction Markdown adaptée au CI :

```bash
translate -l "ko ja" -md -y -s
```

Vérifier la sortie traduite :

```bash
co-op-review -l "ko ja"
```

Prévisualiser la migration des liens :

```bash
migrate-links -l "ko" --dry-run
```