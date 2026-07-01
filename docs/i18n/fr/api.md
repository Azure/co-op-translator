# API Python

L'API Python publique stable est exportée depuis `co_op_translator.api`. La plupart des intégrations utilisent l'un de ces flux de travail :

| Scénario | À utiliser lorsque | API principales |
| --- | --- | --- |
| Traduire des fichiers ou documents individuels | Votre application lit le contenu source, appelle Co-op Translator pour la traduction, et décide où enregistrer le résultat. | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Préparer le contenu pour la traduction par un agent hôte | Votre MCP hôte ou modèle d'application traduira des morceaux, tandis que Co-op Translator gère le découpage et la reconstitution. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Traduire un dépôt entier | Vous voulez que l'API Python se comporte comme la CLI et gère la découverte, les chemins de sortie, les métadonnées, le nettoyage et les écritures. | `run_translation` |

La plupart des modules de bas niveau sous `core`, `config`, `review`, et `utils` sont des détails d'implémentation utilisés par ces points d'entrée API.

Les clients MCP utilisent la même API publique via le [MCP Server](mcp.md). Utilisez cette page lorsque vous appelez Python directement, et le guide MCP lorsque vous exposez Co-op Translator à un agent ou éditeur. Si vous hésitez entre CLI, API Python et MCP, commencez par [Choose Your Workflow](workflows.md).

## Flux initial de l'API

Commencez ici si vous appelez Co-op Translator depuis du code Python :

1. Configurez un fournisseur LLM comme décrit dans [Configuration](configuration.md), sauf si vous ne préparez que des morceaux Markdown ou notebook pour la traduction par un agent hôte.
2. Décidez si votre application gère les E/S de fichiers.
3. Utilisez les API de contenu lorsque votre application lit et écrit des fichiers individuels.
4. Utilisez `run_translation` lorsque Co-op Translator doit traiter un dépôt comme la CLI.
5. Utilisez `run_review` après la traduction si vous avez besoin de vérifications déterministes en automatisation.

| Objectif | API de départ |
| --- | --- |
| Traduire une chaîne ou un fichier Markdown | `translate_markdown_content` |
| Traduire un payload de notebook | `translate_notebook_content` |
| Traduire une image | `translate_image_content` |
| Laisser un agent hôte traduire des morceaux Markdown ou notebook | `start_markdown_agent_translation` ou `start_notebook_agent_translation` |
| Réécrire les liens traduits après avoir choisi un chemin de sortie | `rewrite_markdown_paths` ou `rewrite_notebook_paths` |
| Traduire un dépôt complet | `run_translation` |
| Relire la sortie traduite | `run_review` |

## Scénario 1 : Traduire des fichiers ou documents individuels

Utilisez ce flux de travail lorsque vous avez déjà un fichier, un buffer d'éditeur, un payload de notebook, une requête MCP ou une entrée de pipeline personnalisée. Votre code gère les E/S de fichiers :

1. Lisez le contenu source.
2. Appelez une API de traduction de contenu.
3. Éventuellement appelez une API de réécriture de chemins si le contenu traduit sera écrit dans un dossier de traduction de projet.
4. Enregistrez ou retournez le résultat depuis votre application.

Les API de traduction de contenu n'exécutent pas la découverte de projet, n'écrivent pas de métadonnées, n'ajoutent pas de mentions et ne réécrivent pas les liens automatiquement.

### Fichier Markdown

```python
import asyncio
from pathlib import Path

from co_op_translator.api import (
    rewrite_markdown_paths,
    translate_markdown_content,
)


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
        policy={
            "language_code": "ko",
            "root_dir": ".",
            "translations_dir": "translations",
            "translated_images_dir": "translated_images",
            "translation_types": ["markdown", "images"],
        },
    )

    target_path.parent.mkdir(parents=True, exist_ok=True)
    target_path.write_text(rewritten, encoding="utf-8")


asyncio.run(main())
```

Si le Markdown traduit ne vivra pas dans une structure de projet Co-op Translator, ignorez `rewrite_markdown_paths` et enregistrez la chaîne traduite directement.

### Fichier Notebook

