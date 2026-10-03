# CLI Referens

Co-op Translator dey install dis command-line entry points:

- `translate`
- `evaluate`
- `migrate-links`
- `co-op-review`
- `co-op-translator-mcp`

The `translate`, `evaluate`, `migrate-links`, and `co-op-review` commands dem dey dispatch through `co_op_translator.__main__`, wey dey pick di command implementation based on di script name wey you call. Di MCP server dey use `co_op_translator.mcp.server` directly.

If you dey decide between CLI, Python API, and MCP, start wit [Choose Your Workflow](workflows.md).

## Console Output

Interactive terminals dey use Rich formatting for di command header, progress, and summaries. CI and non-interactive output go automatically fall back to plain text.

Set `CO_OP_TRANSLATOR_OUTPUT_STYLE=plain` make e force plain output, or `CO_OP_TRANSLATOR_OUTPUT_STYLE=rich` make e force Rich output. Set `CO_OP_TRANSLATOR_NO_PROGRESS=1` make summaries remain but suppress live progress bars.

Use `translate --json-events progress.ndjson` when another system need machine-readable progress. Di CLI still dey render human-facing output, while di NDJSON file go receive versioned `co-op.translation.event.v1` events wey get stable fields like `type`, `stage_key`, `completed`, `total`, and `current_path`.





## First-Time CLI Flow

Start here if you dey use Co-op Translator from terminal:

1. Configure an LLM provider like e explain for [Configuration](configuration.md).
2. Choose di kind content wey you wan translate.
3. Run one focused command first, for example Markdown-only translation.
4. Use `--dry-run` before you make big changes for repository.
5. Use `co-op-review` after translation make you check structure and freshness.

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

Write structured progress events:

```bash
translate -l "ko ja" -md --json-events progress.ndjson
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
| `--json-events` | No | Write machine-readable translation progress events as NDJSON. |
| `-x`, `--fix` | No | Retranslate low-confidence Markdown files based on previous evaluation results. |
| `-c`, `--min-confidence` | No | Confidence threshold for `--fix`. Defaults to `0.7`. |
| `--add-disclaimer`, `--no-disclaimer` | No | Add or suppress machine translation disclaimers. Defaults to enabled in the CLI. |
| `-f`, `--fast` | No | Deprecated fast image mode. |
| `-y`, `--yes` | No | Auto-confirm prompts, useful in CI. |
| `--repo-url` | No | Repository URL used in the README languages table sparse-checkout advisory. |
| `--migrate-language-folders` | No | Rename legacy alias folders, such as `cn` or `tw`, to canonical BCP 47 folders. |
| `--dry-run` | No | Preview language folder migration and translation estimates without writing files. |

If no type flag dey provided, `translate` go process Markdown, notebooks, and images. Image translation need Azure AI Vision configuration.

## evaluate

Evaluate translated Markdown quality for one language.

!!! warning "Experimental"
    `evaluate` na experimental. E fit use rule-based and LLM-based quality checks, e dey write evaluation results into translation metadata, and e scoring model and metadata behavior fit change.

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
| `-c`, `--min-confidence` | No | Threshold wey dem use when dem list low-confidence translations. Defaults to `0.7`. |
| `-d`, `--debug` | No | Enable debug logging. |
| `-s`, `--save-logs` | No | Save DEBUG-level logs under `<root-dir>/logs/`. |
| `-f`, `--fast` | No | Rule-based evaluation only. |
| `-D`, `--deep` | No | LLM-based evaluation only. |

By default, `evaluate` dey use both rule-based and LLM-based evaluation. Results dey write into translation metadata and dem go show summary for di console.

## co-op-review

Run deterministic translation maintenance checks without API credentials.

!!! note "Beta"
    `co-op-review` na beta deterministic review command. E no dey call model providers or write files, but di checks and issue output schema fit change.

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

Review just the README after a README-only translation:

```bash
translate -l "ko" --readme-only -y
co-op-review -l "ko" --readme-only --format github
```

`--readme-only` go ignore other documents and nested READMEs. E go fail if di root `README.md` dey missing. Combined wit `--changed-from`, e go review di README only when dat source file change. README-only translation dey leave di source README unchanged, including any shared-section markers.




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
| `-l`, `--language-code` | No | Language code to review. Fit pass am multiple times or as space-separated value. Defaults to all discovered translation languages. |
| `-r`, `--root-dir` | No | Project root. Defaults to the current directory. |
| `--changed-from` | No | Git ref wey dem use to limit review to source files wey don change. |
| `--readme-only` | No | Review only di root `README.md` translation. |
| `--format` | No | Output format: `text` or `github`. Defaults to `text`. |

`co-op-review` right now dey check for missing translated files, missing or stale translation metadata, Markdown frontmatter and code fence integrity, invalid translated notebook JSON, and missing local Markdown or image link targets. Missing links be warnings by default; structural and freshness problems go make di command fail.

## co-op-translator-mcp

Run the Co-op Translator MCP server for agents, editors, and MCP-compatible clients.

```bash
co-op-translator-mcp
```

The default transport na `stdio`. See di [MCP Server](mcp.md) guide for client configuration, tools, resources, and safety notes.

### Options

| Option | Required | Description |
| --- | --- | --- |
| `--transport` | No | MCP transport: `stdio`, `streamable-http`, or `sse`. Defaults to `stdio`. |

## migrate-links

Reprocess translated Markdown files and update notebook links so dem go point to translated notebooks when dem dey available.

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
| `--dry-run` | No | Show files wey for change without writing updates. |
| `--fallback-to-original`, `--no-fallback-to-original` | No | Use original notebook links when translated notebooks dey missing. Enabled by default. |
| `-d`, `--debug` | No | Enable debug logging. |
| `-s`, `--save-logs` | No | Save DEBUG-level logs under `<root-dir>/logs/`. |
| `-y`, `--yes` | No | Auto-confirm prompts when processing all languages. |

## Environment

When one command need provider credentials, configure one of these provider sets. `translate --dry-run` and `co-op-review` no need provider credentials:

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

# Abi Anthropic
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

Image translation still need Azure AI Vision:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

## Output layout

Text translations dem dey write under:

```text
translations/<language-code>/<original-path>
```

Translated image output dem dey write under:

```text
translated_images/<language-code>/<original-path>
```

For example, translating `README.md` and `docs/setup.md` into Korean go produce:

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