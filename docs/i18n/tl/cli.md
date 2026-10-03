# Sanggunian ng CLI

Nag-iinstall ang Co-op Translator ng mga sumusunod na entry point para sa command-line:

- `translate`
- `evaluate`
- `migrate-links`
- `co-op-review`
- `co-op-translator-mcp`

Ang mga utos na `translate`, `evaluate`, `migrate-links`, at `co-op-review` ay ipinapasa sa pamamagitan ng `co_op_translator.__main__`, na pinipili ang implementasyon ng utos batay sa pangalan ng script na tinawag. Direktang ginagamit ng MCP server ang `co_op_translator.mcp.server`.

Kung nag-aalinlangan ka sa pagitan ng CLI, Python API, at MCP, magsimula sa [Piliin ang Iyong Workflow](workflows.md).

## Output ng Console

Gumagamit ang mga interactive na terminal ng Rich formatting para sa header ng utos, pag-unlad (progress), at mga buod. Ang output sa CI at hindi-interactive ay awtomatikong bumabalik sa plain text.

Itakda ang `CO_OP_TRANSLATOR_OUTPUT_STYLE=plain` para pilitin ang plain output, o `CO_OP_TRANSLATOR_OUTPUT_STYLE=rich` para pilitin ang Rich output. Itakda ang `CO_OP_TRANSLATOR_NO_PROGRESS=1` upang panatilihin ang mga buod habang sinasawalang-bahala ang mga live progress bar.

Gamitin ang `translate --json-events progress.ndjson` kapag kailangan ng isa pang sistema ng machine-readable progreso. Nagpapatuloy ang CLI sa pag-render ng human-facing output, habang nakatatanggap ang NDJSON file ng versioned `co-op.translation.event.v1` events na may mga stable na field tulad ng `type`, `stage_key`, `completed`, `total`, at `current_path`.





## Daloy para sa Unang Gamit ng CLI

Magsimula rito kung ginagamit mo ang Co-op Translator mula sa terminal:

1. I-configure ang isang LLM provider tulad ng ipinapaliwanag sa [Konfigurasyon](configuration.md).
2. Piliin ang uri ng nilalaman na nais mong isalin.
3. Patakbuhin muna ang isang nakatuong utos, tulad ng pagsasalin ng Markdown lamang.
4. Gamitin ang `--dry-run` bago ang malalaking pagbabago sa repository.
5. Gamitin ang `co-op-review` pagkatapos ng pagsasalin upang suriin ang estruktura at pagiging napapanahon.

| Layunin | Utos para simulan |
| --- | --- |
| Isalin ang mga dokumentong Markdown | `translate -l "ko" -md` |
| Isalin ang mga notebook | `translate -l "ko" -nb` |
| Isalin ang teksto sa imahe | `translate -l "ko" -img` |
| I-preview ang trabaho nang hindi nagsusulat ng mga file | `translate -l "ko" -md --dry-run` |
| Suriin ang umiiral na mga pagsasalin | `co-op-review -l "ko"` |
| I-update ang mga link ng notebook at Markdown | `migrate-links -l "ko" --dry-run` |
| I-expose ang mga tool sa isang MCP client | I-configure ang [MCP Server](mcp.md) sa halip na patakbuhin ang mga utos ng CLI nang direkta. |

## translate

Isalin ang mga Markdown file, notebook, at teksto sa imahe sa isa o higit pang mga target na wika.

```bash
translate -l "ko ja fr"
```

### Mga karaniwang halimbawa

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

I-update ang umiiral na mga pagsasalin sa pamamagitan ng pagtanggal at muling paggawa ng mga ito:

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

Isulat ang istrukturadong mga event ng progreso:

```bash
translate -l "ko ja" -md --json-events progress.ndjson
```

### Mga Opsyon

| Opsyon | Kinakailangan | Paglalarawan |
| --- | --- | --- |
| `-l`, `--language-codes` | Yes | Mga code ng wika na pinaghihiwalay ng espasyo, tulad ng `"es fr de"`, o `"all"`. |
| `-r`, `--root-dir` | No | Project root. Defaults to the current directory. |
| `-u`, `--update` | No | Tanggalin ang umiiral na mga pagsasalin para sa mga piniling wika at muling likhain ang mga ito. |
| `-img`, `--images` | No | Isalin lamang ang mga file ng imahe. |
| `-md`, `--markdown` | No | Isalin lamang ang mga Markdown file. |
| `-nb`, `--notebook` | No | Isalin lamang ang mga Jupyter notebook file. |
| `-d`, `--debug` | No | I-enable ang debug logging sa console. |
| `-s`, `--save-logs` | No | I-save ang DEBUG-level na mga log sa ilalim ng `<root-dir>/logs/`. |
| `--json-events` | No | Isulat ang machine-readable na mga event ng progreso ng pagsasalin bilang NDJSON. |
| `-x`, `--fix` | No | Muling isalin ang mga Markdown file na may mababang kumpiyansa batay sa mga naunang resulta ng ebalwasyon. |
| `-c`, `--min-confidence` | No | Hangganan ng kumpiyansa para sa `--fix`. Defaults to `0.7`. |
| `--add-disclaimer`, `--no-disclaimer` | No | Magdagdag o itanggi ang mga disclaimer para sa machine translation. Defaults to enabled in the CLI. |
| `-f`, `--fast` | No | Deprecated fast image mode. |
| `-y`, `--yes` | No | Awtomatikong kumpirmahin ang mga prompt, kapaki-pakinabang sa CI. |
| `--repo-url` | No | Repository URL na ginagamit sa README languages table sparse-checkout advisory. |
| `--migrate-language-folders` | No | Palitan ang pangalan ng legacy alias folders, tulad ng `cn` o `tw`, sa canonical na mga folder na sumusunod sa BCP 47. |
| `--dry-run` | No | I-preview ang migration ng language folder at mga pagtatantya ng pagsasalin nang hindi nagsusulat ng mga file. |

