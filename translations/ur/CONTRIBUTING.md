<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d95d7ec0097c5569ac16dd42840787a2",
  "translation_date": "2025-06-12T09:26:19+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "ur"
}
-->
# تعاون مترجم میں تعاون

یہ پروجیکٹ تعاون اور تجاویز کا خیرمقدم کرتا ہے۔ زیادہ تر تعاون کے لیے آپ کو ایک Contributor License Agreement (CLA) سے اتفاق کرنا ہوگا جو یہ ظاہر کرتا ہے کہ آپ کے پاس حق ہے اور آپ واقعی ہمیں اپنے تعاون کے استعمال کے حقوق دیتے ہیں۔ تفصیلات کے لیے ملاحظہ کریں https://cla.opensource.microsoft.com۔

جب آپ pull request جمع کرواتے ہیں، تو ایک CLA بوٹ خودکار طور پر طے کرے گا کہ آیا آپ کو CLA فراہم کرنا ضروری ہے اور PR کو مناسب طریقے سے سجائے گا (مثلاً، اسٹیٹس چیک، تبصرہ)۔ بس بوٹ کی ہدایات پر عمل کریں۔ آپ کو یہ صرف ایک بار ہمارے CLA استعمال کرنے والے تمام ریپوز میں کرنا ہوگا۔

## ترقیاتی ماحول کی ترتیب

اس پروجیکٹ کے لیے ترقیاتی ماحول ترتیب دینے کے لیے، ہم سفارش کرتے ہیں کہ Poetry استعمال کریں تاکہ dependencies کا انتظام کیا جا سکے۔ ہم `pyproject.toml` استعمال کرتے ہیں تاکہ پروجیکٹ کی dependencies کو منظم کیا جا سکے، لہٰذا dependencies انسٹال کرنے کے لیے Poetry استعمال کریں۔

### ورچوئل ماحول بنائیں

#### pip استعمال کرتے ہوئے

```bash
python -m venv .venv
```

#### Poetry استعمال کرتے ہوئے

```bash
poetry init
```

### ورچوئل ماحول کو فعال کریں

#### pip اور Poetry دونوں کے لیے

- ونڈوز:

    ```bash
    .venv\Scripts\activate.bat
    ```

- میک/لینکس:

    ```bash
    source .venv/bin/activate
    ```

#### Poetry استعمال کرتے ہوئے

```bash
poetry shell
```

### پیکج اور ضروری پیکجز انسٹال کرنا

#### Poetry استعمال کرتے ہوئے (pyproject.toml سے)

```bash
poetry install
```

### دستی ٹیسٹنگ

PR جمع کروانے سے پہلے، ترجمے کی فعالیت کو حقیقی دستاویزات کے ساتھ ٹیسٹ کرنا ضروری ہے:

1. روٹ ڈائریکٹری میں ایک ٹیسٹ ڈائریکٹری بنائیں:
    ```bash
    mkdir test_docs
    ```

2. کچھ مارک ڈاؤن دستاویزات اور تصاویر جو آپ ترجمہ کرنا چاہتے ہیں، ٹیسٹ ڈائریکٹری میں کاپی کریں۔ مثلاً:
    ```bash
    cp /path/to/your/docs/*.md test_docs/
    cp /path/to/your/images/*.png test_docs/
    ```

3. پیکج لوکل طور پر انسٹال کریں:
    ```bash
    pip install -e .
    ```

4. اپنے ٹیسٹ دستاویزات پر Co-op Translator چلائیں:
    ```bash
    python -m co_op_translator --language-codes ko --root-dir test_docs
    ```

5. `test_docs/translations` and `test_docs/translated_images` to verify:
   - The translation quality
   - The metadata comments are correct
   - The original markdown structure is preserved
   - Links and images are working properly

This manual testing helps ensure that your changes work well in real-world scenarios.

### Environment variables

1. Create an `.env` file in the root directory by copying the provided `.env.template` فائل میں ترجمہ شدہ فائلز چیک کریں۔
1. ماحول کے متغیرات کو ہدایات کے مطابق پر کریں۔

> [!TIP]
>
> ### اضافی ترقیاتی ماحول کے اختیارات
>
> پروجیکٹ کو لوکل چلانے کے علاوہ، آپ GitHub Codespaces یا VS Code Dev Containers بھی استعمال کر سکتے ہیں تاکہ متبادل ترقیاتی ماحول ترتیب دیا جا سکے۔
>
> #### GitHub Codespaces
>
> آپ GitHub Codespaces استعمال کر کے اس نمونے کو ورچوئل طور پر چلا سکتے ہیں اور کوئی اضافی سیٹنگ یا ترتیب درکار نہیں۔
>
> بٹن آپ کے براؤزر میں ویب بیسڈ VS Code کا انسٹینس کھولے گا:
>
> 1. ٹیمپلیٹ کھولیں (یہ چند منٹ لے سکتا ہے):
>
>     [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/azure/co-op-translator)
>
> #### VS Code Dev Containers کے ذریعے لوکل چلانا
>
> ⚠️ یہ آپشن صرف اس صورت میں کام کرے گا جب آپ کے Docker Desktop کو کم از کم 16 GB RAM مختص کی گئی ہو۔ اگر آپ کے پاس 16 GB سے کم RAM ہے، تو آپ [GitHub Codespaces آپشن](../..) آزما سکتے ہیں یا [لوکل ترتیب دے سکتے ہیں](../..)۔
>
> ایک متعلقہ آپشن VS Code Dev Containers ہے، جو پروجیکٹ کو آپ کے لوکل VS Code میں [Dev Containers ایکسٹینشن](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) کے ذریعے کھولے گا:
>
> 1. Docker Desktop شروع کریں (اگر انسٹال نہیں کیا تو انسٹال کریں)
> 2. پروجیکٹ کھولیں:
>
>    [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator)


