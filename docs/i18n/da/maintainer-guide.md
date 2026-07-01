# Vedligeholdervejledning

Denne side opsummerer, hvordan API'en, CLI'en og dokumentationssitet er forbundet.

## Offentlig API-grænse

Den stabile Python-API eksporteres fra:

```python
co_op_translator.api
```

Den offentlige API er organiseret i hjælpere til indholdsoversættelse, hjælpere til sti-omskrivning, projektstyring og gennemgang:

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

Når der tilføjes nye offentlige API'er, opdater:

- `src/co_op_translator/api/__init__.py`
- `docs/api.md`
- relevant API-tests under `tests/co_op_translator/`, såsom `test_api.py` eller `test_review_api.py`

Undlad at dokumentere lavniveau-`core`-moduler som stabile API'er, medmindre projektet har til hensigt at understøtte dem direkte.

## CLI-entrépunkter

Pakken definerer disse Poetry-scripts:

```toml
[tool.poetry.scripts]
translate = "co_op_translator.__main__:main"
evaluate = "co_op_translator.__main__:main"
migrate-links = "co_op_translator.__main__:main"
co-op-review = "co_op_translator.__main__:main"
co-op-translator-mcp = "co_op_translator.mcp.server:main"
```

`src/co_op_translator/__main__.py` videresender efter scriptnavn:

- `translate` kalder `co_op_translator.cli.translate.translate_command`
- `evaluate` kalder `co_op_translator.cli.evaluate.evaluate_command`
- `migrate-links` kalder `co_op_translator.cli.migrate_links.migrate_links_command`
- `co-op-review` kalder `co_op_translator.cli.review.review_command`

`co-op-translator-mcp` omgår `__main__.py` og kalder `co_op_translator.mcp.server:main` direkte.

Når CLI-indstillinger tilføjes eller ændres, opdater:

- den relevante `src/co_op_translator/cli/*.py` kommando
- `docs/cli.md`
- CLI-relaterede tests, hvis adfærden ændres

## MCP-server

MCP-serveren er implementeret i:

```python
co_op_translator.mcp.server
```

Serveren pakker bevidst den offentlige Python-API ind i stedet for at kalde lavniveau-`core`-moduler. Bevar denne grænseflade, så MCP-klienter, Python-kaldere og CLI'en deler samme adfærd.

Når MCP-værktøjer tilføjes eller ændres, opdater:

- `src/co_op_translator/mcp/server.py`
- `tests/co_op_translator/test_mcp_server.py`
- `docs/mcp.md`
- `docs/api.md` hvis den offentlige API-flade ændres

Repository-oversættelsesværktøjer kan kaldes via modeller gennem MCP og kan skrive mange filer. Hold `dry_run=True` som standard og kræv `confirm_write=True` før projektoversættelse uden dry_run.

## Oversættelsesflow

Det overordnede flow for projektoversættelse er:

1. Pars CLI-argumenter eller API-parametre.
2. Valider LLM-konfigurationen med `LLMConfig`.
3. Valider Azure AI Vision, når billedoversættelse er valgt.
4. Normaliser sprogkoder.
5. Opdag ældre aliaser for sprogmapper.
6. Anslå oversættelsesomfang.
7. Opdater README-sprog-/kursussektioner når det er relevant.
8. Deleger projektoversættelse til `ProjectTranslator`.
9. `ProjectTranslator` delegerer filbehandling til `TranslationManager`.

`TranslationManager` er sammensat af fokuserede filtype-mixins:

- `ProjectMarkdownTranslationMixin` håndterer læsning af Markdown-filer, indholdsoversættelse, sti-omskrivning, metadata, ansvarsfraskrivelser og skrivning.
- `ProjectNotebookTranslationMixin` håndterer læsning af notebook-filer, oversættelse af Markdown-celler, sti-omskrivning, metadata, ansvarsfraskrivelser og skrivning.
- `ProjectImageTranslationMixin` håndterer billedopdagelse, tekstudtræk/oversættelse, skrivning af gengivne billeder og metadata.

De lavere niveau indholds-API'er springer projektworkflowet over:

1. `translate_markdown_content` og `translate_notebook_content` oversætter kun indhold i hukommelsen.
2. `translate_image_content` oversætter tekst i et enkelt billede og returnerer et gengivet billedobjekt.
3. `rewrite_markdown_paths` og `rewrite_notebook_paths` er eksplicitte efterbehandlingshjælpere. De foretager ingen oversættelse og skriver ikke til projektet.

## Gennemgangsflow

Det deterministiske gennemgangsflow er:

1. Pars CLI-argumenter eller API-parametre.
2. Normaliser de anmodede sprogkoder.
3. Opbyg ét eller flere gennemgangsmål fra `root_dir`, `root_dirs` eller `groups`.
4. Begræns eventuelt kildefiler med `--changed-from`.
5. Kør deterministiske checks for struktur, aktualitet af oversættelser, Markdown-integritet og lokale link-/billedstier.
6. Udskriv enten tekstoutput eller GitHub-variant af Markdown.
7. Afslut med fejl, når der findes gennemgangsfejl.

Gennemgangsflowet kræver ikke API-nøgler og bør forblive velegnet til pull request CI. Pull request-workflowet skriver et tjekresumé ved hver kørsel og poster kun en PR-kommentar, når `co-op-review` fejler.

## Dokumentationssitet

Dokumentationssitet konfigureres af:

```text
mkdocs.yml
requirements-docs.txt
docs/
```

`docs/`-mappen er den kanoniske dokumentationskilde. Tilføj ikke nye slutbrugerguider uden for denne mappe, medmindre projektet bevidst indfører en anden offentlig dokumentationsflade.

Byg lokalt:

```bash
python -m pip install -r requirements-docs.txt
python -m mkdocs build --strict
```

Forhåndsvis lokalt:

```bash
python -m mkdocs serve
```

Det genererede site skrives til `site/`, som er ignoreret af git.

## GitHub Pages-workflow

`.github/workflows/docs.yml` bygger sitet på pull requests og udruller det ved pushes til `main`.

Workflowet installerer:

```bash
pip install -r requirements-docs.txt
```

Dokumentationsworkflowet installerer kun dokumentationsværktøjskæden. `mkdocs.yml` peger `mkdocstrings` på `src/`, så sider for offentlig API kan gengives fra kildetræet uden at installere hele runtime-afhængighedssættet. Hvis fremtidige API-dokumenter kræver import af valgfrie runtime-udbydere under buildet, opdater både `.github/workflows/docs.yml` og denne guide samtidig.

## Dokumentationskvalitetskrav

Før ændringer i dokumentationen flettes, kør:

```bash
python -m mkdocs build --strict
git diff --check
```

Brug strenge builds, så brudte links, ugyldige navigationsposter og problemer med API-gengivelse fejler tidligt.