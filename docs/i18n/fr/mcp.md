# Serveur MCP

Co-op Translator inclut un serveur Model Context Protocol pour les agents, éditeurs et clients compatibles MCP.

Pour la configuration locale par défaut, les utilisateurs n'exécutent pas un serveur séparé manuellement. Ils configurent leur client MCP, et le client lance automatiquement `co-op-translator-mcp` via `stdio` lorsqu'il a besoin des outils Co-op Translator.

Si vous hésitez entre l'interface en ligne de commande, l'API Python et MCP, commencez par [Choisissez votre flux de travail](workflows.md).

Utilisez MCP lorsqu'un agent ou un éditeur doit appeler Co-op Translator directement :

| Objectif utilisateur | Outils MCP |
| --- | --- |
| Traduire un document Markdown, un notebook ou une image | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content` |
| Traduire du contenu Markdown ou de notebook avec le modèle de l'agent hôte | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Réécrire les liens Markdown ou notebook traduits après avoir choisi le chemin de sortie | `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Traduire un dépôt entier comme avec la CLI | `run_translation`, `translate_project` |
| Examiner la sortie traduite sans identifiants LLM | `run_review` |
| Inspecter les capacités et l'état de l'environnement | `get_api_overview`, `list_supported_languages`, `get_configuration_status` |

Le serveur MCP encapsule la même API publique Python documentée dans [Python API](api.md). Les outils basés sur un fournisseur utilisent les mêmes fournisseurs configurés que la CLI et l'API Python. Les outils assistés par un agent préparent des fragments pour que l'agent hôte MCP les traduise, puis utilisent Co-op Translator pour reconstruire le Markdown ou le notebook final.

## Étape 1 : Installer et configurer Co-op Translator

Installez Co-op Translator dans l'environnement Python que votre client MCP utilisera :

```bash
pip install co-op-translator
```

Pour le développement local à partir de ce dépôt, installez le paquet en mode modifiable :

```bash
pip install -e .
```

Choisissez le mode de traduction que votre client MCP utilisera :

| Mode | À utiliser pour | Identifiants |
| --- | --- | --- |
| Basé sur un fournisseur | Co-op Translator appelle `translate_markdown_content`, `translate_notebook_content`, `translate_image_content` ou `run_translation`. | La traduction nécessite Azure OpenAI, OpenAI ou Anthropic. La traduction d'images nécessite également Azure AI Vision. |
| Assisté par un agent | L'agent hôte MCP traduit les fragments retournés par `start_markdown_agent_translation` ou `start_notebook_agent_translation`. | Aucune information d'identification de fournisseur LLM pour Co-op Translator n'est requise pour les fragments Markdown ou notebook. La traduction d'images n'est pas encore couverte par le mode assisté par agent. |

Si vous commencez par la traduction de Markdown ou de notebooks à l'intérieur d'un agent comme Codex ou Claude Code, commencez par le mode assisté par agent. Utilisez le mode basé sur un fournisseur lorsque vous souhaitez que Co-op Translator appelle lui-même vos fournisseurs configurés, lorsque vous traduisez des images, ou lorsque vous exécutez une traduction au niveau du dépôt comme avec la CLI.

Configurez un fournisseur pour les flux de travail basés sur un fournisseur :

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

La traduction d'images basée sur un fournisseur nécessite en outre :

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

!!! note
    Le mode assisté par agent couvre actuellement le Markdown et les cellules Markdown des notebooks. La traduction d'images utilise toujours le pipeline d'images basé sur un fournisseur et nécessite Azure AI Vision pour l'OCR et le rendu prenant en compte la mise en page.

## Étape 2 : Configurez votre client MCP

Pour la configuration locale normale `stdio`, ajoutez Co-op Translator à la configuration de votre client MCP. Le client démarrera et arrêtera le processus automatiquement.

Configuration pour le paquet installé :

```json
{
  "mcpServers": {
    "co-op-translator": {
      "command": "co-op-translator-mcp",
      "args": []
    }
  }
}
```

Configuration du checkout source sur Windows :

```json
{
  "mcpServers": {
    "co-op-translator": {
      "command": "C:\\Users\\you\\dev\\co-op-translator\\.venv\\Scripts\\python.exe",
      "args": ["-m", "co_op_translator.mcp.server"],
      "cwd": "C:\\Users\\you\\dev\\co-op-translator"
    }
  }
}
```

Configuration du checkout de la source sur macOS ou Linux :

