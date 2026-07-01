# Troubleshooting

Use this page when a translation run succeeds unexpectedly, fails during configuration, or produces output that needs review.

## Start Here

1. Run a focused command first, such as `translate -l "ko" -md`.
2. Add `-d` for console debug logs.
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

- Configure Azure OpenAI or OpenAI.
- Verify the variables are in the environment where the command runs.
- For local usage, put them in `.env` at the project root.

See [Configuration](configuration.md).

### Image Translation Without Azure AI Vision

Error:

```text
Image translation requested but Azure AI Service is not configured.
```

Fix:

- Add `AZURE_AI_SERVICE_API_KEY`.
- Add `AZURE_AI_SERVICE_ENDPOINT`.
- Or run a text-only command such as `translate -l "ko" -md`.

### Invalid Key or Endpoint

Symptoms can include `401`, redacted permission errors, or endpoint access errors.

Fix:

- Confirm the key belongs to the same Azure resource as the endpoint.
- Confirm the resource supports Vision when using `-img`.
- Confirm Azure OpenAI deployment name and API version match your deployment.
- Run with debug logs: `translate -l "ko" -md -d -s`.

## No Files Were Translated

Common causes:

- The selected flags do not match your files.
- Existing translated files are already present.
- Source files are under excluded directories.
- The command is running from the wrong project root.

Checks:

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -nb --dry-run
translate -l "ko" -img --dry-run
```

Use `--root-dir` when the command is run outside the project root.

## Unexpected Link Behavior

Link rewriting depends on selected content types:

- `-nb` included: notebook links can point to translated notebooks.
- `-nb` excluded: notebook links can remain pointed at source notebooks.
- `-img` included: image links can point to translated images.
- `-img` excluded: image links can remain pointed at source images.

Run a full content translation when all internal links should prefer translated outputs:

```bash
translate -l "ko" -md -nb -img
```

Run link review after translation:

```bash
co-op-review -l "ko"
```

## Markdown Rendering Issues

If translated Markdown renders incorrectly:

- Check that frontmatter starts and ends with `---`.
- Check that code fence counts match between source and translated files.
- Run `co-op-review` to catch common structure issues.
- Re-translate the specific file if the output was corrupted.

```bash
co-op-review -l "ko" --format github
```

## GitHub Action Ran but No Pull Request Was Created

If `peter-evans/create-pull-request` reports that the branch is not ahead of base, the workflow found no files to commit.

Likely causes:

- The translation run produced no changes.
- `.gitignore` excludes `translations/`, `translated_images/`, or translated notebooks.
- `add-paths` does not match the generated output directories.
- The translation step exited early.

Fixes:

1. Confirm generated files exist in `translations/` or `translated_images/`.
2. Confirm `.gitignore` does not ignore generated outputs.
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

Machine translations may need human review. Use `evaluate` only when you want experimental quality scoring and low-confidence repair workflows.

!!! warning "Experimental"
    `evaluate` can use rule-based and LLM-based checks, and its scoring model and metadata behavior may change. Keep it out of required CI gates unless your workflow is prepared for changes.

For deterministic CI checks, use `co-op-review` instead.