<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d95d7ec0097c5569ac16dd42840787a2",
  "translation_date": "2025-06-12T09:25:07+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "ru"
}
-->
# Вклад в Co-op Translator

Этот проект приветствует вклад и предложения. Большинство вкладов требуют вашего согласия с Contributor License Agreement (CLA), в котором вы подтверждаете, что имеете право и действительно предоставляете нам права на использование вашего вклада. Для подробностей посетите https://cla.opensource.microsoft.com.

При отправке pull request, бот CLA автоматически определит, нужно ли вам предоставить CLA, и отметит PR соответствующим образом (например, проверкой статуса или комментарием). Просто следуйте инструкциям бота. Это нужно сделать только один раз для всех репозиториев, использующих наш CLA.

## Настройка среды разработки

Для настройки среды разработки этого проекта мы рекомендуем использовать Poetry для управления зависимостями. Мы используем `pyproject.toml` для управления зависимостями проекта, поэтому для установки зависимостей следует использовать Poetry.

### Создание виртуального окружения

#### С помощью pip

```bash
python -m venv .venv
```

#### С помощью Poetry

```bash
poetry init
```

### Активация виртуального окружения

#### Для pip и Poetry

- Windows:

    ```bash
    .venv\Scripts\activate.bat
    ```

- Mac/Linux:

    ```bash
    source .venv/bin/activate
    ```

#### С помощью Poetry

```bash
poetry shell
```

### Установка пакета и необходимых зависимостей

#### С помощью Poetry (из pyproject.toml)

```bash
poetry install
```

### Ручное тестирование

Перед отправкой PR важно протестировать функциональность перевода на реальной документации:

1. Создайте папку test в корневом каталоге:
    ```bash
    mkdir test_docs
    ```

2. Скопируйте в папку test markdown-документацию и изображения, которые хотите перевести. Например:
    ```bash
    cp /path/to/your/docs/*.md test_docs/
    cp /path/to/your/images/*.png test_docs/
    ```

3. Установите пакет локально:
    ```bash
    pip install -e .
    ```

4. Запустите Co-op Translator для ваших тестовых документов:
    ```bash
    python -m co_op_translator --language-codes ko --root-dir test_docs
    ```

5. Проверьте переведённые файлы в `test_docs/translations` and `test_docs/translated_images` to verify:
   - The translation quality
   - The metadata comments are correct
   - The original markdown structure is preserved
   - Links and images are working properly

This manual testing helps ensure that your changes work well in real-world scenarios.

### Environment variables

1. Create an `.env` file in the root directory by copying the provided `.env.template`.
1. Заполните переменные окружения согласно инструкциям.

> [!TIP]
>
> ### Дополнительные варианты настройки среды разработки
>
> Помимо локального запуска проекта, вы можете использовать GitHub Codespaces или VS Code Dev Containers для альтернативной настройки среды разработки.
>
> #### GitHub Codespaces
>
> Вы можете запускать эти примеры виртуально с помощью GitHub Codespaces без дополнительной настройки.
>
> Кнопка откроет веб-версию VS Code в вашем браузере:
>
> 1. Откройте шаблон (это может занять несколько минут):
>
>     [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/azure/co-op-translator)
>
> #### Локальный запуск с использованием VS Code Dev Containers
>
> ⚠️ Этот вариант работает только если в Docker Desktop выделено минимум 16 ГБ оперативной памяти. Если у вас меньше 16 ГБ, попробуйте вариант с [GitHub Codespaces](../..) или [настройте локально](../..).
>
> Связанный вариант — VS Code Dev Containers, который откроет проект в вашем локальном VS Code с помощью [расширения Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers):
>
> 1. Запустите Docker Desktop (установите, если ещё не установлен)
> 2. Откройте проект:
>
>    [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator)


### Стиль кода

Мы используем [Black](https://github.com/psf/black) в качестве форматтера кода Python для поддержания единообразного стиля кода по всему проекту. Black — это строгий форматтер, который автоматически форматирует Python-код в соответствии с принятым стилем Black.

#### Конфигурация

Конфигурация Black указана в нашем `pyproject.toml`:

```toml
[tool.black]
line-length = 88
target-version = ['py310']
include = '\.pyi?$'
```

#### Установка Black

Вы можете установить Black с помощью Poetry (рекомендуется) или pip:

##### С помощью Poetry

Black устанавливается автоматически при настройке среды разработки:
```bash
poetry install
```

##### С помощью pip

Если вы используете pip, можно установить Black напрямую:
```bash
pip install black
```

#### Использование Black

##### С Poetry

1. Отформатировать все Python-файлы в проекте:
    ```bash
    poetry run black .
    ```

2. Отформатировать конкретный файл или папку:
    ```bash
    poetry run black path/to/file_or_directory
    ```

##### С pip

1. Отформатировать все Python-файлы в проекте:
    ```bash
    black .
    ```

2. Отформатировать конкретный файл или папку:
    ```bash
    black path/to/file_or_directory
    ```

> [!TIP]
> Рекомендуем настроить ваш редактор на автоматическое форматирование кода с помощью Black при сохранении. Большинство современных редакторов поддерживают это через расширения или плагины.

## Запуск Co-op Translator

Чтобы запустить Co-op Translator с помощью Poetry в вашей среде, выполните следующие шаги:

1. Перейдите в папку, где хотите провести тесты перевода, или создайте временную папку для тестирования.

2. Выполните следующую команду. Флаг `-l ko` with the language code you wish to translate into. The `-d` означает режим отладки.

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> [!NOTE]
> Убедитесь, что среда Poetry активирована (poetry shell) перед запуском команды.

## Поддерживающие проект

### Формат сообщений коммитов и стратегия слияния

Для обеспечения последовательности и ясности истории коммитов в нашем проекте мы используем определённый формат сообщений коммитов **для итогового сообщения коммита** при использовании стратегии **Squash and Merge**.

При слиянии pull request (PR) все отдельные коммиты объединяются в один. Итоговое сообщение коммита должно иметь следующий формат для поддержания чистой и понятной истории.

#### Формат сообщения коммита (для squash and merge)

Мы используем следующий формат сообщений коммитов:

```bash
<type>: <description> (#<PR number>)
```

- **type**: указывает категорию коммита. Мы используем следующие типы:
  - `Docs`: For documentation updates.
  - `Build`: For changes related to the build system or dependencies, including updates to configuration files, CI workflows, or the Dockerfile.
  - `Core`: For modifications to the project's core functionality or features, particularly those involving files in the `src/co_op_translator/core` directory.

- **description**: A concise summary of the change.
- **PR number**: The number of the pull request associated with the commit.

**Examples**:

- `Docs: Обновление инструкции по установке для ясности (#50)`
- `Core: Улучшение обработки перевода изображений (#60)`

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

- `исправление опечатки`
- `обновление README`
- `корректировка форматирования`

They should be squashed into:
`Docs: Улучшение ясности и форматирования документации (#65)`

**Отказ от ответственности**:  
Этот документ был переведен с использованием сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия обеспечить точность, имейте в виду, что автоматический перевод может содержать ошибки или неточности. Оригинальный документ на его исходном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется обращаться к профессиональному переводу, выполненному человеком. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования данного перевода.