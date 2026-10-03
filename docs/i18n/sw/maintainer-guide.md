# Mwongozo wa Msimamizi

Ukurasa huu unafupisha jinsi API, CLI, na tovuti ya nyaraka zinavyounganishwa.

## Mipaka ya API ya Umma

API thabiti ya Python inatolewa kutoka:

```python
co_op_translator.api
```

API ya umma imepangwa kuwa visaidizi vya tafsiri ya yaliyomo, visaidizi vya kuandika upya njia, upangaji wa miradi, na ukaguzi:

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

`TranslationStateProvider` ni mpaka wa uhifadhi kwa miunganisho iliyowekwa mwenyeji.
Inapaswa kuweka wagombea waliotengenezwa tofauti na misingi iliyokubaliwa ili
tafsiri isiyounganishwa hawezi kuwa chanzo cha ukweli.

Unapoongeza API mpya za umma, sasisha:

- `src/co_op_translator/api/__init__.py`
- `docs/api.md`
- vipimo vinavyohusiana vya API chini ya `tests/co_op_translator/`, kama `test_api.py` au `test_review_api.py`

Epuka kuandika nyaraka kwa moduli za chini za `core` kama API thabiti isipokuwa mradi unakusudia kuziunga mkono moja kwa moja.

## Nukta za kuingia za CLI

Kifurushi kinafafanua skripti hizi za Poetry:

```toml
[tool.poetry.scripts]
translate = "co_op_translator.__main__:main"
evaluate = "co_op_translator.__main__:main"
migrate-links = "co_op_translator.__main__:main"
co-op-review = "co_op_translator.__main__:main"
co-op-translator-mcp = "co_op_translator.mcp.server:main"
```

`src/co_op_translator/__main__.py` hutuma kwa kutumia jina la skripti:

- `translate` inaita `co_op_translator.cli.translate.translate_command`
- `evaluate` inaita `co_op_translator.cli.evaluate.evaluate_command`
- `migrate-links` inaita `co_op_translator.cli.migrate_links.migrate_links_command`
- `co-op-review` inaita `co_op_translator.cli.review.review_command`

`co-op-translator-mcp` hupitisha `__main__.py` na inaita `co_op_translator.mcp.server:main` moja kwa moja.

Unapoongeza au kubadilisha chaguo za CLI, sasisha:

- amri husika `src/co_op_translator/cli/*.py`
- `docs/cli.md`
- Vipimo vinavyohusiana na CLI, ikiwa tabia inabadilika

## MCP server

Seva ya MCP imetekelezwa katika:

```python
co_op_translator.mcp.server
```

Seva kwa makusudi inafunika API ya Python ya umma badala ya kuita moduli za `core` za ngazi ya chini. Weka mpaka huu bila kubadilika ili wateja wa MCP, waiteaji wa Python, na CLI washirikiane kwa tabia ile ile.

Unapoongeza au kubadilisha zana za MCP, sasisha:

- `src/co_op_translator/mcp/server.py`
- `tests/co_op_translator/test_mcp_server.py`
- `docs/mcp.md`
- `docs/api.md` ikiwa uso wa API ya umma unabadilika

Zana za tafsiri za hazina zinaweza kuitwa kwa mfano kupitia MCP na zinaweza kuandika faili nyingi. Weka `dry_run=True` kama chaguo-msingi na hitaji `confirm_write=True` kabla ya tafsiri ya mradi isiyokuwa dry-run.

## Mtiririko wa Tafsiri

Mtiririko wa juu wa tafsiri ya mradi ni:

1. Changanua hoja za CLI au vigezo vya API.
2. Thibitisha usanidi wa LLM kwa `LLMConfig`.
3. Thibitisha Azure AI Vision wakati tafsiri ya picha imechaguliwa.
4. Sawaisha misimbo ya lugha.
5. Gundua majina mbadala ya folda za lugha za zamani.
6. Kukadiria kiasi cha tafsiri.
7. Sasisha sehemu za lugha/kozi za README inapofaa.
8. Toa jukumu la tafsiri ya mradi kwa `ProjectTranslator`.
9. `ProjectTranslator` hutoa uendeshaji wa faili kwa `TranslationManager`.

