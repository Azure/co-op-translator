# CLI ਰੈਫਰੈਂਸ

Co-op Translator ਇਹਨਾਂ ਕਮਾਂਡ-ਲਾਈਨ ਐਂਟਰੀ ਪੌਇੰਟਸ ਨੂੰ ਇੰਸਟਾਲ ਕਰਦਾ ਹੈ:

- `translate`
- `evaluate`
- `migrate-links`
- `co-op-review`
- `co-op-translator-mcp`

The `translate`, `evaluate`, `migrate-links`, and `co-op-review` commands dispatch through `co_op_translator.__main__`, which selects the command implementation based on the invoked script name. The MCP server uses `co_op_translator.mcp.server` directly.

ਜੇ ਤੁਸੀਂ CLI, Python API, ਅਤੇ MCP ਵਿੱਚੋਂ ਫੈਸਲਾ ਕਰ ਰਹੇ ਹੋ, ਤਾਂ [ਆਪਣਾ ਵਰਕਫਲੋ ਚੁਣੋ](workflows.md) ਤੋਂ ਸ਼ੁਰੂ ਕਰੋ।

## ਪਹਿਲੀ ਵਾਰੀ CLI ਫਲੋ

Start here if you are using Co-op Translator from a terminal:

1. ਇੱਕ LLM ਪ੍ਰਦਾਤਾ ਸੰਰਚਿਤ ਕਰੋ ਜਿਵੇਂ ਕਿ [ਸੰਰਚਨਾ](configuration.md) ਵਿੱਚ ਵਰਣਨ ਕੀਤਾ ਗਿਆ ਹੈ।
2. ਉਹ ਸਮੱਗਰੀ ਕਿਸਮ ਚੁਣੋ ਜਿਸਨੂੰ ਤੁਸੀਂ ਅਨੁਵਾਦ ਕਰਨਾ ਚਾਹੁੰਦੇ ਹੋ।
3. ਪਹਿਲਾਂ ਕਿਸੇ ਮੁੱਖ-ਕੇਂਦਰਤ ਕਮਾਂਡ ਨੂੰ ਚਲਾਓ, ਉਦਾਹਰਨ ਵਜੋਂ ਕੇਵਲ Markdown ਅਨੁਵਾਦ।
4. ਵੱਡੀਆਂ ਰਿਪੋਜ਼ਟਰੀ ਬਦਲਾਵਾਂ ਤੋਂ ਪਹਿਲਾਂ `--dry-run` ਵਰਤੋਂ।
5. ਅਨੁਵਾਦ ਦੇ ਬਾਅਦ ਰਚਨਾ ਅਤੇ ਤਾਜ਼ਗੀ ਜਾਂਚਣ ਲਈ `co-op-review` ਵਰਤੋਂ।

| ਉਦੇਸ਼ | ਸ਼ੁਰੂ ਕਰਨ ਲਈ ਕਮਾਂਡ |
| --- | --- |
| Markdown ਦਸਤਾਵੇਜ਼ਾਂ ਦਾ ਅਨੁਵਾਦ ਕਰੋ | `translate -l "ko" -md` |
| ਨੋਟਬੁੱਕਾਂ ਦਾ ਅਨੁਵਾਦ ਕਰੋ | `translate -l "ko" -nb` |
| ਚਿੱਤਰ ਟੈਕਸਟ ਦਾ ਅਨੁਵਾਦ | `translate -l "ko" -img` |
| ਫਾਇਲਾਂ ਲਿਖਣ ਤੋਂ ਬਿਨਾਂ ਕੰਮ ਦਾ ਪ੍ਰੀਵਿਊ | `translate -l "ko" -md --dry-run` |
| ਮੌਜੂਦਾ ਅਨੁਵਾਦਾਂ ਦੀ ਸਮੀਖਿਆ ਕਰੋ | `co-op-review -l "ko"` |
| ਨੋਟਬੁੱਕ ਅਤੇ Markdown ਲਿੰਕਾਂ ਨੂੰ ਅੱਪਡੇਟ ਕਰੋ | `migrate-links -l "ko" --dry-run` |
| ਟੂਲਾਂ ਨੂੰ MCP ਕਲਾਇੰਟ ਲਈ ਉਪਲਬਧ ਕਰੋ | Configure the [MCP ਸਰਵਰ](mcp.md) instead of running CLI commands directly. |

## translate

Markdown ਫਾਇਲਾਂ, ਨੋਟਬੁੱਕਾਂ, ਅਤੇ ਚਿੱਤਰ ਟੈਕਸਟ ਨੂੰ ਇੱਕ ਜਾਂ ਵੱਧ ਟਾਰਗੇਟ ਭਾਸ਼ਾਵਾਂ ਵਿੱਚ ਅਨੁਵਾਦ ਕਰੋ।

