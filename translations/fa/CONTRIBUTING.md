<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d95d7ec0097c5569ac16dd42840787a2",
  "translation_date": "2025-06-12T09:25:53+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "fa"
}
-->
# مشارکت در Co-op Translator

این پروژه از مشارکت‌ها و پیشنهادات استقبال می‌کند. بیشتر مشارکت‌ها مستلزم موافقت شما با قرارداد مجوز مشارکت‌کننده (CLA) است که اعلام می‌کند شما حق دارید و واقعاً این حق را به ما می‌دهید که از مشارکت شما استفاده کنیم. برای جزئیات بیشتر به https://cla.opensource.microsoft.com مراجعه کنید.

هنگامی که درخواست pull ارسال می‌کنید، ربات CLA به‌طور خودکار تعیین می‌کند که آیا نیاز به ارائه CLA دارید و درخواست را به‌طور مناسب علامت‌گذاری می‌کند (مثلاً بررسی وضعیت، نظر). کافی است دستورالعمل‌های ارائه‌شده توسط ربات را دنبال کنید. تنها یک بار برای همه مخازن استفاده‌کننده از CLA ما باید این کار را انجام دهید.

## راه‌اندازی محیط توسعه

برای راه‌اندازی محیط توسعه این پروژه، توصیه می‌کنیم از Poetry برای مدیریت وابستگی‌ها استفاده کنید. ما از `pyproject.toml` برای مدیریت وابستگی‌های پروژه استفاده می‌کنیم، بنابراین برای نصب وابستگی‌ها باید از Poetry استفاده کنید.

### ایجاد محیط مجازی

#### استفاده از pip

```bash
python -m venv .venv
```

#### استفاده از Poetry

```bash
poetry init
```

### فعال‌سازی محیط مجازی

#### برای هر دو pip و Poetry

- ویندوز:

    ```bash
    .venv\Scripts\activate.bat
    ```

- مک/لینوکس:

    ```bash
    source .venv/bin/activate
    ```

#### استفاده از Poetry

```bash
poetry shell
```

### نصب بسته و بسته‌های مورد نیاز

#### استفاده از Poetry (از pyproject.toml)

```bash
poetry install
```

### تست دستی

قبل از ارسال PR، مهم است که عملکرد ترجمه را با مستندات واقعی تست کنید:

1. یک دایرکتوری تست در دایرکتوری اصلی ایجاد کنید:
    ```bash
    mkdir test_docs
    ```

2. برخی از مستندات مارک‌داون و تصاویر مورد نظر برای ترجمه را در دایرکتوری تست کپی کنید. برای مثال:
    ```bash
    cp /path/to/your/docs/*.md test_docs/
    cp /path/to/your/images/*.png test_docs/
    ```

3. بسته را به صورت محلی نصب کنید:
    ```bash
    pip install -e .
    ```

4. Co-op Translator را روی مستندات تست خود اجرا کنید:
    ```bash
    python -m co_op_translator --language-codes ko --root-dir test_docs
    ```

5. فایل‌های ترجمه‌شده را در `test_docs/translations` and `test_docs/translated_images` to verify:
   - The translation quality
   - The metadata comments are correct
   - The original markdown structure is preserved
   - Links and images are working properly

This manual testing helps ensure that your changes work well in real-world scenarios.

### Environment variables

1. Create an `.env` file in the root directory by copying the provided `.env.template` بررسی کنید.
1. متغیرهای محیطی را مطابق راهنمایی پر کنید.

> [!TIP]
>
> ### گزینه‌های اضافی محیط توسعه
>
> علاوه بر اجرای پروژه به‌صورت محلی، می‌توانید از GitHub Codespaces یا VS Code Dev Containers برای راه‌اندازی جایگزین محیط توسعه استفاده کنید.
>
> #### GitHub Codespaces
>
> می‌توانید این نمونه‌ها را به صورت مجازی با استفاده از GitHub Codespaces اجرا کنید و نیازی به تنظیمات اضافی نیست.
>
> این دکمه یک نمونه VS Code مبتنی بر وب را در مرورگر شما باز می‌کند:
>
> 1. قالب را باز کنید (ممکن است چند دقیقه طول بکشد):
>
>     [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/azure/co-op-translator)
>
> #### اجرای محلی با استفاده از VS Code Dev Containers
>
> ⚠️ این گزینه فقط در صورتی کار می‌کند که Docker Desktop شما حداقل ۱۶ گیگابایت رم اختصاص داده باشد. اگر کمتر از ۱۶ گیگابایت رم دارید، می‌توانید گزینه [GitHub Codespaces](../..) را امتحان کنید یا [به‌صورت محلی راه‌اندازی کنید](../..).
>
> گزینه مرتبط VS Code Dev Containers است که پروژه را در VS Code محلی شما با استفاده از [افزونه Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) باز می‌کند:
>
> 1. Docker Desktop را راه‌اندازی کنید (اگر نصب نیست، نصب کنید)
> 2. پروژه را باز کنید:
>
>    [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator)


