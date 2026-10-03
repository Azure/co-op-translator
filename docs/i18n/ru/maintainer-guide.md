# Руководство для мейнтейнера

На этой странице кратко изложено, как связаны API, CLI и сайт документации.

## Граница публичного API

Стабильный Python API экспортируется из:

```python
co_op_translator.api
```

Публичный API организован в виде помощников для перевода содержимого, помощников для переписывания путей, оркестровки проектов и обзора:

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

`TranslationStateProvider` является границей персистентности для размещённых интеграций.
Он должен держать сгенерированные кандидаты отдельно от принятых базовых версий, чтобы
несмёрженный перевод не мог стать источником истины.

При добавлении новых публичных API обновите:

- `src/co_op_translator/api/__init__.py`
- `docs/api.md`
- соответствующие тесты API в каталоге `tests/co_op_translator/`, например `test_api.py` или `test_review_api.py`

Избегайте документирования низкоуровневых модулей `core` как стабильного API, если проект не намерен поддерживать их напрямую.

## Точки входа CLI

Пакет определяет следующие скрипты Poetry:

```toml
[tool.poetry.scripts]
translate = "co_op_translator.__main__:main"
evaluate = "co_op_translator.__main__:main"
migrate-links = "co_op_translator.__main__:main"
co-op-review = "co_op_translator.__main__:main"
co-op-translator-mcp = "co_op_translator.mcp.server:main"
```

`src/co_op_translator/__main__.py` перенаправляет по имени скрипта:

- `translate` вызывает `co_op_translator.cli.translate.translate_command`
- `evaluate` вызывает `co_op_translator.cli.evaluate.evaluate_command`
- `migrate-links` вызывает `co_op_translator.cli.migrate_links.migrate_links_command`
- `co-op-review` вызывает `co_op_translator.cli.review.review_command`

`co-op-translator-mcp` обходит `__main__.py` и напрямую вызывает `co_op_translator.mcp.server:main`.

При добавлении или изменении опций CLI обновите:

- соответствующую команду в `src/co_op_translator/cli/*.py`
- `docs/cli.md`
- тесты, связанные с CLI, если поведение меняется

## Сервер MCP

Сервер MCP реализован в:

```python
co_op_translator.mcp.server
```

Сервер сознательно оборачивает публичный Python API, а не вызывает низкоуровневые модули `core`. Сохраните эту границу, чтобы клиенты MCP, вызовы из Python и CLI имели одинаковое поведение.

При добавлении или изменении инструментов MCP обновите:

- `src/co_op_translator/mcp/server.py`
- `tests/co_op_translator/test_mcp_server.py`
- `docs/mcp.md`
- `docs/api.md`, если поверхность публичного API изменится

Инструменты перевода репозитория доступны для вызова через MCP и могут записывать множество файлов. Сохраняйте `dry_run=True` по умолчанию и требуйте `confirm_write=True` перед выполнением перевода проекта не в режиме dry-run.

## Поток перевода

Общий поток перевода проекта выглядит так:

1. Разобрать аргументы CLI или параметры API.
2. Проверить конфигурацию LLM с помощью `LLMConfig`.
3. Проверить Azure AI Vision при выборе перевода изображений.
4. Нормализовать коды языков.
5. Обнаружить устаревшие псевдонимы папок языков.
6. Оценить объём перевода.
7. Обновить разделы README, связанные с языком/курсом, если это применимо.
8. Делегировать перевод проекта `ProjectTranslator`.
9. `ProjectTranslator` делегирует обработку файлов `TranslationManager`.

`TranslationManager` состоит из специализированных миксинов для типов файлов:

- `ProjectMarkdownTranslationMixin` обрабатывает чтение Markdown-файлов, перевод содержимого, переписывание путей, метаданные, дисклеймеры и запись.
- `ProjectNotebookTranslationMixin` обрабатывает чтение файлов notebook, перевод Markdown-ячееек, переписывание путей, метаданные, дисклеймеры и запись.
- `ProjectImageTranslationMixin` отвечает за обнаружение изображений, извлечение/перевод текста, запись сгенерированных изображений и метаданные.

Низкоуровневые API содержимого пропускают рабочий процесс проекта:

1. `translate_markdown_content` и `translate_notebook_content` переводят только содержимое в памяти.
2. `translate_image_content` переводит текст в одном изображении и возвращает объект с отрендеренным изображением.
3. `rewrite_markdown_paths` и `rewrite_notebook_paths` — это явные вспомогательные функции постобработки. Они не выполняют перевод и не записывают файлы проекта.

## Поток обзора

Детерминированный поток обзора выглядит так:

1. Разобрать аргументы CLI или параметры API.
2. Нормализовать запрошенные коды языков.
3. Построить одну или несколько целей обзора из `root_dir`, `root_dirs` или `groups`.
4. По желанию ограничить исходные файлы с помощью `--changed-from`.
5. Запустить детерминированные проверки структуры, актуальности перевода, целостности Markdown и локальных путей ссылок/изображений.
6. Вывести либо текстовый вывод, либо Markdown в стиле GitHub.
7. Завершиться с ошибкой, если обнаружены ошибки обзора.

Поток обзора не требует ключей API и остаётся доступным для локальных проверок или включаемого CI у потребителя. В этом репозитории `co-op-review` не запускается автоматически для каждого pull request.

## Сайт документации

Сайт документации настраивается с помощью:

```text
mkdocs.yml
requirements-docs.txt
docs/
```

Каталог `docs/` является каноническим источником документации. Не добавляйте новые руководства для конечных пользователей за пределами этого каталога, если проект намеренно не вводит другую публикуемую поверхность документации.

Сборка локально:

```bash
python -m pip install -r requirements-docs.txt
python -m mkdocs build --strict
```

Предпросмотр локально:

```bash
python -m mkdocs serve
```

Сгенерированный сайт записывается в `site/`, который игнорируется git.

## Рабочий процесс GitHub Pages

`.github/workflows/docs.yml` собирает сайт при pull request и развёртывает его при пушах в `main`.

Рабочий процесс устанавливает:

```bash
pip install -r requirements-docs.txt
```

Workflow документации устанавливает только набор инструментов документации. `mkdocs.yml` указывает `mkdocstrings` на `src/`, чтобы страницы публичного API могли рендериться из исходного дерева без установки полного набора зависимостей времени выполнения. Если будущая документация API потребует импортировать опциональные runtime-провайдеры во время сборки, обновите одновременно и `.github/workflows/docs.yml`, и это руководство.

## Порог качества документации

Перед объединением изменений в документации запустите:

```bash
python -m mkdocs build --strict
git diff --check
```

Используйте строгую сборку, чтобы битые ссылки, неверные элементы навигации и проблемы с рендерингом API приводили к ошибке на раннем этапе.