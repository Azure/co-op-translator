# Onderhoudersgids

Deze pagina vat samen hoe de API, CLI en de documentatiesite met elkaar verbonden zijn.

## Publieke API-grens

De stabiele Python API wordt geëxporteerd vanuit:

```python
co_op_translator.api
```

De publieke API is georganiseerd in hulpfuncties voor inhoudsvertaling, hulpfuncties voor padherschrijving, projectorchestratie en review:

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

Wanneer je nieuwe publieke API's toevoegt, werk dan bij:

- `src/co_op_translator/api/__init__.py`
- `docs/api.md`
- relevante API-tests in `tests/co_op_translator/`, zoals `test_api.py` of `test_review_api.py`

Vermijd het documenteren van lagere `core`-modules als stabiele API tenzij het project van plan is ze direct te ondersteunen.

## CLI-entrypoints

Het pakket definieert deze Poetry-scripts:

```toml
[tool.poetry.scripts]
translate = "co_op_translator.__main__:main"
evaluate = "co_op_translator.__main__:main"
migrate-links = "co_op_translator.__main__:main"
co-op-review = "co_op_translator.__main__:main"
co-op-translator-mcp = "co_op_translator.mcp.server:main"
```

`src/co_op_translator/__main__.py` verwerkt op basis van de scriptnaam:

- `translate` roept `co_op_translator.cli.translate.translate_command` aan
- `evaluate` roept `co_op_translator.cli.evaluate.evaluate_command` aan
- `migrate-links` roept `co_op_translator.cli.migrate_links.migrate_links_command` aan
- `co-op-review` roept `co_op_translator.cli.review.review_command` aan

`co-op-translator-mcp` omzeilt `__main__.py` en roept direct `co_op_translator.mcp.server:main` aan.

Wanneer je CLI-opties toevoegt of wijzigt, werk dan bij:

- het relevante `src/co_op_translator/cli/*.py`-commando
- `docs/cli.md`
- CLI-gerelateerde tests, als het gedrag verandert

## MCP-server

De MCP-server is geïmplementeerd in:

```python
co_op_translator.mcp.server
```

De server wikkelt opzettelijk de publieke Python API in in plaats van lagere-`core`-modules aan te roepen. Houd deze grens intact zodat MCP-clients, Python-aanroepen en de CLI hetzelfde gedrag delen.

Wanneer je MCP-tools toevoegt of wijzigt, werk dan bij:

- `src/co_op_translator/mcp/server.py`
- `tests/co_op_translator/test_mcp_server.py`
- `docs/mcp.md`
- `docs/api.md` als de publieke API-oppervlakte verandert

Repository-vertalingstools kunnen via MCP door het model worden aangeroepen en kunnen veel bestanden schrijven. Houd `dry_run=True` als standaard en vereis `confirm_write=True` voordat projectvertaling buiten de dry-run wordt uitgevoerd.

## Vertaalstroom

De hoog-niveau projectvertalingstroom is:

1. Parseer CLI-argumenten of API-parameters.
2. Valideer de LLM-configuratie met `LLMConfig`.
3. Valideer Azure AI Vision wanneer beeldvertaling is geselecteerd.
4. Normaliseer taalcodes.
5. Detecteer legacy-taalmappen aliassen.
6. Schat het vertaalvolume.
7. Werk README taal- en cursussecties bij indien van toepassing.
8. Delegeer projectvertaling aan `ProjectTranslator`.
9. `ProjectTranslator` delegeert bestandsverwerking aan `TranslationManager`.

`TranslationManager` is samengesteld uit gerichte bestandstype-mixins:

- `ProjectMarkdownTranslationMixin` behandelt het lezen van Markdown-bestanden, inhoudsvertaling, padherschrijving, metadata, disclaimers en het schrijven.
- `ProjectNotebookTranslationMixin` behandelt het lezen van notebook-bestanden, vertaling van Markdown-cellen, padherschrijving, metadata, disclaimers en het schrijven.
- `ProjectImageTranslationMixin` behandelt het ontdekken van afbeeldingen, tekstextractie/-vertaling, het wegschrijven van gerenderde afbeeldingen en metadata.

De lagere-niveau content-API's slaan de projectworkflow over:

1. `translate_markdown_content` en `translate_notebook_content` vertalen alleen inhoud in het geheugen.
2. `translate_image_content` vertaalt tekst in een enkele afbeelding en geeft een gerenderd afbeeldingsobject terug.
3. `rewrite_markdown_paths` en `rewrite_notebook_paths` zijn expliciete naverwerkingshelpers. Ze voeren geen vertaling uit en schrijven niets naar het project.

## Reviewproces

Het deterministische reviewproces is:

1. Parseer CLI-argumenten of API-parameters.
2. Normaliseer gevraagde taalcodes.
3. Bouw één of meer reviewdoelen op uit `root_dir`, `root_dirs` of `groups`.
4. Beperk optioneel de bronbestanden met `--changed-from`.
5. Voer deterministische controles uit op structuur, actualiteit van vertalingen, Markdown-integriteit en lokale link-/afbeeldingspaden.
6. Print ofwel tekstoutput of GitHub-geflavoured Markdown.
7. Stop met een foutstatus wanneer reviewfouten worden gevonden.

Het reviewproces vereist geen API-sleutels en moet geschikt blijven voor pull request CI. De pull request-workflow schrijft bij elke run een controlesamenvatting en plaatst alleen een PR-opmerking wanneer `co-op-review` faalt.

## Documentatiesite

De documentatiesite wordt geconfigureerd door:

```text
mkdocs.yml
requirements-docs.txt
docs/
```

De `docs/`-map is de canonieke documentatiebron. Voeg geen nieuwe eindgebruikersgidsen buiten deze map toe, tenzij het project bewust een ander gepubliceerd documentatieoppervlak introduceert.

Lokaal bouwen:

```bash
python -m pip install -r requirements-docs.txt
python -m mkdocs build --strict
```

Lokaal bekijken:

```bash
python -m mkdocs serve
```

De gegenereerde site wordt geschreven naar `site/`, dat door git wordt genegeerd.

## GitHub Pages-workflow

`.github/workflows/docs.yml` bouwt de site bij pull requests en publiceert die bij pushes naar `main`.

De workflow installeert:

```bash
pip install -r requirements-docs.txt
```

De docs-workflow installeert alleen de documentatietoolketen. `mkdocs.yml` wijst `mkdocstrings` naar `src/` zodat publieke API-pagina's uit de bronboom kunnen worden gerenderd zonder de volledige runtime-afhankelijkheden te installeren. Als toekomstige API-documentatie het importeren van optionele runtime-providers vereist tijdens de build, werk dan zowel `.github/workflows/docs.yml` als deze gids bij.

## Kwaliteitsnorm voor documentatie

Voordat je documentatiewijzigingen samenvoegt, voer uit:

```bash
python -m mkdocs build --strict
git diff --check
```

Gebruik strikte builds zodat gebroken links, ongeldige navigatie-items en API-renderingproblemen vroegtijdig falen.