### سبک کدنویسی

ما از [Black](https://github.com/psf/black) به عنوان فرمت‌کننده کد پایتون استفاده می‌کنیم تا سبک کد در سراسر پروژه یکدست بماند. Black یک فرمت‌کننده کد بدون مصالحه است که به‌طور خودکار کد پایتون را بازفرمت می‌کند تا با سبک کد Black هماهنگ شود.

#### پیکربندی

پیکربندی Black در `pyproject.toml` ما مشخص شده است:

```toml
[tool.black]
line-length = 88
target-version = ['py310']
include = '\.pyi?$'
```

#### نصب Black

می‌توانید Black را با استفاده از Poetry (توصیه شده) یا pip نصب کنید:

##### استفاده از Poetry

Black به‌صورت خودکار هنگام راه‌اندازی محیط توسعه نصب می‌شود:
```bash
poetry install
```

##### استفاده از pip

اگر از pip استفاده می‌کنید، می‌توانید Black را مستقیماً نصب کنید:
```bash
pip install black
```

#### استفاده از Black

##### با Poetry

1. تمام فایل‌های پایتون پروژه را فرمت کنید:
    ```bash
    poetry run black .
    ```

2. یک فایل یا دایرکتوری خاص را فرمت کنید:
    ```bash
    poetry run black path/to/file_or_directory
    ```

##### با pip

1. تمام فایل‌های پایتون پروژه را فرمت کنید:
    ```bash
    black .
    ```

2. یک فایل یا دایرکتوری خاص را فرمت کنید:
    ```bash
    black path/to/file_or_directory
    ```

> [!TIP]
> توصیه می‌کنیم ویرایشگر خود را طوری تنظیم کنید که هنگام ذخیره به‌طور خودکار کد را با Black فرمت کند. بیشتر ویرایشگرهای مدرن این قابلیت را از طریق افزونه یا پلاگین پشتیبانی می‌کنند.

## اجرای Co-op Translator

برای اجرای Co-op Translator با استفاده از Poetry در محیط خود، مراحل زیر را دنبال کنید:

1. به دایرکتوری‌ای بروید که می‌خواهید تست‌های ترجمه را در آن انجام دهید یا یک پوشه موقت برای تست بسازید.

2. دستور زیر را اجرا کنید. پرچم `-l ko` with the language code you wish to translate into. The `-d` حالت اشکال‌زدایی را نشان می‌دهد.

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> [!NOTE]
> مطمئن شوید محیط Poetry شما فعال است (poetry shell) قبل از اجرای دستور.

## نگهدارندگان

### پیام کامیت و استراتژی ادغام

برای اطمینان از ثبات و وضوح در تاریخچه کامیت پروژه، ما از قالب خاصی برای پیام کامیت **کامیت نهایی** هنگام استفاده از استراتژی **Squash and Merge** پیروی می‌کنیم.

وقتی یک pull request (PR) ادغام می‌شود، کامیت‌های جداگانه به یک کامیت واحد فشرده می‌شوند. پیام کامیت نهایی باید قالب زیر را داشته باشد تا تاریخچه‌ای تمیز و منسجم حفظ شود.

#### قالب پیام کامیت (برای squash and merge)

ما از قالب زیر برای پیام‌های کامیت استفاده می‌کنیم:

```bash
<type>: <description> (#<PR number>)
```

- **type**: دسته‌بندی کامیت را مشخص می‌کند. ما از انواع زیر استفاده می‌کنیم:
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

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه ماشینی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نادرستی‌هایی باشند. سند اصلی به زبان بومی آن باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، توصیه می‌شود از ترجمه حرفه‌ای انسانی استفاده شود. ما مسئول هیچ گونه سوءتفاهم یا تفسیر نادرستی که ناشی از استفاده از این ترجمه باشد، نیستیم.