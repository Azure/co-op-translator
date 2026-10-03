# اقدامات GitHub

هنگامی که می‌خواهید یک مخزن به‌صورت خودکار مستندات تغییر یافته را ترجمه کند و یک pull request با خروجی‌های تولید شده باز کند، از GitHub Actions استفاده کنید.

با پیکربندی استاندارد `GITHUB_TOKEN` شروع کنید، از جمله برای مخازن سازمانی که سیاست اجازه می‌دهد. وقتی سازمان شما نیاز به هویت یک App دارد یا نیاز به اجرای خودکار جریان‌های کاری پایین‌دست دارید، به بخش [راه‌اندازی GitHub App](#github-app-setup) مراجعه کنید.

**ویرایش‌های انسانی:** این جریان‌های کاری فایل‌های منبع تغییر یافته را به‌طور کامل مجدداً ترجمه می‌کنند و می‌توانند عبارت‌هایی که در ترجمه‌ها ویرایش شده‌اند را بازنویسی کنند. قبل از مرج کردن، هر PR را بازبینی کنید. برای حفظ سطح بلوک‌های Markdown از ویرایش‌های پذیرفته‌شده، نیاز به ادغام سفارشی با [Python API translation state provider](api.md#preserve-accepted-human-edits-with-a-translation-state-provider) است.

## اولین PR ترجمه‌ی README شما

با یک فایل ریشه‌ای `README.md` و یک زبان هدف شروع کنید. این جریان کاری تنها Markdown را ترجمه می‌کند، بنابراین Azure AI Vision مورد نیاز نیست.

1. فایل [translate-readme.yml](../../assets/workflows/translate-readme.yml) ([مشاهدهٔ الگو در GitHub](https://github.com/Azure/co-op-translator/blob/main/docs/assets/workflows/translate-readme.yml)) را در `.github/workflows/translate-readme.yml` در مخزنی که می‌خواهید ترجمه کنید کپی کنید، و آن را به شاخهٔ پیش‌فرض آن مخزن کامیت کنید. این الگو از Action ریشه‌ای `Azure/co-op-translator@main` استفاده می‌کند که CLI را از همان مرجع منبع نصب می‌کند. برای اجرای قابل بازتولید، یک کامیت بررسی‌شده را پین کنید.
2. به **Actions > Translate README > Run workflow** بروید، یک زبان انتخاب کنید، و تیک **Preview only** را بزنید. برآورد توکن را در مرحلهٔ پیش‌نمایش بررسی کنید. پیش‌نمایش هیچ‌یک از ارائه‌دهندگان مدل را فراخوانی نمی‌کند، ترجمه‌ها را نمی‌نویسد، و PR ایجاد نمی‌کند.
3. اسرار مربوط به یک [ارائه‌دهندهٔ متن](#prerequisites) را اضافه کنید، و گزینهٔ **اجازه دهید GitHub Actions درخواست‌های pull را ایجاد و تأیید کند** را در **تنظیمات > Actions > General** فعال نمایید. الگو برای کار خود `contents: write` و `pull-requests: write` را درخواست می‌کند؛ نیازی به تغییر مجوزهای پیش‌فرض برای هر جریان کاری نیست. اگر سیاست سازمانی این مجوزها یا این تنظیم را مسدود می‌کند، از یک مدیر در مورد یک [اپلیکیشن GitHub](#github-app-setup) تأیید‌شده سؤال کنید.
4. جریان کاری را دوباره اجرا کنید و تیک **Preview only** را بردارید. این پیش‌نمایش می‌کند، ترجمه می‌کند، `co-op-review --readme-only` را اجرا می‌کند، و تنها پس از موفقیت در ترجمه و بازبینی یک PR ترجمه ایجاد یا به‌روز می‌کند. خلاصهٔ جریان کاری به PR لینک می‌دهد.
5. عبارت‌بندی و تغییرات فایل در PR را بازبینی کنید، سپس وقتی آماده بودید مرج کنید. جریان کاری به‌صورت خودکار مرج نمی‌کند.

PR تنها شامل `translations/<language>/README.md` و فایل متادیتای زبان آن است. README منبع بدون تغییر باقی می‌ماند، و لینک‌ها به سایر اسناد همچنان به اسناد منبع اشاره می‌کنند. بدنهٔ PR فهرستی از فایل‌های تغییر یافته و نتایج بازبینی ساختاری را فهرست می‌کند. اگر ترجمه یا بازبینی شکست خورد، خلاصهٔ جریان کاری و لاگ‌های مرحلهٔ ناموفق را بررسی کنید؛ در این صورت هیچ PR‌ای ایجاد نمی‌شود. اگر تغییری وجود نداشته باشد، نیازی به PR جدید نیست.

**یادداشت سازمان و CI:** استفاده از GitHub App اختیاری است و الزام مالکیت سازمانی نیست. با `GITHUB_TOKEN`، جریان‌های کاری مربوط به pull-request برای باز کردن، به‌روزرسانی یا بازکردن مجدد PR نیازمند کاربری با سطح دسترسی نوشتن هستند تا گزینهٔ **Approve workflows to run** را انتخاب کند. جریان‌های کاری push با این توکن تحریک نمی‌شوند. برای CI پایین‌دست بدون حضور انسانی، به [راه‌اندازی GitHub App](#github-app-setup) و [قوانین تحریک جریان کاری](https://docs.github.com/en/actions/how-tos/writing-workflows/choosing-when-your-workflow-runs/triggering-a-workflow) GitHub مراجعه کنید.

## پیش‌نیازها

قبل از ایجاد جریان کاری، اسرار سرویس‌های AI که اجرای ترجمه شما نیاز دارد را پیکربندی کنید.

ترجمهٔ متن به یک ارائه‌دهندهٔ مدل زبانی نیاز دارد:

- Azure OpenAI: `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_MODEL_NAME`, `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME`, `AZURE_OPENAI_API_VERSION`
- OpenAI: `OPENAI_API_KEY`, `OPENAI_CHAT_MODEL_ID`, plus optional `OPENAI_ORG_ID` and `OPENAI_BASE_URL`
- Anthropic: `ANTHROPIC_API_KEY`, `ANTHROPIC_MODEL`, plus optional `ANTHROPIC_BASE_URL`

برای ترجمهٔ تصاویر همچنین Azure AI Vision لازم است:

- `AZURE_AI_SERVICE_API_KEY`
- `AZURE_AI_SERVICE_ENDPOINT`

برای جزئیات پیکربندی محلی به [Configuration](configuration.md) و [Azure AI Setup](azure-ai-setup.md) مراجعه کنید.

## پیکربندی استاندارد

پس از امتحان جریان کاری README، از این پیکربندی برای ترجمهٔ فایل‌های Markdown یک مخزن به چندین زبان استفاده کنید. این کار قبل از باز کردن PR یک بازبینی Markdown اجرا می‌کند و نیاز به Azure AI Vision ندارد.

### مرحلهٔ ۱: افزودن اسرار مخزن

در مخزن هدف خود، به **Settings** > **Secrets and variables** > **Actions** بروید، سپس اسرار ارائه‌دهنده‌ای را که جریان کاری استفاده می‌کند اضافه کنید.

![انتخاب اسرار Actions](../../assets/github-actions/select-setting-action.png)

### مرحلهٔ ۲: فعال‌سازی مجوزهای جریان کاری

به **Settings** > **Actions** > **General** بروید.

در بخش **Workflow permissions**:

1. گزینهٔ **اجازه دهید GitHub Actions درخواست‌های pull را ایجاد و تأیید کند** را فعال کنید.
2. تنظیم را ذخیره کنید.

کار زیر به‌صراحت `contents: write` و `pull-requests: write` را درخواست می‌کند. مجوزهای پیش‌فرض جریان کاری مخزن را تغییر ندهید. اگر سیاست سازمانی ایجاد PR را مسدود می‌کند، از یک مدیر در مورد یک [GitHub App](#github-app-setup) تایید‌شده پرس‌وجو کنید.

### مرحلهٔ ۳: افزودن جریان کاری

فایل `.github/workflows/co-op-translator.yml` را ایجاد کنید:

```yaml
name: Co-op Translator

on:
  push:
    branches:
      - main

jobs:
  co-op-translator:
    runs-on: ubuntu-latest
    env:
      TARGET_LANGUAGES: "es fr de"

    permissions:
      contents: write
      pull-requests: write

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Set up Python
        uses: actions/setup-python@v7
        with:
          python-version: "3.11"

      - name: Install Co-op Translator
        run: |
          python -m pip install --upgrade pip
          pip install co-op-translator

      - name: Run Co-op Translator
        env:
          PYTHONIOENCODING: utf-8
          AZURE_OPENAI_API_KEY: ${{ secrets.AZURE_OPENAI_API_KEY }}
          AZURE_OPENAI_ENDPOINT: ${{ secrets.AZURE_OPENAI_ENDPOINT }}
          AZURE_OPENAI_MODEL_NAME: ${{ secrets.AZURE_OPENAI_MODEL_NAME }}
          AZURE_OPENAI_CHAT_DEPLOYMENT_NAME: ${{ secrets.AZURE_OPENAI_CHAT_DEPLOYMENT_NAME }}
          AZURE_OPENAI_API_VERSION: ${{ secrets.AZURE_OPENAI_API_VERSION }}
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
          OPENAI_ORG_ID: ${{ secrets.OPENAI_ORG_ID }}
          OPENAI_CHAT_MODEL_ID: ${{ secrets.OPENAI_CHAT_MODEL_ID }}
          OPENAI_BASE_URL: ${{ secrets.OPENAI_BASE_URL }}
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
          ANTHROPIC_MODEL: ${{ secrets.ANTHROPIC_MODEL }}
          ANTHROPIC_BASE_URL: ${{ secrets.ANTHROPIC_BASE_URL }}
        run: |
          translate -l "$TARGET_LANGUAGES" -md -y

      - name: Review Markdown translations
        run: |
          python - <<'PY'
          import os
          from co_op_translator.api import run_review

          run_review(
              language_codes=os.environ["TARGET_LANGUAGES"].split(),
              markdown=True,
              notebook=False,
              output_format="github",
          )
          PY

      - name: Create Pull Request with translations
        uses: peter-evans/create-pull-request@v5
        with:
          token: ${{ secrets.GITHUB_TOKEN }}
          commit-message: "Update translations via Co-op Translator"
          title: "Update translations via Co-op Translator"
          body: |
            This PR updates translations for recent changes to the main branch.
            Markdown structure, freshness, and local links were reviewed.
            Review translation wording before merging.

            Generated by Co-op Translator.
          branch: update-translations
          base: main
          labels: translation, automated-pr
          delete-branch: true
          add-paths: |
            translations/
```

مقدار `TARGET_LANGUAGES` را به زبان‌هایی که پروژهٔ شما نیاز دارد تغییر دهید. بازبینی از Python API برای بررسی تنها Markdown استفاده می‌کند که با مرحلهٔ ترجمه مطابقت دارد. خطا در ترجمه یا بازبینی قبل از ایجاد PR کار را متوقف می‌کند. جریان کاری PR را به‌طور خودکار مرج نمی‌کند. برای مخازن بزرگ، یک فیلتر `paths:` را زیر `on.push` اضافه کنید تا جریان کاری تنها زمانی اجرا شود که مستندات تغییر کنند.

### اختیاری: دفترچه‌ها (notebooks) و تصاویر

برای دفترچه‌ها، `-nb` را به فرمان ترجمه اضافه کنید و `notebook=True` را در مرحلهٔ بازبینی تنظیم کنید. برای متن تصاویر، دو [Azure AI Vision secrets](#prerequisites) را پیکربندی کنید، آن‌ها را در `env` مرحلهٔ ترجمه پاس دهید، `-img` را به فرمان اضافه کنید، و `translated_images/` را به `add-paths` مرحلهٔ PR اضافه نمایید. تصاویر ترجمه‌شده را به‌صورت بصری بازبینی کنید؛ بازبینی تعیین‌شده صحت متن تصویر یا دقت زبانی را تضمین نمی‌کند.

## راه‌اندازی GitHub App

زمانی که سازمان شما نیاز به هویت App دارد یا وقتی PR تولیدشده باید بدون مرحلهٔ تأیید `GITHUB_TOKEN`، CI پایین‌دست را تحریک کند، از یک GitHub App تأیید‌شده استفاده کنید. یک App سیاست سازمان را دور نمی‌زند؛ مدیران نصب و مجوزهای آن را هنوز کنترل می‌کنند.

### مرحلهٔ ۱: ایجاد یا نصب یک GitHub App

در صورت دسترس بودن از یک App ارائه‌شده توسط سازمان استفاده کنید، یا یکی بسازید که دسترسی خواندن/نوشتن به **Contents** و **Pull requests** داشته باشد. آن را روی مخزن هدف با هر تأیید سازمانی لازم نصب کنید.

ثبت کنید:

- شناسهٔ App
- محتوای کلید خصوصی

آن‌ها را به‌عنوان اسرار مخزن ذخیره کنید:

- `GH_APP_ID`
- `GH_APP_PRIVATE_KEY`

### مرحلهٔ ۲: تولید یک توکن App

این مرحله را بلافاصله قبل از مرحلهٔ pull request موجود اضافه کنید. برای قالب README، از همان شرط موفقیت استفاده کنید تا پیش‌نمایش‌ها و ترجمه‌های ناموفق درخواست توکن App نکنند:

```yaml
      - name: Authenticate GitHub App
        id: generate_token
        if: ${{ !inputs.preview && steps.translate.outcome == 'success' && steps.review.outcome == 'success' }}
        uses: actions/create-github-app-token@v2
        with:
          app-id: ${{ secrets.GH_APP_ID }}
          private-key: ${{ secrets.GH_APP_PRIVATE_KEY }}
          permission-contents: write
          permission-pull-requests: write
```

سپس تنها ورودی `token` از مرحلهٔ pull request موجود را به `${{ steps.generate_token.outputs.token }}` تغییر دهید. شرط موفقیت، شاخه، بدنهٔ PR، و `add-paths` آن را بدون تغییر نگه دارید. به‌طور پیش‌فرض این توکن به مخزن جاری محدود است. هنگام تطبیق پیکربندی استاندارد به‌جای قالب README، `if` بالا را حذف کنید: آن جریان کاری از شرط موفقیت پیش‌فرض استفاده می‌کند، بنابراین ایجاد توکن و ایجاد PR تنها پس از موفقیت ترجمه و بازبینی اجرا می‌شوند.

برای نصب و مجوزهای توکن به Action رسمی [create-github-app-token](https://github.com/actions/create-github-app-token/tree/v2) مراجعه کنید.

## محدودیت‌های Runner

اجراکننده‌های میزبانی‌شده توسط GitHub دارای حداکثر مدت زمان کار هستند. مخازن بزرگ یا تعداد زیاد زبان‌های هدف می‌تواند بیش از این حد شود.

برای بارهای کاری بزرگ ترجمه:

- در هر اجرا زبان‌های کمتری را ترجمه کنید.
- از پرچم‌های محتوا مانند `-md`، `-nb` یا `-img` استفاده کنید.
- هنگامی که اندازهٔ مخزن یا تأخیر مدل موجب غیرقابل اعتماد شدن اجراکننده‌های میزبانی‌شده می‌شود، از یک runner خودمیزبان استفاده کنید.

## بازبینی در CI

وقتی یک pull request باید ترجمه‌های تولیدشده را بدون فراخوانی ارائه‌دهندگان LLM یا Vision اعتبارسنجی کند، از `co-op-review` استفاده کنید.

```yaml
      - name: Review translated outputs
        run: |
          co-op-review --changed-from "origin/${{ github.base_ref }}" --format github
```

`co-op-review` یک فرمان بازبینی تعیین‌شده در حالت بتا است. بررسی‌ها و ساختار خروجی آن ممکن است تکامل یابد، اما طوری طراحی شده است که برای CI ایمن باشد زیرا فایل‌ها را نمی‌نویسد و ارائه‌دهندگان مدل را فراخوانی نمی‌کند.