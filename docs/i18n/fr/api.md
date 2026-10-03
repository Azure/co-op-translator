# API Python

L'API publique stable pour Python est exportée depuis `co_op_translator.api`. La plupart des intégrations utilisent l'un de ces flux de travail :

| Scénario | À utiliser lorsque | Principales API |
| --- | --- | --- |
| Traduire des fichiers ou documents individuels | Votre application lit le contenu source, appelle Co-op Translator pour la traduction et décide où enregistrer le résultat. | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Préparer le contenu pour la traduction par un agent hôte | Votre hôte MCP ou modèle d'application traduira les segments, tandis que Co-op Translator gère la segmentation et la reconstruction. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Traduire un dépôt entier | Vous voulez que l'API Python se comporte comme l'interface CLI et gère la découverte, les chemins de sortie, les métadonnées, le nettoyage et les écritures. | `run_translation` |

La plupart des modules de bas niveau sous `core`, `config`, `review` et `utils` sont des détails d'implémentation utilisés par ces points d'entrée de l'API.

Les clients MCP utilisent la même API publique via le [MCP Server](mcp.md). Utilisez cette page lorsque vous appelez Python directement, et le guide MCP lorsque vous exposez Co-op Translator à un agent ou un éditeur. Si vous hésitez entre CLI, API Python et MCP, commencez par [Choose Your Workflow](workflows.md).

## Flux initial de l'API

Commencez ici si vous appelez Co-op Translator depuis du code Python :

1. Configurez un fournisseur LLM comme décrit dans [Configuration](configuration.md), sauf si vous préparez uniquement des segments Markdown ou de notebook pour une traduction par un agent hôte.
2. Décidez si votre application gère les E/S de fichiers.
3. Utilisez les API de contenu lorsque votre application lit et écrit des fichiers individuels.
4. Utilisez `run_translation` lorsque Co-op Translator doit traiter un dépôt comme le fait la CLI.
5. Utilisez `run_review` après la traduction si vous avez besoin de contrôles déterministes en automatisation.

| Objectif | API de départ |
| --- | --- |
| Traduire une chaîne ou un fichier Markdown | `translate_markdown_content` |
| Traduire un payload de notebook | `translate_notebook_content` |
| Traduire une image | `translate_image_content` |
| Laisser un agent hôte traduire des segments Markdown ou de notebook | `start_markdown_agent_translation` ou `start_notebook_agent_translation` |
| Réécrire les liens traduits après avoir choisi un chemin de sortie | `rewrite_markdown_paths` ou `rewrite_notebook_paths` |
| Traduire un dépôt complet | `run_translation` |
| Review translated output | `run_review` |

## Scénario 1 : Traduire des fichiers ou documents individuels

Utilisez ce flux de travail lorsque vous disposez déjà d'un fichier, d'un buffer d'éditeur, d'un payload de notebook, d'une requête MCP ou d'une entrée de pipeline personnalisé. Votre code gère les E/S de fichiers :

1. Lisez le contenu source.
2. Appelez une API de traduction de contenu.
3. Éventuellement appelez une API de réécriture de chemins si le contenu traduit doit être écrit dans un dossier de traduction du projet.
4. Enregistrez ou renvoyez le résultat depuis votre application.

Les API de traduction de contenu n'exécutent pas la découverte de projet, n'écrivent pas de métadonnées, n'ajoutent pas de mentions légales et ne réécrivent pas les liens automatiquement.

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

Si le Markdown traduit ne sera pas intégré dans la structure d'un projet Co-op Translator, sautez `rewrite_markdown_paths` et enregistrez la chaîne traduite directement.

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

`translate_image_content` lit l'image source et retourne une `PIL.Image.Image` rendue. Il n'écrit pas les métadonnées d'image traduites.

## Scénario 2 : Traduire un dépôt entier

Utilisez ce flux de travail lorsque vous souhaitez que l'API Python se comporte comme la CLI `translate`. `run_translation` découvre les fichiers pris en charge, traduit les types de contenu sélectionnés, réécrit les chemins, écrit les fichiers de sortie, met à jour les métadonnées et effectue des tâches de maintenance de la traduction telles que le nettoyage.

`run_translation` est le point d'entrée privilégié pour l'orchestration de projet. `translate_project` est exporté comme alias de compatibilité avec le même comportement.

