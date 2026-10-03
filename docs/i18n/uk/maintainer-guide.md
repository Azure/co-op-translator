# Посібник для підтримувача

Ця сторінка підсумовує, як API, CLI та сайт документації пов'язані між собою.

## Межа публічного API

Стабільний Python API експортується з:

```python
co_op_translator.api
```

Публічний API організовано у помічники для перекладу вмісту, переписування шляхів, оркестрації проєкту та рецензування:

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

`TranslationStateProvider` є межею персистенції для розміщених інтеграцій.
Він повинен зберігати згенеровані варіанти окремо від прийнятих базових версій, щоб
необ'єднаний переклад не став джерелом істини.

При додаванні нових публічних API оновіть:

- `src/co_op_translator/api/__init__.py`
- `docs/api.md`
- відповідні тести API в `tests/co_op_translator/`, такі як `test_api.py` або `test_review_api.py`

Уникайте документування нижчестоячих модулів `core` як стабільного API, якщо проєкт не планує підтримувати їх безпосередньо.

## Точки входу CLI

Пакет визначає ці скрипти Poetry:

```toml
[tool.poetry.scripts]
translate = "co_op_translator.__main__:main"
evaluate = "co_op_translator.__main__:main"
migrate-links = "co_op_translator.__main__:main"
co-op-review = "co_op_translator.__main__:main"
co-op-translator-mcp = "co_op_translator.mcp.server:main"
```

`src/co_op_translator/__main__.py` розподіляє виклик за назвою скрипта:

- `translate` викликає `co_op_translator.cli.translate.translate_command`
- `evaluate` викликає `co_op_translator.cli.evaluate.evaluate_command`
- `migrate-links` викликає `co_op_translator.cli.migrate_links.migrate_links_command`
- `co-op-review` викликає `co_op_translator.cli.review.review_command`

`co-op-translator-mcp` обходить `__main__.py` і безпосередньо викликає `co_op_translator.mcp.server:main`.

При додаванні або зміні опцій CLI оновіть:

- відповідну команду в `src/co_op_translator/cli/*.py`
- `docs/cli.md`
- тести, пов'язані з CLI, якщо поведінка змінюється

## MCP server

Сервер MCP реалізовано в:

```python
co_op_translator.mcp.server
```

Сервер навмисно обгортає публічний Python API замість виклику нижчестоячих модулів `core`. Зберігайте цю межу, щоб клієнти MCP, виклики з Python і CLI мали однакову поведінку.

При додаванні або зміні інструментів MCP оновіть:

- `src/co_op_translator/mcp/server.py`
- `tests/co_op_translator/test_mcp_server.py`
- `docs/mcp.md`
- `docs/api.md` якщо поверхня публічного API змінюється

Інструменти перекладу репозиторію можна викликати через MCP і вони можуть записувати багато файлів. Залишайте `dry_run=True` за замовчуванням і вимагайте `confirm_write=True` перед перекладом проєкту не в режимі dry_run.

## Потік перекладу

Високорівневий потік перекладу проєкту:

1. Розбір аргументів CLI або параметрів API.
2. Перевірити конфігурацію LLM за допомогою `LLMConfig`.
3. Перевірити Azure AI Vision, коли обрано переклад зображень.
4. Нормалізувати коди мов.
5. Виявити застарілі псевдоніми папок мов.
6. Оцінити обсяг перекладу.
7. Оновити розділи мови/курсу в README, коли це застосовно.
8. Делегувати переклад проєкту `ProjectTranslator`.
9. `ProjectTranslator` делегує обробку файлів `TranslationManager`.

`TranslationManager` складається зі спеціалізованих mixin-ів для типів файлів:

- `ProjectMarkdownTranslationMixin` обробляє читання Markdown-файлів, переклад вмісту, переписування шляхів, метадані, застереження та запис.
- `ProjectNotebookTranslationMixin` обробляє читання ноутбуків, переклад Markdown-ячейок, переписування шляхів, метадані, застереження та запис.
- `ProjectImageTranslationMixin` обробляє виявлення зображень, вилучення/переклад тексту, запис рендерених зображень та метадані.

Нижчестоячі API вмісту пропускають робочий процес проєкту:

1. `translate_markdown_content` та `translate_notebook_content` перекладають лише вміст у пам'яті.
2. `translate_image_content` перекладає текст в одному зображенні і повертає об'єкт рендереного зображення.
3. `rewrite_markdown_paths` та `rewrite_notebook_paths` — явні допоміжні засоби постобробки. Вони не виконують переклад і не записують файли проєкту.

## Потік рецензування

Детермінований потік рецензування:

1. Розбір аргументів CLI або параметрів API.
2. Нормалізувати запитані коди мов.
3. Побудувати одну або кілька цілей рецензування з `root_dir`, `root_dirs` або `groups`.
4. За бажанням обмежити вихідні файли за допомогою `--changed-from`.
5. Запустити детерміновані перевірки структури, свіжості перекладів, цілісності Markdown та локальних шляхів для посилань/зображень.
6. Вивести або текстовий результат, або Markdown у стилі GitHub.
7. Завершити з помилкою, якщо знайдено помилки рецензування.

Потік рецензування не вимагає API-ключів і залишається доступним для локальних перевірок або опціонального CI у споживача. Цей репозиторій не запускає `co-op-review` автоматично для кожного pull request.

## Сайт документації

Сайт документації налаштовано за допомогою:

```text
mkdocs.yml
requirements-docs.txt
docs/
```

Каталог `docs/` є канонічним джерелом документації. Не додавайте нові посібники для користувачів поза цим каталогом, якщо проєкт навмисно не вводить іншу публічну документаційну поверхню.

Збирайте локально:

```bash
python -m pip install -r requirements-docs.txt
python -m mkdocs build --strict
```

Preview локально:

```bash
python -m mkdocs serve
```

Згенерований сайт записується до `site/`, який ігнорується git.

## Робочий процес GitHub Pages

`.github/workflows/docs.yml` збирає сайт для pull request-ів і розгортає його при пушах у `main`.

Робочий процес встановлює:

```bash
pip install -r requirements-docs.txt
```

Робочий процес документації встановлює лише інструментарій документації. `mkdocs.yml` вказує `mkdocstrings` на `src/`, щоб сторінки публічного API могли бути згенеровані з дерева джерел без встановлення повного набору залежностей часу виконання. Якщо майбутня документація API вимагатиме імпорту опційних провайдерів часу виконання під час збірки, оновіть одночасно `.github/workflows/docs.yml` і цей посібник.

## Рівень якості документації

Перед злиттям змін у документації виконайте:

```bash
python -m mkdocs build --strict
git diff --check
```

Використовуйте суворі збірки, щоб зламані посилання, недійсні елементи навігації та проблеми рендерингу API викликали помилки на ранньому етапі.