`TranslationManager` inaundwa kutoka kwa mixin za aina ya faili zilizolengwa:

- `ProjectMarkdownTranslationMixin` hushughulikia usomaji wa faili za Markdown, tafsiri ya yaliyomo, uandishi upya wa njia, metadata, taarifa za kukataa, na uandishi.
- `ProjectNotebookTranslationMixin` hushughulikia usomaji wa faili za notebook, tafsiri ya seli za Markdown, uandishi upya wa njia, metadata, taarifa za kukataa, na uandishi.
- `ProjectImageTranslationMixin` hushughulikia ugunduzi wa picha, uchomaji/tafsiri ya maandishi, uandishi wa picha zilizochorwa, na metadata.

API za maudhui za ngazi ya chini zinaruka mtiririko wa kazi wa mradi:

1. `translate_markdown_content` na `translate_notebook_content` zinafasiri yaliyomo katika kumbukumbu pekee.
2. `translate_image_content` inatafsiri maandishi katika picha moja na inarejesha kitu cha picha iliyochorwa.
3. `rewrite_markdown_paths` na `rewrite_notebook_paths` ni visaidizi vya uchakataji wa baada ya wazi. Hawaitekelezi tafsiri wala uandishi wa mradi.

## Mtiririko wa Mapitio

Mtiririko wa ukaguzi unaotegemewa ni:

1. Changanua hoja za CLI au vigezo vya API.
2. Sawaisha misimbo ya lugha zilizohitajika.
3. Jenga lengo moja au zaidi la ukaguzi kutoka `root_dir`, `root_dirs`, au `groups`.
4. Hiari punguza faili za chanzo kwa `--changed-from`.
5. Endesha ukaguzi wa deterministic kwa muundo, ubora wa tafsiri, uadilifu wa Markdown, na njia za viungo/picha za ndani.
6. Chapisha ama matokeo ya maandishi au Markdown yenye ladha ya GitHub.
7. Toka kwa hitimisho la kushindwa wakati makosa ya ukaguzi yanapopatikana.

Mtiririko wa ukaguzi hautegemei funguo za API na unabaki kupatikana kwa ukaguzi wa ndani au CI ya mteja inayojiunga kwa hiari. Hifadhi hii haisiendesha `co-op-review` moja kwa moja kwenye kila pull request.

## Tovuti ya nyaraka

Tovuti ya nyaraka imewekwa kwa:

```text
mkdocs.yml
requirements-docs.txt
docs/
```

Katalogi ya `docs/` ni chanzo rasmi cha nyaraka. Usiongeze mwongozo mpya wa mtumiaji wa mwisho nje ya katalogi hii isipokuwa mradi uteule kuanzisha uso mwingine wa nyaraka uliochapishwa.

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

## Mtiririko wa kazi wa GitHub Pages

`.github/workflows/docs.yml` inajenga tovuti kwenye ombi za pull na kuipeleka (deploy) wakati wa kutuma (push) kwa `main`.

The workflow installs:

```bash
pip install -r requirements-docs.txt
```

Mtiririko wa kazi wa nyaraka unasakinisha tu zana za kuandaa nyaraka. `mkdocs.yml` inaelekeza `mkdocstrings` kwa `src/` ili kurasa za API za umma ziweze kuundwa kutoka mti wa chanzo bila kusakinisha seti kamili ya utegemezi wa wakati wa utekelezaji. Ikiwa nyaraka za API zijazo zitahitaji kuingiza watoa huduma za wakati wa utekelezaji wa hiari wakati wa ujenzi, sasisha `.github/workflows/docs.yml` na mwongozo huu pamoja.

## Kiwango cha ubora wa nyaraka

Before merging documentation changes, run:

```bash
python -m mkdocs build --strict
git diff --check
```

Tumia ujenzi mkali ili viungo vilivyovunjika, vipengee vya urambazaji visivyofaa, na masuala ya uwasilishaji wa API yashindikane mapema.