Traduire les fichiers Markdown du dépôt courant en coréen et en japonais :

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    markdown=True,
)
```

Traduire uniquement les notebooks depuis un root de projet spécifique :

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

Enregistrer des événements de progression structurés pour une intégration :

```python
from co_op_translator.api import TranslationEvent, run_translation


def on_event(event: TranslationEvent) -> None:
    payload = event.to_dict()
    # Stockez la charge utile dans votre table job-event ou diffusez-la en continu vers votre interface utilisateur.


run_translation(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
    progress_callback=on_event,
)
```

Les événements utilisent le schéma versionné `co-op.translation.event.v1`. Les intégrations devraient
se baser sur des champs stables tels que `type` et `stage_key`, pas sur du texte
destiné à l'affichage en console ou sur `stage_label`.

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

Si aucun des paramètres `markdown`, `notebook` ou `images` n'est défini, l'API traduit tous les types pris en charge : Markdown, notebooks et images.

### Préserver les modifications humaines acceptées avec un fournisseur d'état de traduction

Par défaut, Co-op Translator conserve son comportement existant au niveau du fichier : lorsqu'un
source Markdown devient obsolète, le fichier traduit entier est regénéré. Les intégrations hébergées
peuvent optionnellement fournir un `TranslationStateProvider` pour préserver les modifications humaines
dans des blocs source qui n'ont pas changé.

Le fournisseur fournit la dernière paire source/cible acceptée et enregistre chaque nouveau
candidat. L'acceptation reste de la responsabilité de l'intégration—par exemple,
après la fusion d'une pull request de traduction :

```python
from pathlib import Path

from co_op_translator.api import (
    TranslationBaseline,
    TranslationUpdate,
    run_translation,
)


class DatabaseTranslationState:
    def load_baseline(
        self,
        *,
        source_path: Path,
        translation_path: Path,
        language_code: str,
    ) -> TranslationBaseline | None:
        row = load_accepted_translation(
            source_path=source_path,
            translation_path=translation_path,
            language_code=language_code,
        )
        if row is None:
            return None
        return TranslationBaseline(
            source_text=row.source_text,
            target_text=row.target_text,
            revision=row.accepted_revision,
        )

    def record_candidate(
        self,
        *,
        source_path: Path,
        translation_path: Path,
        language_code: str,
        source_text: str,
        target_text: str,
        update: TranslationUpdate,
    ) -> None:
        save_translation_candidate(
            source_path=source_path,
            translation_path=translation_path,
            language_code=language_code,
            source_text=source_text,
            target_text=target_text,
            mode=update.mode,
            fallback_reason=update.fallback_reason,
        )


run_translation(
    language_codes="ko",
    root_dir="./course",
    markdown=True,
    translation_state_provider=DatabaseTranslationState(),
)
```

Pour les fichiers Markdown disposant d'une baseline acceptée valide, Co-op Translator aligne
les blocs Markdown de premier niveau. Les blocs source inchangés réutilisent les blocs traduits
actuels, y compris les modifications effectuées par des personnes ; les blocs source modifiés ou ajoutés sont envoyés
pour traduction ; les blocs source supprimés sont retirés. Si l'alignement est ambigu,
la structure cible a changé, une traduction de bloc est invalide, ou aucune baseline n'est
disponible, Co-op Translator revient en toute sécurité au chemin existant de traduction complète
du fichier.

Cette API stocke l'état de traduction du document, pas une mémoire de traduction de phrases ou
de segments trans-document. Elle s'applique actuellement à la traduction de projets Markdown.
Le comportement pour les notebooks et les images reste inchangé. Passer `update=True`
demande toujours une régénération complète.

Si un ou plusieurs fichiers ne peuvent pas être traduits, `run_translation` lève une
`RuntimeError` après la fin du flux de projet au lieu de signaler un
exécutable réussi avec sortie manquante. Les intégrations devraient considérer cela comme un échec
et conserver l'état de traduction accepté précédent.

## Réviser la sortie traduite

`run_review` exécute des contrôles de traduction déterministes sans identifiants LLM ou Vision.

!!! note "Bêta"
    `run_review` est une API de revue déterministe en version bêta. Elle n'appelle pas les fournisseurs de modèles ni n'écrit de fichiers, mais les contrôles et les schémas d'incidents peuvent évoluer.

```python
from co_op_translator.api import run_review

