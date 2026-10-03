# CLI Reference

Co-op Translator installs these command-line entry points:

- `translate`
- `evaluate`
- `migrate-links`
- `co-op-review`
- `co-op-translator-mcp`

The `translate`, `evaluate`, `migrate-links`, and `co-op-review` commands dispatch through `co_op_translator.__main__`, which selects the command implementation based on the invoked script name. The MCP server uses `co_op_translator.mcp.server` directly.

If you are deciding between CLI, Python API, and MCP, start with [Choose Your Workflow](workflows.md).

## Console Output

Interactive terminals use Rich formatting for the command header, progress, and summaries. CI and non-interactive output automatically fall back to plain text.

Set `CO_OP_TRANSLATOR_OUTPUT_STYLE=plain` to force plain output, or `CO_OP_TRANSLATOR_OUTPUT_STYLE=rich` to force Rich output. Set `CO_OP_TRANSLATOR_NO_PROGRESS=1` to keep summaries while suppressing live progress bars.

Use `translate --json-events progress.ndjson` when another system needs
machine-readable progress. The CLI continues to render human-facing output, while
the NDJSON file receives versioned `co-op.translation.event.v1` events with
stable fields such as `type`, `stage_key`, `completed`, `total`, and
`current_path`.

## First-Time CLI Flow

Start here if you are using Co-op Translator from a terminal:

1. Configure an LLM provider as described in [Configuration](configuration.md).
2. Choose the content type you want to translate.
3. Run a focused command first, such as Markdown-only translation.
4. Use `--dry-run` before large repository changes.
5. Use `co-op-review` after translation to check structure and freshness.

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

Write documentation translations to `docs/i18n/<lang>/`:

```bash
translate --source docs --output docs/i18n -l "ko ja" -md
```

`--source` is an alias for `--root-dir`, and `--output` is an alias for
`--translations-dir`. An output path already under the source, such as
`--source docs --output docs/i18n`, is resolved correctly and automatically
excluded from source discovery. The same path model is used by translation,
review, and link migration. Image output stays under
`<source>/translated_images/`. Without `--output`, text output defaults to
`<source>/translations/`.

Limit discovery and supply project terminology from a UTF-8 context file:

```bash
translate --source docs --output docs/i18n -l "ko" -md \
  --include "guides/**/*.md" --exclude "archive/**" \
  --context-file translation-context.md --non-interactive
```

Context is inserted after Co-op Translator's mandatory Markdown protection
rules, so it cannot disable preservation of code or link destinations.

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

Create a plan before a large run:

```bash
translate --source docs --output docs/i18n -l "ko ja" -md \
  --include "**/*.md" --dry-run --plan-json plan.json
```

During `--dry-run`, `--plan-json` is the only requested output file that is
written. Provider credentials are not required.

### Text concurrency

Use `--concurrency` to process multiple text file/language pairs at once:

```bash
translate -l "ko ja fr" -md -nb --concurrency 4
```

The default is `1`, preserving sequential execution. The value must be a positive
integer. The limit applies within each text stage to new and outdated Markdown
and notebook translations, formatting retries, `--fix`, and README-only languages.
Chunks and notebook cells within a file retain their existing processing order.
Image translation concurrency is unchanged.

Choose a value that fits your provider's request and token quotas; reduce it if
the provider throttles requests. This setting limits active file/language jobs,
not requests per minute. `--dry-run` remains a local estimate and starts no
translation workers.

### Options

| Option | Required | Description |
| --- | --- | --- |
| `-l`, `--language-codes` | Yes | Space-separated language codes, such as `"es fr de"`, or `"all"`. |
| `-r`, `--root-dir`, `--source` | No | Source root. Defaults to the current directory. |
| `--translations-dir`, `--output` | No | Markdown and notebook output directory. Relative paths resolve under the source unless they already include the source prefix; defaults to `translations`. |
| `--include` | No | Include source paths matching this glob. Repeat for multiple patterns. |
| `--exclude` | No | Exclude source paths matching this glob. Repeat for multiple patterns. |
| `--context-file` | No | UTF-8 terminology and style instructions applied after mandatory syntax-preservation rules. |
| `--concurrency` | No | Maximum simultaneous text file/language translations. Positive integer; defaults to `1`. |
| `-u`, `--update` | No | Delete existing translations for selected languages and recreate them. |
| `-img`, `--images` | No | Translate only image files. |
| `-md`, `--markdown` | No | Translate only Markdown files. |
| `-nb`, `--notebook` | No | Translate only Jupyter notebook files. |
| `-d`, `--debug` | No | Enable debug logging in the console. |
| `-s`, `--save-logs` | No | Save DEBUG-level logs under `<root-dir>/logs/`. |
| `--json-events` | No | Write machine-readable translation progress events as NDJSON. |
| `--plan-json` | No | Write a versioned JSON translation plan. This remains enabled during `--dry-run`. |
| `-x`, `--fix` | No | Retranslate low-confidence Markdown files based on previous evaluation results. |
| `-c`, `--min-confidence` | No | Confidence threshold for `--fix`. Defaults to `0.7`. |
| `--add-disclaimer`, `--no-disclaimer` | No | Add or suppress machine translation disclaimers. Defaults to enabled in the CLI. |
| `-f`, `--fast` | No | Deprecated fast image mode. |
| `-y`, `--yes`, `--non-interactive` | No | Auto-confirm prompts, useful in CI and agent runs. |
| `--repo-url` | No | Repository URL used in the README languages table sparse-checkout advisory. |
| `--migrate-language-folders` | No | Rename legacy alias folders, such as `cn` or `tw`, to canonical BCP 47 folders. |
| `--dry-run` | No | Preview language folder migration and translation estimates without writing files. |

