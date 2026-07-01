# Fix Wahala

Use dis page wen translation run succeed wen you no expect, fail during configuration, or e produce output wey need to be checked.

## Start from here

1. Run one focused command first, like `translate -l "ko" -md`.
2. Add `-d` make console show debug logs.
3. Add `-s` to save debug logs under `<root-dir>/logs/`.
4. Run `co-op-review` after translation to check freshness, structure, and local links.

```bash
translate -l "ko" -md -d -s
co-op-review -l "ko"
```

## Configuration Errors

### No Language Model Provider

Error:

```text
No language model configuration found.
```

Fix:

- Set up Azure OpenAI or OpenAI.
- Make sure the variables dey for the environment wey the command dey run.
- If you dey use locally, put dem inside `.env` for the project root.

See [Configuration](configuration.md).

### Image Translation Without Azure AI Vision

Error:

```text
Image translation requested but Azure AI Service is not configured.
```

Fix:

- Add `AZURE_AI_SERVICE_API_KEY`.
- Add `AZURE_AI_SERVICE_ENDPOINT`.
- Or run one text-only command like `translate -l "ko" -md`.

### Invalid Key or Endpoint

Symptoms fit include `401`, redacted permission errors, or endpoint access errors.

Fix:

- Confirm say the key belong to the same Azure resource as the endpoint.
- Confirm say the resource support Vision when you dey use `-img`.
- Confirm Azure OpenAI deployment name and API version match your deployment.
- Run with debug logs: `translate -l "ko" -md -d -s`.

## No Files Were Translated

Common causes:

- The selected flags no match your files.
- Translated files don already dey present.
- Source files dey under excluded directories.
- The command dey run from wrong project root.

Checks:

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -nb --dry-run
translate -l "ko" -img --dry-run
```

Use `--root-dir` when the command dey run outside the project root.

## Unexpected Link Behavior

Link rewriting depend on which content types you select:

- `-nb` included: notebook links fit point to translated notebooks.
- `-nb` excluded: notebook links fit still point to source notebooks.
- `-img` included: image links fit point to translated images.
- `-img` excluded: image links fit still point to source images.

Run full content translation when you want all internal links to prefer translated outputs:

```bash
translate -l "ko" -md -nb -img
```

Run link review after translation:

```bash
co-op-review -l "ko"
```

## Markdown Rendering Issues

If translated Markdown no dey render correct:

- Check say frontmatter start and end with `---`.
- Check say code fence counts match between source and translated files.
- Run `co-op-review` to catch common structure issues.
- Re-translate the specific file if the output don corrupt.

```bash
co-op-review -l "ko" --format github
```

## GitHub Action Ran but No Pull Request Was Created

If `peter-evans/create-pull-request` talk say the branch no ahead of base, the workflow no find files to commit.

Likely causes:

- The translation run no produce any changes.
- `.gitignore` dey exclude `translations/`, `translated_images/`, or translated notebooks.
- `add-paths` no match the generated output directories.
- The translation step exit early.

Fixes:

1. Confirm generated files dey for `translations/` or `translated_images/`.
2. Confirm `.gitignore` no dey ignore the generated outputs.
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

5. Confirm workflow permissions include:

   ```yaml
   permissions:
     contents: write
     pull-requests: write
   ```

## Translation Quality

Machine translations fit need human review. Use `evaluate` only when you want experimental quality scoring and low-confidence repair workflows.

!!! warning "Experimental"
    `evaluate` fit use rule-based and LLM-based checks, and im scoring model and metadata behavior fit change. Keep am outside required CI gates unless your workflow don ready for changes.

For deterministic CI checks, use `co-op-review` instead.