Kung walang ibinigay na type flag, pinoproseso ng `translate` ang Markdown, notebook, at mga imahe. Nangangailangan ng konfigurasyon ng Azure AI Vision ang pagsasalin ng imahe.

## evaluate

Suriin ang kalidad ng naisaling Markdown para sa isang wika.

!!! warning "Eksperimental"
    `evaluate` ay eksperimental. Maaari itong gumamit ng rule-based at LLM-based na mga quality check, sinusulat ang mga resulta ng ebalwasyon sa metadata ng pagsasalin, at maaaring magbago ang modelo ng pag-score at pag-uugali ng metadata.

```bash
evaluate -l "ko"
```

### Mga karaniwang halimbawa

Gumamit ng mas mahigpit na hangganan para sa mababang kumpiyansa:

```bash
evaluate -l "es" -c 0.8
```

Patakbuhin lamang ang mga rule-based na pagsusuri:

```bash
evaluate -l "fr" -f
```

Patakbuhin lamang ang mga LLM-based na pagsusuri:

```bash
evaluate -l "ja" -D
```

### Mga Opsyon

| Opsyon | Kinakailangan | Paglalarawan |
| --- | --- | --- |
| `-l`, `--language-code` | Yes | Isang code ng wika na susuriin. Ang mga alias na code ay ino-normalize. |
| `-r`, `--root-dir` | No | Project root. Defaults to the current directory. |
| `-c`, `--min-confidence` | No | Hangganan na ginagamit kapag inililista ang mga pagsasaling may mababang kumpiyansa. Defaults to `0.7`. |
| `-d`, `--debug` | No | I-enable ang debug logging. |
| `-s`, `--save-logs` | No | I-save ang DEBUG-level na mga log sa ilalim ng `<root-dir>/logs/`. |
| `-f`, `--fast` | No | Rule-based na pagsusuri lamang. |
| `-D`, `--deep` | No | LLM-based na pagsusuri lamang. |

Sa default, gumagamit ang `evaluate` ng parehong rule-based at LLM-based na pagsusuri. Ang mga resulta ay isinusulat sa metadata ng pagsasalin at ibinubuod sa console.

## co-op-review

Patakbuhin ang deterministic na mga tsek para sa maintenance ng pagsasalin nang walang API credentials.

!!! note "Beta"
    `co-op-review` ay isang beta na deterministic review command. Hindi ito tumatawag ng model providers o nagsusulat ng mga file, ngunit ang mga tsek at schema ng issue output nito ay maaaring magbago.

```bash
co-op-review -l "ko"
```

### Mga karaniwang halimbawa

Suriin ang mga pagsasalin sa Koreano at Hapon mula sa kasalukuyang direktoryo:

```bash
co-op-review -l "ko ja"
```

Suriin ang isang partikular na root ng proyekto:

```bash
co-op-review -l "fr" -r ./my-course
```

Suriin lamang ang README pagkatapos ng pagsasalin na nakatuon lamang sa README:

```bash
translate -l "ko" --readme-only -y
co-op-review -l "ko" --readme-only --format github
```

`--readme-only` ay ipinagwawalang-bahala ang ibang dokumento at mga nested na README. Nabibigo ito kung nawawala ang root
`README.md`. Kapag pinagsama sa `--changed-from`, sinusuri nito ang README lamang
kapag nagbago ang source file na iyon. Ang README-only na pagsasalin ay iniiwan ang pinagmumulang README
hindi binabago, kabilang ang anumang mga marker ng shared-section.

Suriin lamang ang mga source file na nagbago kumpara sa isang base ref:

```bash
co-op-review -l "ko" --changed-from origin/main
```

I-print ang GitHub-flavored Markdown na output para sa mga buod ng CI:

```bash
co-op-review -l "ko ja" --changed-from origin/main --format github
```

