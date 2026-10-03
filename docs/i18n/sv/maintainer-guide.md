# Underhållsguide

Denna sida sammanfattar hur API:t, CLI:n och dokumentationssajten är kopplade till varandra.

## Offentlig API-gräns

Det stabila Python-API:t exporteras från:

```python
co_op_translator.api
```

Det offentliga API:et är organiserat i hjälpverktyg för innehållsöversättning, hjälpverktyg för sökvägsomskrivning, projektorkestrering och granskning:

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

`TranslationStateProvider` är persistensgränsen för hostade integrationer.
Den måste hålla genererade kandidater åtskilda från accepterade baslinjer så att en
icke sammanslagen översättning inte kan bli sanningskällan.

När du lägger till nya offentliga API:er, uppdatera:

- `src/co_op_translator/api/__init__.py`
- `docs/api.md`
- relevanta API-tester under `tests/co_op_translator/`, såsom `test_api.py` eller `test_review_api.py`

Undvik att dokumentera lägre nivåns `core`-moduler som ett stabilt API om projektet inte avser att stödja dem direkt.

## CLI-ingångspunkter

Paketet definierar dessa Poetry-skript:

```toml
[tool.poetry.scripts]
translate = "co_op_translator.__main__:main"
evaluate = "co_op_translator.__main__:main"
migrate-links = "co_op_translator.__main__:main"
co-op-review = "co_op_translator.__main__:main"
co-op-translator-mcp = "co_op_translator.mcp.server:main"
```

`src/co_op_translator/__main__.py` dirigerar baserat på skriptnamn:

- `translate` anropar `co_op_translator.cli.translate.translate_command`
- `evaluate` anropar `co_op_translator.cli.evaluate.evaluate_command`
- `migrate-links` anropar `co_op_translator.cli.migrate_links.migrate_links_command`
- `co-op-review` anropar `co_op_translator.cli.review.review_command`

`co-op-translator-mcp` kringgår `__main__.py` och anropar `co_op_translator.mcp.server:main` direkt.

När du lägger till eller ändrar CLI-alternativ, uppdatera:

- det relevanta kommandot i `src/co_op_translator/cli/*.py`
- `docs/cli.md`
- CLI-relaterade tester, om beteendet ändras

## MCP-server

MCP-servern är implementerad i:

```python
co_op_translator.mcp.server
```

Servern omsluter avsiktligt det offentliga Python-API:et istället för att anropa lägre nivåns `core`-moduler. Behåll denna gräns så att MCP-klienter, Python-anropare och CLI:n delar samma beteende.

När du lägger till eller ändrar MCP-verktyg, uppdatera:

- `src/co_op_translator/mcp/server.py`
- `tests/co_op_translator/test_mcp_server.py`
- `docs/mcp.md`
- `docs/api.md` om den offentliga API-ytan ändras

Repository-översättningsverktyg kan anropas av modellen via MCP och kan skriva många filer. Behåll `dry_run=True` som standard och kräva `confirm_write=True` innan projektöversättning utan dry-run.

## Översättningsflöde

Det övergripande projektöversättningsflödet är:

1. Tolka CLI-argument eller API-parametrar.
2. Validera LLM-konfigurationen med `LLMConfig`.
3. Validera Azure AI Vision när bildöversättning är valt.
4. Normalisera språkkoder.
5. Upptäck äldre alias för språkmappar.
6. Uppskatta översättningsvolym.
7. Uppdatera README:s språk-/kurssektioner när det är tillämpligt.
8. Delegera projektöversättningen till `ProjectTranslator`.
9. `ProjectTranslator` delegerar filhantering till `TranslationManager`.

`TranslationManager` är sammansatt av fokuserade mixins för filtyper:

- `ProjectMarkdownTranslationMixin` hanterar läsning av Markdown-filer, innehållsöversättning, sökvägsomskrivning, metadata, ansvarsfriskrivningar och skrivningar.
- `ProjectNotebookTranslationMixin` hanterar läsning av notebook-filer, översättning av Markdown-celler, sökvägsomskrivning, metadata, ansvarsfriskrivningar och skrivningar.
- `ProjectImageTranslationMixin` hanterar bildupptäckt, textutvinning/översättning, renderade bildskrivningar och metadata.

De lägre nivåernas innehålls-API:er hoppar över projektarbetsflödet:

1. `translate_markdown_content` och `translate_notebook_content` översätter endast innehåll i minnet.
2. `translate_image_content` översätter text i en enskild bild och returnerar ett renderat bildobjekt.
3. `rewrite_markdown_paths` och `rewrite_notebook_paths` är explicita efterbehandlingshjälpmedel. De utför ingen översättning och inga projekt-skrivningar.

## Granskningsflöde

Det deterministiska granskningsflödet är:

1. Tolka CLI-argument eller API-parametrar.
2. Normalisera begärda språkkoder.
3. Bygg ett eller flera granskningsmål från `root_dir`, `root_dirs` eller `groups`.
4. Valfritt: begränsa källfiler med `--changed-from`.
5. Kör deterministiska kontroller för struktur, översättningsfärskhet, Markdown-integritet och lokala länk-/bildsökvägar.
6. Skriv ut antingen textutdata eller GitHub-flavored Markdown.
7. Avsluta med fel när granskningsfel hittas.

Granskningsflödet kräver inga API-nycklar och förblir tillgängligt för lokala kontroller eller opt-in konsument-CI. Det här repositoryt kör inte `co-op-review` automatiskt på varje pull request.

## Dokumentationssajt

Dokumentationssajten konfigureras av:

```text
mkdocs.yml
requirements-docs.txt
docs/
```

`docs/`-katalogen är den kanoniska dokumentationskällan. Lägg inte till nya användarguider utanför denna katalog om inte projektet avsiktligt inför en annan publicerad dokumentationsyta.

Bygg lokalt:

```bash
python -m pip install -r requirements-docs.txt
python -m mkdocs build --strict
```

Förhandsgranska lokalt:

```bash
python -m mkdocs serve
```

Den genererade sajten skrivs till `site/`, som ignoreras av git.

## GitHub Pages-arbetsflöde

`.github/workflows/docs.yml` bygger sajten vid pull requests och distribuerar den vid pushar till `main`.

Arbetetsflödet installerar:

```bash
pip install -r requirements-docs.txt
```

Dokumentationsarbetsflödet installerar endast dokumentationsverktygskedjan. `mkdocs.yml` pekar `mkdocstrings` mot `src/` så att sidor för offentliga API:er kan renderas från källträdet utan att installera hela runtime-beroendesatsen. Om framtida API-dokumentationer kräver import av valfria runtime-leverantörer under byggnationen, uppdatera både `.github/workflows/docs.yml` och den här guiden samtidigt.

## Dokumentationens kvalitetskrav

Innan dokumentationsändringar slås samman, kör:

```bash
python -m mkdocs build --strict
git diff --check
```

Använd strikta byggen så att brutna länkar, ogiltiga navigeringsposter och problem vid API-rendering upptäcks tidigt.