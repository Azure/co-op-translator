# Choisissez votre flux de travail

Co-op Translator peut être utilisé de trois manières : la CLI, l'API Python et le serveur MCP. Ils partagent les mêmes capacités de traduction, mais chacun correspond à un flux de travail différent.

Utilisez cette page lorsque vous décidez par où commencer.

**Si vous modifiez les traductions manuellement :** les workflows CLI et Actions par défaut retransluisent les fichiers source modifiés dans leur intégralité, donc vos formulations dans ces fichiers peuvent être écrasées. Examinez le diff avant d'accepter une mise à jour. Pour la préservation au niveau des blocs Markdown des modifications acceptées, utilisez le fournisseur d'état de traduction facultatif de l'[API Python](api.md#preserve-accepted-human-edits-with-a-translation-state-provider).

## Décision rapide

| Si vous voulez... | Utiliser | Commencez ici |
| --- | --- | --- |
| Traduire ou réviser un dépôt depuis un terminal | CLI | [Référence CLI](cli.md) |
| Ajouter la traduction à un script Python, un service, un notebook ou une tâche CI | API Python | [API Python](api.md) |
| Laisser un agent, un éditeur ou un client compatible MCP traduire le contenu pour vous | Serveur MCP | [Serveur MCP](mcp.md) |
| Traduire un document Markdown, un notebook ou une image que votre application a déjà chargé | API Python ou Serveur MCP | [API Python](api.md) ou [Serveur MCP](mcp.md) |
| Traduire un dépôt entier avec des dossiers de sortie standard et des métadonnées | CLI ou `run_translation` | [Référence CLI](cli.md) ou [API Python](api.md) |

## Utilisez la CLI lorsque

Choisissez la CLI lorsqu'une personne ou une tâche CI pilote la traduction du dépôt depuis un shell.

La CLI est la voie la plus directe lorsque vous voulez que Co-op Translator découvre les fichiers du projet, crée des sorties traduites, préserve la structure du projet, mette à jour les métadonnées et exécute des commandes de revue.

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -md -nb
co-op-review -l "ko"
migrate-links -l "ko" --dry-run
```

Cet exemple traduit Markdown et notebooks. Ajoutez `-img` uniquement après avoir configuré [Azure AI Vision](configuration.md#azure-ai-vision). Pour une première exécution uniquement Markdown, suivez [Votre première traduction](first-translation.md).

Convient bien pour :

- Vous traduisez un dépôt depuis votre terminal.
- Vous voulez une commande reproductible pour les workflows CI ou de publication.
- Vous souhaitez la découverte de projet intégrée, des chemins de sortie, des métadonnées, le nettoyage et la revue.
- Vous préférez une interface en ligne de commande plutôt que d'écrire du code Python.

## Utilisez l'API Python lorsque

Choisissez l'API Python lorsque votre propre code doit contrôler le flux de travail.

L'API est utile pour les applications, scripts d'automatisation, notebooks, services et pipelines personnalisés. Elle vous permet d'appeler des API de traduction de contenu de bas niveau pour des fichiers individuels, ou d'exécuter la même orchestration au niveau du dépôt utilisée par la CLI.

Traduisez un document Markdown et décidez où l'enregistrer :

```python
import asyncio
from pathlib import Path

from co_op_translator.api import rewrite_markdown_paths, translate_markdown_content


async def main() -> None:
    source_path = Path("docs/guide.md")
    target_path = Path("translations/ko/docs/guide.md")

    translated = await translate_markdown_content(
        source_path.read_text(encoding="utf-8"),
        "ko",
        {"source_path": source_path},
    )

    rewritten = rewrite_markdown_paths(
        translated,
        source_path=source_path,
        target_path=target_path,
    )

    target_path.parent.mkdir(parents=True, exist_ok=True)
    target_path.write_text(rewritten, encoding="utf-8")


asyncio.run(main())
```

Exécutez une traduction de dépôt depuis Python :

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    notebook=True,
    images=False,
    dry_run=True,
)
```