run_review(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
)
```

Après une traduction limitée au README, utilisez la même portée pour la revue :

```python
run_review(language_codes="ko", root_dir="./my-course", readme_only=True)
```

`readme_only=True` vérifie uniquement `README.md` sous chaque racine source configurée,
y compris les `groups` personnalisés et les répertoires de sortie. Les autres documents et README
imbriqués sont exclus. L'absence d'un README source lève `ValueError` ; des
contrôles de traduction échoués lèvent `RuntimeError`.

Réviser uniquement les fichiers modifiés par rapport à une référence de base et afficher une sortie au format GitHub :

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

## Exemples API à copier-coller

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
        "[Setup](../setup.md)\n\n![Hero](images/hero.png)",
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

Préserver les termes du glossaire :

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
    TranslationBaseline,
    TranslationStateProvider,
    TranslationUpdate,
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

::: co_op_translator.api.TranslationBaseline

::: co_op_translator.api.TranslationStateProvider

::: co_op_translator.api.TranslationUpdate

::: co_op_translator.api.run_translation

::: co_op_translator.api.translate_project

::: co_op_translator.api.run_review

## API de traduction de contenu

Les API de traduction de contenu sont destinées aux intégrations qui ont déjà du contenu en mémoire, comme une extension d'éditeur, un outil MCP, un processeur de notebooks ou un pipeline personnalisé.

| Fonction | Entrée | Sortie | E/S de fichiers | Remarques |
| --- | --- | --- | --- | --- |
| `translate_markdown_content` | Markdown `str` | Markdown `str` | Non | Asynchrone. Traduit uniquement le contenu Markdown. Il ne réécrit pas les liens, n'écrit pas de métadonnées et n'ajoute pas de mentions légales. |
| `translate_notebook_content` | Notebook JSON `str` or `dict` | Notebook JSON `str` | Non | Asynchrone. Traduit les cellules Markdown et préserve les cellules non-Markdown. Il ne réécrit pas les liens, n'écrit pas de métadonnées et n'ajoute pas de mentions légales. |
| `translate_image_content` | Image path | `PIL.Image.Image` | Lit uniquement l'image source | Synchrone. Extrait et traduit le texte de l'image, puis retourne une image rendue. Il n'enregistre pas les métadonnées d'image traduites. |

`translate_markdown_content` et `translate_notebook_content` acceptent un `source_path` optionnel via leurs options. Le chemin est passé comme contexte au traducteur ; les appelants restent responsables de toute réécriture de chemin spécifique au projet après la traduction.

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

Les API assistées par agent n'appellent pas le fournisseur LLM configuré depuis Co-op Translator. Elles préparent des segments Markdown ou de notebook pour qu'un agent hôte les traduise, puis reconstruisent le contenu final à partir des segments traduits.

| Fonction | Objectif |
| --- | --- |
| `start_markdown_agent_translation` | Retourne un job Markdown autonome avec des chunks, des prompts et l'état de reconstruction. |
| `finish_markdown_agent_translation` | Reconstruit le Markdown à partir d'un job et des chunks traduits par l'agent hôte. |
| `start_notebook_agent_translation` | Retourne un job de notebook avec des chunks de cellules Markdown pour traduction par l'agent hôte. |
| `finish_notebook_agent_translation` | Reconstruit le JSON du notebook tout en préservant les cellules de code, les sorties et les métadonnées. |

Ce flux de travail est principalement destiné aux hôtes MCP. Si vous avez besoin d'une traduction de dépôt en production avec Co-op Translator gérant les appels aux fournisseurs, utilisez `translate_markdown_content`, `translate_notebook_content` ou `run_translation`.

## API de réécriture de chemins

Les API de réécriture de chemins n'effectuent aucune traduction. Elles mettent à jour les liens et les chemins du frontmatter une fois que les appelants connaissent le chemin source, le chemin cible traduit et la structure du projet.

| Fonction | Portée | Remarques |
| --- | --- | --- |
| `rewrite_markdown_paths` | Corps Markdown et frontmatter | Réécrit les liens Markdown et les champs de chemin du frontmatter pris en charge pour une cible traduite. |
| `rewrite_notebook_paths` | Cellules Markdown dans le JSON du notebook | Applique la réécriture de chemins Markdown à chaque cellule Markdown et laisse les cellules non-Markdown inchangées. |

L'argument `policy` peut être un dictionnaire avec ces champs :

| Champ | Obligatoire | Objet |
| --- | --- | --- |
| `language_code` | Oui | Code de langue cible, par exemple `"ko"` ou `"pt-BR"`. |
| `root_dir` | Non | Racine du projet source. Par défaut `"."`. |
| `translations_dir` | Non | Répertoire de sortie des traductions textuelles. Par défaut `translations` sous `root_dir`. |
| `translated_images_dir` | Non | Répertoire de sortie des images traduites. Par défaut `translated_images` sous `root_dir`. |
| `translation_types` | Non | Types de traduction activés. Par défaut Markdown, notebooks et images. |
| `lang_subdir` | Non | Sous-répertoire optionnel sous chaque dossier de langue. |

## Paramètres de traduction de projet

| Paramètre | Type | Valeur par défaut | Objet |
| --- | --- | --- | --- |
| `language_codes` | `str` | Obligatoire | Codes de langues cibles séparés par des espaces, par exemple `"ko ja fr"`, ou `"all"`. Les codes alias sont normalisés en valeurs BCP 47 canoniques. |
| `root_dir` | `str` | `"."` | Racine du projet pour une seule cible de traduction. Ignoré lorsque `root_dirs` ou `groups` sont fournis. |
| `update` | `bool` | `False` | Supprimer et recréer les traductions existantes pour les langues sélectionnées. |
| `images` | `bool` | `False` | Inclure la traduction d'images. Nécessite la configuration Azure AI Vision. |
| `markdown` | `bool` | `False` | Inclure la traduction Markdown. |
| `notebook` | `bool` | `False` | Inclure la traduction de notebooks Jupyter. |
| `debug` | `bool` | `False` | Activer la journalisation de débogage. |
| `save_logs` | `bool` | `False` | Enregistrer les fichiers journaux de niveau DEBUG sous le répertoire racine `logs/`. |
| `yes` | `bool` | `True` | Confirme automatiquement les invites pour une utilisation programmatique et en CI. |
| `add_disclaimer` | `bool` | `False` | Ajouter des avertissements de traduction automatique aux fichiers Markdown et aux notebooks traduits. |
| `translations_dir` | `str \| None` | `None` | Répertoire de sortie personnalisé pour les traductions de texte. Les chemins relatifs sont résolus par rapport à chaque racine. |
| `image_dir` | `str \| None` | `None` | Répertoire de sortie personnalisé pour les images traduites. Les chemins relatifs sont résolus par rapport à chaque racine. |
| `root_dirs` | `Iterable[str] \| None` | `None` | Plusieurs racines partageant les mêmes paramètres de sortie. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | Paires explicites `(root_dir, translations_dir)`. Prend la priorité sur `root_dirs`. |
| `repo_url` | `str \| None` | `None` | URL du dépôt utilisée pour le rendu des indications du tableau des langues du README. |
| `glossaries` | `Iterable[str] \| None` | `None` | Termes de glossaire à préserver pendant la traduction. Les doublons et les termes vides sont normalisés. |
| `dry_run` | `bool` | `False` | Estimer le volume de traduction et prévisualiser le comportement de migration sans écrire de fichiers. |
| `translation_state_provider` | `TranslationStateProvider \| None` | `None` | Adaptateur optionnel de persistance pour baseline acceptée et candidats pour les mises à jour incrémentales de Markdown. Le fait de l'omettre préserve le comportement existant de traitement complet des fichiers. |

## Paramètres de revue

`run_review` reflète intentionnellement la signature de `run_translation` lorsque c'est possible afin que l'automatisation puisse basculer entre les flux de travail de traduction et de revue avec un minimum de branchements.

| Paramètre | Type | Défaut | But |
| --- | --- | --- | --- |
| `language_codes` | `str \| Iterable[str]` | `"all"` | Dossiers de langue cibles à examiner. Les chaînes séparées par des espaces et les itérables sont acceptés. `"all"` examine toutes les langues de traduction détectées. |
| `root_dir` | `str` | `"."` | Racine du projet pour une seule cible de revue. Ignorée lorsque `root_dirs` ou `groups` sont fournis. |
| `markdown` | `bool` | `False` | Inclure les fichiers source Markdown et MDX. |
| `notebook` | `bool` | `False` | Inclure les fichiers source de notebooks Jupyter. |
| `images` | `bool` | `False` | Réservé pour la parité avec les options de traduction. Les références de lien vers les images sont vérifiées à partir du Markdown. |
| `translations_dir` | `str \| None` | `None` | Répertoire de sortie personnalisé pour les traductions de texte. Les chemins relatifs sont résolus par rapport à chaque racine. |
| `root_dirs` | `Iterable[str] \| None` | `None` | Plusieurs racines partageant les mêmes paramètres de sortie. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | Paires explicites `(root_dir, translations_dir)`. Prend la priorité sur `root_dirs`. |
| `changed_from` | `str \| None` | `None` | Référence Git utilisée pour limiter la revue aux fichiers source modifiés. |
| `readme_only` | `bool` | `False` | Revoir uniquement `README.md` sous chaque racine source. L'absence d'un README source lève `ValueError`. |
| `output_format` | `str` | `"text"` | Format de sortie de la revue. Les valeurs prises en charge sont `"text"` et `"github"`. |
| `fail_on_warnings` | `bool` | `False` | Traiter les avertissements comme des échecs en plus des erreurs. |
| `debug` | `bool` | `False` | Activer la journalisation de débogage. |
| `save_logs` | `bool` | `False` | Enregistrer les fichiers journaux au niveau DEBUG dans le répertoire racine `logs/`. |

Si aucun des paramètres `markdown`, `notebook` ou `images` n'est défini, l'API passe en revue les Markdown, les notebooks et les références de liens d'images lorsque cela s'applique. La revue n'appelle pas de fournisseur LLM et ne nécessite pas de clés API.

## Exigences de configuration

Les API de traduction reposant sur un fournisseur nécessitent une configuration du fournisseur avant la traduction :

- La traduction de Markdown et de notebooks nécessite un fournisseur LLM. Configurez Azure OpenAI, OpenAI ou Anthropic.
- La traduction d'images nécessite Azure AI Vision en plus du fournisseur LLM.
- `run_translation` exécute des vérifications de connectivité légères avant le début de la traduction du projet.
- Les API assistées par agent `start_*_agent_translation` et `finish_*_agent_translation` n'appellent pas les fournisseurs LLM de Co-op Translator. L'application hôte ou l'agent MCP traduit les segments préparés.
- `rewrite_markdown_paths`, `rewrite_notebook_paths` et `run_review` sont déterministes et ne nécessitent pas d'identifiants de fournisseur.

Variables Azure OpenAI requises :

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Variables OpenAI requises :

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

Variables Anthropic requises :

```bash
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

