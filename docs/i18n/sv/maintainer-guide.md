# Underhållarguide

Denna sida sammanfattar hur API:et, CLI:t och dokumentationssajten är kopplade tillsammans.

## Publikt API-gränssnitt

Det stabila Python-API:et exporteras från:

```python
co_op_translator.api
```

Det publika API:et är indelat i hjälpkomponenter för innehållsöversättning, hjälpkomponenter för sökvägsomskrivning, projektorkestrering och granskning:

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

När du lägger till nya publika API:er, uppdatera:

- `src/co_op_translator/api/__init__.py`
- `docs/api.md`
- relevant API-tester under `tests/co_op_translator/`, såsom `test_api.py` eller `test_review_api.py`

Undvik att dokumentera lägre nivåers `core`-moduler som ett stabilt API om projektet inte avser att stödja dem direkt.

## CLI-entrépunkter

Paketet definierar dessa Poetry-skript:

```toml
[tool.poetry.scripts]
translate = "co_op_translator.__main__:main"
evaluate = "co_op_translator.__main__:main"
migrate-links = "co_op_translator.__main__:main"
co-op-review = "co_op_translator.__main__:main"
co-op-translator-mcp = "co_op_translator.mcp.server:main"
```

`src/co_op_translator/__main__.py` dirigerar efter skriptnamn:

- `translate` anropar `co_op_translator.cli.translate.translate_command`
- `evaluate` anropar `co_op_translator.cli.evaluate.evaluate_command`
- `migrate-links` anropar `co_op_translator.cli.migrate_links.migrate_links_command`
- `co-op-review` anropar `co_op_translator.cli.review.review_command`

`co-op-translator-mcp` omgår `__main__.py` och anropar `co_op_translator.mcp.server:main` direkt.

När du lägger till eller ändrar CLI-alternativ, uppdatera:

- det relevanta kommandot i `src/co_op_translator/cli/*.py`
- `docs/cli.md`
- CLI-relaterade tester, om beteendet ändras

## MCP-server

MCP-servern är implementerad i:

```python
co_op_translator.mcp.server
```

Servern kapslar medvetet in det publika Python-API:et istället för att anropa lägre nivåers `core`-moduler. Behåll denna gräns så att MCP-klienter, Python-anropare och CLI:t delar samma beteende.

När du lägger till eller ändrar MCP-verktyg, uppdatera:

- `src/co_op_translator/mcp/server.py`
- `tests/co_op_translator/test_mcp_server.py`
- `docs/mcp.md`
- `docs/api.md` om den publika API-ytan ändras

Verktyg för översättning av repository är anropbara via modeller genom MCP och kan skriva många filer. Behåll `dry_run=True` som standard och kräva `confirm_write=True` innan projektöversättning utan dry run.

## Översättningsflöde

Det övergripande projektöversättningsflödet är:

1. Analysera CLI-argument eller API-parametrar.
2. Validera LLM-konfigurationen med `LLMConfig`.
3. Validera Azure AI Vision när bildöversättning är vald.
4. Normalisera språkkoder.
5. Identifiera äldre alias för språkmappar.
6. Uppskatta översättningsvolymen.
7. Uppdatera README:s språk-/kursavsnitt när det är tillämpligt.
8. Deleguera projektöversättningen till `ProjectTranslator`.
9. `ProjectTranslator` delegerar filbearbetning till `TranslationManager`.

`TranslationManager` är sammansatt av fokuserade mixins för filtyper:

- `ProjectMarkdownTranslationMixin` hanterar läsning av Markdown-filer, innehållsöversättning, sökvägsomskrivning, metadata, ansvarsfriskrivningar och filskrivningar.
- `ProjectNotebookTranslationMixin` hanterar läsning av notebook-filer, översättning av Markdown-celler, sökvägsomskrivning, metadata, ansvarsfriskrivningar och filskrivningar.
- `ProjectImageTranslationMixin` hanterar upptäckt av bilder, textutvinning/översättning, skrivning av renderade bilder och metadata.

De lägre nivåernas innehålls-API:er hoppar över projektarbetsflödet:

1. `translate_markdown_content` och `translate_notebook_content` översätter endast innehåll i minnet.
2. `translate_image_content` översätter text i en enskild bild och returnerar ett renderat bildobjekt.
3. `rewrite_markdown_paths` och `rewrite_notebook_paths` är explicita efterbearbetningshjälpare. De utför ingen översättning och inga projekt-skrivningar.

## Granskningsflöde

Det deterministiska granskningsflödet är:

1. Analysera CLI-argument eller API-parametrar.
2. Normalisera begärda språkkoder.
3. Bygg ett eller flera granskningsmål från `root_dir`, `root_dirs` eller `groups`.
4. Begränsa valfritt källfiler med `--changed-from`.
5. Kör deterministiska kontroller för struktur, översättningarnas aktualitet, Markdown-integritet och lokala länk-/bildsökvägar.
6. Skriv ut antingen textutdata eller GitHub-flavored Markdown.
7. Avsluta med fel när granskningsfel hittas.

Granskningsflödet kräver inga API-nycklar och bör förbli lämpligt för pull request CI. Pull request-arbetsflödet skriver en kontrollsammanfattning vid varje körning och postar endast en PR-kommentar när `co-op-review` misslyckas.

## Dokumentationssajten

Dokumentsajten konfigureras av:

```text
mkdocs.yml
requirements-docs.txt
docs/
```

`docs/`-katalogen är den kanoniska dokumentationskällan. Lägg inte till nya slutanvändarguider utanför denna katalog om projektet inte avsiktligt introducerar en annan publicerad dokumentationsyta.

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

.github/workflows/docs.yml bygger sajten vid pull requests och distribuerar den vid pushar till `main`.

Arbetsflödet installerar:

```bash
pip install -r requirements-docs.txt
```

Dokumentsarbetsflödet installerar endast dokumentationsverktygskedjan. `mkdocs.yml` pekar `mkdocstrings` mot `src/` så att publika API-sidor kan renderas från källträdet utan att installera hela runtime-beroendesatsen. Om framtida API-dokumentation kräver att valfria runtime-leverantörer importeras under bygget, uppdatera både `.github/workflows/docs.yml` och denna guide tillsammans.

## Dokumentationskvalitetsnivå

Innan du mergar dokumentationsändringar, kör:

```bash
python -m mkdocs build --strict
git diff --check
```

Använd strikta byggen så att brutna länkar, ogiltiga navigeringsposter och problem med API-rendering upptäcks tidigt.