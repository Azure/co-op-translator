# Усунення неполадок

Use this page when a translation run succeeds unexpectedly, fails during configuration, or produces output that needs review.

## Start Here

1. Run a focused command first, such as `translate -l "ko" -md`.
2. Add `-d` for console debug logs.
3. Add `-s` to save debug logs under `<root-dir>/logs/`.
4. Run `co-op-review` after translation to check freshness, structure, and local links.

```bash
translate -l "ko" -md -d -s
co-op-review -l "ko"
```

## Configuration Errors

### No Language Model Provider

Помилка:

```text
No language model configuration found.
```

Виправлення:

- Налаштуйте Azure OpenAI або OpenAI.
- Перевірте, що змінні присутні в середовищі, де виконується команда.
- Для локального використання помістіть їх у `.env` в корені проєкту.

Див. [Налаштування](configuration.md).

### Image Translation Without Azure AI Vision

Помилка:

```text
Image translation requested but Azure AI Service is not configured.
```

Виправлення:

- Додайте `AZURE_AI_SERVICE_API_KEY`.
- Додайте `AZURE_AI_SERVICE_ENDPOINT`.
- Або запустіть команду лише для тексту, наприклад `translate -l "ko" -md`.

### Invalid Key or Endpoint

Симптоми можуть включати `401`, приховані помилки дозволів або помилки доступу до кінцевої точки.

Виправлення:

- Підтвердіть, що ключ належить до того самого ресурсу Azure, що й кінцева точка.
- Підтвердіть, що ресурс підтримує Vision при використанні `-img`.
- Переконайтеся, що назва розгортання Azure OpenAI та версія API відповідають вашому розгортанню.
- Запустіть з журналами налагодження: `translate -l "ko" -md -d -s`.

## No Files Were Translated

Поширені причини:

- Обрані прапори не відповідають вашим файлам.
- Перекладені файли вже присутні.
- Файли-джерела знаходяться в виключених каталогах.
- Команда запускається з неправильного кореня проєкту.

Перевірки:

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -nb --dry-run
translate -l "ko" -img --dry-run
```

Use `--root-dir` when the command is run outside the project root.

## Unexpected Link Behavior

Переписування посилань залежить від обраних типів вмісту:

- `-nb` включено: посилання на ноутбуки можуть вказувати на перекладені ноутбуки.
- `-nb` виключено: посилання на ноутбуки можуть залишатися спрямованими на вихідні ноутбуки.
- `-img` включено: посилання на зображення можуть вказувати на перекладені зображення.
- `-img` виключено: посилання на зображення можуть залишатися спрямованими на вихідні зображення.

Запустіть повний переклад вмісту, коли всі внутрішні посилання повинні надавати перевагу перекладеним результатам:

```bash
translate -l "ko" -md -nb -img
```

Запустіть перевірку посилань після перекладу:

```bash
co-op-review -l "ko"
```

## Markdown Rendering Issues

Якщо перекладений Markdown відображається неправильно:

- Переконайтеся, що frontmatter починається і закінчується `---`.
- Перевірте, що кількість обрамлень коду збігається між вихідними та перекладеними файлами.
- Запустіть `co-op-review`, щоб виявити поширені проблеми зі структурою.
- Повторно перекладіть конкретний файл, якщо вихід було пошкоджено.

```bash
co-op-review -l "ko" --format github
```

## GitHub Action Ran but No Pull Request Was Created

Якщо `peter-evans/create-pull-request` повідомляє, що гілка не випереджає базову, робочий процес не знайшов файлів для коміту.

Можливі причини:

- Переклад не дав змін.
- `.gitignore` виключає `translations/`, `translated_images/` або перекладені ноутбуки.
- `add-paths` не відповідає згенерованим вихідним директоріям.
- Крок перекладу завершився достроково.

Виправлення:

1. Підтвердіть, що згенеровані файли існують у `translations/` або `translated_images/`.
2. Підтвердіть, що `.gitignore` не ігнорує згенеровані вихідні файли.
3. Використовуйте відповідні `add-paths`:

   ```yaml
   with:
     add-paths: |
       translations/
       translated_images/
   ```

4. Тимчасово додайте прапори налагодження до команди translate:

   ```bash
   translate -l "ko" -md -d -s
   ```

5. Підтвердіть, що дозволи робочого процесу включають:

   ```yaml
   permissions:
     contents: write
     pull-requests: write
   ```

## Translation Quality

Машинні переклади можуть потребувати людського перегляду. Використовуйте `evaluate` тільки коли ви хочете експериментальну оцінку якості та робочі процеси виправлення з низькою довірою.

!!! warning "Experimental"
    `evaluate` can use rule-based and LLM-based checks, and its scoring model and metadata behavior may change. Keep it out of required CI gates unless your workflow is prepared for changes.

Для детермінованих перевірок CI використовуйте натомість `co-op-review`.