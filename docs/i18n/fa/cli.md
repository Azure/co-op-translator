# مرجع CLI

Co-op Translator نقاط ورود خط فرمان زیر را نصب می‌کند:

- `translate`
- `evaluate`
- `migrate-links`
- `co-op-review`
- `co-op-translator-mcp`

دستورات `translate`، `evaluate`، `migrate-links` و `co-op-review` از طریق `co_op_translator.__main__` ارسال می‌شوند که پیاده‌سازی دستور را بر اساس نام اسکریپت فراخوانی‌شده انتخاب می‌کند. سرور MCP مستقیماً از `co_op_translator.mcp.server` استفاده می‌کند.

اگر بین CLI، API پایتون و MCP تصمیم می‌گیرید، از [Choose Your Workflow](workflows.md) شروع کنید.

## جریان اولیه CLI

اگر از Co-op Translator از طریق ترمینال استفاده می‌کنید از این‌جا شروع کنید:

1. یک ارائه‌دهنده LLM را طبق توضیحات در [Configuration](configuration.md) پیکربندی کنید.
2. نوع محتوایی را که می‌خواهید ترجمه کنید انتخاب کنید.
3. ابتدا یک فرمان متمرکز را اجرا کنید، مانند ترجمه فقط Markdown.
4. قبل از اعمال تغییرات بزرگ در مخزن از `--dry-run` استفاده کنید.
5. پس از ترجمه از `co-op-review` برای بررسی ساختار و تازگی استفاده کنید.

| Goal | Command to start with |
| --- | --- |
| Translate Markdown documents | `translate -l "ko" -md` |
| Translate notebooks | `translate -l "ko" -nb` |
| Translate image text | `translate -l "ko" -img` |
| Preview work without writing files | `translate -l "ko" -md --dry-run` |
| Review existing translations | `co-op-review -l "ko"` |
| Update notebook and Markdown links | `migrate-links -l "ko" --dry-run` |
| Expose tools to an MCP client | Configure the [MCP Server](mcp.md) instead of running CLI commands directly. |

## translate

Translate Markdown files, notebooks, and image text into one or more target languages.

```bash
translate -l "ko ja fr"
```

### مثال‌های رایج

ترجمه فقط Markdown:

```bash
translate -l "de" -md
```

ترجمه فقط دفترچه‌ها:

```bash
translate -l "zh-CN" -nb
```

ترجمه Markdown و تصاویر:

```bash
translate -l "pt-BR" -md -img
```

به‌روزرسانی ترجمه‌های موجود با حذف و بازسازی آن‌ها:

```bash
translate -l "ko" -u
```

اجرای بدون درخواست‌های تعاملی:

```bash
translate -l "ko ja" -md -y
```

ذخیره لاگ‌ها:

```bash
translate -l "ko" -s
```

### گزینه‌ها

| Option | Required | Description |
| --- | --- | --- |
| `-l`, `--language-codes` | Yes | Space-separated language codes, such as `"es fr de"`, or `"all"`. |
| `-r`, `--root-dir` | No | Project root. Defaults to the current directory. |
| `-u`, `--update` | No | Delete existing translations for selected languages and recreate them. |
| `-img`, `--images` | No | Translate only image files. |
| `-md`, `--markdown` | No | Translate only Markdown files. |
| `-nb`, `--notebook` | No | Translate only Jupyter notebook files. |
| `-d`, `--debug` | No | Enable debug logging in the console. |
| `-s`, `--save-logs` | No | Save DEBUG-level logs under `<root-dir>/logs/`. |
| `-x`, `--fix` | No | Retranslate low-confidence Markdown files based on previous evaluation results. |
| `-c`, `--min-confidence` | No | Confidence threshold for `--fix`. Defaults to `0.7`. |
| `--add-disclaimer`, `--no-disclaimer` | No | Add or suppress machine translation disclaimers. Defaults to enabled in the CLI. |
| `-f`, `--fast` | No | Deprecated fast image mode. |
| `-y`, `--yes` | No | Auto-confirm prompts, useful in CI. |
| `--repo-url` | No | Repository URL used in the README languages table sparse-checkout advisory. |
| `--migrate-language-folders` | No | Rename legacy alias folders, such as `cn` or `tw`, to canonical BCP 47 folders. |
| `--dry-run` | No | Preview language folder migration and translation estimates without writing files. |

اگر هیچ فلگ نوعی ارائه نشود، `translate` اسناد Markdown، دفترچه‌ها و تصاویر را پردازش می‌کند. ترجمه تصویر نیاز به پیکربندی Azure AI Vision دارد.

## evaluate

Evaluate translated Markdown quality for one language.

!!! warning "تجربی"
    `evaluate` آزمایشی است. این فرمان می‌تواند از بررسی‌های مبتنی بر قوانین و مبتنی بر LLM استفاده کند، نتایج ارزیابی را در متادیتای ترجمه می‌نویسد و مدل امتیازدهی و رفتار متادیتا ممکن است تغییر کند.

```bash
evaluate -l "ko"
```

### مثال‌های رایج

استفاده از آستانه پایین‌تر برای اعتماد:

```bash
evaluate -l "es" -c 0.8
```

اجرای چک‌های فقط مبتنی بر قوانین:

```bash
evaluate -l "fr" -f
```

اجرای چک‌های فقط مبتنی بر LLM:

```bash
evaluate -l "ja" -D
```

### گزینه‌ها

| Option | Required | Description |
| --- | --- | --- |
| `-l`, `--language-code` | Yes | Single language code to evaluate. Alias codes are normalized. |
| `-r`, `--root-dir` | No | Project root. Defaults to the current directory. |
| `-c`, `--min-confidence` | No | Threshold used when listing low-confidence translations. Defaults to `0.7`. |
| `-d`, `--debug` | No | Enable debug logging. |
| `-s`, `--save-logs` | No | Save DEBUG-level logs under `<root-dir>/logs/`. |
| `-f`, `--fast` | No | Rule-based evaluation only. |
| `-D`, `--deep` | No | LLM-based evaluation only. |

