# Microsoft Beginners Repositories

This page is for maintainers of Microsoft "For Beginners" repositories that use the shared "Other Courses" README section.

Most Co-op Translator users do not need this page.

## Auto-Sync the Other Courses Section

Add these markers around the "Other Courses" section in your README:

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

Each time Co-op Translator runs through the CLI or GitHub Actions, it replaces the content between the markers with the packaged template.

## Update the Shared Template

The template source lives at:

```text
src/co_op_translator/templates/other_courses.md
```

To update the shared content:

1. Edit the template.
2. Open a pull request to Co-op Translator.
3. After the change is released, run Co-op Translator in the target repository.

## Sparse Checkout Advisory

Large course repositories can become expensive to clone when they include many translated outputs. You can include this advisory in generated language sections:

```markdown
> **Prefer to Clone Locally?**
>
> This repository includes many language translations, which can significantly increase download size. To clone without translations, use sparse checkout:
>
> ```bash
> git clone --filter=blob:none --sparse https://github.com/org/repo.git
> cd repo
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
```
