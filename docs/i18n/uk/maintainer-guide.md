# Керівництво для підтримувача

На цій сторінці підсумовано, як пов'язані між собою API, CLI та сайт документації.

## Межа публічного API

Стабільний Python API експортується з:

```python
co_op_translator.api
```

Публічний API організовано у вигляді допоміжних засобів для перекладу вмісту, переписування шляхів, оркестрації проєктів та перевірки:

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

При додаванні нових публічних API оновіть:

- `src/co_op_translator/api/__init__.py`
- `docs/api.md`
- relevant API tests under `tests/co_op_translator/`, such as `test_api.py` or `test_review_api.py`

Уникайте документувати нижчого рівня модулі `core` як стабільний API, якщо проєкт не планує підтримувати їх безпосередньо.

## CLI entry points

Пакет визначає такі скрипти Poetry:

```toml
[tool.poetry.scripts]
translate = "co_op_translator.__main__:main"
evaluate = "co_op_translator.__main__:main"
migrate-links = "co_op_translator.__main__:main"
co-op-review = "co_op_translator.__main__:main"
co-op-translator-mcp = "co_op_translator.mcp.server:main"
```

`src/co_op_translator/__main__.py` спрямовує виконання відповідно до імені скрипта:

- `translate` викликає `co_op_translator.cli.translate.translate_command`
- `evaluate` викликає `co_op_translator.cli.evaluate.evaluate_command`
- `migrate-links` викликає `co_op_translator.cli.migrate_links.migrate_links_command`
- `co-op-review` викликає `co_op_translator.cli.review.review_command`

`co-op-translator-mcp` обминає `__main__.py` і викликає `co_op_translator.mcp.server:main` безпосередньо.

При додаванні або зміні опцій CLI, оновіть:

- the relevant `src/co_op_translator/cli/*.py` command
- `docs/cli.md`
- CLI-related tests, if behavior changes

## MCP server

Сервер MCP реалізований у:

```python
co_op_translator.mcp.server
```

Сервер умисно обгортає публічний Python API замість виклику нижчестоящих модулів `core`. Зберігайте цю межу незмінною, щоб клієнти MCP, виклики з Python та CLI мали однакову поведінку.

При додаванні або зміні інструментів MCP оновіть:

- `src/co_op_translator/mcp/server.py`
- `tests/co_op_translator/test_mcp_server.py`
- `docs/mcp.md`
- `docs/api.md` if the public API surface changes

Інструменти перекладу репозиторію можуть бути викликані через MCP і можуть записувати багато файлів. За замовчуванням залишайте `dry_run=True` і вимагайте `confirm_write=True` перед перекладом проєкту не у режимі dry-run.

## Translation flow

Високорівневий потік перекладу проєкту:

1. Розібрати аргументи CLI або параметри API.
2. Перевірити конфігурацію LLM за допомогою `LLMConfig`.
3. Перевірити Azure AI Vision, якщо обрано переклад зображень.
4. Нормалізувати коди мов.
5. Виявити застарілі псевдоніми папок мов.
6. Оцінити обсяг перекладу.
7. Оновити секції README про мову/курс за потреби.
8. Делегувати переклад проєкту `ProjectTranslator`.
9. `ProjectTranslator` делегує обробку файлів `TranslationManager`.

`TranslationManager` складається зі спрямованих на конкретні типи файлів міксинів:

- `ProjectMarkdownTranslationMixin` обробляє читання файлів Markdown, переклад вмісту, переписування шляхів, метадані, застереження та запис.
- `ProjectNotebookTranslationMixin` обробляє читання файлів ноутбуків, переклад Markdown-клітинок, переписування шляхів, метадані, застереження та запис.
- `ProjectImageTranslationMixin` обробляє виявлення зображень, витяг/переклад тексту, запис відрендерених зображень та метадані.

Нижчестоячі API для вмісту обходять робочий процес проєкту:

1. `translate_markdown_content` та `translate_notebook_content` перекладають лише вміст в пам'яті.
2. `translate_image_content` перекладає текст на одному зображенні й повертає об'єкт з відрендереним зображенням.
3. `rewrite_markdown_paths` та `rewrite_notebook_paths` є явними допоміжними функціями постобробки. Вони не виконують перекладу і не записують файли проєкту.

## Review flow

Детермінований потік перевірки:

1. Розібрати аргументи CLI або параметри API.
2. Нормалізувати запитані коди мов.
3. Створити одну або кілька цілей перевірки з `root_dir`, `root_dirs` або `groups`.
4. За бажанням обмежити файли-джерела за допомогою `--changed-from`.
5. Запустити детерміновані перевірки структури, актуальності перекладу, цілісності Markdown та локальних шляхів посилань/зображень.
6. Вивести або текстовий результат, або Markdown у стилі GitHub.
7. Завершити з помилкою, якщо виявлені помилки перевірки.

Потік перевірки не потребує ключів API і має залишатися придатним для CI pull request-ів. Робочий процес pull request записує зведення перевірки при кожному запуску і робить коментар у PR лише коли `co-op-review` зазнає невдачі.

## Documentation site

Сайт документації налаштований за допомогою:

```text
mkdocs.yml
requirements-docs.txt
docs/
```

Каталог `docs/` є канонічним джерелом документації. Не додавайте нові довідники для кінцевих користувачів поза цим каталогом, якщо проєкт свідомо не вводить інше опубліковане джерело документації.

Збирати локально:

```bash
python -m pip install -r requirements-docs.txt
python -m mkdocs build --strict
```

Попередній перегляд локально:

```bash
python -m mkdocs serve
```

Згенерований сайт записується до `site/`, який ігнорується git.

## GitHub Pages workflow

`.github/workflows/docs.yml` будує сайт під час pull request-ів і розгортає його при пушах у `main`.

Робочий процес встановлює:

```bash
pip install -r requirements-docs.txt
```

Робочий процес для документації встановлює лише інструменти для документації. `mkdocs.yml` вказує `mkdocstrings` на `src/`, тому сторінки публічного API можуть бути згенеровані з дерева вихідного коду без встановлення повного набору залежностей виконання. Якщо майбутня документація API вимагатиме імпорту опціональних runtime провайдерів під час збірки, оновіть одночасно і `.github/workflows/docs.yml`, і цей посібник.

## Docs quality bar

Перед злиттям змін у документації запустіть:

```bash
python -m mkdocs build --strict
git diff --check
```

Використовуйте сувору збірку, щоб зламані посилання, недійсні елементи навігації та проблеми рендерингу API спричиняли помилку на ранньому етапі.