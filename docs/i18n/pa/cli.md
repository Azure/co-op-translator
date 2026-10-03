# CLI ਸੰਦਰਭ

Co-op Translator ਇਹ ਹੇਠ ਲਿਖੇ ਕਮਾਂਡ-ਲਾਈਨ ਐਂਟਰੀ ਪੁਆਇੰਟਸ ਸਥਾਪਿਤ ਕਰਦਾ ਹੈ:

- `translate`
- `evaluate`
- `migrate-links`
- `co-op-review`
- `co-op-translator-mcp`

`translate`, `evaluate`, `migrate-links`, ਅਤੇ `co-op-review` ਕਮਾਂਡਾਂ `co_op_translator.__main__` ਰਾਹੀਂ ਡਿਸਪੈਚ ਹੁੰਦੀਆਂ ਹਨ, ਜੋ ਕਿ ਕਾਲ ਕੀਤੇ ਗਏ ਸਕ੍ਰਿਪਟ ਨਾਮ ਦੇ ਆਧਾਰ 'ਤੇ ਕਮਾਂਡ ਇੰਪਲਿਮੇਂਟੇਸ਼ਨ ਨੂੰ ਚੁਣਦਾ ਹੈ। MCP ਸਰਵਰ ਸਿੱਧਾ `co_op_translator.mcp.server` ਵਰਤਦਾ ਹੈ।

ਜੇ ਤੁਸੀਂ CLI, Python API, ਅਤੇ MCP ਵਿਚਕਾਰ ਫੈਸਲਾ ਕਰ ਰਹੇ ਹੋ, ਤਾਂ [ਆਪਣਾ ਵਰਕਫਲੋ ਚੁਣੋ](workflows.md) ਨਾਲ ਸ਼ੁਰੂ ਕਰੋ।

## ਕੰਸੋਲ ਆਉਟਪੁੱਟ

ਇੰਟਰਐਕਟਿਵ ਟਰਮੀਨਲ ਕਮਾਂਡ ਹੈਡਰ, ਪ੍ਰਗਤੀ, ਅਤੇ ਸੰਖੇਪ ਲਈ Rich ਫਾਰਮੈਟਿੰਗ ਵਰਤਦੇ ਹਨ। CI ਅਤੇ ਗੈਰ-ਇੰਟਰਐਕਟਿਵ ਆਉਟਪੁੱਟ ਆਟੋਮੈਟਿਕ ਤੌਰ 'ਤੇ ਸਧਾਰਨ ਪਾਠ (plain text) ਵਲ ਵਾਪਸ ਆ ਜਾਂਦਾ ਹੈ।

ਸਾਦਾ ਆਉਟਪੁੱਟ ਨੂੰ ਫੋਰਸ ਕਰਨ ਲਈ `CO_OP_TRANSLATOR_OUTPUT_STYLE=plain` ਸੈੱਟ ਕਰੋ, ਜਾਂ Rich ਆਉਟਪੁੱਟ ਨੂੰ ਫੋਰਸ ਕਰਨ ਲਈ `CO_OP_TRANSLATOR_OUTPUT_STYLE=rich` ਸੈੱਟ ਕਰੋ। ਲਾਈਵ ਪ੍ਰੋਗਰੈੱਸ ਬਾਰਾਂ ਨੂੰ ਦਬਾਕੇ ਸਾਰਾਂ (summaries) ਰੱਖਣ ਲਈ `CO_OP_TRANSLATOR_NO_PROGRESS=1` ਸੈੱਟ ਕਰੋ।

