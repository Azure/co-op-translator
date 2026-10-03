# Водич за одржаваче

Ова страница резимира како су API, CLI и сајт документације повезани.

## Јавна граница API-ја

Стабилан Python API се експортује из:

```python
co_op_translator.api
```

Јавни API је организован у помоћне функције за превођење садржаја, помоћне функције за преписивање путева, оркестрацију пројеката и преглед:

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

`TranslationStateProvider` је граница перзистенције за хостиране интеграције.
Она мора да одржава генерисане предлоге одвојеним од прихваћених базних верзија тако да један
неутврђен превод не постане извор истине.

Када додајете нове јавне API-је, ажурирајте:

- `src/co_op_translator/api/__init__.py`
- `docs/api.md`
- релевантне API тестове у оквиру `tests/co_op_translator/`, као што су `test_api.py` или `test_review_api.py`

Избегавајте документацију нижеразинских `core` модула као стабилног API-ја осим ако пројекат не намерава да их директно подржава.

## CLI улазне тачке

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

Када додајете или мењате CLI опције, ажурирајте:

- релевантну команду у `src/co_op_translator/cli/*.py`
- `docs/cli.md`
- тестове везане за CLI, ако се понашање промени

## MCP сервер

MCP сервер је имплементиран у:

```python
co_op_translator.mcp.server
```

Сервер намерно омотава јавни Python API уместо да позива нижеразинске `core` модуле. Оставите ову границу нетакнутом како би MCP клијенти, Python позиваоци и CLI делили исто понашање.

Када додајете или мењате MCP алате, ажурирајте:

- `src/co_op_translator/mcp/server.py`
- `tests/co_op_translator/test_mcp_server.py`
- `docs/mcp.md`
- `docs/api.md` ако се јавна површина API-ја промени

Алатке за превођење у репозиторијуму могу се позивати преко модела преко MCP и могу записати много фајлова. Држите `dry_run=True` као подразумевано и захтевајте `confirm_write=True` пре него што се изврши превођење пројекта које није у режиму dry_run.

## Ток превођења

Општи ток превођења пројекта је:

1. Парсирајте CLI аргументе или API параметре.
2. Верификујте конфигурацију LLM-а помоћу `LLMConfig`.
3. Верификујте Azure AI Vision када је изабрано превођење слика.
4. Нормализујте кодове језика.
5. Откријте застареле алијасе фолдера за језике.
6. Процените обим превођења.
7. Ажурирајте секције језика/курса у README-у када је применљиво.
8. Делегирајте превођење пројекта на `ProjectTranslator`.
9. `ProjectTranslator` предаје обраду фајлова `TranslationManager`.

`TranslationManager` је састављен од фокусираних mixin-ова по типу фајла:

- `ProjectMarkdownTranslationMixin` обрађује читање Markdown фајлова, превођење садржаја, преписивање путева, метаподатке, одрицања одговорности и уписе.
- `ProjectNotebookTranslationMixin` обрађује читање notebook фајлова, превођење Markdown ћелија, преписивање путева, метаподатке, одрицања одговорности и уписе.
- `ProjectImageTranslationMixin` обрађује откривање слика, екстракцију/превођење текста, уписе рендерованих слика и метаподатке.

Нижеразински API-ји за садржај прескачу пројектни ток рада:

1. `translate_markdown_content` и `translate_notebook_content` преводе само садржај у меморији.
2. `translate_image_content` преводи текст у једној слици и враћа објекат рендероване слике.
3. `rewrite_markdown_paths` и `rewrite_notebook_paths` су експлицитне помоћне функције за пост-процесирање. Не врше превођење нити уписе у пројекат.

## Ток прегледа

Детерминистички ток прегледа је:

1. Парсирајте CLI аргументе или API параметре.
2. Нормализујте тражене кодове језика.
3. Направите један или више циљева прегледа из `root_dir`, `root_dirs` или `groups`.
4. Опционално ограничите изворне фајлове помоћу `--changed-from`.
5. Покрените детерминистичке провере структуре, свежине превода, интегритета Markdown-а и локалних путања за линкове/слике.
6. Испишите или текстуални излаз или GitHub-flavored Markdown.
7. Изађите са грешком када се пронађу грешке у прегледу.

Ток прегледа не захтева API кључеве и остаје доступан за локалне провере или опционални потрошачки CI. Овај репозиторијум не покреће `co-op-review` аутоматски на сваком pull request-у.

## Сајт документације

Сајт документације се конфигурише помоћу:

```text
mkdocs.yml
requirements-docs.txt
docs/
```

Директоријум `docs/` је канонски извор документације. Не додајте нове водиче за крајње кориснике ван овог директоријума осим ако пројекат намерно не уводи другу објављену површину документације.

Изградите локално:

```bash
python -m pip install -r requirements-docs.txt
python -m mkdocs build --strict
```

Прегледајте локално:

```bash
python -m mkdocs serve
```

Генерисани сајт се записује у `site/`, који git игнорише.

## GitHub Pages радни ток

`.github/workflows/docs.yml` гради сајт на pull request-овима и деплојује га при push-евима на `main`.

Радни ток инсталира:

```bash
pip install -r requirements-docs.txt
```

Workflow за документацију инсталира само алатку за документацију. `mkdocs.yml` усмерава `mkdocstrings` на `src/` тако да јавне странице API-ја могу бити рендероване из стабла извора без инсталирања целог скупа runtime зависности. Ако будуће API документације захтевају увоз опционих runtime провајдера током израде, ажурирајте и `.github/workflows/docs.yml` и овај водич заједно.

## Ниво квалитета документације

Пре спајања измена у документацији, покрените:

```bash
python -m mkdocs build --strict
git diff --check
```

Користите строге билдове тако да покварени линкови, неважећи уноси у навигацији и проблеми са рендеровањем API-ја буду откривени рано.