```json
{
  "mcpServers": {
    "co-op-translator": {
      "command": "/Users/you/dev/co-op-translator/.venv/bin/python",
      "args": ["-m", "co_op_translator.mcp.server"],
      "cwd": "/Users/you/dev/co-op-translator"
    }
  }
}
```

Après avoir modifié la configuration du client MCP, redémarrez ou rechargez le client afin qu'il puisse découvrir le nouveau serveur.

## Étape 3 : Vérifiez le serveur dans le client

Demandez au client MCP de lister les outils disponibles, ou appelez d'abord l'un des assistants en lecture seule :

```json
{
  "tool": "get_api_overview",
  "arguments": {}
}
```

Contrôles utiles à effectuer en premier :

| Outil | Que vérifier |
| --- | --- |
| `get_api_overview` | Confirme que le serveur est joignable et affiche les workflows disponibles. |
| `list_supported_languages` | Confirme que les données de langue empaquetées peuvent être chargées. |
| `get_configuration_status` | Confirme la disponibilité des fournisseurs LLM et Vision sans exposer de valeurs secrètes. |

## Étape 4 : Choisissez un flux de travail

### Traduire des fichiers ou documents individuels

Utilisez les outils de contenu basés sur un fournisseur lorsque le client MCP possède déjà le contenu du document ou le chemin de l'image et que Co-op Translator doit appeler les fournisseurs de traduction configurés.

Pour le Markdown :

1. Appelez `translate_markdown_content` avec `document`, `language_code`, et éventuellement `source_path`.
2. Si le résultat traduit doit être écrit dans une disposition de sortie Co-op Translator, appelez `rewrite_markdown_paths`.
3. Laissez le client écrire ou retourner le `content` final.

Pour les notebooks :

1. Appelez `translate_notebook_content` avec le JSON du notebook et `language_code`.
2. Appelez `rewrite_notebook_paths` si les liens traduits dans le notebook doivent être ajustés pour un chemin cible.
3. Écrivez ou retournez le JSON final du notebook.

Pour les images :

1. Appelez `translate_image_content` avec `image_path`, `language_code`, et éventuellement `root_dir` ou `fast_mode`.
2. Lisez le `data_base64` et le `mime_type` retournés.
3. Si `output_path` est fourni, l'image traduite est également enregistrée à cet emplacement.

Les outils de contenu n'effectuent pas la découverte de projet, les mises à jour des métadonnées, les avertissements, ni la réécriture automatique des chemins. Si vous souhaitez que l'agent hôte traduise des fragments Markdown ou de notebook sans identifiants de fournisseur LLM pour Co-op Translator, utilisez le flux de travail assisté par agent ci-dessous.

### Traduire avec le modèle de l'agent hôte

Utilisez les outils assistés par agent lorsque vous souhaitez que l'agent hôte MCP, comme un assistant de codage, produise le texte traduit plutôt que de configurer un fournisseur LLM pour Co-op Translator.

Dans un client MCP basé sur le chat, vous n'avez normalement pas besoin d'écrire vous-même le JSON d'outil. Demandez à l'agent d'utiliser le flux de travail assisté par agent :

```text
Translate this Markdown file to Korean with Co-op Translator MCP.
Use agent-assisted mode: call start_markdown_agent_translation, translate the returned chunks with your own model, then call finish_markdown_agent_translation.
Keep Markdown formatting, code blocks, and links intact.
```

Pour les notebooks, utilisez le même schéma :

```text
Translate this notebook to Korean with Co-op Translator MCP.
Use start_notebook_agent_translation, translate the returned Markdown-cell chunks with your own model, then call finish_notebook_agent_translation.
Preserve code cells, outputs, and notebook metadata.
```

Si votre client MCP prend en charge les invites serveur, utilisez `agent_assisted_markdown_translation_prompt` pour que le client charge les mêmes instructions de flux de travail.

Pour le Markdown :

1. Appelez `start_markdown_agent_translation` avec `document`, `language_code`, et éventuellement `source_path`.
2. Traduisez chaque fragment retourné dans l'agent hôte en suivant le `prompt` du fragment.
3. Appelez `finish_markdown_agent_translation` avec le `job` original et les fragments traduits en utilisant `chunk_id` et `translated_text`.
4. Si le contenu doit être écrit vers un chemin cible traduit, appelez `rewrite_markdown_paths`.

Pour les notebooks :

1. Appelez `start_notebook_agent_translation` avec le JSON du notebook et `language_code`.
2. Traduisez chaque fragment retourné dans l'agent hôte.
3. Appelez `finish_notebook_agent_translation` avec le `job` original et les fragments traduits.
4. Appelez `rewrite_notebook_paths` si les liens traduits du notebook nécessitent un ajustement du chemin cible.

