<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d95d7ec0097c5569ac16dd42840787a2",
  "translation_date": "2025-06-12T09:45:35+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "uk"
}
-->
# Contributing to Co-op Translator

Цей проєкт вітає внески та пропозиції. Більшість внесків вимагають, щоб ви погодилися з Contributor License Agreement (CLA), що підтверджує ваше право і фактичну згоду надати нам права на використання вашого внеску. Деталі можна знайти за адресою https://cla.opensource.microsoft.com.

Коли ви надсилаєте pull request, CLA-бот автоматично визначить, чи потрібно вам надати CLA, і відповідно позначить PR (наприклад, перевірка статусу, коментар). Просто дотримуйтесь інструкцій бота. Вам потрібно зробити це лише один раз для всіх репозиторіїв, які використовують наш CLA.

## Налаштування середовища розробки

Для налаштування середовища розробки цього проєкту ми рекомендуємо використовувати Poetry для керування залежностями. Ми використовуємо `pyproject.toml` для керування залежностями проєкту, тому для встановлення залежностей слід використовувати Poetry.

### Створення віртуального середовища

#### Використання pip

```bash
python -m venv .venv
```

#### Використання Poetry

```bash
poetry init
```

### Активація віртуального середовища

#### Для pip і Poetry

- Windows:

    ```bash
    .venv\Scripts\activate.bat
    ```

- Mac/Linux:

    ```bash
    source .venv/bin/activate
    ```

#### Використання Poetry

```bash
poetry shell
```

### Встановлення пакету та необхідних пакетів

#### Використання Poetry (з pyproject.toml)

```bash
poetry install
```

### Ручне тестування

Перед подачею PR важливо протестувати функціонал перекладу на реальній документації:

1. Створіть тестову директорію в кореневій папці:
    ```bash
    mkdir test_docs
    ```

2. Скопіюйте до тестової директорії деякі markdown-документи та зображення, які хочете перекласти. Наприклад:
    ```bash
    cp /path/to/your/docs/*.md test_docs/
    cp /path/to/your/images/*.png test_docs/
    ```

3. Встановіть пакет локально:
    ```bash
    pip install -e .
    ```

4. Запустіть Co-op Translator на ваших тестових документах:
    ```bash
    python -m co_op_translator --language-codes ko --root-dir test_docs
    ```

5. Перевірте перекладені файли в `test_docs/translations` and `test_docs/translated_images` to verify:
   - The translation quality
   - The metadata comments are correct
   - The original markdown structure is preserved
   - Links and images are working properly

This manual testing helps ensure that your changes work well in real-world scenarios.

### Environment variables

1. Create an `.env` file in the root directory by copying the provided `.env.template` файлі.
1. Заповніть змінні середовища згідно з інструкціями.

> [!TIP]
>
> ### Додаткові варіанти налаштування середовища розробки
>
> Окрім запуску проєкту локально, ви також можете використовувати GitHub Codespaces або VS Code Dev Containers для альтернативного налаштування середовища розробки.
>
> #### GitHub Codespaces
>
> Ви можете запускати ці приклади віртуально, використовуючи GitHub Codespaces, і додаткові налаштування не потрібні.
>
> Кнопка відкриє веб-версію VS Code у вашому браузері:
>
> 1. Відкрийте шаблон (це може зайняти кілька хвилин):
>
>     [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/azure/co-op-translator)
>
> #### Локальний запуск через VS Code Dev Containers
>
> ⚠️ Цей варіант працюватиме лише, якщо Docker Desktop має виділено щонайменше 16 ГБ оперативної пам’яті. Якщо у вас менше 16 ГБ, спробуйте [GitHub Codespaces](../..) або [налаштуйте локально](../..).
>
> Пов’язаний варіант — VS Code Dev Containers, який відкриє проєкт у вашому локальному VS Code з використанням [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers):
>
> 1. Запустіть Docker Desktop (встановіть, якщо ще не встановлено)
> 2. Відкрийте проєкт:
>
>    [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator)


### Стиль коду