`ANTHROPIC_BASE_URL` et `ANTHROPIC_MAX_TOKENS` sont optionnels. Microsoft Agent Framework est le client de modèle par défaut pour tous les fournisseurs à partir de Co-op Translator 0.22.0. Semantic Kernel peut encore être sélectionné temporairement avec `CO_OP_TRANSLATOR_MODEL_CLIENT="semantic-kernel"`, mais cela génère un avertissement de dépréciation ; voir [configuration](configuration.md#model-client-backend) pour le plan de suppression progressive.

Variables Azure AI Vision requises pour la traduction d'images :

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

`run_review` est déterministe et ne nécessite pas de configuration LLM ni Azure AI Vision.

## Remarques sur le comportement

- Les API de traduction de contenu séparent la traduction du réécriture des chemins du projet. Appelez explicitement `rewrite_markdown_paths` ou `rewrite_notebook_paths` lorsque le contenu traduit nécessite l'ajustement des liens relatifs au projet pour un emplacement cible.
- Les API d'orchestration de projet ajoutent un comportement de projet autour de la traduction de contenu, y compris la découverte de fichiers, les écritures, la réécriture de chemins, les métadonnées, le nettoyage et les avertissements optionnels.
- `run_translation` affiche les résumés d'avancement et d'estimation via le même rapporteur basé sur Rich utilisé par la CLI. La sortie non interactive revient au texte brut.
- `dry_run=True` calcule des estimations en utilisant des mises à jour virtuelles du README, mais n'écrit pas le README ni les fichiers de traduction.
- Les `groups` sont traités séquentiellement. Une estimation agrégée unique est imprimée avant le début du travail.
- Lorsque la traduction d'images est sélectionnée, l'absence de configuration Vision déclenche une erreur avant le début de la traduction.
- Les dossiers de langue existants basés sur des alias sont détectés et peuvent être migrés vers des noms de dossiers de langue canoniques dans le cadre de l'exécution.
- `run_review` échoue en cas de fichiers traduits manquants, de métadonnées de traduction manquantes ou obsolètes, d'entêtes/frontmatter ou de blocs de code Markdown malformés, et de JSON de notebook traduit invalide.
- `run_review` signale par défaut les cibles de liens Markdown et d'images locales manquantes comme des avertissements.

## Chemin d'appel interne

L'API délègue à la même implémentation cœur utilisée par la CLI :

Traduction :

1. `co_op_translator.api.translation.translate_markdown_content`, `translate_notebook_content`, or `translate_image_content` for in-memory translation.
2. `co_op_translator.api.translation.rewrite_markdown_paths` or `rewrite_notebook_paths` for explicit path post-processing.
3. `co_op_translator.api.translation.run_translation` for full project orchestration.
4. `co_op_translator.config.Config`, `LLMConfig`, and `VisionConfig`.
5. `co_op_translator.core.project.ProjectTranslator`.
6. `co_op_translator.core.project.TranslationManager`.
7. Mixins de traduction ciblée de projet pour Markdown, notebooks et images.
8. Traducteurs Markdown, notebook, texte et image sous `co_op_translator.core`.

Revue :

1. `co_op_translator.api.review.run_review`
2. `co_op_translator.review.targets.build_review_targets`
3. `co_op_translator.review.runner.ReviewRunner`
4. Vérifications déterministes sous `co_op_translator.review.checks`

Les classes suivantes sont utiles aux mainteneurs, mais ne sont pas exportées comme API stable au niveau du paquet.

| Classe | Module | Responsabilité |
| --- | --- | --- |
| `ProjectTranslator` | `co_op_translator.core.project.project_translator` | Coordonne la traduction au niveau du projet, la gestion des répertoires, la normalisation des métadonnées par langue, et la délégation aux traducteurs Markdown, notebook et image. |
| `TranslationManager` | `co_op_translator.core.project.translation` | Effectue le travail de traitement asynchrone des fichiers pour Markdown, notebooks, images, la détection d'obsolescence et les mises à jour des métadonnées de traduction. |
| `ProjectMarkdownTranslationMixin` | `co_op_translator.core.project.translation.project_markdown_translation` | Orchestre les lectures de fichiers Markdown, la traduction du contenu, la réécriture des chemins, les métadonnées, les avertissements, et les écritures. |
| `ProjectNotebookTranslationMixin` | `co_op_translator.core.project.translation.project_notebook_translation` | Orchestre les lectures de fichiers notebook, la traduction des cellules Markdown, la réécriture des chemins, les métadonnées, les avertissements, et les écritures. |
| `ProjectImageTranslationMixin` | `co_op_translator.core.project.translation.project_image_translation` | Orchestre la découverte des images source, la traduction d'images, les chemins de sortie, les métadonnées, et les écritures. |
| `ProjectEvaluator` | `co_op_translator.core.project.project_evaluator` | Trouve les paires Markdown traduites, évalue la qualité de la traduction, et lit les métadonnées de confiance pour les workflows de réparation à faible confiance. |
| `ReviewRunner` | `co_op_translator.review.runner` | Coordonne les vérifications déterministes de revue entre les fichiers source, les langues cibles, et les racines de traduction configurées. |
| `ReviewTarget` | `co_op_translator.review.targets` | Décrit une racine source et le répertoire de sortie de traduction examiné pour cette racine. |
| `LanguageFolderMigrator` | `co_op_translator.core.project.language_migrator` | Détecte les dossiers de langue legacy basés sur des alias et prépare des plans de migration vers des dossiers canoniques BCP 47. |
| `Config` | `co_op_translator.config.base_config` | Charge les fichiers `.env` et vérifie si les fournisseurs LLM requis et Vision optionnels sont configurés. |
| `LLMConfig` | `co_op_translator.config.llm_config.config` | Détecte automatiquement Azure OpenAI, OpenAI ou Anthropic, valide les variables d'environnement requises, et exécute des vérifications de connectivité du fournisseur. |
| `VisionConfig` | `co_op_translator.config.vision_config.config` | Détecte la configuration Azure AI Vision et exécute des vérifications de connectivité pour la traduction d'images. |