```python
import asyncio
from pathlib import Path

from co_op_translator.api import (
    rewrite_notebook_paths,
    translate_notebook_content,
)


async def main() -> None:
    source_path = Path("docs/tutorial.ipynb")
    target_path = Path("translations/ja/docs/tutorial.ipynb")

    translated_json = await translate_notebook_content(
        source_path.read_text(encoding="utf-8"),
        "ja",
        {"source_path": source_path},
    )

    rewritten_json = rewrite_notebook_paths(
        translated_json,
        source_path=source_path,
        target_path=target_path,
        policy={
            "language_code": "ja",
            "root_dir": ".",
            "translations_dir": "translations",
            "translated_images_dir": "translated_images",
            "translation_types": ["notebook", "images"],
        },
    )

    target_path.parent.mkdir(parents=True, exist_ok=True)
    target_path.write_text(rewritten_json, encoding="utf-8")


asyncio.run(main())
```

`translate_notebook_content` traduit les cellules Markdown et préserve les cellules non-Markdown. La réécriture des chemins est appliquée uniquement aux cellules Markdown.

### Fichier image

```python
from pathlib import Path

from co_op_translator.api import translate_image_content

source_path = Path("docs/images/hero.png")
target_path = Path("translated_images/fr/hero.png")

translated_image = translate_image_content(
    source_path,
    "fr",
    {
        "root_dir": ".",
        "fast_mode": False,
    },
)

target_path.parent.mkdir(parents=True, exist_ok=True)
translated_image.save(target_path)
```

`translate_image_content` lit l'image source et renvoie une `PIL.Image.Image` rendue. Il n'écrit pas les métadonnées d'image traduites.

## Scénario 2 : Traduire un dépôt entier

Utilisez ce flux de travail lorsque vous souhaitez que l'API Python se comporte comme la CLI `translate`. `run_translation` découvre les fichiers pris en charge, traduit les types de contenu sélectionnés, réécrit les chemins, écrit les fichiers de sortie, met à jour les métadonnées et effectue des tâches de maintenance de traduction telles que le nettoyage.

`run_translation` est le point d'entrée d'orchestration de projet recommandé. `translate_project` est exporté en alias de compatibilité avec le même comportement.

Traduire les fichiers Markdown du dépôt courant en coréen et japonais :

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    markdown=True,
)
```

Traduire uniquement les notebooks depuis un répertoire racine de projet spécifique :

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="fr",
    root_dir="./my-course",
    notebook=True,
)
```

Prévisualiser le volume de traduction sans écrire de fichiers :

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="es de",
    root_dir="./my-course",
    markdown=True,
    dry_run=True,
)
```

Traduire plusieurs racines de contenu en un seul appel :

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    root_dirs=["./docs", "./labs"],
)
```

Écrire les traductions dans des groupes de sortie explicites :

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ja",
    markdown=True,
    groups=[
        ("./course-a", "./localized/course-a"),
        ("./course-b", "./localized/course-b"),
    ],
)
```

Utilisez un espace réservé par langue lorsque chaque langue doit contenir un sous-répertoire imbriqué :

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    groups=[
        ("./course", "./translations/<lang>/course"),
    ],
)
```

Si aucun de `markdown`, `notebook` ou `images` n'est défini, l'API traduit tous les types pris en charge : Markdown, notebooks et images.

## Revue de la sortie traduite

`run_review` exécute des vérifications de traduction déterministes sans identifiants LLM ou Vision.

!!! note "Bêta"
    `run_review` est une API de revue déterministe en bêta. Elle n'appelle pas les fournisseurs de modèles ni n'écrit de fichiers, mais les schémas des vérifications et des problèmes peuvent évoluer.

```python
from co_op_translator.api import run_review

run_review(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
)
```

Relire uniquement les fichiers modifiés par rapport à une référence de base et afficher une sortie au format GitHub :

```python
from co_op_translator.api import run_review

run_review(
    language_codes="ko",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
    changed_from="origin/main",
    output_format="github",
)
```

## Exemples d'API à copier-coller

Traduire du contenu Markdown sans écrire de fichiers :

```python
import asyncio

from co_op_translator.api import translate_markdown_content


async def main() -> None:
    translated = await translate_markdown_content(
        "# Hello\n\nWelcome to the course.",
        "ko",
    )
    print(translated)


asyncio.run(main())
```

Traduire et réécrire les liens Markdown :

```python
import asyncio

from co_op_translator.api import rewrite_markdown_paths, translate_markdown_content


async def main() -> None:
    translated = await translate_markdown_content(
        "[Setup](../setup.md)\n\n![Hero](../../images/hero.png)",
        "ko",
        {"source_path": "docs/guide.md"},
    )
    rewritten = rewrite_markdown_paths(
        translated,
        source_path="docs/guide.md",
        target_path="translations/ko/docs/guide.md",
        policy={
            "language_code": "ko",
            "root_dir": ".",
            "translations_dir": "translations",
            "translated_images_dir": "translated_images",
            "translation_types": ["markdown", "images"],
        },
    )
    print(rewritten)


asyncio.run(main())
```