ਜਦੋਂ ਕਿਸੇ ਹੋਰ ਸਿਸਟਮ ਨੂੰ ਲੋੜ ਹੋਵੇ ਤਾਂ `translate --json-events progress.ndjson` ਵਰਤੋ
ਮਸ਼ੀਨ-ਪੜ੍ਹਨਯੋਗ ਪ੍ਰਗਤੀ। CLI ਮਨੁੱਖ-ਮੁਖੀ ਆਉਟਪੁੱਟ ਨੂੰ ਰੈਂਡਰ ਕਰਨਾ ਜਾਰੀ ਰੱਖਦੀ ਹੈ, ਜਦਕਿ
NDJSON ਫਾਇਲ ਵਰਜਨ ਕੀਤੀਆਂ `co-op.translation.event.v1` ਇਵੈਂਟਾਂ ਪ੍ਰਾਪਤ ਕਰਦੀ ਹੈ ਜਿਨ੍ਹਾਂ ਵਿੱਚ
ਸਥਿਰ ਫੀਲਡਾਂ ਜਿਵੇਂ `type`, `stage_key`, `completed`, `total`, ਅਤੇ
`current_path`.

## ਪਹਿਲੀ ਵਾਰੀ CLI ਫਲੋ

ਇਹਥੋਂ ਸ਼ੁਰੂ ਕਰੋ ਜੇ ਤੁਸੀਂ ਟਰਮੀਨਲ ਤੋਂ Co-op Translator ਵਰਤ ਰਹੇ ਹੋ:

1. ਇੱਕ LLM ਪ੍ਰੋਵਾਈਡਰ ਕਨਫਿਗਰ ਕਰੋ ਜਿਵੇਂ [Configuration](configuration.md) ਵਿੱਚ ਦਰਸਾਇਆ ਗਿਆ ਹੈ।
2. ਉਸ ਸਮੱਗਰੀ ਦੀ ਕਿਸਮ ਚੁਣੋ ਜਿਸ ਦਾ ਤੁਸੀਂ ਅਨੁਵਾਦ ਕਰਨਾ ਚਾਹੁੰਦੇ ਹੋ।
3. ਪਹਿਲਾਂ ਇੱਕ ਧਿਆਨ ਕੇਂਦਰਤ ਕਮਾਂਡ ਚਲਾਓ, ਜਿਵੇਂ ਕਿ ਕੇਵਲ Markdown ਦਾ ਅਨੁਵਾਦ।
4. Use `--dry-run` before large repository changes.
5. ਅਨੁਵਾਦ ਤੋਂ ਬਾਅਦ ਢਾਂਚਾ ਅਤੇ ਤਾਜਗੀ ਦੇ ਜਾਂਚ ਲਈ `co-op-review` ਦੀ ਵਰਤੋਂ ਕਰੋ।

| Goal | Command to start with |
| --- | --- |
| Translate Markdown documents | `translate -l "ko" -md` |
| Translate notebooks | `translate -l "ko" -nb` |
| Translate image text | `translate -l "ko" -img` |
| Preview work without writing files | `translate -l "ko" -md --dry-run` |
| Review existing translations | `co-op-review -l "ko"` |
| Update notebook and Markdown links | `migrate-links -l "ko" --dry-run` |
| MCP client ਨੂੰ ਟੂਲ ਉਪਲਬਧ ਕਰੋ | CLI ਕਮਾਂਡਾਂ ਨੂੰ ਸਿੱਧਾ ਚਲਾਉਣ ਦੀ ਬਜਾਏ [MCP Server](mcp.md) ਨੂੰ ਕਨਫਿਗਰ ਕਰੋ। |

## translate

Markdown ਫਾਈਲਾਂ, ਨੋਟਬੁੱਕ, ਅਤੇ ਚਿੱਤਰ ਟੈਕਸਟ ਨੂੰ ਇੱਕ ਜਾਂ ਵੱਧ ਨਿਸ਼ਾਨਾ ਭਾਸ਼ਾਵਾਂ ਵਿੱਚ ਅਨੁਵਾਦ ਕਰੋ।

```bash
translate -l "ko ja fr"
```

### ਆਮ ਉਦਾਹਰਣ

ਸਿਰਫ Markdown ਅਨੁਵਾਦ ਕਰੋ:

```bash
translate -l "de" -md
```

ਸਿਰਫ ਨੋਟਬੁੱਕ ਅਨੁਵਾਦ ਕਰੋ:

```bash
translate -l "zh-CN" -nb
```