```bash
translate -l "ko ja fr"
```

### ਆਮ ਉਦਾਹਰਨ

ਕੇਵਲ Markdown ਦਾ ਅਨੁਵਾਦ:

```bash
translate -l "de" -md
```

ਕੇਵਲ ਨੋਟਬੁੱਕ ਦਾ ਅਨੁਵਾਦ:

```bash
translate -l "zh-CN" -nb
```

Markdown ਅਤੇ ਚਿੱਤਰਾਂ ਦਾ ਅਨੁਵਾਦ:

```bash
translate -l "pt-BR" -md -img
```

ਮੌਜੂਦਾ ਅਨੁਵਾਦਾਂ ਨੂੰ ਮਿਟਾ ਕੇ ਮੁੜ ਬਣਾਓ:

```bash
translate -l "ko" -u
```

ਇੰਟਰਐਕਟਿਵ ਪ੍ਰੌਂਪਟਾਂ ਬਿਨਾਂ ਚਲਾਓ:

```bash
translate -l "ko ja" -md -y
```

ਲਾਗ ਸੇਵ ਕਰੋ:

```bash
translate -l "ko" -s
```

### ਵਿਕਲਪ

| ਵਿਕਲਪ | ਲਾਜ਼ਮੀ | ਵੇਰਵਾ |
| --- | --- | --- |
| `-l`, `--language-codes` | Yes | ਸਪੇਸ-ਵੱਖ ਕੀਤੇ ਭਾਸ਼ਾ ਕੋਡ, ਜਿਵੇਂ `"es fr de"`, ਜਾਂ `"all"`. |
| `-r`, `--root-dir` | No | ਪ੍ਰੋਜੈਕਟ ਰੂਟ। ਡਿਫਾਲਟ ਤੌਰ 'ਤੇ ਮੌਜੂਦਾ ਡਾਇਰੈਕਟਰੀ। |
| `-u`, `--update` | No | ਚੁਣੀਆਂ ਭਾਸ਼ਾਵਾਂ ਲਈ ਮੌਜੂਦਾ ਅਨੁਵਾਦਾਂ ਨੂੰ ਮਿਟਾਓ ਅਤੇ ਮੁੜ ਬਣਾਓ। |
| `-img`, `--images` | No | ਕੇਵਲ ਚਿੱਤਰ ਫਾਇਲਾਂ ਦਾ ਅਨੁਵਾਦ ਕਰੋ। |
| `-md`, `--markdown` | No | ਕੇਵਲ Markdown ਫਾਇਲਾਂ ਦਾ ਅਨੁਵਾਦ ਕਰੋ। |
| `-nb`, `--notebook` | No | ਕੇਵਲ Jupyter ਨੋਟਬੁੱਕ ਫਾਇਲਾਂ ਦਾ ਅਨੁਵਾਦ ਕਰੋ। |
| `-d`, `--debug` | No | ਕਨਸੋਲ ਵਿੱਚ ਡੀਬੱਗ ਲੌਗਿੰਗ ਨੂੰ ਯੋਗ ਕਰੋ। |
| `-s`, `--save-logs` | No | DEBUG-ਸਤਰ ਦੀਆਂ ਲੌਗ ਫਾਇਲਾਂ ਨੂੰ `<root-dir>/logs/` ਹੇਠ ਸੇਵ ਕਰੋ। |
| `-x`, `--fix` | No | ਪਿਛਲੇ ਮੁਲਾਂਕਣ ਨਤੀਜਿਆਂ ਦੇ ਅਧਾਰ 'ਤੇ ਘੱਟ-ਵਿਸ਼ਵਾਸ ਵਾਲੀਆਂ Markdown ਫਾਇਲਾਂ ਨੂੰ ਦੁਬਾਰਾ ਅਨੁਵਾਦ ਕਰੋ। |
| `-c`, `--min-confidence` | No | `--fix` ਲਈ ਵਿਸ਼ਵਾਸ ਦੀ ਸੀਮਾ। ਡਿਫਾਲਟ ਹੈ `0.7`. |
| `--add-disclaimer`, `--no-disclaimer` | No | ਮਸ਼ੀਨ ਅਨੁਵਾਦ ਡਿਸਕਲੇਮਰ ਜੋੜੋ ਜਾਂ ਰੋਕੋ। CLI ਵਿੱਚ ਡਿਫਾਲਟ ਤੌਰ 'ਤੇ ਯੋਗ ਹੈ। |
| `-f`, `--fast` | No | ਤੇਜ਼ (fast) ਚਿੱਤਰ ਮੋਡ — ਡੈਪਰੀਕੇਟਡ। |
| `-y`, `--yes` | No | ਪ੍ਰੌਂਪਟਾਂ ਨੂੰ ਆਟੋ-ਕੰਫਰਮ ਕਰੋ, CI ਵਿੱਚ ਲਾਭਦਾਇਕ। |
| `--repo-url` | No | README ਭਾਸ਼ਾ ਟੇਬਲ ਦੀ sparse-checkout ਸਲਾਹ ਵਿੱਚ ਵਰਤਿਆ ਜਾਣ ਵਾਲਾ ਰਿਪੋਜ਼ਟਰੀ URL। |
| `--migrate-language-folders` | No | ਪੁਰਾਣੇ ਉਪਨਾਮ ਫੋਲਡਰਾਂ ਨੂੰ (ਉਦਾਹਰਨ: `cn` ਜਾਂ `tw`) canonical BCP 47 ਫੋਲਡਰਾਂ ਵਿੱਚ ਨਾਂ-ਬਦਲੋ। |
| `--dry-run` | No | ਫਾਇਲਾਂ ਲਿਖੇ ਬਿਨਾਂ ਭਾਸ਼ਾ ਫੋਲਡਰ ਮਾਈਗ੍ਰੇਸ਼ਨ ਅਤੇ ਅਨੁਵਾਦ ਅੰਦਾਜ਼ੇ ਦੇ ਪ੍ਰੀਵਿਊ। |