Traduire un dépôt depuis Python :

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    root_dir="./course",
    markdown=True,
    yes=True,
)
```

Traduire plusieurs racines :

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    root_dirs=[
        "./docs",
        "./labs",
    ],
)
```

Conserver les termes du glossaire :

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="fr",
    markdown=True,
    glossaries=[
        "Co-op Translator",
        "Azure AI Foundry",
        "GitHub Actions",
    ],
)
```

## Points d'entrée publics

```python
from co_op_translator.api import (
    ImageTranslationOptions,
    MarkdownTranslationOptions,
    NotebookTranslationOptions,
    finish_markdown_agent_translation,
    finish_notebook_agent_translation,
    run_review,
    run_translation,
    rewrite_markdown_paths,
    rewrite_notebook_paths,
    start_markdown_agent_translation,
    start_notebook_agent_translation,
    translate_image_content,
    translate_markdown_content,
    translate_notebook_content,
    translate_project,
)
```

::: co_op_translator.api.translate_markdown_content

::: co_op_translator.api.translate_notebook_content

::: co_op_translator.api.translate_image_content

::: co_op_translator.api.start_markdown_agent_translation

::: co_op_translator.api.finish_markdown_agent_translation

::: co_op_translator.api.start_notebook_agent_translation

::: co_op_translator.api.finish_notebook_agent_translation

::: co_op_translator.api.rewrite_markdown_paths

::: co_op_translator.api.rewrite_notebook_paths

::: co_op_translator.api.MarkdownTranslationOptions

::: co_op_translator.api.NotebookTranslationOptions

::: co_op_translator.api.ImageTranslationOptions

::: co_op_translator.api.run_translation

::: co_op_translator.api.translate_project

::: co_op_translator.api.run_review

## API de traduction de contenu

Les API de traduction de contenu sont destinées aux intégrations qui ont déjà du contenu en mémoire, comme une extension d'éditeur, un outil MCP, un processeur de notebook ou un pipeline personnalisé.

| Fonction | Entrée | Sortie | E/S de fichiers | Remarques |
| --- | --- | --- | --- | --- |
| `translate_markdown_content` | Markdown `str` | Markdown `str` | Non | Asynchrone. Traduit uniquement le contenu Markdown. Il ne réécrit pas les liens, n'écrit pas de métadonnées et n'ajoute pas de mentions. |
| `translate_notebook_content` | Notebook JSON `str` ou `dict` | Notebook JSON `str` | Non | Asynchrone. Traduit les cellules Markdown et préserve les cellules non-Markdown. Il ne réécrit pas les liens, n'écrit pas de métadonnées et n'ajoute pas de mentions. |
| `translate_image_content` | Chemin d'image | `PIL.Image.Image` | Lit uniquement l'image source | Synchrone. Extrait et traduit le texte de l'image, puis renvoie une image rendue. Il n'enregistre pas les métadonnées d'image traduites. |

`translate_markdown_content` et `translate_notebook_content` acceptent un `source_path` optionnel via leurs options. Le chemin est passé en contexte au traducteur ; les appelants restent responsables de toute réécriture de chemin spécifique au projet après la traduction.

```python
from co_op_translator.api import MarkdownTranslationOptions, translate_markdown_content

