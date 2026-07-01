# Gabay para sa Tagapangasiwa

Nilalaman ng pahinang ito ay nagbubuod kung paano pinag-uugnay ang API, CLI, at site ng dokumentasyon.

## Pampublikong hangganan ng API

Ang matatag na Python API ay ine-export mula sa:

```python
co_op_translator.api
```

Ang pampublikong API ay nakaayos sa mga helper para sa pagsasalin ng nilalaman, mga helper para sa pagsusulat-muli ng path, pag-orchestration ng proyekto, at pag-review:

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

Kapag nagdaragdag ng bagong pampublikong mga API, i-update:

- `src/co_op_translator/api/__init__.py`
- `docs/api.md`
- mga kaugnay na API tests sa ilalim ng `tests/co_op_translator/`, tulad ng `test_api.py` o `test_review_api.py`

Iwasang idokumento ang mas mababang-level na `core` modules bilang matatag na API maliban kung ang proyekto ay naglalayong suportahan ang mga ito nang direkta.

## Mga entry point ng CLI

Nagtatakda ang package ng mga sumusunod na Poetry scripts:

```toml
[tool.poetry.scripts]
translate = "co_op_translator.__main__:main"
evaluate = "co_op_translator.__main__:main"
migrate-links = "co_op_translator.__main__:main"
co-op-review = "co_op_translator.__main__:main"
co-op-translator-mcp = "co_op_translator.mcp.server:main"
```

`src/co_op_translator/__main__.py` ay nagdi-dispatch base sa pangalan ng script:

- `translate` tumatawag sa `co_op_translator.cli.translate.translate_command`
- `evaluate` tumatawag sa `co_op_translator.cli.evaluate.evaluate_command`
- `migrate-links` tumatawag sa `co_op_translator.cli.migrate_links.migrate_links_command`
- `co-op-review` tumatawag sa `co_op_translator.cli.review.review_command`

Ang `co-op-translator-mcp` ay binabypass ang `__main__.py` at tumatawag nang direkta sa `co_op_translator.mcp.server:main`.

Kapag nagdaragdag o nagbabago ng mga opsyon ng CLI, i-update:

- ang kaugnay na `src/co_op_translator/cli/*.py` command
- `docs/cli.md`
- mga tests na may kaugnayan sa CLI, kung nagbabago ang behavior

## MCP server

Ang MCP server ay ipinatupad sa:

```python
co_op_translator.mcp.server
```

Sinasadyang binalot ng server ang pampublikong Python API sa halip na tumawag sa mas mababang-level na `core` modules. Panatilihin ang hangganang ito upang ang mga MCP client, Python caller, at ang CLI ay magbahagi ng parehong behavior.

Kapag nagdaragdag o nagbabago ng mga MCP tool, i-update:

- `src/co_op_translator/mcp/server.py`
- `tests/co_op_translator/test_mcp_server.py`
- `docs/mcp.md`
- `docs/api.md` kung nagbabago ang pampublikong API surface

Ang mga repository translation tool ay maaaring tawagin bilang model-callable sa pamamagitan ng MCP at maaaring magsulat ng maraming file. Panatilihing `dry_run=True` bilang default at mangailangan ng `confirm_write=True` bago magsagawa ng non-dry-run na pagsasalin ng proyekto.

## Daloy ng pagsasalin

Ang mataas-na-level na daloy ng pagsasalin ng proyekto ay:

1. I-parse ang mga argumento ng CLI o mga parameter ng API.
2. I-validate ang LLM configuration gamit ang `LLMConfig`.
3. I-validate ang Azure AI Vision kapag napili ang pagsasalin ng imahe.
4. I-normalize ang mga language codes.
5. Tuklasin ang mga legacy language folder aliases.
6. Tantyahin ang dami ng pagsasalin.
7. I-update ang mga seksyon ng README na may language/course kapag naaangkop.
8. Idelegate ang pagsasalin ng proyekto sa `ProjectTranslator`.
9. Ang `ProjectTranslator` ay nagde-delegate ng pagproseso ng file sa `TranslationManager`.

