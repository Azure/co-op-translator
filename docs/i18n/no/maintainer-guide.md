# Vedlikeholderguide

Denne siden oppsummerer hvordan API-et, CLI-en og dokumentasjonsnettstedet er koblet sammen.

## Offentlig API-grense

Den stabile Python-API-en eksporteres fra:

```python
co_op_translator.api
```

Det offentlige API-et er organisert i hjelpefunksjoner for innholdsoversettelse, hjelpefunksjoner for sti-omskriving, prosjektorkestrering og gjennomgang:

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

`TranslationStateProvider` er persistensgrensen for hostede integrasjoner.
Den må holde genererte kandidater adskilt fra aksepterte baselines slik at en
ikke-sammenslått oversettelse ikke kan bli sannhetskilden.

Når du legger til nye offentlige API-er, oppdater:

- `src/co_op_translator/api/__init__.py`
- `docs/api.md`
- relevant API tests under `tests/co_op_translator/`, such as `test_api.py` or `test_review_api.py`

Unngå å dokumentere lavnivå `core`-moduler som stabilt API med mindre prosjektet har til hensikt å støtte dem direkte.

## CLI-inngangspunkter

Pakken definerer disse Poetry-skriptene:

```toml
[tool.poetry.scripts]
translate = "co_op_translator.__main__:main"
evaluate = "co_op_translator.__main__:main"
migrate-links = "co_op_translator.__main__:main"
co-op-review = "co_op_translator.__main__:main"
co-op-translator-mcp = "co_op_translator.mcp.server:main"
```

`src/co_op_translator/__main__.py` videresender basert på skriptnavn:

- `translate` kaller `co_op_translator.cli.translate.translate_command`
- `evaluate` kaller `co_op_translator.cli.evaluate.evaluate_command`
- `migrate-links` kaller `co_op_translator.cli.migrate_links.migrate_links_command`
- `co-op-review` kaller `co_op_translator.cli.review.review_command`

`co-op-translator-mcp` omgår `__main__.py` og kaller `co_op_translator.mcp.server:main` direkte.

Når du legger til eller endrer CLI-alternativer, oppdater:

- den relevante `src/co_op_translator/cli/*.py`-kommandoen
- `docs/cli.md`
- CLI-relaterte tester, hvis atferden endres

## MCP-server

MCP-serveren er implementert i:

```python
co_op_translator.mcp.server
```

Serveren pakker bevisst inn det offentlige Python-API-et i stedet for å kalle lavnivå `core`-moduler. Behold denne grensen slik at MCP-klienter, Python-kallere og CLI-en deler samme oppførsel.

Når du legger til eller endrer MCP-verktøy, oppdater:

- `src/co_op_translator/mcp/server.py`
- `tests/co_op_translator/test_mcp_server.py`
- `docs/mcp.md`
- `docs/api.md` hvis den offentlige API-overflaten endres

Repository-oversettelsesverktøy kan kalles av modellen via MCP og kan skrive mange filer. Hold `dry_run=True` som standard og krev `confirm_write=True` før prosjektoversettelse uten dry_run.

## Oversettelsesflyt

Den overordnede prosjektoversettelsesflyten er:

1. Parse CLI-argumenter eller API-parametre.
2. Valider LLM-konfigurasjon med `LLMConfig`.
3. Valider Azure AI Vision når bildeoversettelse er valgt.
4. Normaliser språkkoder.
5. Oppdag eldre aliaser for språkmapper.
6. Estimer oversettelsesvolumet.
7. Oppdater README-språk- og kursseksjoner når det er aktuelt.
8. Deleger prosjektoversettelsen til `ProjectTranslator`.
9. `ProjectTranslator` delegerer filbehandling til `TranslationManager`.

`TranslationManager` er satt sammen av fokuserte mixins for filtyper:

- `ProjectMarkdownTranslationMixin` håndterer lesing av Markdown-filer, innholdsoversettelse, sti-omskriving, metadata, ansvarsfraskrivelser og skriving.
- `ProjectNotebookTranslationMixin` håndterer lesing av notatbokfiler, oversettelse av Markdown-celler, sti-omskriving, metadata, ansvarsfraskrivelser og skriving.
- `ProjectImageTranslationMixin` håndterer bildeoppdagelse, tekstuttrekk/oversettelse, skriving av rendrerte bilder og metadata.

De lavnivå innholds-API-ene hopper over prosjektarbeidsflyten:

1. `translate_markdown_content` og `translate_notebook_content` oversetter kun innhold i minnet.
2. `translate_image_content` oversetter tekst i et enkelt bilde og returnerer et rendrert bildeobjekt.
3. `rewrite_markdown_paths` og `rewrite_notebook_paths` er eksplisitte etterbehandlingshjelpere. De utfører ingen oversettelse og ingen prosjekt-skrivinger.

## Gjennomgangsflyt

Den deterministiske gjennomgangsflyten er:

1. Parse CLI-argumenter eller API-parametre.
2. Normaliser forespurte språkkoder.
3. Bygg ett eller flere gjennomgangsmål fra `root_dir`, `root_dirs`, eller `groups`.
4. Valgfritt: begrens kildefiler med `--changed-from`.
5. Kjør deterministiske kontroller for struktur, oversettelsenes ferskhet, Markdown-integritet og lokale lenke-/bildefilstier.
6. Skriv ut enten tekstutdata eller GitHub-flavored Markdown.
7. Avslutt med en feilkode når gjennomgangsfeil oppdages.

Gjennomgangsfloden krever ikke API-nøkler og er fortsatt tilgjengelig for lokale kontroller eller opt-in forbruker-CI. Dette depotet kjører ikke `co-op-review` automatisk på hver pull request.

## Dokumentasjonsnettsted

Dokumentasjonsnettstedet konfigureres av:

```text
mkdocs.yml
requirements-docs.txt
docs/
```

Katalogen `docs/` er den kanoniske dokumentasjonskilden. Ikke legg til nye brukerveiledninger utenfor denne katalogen med mindre prosjektet med hensikt introduserer en annen publisert dokumentasjonsflate.

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

`.github/workflows/docs.yml` bygger nettstedet ved pull requests og distribuerer det ved push til `main`.

Arbeidsflyten installerer:

```bash
pip install -r requirements-docs.txt
```

Dokumentasjonsarbeidsflyten installerer bare dokumentasjonsverktøykjeden. `mkdocs.yml` peker `mkdocstrings` mot `src/` slik at offentlige API-sider kan rendres fra kildetreet uten å installere hele settet av runtime-avhengigheter. Hvis fremtidige API-dokumenter krever import av valgfrie runtime-leverandører under bygging, oppdater både `.github/workflows/docs.yml` og denne guiden samtidig.

## Kvalitetskrav for dokumentasjon

Før du slår sammen dokumentasjonsendringer, kjør:

```bash
python -m mkdocs build --strict
git diff --check
```

Bruk strenge bygg slik at brutte lenker, ugyldige navigasjonsoppføringer og problemer med API-rendering feiler tidlig.