Ми використовуємо [Black](https://github.com/psf/black) як форматувач коду Python, щоб підтримувати послідовний стиль коду в проєкті. Black — це безкомпромісний форматувач, який автоматично переформатовує Python-код відповідно до стилю Black.

#### Конфігурація

Конфігурація Black визначена в нашому `pyproject.toml`:

```toml
[tool.black]
line-length = 88
target-version = ['py310']
include = '\.pyi?$'
```

#### Встановлення Black

Ви можете встановити Black за допомогою Poetry (рекомендовано) або pip:

##### Використання Poetry

Black встановлюється автоматично під час налаштування середовища розробки:
```bash
poetry install
```

##### Використання pip

Якщо ви використовуєте pip, можна встановити Black напряму:
```bash
pip install black
```

#### Використання Black

##### З Poetry

1. Відформатуйте всі Python-файли в проєкті:
    ```bash
    poetry run black .
    ```

2. Відформатуйте конкретний файл або директорію:
    ```bash
    poetry run black path/to/file_or_directory
    ```

##### З pip

1. Відформатуйте всі Python-файли в проєкті:
    ```bash
    black .
    ```

2. Відформатуйте конкретний файл або директорію:
    ```bash
    black path/to/file_or_directory
    ```

> [!TIP]
> Рекомендуємо налаштувати ваш редактор так, щоб він автоматично форматував код за допомогою Black при збереженні. Більшість сучасних редакторів підтримують це через розширення або плагіни.

## Запуск Co-op Translator

Щоб запустити Co-op Translator за допомогою Poetry у вашому середовищі, виконайте наступні кроки:

1. Перейдіть у директорію, де хочете провести тестування перекладу, або створіть тимчасову папку для тестування.

2. Виконайте наступну команду. Прапорець `-l ko` with the language code you wish to translate into. The `-d` вказує на режим відлагодження.

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> [!NOTE]
> Переконайтеся, що ваше середовище Poetry активоване (poetry shell) перед запуском команди.

## Утримувачі проєкту

### Формат повідомлення коміту та стратегія злиття

Для забезпечення послідовності та зрозумілості історії комітів проєкту ми дотримуємося конкретного формату повідомлення коміту **для фінального повідомлення коміту** при використанні стратегії **Squash and Merge**.

Коли pull request (PR) зливається, окремі коміти об’єднуються в один. Остаточне повідомлення коміту має відповідати наведеному нижче формату для підтримки чистої та послідовної історії.

#### Формат повідомлення коміту (для squash and merge)

Ми використовуємо такий формат повідомлень комітів:

```bash
<type>: <description> (#<PR number>)
```

- **type**: Визначає категорію коміту. Використовуємо такі типи:
  - `Docs`: For documentation updates.
  - `Build`: For changes related to the build system or dependencies, including updates to configuration files, CI workflows, or the Dockerfile.
  - `Core`: For modifications to the project's core functionality or features, particularly those involving files in the `src/co_op_translator/core` directory.

- **description**: A concise summary of the change.
- **PR number**: The number of the pull request associated with the commit.

**Examples**:

- `Docs: Update installation instructions for clarity (#50)`
- `Core: Improve handling of image translation (#60)`

> [!NOTE]
> Currently, the **`Docs`**, **`Core`**, and **`Build`** prefixes are automatically added to PR titles based on the labels applied to the modified source code. As long as the correct label is applied, you typically don't need to manually update the PR title. You just need to verify that everything is correct and the prefix has been generated appropriately.

#### Merge strategy

We use **Squash and Merge** as our default strategy for pull requests. This strategy ensures that commit messages follow our format, even if individual commits don't.

**Reasons**:

- A clean, linear project history.
- Consistency in commit messages.
- Reduced noise from minor commits (e.g., "fix typo").

When merging, ensure the final commit message follows the commit message format described above.

**Example of Squash and Merge**
If a PR contains the following commits:

- `fix typo`
- `update README`
- `adjust formatting`

They should be squashed into:
`Docs: Improve documentation clarity and formatting (#65)`

**Відмова від відповідальності**:  
Цей документ було перекладено за допомогою сервісу автоматичного перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, зверніть увагу, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується звертатися до професійного перекладу, виконаного людиною. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.