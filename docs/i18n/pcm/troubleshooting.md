# How to Solve Wahala

Use dis page wen translation run succeed wey nobody expect, fail during configuration, or produce output wey need review.

## How to Start

1. First run small focused command, like `translate -l "ko" -md`.
2. Put `-d` make e show console debug logs.
3. Put `-s` make e save debug logs for `<root-dir>/logs/`.
4. Run `co-op-review` after translation make you check freshness, structure, and local links.

```bash
translate -l "ko" -md -d -s
co-op-review -l "ko"
```

## Configuration Wahala

### No Language Model Provider

Error:

```text
No language model configuration found.
```

Fix:

- Configure Azure OpenAI, OpenAI, or Anthropic.
- Verify say the variables dey for the environment wey the command dey run.
- For local use, put dem for `.env` for the project root.

See [Configuration](configuration.md).

### Image Translation Without Azure AI Vision

Error:

```text
Image translation requested but Azure AI Service is not configured.
```

Fix:

- Add `AZURE_AI_SERVICE_API_KEY`.
- Add `AZURE_AI_SERVICE_ENDPOINT`.
- Or run text-only command like `translate -l "ko" -md`.

### Invalid Key or Endpoint

Symptoms fit include `401`, redacted permission errors, or endpoint access errors.

Fix:

- Confirm say the key belong to the same Azure resource as the endpoint.
- Confirm say the resource support Vision if you dey use `-img`.
- Confirm Azure OpenAI deployment name and API version dey match your deployment.
- Run with debug logs: `translate -l "ko" -md -d -s`.

## No Files No Translate

Common causes:

- The selected flags no match your files.
- Translated files don already dey present.
- Source files dey under excluded directories.
- The command dey run from the wrong project root.

Checks:

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -nb --dry-run
translate -l "ko" -img --dry-run
```

Use `--root-dir` wen the command dey run outside the project root.

## Unexpected Link Behavior

Link rewriting depend on selected content types:

- `-nb` included: notebook links fit point to translated notebooks.
- `-nb` excluded: notebook links fit remain point to source notebooks.
- `-img` included: image links fit point to translated images.
- `-img` excluded: image links fit remain point to source images.

Run full content translation when all internal links suppose prefer translated outputs:

```bash
translate -l "ko" -md -nb -img
```

Run link review after translation:

```bash
co-op-review -l "ko"
```

## Markdown Rendering Wahala

If translated Markdown no render correct:

- Check say frontmatter start and end with `---`.
- Check say code fence counts match between source and translated files.
- Run `co-op-review` to catch common structure issues.
- Re-translate that specific file if the output corrupt.

```bash
co-op-review -l "ko" --format github
```

## GitHub Action Run but No Pull Request Create

If `peter-evans/create-pull-request` report say the branch no ahead of base, the workflow no find files to commit.

Likely causes:

- The translation run no produce any changes.
- `.gitignore` dey exclude `translations/`, `translated_images/`, or translated notebooks.
- `add-paths` no match the generated output directories.
- The translation step stop early.

Fixes:

1. Confirm say generated files dey for `translations/` or `translated_images/`.
2. Confirm `.gitignore` no ignore generated outputs.
3. Use matching `add-paths`:

   ```yaml
   with:
     add-paths: |
       translations/
       translated_images/
   ```

4. Temporarily add debug flags to the translate command:

   ```bash
   translate -l "ko" -md -d -s
   ```

5. Confirm say workflow permissions include:

   ```yaml
   permissions:
     contents: write
     pull-requests: write
   ```

## Translation Quality

Machine translations fit need human review. Use `evaluate` only if you want experimental quality scoring and low-confidence repair workflows.

!!! warning "Experimental"
    `evaluate` fit use rule-based and LLM-based checks, and its scoring model and metadata behavior fit change. Keep am out of required CI gates unless your workflow don ready for changes.

For deterministic CI checks, use `co-op-review` instead.