Convient bien pour :

- Votre application lit déjà des fichiers, des tampons (buffers), des notebooks ou des octets d'image.
- Vous avez besoin d'une validation, d'un stockage, de la journalisation, de reprises ou de flux d'approbation personnalisés.
- Vous souhaitez traduire un seul document, notebook ou image sans traiter l'ensemble du dépôt.
- Vous voulez la traduction du dépôt, mais depuis une automatisation Python plutôt qu'une commande shell.

## Utilisez le serveur MCP lorsque

Choisissez le serveur MCP lorsqu'un agent, un éditeur ou un client compatible MCP doit appeler les outils Co-op Translator.

Dans la configuration locale normale, l'utilisateur ne garde pas manuellement un serveur en cours d'exécution. Le client MCP démarre `co-op-translator-mcp` via `stdio` lorsqu'il a besoin des outils.

Exemples de requêtes utilisateur qu'un agent pourrait traiter :

- "Traduire ce fichier Markdown en coréen et garder les liens corrects."
- "Traduire ce fichier Markdown en coréen avec le workflow MCP assisté par agent, en utilisant votre propre modèle pour les fragments traduits."
- "Traduire ce notebook en coréen, préserver les cellules de code et utiliser Co-op Translator MCP pour reconstruire le notebook."
- "Traduire le texte de cette image en japonais et enregistrer le résultat."
- "Simuler (dry-run) une traduction de dépôt en espagnol et me dire ce qui changerait."
- "Vérifier si la sortie de la traduction en coréen est à jour."

Pour le Markdown et les notebooks, MCP peut fonctionner en deux modes :

| Mode | À utiliser lorsque | Outils principaux |
| --- | --- | --- |
| Assisté par un agent | L'agent hôte MCP doit traduire les fragments avec son propre modèle, sans les identifiants de fournisseur LLM de Co-op Translator. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Appuyé par un fournisseur | Co-op Translator doit appeler Azure OpenAI, OpenAI ou Anthropic directement. | `translate_markdown_content`, `translate_notebook_content` |

Format d'appel de l'outil Markdown en mode fournisseur MCP :

```json
{
  "tool": "translate_markdown_content",
  "arguments": {
    "document": "# Setup\n\nInstall Co-op Translator first.",
    "language_code": "ko",
    "options": {
      "source_path": "docs/setup.md"
    }
  }
}
```

Format d'appel de l'outil image MCP :

```json
{
  "tool": "translate_image_content",
  "arguments": {
    "image_path": "assets/architecture.png",
    "language_code": "ko",
    "output_path": "translated_images/ko/assets/architecture.png"
  }
}
```

La traduction de dépôt est en mode simulation (dry-run) par défaut via MCP :

```json
{
  "tool": "run_translation",
  "arguments": {
    "language_codes": ["ko"],
    "translate_markdown": true,
    "translate_notebooks": true,
    "translate_images": false,
    "dry_run": true
  }
}
```

Convient bien pour :

- Vous souhaitez des workflows de traduction en langage naturel intégrés à un agent ou un éditeur.
- Vous voulez la traduction de Markdown ou de notebooks où le modèle de l'agent hôte traduit des fragments préparés.
- Vous voulez que l'agent traduise du contenu sélectionné plutôt que l'ensemble du dépôt.
- Vous souhaitez une étape d'approbation avant les écritures à l'échelle du dépôt.
- Vous voulez une interface unique qui expose des outils pour Markdown, notebooks, images, révision et réécriture de chemins.

## Comment ils s'intègrent

La CLI est la meilleure option par défaut pour les personnes traduisant des dépôts. L'API Python est préférable lorsque votre code contrôle le flux de travail. Le serveur MCP est préférable lorsque c'est un agent ou un éditeur qui contrôle le flux de travail.

Les trois voies utilisent la même API publique Co-op Translator, vous pouvez donc commencer avec la CLI, automatiser ensuite avec Python, et exposer les mêmes capacités aux clients MCP lorsque vous avez besoin de workflows pilotés par agent.