به‌صورت پیش‌فرض، `evaluate` از هر دو ارزیابی مبتنی بر قوانین و مبتنی بر LLM استفاده می‌کند. نتایج در متادیتای ترجمه نوشته می‌شوند و در کنسول خلاصه می‌شوند.

## co-op-review

Run deterministic translation maintenance checks without API credentials.

!!! note "نسخه بتا"
    `co-op-review` یک فرمان بازبینی تعیین‌شونده در نسخه بتا است. این فرمان از ارائه‌دهندگان مدل استفاده نمی‌کند و فایل‌ها را نمی‌نویسد، اما چک‌ها و ساختار خروجی مسائل ممکن است تکامل یابند.

```bash
co-op-review -l "ko"
```

### مثال‌های رایج

بازبینی ترجمه‌های کره‌ای و ژاپنی از دایرکتوری جاری:

```bash
co-op-review -l "ko ja"
```

بازبینی یک ریشه پروژه مشخص:

```bash
co-op-review -l "fr" -r ./my-course
```

بازبینی فقط فایل‌های منبع تغییر یافته در برابر یک ref پایه:

```bash
co-op-review -l "ko" --changed-from origin/main
```

چاپ خروجی Markdown با فرمت GitHub برای خلاصه‌های CI:

```bash
co-op-review -l "ko ja" --changed-from origin/main --format github
```

### گزینه‌ها

| Option | Required | Description |
| --- | --- | --- |
| `-l`, `--language-code` | No | Language code to review. Can be passed multiple times or as a space-separated value. Defaults to all discovered translation languages. |
| `-r`, `--root-dir` | No | Project root. Defaults to the current directory. |
| `--changed-from` | No | Git ref used to limit review to changed source files. |
| `--format` | No | Output format: `text` or `github`. Defaults to `text`. |

`co-op-review` در حال حاضر برای فایل‌های ترجمه‌شده گمشده، متادیتای ترجمه مفقود یا قدیمی، یکپارچگی frontmatter و code fenceهای Markdown، JSON دفترچه ترجمه‌شده نامعتبر و هدف‌های لینک محلی Markdown یا تصویر گمشده بررسی می‌کند. لینک‌های مفقود به‌صورت پیش‌فرض هشدار هستند؛ مشکلات ساختاری و تازگی فرمان را شکست می‌دهند.

## co-op-translator-mcp

Run the Co-op Translator MCP server for agents, editors, and MCP-compatible clients.

```bash
co-op-translator-mcp
```

The default transport is `stdio`. See the [MCP Server](mcp.md) guide for client configuration, tools, resources, and safety notes.

### Options

| Option | Required | Description |
| --- | --- | --- |
| `--transport` | No | MCP transport: `stdio`, `streamable-http`, or `sse`. Defaults to `stdio`. |

## migrate-links

Reprocess translated Markdown files and update notebook links so they point to translated notebooks when available.

```bash
migrate-links -l "ko ja"
```

### مثال‌های رایج

پیش‌نمایش به‌روزرسانی لینک‌ها:

```bash
migrate-links -l "ko" --dry-run
```

پردازش همه زبان‌های پشتیبانی‌شده بدون تأیید:

```bash
migrate-links -l "all" -y
```

فقط بازنویسی لینک‌ها زمانی که دفترچه‌های ترجمه‌شده موجود باشند:

```bash
migrate-links -l "ko" --no-fallback-to-original
```

### گزینه‌ها

| Option | Required | Description |
| --- | --- | --- |
| `-l`, `--language-codes` | Yes | Space-separated language codes, or `"all"`. |
| `-r`, `--root-dir` | No | Project root. Defaults to the current directory. |
| `--image-dir` | No | Translated image directory relative to the root. Defaults to `translated_images`. |
| `--dry-run` | No | Show files that would change without writing updates. |
| `--fallback-to-original`, `--no-fallback-to-original` | No | Use original notebook links when translated notebooks are missing. Enabled by default. |
| `-d`, `--debug` | No | Enable debug logging. |
| `-s`, `--save-logs` | No | Save DEBUG-level logs under `<root-dir>/logs/`. |
| `-y`, `--yes` | No | Auto-confirm prompts when processing all languages. |

## محیط

All commands require one configured LLM provider:

```bash
# آزور اوپن‌ای‌آی
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"

# یا اوپن‌ای‌آی
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

Image translation additionally requires Azure AI Vision:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

## ساختار خروجی

Text translations are written under:

```text
translations/<language-code>/<original-path>
```

Translated image output is written under:

```text
translated_images/<language-code>/<original-path>
```

For example, translating `README.md` and `docs/setup.md` into Korean produces:

```text
translations/ko/README.md
translations/ko/docs/setup.md
```

## مثال‌های CLI برای کپی-پیست

Translate Markdown into three languages:

```bash
translate -l "ko ja fr" -md
```

Translate notebooks only:

```bash
translate -l "zh-CN" -nb
```

Translate images only:

```bash
translate -l "pt-BR" -img
```

Preview Markdown translation without writing files:

```bash
translate -l "de es" -md --dry-run
```

Repair low-confidence Markdown translations:

```bash
evaluate -l "ko" -c 0.8
translate -l "ko" --fix -c 0.8 -md
```

Run CI-friendly Markdown translation:

```bash
translate -l "ko ja" -md -y -s
```

Review translated output:

```bash
co-op-review -l "ko ja"
```

Preview link migration:

```bash
migrate-links -l "ko" --dry-run
```