ਜੇ ਕੋਈ ਕਿਸਮ ਫਲੈਗ ਨਹੀਂ ਦਿੱਤਾ ਗਿਆ, ਤਾਂ `translate` Markdown, ਨੋਟਬੁੱਕ, ਅਤੇ ਚਿੱਤਰਾਂ ਨੂੰ ਪ੍ਰੋਸੈੱਸ ਕਰਦਾ ਹੈ। ਚਿੱਤਰ ਅਨੁਵਾਦ ਲਈ Azure AI Vision ਸੰਰਚਨਾ ਦੀ ਲੋੜ ਹੁੰਦੀ ਹੈ।

## evaluate

Evaluate translated Markdown quality for one language.

!!! warning "Experimental"
    `evaluate` ਪ੍ਰਯੋਗਾਤਮਕ ਹੈ। ਇਹ ਨਿਯਮ-ਆਧਾਰਿਤ ਅਤੇ LLM-ਆਧਾਰਿਤ ਗੁਣਵੱਤਾ ਜਾਂਚ ਵਰਤ ਸਕਦਾ ਹੈ, ਮੁਲਾਂਕਣ ਨਤੀਜੇ ਅਨੁਵਾਦ ਮੈਟਾਡੇਟਾ ਵਿੱਚ ਲਿਖੇ ਜਾਂਦੇ ਹਨ, ਅਤੇ ਇਸ ਦਾ ਸਕੋਰਿੰਗ ਮਾਡਲ ਅਤੇ ਮੈਟਾਡੇਟਾ ਵਿਹਾਰ ਬਦਲ ਸਕਦਾ ਹੈ।

```bash
evaluate -l "ko"
```

### ਆਮ ਉਦਾਹਰਨ

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

### ਵਿਕਲਪ

| ਵਿਕਲਪ | ਲਾਜ਼ਮੀ | ਵੇਰਵਾ |
| --- | --- | --- |
| `-l`, `--language-code` | Yes | ਇਕੱਲਾ ਭਾਸ਼ਾ ਕੋਡ ਜਿਸ ਦਾ ਮੁਲਾਂਕਣ ਕੀਤਾ ਜਾਵੇ। ਉਪਨਾਮ ਕੋਡ ਨਾਰਮਲਾਈਜ਼ ਕੀਤੇ ਜਾਂਦੇ ਹਨ। |
| `-r`, `--root-dir` | No | ਪ੍ਰੋਜੈਕਟ ਰੂਟ। ਡਿਫਾਲਟ ਤੌਰ 'ਤੇ ਮੌਜੂਦਾ ਡਾਇਰੈਕਟਰੀ। |
| `-c`, `--min-confidence` | No | ਘੱਟ-ਵਿਸ਼ਵਾਸ ਵਾਲੇ ਅਨੁਵਾਦਾਂ ਨੂੰ ਲਿਸਟ ਕਰਨ ਵੇਲੇ ਵਰਤੀ ਜਾਣ ਵਾਲੀ ਸੀਮਾ। ਡਿਫਾਲਟ `0.7`. |
| `-d`, `--debug` | No | ਡੀਬੱਗ ਲੌਗਿੰਗ ਯੋਗ ਕਰੋ। |
| `-s`, `--save-logs` | No | DEBUG-ਸਤਰ ਦੀਆਂ ਲੌਗ ਫਾਇਲਾਂ ਨੂੰ `<root-dir>/logs/` ਹੇਠ ਸੇਵ ਕਰੋ। |
| `-f`, `--fast` | No | ਕੇਵਲ ਨਿਯਮ-ਆਧਾਰਿਤ ਮੁਲਾਂਕਣ। |
| `-D`, `--deep` | No | ਕੇਵਲ LLM-ਆਧਾਰਿਤ ਮੁਲਾਂਕਣ। |

