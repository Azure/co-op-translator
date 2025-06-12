<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d95d7ec0097c5569ac16dd42840787a2",
  "translation_date": "2025-06-12T09:45:00+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "my"
}
-->
# Co-op Translator میں تعاون کرنا

یہ پروجیکٹ تعاون اور تجاویز کا خیرمقدم کرتا ہے۔ زیادہ تر تعاون کے لیے آپ کو ایک  
Contributor License Agreement (CLA) سے اتفاق کرنا ہوتا ہے جس میں آپ اس بات کا اعلان کرتے ہیں کہ آپ کے پاس  
اپنے تعاون کے استعمال کے حقوق دینے کا اختیار اور حق ہے۔ تفصیلات کے لیے، یہاں جائیں: https://cla.opensource.microsoft.com۔

جب آپ pull request جمع کروائیں گے، تو CLA بوٹ خود بخود فیصلہ کرے گا کہ آیا آپ کو CLA فراہم کرنے کی ضرورت ہے  
اور PR پر مناسب نشان لگا دے گا (مثلاً، status check، comment)۔ بس بوٹ کی ہدایات پر عمل کریں۔  
یہ عمل آپ کو تمام ریپوز میں صرف ایک بار کرنا ہوگا جو ہمارا CLA استعمال کرتے ہیں۔

## Development environment setup

اس پروجیکٹ کے لیے development environment سیٹ اپ کرنے کے لیے، ہم dependencies کے انتظام کے لیے Poetry استعمال کرنے کی سفارش کرتے ہیں۔ ہم `pyproject.toml` کو project dependencies کے انتظام کے لیے استعمال کرتے ہیں، اس لیے dependencies انسٹال کرنے کے لیے Poetry استعمال کریں۔

### Create a virtual environment

#### Using pip

```bash
python -m venv .venv
```

#### Using Poetry

```bash
poetry init
```

### Activate the virtual environment

#### For both pip and Poetry

- Windows:

    ```bash
    .venv\Scripts\activate.bat
    ```

- Mac/Linux:

    ```bash
    source .venv/bin/activate
    ```

#### Using Poetry

```bash
poetry shell
```

### Installing the Package and required Packages

#### Using Poetry (from pyproject.toml)

```bash
poetry install
```

### Manual testing

PR جمع کروانے سے پہلے، ترجمے کی فعالیت کو اصلی دستاویزات کے ساتھ آزمانا ضروری ہے:

1. روٹ ڈائریکٹری میں ایک test ڈائریکٹری بنائیں:
    ```bash
    mkdir test_docs
    ```

2. کچھ markdown دستاویزات اور تصاویر جو آپ ترجمہ کرنا چاہتے ہیں، test ڈائریکٹری میں کاپی کریں۔ مثال کے طور پر:
    ```bash
    cp /path/to/your/docs/*.md test_docs/
    cp /path/to/your/images/*.png test_docs/
    ```

3. پیکیج کو لوکل طور پر انسٹال کریں:
    ```bash
    pip install -e .
    ```

4. اپنے test دستاویزات پر Co-op Translator چلائیں:
    ```bash
    python -m co_op_translator --language-codes ko --root-dir test_docs
    ```

5. ترجمہ شدہ فائلز `test_docs/translations` and `test_docs/translated_images` to verify:
   - The translation quality
   - The metadata comments are correct
   - The original markdown structure is preserved
   - Links and images are working properly

This manual testing helps ensure that your changes work well in real-world scenarios.

### Environment variables

1. Create an `.env` file in the root directory by copying the provided `.env.template` فائل میں چیک کریں۔  
1. ماحول کی متغیرات کو ہدایات کے مطابق پُر کریں۔

> [!TIP]
>
> ### اضافی development environment کے اختیارات
>
> مقامی طور پر پروجیکٹ چلانے کے علاوہ، آپ GitHub Codespaces یا VS Code Dev Containers بھی استعمال کر سکتے ہیں جو ایک متبادل development environment سیٹ اپ فراہم کرتے ہیں۔
>
> #### GitHub Codespaces
>
> آپ GitHub Codespaces کا استعمال کرتے ہوئے یہ نمونے ورچوئلی چلا سکتے ہیں اور کسی اضافی سیٹنگ یا سیٹ اپ کی ضرورت نہیں۔
>
> یہ بٹن آپ کے براؤزر میں ویب بیسڈ VS Code انسٹینس کھولے گا:
>
> 1. ٹیمپلیٹ کھولیں (یہ کچھ منٹ لے سکتا ہے):
>
>     [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/azure/co-op-translator)
>
> #### VS Code Dev Containers کے ذریعے مقامی طور پر چلانا
>
> ⚠️ یہ آپشن صرف اس صورت میں کام کرے گا جب آپ کے Docker Desktop کو کم از کم 16 GB RAM مختص کی گئی ہو۔ اگر آپ کے پاس 16 GB سے کم RAM ہے، تو آپ [GitHub Codespaces آپشن](../..) یا [مقامی سیٹ اپ](../..) آزما سکتے ہیں۔
>
> ایک متعلقہ آپشن VS Code Dev Containers ہے، جو پروجیکٹ کو آپ کے مقامی VS Code میں [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) کے ذریعے کھولے گا:
>
> 1. Docker Desktop شروع کریں (اگر انسٹال نہیں ہے تو انسٹال کریں)
> 2. پروجیکٹ کھولیں:
>
>    [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator)


