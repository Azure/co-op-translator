# Onderhoudershandleiding

Deze pagina vat samen hoe de API, CLI en documentatiesite met elkaar verbonden zijn.

## Publieke API-grens

De stabiele Python-API wordt geëxporteerd vanuit:

```python
co_op_translator.api
```

De publieke API is georganiseerd in helpers voor contentvertaling, helpers voor padherschrijving, projectorchestratie, en beoordeling:

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

`TranslationStateProvider` is de persistentiegrens voor gehoste integraties.
Het moet gegenereerde kandidaten gescheiden houden van geaccepteerde baselines zodat een
niet-geïntegreerde vertaling geen bron van waarheid kan worden.

Wanneer je nieuwe publieke API's toevoegt, werk dan bij:

- `src/co_op_translator/api/__init__.py`
- `docs/api.md`
- relevant API tests onder `tests/co_op_translator/`, zoals `test_api.py` of `test_review_api.py`

Vermijd het documenteren van lager-niveau `core` modules als stabiele API tenzij het project van plan is ze rechtstreeks te ondersteunen.

## CLI-entrypunten

Het pakket definieert deze Poetry-scripts:

```toml
[tool.poetry.scripts]
translate = "co_op_translator.__main__:main"
evaluate = "co_op_translator.__main__:main"
migrate-links = "co_op_translator.__main__:main"
co-op-review = "co_op_translator.__main__:main"
co-op-translator-mcp = "co_op_translator.mcp.server:main"
```

`src/co_op_translator/__main__.py` stuurt aan op basis van de scriptnaam:

- `translate` roept `co_op_translator.cli.translate.translate_command` aan
- `evaluate` roept `co_op_translator.cli.evaluate.evaluate_command` aan
- `migrate-links` roept `co_op_translator.cli.migrate_links.migrate_links_command` aan
- `co-op-review` roept `co_op_translator.cli.review.review_command` aan

`co-op-translator-mcp` omzeilt `__main__.py` en roept `co_op_translator.mcp.server:main` direct aan.

Wanneer je CLI-opties toevoegt of wijzigt, werk dan bij:

- the relevant `src/co_op_translator/cli/*.py` command
- `docs/cli.md`
- CLI-gerelateerde tests, als het gedrag verandert

## MCP-server

De MCP-server is geïmplementeerd in:

```python
co_op_translator.mcp.server
```

De server wikkelt opzettelijk de publieke Python-API in in plaats van lagere-niveau `core` modules aan te roepen. Houd deze grens intact zodat MCP-clients, Python-oproepers, en de CLI hetzelfde gedrag delen.

Wanneer je MCP-tools toevoegt of wijzigt, werk dan bij:

- `src/co_op_translator/mcp/server.py`
- `tests/co_op_translator/test_mcp_server.py`
- `docs/mcp.md`
- `docs/api.md` if the public API surface changes

Repository-vertalingshulpmiddelen zijn model-aanroepbaar via MCP en kunnen veel bestanden schrijven. Houd `dry_run=True` als standaard en vereis `confirm_write=True` voordat projectvertaling buiten dry-run plaatsvindt.

## Vertaalproces

Het projectvertalingsproces op hoofdlijnen is:

1. Parseer CLI-argumenten of API-parameters.
2. Valideer LLM-configuratie met `LLMConfig`.
3. Valideer Azure AI Vision wanneer beeldvertaling is geselecteerd.
4. Normaliseer taalcodes.
5. Detecteer verouderde aliasnamen van taalmappen.
6. Schat het vertaalvolume.
7. Werk README-taal-/cursussecties bij indien van toepassing.
8. Delegeer projectvertaling aan `ProjectTranslator`.
9. `ProjectTranslator` delegeert bestandsverwerking aan `TranslationManager`.

`TranslationManager` is samengesteld uit mixins gericht op bestandstypen:

- `ProjectMarkdownTranslationMixin` behandelt Markdown-bestandlezingen, contentvertaling, padherschrijving, metadata, disclaimers, en schrijfbewerkingen.
- `ProjectNotebookTranslationMixin` behandelt notebook-bestandslezingen, vertaling van Markdown-cellen, padherschrijving, metadata, disclaimers, en schrijfbewerkingen.
- `ProjectImageTranslationMixin` behandelt afbeeldingsdetectie, tekstextractie/-vertaling, het wegschrijven van gerenderde afbeeldingen, en metadata.

De content-API's op een lager niveau slaan de projectworkflow over:

1. `translate_markdown_content` en `translate_notebook_content` vertalen alleen inhoud in het geheugen.
2. `translate_image_content` vertaalt tekst in één afbeelding en retourneert een gerenderd afbeeldingsobject.
3. `rewrite_markdown_paths` en `rewrite_notebook_paths` zijn expliciete hulpmiddelen voor nabewerking. Ze voeren geen vertaling uit en schrijven niets weg naar het project.

## Beoordelingsproces

Het deterministische beoordelingsproces is:

1. Parseer CLI-argumenten of API-parameters.
2. Normaliseer gevraagde taalcodes.
3. Bouw één of meer review-doelen vanuit `root_dir`, `root_dirs`, of `groups`.
4. Beperk optioneel de bronbestanden met `--changed-from`.
5. Voer deterministische controles uit voor structuur, actualiteit van vertalingen, Markdown-integriteit, en lokale link-/afbeeldingspaden.
6. Geef tekstoutput of GitHub-flavored Markdown weer.
7. Stop met een foutstatus wanneer reviewfouten worden gevonden.

Het reviewproces vereist geen API-sleutels en blijft beschikbaar voor lokale controles of opt-in consument CI. Deze repository voert `co-op-review` niet automatisch uit bij elke pull request.

## Documentatiesite

De docs-site wordt geconfigureerd door:

```text
mkdocs.yml
requirements-docs.txt
docs/
```

De `docs/` directory is de canonieke documentatiebron. Voeg geen nieuwe eindgebruikershandleidingen toe buiten deze directory tenzij het project opzettelijk een ander gepubliceerd documentatieoppervlak introduceert.

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

## GitHub Pages-werkstroom

`.github/workflows/docs.yml` bouwt de site bij pull requests en zet deze bij pushes naar `main` in.

The workflow installs:

```bash
pip install -r requirements-docs.txt
```

De docs-workflow installeert alleen de toolchain voor documentatie. `mkdocs.yml` wijst `mkdocstrings` naar `src/` zodat openbare API-pagina's vanuit de bronboom kunnen worden gerenderd zonder het volledige runtime-afhankelijkhedenpakket te installeren. Als toekomstige API-docs vereisen dat optionele runtime-providers tijdens de build worden geïmporteerd, werk dan zowel `.github/workflows/docs.yml` als deze gids bij.

## Kwaliteitsnorm voor documentatie

Before merging documentation changes, run:

```bash
python -m mkdocs build --strict
git diff --check
```

Gebruik strikte builds zodat kapotte links, ongeldige navigatie-items en problemen bij het renderen van de API vroegtijdig falen.