### کوڈ اسٹائل

ہم [Black](https://github.com/psf/black) استعمال کرتے ہیں تاکہ Python کوڈ فارمیٹر کے طور پر پروجیکٹ میں یکساں کوڈ اسٹائل برقرار رکھا جا سکے۔ Black ایک غیر متزلزل کوڈ فارمیٹر ہے جو خودکار طور پر Python کوڈ کو Black کوڈ اسٹائل کے مطابق دوبارہ فارمیٹ کرتا ہے۔

#### کنفیگریشن

Black کی کنفیگریشن ہماری `pyproject.toml` میں مخصوص ہے:

```toml
[tool.black]
line-length = 88
target-version = ['py310']
include = '\.pyi?$'
```

#### Black انسٹال کرنا

آپ Black Poetry (تجویز کردہ) یا pip دونوں سے انسٹال کر سکتے ہیں:

##### Poetry استعمال کرتے ہوئے

جب آپ ترقیاتی ماحول سیٹ اپ کرتے ہیں تو Black خودکار طور پر انسٹال ہو جاتا ہے:
```bash
poetry install
```

##### pip استعمال کرتے ہوئے

اگر آپ pip استعمال کر رہے ہیں تو Black کو براہ راست انسٹال کر سکتے ہیں:
```bash
pip install black
```

#### Black استعمال کرنا

##### Poetry کے ساتھ

1. پروجیکٹ میں تمام Python فائلز کو فارمیٹ کریں:
    ```bash
    poetry run black .
    ```

2. کسی مخصوص فائل یا ڈائریکٹری کو فارمیٹ کریں:
    ```bash
    poetry run black path/to/file_or_directory
    ```

##### pip کے ساتھ

1. پروجیکٹ میں تمام Python فائلز کو فارمیٹ کریں:
    ```bash
    black .
    ```

2. کسی مخصوص فائل یا ڈائریکٹری کو فارمیٹ کریں:
    ```bash
    black path/to/file_or_directory
    ```

> [!TIP]
> ہم سفارش کرتے ہیں کہ آپ اپنے ایڈیٹر کو اس طرح سیٹ کریں کہ کوڈ کو محفوظ کرتے وقت خودکار طور پر Black کے ذریعے فارمیٹ کرے۔ زیادہ تر جدید ایڈیٹرز اس کی حمایت ایکسٹینشنز یا پلگ انز کے ذریعے کرتے ہیں۔

## Co-op Translator چلانا

اپنے ماحول میں Poetry استعمال کرتے ہوئے Co-op Translator چلانے کے لیے درج ذیل مراحل پر عمل کریں:

1. اس ڈائریکٹری پر جائیں جہاں آپ ترجمے کے ٹیسٹ کرنا چاہتے ہیں یا ٹیسٹنگ کے لیے عارضی فولڈر بنائیں۔

2. درج ذیل کمانڈ چلائیں۔ `-l ko` with the language code you wish to translate into. The `-d` فلیگ ڈیبگ موڈ ظاہر کرتا ہے۔

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> [!NOTE]
> کمانڈ چلانے سے پہلے یقینی بنائیں کہ آپ کا Poetry ماحول فعال ہے (poetry shell)۔

## مینٹینرز

### کمیٹ میسج اور مرج حکمت عملی

اپنے پروجیکٹ کی کمیٹ ہسٹری میں یکسانیت اور وضاحت کو یقینی بنانے کے لیے، ہم **Squash and Merge** حکمت عملی استعمال کرتے ہوئے **آخری کمیٹ میسج** کے لیے مخصوص کمیٹ میسج فارمیٹ پر عمل کرتے ہیں۔

جب کوئی pull request (PR) مرج ہوتا ہے، تو انفرادی کمیٹس کو ایک واحد کمیٹ میں سمودھ کیا جائے گا۔ آخری کمیٹ میسج نیچے دیے گئے فارمیٹ کے مطابق ہونا چاہیے تاکہ ہسٹری صاف اور یکساں رہے۔

#### کمیٹ میسج فارمیٹ (squash and merge کے لیے)

ہم کمیٹ میسجز کے لیے درج ذیل فارمیٹ استعمال کرتے ہیں:

```bash
<type>: <description> (#<PR number>)
```

- **type**: کمیٹ کی قسم کی وضاحت کرتا ہے۔ ہم درج ذیل اقسام استعمال کرتے ہیں:
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

**دستخط**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ اگرچہ ہم درستگی کی کوشش کرتے ہیں، براہ کرم آگاہ رہیں کہ خودکار تراجم میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصل دستاویز اپنی مادری زبان میں ہی معتبر ماخذ سمجھی جانی چاہیے۔ اہم معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ ہم اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کے ذمہ دار نہیں ہیں۔