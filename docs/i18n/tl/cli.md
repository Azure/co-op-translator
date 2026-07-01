# CLI Reference

I-install ng Co-op Translator ang mga sumusunod na command-line entry point:

- `translate`
- `evaluate`
- `migrate-links`
- `co-op-review`
- `co-op-translator-mcp`

Ang `translate`, `evaluate`, `migrate-links`, at `co-op-review` na mga command ay ipinapasa sa pamamagitan ng `co_op_translator.__main__`, na pumipili ng implementasyon ng command batay sa pangalan ng script na tinawag. Direktang ginagamit ng MCP server ang `co_op_translator.mcp.server`.

Kung nag-aalangan ka sa pagitan ng CLI, Python API, at MCP, magsimula sa [Piliin ang Iyong Daloy ng Trabaho](workflows.md).

## First-Time CLI Flow

Magsimula dito kung gumagamit ka ng Co-op Translator mula sa terminal:

1. I-configure ang isang LLM provider tulad ng nakasaad sa [Konfigurasiyon](configuration.md).
2. Piliin ang uri ng nilalaman na nais mong isalin.
3. Patakbuhin muna ang isang nakatuon na command, tulad ng pagsasalin na Markdown lamang.
4. Gumamit ng `--dry-run` bago gumawa ng malalaking pagbabago sa repositoryo.
5. Gumamit ng `co-op-review` pagkatapos ng pagsasalin upang suriin ang istruktura at pagiging sariwa.

| Goal | Command to start with |
| --- | --- |
| Translate Markdown documents | `translate -l "ko" -md` |
| Translate notebooks | `translate -l "ko" -nb` |
| Translate image text | `translate -l "ko" -img` |
| Preview work without writing files | `translate -l "ko" -md --dry-run` |
| Review existing translations | `co-op-review -l "ko"` |
| Update notebook and Markdown links | `migrate-links -l "ko" --dry-run` |
| Expose tools to an MCP client | I-configure ang [MCP Server](mcp.md) sa halip na direktang pagpapatakbo ng mga CLI command. |

## translate

Isalin ang mga Markdown file, notebook, at teksto ng imahe sa isa o higit pang target na wika.

```bash
translate -l "ko ja fr"
```

### Karaniwang mga halimbawa

Isalin lamang ang Markdown:

```bash
translate -l "de" -md
```

Isalin lamang ang mga notebook:

```bash
translate -l "zh-CN" -nb
```

Isalin ang Markdown at mga imahe:

```bash
translate -l "pt-BR" -md -img
```

I-update ang umiiral na mga pagsasalin sa pamamagitan ng pagtanggal at muling paglikha ng mga ito:

```bash
translate -l "ko" -u
```

Patakbuhin nang walang interactive na mga prompt:

```bash
translate -l "ko ja" -md -y
```

I-save ang mga log:

```bash
translate -l "ko" -s
```

### Mga Opsyon

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

Kung walang type flag na ibinigay, pinoproseso ng `translate` ang Markdown, notebook, at mga imahe. Kinakailangan ang pag-configure ng Azure AI Vision para sa pagsasalin ng imahe.

## evaluate

Suriin ang kalidad ng isinaling Markdown para sa isang wika.

!!! warning "Eksperimental"
    Eksperimental ang `evaluate`. Maaari itong gumamit ng rule-based at LLM-based na mga pagsusuri ng kalidad, sinusulat ang mga resulta ng ebalwasyon sa translation metadata, at maaaring magbago ang modelo ng pagscore at pag-uugali ng metadata.

```bash
evaluate -l "ko"
```

### Karaniwang mga halimbawa

Gumamit ng mas mahigpit na low-confidence threshold:

```bash
evaluate -l "es" -c 0.8
```

Patakbuhin ang rule-based checks lamang:

```bash
evaluate -l "fr" -f
```

Patakbuhin ang LLM-based checks lamang:

```bash
evaluate -l "ja" -D
```

### Mga Opsyon

| Option | Required | Description |
| --- | --- | --- |
| `-l`, `--language-code` | Yes | Single language code to evaluate. Alias codes are normalized. |
| `-r`, `--root-dir` | No | Project root. Defaults to the current directory. |
| `-c`, `--min-confidence` | No | Threshold used when listing low-confidence translations. Defaults to `0.7`. |
| `-d`, `--debug` | No | Enable debug logging. |
| `-s`, `--save-logs` | No | Save DEBUG-level logs under `<root-dir>/logs/`. |
| `-f`, `--fast` | No | Rule-based evaluation only. |
| `-D`, `--deep` | No | LLM-based evaluation only. |

Sa default, gumagamit ang `evaluate` ng parehong rule-based at LLM-based na ebalwasyon. Isinusulat ang mga resulta sa translation metadata at pinapaikli sa console.

