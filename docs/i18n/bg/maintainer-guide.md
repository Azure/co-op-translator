# Ръководство за поддържащите

Тази страница обобщава как са свързани API, CLI и сайтът с документация.

## Граница на публичното API

Стабилният Python API е експортиран от:

```python
co_op_translator.api
```

Публичното API е организирано в помощни функции за превод на съдържание, помощни функции за пренаписване на пътища, оркестрация на проекти и преглед:

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

Когато добавяте нови публични API, обновете:

- `src/co_op_translator/api/__init__.py`
- `docs/api.md`
- релевантните API тестове под `tests/co_op_translator/`, като например `test_api.py` или `test_review_api.py`

Избягвайте документиране на по-ниско ниво `core` модули като стабилно API, освен ако проектът не възнамерява да ги поддържа директно.

## CLI входни точки

Пакетът дефинира тези Poetry скриптове:

```toml
[tool.poetry.scripts]
translate = "co_op_translator.__main__:main"
evaluate = "co_op_translator.__main__:main"
migrate-links = "co_op_translator.__main__:main"
co-op-review = "co_op_translator.__main__:main"
co-op-translator-mcp = "co_op_translator.mcp.server:main"
```

`src/co_op_translator/__main__.py` разпределя съобразно името на скрипта:

- `translate` извиква `co_op_translator.cli.translate.translate_command`
- `evaluate` извиква `co_op_translator.cli.evaluate.evaluate_command`
- `migrate-links` извиква `co_op_translator.cli.migrate_links.migrate_links_command`
- `co-op-review` извиква `co_op_translator.cli.review.review_command`

`co-op-translator-mcp` заобикаля `__main__.py` и извиква `co_op_translator.mcp.server:main` директно.

Когато добавяте или променяте CLI опции, обновете:

- съответната команда в `src/co_op_translator/cli/*.py`
- `docs/cli.md`
- тестовете, свързани с CLI, ако поведението се промени

## MCP сървър

MCP сървърът е имплементиран в:

```python
co_op_translator.mcp.server
```

Сървърът умишлено обвива публичното Python API, вместо да извиква по-ниско ниво `core` модули. Поддържайте тази граница непокътната, така че MCP клиентите, Python извикващите и CLI да споделят едно и също поведение.

Когато добавяте или променяте MCP инструменти, обновете:

- `src/co_op_translator/mcp/server.py`
- `tests/co_op_translator/test_mcp_server.py`
- `docs/mcp.md`
- `docs/api.md` ако повърхността на публичния API се промени

Инструментите за превод на хранилище са извикваеми от модел чрез MCP и могат да пишат много файлове. Дръжте `dry_run=True` като подразбиране и изисквайте `confirm_write=True` преди превод на проект, който не е в dry-run режим.

## Поток на превода

Високо ниво потокът за превод на проекта е:

1. Обработване на CLI аргументи или параметри на API.
2. Проверка на конфигурацията на LLM чрез `LLMConfig`.
3. Проверка на Azure AI Vision, когато е избран превод на изображения.
4. Нормализиране на кодовете на езиците.
5. Откриване на наследени псевдоними на папки за езици.
6. Оценка на обема на превода.
7. Актуализиране на секциите за език/курс в README, когато е приложимо.
8. Делегиране на превода на проекта към `ProjectTranslator`.
9. `ProjectTranslator` делегира обработката на файловете на `TranslationManager`.

`TranslationManager` се състои от миксини, фокусирани върху типове файлове:

- `ProjectMarkdownTranslationMixin` обработва четене на Markdown файлове, превод на съдържание, пренаписване на пътища, метаданни, откази от отговорност и записване.
- `ProjectNotebookTranslationMixin` обработва четене на notebook файлове, превод на Markdown клетки, пренаписване на пътища, метаданни, откази от отговорност и записване.
- `ProjectImageTranslationMixin` обработва откриване на изображения, извличане/превод на текст, записване на рендерирани изображения и метаданни.

По-ниско нивото content API пропускат работния процес на проекта:

1. `translate_markdown_content` и `translate_notebook_content` превеждат само съдържание в паметта.
2. `translate_image_content` превежда текста в едно изображение и връща рендериран обект изображение.
3. `rewrite_markdown_paths` и `rewrite_notebook_paths` са експлицитни помощници за пост-обработка. Те не извършват превод и не правят записи в проекта.

## Поток на прегледа

Детерминираният поток за преглед е:

1. Обработване на CLI аргументи или параметри на API.
2. Нормализиране на заявените езикови кодове.
3. Създаване на една или повече цели за преглед от `root_dir`, `root_dirs` или `groups`.
4. По избор ограничете изходните файлове с `--changed-from`.
5. Извършване на детерминирани проверки за структура, свежест на превода, цялост на Markdown и локални пътища към връзки/изображения.
6. Извеждане или като текст, или като Markdown във формат GitHub.
7. Изход с грешка, когато са открити грешки при прегледа.

Потокът за преглед не изисква API ключове и трябва да остане подходящ за CI при pull request. Работният процес за pull request записва резюме на проверките при всяко изпълнение и публикува коментар в PR само когато `co-op-review` се провали.

## Сайт за документация

Сайтът с документация е конфигуриран от:

```text
mkdocs.yml
requirements-docs.txt
docs/
```

Директорията `docs/` е каноничният източник на документация. Не добавяйте нови ръководства за крайни потребители извън тази директория, освен ако проектът умишлено не въвежда друга публикувана повърхност за документация.

Изграждане локално:

```bash
python -m pip install -r requirements-docs.txt
python -m mkdocs build --strict
```

Преглед локално:

```bash
python -m mkdocs serve
```

Генерираният сайт се записва в `site/`, която е игнорирана от git.

## Работен процес за GitHub Pages

`.github/workflows/docs.yml` изгражда сайта при pull request-и и го публикува при push към `main`.

Работният процес инсталира:

```bash
pip install -r requirements-docs.txt
```

Работният процес за документация инсталира само инструментариума за документация. `mkdocs.yml` насочва `mkdocstrings` към `src/`, така че страниците за публичното API да могат да се генерират от изходното дърво без инсталиране на пълния набор от runtime зависимости. Ако бъдещите API документации изискват импортиране на опционални runtime доставчици по време на изграждането, обновете едновременно `.github/workflows/docs.yml` и това ръководство.

## Стандарт за качество на документацията

Преди сливане на промените в документацията, изпълнете:

```bash
python -m mkdocs build --strict
git diff --check
```

Използвайте строги изграждания, така че счупените връзки, невалидните навигационни елементи и проблемите с рендирането на API да се откриват рано.