# CLI Reference

Co-op Translator installerer disse kommandolinjeindgangspunkter:

- `translate`
- `evaluate`
- `migrate-links`
- `co-op-review`
- `co-op-translator-mcp`

The `translate`, `evaluate`, `migrate-links`, and `co-op-review` commands dispatch through `co_op_translator.__main__`, which selects the command implementation based on the invoked script name. The MCP server uses `co_op_translator.mcp.server` directly.

If you are deciding between CLI, Python API, and MCP, start with [Choose Your Workflow](workflows.md).

## First-Time CLI Flow

Start her, hvis du bruger Co-op Translator fra en terminal:

1. Configure an LLM provider as described in [Configuration](configuration.md).
2. Choose the content type you want to translate.
3. Run a focused command first, such as Markdown-only translation.
4. Use `--dry-run` before large repository changes.
5. Use `co-op-review` after translation to check structure and freshness.

| Mål | Kommando til at starte med |
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

### Indstillinger

| Option | Påkrævet | Beskrivelse |
| --- | --- | --- |
| `-l`, `--language-codes` | Ja | Space-separated language codes, such as `"es fr de"`, or `"all"`. |
| `-r`, `--root-dir` | Nej | Project root. Defaults to the current directory. |
| `-u`, `--update` | Nej | Delete existing translations for selected languages and recreate them. |
| `-img`, `--images` | Nej | Translate only image files. |
| `-md`, `--markdown` | Nej | Translate only Markdown files. |
| `-nb`, `--notebook` | Nej | Translate only Jupyter notebook files. |
| `-d`, `--debug` | Nej | Enable debug logging in the console. |
| `-s`, `--save-logs` | Nej | Save DEBUG-level logs under `<root-dir>/logs/`. |
| `-x`, `--fix` | Nej | Retranslate low-confidence Markdown files based on previous evaluation results. |
| `-c`, `--min-confidence` | Nej | Confidence threshold for `--fix`. Defaults to `0.7`. |
| `--add-disclaimer`, `--no-disclaimer` | Nej | Add or suppress machine translation disclaimers. Defaults to enabled in the CLI. |
| `-f`, `--fast` | Nej | Deprecated fast image mode. |
| `-y`, `--yes` | Nej | Auto-confirm prompts, useful in CI. |
| `--repo-url` | Nej | Repository URL used in the README languages table sparse-checkout advisory. |
| `--migrate-language-folders` | Nej | Rename legacy alias folders, such as `cn` or `tw`, to canonical BCP 47 folders. |
| `--dry-run` | Nej | Preview language folder migration and translation estimates without writing files. |

If no type flag is provided, `translate` processes Markdown, notebooks, and images. Image translation requires Azure AI Vision configuration.

## evaluate

Evaluate translated Markdown quality for one language.

!!! warning "Eksperimentel"
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

### Indstillinger

| Option | Påkrævet | Beskrivelse |
| --- | --- | --- |
| `-l`, `--language-code` | Ja | Single language code to evaluate. Alias codes are normalized. |
| `-r`, `--root-dir` | Nej | Project root. Defaults to the current directory. |
| `-c`, `--min-confidence` | Nej | Threshold used when listing low-confidence translations. Defaults to `0.7`. |
| `-d`, `--debug` | Nej | Enable debug logging. |
| `-s`, `--save-logs` | Nej | Save DEBUG-level logs under `<root-dir>/logs/`. |
| `-f`, `--fast` | Nej | Rule-based evaluation only. |
| `-D`, `--deep` | Nej | LLM-based evaluation only. |

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

Review only source files changed against a base ref:

```bash
co-op-review -l "ko" --changed-from origin/main
```

Print GitHub-flavored Markdown output for CI summaries:

```bash
co-op-review -l "ko ja" --changed-from origin/main --format github
```

### Indstillinger

| Option | Påkrævet | Beskrivelse |
| --- | --- | --- |
| `-l`, `--language-code` | Nej | Language code to review. Can be passed multiple times or as a space-separated value. Defaults to all discovered translation languages. |
| `-r`, `--root-dir` | Nej | Project root. Defaults to the current directory. |
| `--changed-from` | Nej | Git ref used to limit review to changed source files. |
| `--format` | Nej | Output format: `text` or `github`. Defaults to `text`. |

`co-op-review` currently checks for missing translated files, missing or stale translation metadata, Markdown frontmatter and code fence integrity, invalid translated notebook JSON, and missing local Markdown or image link targets. Missing links are warnings by default; structural and freshness problems fail the command.

## co-op-translator-mcp

Run the Co-op Translator MCP server for agents, editors, and MCP-compatible clients.

```bash
co-op-translator-mcp
```

The default transport is `stdio`. See the [MCP Server](mcp.md) guide for client configuration, tools, resources, and safety notes.

### Indstillinger

| Option | Påkrævet | Beskrivelse |
| --- | --- | --- |
| `--transport` | Nej | MCP transport: `stdio`, `streamable-http`, or `sse`. Defaults to `stdio`. |

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

### Indstillinger

| Option | Påkrævet | Beskrivelse |
| --- | --- | --- |
| `-l`, `--language-codes` | Ja | Space-separated language codes, or `"all"`. |
| `-r`, `--root-dir` | Nej | Project root. Defaults to the current directory. |
| `--image-dir` | Nej | Translated image directory relative to the root. Defaults to `translated_images`. |
| `--dry-run` | Nej | Show files that would change without writing updates. |
| `--fallback-to-original`, `--no-fallback-to-original` | Nej | Use original notebook links when translated notebooks are missing. Enabled by default. |
| `-d`, `--debug` | Nej | Enable debug logging. |
| `-s`, `--save-logs` | Nej | Save DEBUG-level logs under `<root-dir>/logs/`. |
| `-y`, `--yes` | Nej | Auto-confirm prompts when processing all languages. |

## Environment

All commands require one configured LLM provider:

```bash
# Azure OpenAI
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"

# Eller OpenAI
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