# Ръководство за поддържащия

Тази страница обобщава как API, CLI и сайтът за документация са свързани помежду си.

## Граница на публичното API

Стабилният Python API се експортира от:

```python
co_op_translator.api
```

Публичният API е организиран в помощни модули за превод на съдържание, помощни модули за пренаписване на пътища, оркестрация на проекти и преглед:

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

`TranslationStateProvider` е границата за персистентност за хоствани интеграции.
Трябва да държи генерираните кандидати отделно от приетите базови версии, така че един
неслят превод да не може да стане източник на истината.

При добавяне на нови публични API-та, актуализирайте:

- `src/co_op_translator/api/__init__.py`
- `docs/api.md`
- релевантните тестове на API под `tests/co_op_translator/`, като например `test_api.py` или `test_review_api.py`

Избягвайте документиране на по-ниско ниво модули `core` като стабилен API, освен ако проектът не възнамерява да ги поддържа директно.

## Точки за вход на CLI

Пакетът дефинира следните Poetry скриптове:

```toml
[tool.poetry.scripts]
translate = "co_op_translator.__main__:main"
evaluate = "co_op_translator.__main__:main"
migrate-links = "co_op_translator.__main__:main"
co-op-review = "co_op_translator.__main__:main"
co-op-translator-mcp = "co_op_translator.mcp.server:main"
```

`src/co_op_translator/__main__.py` пренасочва според името на скрипта:

- `translate` извиква `co_op_translator.cli.translate.translate_command`
- `evaluate` извиква `co_op_translator.cli.evaluate.evaluate_command`
- `migrate-links` извиква `co_op_translator.cli.migrate_links.migrate_links_command`
- `co-op-review` извиква `co_op_translator.cli.review.review_command`

`co-op-translator-mcp` заобикаля `__main__.py` и извиква `co_op_translator.mcp.server:main` директно.

Когато добавяте или променяте опции на CLI, актуализирайте:

- съответната команда в `src/co_op_translator/cli/*.py`
- `docs/cli.md`
- Тестове, свързани с CLI, ако поведението се промени

## MCP сървър

MCP сървърът е реализиран в:

```python
co_op_translator.mcp.server
```

Сървърът умишлено обгръща публичния Python API, вместо да извиква по-ниско ниво модулите `core`. Запазете тази граница непокътната, така че MCP клиентите, Python извикващите и CLI да споделят едно и също поведение.

При добавяне или промяна на MCP инструменти, актуализирайте:

- `src/co_op_translator/mcp/server.py`
- `tests/co_op_translator/test_mcp_server.py`
- `docs/mcp.md`
- `docs/api.md` ако повърхността на публичния API се промени

Инструментите за превод на хранилището могат да бъдат извиквани като модел чрез MCP и могат да записват много файлове. Запазете `dry_run=True` като по подразбиране и изисквайте `confirm_write=True` преди превод на проект извън dry-run режим.

## Поток на превода

Основният поток за превод на проекта е:

1. Парсирайте CLI аргументите или параметрите на API.
2. Валидирайте конфигурацията на LLM с `LLMConfig`.
3. Валидирайте Azure AI Vision когато е избран превод на изображения.
4. Нормализирайте езиковите кодове.
5. Открийте наследени алиаси на папки за езици.
6. Оценете обема на превода.
7. Актуализирайте секциите за език/курс в README, когато е приложимо.
8. Делегирайте превода на проекта на `ProjectTranslator`.
9. `ProjectTranslator` делегира обработката на файлове на `TranslationManager`.

`TranslationManager` се състои от смесители (mixins), фокусирани върху типовете файлове:

- `ProjectMarkdownTranslationMixin` обработва четене на Markdown файлове, превод на съдържанието, пренаписване на пътища, метаданни, откази от отговорност и записване.
- `ProjectNotebookTranslationMixin` обработва четене на notebook файлове, превод на Markdown клетки, пренаписване на пътища, метаданни, откази от отговорност и записване.
- `ProjectImageTranslationMixin` обработва откриването на изображения, извличане/превод на текст, записване на рендирани изображения и метаданни.

APIs на по-ниско ниво за съдържание пропускат работния процес на проекта:

1. `translate_markdown_content` и `translate_notebook_content` превеждат само съдържание в паметта.
2. `translate_image_content` превежда текст в едно изображение и връща обект на рендирано изображение.
3. `rewrite_markdown_paths` и `rewrite_notebook_paths` са явни помощни средства за постобработка. Те не извършват превод и не извършват запис в рамките на проект.

## Поток на прегледа

Детерминираният поток за преглед е:

1. Парсирайте CLI аргументите или API параметрите.
2. Нормализирайте заявените езикови кодове.
3. Създайте един или повече цели за преглед от `root_dir`, `root_dirs`, или `groups`.
4. По желание ограничете изходните файлове с `--changed-from`.
5. Изпълнете детерминирани проверки за структура, свежест на превода, целостта на Markdown и локалните пътища към връзки/изображения.
6. Отпечатайте или текстов изход, или Markdown във формат GitHub.
7. Излезте с грешка когато бъдат намерени грешки при прегледа.

Потокът за преглед не изисква API ключове и остава наличен за локални проверки или CI по избор за потребителя. Това хранилище не изпълнява автоматично `co-op-review` при всяка pull заявка.

## Сайт за документация

Сайтът с документи е конфигуриран чрез:

```text
mkdocs.yml
requirements-docs.txt
docs/
```

Директорият `docs/` е каноничният източник на документация. Не добавяйте нови ръководства за крайни потребители извън тази директория, освен ако проектът умишлено не въвежда друга публикувана повърхност за документация.

Изграждане локално:

```bash
python -m pip install -r requirements-docs.txt
python -m mkdocs build --strict
```

Преглед локално:

```bash
python -m mkdocs serve
```

Генерираният сайт се записва в `site/`, който е игнориран от git.

## Работен поток за GitHub Pages

`.github/workflows/docs.yml` изгражда сайта при pull заявки и го разгръща при push към `main`.

Работният поток инсталира:

```bash
pip install -r requirements-docs.txt
```

Работният поток за документацията инсталира само инструменталния стек за документация. `mkdocs.yml` насочва `mkdocstrings` към `src/`, така че страниците за публичния API могат да бъдат рендирани от източника без инсталиране на целия набор от зависимости за runtime. Ако бъдещите API документи изискват импортиране на опционални runtime доставчици по време на изграждане, актуализирайте както `.github/workflows/docs.yml`, така и това ръководство заедно.

## Критерии за качество на документацията

Преди да слеете промените в документацията, изпълнете:

```bash
python -m mkdocs build --strict
git diff --check
```

Използвайте строги сборки, така че счупени връзки, невалидни навигационни записи и проблеми с рендирането на API да се провалят рано.