ਡਿਫਾਲਟ ਰੂਪ ਵਿੱਚ, `evaluate` ਨਿਯਮ-ਆਧਾਰਿਤ ਅਤੇ LLM-ਆਧਾਰਿਤ ਦੋਵੇਂ ਮੁਲਾਂਕਣ ਵਰਤਦਾ ਹੈ। ਨਤੀਜੇ ਅਨੁਵਾਦ ਮੈਟਾਡੇਟਾ ਵਿੱਚ ਲਿਖੇ ਜਾਂਦੇ ਹਨ ਅਤੇ ਕਨਸੋਲ ਵਿੱਚ ਸੰਖੇਪ ਕੀਤੇ ਜਾਂਦੇ ਹਨ।

## co-op-review

API ਪ੍ਰਮਾਣ-ਪੱਤਰਾਂ ਦੇ ਬਿਨਾਂ ਨਿਰਧਾਰਤ ਅਨੁਵਾਦ ਰਖ-ਰਖਾਵ ਜਾਂਚਾਂ ਚਲਾਓ।

!!! note "Beta"
    `co-op-review` ਇੱਕ ਬੇਟਾ ਨਿਰਧਾਰਤ ਸਮੀਖਿਆ ਕਮਾਂਡ ਹੈ। ਇਹ ਮਾਡਲ ਪ੍ਰਦਾਤਿਆਂ ਨੂੰ ਕਾਲ ਨਹੀਂ ਕਰਦਾ ਅਤੇ ਫਾਇਲਾਂ ਨਹੀਂ ਲਿਖਦਾ, ਪਰ ਇਸ ਦੀਆਂ ਜਾਂਚਾਂ ਅਤੇ ਇਸ਼ੂ ਆਉਟਪੁੱਟ ਸਕੀਮਾ ਬਦਲ ਸਕਦੇ ਹਨ।

```bash
co-op-review -l "ko"
```

### ਆਮ ਉਦਾਹਰਨ

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

### ਵਿਕਲਪ

| ਵਿਕਲਪ | ਲਾਜ਼ਮੀ | ਵੇਰਵਾ |
| --- | --- | --- |
| `-l`, `--language-code` | No | ਸਮੀਖਿਆ ਲਈ ਭਾਸ਼ਾ ਕੋਡ। ਇਹ ਕਈ ਵਾਰੀ ਦਿੱਤਾ ਜਾ ਸਕਦਾ ਹੈ ਜਾਂ ਸਪੇਸ-ਵੱਖ ਕੀਤੇ ਮੁੱਲ ਵਜੋਂ। ਡਿਫਾਲਟ ਤੌਰ 'ਤੇ ਸਭ ਮਿਲੀਆਂ ਅਨੁਵਾਦ ਭਾਸ਼ਾਵਾਂ। |
| `-r`, `--root-dir` | No | ਪ੍ਰੋਜੈਕਟ ਰੂਟ। ਡਿਫਾਲਟ ਤੌਰ 'ਤੇ ਮੌਜੂਦਾ ਡਾਇਰੈਕਟਰੀ। |
| `--changed-from` | No | ਸਮੀਖਿਆ ਨੂੰ ਬਦਲੇ ਹੋਏ ਸਰੋਤ ਫਾਇਲਾਂ ਤੱਕ ਸੀਮਤ ਕਰਨ ਲਈ ਵਰਤਿਆ ਜਾਣ ਵਾਲਾ Git ref। |
| `--format` | No | ਆਉਟਪੁੱਟ ਫਾਰਮੈਟ: `text` ਜਾਂ `github`. ਡਿਫਾਲਟ `text`. |