### Code Style

ہم پورے پروجیکٹ میں consistent code style برقرار رکھنے کے لیے Python کوڈ فارمیٹر کے طور پر [Black](https://github.com/psf/black) استعمال کرتے ہیں۔ Black ایک سخت کوڈ فارمیٹر ہے جو Python کوڈ کو خودکار طور پر Black کے code style کے مطابق دوبارہ فارمیٹ کرتا ہے۔

#### Configuration

Black کی configuration ہمارے `pyproject.toml` میں مخصوص کی گئی ہے:

```toml
[tool.black]
line-length = 88
target-version = ['py310']
include = '\.pyi?$'
```

#### Installing Black

آپ Black کو Poetry (تجویز کردہ) یا pip کے ذریعے انسٹال کر سکتے ہیں:

##### Using Poetry

جب آپ development environment سیٹ اپ کرتے ہیں تو Black خود بخود انسٹال ہو جاتا ہے:  
```bash
poetry install
```

##### Using pip

اگر آپ pip استعمال کر رہے ہیں، تو آپ Black کو براہ راست انسٹال کر سکتے ہیں:  
```bash
pip install black
```

#### Using Black

##### With Poetry

1. پروجیکٹ میں تمام Python فائلز کو فارمیٹ کریں:  
    ```bash
    poetry run black .
    ```

2. مخصوص فائل یا ڈائریکٹری کو فارمیٹ کریں:  
    ```bash
    poetry run black path/to/file_or_directory
    ```

##### With pip

1. پروجیکٹ میں تمام Python فائلز کو فارمیٹ کریں:  
    ```bash
    black .
    ```

2. مخصوص فائل یا ڈائریکٹری کو فارمیٹ کریں:  
    ```bash
    black path/to/file_or_directory
    ```

> [!TIP]
> ہم تجویز کرتے ہیں کہ آپ اپنا ایڈیٹر اس طرح سیٹ کریں کہ کوڈ کو save کرتے وقت خودکار طور پر Black کے ساتھ فارمیٹ کرے۔ زیادہ تر جدید ایڈیٹرز اس کے لیے extensions یا plugins فراہم کرتے ہیں۔

## Co-op Translator چلانا

اپنے ماحول میں Poetry کے ذریعے Co-op Translator چلانے کے لیے، درج ذیل اقدامات کریں:

1. اس ڈائریکٹری میں جائیں جہاں آپ ترجمے کے ٹیسٹ کرنا چاہتے ہیں یا ٹیسٹنگ کے لیے عارضی فولڈر بنائیں۔

2. درج ذیل کمانڈ چلائیں۔ `-l ko` with the language code you wish to translate into. The `-d` فلیگ debug موڈ ظاہر کرتا ہے۔

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> [!NOTE]
> کمانڈ چلانے سے پہلے یقینی بنائیں کہ آپ کا Poetry environment فعال ہے (poetry shell)۔

## Maintainers

### Commit message اور Merge کی حکمت عملی

اپنے پروجیکٹ کے commit history میں یکسانیت اور وضاحت کو یقینی بنانے کے لیے، ہم **Squash and Merge** حکمت عملی استعمال کرتے ہوئے **آخری commit message** کے لیے ایک خاص format پر عمل کرتے ہیں۔

جب pull request (PR) merge ہوتا ہے، تو انفرادی commits ایک single commit میں squash ہو جاتے ہیں۔ آخری commit message نیچے دیے گئے format کے مطابق ہونی چاہیے تاکہ history صاف اور consistent رہے۔

#### Commit message format (for squash and merge)

ہم commit messages کے لیے درج ذیل format استعمال کرتے ہیں:

```bash
<type>: <description> (#<PR number>)
```

- **type**: commit کی قسم بتاتا ہے۔ ہم درج ذیل types استعمال کرتے ہیں:  
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

Sure! Could you please specify which language you mean by "my"? For example, "my" could refer to Myanmar (Burmese) language or something else. Let me know so I can provide the correct translation.