## co-op-review

Patakbuhin ang deterministic na mga check sa pagpapanatili ng pagsasalin nang walang mga kredensyal ng API.

!!! note "Beta"
    Ang `co-op-review` ay isang beta na deterministic review command. Hindi ito tumatawag sa mga model provider o sumusulat ng mga file, ngunit maaaring magbago ang mga check at schema ng output ng isyu nito.

```bash
co-op-review -l "ko"
```

### Karaniwang mga halimbawa

Suriin ang mga pagsasalin sa Korean at Japanese mula sa kasalukuyang direktoryo:

```bash
co-op-review -l "ko ja"
```

Suriin ang isang partikular na project root:

```bash
co-op-review -l "fr" -r ./my-course
```

Suriin lamang ang source files na binago laban sa isang base ref:

```bash
co-op-review -l "ko" --changed-from origin/main
```

I-print ang GitHub-flavored Markdown output para sa mga buod ng CI:

```bash
co-op-review -l "ko ja" --changed-from origin/main --format github
```

### Mga Opsyon

| Option | Required | Description |
| --- | --- | --- |
| `-l`, `--language-code` | No | Language code to review. Can be passed multiple times or as a space-separated value. Defaults to all discovered translation languages. |
| `-r`, `--root-dir` | No | Project root. Defaults to the current directory. |
| `--changed-from` | No | Git ref used to limit review to changed source files. |
| `--format` | No | Output format: `text` or `github`. Defaults to `text`. |

Sinusuri ng `co-op-review` sa kasalukuyan ang nawawalang mga isinaling file, nawawala o stale na translation metadata, integridad ng Markdown frontmatter at code fence, invalid na translated notebook JSON, at nawawalang lokal na Markdown o image link targets. Ang nawawalang mga link ay mga babala bilang default; ang mga suliranin sa istruktura at pagiging sariwa ay nagpapabigo sa command.

## co-op-translator-mcp

Patakbuhin ang Co-op Translator MCP server para sa mga agent, editor, at MCP-compatible na mga kliyente.

```bash
co-op-translator-mcp
```

Ang default na transport ay `stdio`. Tingnan ang gabay na [MCP Server](mcp.md) para sa configuration ng kliyente, mga tool, resources, at mga paalala sa kaligtasan.

### Mga Opsyon

| Option | Required | Description |
| --- | --- | --- |
| `--transport` | No | MCP transport: `stdio`, `streamable-http`, or `sse`. Defaults to `stdio`. |

## migrate-links

Muling iproseso ang mga isinaling Markdown file at i-update ang mga link ng notebook upang ituro sa mga isinaling notebook kapag magagamit.

```bash
migrate-links -l "ko ja"
```

### Karaniwang mga halimbawa

I-preview ang mga pag-update ng link:

```bash
migrate-links -l "ko" --dry-run
```

Iproseso ang lahat ng suportadong wika nang walang kumpirmasyon:

```bash
migrate-links -l "all" -y
```

Isulat lamang muli ang mga link kapag umiiral ang mga isinaling notebook:

```bash
migrate-links -l "ko" --no-fallback-to-original
```

### Mga Opsyon

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

Lahat ng command ay nangangailangan ng isang naka-configure na LLM provider:

```bash
# Azure OpenAI
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"

# O OpenAI
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

Kailangan din ng image translation ang Azure AI Vision:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

## Output layout

Isinusulat ang mga text translation sa ilalim ng:

```text
translations/<language-code>/<original-path>
```

Isinusulat ang isinaling image output sa ilalim ng:

```text
translated_images/<language-code>/<original-path>
```

Halimbawa, ang pagsasalin ng `README.md` at `docs/setup.md` sa Korean ay nagbubunga ng:

```text
translations/ko/README.md
translations/ko/docs/setup.md
```

## Mga Halimbawa (Copy-Paste) ng CLI

Isalin ang Markdown sa tatlong wika:

```bash
translate -l "ko ja fr" -md
```

Isalin lamang ang mga notebook:

```bash
translate -l "zh-CN" -nb
```

Isalin lamang ang mga imahe:

```bash
translate -l "pt-BR" -img
```

I-preview ang pagsasalin ng Markdown nang hindi nagsusulat ng mga file:

```bash
translate -l "de es" -md --dry-run
```

Ayusin ang mga low-confidence na pagsasalin ng Markdown:

```bash
evaluate -l "ko" -c 0.8
translate -l "ko" --fix -c 0.8 -md
```

Patakbuhin ang CI-friendly na pagsasalin ng Markdown:

```bash
translate -l "ko ja" -md -y -s
```

Suriin ang naisalining output:

```bash
co-op-review -l "ko ja"
```

I-preview ang migration ng link:

```bash
migrate-links -l "ko" --dry-run
```