Markdown ਅਤੇ ਚਿੱਤਰ ਦੋਵਾਂ ਦਾ ਅਨੁਵਾਦ ਕਰੋ:

```bash
translate -l "pt-BR" -md -img
```

ਮੌਜੂਦਾ ਅਨੁਵਾਦਾਂ ਨੂੰ ਮਿਟਾ ਕੇ ਮੁੜ ਬਣਾਕੇ ਅਪਡੇਟ ਕਰੋ:

```bash
translate -l "ko" -u
```

ਇੰਟਰਐਕਟਿਵ ਪ੍ਰੋੰਪਟਸ ਤੋਂ ਬਿਨਾਂ ਚਲਾਓ:

```bash
translate -l "ko ja" -md -y
```

ਲੌਗ ਸੇਵ ਕਰੋ:

```bash
translate -l "ko" -s
```

ਸੰਰਚਿਤ ਪ੍ਰਗਤੀ ਇਵੈਂਟ ਲਿਖੋ:

```bash
translate -l "ko ja" -md --json-events progress.ndjson
```

### ਵਿਕਲਪ

| Option | Required | Description |
| --- | --- | --- |
| `-l`, `--language-codes` | ਹਾਂ | ਸਪੇਸ ਨਾਲ ਵੱਖ-ਵੱਖ ਕੀਤੇ ਭਾਸ਼ਾ ਕੋਡ, ਜਿਵੇਂ `"es fr de"`, ਜਾਂ `"all"`. |
| `-r`, `--root-dir` | No | Project root. Defaults to the current directory. |
| `-u`, `--update` | ਨਹੀਂ | ਚੁਣੀਆਂ ਭਾਸ਼ਾਵਾਂ ਲਈ ਮੌਜੂਦਾ ਅਨੁਵਾਦ ਮਿਟਾਓ ਅਤੇ ਉਨ੍ਹਾਂ ਨੂੰ ਮੁੜ ਬਣਾਓ। |
| `-img`, `--images` | No | Translate only image files. |
| `-md`, `--markdown` | No | Translate only Markdown files. |
| `-nb`, `--notebook` | No | Translate only Jupyter notebook files. |
| `-d`, `--debug` | ਨਹੀਂ | ਕੰਸੋਲ ਵਿੱਚ ਡੀਬੱਗ ਲੌਗਿੰਗ ਚਾਲੂ ਕਰੋ. |
| `-s`, `--save-logs` | No | Save DEBUG-level logs under `<root-dir>/logs/`. |
| `--json-events` | ਨਹੀਂ | ਮਸ਼ੀਨ-ਰੀਡੇਬਲ ਅਨੁਵਾਦ ਪ੍ਰਗਤੀ ਘਟਨਾਵਾਂ ਨੂੰ NDJSON ਵਜੋਂ ਲਿਖੋ. |
| `-x`, `--fix` | ਨਹੀਂ | ਪਿਛਲੇ ਮੁਲਾਂਕਣ ਨਤੀਜਿਆਂ ਦੇ ਆਧਾਰ 'ਤੇ ਘੱਟ-ਭਰੋਸੇਯੋਗ Markdown ਫਾਇਲਾਂ ਨੂੰ ਮੁੜ ਅਨੁਵਾਦ ਕਰੋ। |
| `-c`, `--min-confidence` | No | Confidence threshold for `--fix`. Defaults to `0.7`. |
| `--add-disclaimer`, `--no-disclaimer` | ਨਹੀਂ | ਮਸ਼ੀਨੀ ਅਨੁਵਾਦ ਡਿਸਕਲੇਮਰ ਜੋੜੋ ਜਾਂ ਰੱਦ ਕਰੋ. CLI ਵਿੱਚ ਡਿਫਾਲਟ ਰੂਪ ਵਿੱਚ ਚਾਲੂ ਹੁੰਦਾ ਹੈ. |
| `-f`, `--fast` | No | Deprecated fast image mode. |
| `-y`, `--yes` | ਨਹੀਂ | ਪ੍ਰੋੰਪਟਾਂ ਨੂੰ ਆਟੋ-ਕਨਫਰਮ ਕਰੋ, CI ਵਿੱਚ ਲਾਭਦਾਇਕ. |
| `--repo-url` | ਨਹੀਂ | README ਦੀ ਭਾਸ਼ਾਵਾਂ ਟੇਬਲ ਦੇ sparse-checkout ਸਲਾਹਕਾਰ ਵਿੱਚ ਵਰਤੀ ਜਾਣ ਵਾਲੀ ਰਿਪੋਜ਼ਿਟਰੀ URL। |
| `--migrate-language-folders` | ਨਹੀਂ | ਪੁਰਾਣੇ ਐਲਿਆਸ ਫੋਲਡਰਾਂ ਨੂੰ, ਜਿਵੇਂ `cn` ਜਾਂ `tw`, ਮਿਆਰੀ BCP 47 ਫੋਲਡਰਾਂ ਵਿੱਚ ਨਾਂ ਬਦਲੋ. |
| `--dry-run` | ਨਹੀਂ | ਫਾਇਲਾਂ ਲਿਖਣ ਤੋਂ ਬਿਨਾਂ ਭਾਸ਼ਾ ਫੋਲਡਰ ਮਾਈਗ੍ਰੇਸ਼ਨ ਅਤੇ ਅਨੁਵਾਦ ਦੇ ਅੰਦਾਜ਼ਿਆਂ ਦਾ ਪ੍ਰੀਵਿਊ ਦਿਖਾਓ। |