Ang `TranslationManager` ay binubuo mula sa mga focused file-type mixins:

- `ProjectMarkdownTranslationMixin` humahawak ng pagbasa ng mga Markdown file, pagsasalin ng nilalaman, pagsusulat-muli ng mga path, metadata, mga paunawa, at pagsusulat.
- `ProjectNotebookTranslationMixin` humahawak ng pagbasa ng mga notebook file, pagsasalin ng Markdown-cell, pagsusulat-muli ng mga path, metadata, mga paunawa, at pagsusulat.
- `ProjectImageTranslationMixin` humahawak ng pagdiskubre ng mga imahe, pagkuha/pagsasalin ng teksto, pagsusulat ng na-render na imahe, at metadata.

Ang mas mababang-level na content APIs ay nilalaktawan ang project workflow:

1. `translate_markdown_content` at `translate_notebook_content` ay nagsasalin ng in-memory na nilalaman lamang.
2. `translate_image_content` ay nagsasalin ng teksto sa isang solong imahe at nagbabalik ng isang rendered image object.
3. `rewrite_markdown_paths` at `rewrite_notebook_paths` ay mga explicit post-processing helpers. Hindi sila nagsasagawa ng pagsasalin at hindi nagsusulat sa proyekto.

## Daloy ng review

Ang deterministic na daloy ng review ay:

1. I-parse ang mga argumento ng CLI o mga parameter ng API.
2. I-normalize ang mga hinihinging language codes.
3. Bumuo ng isa o higit pang review targets mula sa `root_dir`, `root_dirs`, o `groups`.
4. Opsyonal na limitahan ang mga source file gamit ang `--changed-from`.
5. Patakbuhin ang deterministic na mga tseke para sa istruktura, pagiging sariwa ng pagsasalin, integridad ng Markdown, at mga lokal na link/image path.
6. I-print alinman sa text output o GitHub-flavored Markdown.
7. Lumabas na may failure kapag may natagpuang mga error sa review.

Ang review flow ay hindi nangangailangan ng API keys at dapat manatiling angkop para sa pull request CI. Ang pull request workflow ay sumusulat ng isang check summary sa bawat takbo at nagpo-post lang ng PR comment kapag nabigo ang `co-op-review`.

## Site ng dokumentasyon

Ang docs site ay naka-configure sa pamamagitan ng:

```text
mkdocs.yml
requirements-docs.txt
docs/
```

Ang `docs/` directory ang kanonikal na pinagmulan ng dokumentasyon. Huwag magdagdag ng mga bagong end-user guides sa labas ng direktoryong ito maliban kung sinasadya ng proyekto na magpakilala ng isa pang inilathalang documentation surface.

I-build nang lokal:

```bash
python -m pip install -r requirements-docs.txt
python -m mkdocs build --strict
```

I-preview nang lokal:

```bash
python -m mkdocs serve
```

Ang nagawang site ay isinusulat sa `site/`, na naka-ignore ng git.

## GitHub Pages workflow

Ang `.github/workflows/docs.yml` ay nagbuo ng site sa pull requests at nag-deploy nito sa mga push sa `main`.

Ang workflow ay nag-iinstall ng:

```bash
pip install -r requirements-docs.txt
```

Ang docs workflow ay nag-iinstall lamang ng documentation toolchain. Itinuturo ng `mkdocs.yml` ang `mkdocstrings` sa `src/` kaya ang mga pampublikong API page ay maaaring i-render mula sa source tree nang hindi ini-install ang buong runtime dependency set. Kung ang mga susunod na API docs ay mangangailangan ng pag-import ng optional runtime providers habang nagbu-build, i-update kapwa ang `.github/workflows/docs.yml` at ang gabay na ito nang sabay.

## Pamantayan ng kalidad ng Docs

Bago pagsamahin ang mga pagbabago sa dokumentasyon, patakbuhin:

```bash
python -m mkdocs build --strict
git diff --check
```

Gumamit ng mahigpit na builds upang ang mga sirang link, invalid na navigation entries, at mga isyu sa pag-render ng API ay mabigo nang maaga.