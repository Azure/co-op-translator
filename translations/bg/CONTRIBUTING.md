<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d95d7ec0097c5569ac16dd42840787a2",
  "translation_date": "2025-06-12T09:43:12+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "bg"
}
-->
# Принос към Co-op Translator

Този проект приема приноси и предложения. Повечето приноси изискват да се съгласите с
Contributor License Agreement (CLA), който декларира, че имате правото и действително предоставяте
правата ни да използваме вашия принос. За подробности посетете https://cla.opensource.microsoft.com.

Когато подадете pull request, CLA бот автоматично ще определи дали трябва да предоставите
CLA и ще маркира PR съответно (напр. статус проверка, коментар). Просто следвайте инструкциите,
предоставени от бота. Това трябва да се направи само веднъж за всички репозитории, използващи нашия CLA.

## Настройка на среда за разработка

За да настроите средата за разработка на този проект, препоръчваме да използвате Poetry за управление на зависимости. Използваме `pyproject.toml` за управление на зависимостите на проекта и затова за инсталиране на зависимости трябва да използвате Poetry.

### Създаване на виртуална среда

#### Използване на pip

```bash
python -m venv .venv
```

#### Използване на Poetry

```bash
poetry init
```

### Активиране на виртуалната среда

#### За pip и Poetry

- Windows:

    ```bash
    .venv\Scripts\activate.bat
    ```

- Mac/Linux:

    ```bash
    source .venv/bin/activate
    ```

#### Използване на Poetry

```bash
poetry shell
```

### Инсталиране на пакета и необходимите пакети

#### Използване на Poetry (от pyproject.toml)

```bash
poetry install
```

### Ръчно тестване

Преди да подадете PR, е важно да тествате функционалността за превод с реална документация:

1. Създайте тестова директория в главната директория:
    ```bash
    mkdir test_docs
    ```

2. Копирайте някаква markdown документация и изображения, които искате да преведете, в тестовата директория. Например:
    ```bash
    cp /path/to/your/docs/*.md test_docs/
    cp /path/to/your/images/*.png test_docs/
    ```

3. Инсталирайте пакета локално:
    ```bash
    pip install -e .
    ```

4. Стартирайте Co-op Translator върху вашите тестови документи:
    ```bash
    python -m co_op_translator --language-codes ko --root-dir test_docs
    ```

5. Проверете преведените файлове в `test_docs/translations` and `test_docs/translated_images` to verify:
   - The translation quality
   - The metadata comments are correct
   - The original markdown structure is preserved
   - Links and images are working properly

This manual testing helps ensure that your changes work well in real-world scenarios.

### Environment variables

1. Create an `.env` file in the root directory by copying the provided `.env.template` файла.
1. Попълнете променливите на средата според указанията.

> [!TIP]
>
> ### Допълнителни опции за среда за разработка
>
> Освен да стартирате проекта локално, можете да използвате GitHub Codespaces или VS Code Dev Containers за алтернативна настройка на среда за разработка.
>
> #### GitHub Codespaces
>
> Можете да стартирате тези примери виртуално чрез GitHub Codespaces без нужда от допълнителни настройки.
>
> Бутонът ще отвори уеб базиран VS Code във вашия браузър:
>
> 1. Отворете шаблона (може да отнеме няколко минути):
>
>     [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/azure/co-op-translator)
>
> #### Стартиране локално чрез VS Code Dev Containers
>
> ⚠️ Тази опция работи само ако Docker Desktop има поне 16 GB RAM. Ако имате по-малко, можете да опитате [GitHub Codespaces опцията](../..) или [да я настроите локално](../..).
>
> Свързана опция е VS Code Dev Containers, който ще отвори проекта във вашия локален VS Code с помощта на [Dev Containers разширението](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers):
>
> 1. Стартирайте Docker Desktop (инсталирайте, ако не е инсталиран)
> 2. Отворете проекта:
>
>    [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator)


### Стил на кода

Използваме [Black](https://github.com/psf/black) като наш Python code formatter, за да поддържаме единен стил на кода в целия проект. Black е безкомпромисен форматиращ инструмент, който автоматично преформатира Python кода, за да отговаря на стандарта на Black.

#### Конфигурация

Конфигурацията на Black е описана в нашия `pyproject.toml`:

```toml
[tool.black]
line-length = 88
target-version = ['py310']
include = '\.pyi?$'
```

#### Инсталиране на Black

Можете да инсталирате Black с помощта на Poetry (препоръчително) или pip:

##### Използване на Poetry

Black се инсталира автоматично при настройка на средата за разработка:
```bash
poetry install
```

##### Използване на pip

Ако използвате pip, можете да инсталирате Black директно:
```bash
pip install black
```

#### Използване на Black

##### С Poetry

1. Форматирайте всички Python файлове в проекта:
    ```bash
    poetry run black .
    ```

2. Форматирайте конкретен файл или директория:
    ```bash
    poetry run black path/to/file_or_directory
    ```

##### С pip

1. Форматирайте всички Python файлове в проекта:
    ```bash
    black .
    ```

2. Форматирайте конкретен файл или директория:
    ```bash
    black path/to/file_or_directory
    ```

> [!TIP]
> Препоръчваме да настроите редактора си да форматира автоматично кода с Black при запис. Повечето съвременни редактори поддържат това чрез разширения или плъгини.

## Стартиране на Co-op Translator

За да стартирате Co-op Translator с Poetry във вашата среда, следвайте следните стъпки:

1. Отидете в директорията, където искате да правите тестове на превода, или създайте временна папка за тестване.

2. Изпълнете следната команда. Флагът `-l ko` with the language code you wish to translate into. The `-d` означава debug режим.

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> [!NOTE]
> Уверете се, че вашата Poetry среда е активирана (poetry shell) преди да изпълните командата.

## Поддържащи

### Формат на commit съобщенията и стратегия за сливане

За да осигурим консистентност и яснота в историята на commit-ите в нашия проект, следваме специфичен формат за commit съобщения **за крайното commit съобщение** при използване на стратегията **Squash and Merge**.

Когато pull request (PR) бъде слят, отделните commit-и се обединяват в един commit. Крайното commit съобщение трябва да следва формата по-долу, за да се поддържа чиста и ясна история.

#### Формат на commit съобщението (за squash and merge)

Използваме следния формат за commit съобщения:

```bash
<type>: <description> (#<PR number>)
```

- **type**: Определя категорията на commit-а. Използваме следните типове:
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

**Отказ от отговорност**:  
Този документ е преведен с помощта на AI преводаческа услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля, имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или неправилни тълкувания, произтичащи от използването на този превод.