ਜੇ ਕੋਈ type ਫਲੈਗ ਦਿੱਤਾ ਨਹੀਂ ਗਿਆ, ਤਾਂ `translate` Markdown, ਨੋਟਬੁੱਕ ਅਤੇ ਚਿੱਤਰਾਂ ਨੂੰ ਪ੍ਰਕਿਰਿਆ ਕਰਦਾ ਹੈ. ਚਿੱਤਰਾਂ ਦੇ ਅਨੁਵਾਦ ਲਈ Azure AI Vision ਸੰਰਚਨਾ ਦੀ ਲੋੜ ਹੁੰਦੀ ਹੈ.

## evaluate

ਇੱਕ ਭਾਸ਼ਾ ਲਈ ਅਨੁਵਾਦ ਕੀਤੇ Markdown ਦੀ ਗੁਣਵੱਤਾ ਦੀ ਮੁੱਲਾਂਕਣ ਕਰੋ।

!!! warning "ਪ੍ਰਯੋਗਾਤਮਕ"
    `evaluate` ਪ੍ਰਯੋਗਾਤਮਕ ਹੈ। ਇਹ ਨਿਯਮ-ਆਧਾਰਿਤ ਅਤੇ LLM-ਆਧਾਰਿਤ ਮਿਆਰ ਜਾਂਚਾਂ ਵਰਤ ਸਕਦਾ ਹੈ, ਮੁਲਾਂਕਣ ਨਤੀਜੇ ਅਨੁਵਾਦ ਮੈਟਾਡੇਟਾ ਵਿੱਚ ਲਿਖਦਾ ਹੈ, ਅਤੇ ਇਸ ਦਾ ਸਕੋਰਿੰਗ ਮਾਡਲ ਅਤੇ ਮੈਟਾਡੇਟਾ ਵਿਹਾਰ ਬਦਲ ਸਕਦੇ ਹਨ।

```bash
evaluate -l "ko"
```

### ਆਮ ਉਦਾਹਰਣ

ਇੱਕ ਕਠੋਰ ਨੀਵੀਂ-ਭਰੋਸਾ ਸੀਮਾ ਵਰਤੋ:

```bash
evaluate -l "es" -c 0.8
```

ਸਿਰਫ ਨਿਯਮ-ਆਧਾਰਿਤ ਜਾਂਚ ਚਲਾਓ:

```bash
evaluate -l "fr" -f
```

