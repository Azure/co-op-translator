# Translate your project

Use this page for a short workflow. For the complete option list, see the [CLI reference](../../docs/cli.md).

## Start narrow

Translate Markdown first. This keeps the first run fast and avoids image configuration while you confirm the language output folder looks right.

```bash
translate -l "ko" -md
```

Markdown output is written under:

```text
translations/ko/
```

## Add notebooks or images

Translate notebooks only:

```bash
translate -l "ko" -nb
```

Translate images only:

```bash
translate -l "ko" -img
```

Image translation requires both an LLM provider and Azure AI Vision. If you omit all content-type flags, `translate` processes Markdown, notebooks, and images, so Vision configuration is required.

## Translate multiple languages

Pass a space-separated list of language codes:

```bash
translate -l "ko ja fr" -md
```

Use `all` only when you intentionally want every supported language:

```bash
translate -l "all" -md -y
```

## Update or repair translations

Delete and recreate translations for selected languages:

```bash
translate -l "ko" -u
```

Evaluate Markdown quality:

```bash
evaluate -l "ko" -c 0.8
```

Retranslate low-confidence Markdown files:

```bash
translate -l "ko" --fix -c 0.8 -md
```

## Review before a pull request

Run deterministic checks without API keys:

```bash
co-op-review -l "ko"
```

In CI or pull request validation, limit review to changed source files and print GitHub-flavored Markdown:

```bash
co-op-review -l "ko" --changed-from origin/main --format github
```

## Keep links current

After translating notebooks, migrate links so translated Markdown points to translated notebooks when available:

```bash
migrate-links -l "ko"
```

Preview link updates without writing files:

```bash
migrate-links -l "ko" --dry-run
```

For troubleshooting and older workflow migration notes, see [Troubleshooting](../troubleshooting.md).