`co-op-review` ਵਰਤਮਾਨ ਵਿੱਚ ਖੋਈ ਹੋਈ ਅਨੁਵਾਦ ਫਾਇਲਾਂ, ਗੁੰਮ ਜਾਂ ਪੁਰਾਣਾ ਹੋਇਆ ਅਨੁਵਾਦ ਮੈਟਾਡੇਟਾ, Markdown frontmatter ਅਤੇ ਕੋਡ ਫੈਨਸ ਦੀ ਇੱਕਤਾ, ਗਲਤ ਅਨੁਵਾਦਸ਼ੁਦਾ ਨੋਟਬੁੱਕ JSON, ਅਤੇ ਗੁੰਮ ਹੋਏ ਲੋਕਲ Markdown ਜਾਂ ਚਿੱਤਰ ਲਿੰਕ ਟਾਰਗੇਟਾਂ ਦੀ ਜਾਂਚ ਕਰਦਾ ਹੈ। ਗੁੰਮ ਲਿੰਕ ਪਹਿਲਾਂ ਤੌਰ 'ਤੇ ਚੇਤਾਵਨੀ ਹੁੰਦੇ ਹਨ; ਰਚਨਾਤਮਕ ਅਤੇ ਤਾਜ਼ਗੀ ਦੇ ਸਮੱਸਿਆਵਾਂ ਕਮਾਂਡ ਨੂੰ ਅਸਫਲ ਕਰ ਦਿੰਦੀਆਂ ਹਨ।

## co-op-translator-mcp

Run the Co-op Translator MCP server for agents, editors, and MCP-compatible clients.

```bash
co-op-translator-mcp
```

The default transport is `stdio`. See the [MCP ਸਰਵਰ](mcp.md) guide for client configuration, tools, resources, and safety notes.

### Options

| Option | Required | Description |
| --- | --- | --- |
| `--transport` | No | MCP transport: `stdio`, `streamable-http`, or `sse`. Defaults to `stdio`. |

## migrate-links

Reprocess translated Markdown files and update notebook links so they point to translated notebooks when available.

```bash
migrate-links -l "ko ja"
```

### ਆਮ ਉਦਾਹਰਨ

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

### ਵਿਕਲਪ

| ਵਿਕਲਪ | ਲਾਜ਼ਮੀ | ਵੇਰਵਾ |
| --- | --- | --- |
| `-l`, `--language-codes` | Yes | ਸਪੇਸ-ਵੱਖ ਕੀਤੇ ਭਾਸ਼ਾ ਕੋਡ, ਜਾਂ `"all"`. |
| `-r`, `--root-dir` | No | ਪ੍ਰੋਜੈਕਟ ਰੂਟ। ਡਿਫਾਲਟ ਤੌਰ 'ਤੇ ਮੌਜੂਦਾ ਡਾਇਰੈਕਟਰੀ। |
| `--image-dir` | No | ਰੂਟ ਦੇ ਸੰਦਰਭ ਵਿੱਚ ਅਨੁਵਾਦ ਚਿੱਤਰ ਡਾਇਰੈਕਟਰੀ। ਡਿਫਾਲਟ `translated_images`. |
| `--dry-run` | No | ਬਦਲਣ ਵਾਲੀਆਂ ਫਾਇਲਾਂ ਦਿਖਾਓ ਬਿਨਾਂ ਅੱਪਡੇਟ ਲਿਖੇ। |
| `--fallback-to-original`, `--no-fallback-to-original` | No | ਜਦੋਂ ਅਨੁਵਾਦ ਨੋਟਬੁੱਕ ਗੈਰ-ਮੌਜੂਦ ਹਨ ਤਾਂ ਮੂਲ ਨੋਟਬੁੱਕ ਲਿੰਕ ਵਰਤੋ। ਡਿਫਾਲਟ ਤੌਰ 'ਤੇ ਯੋਗ ਹੈ। |
| `-d`, `--debug` | No | ਡੀਬੱਗ ਲੌਗਿੰਗ ਯੋਗ ਕਰੋ। |
| `-s`, `--save-logs` | No | DEBUG-ਸਤਰ ਦੀਆਂ ਲੌਗ ਫਾਇਲਾਂ ਨੂੰ `<root-dir>/logs/` ਹੇਠ ਸੇਵ ਕਰੋ। |
| `-y`, `--yes` | No | ਸਾਰੇ ਭਾਸ਼ਾਵਾਂ ਪ੍ਰੋਸੈੱਸ ਕਰਨ ਵੇਲੇ ਪ੍ਰੌਂਪਟਾਂ ਨੂੰ ਆਟੋ-ਕੰਫਰਮ ਕਰੋ। |

## Environment

All commands require one configured LLM provider:

```bash
# ਐਜ਼ਰ ਓਪਨਏਆਈ
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"

# ਜਾਂ ਓਪਨਏਆਈ
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