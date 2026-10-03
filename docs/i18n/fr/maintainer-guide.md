# Guide du mainteneur

Cette page résume comment l'API, la CLI et le site de documentation sont connectés.

## Frontière de l'API publique

L'API Python stable est exportée depuis:

```python
co_op_translator.api
```

L'API publique est organisée en assistants de traduction de contenu, en assistants de réécriture de chemins, en orchestration de projet et en revue :

```python
from co_op_translator.api import (
    ImageTranslationOptions,
    MarkdownTranslationOptions,
    NotebookTranslationOptions,
    TranslationBaseline,
    TranslationStateProvider,
    TranslationUpdate,
    run_review,
    run_translation,
    rewrite_markdown_paths,
    rewrite_notebook_paths,
    translate_image_content,
    translate_markdown_content,
    translate_notebook_content,
    translate_project,
)
```

`TranslationStateProvider` est la frontière de persistance pour les intégrations hébergées.
Il doit garder les candidats générés séparés des bases de référence acceptées afin qu'une
traduction non fusionnée ne devienne la source de vérité.

Lors de l'ajout de nouvelles API publiques, mettez à jour:

- `src/co_op_translator/api/__init__.py`
- `docs/api.md`
- les tests API pertinents sous `tests/co_op_translator/`, tels que `test_api.py` ou `test_review_api.py`

Évitez de documenter les modules `core` de niveau inférieur comme API stable sauf si le projet a l'intention de les prendre en charge directement.

## Points d'entrée CLI

Le paquet définit ces scripts Poetry:

```toml
[tool.poetry.scripts]
translate = "co_op_translator.__main__:main"
evaluate = "co_op_translator.__main__:main"
migrate-links = "co_op_translator.__main__:main"
co-op-review = "co_op_translator.__main__:main"
co-op-translator-mcp = "co_op_translator.mcp.server:main"
```

`src/co_op_translator/__main__.py` redirige en fonction du nom du script :

- `translate` appelle `co_op_translator.cli.translate.translate_command`
- `evaluate` appelle `co_op_translator.cli.evaluate.evaluate_command`
- `migrate-links` appelle `co_op_translator.cli.migrate_links.migrate_links_command`
- `co-op-review` appelle `co_op_translator.cli.review.review_command`

`co-op-translator-mcp` contourne `__main__.py` et appelle directement `co_op_translator.mcp.server:main`.

Lors de l'ajout ou de la modification d'options CLI, mettez à jour:

- la commande pertinente dans `src/co_op_translator/cli/*.py`
- `docs/cli.md`
- les tests liés à la CLI, si le comportement change

## MCP server

Le serveur MCP est implémenté dans:

```python
co_op_translator.mcp.server
```

Le serveur enveloppe intentionnellement l'API Python publique plutôt que d'appeler les modules `core` de bas niveau. Gardez cette frontière intacte afin que les clients MCP, les appelants Python et la CLI partagent le même comportement.

Lors de l'ajout ou de la modification d'outils MCP, mettez à jour:

- `src/co_op_translator/mcp/server.py`
- `tests/co_op_translator/test_mcp_server.py`
- `docs/mcp.md`
- `docs/api.md` si la surface de l'API publique change

Les outils de traduction du dépôt sont appelables par modèle via MCP et peuvent écrire de nombreux fichiers. Gardez `dry_run=True` comme valeur par défaut et exigez `confirm_write=True` avant une traduction de projet en mode non-dry-run.

## Flux de traduction

Le flux de traduction de projet de haut niveau est :

1. Analyser les arguments CLI ou les paramètres d'API.
2. Valider la configuration LLM avec `LLMConfig`.
3. Valider Azure AI Vision lorsque la traduction d'images est sélectionnée.
4. Normaliser les codes de langue.
5. Détecter les alias de dossiers de langue hérités.
6. Estimer le volume de traduction.
7. Mettre à jour les sections de langue/cours du README lorsque cela est applicable.
8. Déléguer la traduction du projet à `ProjectTranslator`.
9. `ProjectTranslator` délègue le traitement des fichiers à `TranslationManager`.

`TranslationManager` est composé de mixins ciblés par type de fichier :

- `ProjectMarkdownTranslationMixin` gère la lecture des fichiers Markdown, la traduction du contenu, la réécriture des chemins, les métadonnées, les clauses de non-responsabilité et les écritures.
- `ProjectNotebookTranslationMixin` gère la lecture des notebooks, la traduction des cellules Markdown, la réécriture des chemins, les métadonnées, les clauses de non-responsabilité et les écritures.
- `ProjectImageTranslationMixin` gère la découverte d'images, l'extraction/traduction de texte, l'écriture des images rendues et les métadonnées.

Les API de contenu de plus bas niveau ignorent le flux de travail du projet :

1. `translate_markdown_content` et `translate_notebook_content` traduisent uniquement le contenu en mémoire.
2. `translate_image_content` traduit le texte d'une seule image et renvoie un objet d'image rendu.
3. `rewrite_markdown_paths` et `rewrite_notebook_paths` sont des outils explicites de post-traitement. Ils n'effectuent aucune traduction et n'écrivent rien dans le projet.

## Flux de revue

Le flux de revue déterministe est :

1. Analyser les arguments CLI ou les paramètres d'API.
2. Normaliser les codes de langue demandés.
3. Construire une ou plusieurs cibles de revue à partir de `root_dir`, `root_dirs` ou `groups`.
4. Optionnellement limiter les fichiers source avec `--changed-from`.
5. Exécuter des vérifications déterministes pour la structure, la fraîcheur des traductions, l'intégrité Markdown et les chemins de liens/images locaux.
6. Afficher soit une sortie texte soit du Markdown au format GitHub.
7. Quitter avec un échec lorsque des erreurs de revue sont trouvées.

Le flux de revue ne nécessite pas de clés d'API et reste disponible pour des vérifications locales ou l'intégration CI optionnelle côté consommateur. Ce dépôt n'exécute pas `co-op-review` automatiquement sur chaque pull request.

## Site de documentation

Le site de documentation est configuré par:

```text
mkdocs.yml
requirements-docs.txt
docs/
```

Le répertoire `docs/` est la source canonique de la documentation. N'ajoutez pas de nouveaux guides destinés aux utilisateurs finaux en dehors de ce répertoire, sauf si le projet introduit intentionnellement une autre surface de documentation publiée.

Build locally:

```bash
python -m pip install -r requirements-docs.txt
python -m mkdocs build --strict
```

Preview locally:

```bash
python -m mkdocs serve
```

The generated site is written to `site/`, which is ignored by git.

## Flux de travail GitHub Pages

`.github/workflows/docs.yml` construit le site lors des pull requests et le déploie à chaque push vers `main`.

The workflow installs:

```bash
pip install -r requirements-docs.txt
```

Le workflow de docs installe uniquement la chaîne d'outils de documentation. `mkdocs.yml` pointe `mkdocstrings` vers `src/` afin que les pages de l'API publique puissent être rendues depuis l'arborescence source sans installer l'ensemble complet des dépendances d'exécution. Si la documentation future de l'API nécessite d'importer des fournisseurs d'exécution optionnels lors de la génération, mettez à jour à la fois `.github/workflows/docs.yml` et ce guide.

## Seuil de qualité de la documentation

Avant de fusionner des modifications de documentation, exécutez:

```bash
python -m mkdocs build --strict
git diff --check
```

Utilisez des builds stricts afin que les liens brisés, les entrées de navigation invalides et les problèmes de rendu de l'API échouent tôt.