Les outils assistés par agent n'appellent pas le fournisseur LLM configuré depuis Co-op Translator. L'agent hôte est responsable de la traduction des fragments retournés. Co-op Translator gère le découpage du Markdown, la préservation des espaces réservés, la reconstruction du frontmatter, le remplacement des cellules du notebook et la normalisation post-traduction.

### Traduire un dépôt entier

Utilisez `run_translation` lorsque l'utilisateur souhaite que Co-op Translator se comporte comme la CLI `translate`.

La traduction de dépôt est par défaut en `dry_run=true` afin qu'un agent puisse inspecter la portée avant les modifications de fichiers :

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "dry_run": true
}
```

Le résultat de `run_translation` inclut un tableau `events` avec des événements d'avancement versionnés
`co-op.translation.event.v1`. Les clients MCP devraient utiliser des champs
tels que `type`, `stage_key`, `completed`, `total`, et `current_path` au lieu de
analyser le texte capturé de la console. Passez `json_events_path` pour écrire aussi ces événements
dans un fichier NDJSON.

Pour autoriser les écritures, l'appelant doit définir à la fois `dry_run=false` et `confirm_write=true` :

```json
{
  "language_codes": "ko",
  "root_dir": ".",
  "markdown": true,
  "dry_run": false,
  "confirm_write": true
}
```

`translate_project` est exposé comme alias de compatibilité pour `run_translation`.

### Vérifier la sortie traduite

Utilisez `run_review` pour des vérifications déterministes qui ne nécessitent pas d'identifiants LLM ou Vision :

!!! note "Beta"
    MCP expose l'API beta `run_review`. Elle est sûre pour les flux de travail de relecture en lecture seule, mais les vérifications de relecture et les schémas d'incidents peuvent évoluer.

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "notebook": true
}
```

Le résultat inclut la sortie textuelle capturée et un résumé structuré de la relecture lorsque disponible.

## Exécutions manuelles du serveur

Les exécutions manuelles servent principalement au débogage ou aux transports qui se comportent comme des serveurs de longue durée.

Déboguez le serveur stdio par défaut :

```bash
co-op-translator-mcp
```

Exécuter depuis un checkout source :

```bash
python -m co_op_translator.mcp.server
```

Exécuter un serveur HTTP ou SSE de longue durée :

```bash
co-op-translator-mcp --transport streamable-http
co-op-translator-mcp --transport sse
```

Pour les intégrations d'éditeur local et d'agent, préférez la configuration `stdio` gérée par le client à l'étape 2.

## Outils

| Outil | But | Écrit des fichiers |
| --- | --- | --- |
| `translate_markdown_content` | Traduire une chaîne Markdown. | Non |
| `translate_notebook_content` | Traduire les cellules Markdown dans le JSON du notebook. | Non |
| `translate_image_content` | Traduire le texte dans une image et retourner les données image en base64. | Optionnel, uniquement lorsque `output_path` est fourni |
| `start_markdown_agent_translation` | Préparer des fragments Markdown pour que l'agent hôte les traduise sans identifiants LLM pour Co-op Translator. | Non |
| `finish_markdown_agent_translation` | Reconstruire le Markdown à partir des fragments traduits par l'agent hôte. | Non |
| `start_notebook_agent_translation` | Préparer des fragments de cellules Markdown du notebook pour l'agent hôte. | Non |
| `finish_notebook_agent_translation` | Reconstruire le JSON du notebook à partir des fragments traduits par l'agent hôte. | Non |
| `rewrite_markdown_paths` | Réécrire les chemins du corps Markdown et du frontmatter pour une cible traduite. | Non |
| `rewrite_notebook_paths` | Réécrire les chemins à l'intérieur des cellules Markdown du notebook. | Non |
| `run_translation` | Exécuter la traduction au niveau du projet comme la CLI. | Oui lorsque `dry_run=false` et `confirm_write=true` |
| `translate_project` | Alias de compatibilité pour `run_translation`. | Oui lorsque `dry_run=false` et `confirm_write=true` |
| `run_review` | Exécuter des vérifications de relecture déterministes. | Non |
| `get_configuration_status` | Signaler les fournisseurs LLM et Vision configurés sans exposer de secrets. | Non |
| `list_supported_languages` | Lister les codes de langues cibles pris en charge. | Non |
| `get_api_overview` | Décrire les workflows et outils MCP disponibles. | Non |