ਸਿਰਫ LLM-ਆਧਾਰਿਤ ਜਾਂਚ ਚਲਾਓ:

```bash
evaluate -l "ja" -D
```

### ਵਿਕਲਪ

| Option | Required | Description |
| --- | --- | --- |
| `-l`, `--language-code` | Yes | Single language code to evaluate. Alias codes are normalized. |
| `-r`, `--root-dir` | No | Project root. Defaults to the current directory. |
| `-c`, `--min-confidence` | ਨਹੀਂ | ਘੱਟ-ਭਰੋਸੇ ਵਾਲੇ ਅਨੁਵਾਦਾਂ ਨੂੰ ਲਿਸਟ ਕਰਦਿਆਂ ਵਰਤਿਆ ਜਾਣ ਵਾਲਾ ਥ੍ਰੇਸ਼ਹੋਲਡ. ਡਿਫਾਲਟ `0.7`. |
| `-d`, `--debug` | No | Enable debug logging. |
| `-s`, `--save-logs` | No | Save DEBUG-level logs under `<root-dir>/logs/`. |
| `-f`, `--fast` | No | Rule-based evaluation only. |
| `-D`, `--deep` | No | LLM-based evaluation only. |

ਮੂਲ ਰੂਪ ਵਿੱਚ, `evaluate` ਨਿਯਮ-ਆਧਾਰਿਤ ਅਤੇ LLM-ਆਧਾਰਿਤ ਮੁਲਾਂਕਣ ਦੋਹਾਂ ਦੀ ਵਰਤੋਂ ਕਰਦਾ ਹੈ। ਨਤੀਜੇ ਅਨੁਵਾਦ ਮੈਟਾ ਡੇਟਾ ਵਿੱਚ ਲਿਖੇ ਜਾਂਦੇ ਹਨ ਅਤੇ ਕੰਸੋਲ ਵਿੱਚ ਸੰਖੇਪ ਕੀਤੇ ਜਾਂਦੇ ਹਨ।

## co-op-review

API ਕ੍ਰੈਡੈਂਸ਼ੀਅਲ ਦੇ ਬਿਨਾਂ ਨਿਰਧਾਰਤ ਤਰਜਮਾ ਰੱਖ-ਰਖਾਵ ਜਾਂਚਾਂ ਚਲਾਓ।

!!! note "ਬੀਟਾ"
    `co-op-review` ਇੱਕ ਬੀਟਾ ਡਿਟਰਮੀਨਿਸਟਿਕ ਸਮੀਖਿਆ ਕਮਾਂਡ ਹੈ। ਇਹ ਮਾਡਲ ਪ੍ਰਦਾਤਾਵਾਂ ਨੂੰ ਕਾਲ ਨਹੀਂ ਕਰਦਾ ਅਤੇ ਫਾਇਲਾਂ ਨਹੀਂ ਲਿਖਦਾ, ਪਰ ਇਸ ਦੀਆਂ ਜਾਂਚਾਂ ਅਤੇ ਮੁਦਿਆਂ ਦੇ ਆਉਟਪੁਟ ਸਕੀਮਾ ਵਿੱਚ ਤਬਦੀਲੀ ਆ ਸਕਦੀ ਹੈ।

```bash
co-op-review -l "ko"
```

### ਆਮ ਉਦਾਹਰਣ

ਮੌਜੂਦਾ ਡਾਇਰੈਕਟਰੀ ਤੋਂ ਕੋਰੀਅਨ ਅਤੇ ਜਪਾਨੀ ਅਨੁਵਾਦ ਸਮੀਖਿਆ ਕਰੋ:

```bash
co-op-review -l "ko ja"
```

ਕਿਸੇ ਵਿਸ਼ੇਸ਼ ਪ੍ਰੋਜੈਕਟ ਰੂਟ ਦੀ ਸਮੀਖਿਆ ਕਰੋ:

```bash
co-op-review -l "fr" -r ./my-course
```

README-only ਅਨੁਵਾਦ ਤੋਂ ਬਾਅਦ ਸਿਰਫ README ਦੀ ਸਮੀਖਿਆ ਕਰੋ:

