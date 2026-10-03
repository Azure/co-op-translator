# Gabay ng Tagapangasiwa

Ibinubuod ng pahinang ito kung paano magkakabit ang API, CLI, at ang site ng dokumentasyon.

## Pampublikong hangganan ng API

Ang matatag na Python API ay inia-export mula sa:

```python
co_op_translator.api
```

Ang pampublikong API ay inayos sa mga katulong para sa pagsasalin ng nilalaman, mga katulong sa pag-rewrite ng landas, pamamahala ng proyekto, at pagsusuri:

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

`TranslationStateProvider` ay ang hangganan ng persistensya para sa mga naka-host na integrasyon.
Dapat nitong panatilihing hiwalay ang mga nabuo na kandidato mula sa mga tinanggap na baseline upang ang isang
ang pagsasalin na hindi pa na-merge ay hindi dapat maging pinagmumulan ng katotohanan.

Kapag nagdaragdag ng bagong pampublikong API, i-update ang:

- `src/co_op_translator/api/__init__.py`
- `docs/api.md`
- ang mga kaugnay na test ng API sa ilalim ng `tests/co_op_translator/`, tulad ng `test_api.py` o `test_review_api.py`

Iwasang idokumento ang mas mababang-level na `core` modules bilang matatag na API maliban kung nilalayong suportahan ito ng proyekto nang direkta.

## Mga entry point ng CLI

Tinukoy ng package ang mga Poetry script na ito:

```toml
[tool.poetry.scripts]
translate = "co_op_translator.__main__:main"
evaluate = "co_op_translator.__main__:main"
migrate-links = "co_op_translator.__main__:main"
co-op-review = "co_op_translator.__main__:main"
co-op-translator-mcp = "co_op_translator.mcp.server:main"
```

`src/co_op_translator/__main__.py` ay nagdi-dispatch ayon sa pangalan ng script:

- `translate` tumatawag sa `co_op_translator.cli.translate.translate_command`
- `evaluate` tumatawag sa `co_op_translator.cli.evaluate.evaluate_command`
- `migrate-links` tumatawag sa `co_op_translator.cli.migrate_links.migrate_links_command`
- `co-op-review` tumatawag sa `co_op_translator.cli.review.review_command`

`co-op-translator-mcp` ay nilalampasan ang `__main__.py` at tumatawag nang direkta sa `co_op_translator.mcp.server:main`.

Kapag nagdaragdag o nagbabago ng mga opsyon ng CLI, i-update ang:

- ang kaugnay na `src/co_op_translator/cli/*.py` command
- `docs/cli.md`
- Mga test na may kaugnayan sa CLI, kung magbabago ang pag-uugali

## MCP server

Ang MCP server ay ipinatupad sa:

```python
co_op_translator.mcp.server
```

Sinasadyang binabalot ng server ang pampublikong Python API sa halip na tumawag sa mas mababang-level na `core` modules. Panatilihin ang hangganang ito nang buo upang ang mga kliyente ng MCP, mga tumatawag mula sa Python, at ang CLI ay magbahagi ng parehong pag-uugali.

Kapag nagdaragdag o nagbabago ng mga tool ng MCP, i-update ang:

- `src/co_op_translator/mcp/server.py`
- `tests/co_op_translator/test_mcp_server.py`
- `docs/mcp.md`
- `docs/api.md` kung magbabago ang saklaw ng pampublikong API

Ang mga tool sa pagsasalin ng repositoryo ay maaaring tawagin ng modelo sa pamamagitan ng MCP at maaaring magsulat ng maraming file. Panatilihin ang `dry_run=True` bilang default at hingin ang `confirm_write=True` bago ang pagsasalin ng proyekto na hindi dry-run.

## Daloy ng Pagsasalin

Ang mataas-na-antasing daloy ng pagsasalin ng proyekto ay:

1. I-parse ang mga argument ng CLI o mga parameter ng API.
2. I-validate ang konfigurasyon ng LLM gamit ang `LLMConfig`.
3. I-validate ang Azure AI Vision kapag pinili ang pagsasalin ng imahe.
4. I-normalize ang mga code ng wika.
5. Tuklasin ang mga legacy na alias ng folder ng wika.
6. Tantiyahin ang dami ng pagsasalin.
7. I-update ang mga seksyon ng wika/kurso sa README kapag naaangkop.
8. I-delegate ang pagsasalin ng proyekto sa `ProjectTranslator`.
9. `ProjectTranslator` ini-delegate ang pagproseso ng mga file sa `TranslationManager`.