## Ressources

| URI de ressource | But |
| --- | --- |
| `co-op://api` | Aperçu JSON des workflows et outils. |
| `co-op://supported-languages` | Liste JSON des codes de langues pris en charge. |
| `co-op://configuration` | Résumé JSON de la disponibilité des fournisseurs sans secrets. |

## Invites

| Invite | But |
| --- | --- |
| `translate_markdown_document_prompt` | Guider un client MCP à travers la traduction du contenu plus la réécriture optionnelle des chemins. |
| `agent_assisted_markdown_translation_prompt` | Guider un client MCP pour la traduction Markdown par l'agent hôte sans identifiants de fournisseur LLM pour Co-op Translator. |
| `translate_repository_prompt` | Guider un client MCP à travers la traduction de dépôt en commençant par un dry-run. |

## Exemples à copier-coller

Traduire du contenu Markdown :

```json
{
  "tool": "translate_markdown_content",
  "arguments": {
    "document": "# Hello\n\nWelcome to the course.",
    "language_code": "ko",
    "source_path": "docs/guide.md"
  }
}
```

Réécrire les liens Markdown traduits :

```json
{
  "tool": "rewrite_markdown_paths",
  "arguments": {
    "content": "[Setup](../setup.md)\n\n![Hero](images/hero.png)",
    "source_path": "docs/guide.md",
    "target_path": "translations/ko/docs/guide.md",
    "policy": {
      "language_code": "ko",
      "root_dir": ".",
      "translations_dir": "translations",
      "translated_images_dir": "translated_images",
      "translation_types": ["markdown", "images"]
    }
  }
}
```

Traduire du Markdown avec le modèle de l'agent hôte :

```json
{
  "tool": "start_markdown_agent_translation",
  "arguments": {
    "document": "# Hello\n\nUse `pip install` to get started.",
    "language_code": "ko",
    "source_path": "docs/guide.md"
  }
}
```

Après que l'agent hôte ait traduit chaque fragment retourné, terminez le travail avec l'objet `job` complet retourné par `start_markdown_agent_translation` :

```text
tool: finish_markdown_agent_translation
arguments:
  job: <the full job object returned by start_markdown_agent_translation>
  translated_chunks:
    - chunk_id: body:1
      translated_text: "# 안녕하세요\n\n시작하려면 `pip install`을 사용하세요."
```

Aperçu de la traduction du dépôt :

```json
{
  "tool": "run_translation",
  "arguments": {
    "language_codes": "ko",
    "root_dir": ".",
    "markdown": true,
    "dry_run": true
  }
}
```

## Dépannage

| Problème | Que tenter |
| --- | --- |
| Le client MCP ne trouve pas `co-op-translator-mcp`. | Utilisez le chemin absolu de l'exécutable Python et la configuration de checkout source `["-m", "co_op_translator.mcp.server"]`. |
| Le serveur est listé mais la traduction échoue. | Appelez `get_configuration_status` et confirmez qu'un fournisseur LLM est disponible. |
| Vous souhaitez la traduction de Markdown ou de notebook sans identifiants de fournisseur. | Utilisez `start_markdown_agent_translation` / `finish_markdown_agent_translation` ou les équivalents pour notebook afin que l'agent hôte traduise les fragments. |
| La traduction d'images échoue. | Confirmez que les variables Azure AI Vision sont définies et appelez `get_configuration_status`. |
| La traduction du dépôt n'écrit pas de fichiers. | Définissez `dry_run=false` et `confirm_write=true` uniquement après approbation explicite de l'utilisateur. |
| Les modifications de la configuration du client n'apparaissent pas. | Redémarrez ou rechargez le client MCP. |

## Notes de sécurité

- Les appels d'outils MCP sont contrôlés par le modèle de l'application hôte, donc la traduction de dépôt est en dry-run par défaut.
- La traduction complète d'un dépôt peut créer, mettre à jour ou supprimer de nombreux fichiers. Exigez une approbation explicite de l'utilisateur avant de définir `confirm_write=true`.
- L'outil d'état de configuration ne renvoie jamais de clés API, d'endpoints, ou d'autres valeurs secrètes.
- La traduction d'images renvoie des données image en base64. Les images volumineuses peuvent produire de grandes réponses d'outil.
- Les outils assistés par agent renvoient les fragments sources et les invites à l'hôte MCP. Ne les utilisez qu'avec du contenu que l'utilisateur accepte d'envoyer à ce modèle d'agent hôte.