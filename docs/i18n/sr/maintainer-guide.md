# Водич за одржаваоца

Ова страница сумира како су API, CLI и сајт документације повезани.

## Јавна граница API-ја

Стабилан Python API се експортује из:

```python
co_op_translator.api
```

Јавни API је организован у помоћнике за превођење садржаја, помоћнике за преписивање путања, оркестрацију пројеката и преглед:

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

Када додате нове јавне API-је, ажурирајте:

- `src/co_op_translator/api/__init__.py`
- `docs/api.md`
- relevant API tests under `tests/co_op_translator/`, such as `test_api.py` or `test_review_api.py`

Избегавајте документацију нижих `core` модула као стабилан API осим ако пројекат не намерава да их директно подржава.

## CLI entry points

Пакет дефинише ове Poetry скрипте:

```toml
[tool.poetry.scripts]
translate = "co_op_translator.__main__:main"
evaluate = "co_op_translator.__main__:main"
migrate-links = "co_op_translator.__main__:main"
co-op-review = "co_op_translator.__main__:main"
co-op-translator-mcp = "co_op_translator.mcp.server:main"
```

`src/co_op_translator/__main__.py` прослеђује по имену скрипте:

- `translate` позива `co_op_translator.cli.translate.translate_command`
- `evaluate` позива `co_op_translator.cli.evaluate.evaluate_command`
- `migrate-links` позива `co_op_translator.cli.migrate_links.migrate_links_command`
- `co-op-review` позива `co_op_translator.cli.review.review_command`

`co-op-translator-mcp` заобилази `__main__.py` и директно позива `co_op_translator.mcp.server:main`.

Када додате или промените CLI опције, ажурирајте:

- одговарајућу команду у `src/co_op_translator/cli/*.py`
- `docs/cli.md`
- CLI-related tests, if behavior changes

## MCP server

MCP сервер је реализован у:

```python
co_op_translator.mcp.server
```

Сервер намерно омотава јавни Python API уместо да позива ниже `core` модуле. Задржите ову границу нетакнутом тако да MCP клијенти, Python позиваоци и CLI деле исто понашање.

Када додате или промените MCP алате, ажурирајте:

- `src/co_op_translator/mcp/server.py`
- `tests/co_op_translator/test_mcp_server.py`
- `docs/mcp.md`
- `docs/api.md` if the public API surface changes

Алатке за превођење у репозиторијуму су позивљиве моделом преко MCP и могу писати много фајлова. Држите `dry_run=True` као подразумевано и захтевајте `confirm_write=True` пре него што се изврши превођење пројекта ван dry run-а.

## Translation flow

Главни ток превођења пројекта је:

1. Парсирајте CLI аргументе или API параметре.
2. Потврдите конфигурацију LLM-а помоћу `LLMConfig`.
3. Потврдите Azure AI Vision када је изабрано превођење слика.
4. Нормализујте кодове језика.
5. Откријте наслеђене алтернативне називе фолдера за језике.
6. Процените обим превођења.
7. Ажурирајте README одељке за језик/курс када је применљиво.
8. Делегирајте превођење пројекта на `ProjectTranslator`.
9. `ProjectTranslator` делегира обраду фајлова на `TranslationManager`.

`TranslationManager` се састоји од mixin-ова фокусираних на тип фајла:

- `ProjectMarkdownTranslationMixin` обрађује читање Markdown фајлова, превођење садржаја, преписивање путања, метаподатке, одрицања и уписивање фајлова.
- `ProjectNotebookTranslationMixin` обрађује читање notebook фајлова, превођење Markdown ћелија, преписивање путања, метаподатке, одрицања и уписивање фајлова.
- `ProjectImageTranslationMixin` обрађује откривање слика, екстракцију/превођење текста, упис рендерованих слика и метаподатке.

Нижи ниво садржајних API-ја прескаче радни ток пројекта:

1. `translate_markdown_content` and `translate_notebook_content` преводе само садржај који је у меморији.
2. `translate_image_content` преводи текст у једној слици и враћа рендеровани објекат слике.
3. `rewrite_markdown_paths` and `rewrite_notebook_paths` су експлицитни помоћници за пост-процесу. Они не врше превођење нити уписивање у пројекат.

## Review flow

Детерминистички ток прегледа је:

1. Парсирајте CLI аргументе или API параметре.
2. Нормализујте тражене кодове језика.
3. Изградите један или више циљева прегледа из `root_dir`, `root_dirs` или `groups`.
4. Опционо ограничите изворне фајлове помоћу `--changed-from`.
5. Покрените детерминистичке провере структуре, свежине превода, интегритета Markdown-а и локалних путања линкова/слика.
6. Испишите или текстуални излаз или Markdown у GitHub стилу.
7. Завршите са грешком када се пронађу грешке у прегледу.

Ток прегледа не захтева API кључеве и треба да остане погодан за CI у оквиру захтева за повлачење (pull request). Радни ток захтева за повлачење записује резиме провере при сваком покретању и само поставља коментар на PR када `co-op-review` закаже.

## Documentation site

Сајт документације је конфигурисан помоћу:

```text
mkdocs.yml
requirements-docs.txt
docs/
```

Директоријум `docs/` је канонски извор документације. Не додајте нове водиче за крајње кориснике изван овог директоријума осим ако пројекат намерно не уведе другу објављену површину документације.

Build locally:

```bash
python -m pip install -r requirements-docs.txt
python -m mkdocs build --strict
```

Preview locally:

```bash
python -m mkdocs serve
```

Генерисани сајт се уписује у `site/`, који је игнорисан од стране git-а.

## GitHub Pages workflow

`.github/workflows/docs.yml` гради сајт на pull request-овима и деплојира га приликом push-ова на `main`.

The workflow installs:

```bash
pip install -r requirements-docs.txt
```

Радни ток за документацију инсталира само алате за документацију. `mkdocs.yml` усмерује `mkdocstrings` на `src/` тако да странице јавног API-ја могу бити рендероване из изворног стабла без инсталирања пуног скупа runtime зависности. Ако будуће API документације захтевају увоз опционалних runtime провајдера током изградње, ажурирајте и `.github/workflows/docs.yml` и овај водич заједно.

## Docs quality bar

Пре спајања измена у документацији, покрените:

```bash
python -m mkdocs build --strict
git diff --check
```

Користите строге билдове тако да покварени линкови, неисправни навигациони уноси и проблеми при приказу API-ја избацују грешке у раној фази.