If no type flag is provided, `translate` processes Markdown, notebooks, and images. Image translation requires Azure AI Vision configuration.

## evaluate

Evaluate translated Markdown quality for one language.

!!! warning "Experimental"
    `evaluate` is experimental. It can use rule-based and LLM-based quality checks, writes evaluation results into translation metadata, and its scoring model and metadata behavior may change.

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

!!! note "Beta"
    `co-op-review` is a beta deterministic review command. It does not call model providers or write files, but its checks and issue output schema may evolve.

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

`--readme-only` ignores other documents and nested READMEs. It fails if the root
`README.md` is missing. Combined with `--changed-from`, it reviews the README only
when that source file changed. README-only translation leaves the source README
unchanged, including any shared-section markers.

Review only source files changed against a base ref:

```bash
co-op-review -l "ko" --changed-from origin/main
```

Print GitHub-flavored Markdown output for CI summaries:

```bash
co-op-review -l "ko ja" --changed-from origin/main --format github
```

Emit a versioned verification report as JSON:

```bash
co-op-review --source docs --output docs/i18n -l "ko" --format json
```

### Options

| Option | Required | Description |
| --- | --- | --- |
| `-l`, `--language-code` | No | Language code to review. Can be passed multiple times or as a space-separated value. Defaults to all discovered translation languages. |
| `-r`, `--root-dir`, `--source` | No | Source root. Defaults to the current directory. |
| `--translations-dir`, `--output` | No | Translation output directory. Defaults to `translations` under the source. |
| `--include` | No | Include source paths matching this glob. Repeat for multiple patterns. |
| `--exclude` | No | Exclude source paths matching this glob. Repeat for multiple patterns. |
| `--changed-from` | No | Git ref used to limit review to changed source files. |
| `--readme-only` | No | Review only the root `README.md` translation. |
| `--format` | No | Output format: `text`, `github`, or `json`. Defaults to `text`. |

`co-op-review` checks missing or stale translations, Markdown and notebook
structure, protected code literals, local links, missing or duplicated prose
blocks, and suspicious unchanged English prose. Completeness and untranslated
prose checks are deterministic heuristics; they identify suspicious output but
do not prove linguistic quality. Missing links and suspicious prose are warnings
by default; structural, freshness, missing-block, and protected-literal problems
fail the command.

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
| `-r`, `--root-dir`, `--source` | No | Source root. Defaults to the current directory. |
| `--translations-dir`, `--output` | No | Translation output directory. Defaults to `translations` under the source. |
| `--include` | No | Include source paths matching this glob. Repeat for multiple patterns. |
| `--exclude` | No | Exclude source paths matching this glob. Repeat for multiple patterns. |
| `--image-dir` | No | Translated image directory relative to the root. Defaults to `translated_images`. |
| `--dry-run` | No | Show files that would change without writing updates. |
| `--fallback-to-original`, `--no-fallback-to-original` | No | Use original notebook links when translated notebooks are missing. Enabled by default. |
| `-d`, `--debug` | No | Enable debug logging. |
| `-s`, `--save-logs` | No | Save DEBUG-level logs under `<root-dir>/logs/`. |
| `-y`, `--yes`, `--non-interactive` | No | Auto-confirm prompts when processing all languages. |

## Machine-readable schemas

All schema names are versioned. Additive fields may be introduced within a
version; consumers should ignore fields they do not recognize.

- `co-op.translation.plan.v1` contains `source`, `output`, `include`,
  `exclude`, `languages`, `new_files`, `outdated_files`, `current_files`,
  `estimated_words`, `estimated_tokens`, and `api_required`. Each file item
  has `file` and `language`. Multi-root API plans wrap individual plans in
  `plans`.
- `co-op.translation.event.v1` is one JSON object per NDJSON line. Every event
  has `schema`, `type`, `run_id`, and `timestamp`. Depending on `type`, it
  may include `file`, `language`, `block`, `attempt`, stage progress, token
  and word estimates, or final `translated` and `failed` counts. Events never
  include credentials, provider secrets, prompts, or translated document
  contents.
- `co-op.translation.verification.v1` contains the resolved root, source files,
  languages, status, issue counts, verification booleans, and issue records.
  Verification booleans cover source freshness, Markdown structure,
  completeness heuristics, protected literals, and links.

## Exit codes

Automation-facing commands use these process exit codes:

| Code | Meaning |
| ---: | --- |
| `0` | Success. |
| `1` | Validation findings, including a failed verification report. |
| `2` | Partial translation failure after other files completed. |
| `3` | Invalid configuration, paths, or missing required provider setup. |
| `4` | Fatal execution failure. |

Successful unchanged files are skipped using their source hashes, so an
interrupted run resumes at file granularity. Failed files are retried on the
next run. Persisted block-level resume state is not currently available.

Markdown translation protects fenced, indented, and inline code before model
calls. It also protects HTTP(S) URLs, GitHub fragment destinations, Markdown
link and image destinations, and `href`/`src` HTML attributes. Human-readable
labels and prose remain available for translation. Keep environment variable
names, commands, paths, product names, and programming identifiers in code spans
or add explicit preservation rules with `--context-file`.

## Environment

When a command requires provider credentials, configure one of these provider sets. `translate --dry-run` and `co-op-review` do not require provider credentials:

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

# Or Anthropic
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
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
