# CLI Reference

Co-op Translator dey install dis command-line entry points:

- `translate`
- `evaluate`
- `migrate-links`
- `co-op-review`
- `co-op-translator-mcp`

Di `translate`, `evaluate`, `migrate-links`, an `co-op-review` commands dey dispatch through `co_op_translator.__main__`, wey dey select di command implementation based on di script name wey you run. Di MCP server dey use `co_op_translator.mcp.server` directly.

If you dey decide between CLI, Python API, an MCP, start wit [Choose Your Workflow](workflows.md).

## First-Time CLI Flow

Start for here if na terminal you dey use Co-op Translator:

1. Configure one LLM provider like e dey explain for [Configuration](configuration.md).
2. Choose di content type wey you wan translate.
3. Run one focused command first, like Markdown-only translation.
4. Use `--dry-run` before you do big changes for repository.
5. Use `co-op-review` after translation to check structure an if tins still fresh.

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

Translate Markdown files, notebooks, an image text go one or more target languages.

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

Update existing translations by deleting an recreating dem:

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
| `-l`, `--language-codes` | Yes | Space-separated language codes, like `"es fr de"`, or `"all"`. |
| `-r`, `--root-dir` | No | Project root. If you no provide, e go use di current directory. |
| `-u`, `--update` | No | Delete existing translations for di selected languages an recreate dem. |
| `-img`, `--images` | No | Translate only image files. |
| `-md`, `--markdown` | No | Translate only Markdown files. |
| `-nb`, `--notebook` | No | Translate only Jupyter notebook files. |
| `-d`, `--debug` | No | Enable debug logging for di console. |
| `-s`, `--save-logs` | No | Save DEBUG-level logs under `<root-dir>/logs/`. |
| `-x`, `--fix` | No | Retranslate low-confidence Markdown files based on previous evaluation results. |
| `-c`, `--min-confidence` | No | Confidence threshold for `--fix`. Defaults to `0.7`. |
| `--add-disclaimer`, `--no-disclaimer` | No | Add or suppress machine translation disclaimers. Defaults to enabled in di CLI. |
| `-f`, `--fast` | No | Deprecated fast image mode. |
| `-y`, `--yes` | No | Auto-confirm prompts, useful for CI. |
| `--repo-url` | No | Repository URL wey dem go use for di README languages table sparse-checkout advisory. |
| `--migrate-language-folders` | No | Rename legacy alias folders, like `cn` or `tw`, to canonical BCP 47 folders. |
| `--dry-run` | No | Preview language folder migration an translation estimates without writing files. |

If you no provide any type flag, `translate` go process Markdown, notebooks, an images. Image translation need Azure AI Vision configuration.

## evaluate

Evaluate translated Markdown quality for one language.

!!! warning "Na experimental"
    `evaluate` na experimental feature. E fit use rule-based an LLM-based quality checks, e go write evaluation results into translation metadata, an di scoring model an metadata behavior fit change.

```bash
evaluate -l "ko"
```

### Common examples

Use more strict low-confidence threshold:

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
| `-l`, `--language-code` | Yes | Single language code wey you wan evaluate. Alias codes go normalize. |
| `-r`, `--root-dir` | No | Project root. If you no provide, e go use di current directory. |
| `-c`, `--min-confidence` | No | Threshold wey dem go use when dem list low-confidence translations. Defaults to `0.7`. |
| `-d`, `--debug` | No | Enable debug logging. |
| `-s`, `--save-logs` | No | Save DEBUG-level logs under `<root-dir>/logs/`. |
| `-f`, `--fast` | No | Rule-based evaluation only. |
| `-D`, `--deep` | No | LLM-based evaluation only. |

By default, `evaluate` go use both rule-based an LLM-based evaluation. Results go enter translation metadata an dem go show summary for di console.

## co-op-review

Run deterministic translation maintenance checks without API credentials.

!!! note "Beta"
    `co-op-review` na beta deterministic review command. E no dey call model providers or write files, but di checks an di issue output schema fit change.

```bash
co-op-review -l "ko"
```

### Common examples

Review Korean an Japanese translations from di current directory:

```bash
co-op-review -l "ko ja"
```

Review one specific project root:

```bash
co-op-review -l "fr" -r ./my-course
```

Review only source files wey change against one base ref:

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
| `-l`, `--language-code` | No | Language code to review. You fit pass am multiple times or as space-separated value. Defaults to all discovered translation languages. |
| `-r`, `--root-dir` | No | Project root. If you no provide, e go use di current directory. |
| `--changed-from` | No | Git ref wey dem go use to limit review to changed source files. |
| `--format` | No | Output format: `text` or `github`. Defaults to `text`. |

`co-op-review` dey check missing translated files, missing or stale translation metadata, Markdown frontmatter an code fence integrity, invalid translated notebook JSON, an missing local Markdown or image link targets. Missing links be warnings by default; structural an freshness problems go make di command fail.

## co-op-translator-mcp

Run di Co-op Translator MCP server for agents, editors, an MCP-compatible clients.

```bash
co-op-translator-mcp
```

Di default transport na `stdio`. See di [MCP Server](mcp.md) guide for client configuration, tools, resources, an safety notes.

### Options

| Option | Required | Description |
| --- | --- | --- |
| `--transport` | No | MCP transport: `stdio`, `streamable-http`, or `sse`. Defaults to `stdio`. |

## migrate-links

Reprocess translated Markdown files an update notebook links so dem go point to translated notebooks when dem dey available.

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

Only rewrite links when translated notebooks dey:

```bash
migrate-links -l "ko" --no-fallback-to-original
```

### Options

| Option | Required | Description |
| --- | --- | --- |
| `-l`, `--language-codes` | Yes | Space-separated language codes, or `"all"`. |
| `-r`, `--root-dir` | No | Project root. If you no provide, e go use di current directory. |
| `--image-dir` | No | Translated image directory relative to di root. Defaults to `translated_images`. |
| `--dry-run` | No | Show files wey for change without writing updates. |
| `--fallback-to-original`, `--no-fallback-to-original` | No | Use original notebook links when translated notebooks dey missing. Enabled by default. |
| `-d`, `--debug` | No | Enable debug logging. |
| `-s`, `--save-logs` | No | Save DEBUG-level logs under `<root-dir>/logs/`. |
| `-y`, `--yes` | No | Auto-confirm prompts when dem process all languages. |

## Environment

All commands need one configured LLM provider:

```bash
# Azure OpenAI
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"

# Abi OpenAI
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

Image translation plus still require Azure AI Vision:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

## Output layout

Text translations dem go write under:

```text
translations/<language-code>/<original-path>
```

Translated image output dem go write under:

```text
translated_images/<language-code>/<original-path>
```

For example, if you translate `README.md` an `docs/setup.md` go Korean e go produce:

```text
translations/ko/README.md
translations/ko/docs/setup.md
```

## Copy-Paste CLI Examples

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