translated = await translate_markdown_content(
    document,
    "ko",
    MarkdownTranslationOptions(source_path="docs/guide.md"),
)
```

Les mêmes options peuvent être passées sous forme de dictionnaires :

```python
translated = await translate_markdown_content(
    document,
    "ko",
    {"source_path": "docs/guide.md"},
)
```

## API de traduction assistée par agent

Les API assistées par agent n'appellent pas Azure OpenAI ni OpenAI depuis Co-op Translator. Elles préparent des morceaux Markdown ou notebook pour qu'un agent hôte les traduise, puis reconstituent le contenu final à partir des morceaux traduits.

| Fonction | Objectif |
| --- | --- |
| `start_markdown_agent_translation` | Retourner un travail Markdown autonome avec des morceaux, des invites et l'état de reconstitution. |
| `finish_markdown_agent_translation` | Reconstituer le Markdown à partir d'un travail et des morceaux traduits par l'agent hôte. |
| `start_notebook_agent_translation` | Retourner un travail de notebook avec des morceaux de cellules Markdown pour la traduction par l'agent hôte. |
| `finish_notebook_agent_translation` | Reconstituer le JSON du notebook tout en préservant les cellules de code, les sorties et les métadonnées. |

Ce flux de travail est principalement destiné aux hôtes MCP. Si vous avez besoin d'une traduction de dépôt en production avec Co-op Translator gérant les appels aux fournisseurs, utilisez `translate_markdown_content`, `translate_notebook_content` ou `run_translation`.

## API de réécriture de chemins

Les API de réécriture de chemins n'effectuent aucune traduction. Elles mettent à jour les liens et les chemins frontmatter après que les appelants connaissent le chemin source, le chemin cible traduit et la structure du projet.

| Fonction | Portée | Remarques |
| --- | --- | --- |
| `rewrite_markdown_paths` | Corps Markdown et frontmatter | Réécrit les liens Markdown et les champs de chemin frontmatter pris en charge pour une cible traduite. |
| `rewrite_notebook_paths` | Cellules Markdown dans le JSON du notebook | Applique la réécriture de chemin Markdown à chaque cellule Markdown et laisse les cellules non-Markdown inchangées. |

L'argument `policy` peut être un dictionnaire avec ces champs :

| Champ | Obligatoire | Objectif |
| --- | --- | --- |
| `language_code` | Yes | Code de langue cible, tel que `"ko"` ou `"pt-BR"`. |
| `root_dir` | No | Racine du projet source. Par défaut à `"."`. |
| `translations_dir` | No | Répertoire de sortie pour les traductions textuelles. Par défaut `translations` sous `root_dir`. |
| `translated_images_dir` | No | Répertoire de sortie des images traduites. Par défaut `translated_images` sous `root_dir`. |
| `translation_types` | No | Types de traduction activés. Par défaut Markdown, notebooks et images. |
| `lang_subdir` | No | Sous-répertoire optionnel sous chaque dossier de langue. |

## Paramètres de traduction du projet

| Paramètre | Type | Par défaut | Objectif |
| --- | --- | --- | --- |
| `language_codes` | `str` | Required | Codes de langue cibles séparés par des espaces, tels que `"ko ja fr"`, ou `"all"`. Les codes d'alias sont normalisés aux valeurs BCP 47 canoniques. |
| `root_dir` | `str` | `"."` | Racine du projet pour une cible de traduction unique. Ignoré lorsque `root_dirs` ou `groups` sont fournis. |
| `update` | `bool` | `False` | Supprimer et recréer les traductions existantes pour les langues sélectionnées. |
| `images` | `bool` | `False` | Inclure la traduction des images. Nécessite la configuration Azure AI Vision. |
| `markdown` | `bool` | `False` | Inclure la traduction Markdown. |
| `notebook` | `bool` | `False` | Inclure la traduction des notebooks Jupyter. |
| `debug` | `bool` | `False` | Activer la journalisation de débogage. |
| `save_logs` | `bool` | `False` | Enregistrer des fichiers de logs au niveau DEBUG sous le répertoire `logs/` racine. |
| `yes` | `bool` | `True` | Confirmer automatiquement les invites pour une utilisation programmatique et CI. |
| `add_disclaimer` | `bool` | `False` | Ajouter des mentions de traduction automatique aux Markdown et notebooks traduits. |
| `translations_dir` | `str \| None` | `None` | Répertoire de sortie personnalisé pour les traductions textuelles. Les chemins relatifs sont résolus par rapport à chaque racine. |
| `image_dir` | `str \| None` | `None` | Répertoire de sortie personnalisé pour les images traduites. Les chemins relatifs sont résolus par rapport à chaque racine. |
| `root_dirs` | `Iterable[str] \| None` | `None` | Plusieurs racines qui partagent les mêmes paramètres de sortie. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | Paires explicites `(root_dir, translations_dir)`. A priorité sur `root_dirs`. |
| `repo_url` | `str \| None` | `None` | URL du dépôt utilisée lors du rendu des indications de tableau de langues du README. |
| `glossaries` | `Iterable[str] \| None` | `None` | Termes de glossaire à préserver pendant la traduction. Les doublons et les termes vides sont normalisés. |
| `dry_run` | `bool` | `False` | Estimer le volume de traduction et prévisualiser le comportement de migration sans écrire de fichiers. |

## Paramètres de revue

`run_review` reflète volontairement la signature de `run_translation` lorsque c'est possible afin que l'automatisation puisse basculer entre les flux de traduction et de revue sans trop de conditions.

| Paramètre | Type | Par défaut | Objectif |
| --- | --- | --- | --- |
| `language_codes` | `str \| Iterable[str]` | `"all"` | Dossiers de langue cibles à réviser. Les chaînes séparées par des espaces et les itérables sont acceptés. `"all"` révise chaque langue de traduction découverte. |
| `root_dir` | `str` | `"."` | Racine du projet pour une cible de revue unique. Ignoré lorsque `root_dirs` ou `groups` sont fournis. |
| `markdown` | `bool` | `False` | Inclure les fichiers source Markdown et MDX. |
| `notebook` | `bool` | `False` | Inclure les fichiers source Jupyter notebook. |
| `images` | `bool` | `False` | Réservé pour la parité avec les options de traduction. Les références aux images sont vérifiées depuis Markdown. |
| `translations_dir` | `str \| None` | `None` | Répertoire de sortie personnalisé pour la traduction de texte. Les chemins relatifs sont résolus par rapport à chaque racine. |
| `root_dirs` | `Iterable[str] \| None` | `None` | Racines multiples qui partagent les mêmes paramètres de sortie. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | Paires explicites `(root_dir, translations_dir)`. Prend le pas sur `root_dirs`. |
| `changed_from` | `str \| None` | `None` | Référence Git utilisée pour limiter la revue aux fichiers source modifiés. |
| `output_format` | `str` | `"text"` | Format de sortie de la revue. Les valeurs prises en charge sont `"text"` et `"github"`. |
| `fail_on_warnings` | `bool` | `False` | Traiter les avertissements comme des échecs en plus des erreurs. |
| `debug` | `bool` | `False` | Activer la journalisation de débogage. |
| `save_logs` | `bool` | `False` | Enregistrer les fichiers de log au niveau DEBUG sous le répertoire racine `logs/`. |

Si aucun de `markdown`, `notebook` ou `images` n'est défini, l'API passe en revue le Markdown, les notebooks et les références de liens d'images lorsque cela est applicable. La revue n'appelle pas de fournisseur LLM et ne nécessite pas de clés d'API.

## Exigences de configuration

Les API de traduction reposant sur un fournisseur nécessitent une configuration du fournisseur avant la traduction :

- La traduction de Markdown et de notebooks nécessite un fournisseur LLM. Configurez soit Azure OpenAI soit OpenAI.
- La traduction d'images nécessite Azure AI Vision en plus du fournisseur LLM.
- `run_translation` effectue des vérifications de connectivité légères avant le début de la traduction du projet.
- Les API assistées par agent `start_*_agent_translation` et `finish_*_agent_translation` n'appellent pas les fournisseurs LLM de Co-op Translator. L'application hôte ou l'agent MCP traduit les segments préparés.
- `rewrite_markdown_paths`, `rewrite_notebook_paths` et `run_review` sont déterministes et ne nécessitent pas de justificatifs de fournisseur.

Variables requises pour Azure OpenAI :

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Variables requises pour OpenAI :

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

Variables requises pour Azure AI Vision pour la traduction d'images :

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

`run_review` est déterministe et ne nécessite pas de configuration Azure OpenAI, OpenAI ou Azure AI Vision.

## Remarques sur le comportement

- Les API de traduction de contenu séparent la traduction du réécriture des chemins du projet. Appelez explicitement `rewrite_markdown_paths` ou `rewrite_notebook_paths` lorsque le contenu traduit nécessite l'ajustement des liens relatifs au projet pour une destination cible.
- Les API d'orchestration de projet ajoutent un comportement de projet autour de la traduction de contenu, incluant la découverte des fichiers, les écritures, la réécriture des chemins, les métadonnées, le nettoyage et les clauses de non-responsabilité optionnelles.
- `run_translation` affiche des résumés de progression et d'estimation via Click, correspondant à l'expérience utilisateur CLI.
- `dry_run=True` calcule des estimations en utilisant des mises à jour virtuelles du README, mais n'écrit pas le README ni les fichiers de traduction.
- Les `groups` sont traités séquentiellement. Une estimation agrégée unique est affichée avant le début des opérations.
- Lorsque la traduction d'images est sélectionnée, l'absence de configuration Vision provoque une erreur avant le début de la traduction.
- Les dossiers de langue existants basés sur des alias sont détectés et peuvent être migrés vers des noms de dossiers de langue canoniques dans le cadre de l'exécution.
- `run_review` échoue en cas de fichiers traduits manquants, de métadonnées de traduction manquantes ou obsolètes, d'un frontmatter Markdown / de blocs de code mal formés, et d'un JSON de notebook traduit invalide.
- Par défaut, `run_review` signale comme avertissements les cibles locales Markdown et les cibles de liens d'images manquantes.

## Chemin d'appel interne

L'API délègue à la même implémentation cœur utilisée par la CLI :

Traduction :

1. `co_op_translator.api.translation.translate_markdown_content`, `translate_notebook_content`, ou `translate_image_content` pour la traduction en mémoire.
2. `co_op_translator.api.translation.rewrite_markdown_paths` ou `rewrite_notebook_paths` pour le post-traitement explicite des chemins.
3. `co_op_translator.api.translation.run_translation` pour l'orchestration complète du projet.
4. `co_op_translator.config.Config`, `LLMConfig`, et `VisionConfig`.
5. `co_op_translator.core.project.ProjectTranslator`.
6. `co_op_translator.core.project.TranslationManager`.
7. Mixin d'orchestration de traduction de projet focalisés pour Markdown, notebooks, et images.
8. Traducteurs de Markdown, notebook, texte et images sous `co_op_translator.core`.

Revue :

1. `co_op_translator.api.review.run_review`
2. `co_op_translator.review.targets.build_review_targets`
3. `co_op_translator.review.runner.ReviewRunner`
4. Vérifications déterministes sous `co_op_translator.review.checks`

Les classes suivantes sont utiles pour les mainteneurs, mais ne sont pas exportées comme API stable au niveau du package.

| Classe | Module | Responsabilité |
| --- | --- | --- |
| `ProjectTranslator` | `co_op_translator.core.project.project_translator` | Coordonne la traduction au niveau du projet, la gestion des répertoires, la normalisation des métadonnées par langue, et la délégation aux traducteurs de Markdown, notebook et images. |
| `TranslationManager` | `co_op_translator.core.project.translation` | Effectue le traitement asynchrone des fichiers pour Markdown, notebooks, images, la détection d'obsolescence, et les mises à jour des métadonnées de traduction. |
| `ProjectMarkdownTranslationMixin` | `co_op_translator.core.project.translation.project_markdown_translation` | Orchestre la lecture des fichiers Markdown, la traduction du contenu, la réécriture des chemins, les métadonnées, les clauses de non-responsabilité, et les écritures. |
| `ProjectNotebookTranslationMixin` | `co_op_translator.core.project.translation.project_notebook_translation` | Orchestre la lecture des fichiers notebook, la traduction des cellules Markdown, la réécriture des chemins, les métadonnées, les clauses de non-responsabilité, et les écritures. |
| `ProjectImageTranslationMixin` | `co_op_translator.core.project.translation.project_image_translation` | Orchestre la découverte des images sources, la traduction des images, les chemins de sortie, les métadonnées, et les écritures. |
| `ProjectEvaluator` | `co_op_translator.core.project.project_evaluator` | Trouve les paires Markdown traduites, évalue la qualité de la traduction, et lit les métadonnées de confiance pour les workflows de réparation à faible confiance. |
| `ReviewRunner` | `co_op_translator.review.runner` | Coordonne les vérifications déterministes sur les fichiers source, les langues cibles, et les racines de traduction configurées. |
| `ReviewTarget` | `co_op_translator.review.targets` | Décrit une racine source et le répertoire de sortie de traduction examiné pour cette racine. |
| `LanguageFolderMigrator` | `co_op_translator.core.project.language_migrator` | Détecte les dossiers de langue hérités basés sur des alias et prépare des plans de migration vers des dossiers BCP 47 canoniques. |
| `Config` | `co_op_translator.config.base_config` | Charge les fichiers `.env` et vérifie si les fournisseurs LLM requis et les fournisseurs Vision optionnels sont configurés. |
| `LLMConfig` | `co_op_translator.config.llm_config.config` | Détecte automatiquement Azure OpenAI ou OpenAI, valide les variables d'environnement requises, et effectue des vérifications de connectivité du fournisseur. |
| `VisionConfig` | `co_op_translator.config.vision_config.config` | Détecte la configuration Azure AI Vision et effectue des vérifications de connectivité pour la traduction d'images. |