### Mga Opsyon

| Opsyon | Kinakailangan | Paglalarawan |
| --- | --- | --- |
| `-l`, `--language-code` | No | Code ng wika na susuriin. Maaaring ipasa nang maramihang beses o bilang isang espasyo-hiwalay na halaga. Default ay lahat ng natuklasang mga wika ng pagsasalin. |
| `-r`, `--root-dir` | No | Project root. Defaults to the current directory. |
| `--changed-from` | No | Git ref na ginagamit para limitahan ang pagsusuri sa mga nagbago na source file. |
| `--readme-only` | No | Suriin lamang ang root `README.md` na pagsasalin. |
| `--format` | No | Output format: `text` or `github`. Defaults to `text`. |

Sa ngayon, sinusuri ng `co-op-review` ang mga nawawalang naisaling file, nawawala o lipas na translation metadata, integridad ng Markdown frontmatter at code fences, invalid na naisaling notebook JSON, at nawawalang lokal na target ng Markdown o image links. Ang mga nawawalang link ay mga babala bilang default; ang mga problema sa estruktura at pagiging napapanahon ay nagpapabigo sa utos.

## co-op-translator-mcp

Patakbuhin ang Co-op Translator MCP server para sa mga agent, editor, at mga kliyenteng MCP-compatible.

```bash
co-op-translator-mcp
```

Ang default transport ay `stdio`. Tingnan ang gabay na [MCP Server](mcp.md) para sa configuration ng kliyente, mga tool, mga mapagkukunan, at mga paunawang pangkaligtasan.

### Mga Opsyon

| Opsyon | Kinakailangan | Paglalarawan |
| --- | --- | --- |
| `--transport` | No | MCP transport: `stdio`, `streamable-http`, or `sse`. Defaults to `stdio`. |

## migrate-links

I-reprocess ang mga naisaling Markdown file at i-update ang mga link ng notebook upang ituro sa mga naisaling notebook kapag magagamit.

```bash
migrate-links -l "ko ja"
```

### Mga karaniwang halimbawa

I-preview ang mga update ng link:

```bash
migrate-links -l "ko" --dry-run
```

Iproseso ang lahat ng sinusuportahang wika nang walang kumpirmasyon:

```bash
migrate-links -l "all" -y
```

Isulat muli ang mga link lamang kapag umiiral ang mga naisaling notebook:

```bash
migrate-links -l "ko" --no-fallback-to-original
```

### Mga Opsyon

| Opsyon | Kinakailangan | Paglalarawan |
| --- | --- | --- |
| `-l`, `--language-codes` | Yes | Mga code ng wika na pinaghihiwalay ng espasyo, o `"all"`. |
| `-r`, `--root-dir` | No | Project root. Defaults to the current directory. |
| `--image-dir` | No | Direktoryo ng naisaling imahe relative sa root. Defaults to `translated_images`. |
| `--dry-run` | No | Ipakita ang mga file na magbabago nang hindi nagsusulat ng mga update. |
| `--fallback-to-original`, `--no-fallback-to-original` | No | Gamitin ang orihinal na mga notebook link kapag nawawala ang naisaling notebook. Naka-enable bilang default. |
| `-d`, `--debug` | No | I-enable ang debug logging. |
| `-s`, `--save-logs` | No | I-save ang DEBUG-level na mga log sa ilalim ng `<root-dir>/logs/`. |
| `-y`, `--yes` | No | Awtomatikong kumpirmahin ang mga prompt kapag pinoproseso ang lahat ng wika. |

## Kapaligiran

Kapag ang isang utos ay nangangailangan ng provider credentials, i-configure ang isa sa mga hanay ng provider na ito. Ang `translate --dry-run` at `co-op-review` ay hindi nangangailangan ng provider credentials:

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

# O Anthropic
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

Karagdagan, nangangailangan ang pagsasalin ng imahe ng Azure AI Vision:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

## Layout ng Output

Isinusulat ang mga tekstong pagsasalin sa:

```text
translations/<language-code>/<original-path>
```

Ang output ng naisaling mga imahe ay isinusulat sa:

```text
translated_images/<language-code>/<original-path>
```

Halimbawa, ang pagsasalin ng `README.md` at `docs/setup.md` sa Koreano ay magreresulta sa:

```text
translations/ko/README.md
translations/ko/docs/setup.md
```

## Mga Halimbawa ng CLI (Copy-Paste)

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

Ayusin ang mga Markdown na pagsasalin na may mababang kumpiyansa:

```bash
evaluate -l "ko" -c 0.8
translate -l "ko" --fix -c 0.8 -md
```

Patakbuhin ang CI-friendly na pagsasalin ng Markdown:

```bash
translate -l "ko ja" -md -y -s
```

Suriin ang naisaling output:

```bash
co-op-review -l "ko ja"
```

I-preview ang migration ng link:

```bash
migrate-links -l "ko" --dry-run
```