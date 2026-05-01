# CLI Reference

Co-op Translator installs four command-line entry points:

- `translate`
- `evaluate`
- `migrate-links`
- `co-op-review`

The dispatch logic lives in `co_op_translator.__main__`, which selects the command implementation based on the invoked script name.

## translate

Translate Markdown files, notebooks, and image text into one or more target languages.

```bash
translate -l "ko ja fr"
```

### Common examples

Translate only Markdown:

```bash
translate -l "de" -md
```

Translate only notebooks:

```bash
translate -l "zh-CN" -nb
```

Translate Markdown and images:

```bash
translate -l "pt-BR" -md -img
```

Update existing translations by deleting and recreating them:

```bash
translate -l "ko" -u
```

Run without interactive prompts:

```bash
translate -l "ko ja" -md -y
```

Save logs:

```bash
translate -l "ko" -s
```

### Options

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

If no type flag is provided, `translate` processes Markdown, notebooks, and images. Image translation requires Azure AI Vision configuration.

## evaluate

Evaluate translated Markdown quality for one language.

```bash
evaluate -l "ko"
```

### Common examples

Use a stricter low-confidence threshold:

```bash
evaluate -l "es" -c 0.8
```

Run rule-based checks only:

```bash
evaluate -l "fr" -f
```

Run LLM-based checks only:

```bash
evaluate -l "ja" -D
```

### Options

| Option | Required | Description |
| --- | --- | --- |
| `-l`, `--language-code` | Yes | Single language code to evaluate. Alias codes are normalized. |
| `-r`, `--root-dir` | No | Project root. Defaults to the current directory. |
| `-c`, `--min-confidence` | No | Threshold used when listing low-confidence translations. Defaults to `0.7`. |
| `-d`, `--debug` | No | Enable debug logging. |
| `-s`, `--save-logs` | No | Save DEBUG-level logs under `<root-dir>/logs/`. |
| `-f`, `--fast` | No | Rule-based evaluation only. |
| `-D`, `--deep` | No | LLM-based evaluation only. |

By default, `evaluate` uses both rule-based and LLM-based evaluation. Results are written into translation metadata and summarized in the console.

## co-op-review

Run deterministic translation maintenance checks without API credentials.

```bash
co-op-review -l "ko"
```

### Common examples

Review Korean and Japanese translations from the current directory:

```bash
co-op-review -l "ko ja"
```

Review a specific project root:

```bash
co-op-review -l "fr" -r ./my-course
```

Review only source files changed against a base ref:

```bash
co-op-review -l "ko" --changed-from origin/main
```

Print GitHub-flavored Markdown output for CI summaries:

```bash
co-op-review -l "ko ja" --changed-from origin/main --format github
```

### Options

| Option | Required | Description |
| --- | --- | --- |
| `-l`, `--language-code` | No | Language code to review. Can be passed multiple times or as a space-separated value. Defaults to all discovered translation languages. |
| `-r`, `--root-dir` | No | Project root. Defaults to the current directory. |
| `--changed-from` | No | Git ref used to limit review to changed source files. |
| `--format` | No | Output format: `text` or `github`. Defaults to `text`. |

`co-op-review` currently checks for missing translated files, missing or stale translation metadata, Markdown frontmatter and code fence integrity, invalid translated notebook JSON, and missing local Markdown or image link targets. Missing links are warnings by default; structural and freshness problems fail the command.

## migrate-links

Reprocess translated Markdown files and update notebook links so they point to translated notebooks when available.

```bash
migrate-links -l "ko ja"
```

### Common examples

Preview link updates:

```bash
migrate-links -l "ko" --dry-run
```

Process all supported languages without confirmation:

```bash
migrate-links -l "all" -y
```

Only rewrite links when translated notebooks exist:

```bash
migrate-links -l "ko" --no-fallback-to-original
```

### Options

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

## Environment

All commands require one configured LLM provider:

```bash
# Azure OpenAI
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"

# Or OpenAI
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

Image translation additionally requires Azure AI Vision:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

## Output layout

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
