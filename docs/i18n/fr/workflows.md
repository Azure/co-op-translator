# Choisissez votre flux de travail

Co-op Translator peut être utilisé de trois manières : la CLI, l'API Python et le serveur MCP. Ils partagent les mêmes capacités de traduction, mais chacun convient à un flux de travail différent.

Utilisez cette page lorsque vous décidez par où commencer.

## Décision rapide

| Si vous voulez... | Utiliser | Commencez ici |
| --- | --- | --- |
| Traduire ou relire un dépôt depuis un terminal | CLI | [CLI Reference](cli.md) |
| Ajouter la traduction à un script Python, un service, un notebook ou une tâche CI | Python API | [Python API](api.md) |
| Laisser un agent, un éditeur ou un client compatible MCP traduire du contenu pour vous | MCP Server | [MCP Server](mcp.md) |
| Traduire un seul document Markdown, notebook ou image que votre application a déjà chargé | API Python ou Serveur MCP | [Python API](api.md) ou [MCP Server](mcp.md) |
| Traduire un dépôt entier avec des dossiers de sortie standard et des métadonnées | CLI ou `run_translation` | [CLI Reference](cli.md) ou [Python API](api.md) |

## Utilisez la CLI lorsque

Choisissez la CLI lorsqu'une personne ou une tâche CI pilote la traduction du dépôt depuis un shell.

La CLI est le chemin le plus direct lorsque vous voulez que Co-op Translator découvre les fichiers du projet, crée des sorties traduites, préserve la disposition du projet, mette à jour les métadonnées et exécute des commandes de révision.

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -md -nb -img
co-op-review -l "ko" -md -nb
migrate-links -l "ko" --dry-run
```

Convient pour :

- Vous traduisez un dépôt depuis votre terminal.
- Vous voulez une commande reproductible pour les workflows CI ou de publication.
- Vous souhaitez la découverte de projet intégrée, les chemins de sortie, les métadonnées, le nettoyage et la révision.
- Vous préférez une interface en ligne de commande plutôt que d'écrire du code Python.

## Utilisez l'API Python lorsque

Choisissez l'API Python lorsque votre propre code doit contrôler le flux de travail.

L'API est utile pour les applications, les scripts d'automatisation, les notebooks, les services et les pipelines personnalisés. Elle vous permet d'appeler des API de traduction de contenu bas niveau pour des fichiers individuels, ou d'exécuter la même orchestration au niveau du dépôt utilisée par la CLI.

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
import asyncio

from co_op_translator.api import run_translation


async def main() -> None:
    await run_translation(
        language_codes=["ko"],
        translate_markdown=True,
        translate_notebooks=True,
        translate_images=False,
        dry_run=True,
    )


asyncio.run(main())
```

Convient pour :

- Votre application lit déjà des fichiers, des buffers, des notebooks ou des octets d'image.
- Vous avez besoin de validations personnalisées, de stockage, de journalisation, de réessais ou de flux d'approbation.
- Vous voulez traduire un seul document, notebook ou image sans traiter l'ensemble du dépôt.
- Vous souhaitez la traduction du dépôt, mais depuis une automatisation Python plutôt qu'une commande shell.

## Utilisez le serveur MCP lorsque

Choisissez le serveur MCP lorsqu'un agent, un éditeur ou un client compatible MCP doit appeler les outils Co-op Translator.

Dans la configuration locale normale, l'utilisateur ne garde pas manuellement un serveur en cours d'exécution. Le client MCP lance `co-op-translator-mcp` via `stdio` lorsqu'il a besoin des outils.

Exemples de demandes utilisateur qu'un agent pourrait traiter :

- "Traduisez ce fichier Markdown en coréen et conservez les liens corrects."
- "Traduisez ce fichier Markdown en coréen avec le flux de travail MCP assisté par agent, en utilisant votre propre modèle pour les segments traduits."
- "Traduisez ce notebook en coréen, conservez les cellules de code et utilisez Co-op Translator MCP pour reconstruire le notebook."
- "Traduisez le texte de cette image en japonais et enregistrez le résultat."
- "Effectuez une simulation d'une traduction de dépôt en espagnol et dites-moi ce qui changerait."
- "Vérifiez si la sortie de la traduction coréenne est à jour."

Pour les fichiers Markdown et les notebooks, le MCP peut fonctionner en deux modes :

| Mode | Utilisez lorsque | Principaux outils |
| --- | --- | --- |
| Agent-assisted | L'agent hôte MCP devrait traduire des segments avec son propre modèle, sans les identifiants du fournisseur LLM de Co-op Translator. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Provider-backed | Co-op Translator doit appeler Azure OpenAI ou OpenAI directement. | `translate_markdown_content`, `translate_notebook_content` |

Forme d'appel de l'outil Markdown pour MCP appuyé par un fournisseur :

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

Forme d'appel de l'outil image MCP :

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

La traduction de dépôt est par défaut effectuée en mode simulation via MCP :

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

Convient pour :

- Vous voulez des workflows de traduction en langage naturel au sein d'un agent ou d'un éditeur.
- Vous souhaitez la traduction de Markdown ou de notebooks où le modèle de l'agent hôte traduit des segments préparés.
- Vous voulez que l'agent traduise du contenu sélectionné au lieu d'un dépôt entier.
- Vous voulez une étape d'approbation avant les écritures sur l'ensemble du dépôt.
- Vous souhaitez une interface unique exposant des outils pour Markdown, notebook, image, révision et réécriture de chemins.

## Comment ils s'articulent

La CLI est le meilleur choix par défaut pour les personnes qui traduisent des dépôts. L'API Python est préférable lorsque votre code contrôle le flux de travail. Le serveur MCP est préférable lorsque un agent ou un éditeur contrôle le flux de travail.

Les trois chemins utilisent la même API publique Co-op Translator, vous pouvez donc commencer avec la CLI, automatiser avec Python plus tard et exposer les mêmes capacités aux clients MCP lorsque vous avez besoin de flux de travail pilotés par des agents.