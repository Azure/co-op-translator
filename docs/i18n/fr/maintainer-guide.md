# Guide du mainteneur

Cette page résume la façon dont l'API, la CLI et le site de documentation sont interconnectés.

## Limite de l'API publique

L'API Python stable est exportée depuis :

```python
co_op_translator.api
```

L'API publique est organisée en assistants de traduction de contenu, assistants de réécriture de chemins, orchestration de projet et revue :

```python
from co_op_translator.api import (
    ImageTranslationOptions,
    MarkdownTranslationOptions,
    NotebookTranslationOptions,
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

Lorsque vous ajoutez de nouvelles API publiques, mettez à jour :

- `src/co_op_translator/api/__init__.py`
- `docs/api.md`
- les tests d'API pertinents sous `tests/co_op_translator/`, tels que `test_api.py` ou `test_review_api.py`

Évitez de documenter les modules `core` de bas niveau comme API stable sauf si le projet a l'intention de les prendre en charge directement.

## Points d'entrée CLI

Le paquet définit ces scripts Poetry :

```toml
[tool.poetry.scripts]
translate = "co_op_translator.__main__:main"
evaluate = "co_op_translator.__main__:main"
migrate-links = "co_op_translator.__main__:main"
co-op-review = "co_op_translator.__main__:main"
co-op-translator-mcp = "co_op_translator.mcp.server:main"
```

`src/co_op_translator/__main__.py` répartit selon le nom du script :

- `translate` appelle `co_op_translator.cli.translate.translate_command`
- `evaluate` appelle `co_op_translator.cli.evaluate.evaluate_command`
- `migrate-links` appelle `co_op_translator.cli.migrate_links.migrate_links_command`
- `co-op-review` appelle `co_op_translator.cli.review.review_command`

`co-op-translator-mcp` contourne `__main__.py` et appelle `co_op_translator.mcp.server:main` directement.

Lorsque vous ajoutez ou modifiez des options CLI, mettez à jour :

- la commande pertinente `src/co_op_translator/cli/*.py`
- `docs/cli.md`
- les tests liés à la CLI, si le comportement change

## Serveur MCP

Le serveur MCP est implémenté dans :

```python
co_op_translator.mcp.server
```

Le serveur encapsule intentionnellement l'API Python publique plutôt que d'appeler les modules `core` de bas niveau. Gardez cette frontière intacte afin que les clients MCP, les appelants Python et la CLI partagent le même comportement.

Lorsque vous ajoutez ou modifiez des outils MCP, mettez à jour :

- `src/co_op_translator/mcp/server.py`
- `tests/co_op_translator/test_mcp_server.py`
- `docs/mcp.md`
- `docs/api.md` si la surface de l'API publique change

Les outils de traduction du dépôt sont appelables via MCP et peuvent écrire de nombreux fichiers. Gardez `dry_run=True` par défaut et exigez `confirm_write=True` avant toute traduction de projet sans dry-run.

## Flux de traduction

Le flux de traduction de projet de haut niveau est :

1. Analyser les arguments CLI ou les paramètres de l'API.
2. Valider la configuration LLM avec `LLMConfig`.
3. Valider Azure AI Vision lorsque la traduction d'image est sélectionnée.
4. Normaliser les codes de langue.
5. Détecter les alias de dossiers de langue hérités.
6. Estimer le volume de traduction.
7. Mettre à jour les sections langue/cours du README lorsque cela s'applique.
8. Déléguer la traduction du projet à `ProjectTranslator`.
9. `ProjectTranslator` délègue le traitement des fichiers à `TranslationManager`.

`TranslationManager` est composé de mixins axés sur les types de fichiers :

- `ProjectMarkdownTranslationMixin` gère la lecture des fichiers Markdown, la traduction de contenu, la réécriture des chemins, les métadonnées, les avertissements, et les écritures.
- `ProjectNotebookTranslationMixin` gère la lecture des fichiers notebook, la traduction des cellules Markdown, la réécriture des chemins, les métadonnées, les avertissements, et les écritures.
- `ProjectImageTranslationMixin` gère la découverte d'images, l'extraction/traduction de texte, l'écriture d'images rendues, et les métadonnées.

Les API de contenu de bas niveau contournent le flux de travail du projet :

1. `translate_markdown_content` et `translate_notebook_content` traduisent uniquement le contenu en mémoire.
2. `translate_image_content` traduit le texte dans une seule image et renvoie un objet image rendu.
3. `rewrite_markdown_paths` et `rewrite_notebook_paths` sont des aides explicites de post-traitement. Ils n'effectuent aucune traduction et n'écrivent rien dans le projet.

## Flux de revue

Le flux de revue déterministe est :

1. Analyser les arguments CLI ou les paramètres de l'API.
2. Normaliser les codes de langue demandés.
3. Construire une ou plusieurs cibles de revue à partir de `root_dir`, `root_dirs` ou `groups`.
4. Limiter éventuellement les fichiers source avec `--changed-from`.
5. Exécuter des vérifications déterministes pour la structure, la fraîcheur des traductions, l'intégrité Markdown et les chemins de liens/images locaux.
6. Afficher soit une sortie texte soit du Markdown au format GitHub.
7. Quitter avec un échec lorsque des erreurs de revue sont trouvées.

Le flux de revue ne nécessite pas de clés d'API et doit rester adapté à l'intégration continue des pull requests. Le workflow de la pull request écrit un résumé de vérification à chaque exécution et n'ajoute un commentaire sur la PR que lorsque `co-op-review` échoue.

## Site de documentation

Le site de documentation est configuré par :

```text
mkdocs.yml
requirements-docs.txt
docs/
```

Le répertoire `docs/` est la source canonique de la documentation. N'ajoutez pas de nouveaux guides destinés aux utilisateurs finaux en dehors de ce répertoire, sauf si le projet introduit intentionnellement une autre surface de documentation publiée.

Build locally :

```bash
python -m pip install -r requirements-docs.txt
python -m mkdocs build --strict
```

Preview locally :

```bash
python -m mkdocs serve
```

Le site généré est écrit dans `site/`, qui est ignoré par git.

## Workflow GitHub Pages

.github/workflows/docs.yml construit le site sur les pull requests et le déploie lors des pushes vers `main`.

Le workflow installe :

```bash
pip install -r requirements-docs.txt
```

Le workflow de docs installe uniquement la chaîne d'outils de documentation. `mkdocs.yml` pointe `mkdocstrings` vers `src/` afin que les pages de l'API publique puissent être générées à partir de l'arbre source sans installer l'ensemble complet des dépendances d'exécution. Si de futures docs API nécessitent d'importer des fournisseurs d'exécution optionnels pendant la construction, mettez à jour à la fois `.github/workflows/docs.yml` et ce guide.

## Seuil de qualité de la documentation

Avant de fusionner des modifications de documentation, exécutez :

```bash
python -m mkdocs build --strict
git diff --check
```

Utilisez des builds stricts afin que les liens cassés, les entrées de navigation invalides et les problèmes de rendu de l'API soient détectés rapidement.