```bash
translate -l "ko" --readme-only -y
co-op-review -l "ko" --readme-only --format github
```

`--readme-only` ਹੋਰ ਦਸਤਾਵੇਜ਼ਾਂ ਅਤੇ ਨੇਸਟਿਡ READMEs ਨੂੰ ਨਜ਼ਰਅੰਦਾਜ਼ ਕਰਦਾ ਹੈ। ਇਹ ਫੇਲ ਹੁੰਦਾ ਹੈ ਜੇ ਰੂਟ
`README.md` ਮੌਜੂਦ ਨਹੀਂ ਹੈ।
`--changed-from` ਨਾਲ, ਇਹ ਸਿਰਫ README ਦੀ ਸਮੀਖਿਆ ਕਰਦਾ ਹੈ
ਸੋਰਸ README ਬਿਨਾਂ ਬਦਲਾਅ ਦੇ ਰਹਿੰਦਾ ਹੈ, ਜਿਸ ਵਿੱਚ ਕਿਸੇ ਵੀ ਸਾਂਝੇ-ਸੈਕਸ਼ਨ ਮਾਰਕਰ ਸ਼ਾਮਲ ਹਨ।

ਸਿਰਫ ਉਹ ਸੋਰਸ ਫਾਈਲਾਂ ਸਮੀਖਿਆ ਕਰੋ ਜੋ ਕਿਸੇ ਬੇਸ ref ਦੇ ਖਿਲਾਫ਼ ਬਦਲੀ ਗਈਆਂ ਹਨ:

```bash
co-op-review -l "ko" --changed-from origin/main
```

CI ਸੰਖੇਪ ਲਈ GitHub-ਫਲੇਵਰਡ Markdown ਨਤੀਜੇ ਪ੍ਰਿੰਟ ਕਰੋ:

```bash
co-op-review -l "ko ja" --changed-from origin/main --format github
```

### ਵਿਕਲਪ

| Option | Required | Description |
| --- | --- | --- |
| `-l`, `--language-code` | No | ਸਮੀਖਿਆ ਲਈ ਭਾਸ਼ਾ ਕੋਡ। ਇਹ ਇੱਕ ਤੋਂ ਵੱਧ ਵਾਰੀ ਜਾਂ ਸਪੇਸ-ਅਲੱਗ ਕੀਮਤ ਦੇ ਤੌਰ 'ਤੇ ਪਾਸ ਕੀਤਾ ਜਾ ਸਕਦਾ ਹੈ। ਡਿਫ਼ਾਲਟ ਸਭ ਖੋਜੀਆਂ ਗਈਆਂ ਅਨੁਵਾਦ ਭਾਸ਼ਾਵਾਂ ਹਨ। |
| `-r`, `--root-dir` | No | Project root. Defaults to the current directory. |
| `--changed-from` | ਨਹੀਂ | Git ref ਜੋ ਸਮੀਖਿਆ ਨੂੰ ਸਿਰਫ ਬਦਲੇ ਹੋਏ ਸਰੋਤ ਫਾਈਲਾਂ ਤੱਕ ਸੀਮਿਤ ਕਰਨ ਲਈ ਵਰਤੀ ਜਾਂਦੀ ਹੈ। |
| `--readme-only` | No | Review only the root `README.md` translation. |
| `--format` | No | Output format: `text` or `github`. Defaults to `text`. |