`TranslationManager` ay binubuo ng mga mixin na nakatuon sa uri ng file:

- `ProjectMarkdownTranslationMixin` humahawak sa pag-basa ng Markdown file, pagsasalin ng nilalaman, pag-rewrite ng landas, metadata, mga disclaimer, at pagsusulat.
- `ProjectNotebookTranslationMixin` humahawak sa pag-basa ng notebook file, pagsasalin ng Markdown-cell, pag-rewrite ng landas, metadata, mga disclaimer, at pagsusulat.
- `ProjectImageTranslationMixin` humahawak sa pagtuklas ng imahe, pag-extract/pagsasalin ng teksto, pagsusulat ng na-render na imahe, at metadata.

Ang mga mababang-level na content API ay hindi dumadaan sa workflow ng proyekto:

1. `translate_markdown_content` at `translate_notebook_content` ay nagsasalin lamang ng in-memory na nilalaman.
2. `translate_image_content` nagsasalin ng teksto sa isang imahe at nagbabalik ng isang na-render na image object.
3. `rewrite_markdown_paths` at `rewrite_notebook_paths` ay mga tahasang post-processing na katulong. Hindi sila gumaganap ng pagsasalin at hindi nagsusulat sa proyekto.

## Daloy ng Pagsusuri

Ang deterministic na daloy ng pagsusuri ay:

1. I-parse ang mga argument ng CLI o mga parameter ng API.
2. I-normalize ang hinihinging mga code ng wika.
3. Bumuo ng isa o higit pang mga review target mula sa `root_dir`, `root_dirs`, o `groups`.
4. Opsyonal na limitahan ang mga source file gamit ang `--changed-from`.
5. Patakbuhin ang deterministic na mga tseke para sa istruktura, pagiging bago ng pagsasalin, integridad ng Markdown, at lokal na mga landas ng link/imahe.
6. I-print alinman ang text output o GitHub-flavored Markdown.
7. Lumabas na may kabiguan kapag may natagpuang mga error sa pagsusuri.

Hindi nangangailangan ng API key ang daloy ng pagsusuri at nananatiling magagamit para sa lokal na mga tseke o opt-in na consumer CI. Hindi awtomatikong pinapatakbo ng repositoryong ito ang `co-op-review` sa bawat pull request.

## Site ng Dokumentasyon

Ang docs site ay naka-configure sa pamamagitan ng:

```text
mkdocs.yml
requirements-docs.txt
docs/
```

Ang direktoryong `docs/` ang kanonikong pinagmulan ng dokumentasyon. Huwag magdagdag ng mga bagong gabay para sa end-user sa labas ng direktoryong ito maliban kung sadyang magpapakilala ang proyekto ng isa pang publikadong dokumentasyon.

Buuin nang lokal:

```bash
python -m pip install -r requirements-docs.txt
python -m mkdocs build --strict
```

Preview nang lokal:

```bash
python -m mkdocs serve
```

Ang nabuo na site ay isinusulat sa `site/`, na ini-ignore ng git.

## Workflow ng GitHub Pages

`.github/workflows/docs.yml` binubuo ang site sa pull requests at dine-deploy ito sa mga push patungo sa `main`.

Ini-install ng workflow ang:

```bash
pip install -r requirements-docs.txt
```

Ini-install lamang ng docs workflow ang toolchain para sa dokumentasyon. Itinuturo ng `mkdocs.yml` ang `mkdocstrings` sa `src/` kaya ang mga pahina ng pampublikong API ay maaaring ma-render mula sa source tree nang hindi ini-install ang buong hanay ng runtime dependencies. Kung sa hinaharap ang mga dokumento ng API ay mangangailangan ng pag-import ng opsyonal na runtime providers habang binubuo, i-update nang sabay ang `.github/workflows/docs.yml` at ang gabay na ito.

## Pamantayan sa Kalidad ng Docs

Bago i-merge ang mga pagbabago sa dokumentasyon, patakbuhin:

```bash
python -m mkdocs build --strict
git diff --check
```

Gumamit ng mahigpit na builds upang ang mga sirang link, hindi wastong mga entry sa nabigasyon, at mga isyu sa pag-render ng API ay agad na mabigo.