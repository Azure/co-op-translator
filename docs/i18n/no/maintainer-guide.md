# Vedlikeholderveiledning

Denne siden oppsummerer hvordan API-en, CLI-en og dokumentasjonsnettstedet er koblet sammen.

## Offentlig API-grense

Den stabile Python-API-en eksporteres fra:

```python
co_op_translator.api
```

Den offentlige API-en er organisert i hjelpefunksjoner for innholdsoversettelse, hjelpefunksjoner for sti-omskriving, prosjektorkestrering og gjennomgang:

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

Når du legger til nye offentlige API-er, oppdater:

- `src/co_op_translator/api/__init__.py`
- `docs/api.md`
- relevante API-tester under `tests/co_op_translator/`, slik som `test_api.py` eller `test_review_api.py`

Unngå å dokumentere lavnivås `core`-moduler som stabilt API med mindre prosjektet har til hensikt å støtte dem direkte.

## CLI inngangspunkter

Pakken definerer disse Poetry-skriptene:

```toml
[tool.poetry.scripts]
translate = "co_op_translator.__main__:main"
evaluate = "co_op_translator.__main__:main"
migrate-links = "co_op_translator.__main__:main"
co-op-review = "co_op_translator.__main__:main"
co-op-translator-mcp = "co_op_translator.mcp.server:main"
```

`src/co_op_translator/__main__.py` ruter etter skriptnavn:

- `translate` kaller `co_op_translator.cli.translate.translate_command`
- `evaluate` kaller `co_op_translator.cli.evaluate.evaluate_command`
- `migrate-links` kaller `co_op_translator.cli.migrate_links.migrate_links_command`
- `co-op-review` kaller `co_op_translator.cli.review.review_command`

`co-op-translator-mcp` omgår `__main__.py` og kaller `co_op_translator.mcp.server:main` direkte.

Når du legger til eller endrer CLI-alternativer, oppdater:

- den relevante `src/co_op_translator/cli/*.py`-kommandoen
- `docs/cli.md`
- CLI-relaterte tester, hvis atferd endres

## MCP-server

MCP-serveren er implementert i:

```python
co_op_translator.mcp.server
```

Serveren pakker bevisst inn den offentlige Python-API-en i stedet for å kalle lavnivås `core`-moduler. Hold denne grensen intakt slik at MCP-klienter, Python-kallere og CLI-en deler samme oppførsel.

Når du legger til eller endrer MCP-verktøy, oppdater:

- `src/co_op_translator/mcp/server.py`
- `tests/co_op_translator/test_mcp_server.py`
- `docs/mcp.md`
- `docs/api.md` hvis den offentlige API-flaten endres

Repository-oversettelsesverktøy er modell-kallbare gjennom MCP og kan skrive mange filer. Hold `dry_run=True` som standard og krev `confirm_write=True` før prosjektoversettelse uten dry-run.

## Oversettelsesflyt

Den overordnede prosjektoversettelsesflyten er:

1. Analyser CLI-argumenter eller API-parametere.
2. Valider LLM-konfigurasjon med `LLMConfig`.
3. Valider Azure AI Vision når bildeoversettelse er valgt.
4. Normaliser språkkoder.
5. Oppdag eldre alias for språkmapper.
6. Estimer oversettelsesvolum.
7. Oppdater README-språk/kursseksjoner når aktuelt.
8. Deleger prosjektoversettelse til `ProjectTranslator`.
9. `ProjectTranslator` delegerer filbehandling til `TranslationManager`.

`TranslationManager` er sammensatt av fokuserte filtype-mixins:

- `ProjectMarkdownTranslationMixin` håndterer lesing av Markdown-filer, innholdsoversettelse, sti-omskriving, metadata, ansvarsfraskrivelser og skriving.
- `ProjectNotebookTranslationMixin` håndterer notatbokfil-lesing, Markdown-celle-oversettelse, sti-omskriving, metadata, ansvarsfraskrivelser og skriving.
- `ProjectImageTranslationMixin` håndterer bildeoppdagelse, tekstekstraksjon/oversettelse, rendrede bildefiler og metadata.

De lavere nivå innholds-API-ene hopper over prosjektarbeidsflyten:

1. `translate_markdown_content` og `translate_notebook_content` oversetter bare innhold i minnet.
2. `translate_image_content` oversetter tekst i ett enkelt bilde og returnerer et rendret bildeobjekt.
3. `rewrite_markdown_paths` og `rewrite_notebook_paths` er eksplisitte etterbehandlingshjelpere. De utfører ingen oversettelse og ingen prosjekt-skrivinger.

## Gjennomgangsflyt

Den deterministiske gjennomgangsflyten er:

1. Analyser CLI-argumenter eller API-parametere.
2. Normaliser forespurte språkkoder.
3. Bygg ett eller flere gjennomgangsmål fra `root_dir`, `root_dirs`, eller `groups`.
4. Valgfritt begrens kildefiler med `--changed-from`.
5. Kjør deterministiske sjekker for struktur, oversettelsesaktualitet, Markdown-integritet og lokale lenke-/bildestier.
6. Skriv ut enten tekstutdata eller GitHub-flavored Markdown.
7. Avslutt med feil når gjennomgangsfeil blir funnet.

Gjennomgangsflyten krever ikke API-nøkler og bør forbli egnet for pull request CI. Pull request-arbeidsflyten skriver en sjekksammendrag ved hver kjøring og legger kun ut en PR-kommentar når `co-op-review` feiler.

## Dokumentasjonsnettsted

Dokumentasjonssiden er konfigurert av:

```text
mkdocs.yml
requirements-docs.txt
docs/
```

`docs/`-katalogen er den kanoniske dokumentasjonskilden. Ikke legg til nye brukerveiledninger utenfor denne katalogen med mindre prosjektet bevisst introduserer et annet publisert dokumentasjonsområde.

Bygg lokalt:

```bash
python -m pip install -r requirements-docs.txt
python -m mkdocs build --strict
```

Forhåndsvis lokalt:

```bash
python -m mkdocs serve
```

Det genererte nettstedet skrives til `site/`, som er ignorert av git.

## GitHub Pages-arbeidsflyt

`.github/workflows/docs.yml` bygger nettstedet på pull requests og distribuerer det ved push til `main`.

Arbeidsflyten installerer:

```bash
pip install -r requirements-docs.txt
```

Dokumentasjonsarbeidsflyten installerer kun dokumentasjonsverktøykjeden. `mkdocs.yml` peker `mkdocstrings` mot `src/` slik at offentlige API-sider kan rendres fra kildetreet uten å installere hele runtime-avhengighetssettet. Hvis fremtidige API-dokumenter krever import av valgfrie runtime-leverandører under byggingen, oppdater både `.github/workflows/docs.yml` og denne veiledningen samtidig.

## Kvalitetskrav for dokumentasjon

Før du slår sammen dokumentasjonsendringer, kjør:

```bash
python -m mkdocs build --strict
git diff --check
```

Bruk strenge bygg slik at ødelagte lenker, ugyldige navigasjonsoppføringer og problemer med API-rendering feiler tidlig.