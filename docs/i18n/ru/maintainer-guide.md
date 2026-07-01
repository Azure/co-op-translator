# Руководство для мейнтейнера

На этой странице кратко описано, как API, CLI и сайт документации связаны между собой.

## Граница публичного API

Стабильный Python API экспортируется из:

```python
co_op_translator.api
```

Публичный API организован в помощники по переводу контента, помощники по переписыванию путей, оркестрацию проектов и обзор:

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

При добавлении новых публичных API обновите:

- `src/co_op_translator/api/__init__.py`
- `docs/api.md`
- соответствующие тесты API в `tests/co_op_translator/`, такие как `test_api.py` или `test_review_api.py`

Не документируйте низкоуровневые модули `core` как стабильный API, если проект не собирается поддерживать их напрямую.

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
- тесты, связанные с CLI, если поведение изменилось

## MCP-сервер

MCP-сервер реализован в:

```python
co_op_translator.mcp.server
```

Сервер сознательно оборачивает публичный Python API вместо вызовов низкоуровневых модулей `core`. Сохраняйте эту границу, чтобы клиенты MCP, вызовы из Python и CLI имели одинаковое поведение.

При добавлении или изменении инструментов MCP обновите:

- `src/co_op_translator/mcp/server.py`
- `tests/co_op_translator/test_mcp_server.py`
- `docs/mcp.md`
- `docs/api.md`, если поверхность публичного API изменяется

Инструменты перевода репозитория доступны для вызова модели через MCP и могут записывать множество файлов. Сохраняйте `dry_run=True` по умолчанию и требуйте `confirm_write=True` перед переводом проекта вне режима `dry_run`.

## Поток перевода

Общий поток перевода проекта:

1. Разбор аргументов CLI или параметров API.
2. Валидация конфигурации LLM с помощью `LLMConfig`.
3. Валидация Azure AI Vision при выборе перевода изображений.
4. Нормализация кодов языков.
5. Обнаружение устаревших псевдонимов папок с языками.
6. Оценка объёма перевода.
7. Обновление разделов README с информацией о языке/курсе при необходимости.
8. Делегирование перевода проекта `ProjectTranslator`.
9. `ProjectTranslator` делегирует обработку файлов `TranslationManager`.

`TranslationManager` собран из специализированных миксинов для типов файлов:

- `ProjectMarkdownTranslationMixin` обрабатывает чтение Markdown-файлов, перевод содержимого, переписывание путей, метаданные, дисклеймеры и запись.
- `ProjectNotebookTranslationMixin` обрабатывает чтение ноутбуков, перевод Markdown-ячееек, переписывание путей, метаданные, дисклеймеры и запись.
- `ProjectImageTranslationMixin` обрабатывает обнаружение изображений, извлечение/перевод текста, запись визуализированных изображений и метаданные.

Низкоуровневые API для работы с контентом пропускают проектный рабочий процесс:

1. `translate_markdown_content` и `translate_notebook_content` переводят только контент в памяти.
2. `translate_image_content` переводит текст на одном изображении и возвращает объект визуализированного изображения.
3. `rewrite_markdown_paths` и `rewrite_notebook_paths` — явные помощники постобработки. Они не выполняют перевод и не записывают проектные файлы.

## Процесс проверки

Детерминированный процесс проверки:

1. Разбор аргументов CLI или параметров API.
2. Нормализация запрошенных кодов языков.
3. Построение одной или нескольких целей проверки из `root_dir`, `root_dirs` или `groups`.
4. При необходимости ограничить исходные файлы с помощью `--changed-from`.
5. Выполнение детерминированных проверок структуры, актуальности перевода, целостности Markdown и локальных путей ссылок/изображений.
6. Вывод либо текстовой информации, либо Markdown в стиле GitHub.
7. Завершение с ошибкой при обнаружении ошибок проверки.

Процесс проверки не требует API-ключей и должен оставаться пригодным для CI pull request-ов. Рабочий процесс pull request-а записывает сводку проверки при каждом запуске и публикует комментарий в PR только когда `co-op-review` завершился с ошибкой.

## Сайт документации

Сайт документации настраивается с помощью:

```text
mkdocs.yml
requirements-docs.txt
docs/
```

Каталог `docs/` является каноническим источником документации. Не добавляйте новые руководства для конечных пользователей за пределами этого каталога, если проект намеренно не вводит другую публикуемую документационную площадку.

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

.github/workflows/docs.yml собирает сайт при pull request-ах и разворачивает его при пушах в ветку `main`.

В workflow устанавливается:

```bash
pip install -r requirements-docs.txt
```

Рабочий процесс документации устанавливает только набор инструментов для документации. Файл `mkdocs.yml` указывает `mkdocstrings` на `src/`, поэтому страницы публичного API могут быть отрисованы из исходного дерева без установки полного набора зависимостей времени выполнения. Если будущие документы API потребуют импорта опциональных провайдеров времени выполнения во время сборки, обновите одновременно `.github/workflows/docs.yml` и это руководство.

## Порог качества документации

Перед слиянием изменений в документации выполните:

```bash
python -m mkdocs build --strict
git diff --check
```

Используйте строгие сборки, чтобы сломанные ссылки, неверные элементы навигации и проблемы с рендерингом API обнаруживались на ранней стадии.