`co-op-review` ਵਰਤਮਾਨ ਵਿੱਚ ਗੁੰਮ ਹੋਏ ਅਨੁਵਾਦਿਤ ਫਾਇਲਾਂ, ਗੁੰਮ ਜਾਂ ਪੁਰਾਣਾ ਹੋ ਚੁੱਕਾ ਅਨੁਵਾਦ ਮੈਟਾ ਡੇਟਾ, Markdown ਫਰੰਟਮੈਟਰ ਅਤੇ ਕੋਡ ਫੇੰਸ ਦੀ ਅਖੰਡਤਾ, ਗਲਤ ਅਨੁਵਾਦਿਤ ਨੋਟਬੁੱਕ JSON, ਅਤੇ ਗੁੰਮ ਲੋਕਲ Markdown ਜਾਂ ਚਿੱਤਰ ਲਿੰਕ ਟਾਰਗਟਾਂ ਦੀ ਜਾਂਚ ਕਰਦਾ ਹੈ। ਗੁੰਮ ਲਿੰਕ ਡਿਫ਼ਾਲਟ ਤੌਰ 'ਤੇ ਚੇਤਾਵਨੀ ਹੁੰਦੇ ਹਨ; ਸੰਰਚਨਾਤਮਕ ਅਤੇ ਤਾਜ਼ਗੀ ਸਮੱਸਿਆਵਾਂ ਕਮਾਂਡ ਨੂੰ ਅਸਫਲ ਕਰ ਦਿੰਦੀਆਂ ਹਨ।

## co-op-translator-mcp

ਏਜੰਟਾਂ, ਐਡਿਟਰਾਂ, ਅਤੇ MCP-ਅਨੁਕੂਲ ਕਲਾਇੰਟਾਂ ਲਈ Co-op Translator MCP ਸਰਵਰ ਚਲਾਓ।

```bash
co-op-translator-mcp
```

ਡਿਫਾਲਟ ਟਰਾਂਸਪੋਰਟ `stdio` ਹੈ। ਕਲਾਇੰਟ ਸੰਰਚਨਾ, ਟੂਲ, ਸਰੋਤ ਅਤੇ ਸੁਰੱਖਿਆ ਨੋਟਸ ਲਈ [MCP ਸਰਵਰ](mcp.md) ਦੀ ਗਾਈਡ ਵੇਖੋ।

### ਵਿਕਲਪ

| Option | Required | Description |
| --- | --- | --- |
| `--transport` | No | MCP transport: `stdio`, `streamable-http`, or `sse`. Defaults to `stdio`. |

## migrate-links

ਅਨੁਵਾਦ ਹੋਈਆਂ Markdown ਫਾਈਲਾਂ ਨੂੰ ਮੁੜ ਪ੍ਰੋਸੈਸ ਕਰੋ ਅਤੇ ਨੋਟਬੁੱਕ ਲਿੰਕ ਅਪਡੇਟ ਕਰੋ ਤਾਂ ਜੋ ਉਹ ਉਪਲਬਧ ਹੋਣ 'ਤੇ ਅਨੁਵਾਦਿਤ ਨੋਟਬੁੱਕ ਵੱਲ ਸੰਕੇਤ ਕਰਨ।

```bash
migrate-links -l "ko ja"
```

### ਆਮ ਉਦਾਹਰਣ

ਲਿੰਕ ਅਪਡੇਟਾਂ ਦਾ ਪੂਰਵੀ ਨਜ਼ਾਰਾ ਕਰੋ:

```bash
migrate-links -l "ko" --dry-run
```

ਸਾਰੇ ਸਮਰਥਿਤ ਭਾਸ਼ਾਵਾਂ ਨੂੰ ਬਿਨਾਂ ਪੁਸ਼ਟੀ ਦੇ ਪ੍ਰੋਸੈਸ ਕਰੋ:

```bash
migrate-links -l "all" -y
```

ਸਿਰਫ ਓਹ ਲਿੰਕ ਦੁਬਾਰਾ ਲਿਖੋ ਜਦੋਂ ਅਨੁਵਾਦਿਤ ਨੋਟਬੁੱਕ ਮੌਜੂਦ ਹੋਣ:

```bash
migrate-links -l "ko" --no-fallback-to-original
```

### ਵਿਕਲਪ

| Option | Required | Description |
| --- | --- | --- |
| `-l`, `--language-codes` | Yes | Space-separated language codes, or `"all"`. |
| `-r`, `--root-dir` | No | Project root. Defaults to the current directory. |
| `--image-dir` | ਨਹੀਂ | ਰੂਟ ਦੇ ਸੰਦਰਭ ਵਿੱਚ ਅਨੁਵਾਦਿਤ ਚਿੱਤਰ ਡਾਇਰੈਕਟਰੀ। ਮੂਲ ਰੂਪ ਵਿੱਚ `translated_images`। |
| `--dry-run` | ਨਹੀਂ | ਅਪਡੇਟ ਲਿਖੇ ਬਿਨਾਂ ਕਿਹੜੀਆਂ ਫਾਈਲਾਂ ਬਦਲਣਗੀਆਂ, ਉਹ ਦਿਖਾਓ। |
| `--fallback-to-original`, `--no-fallback-to-original` | No | ਜਦੋਂ ਅਨੁਵਾਦਿਤ ਨੋਟਬੁੱਕ ਲਾਪਤਾ ਹੁੰਦੇ ਹਨ ਤਾਂ ਮੂਲ ਨੋਟਬੁੱਕ ਲਿੰਕ ਵਰਤੋ। ਡਿਫ਼ਾਲਟ ਰੂਪ ਵਿੱਚ ਯੋਗ ਹੈ। |
| `-d`, `--debug` | No | Enable debug logging. |
| `-s`, `--save-logs` | No | Save DEBUG-level logs under `<root-dir>/logs/`. |
| `-y`, `--yes` | ਨਹੀਂ | ਸਾਰੀਆਂ ਭਾਸ਼ਾਵਾਂ ਨੂੰ ਪ੍ਰਕਿਰਿਆ ਕਰਦੇ ਸਮੇਂ ਪ੍ਰੰਪਟਾਂ ਨੂੰ ਆਟੋ-ਕਨਫਰਮ ਕਰੋ। |

## Environment

ਜਦੋਂ ਕਿਸੇ ਕਮਾਂਡ ਨੂੰ ਪ੍ਰੋਵਾਇਡਰ ਕ੍ਰੈਡੈਂਸ਼ਲ ਦੀ ਲੋੜ ਹੋਵੇ, ਤਾਂ ਇਹਨਾਂ ਪ੍ਰੋਵਾਇਡਰ ਸੈੱਟਾਂ ਵਿੱਚੋਂ ਇੱਕ ਨੂੰ ਕਨਫਿਗਰ ਕਰੋ। `translate --dry-run` ਅਤੇ `co-op-review` ਨੂੰ ਪ੍ਰੋਵਾਇਡਰ ਕ੍ਰੈਡੈਂਸ਼ਲ ਦੀ ਲੋੜ ਨਹੀਂ ਹੈ:

```bash
# ਅਜ਼ੂਰ ਓਪਨਏਆਈ
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"

# ਜਾਂ ਓਪਨਏਆਈ
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"

# ਜਾਂ ਐਂਥਰੋਪਿਕ
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

ਚਿੱਤਰ ਅਨੁਵਾਦ ਲਈ ਅਤਿਰਿਕਤ ਤੌਰ 'ਤੇ Azure AI Vision ਦੀ ਲੋੜ ਹੁੰਦੀ ਹੈ:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

## ਆਉਟਪੁੱਟ ਲੇਆਉਟ

Text translations are written under:

```text
translations/<language-code>/<original-path>
```

ਅਨੁਵਾਦਿਤ ਚਿੱਤਰ ਆਉਟਪੁੱਟ ਲਿਖਿਆ ਜਾਂਦਾ ਹੈ:

```text
translated_images/<language-code>/<original-path>
```

For example, translating `README.md` and `docs/setup.md` into Korean produces:

```text
translations/ko/README.md
translations/ko/docs/setup.md
```

## ਕਾਪੀ-ਪੇਸਟ CLI ਉਦਾਹਰਨਾਂ

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

ਫਾਈਲਾਂ ਨੂੰ ਲਿਖਣ ਤੋਂ ਬਿਨਾਂ Markdown ਅਨੁਵਾਦ ਦਾ ਪ੍ਰੀਵਿਊ:

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