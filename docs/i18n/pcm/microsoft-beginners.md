# Microsoft Repositories wey Beginners fit use

Dis page na for maintainers of Microsoft "For Beginners" repositories wey dey use di shared "Other Courses" README section.

Most Co-op Translator users no need dis page.

## Auto-Sync di Other Courses Section

Put these markers around di "Other Courses" section for your README:

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

Every time Co-op Translator run for the CLI or GitHub Actions, e go replace di content between di markers with di packaged template.

## Update di Shared Template

Di template source dey for:

```text
src/co_op_translator/templates/other_courses.md
```

To update di shared content:

1. Edit di template.
2. Open a pull request to Co-op Translator.
3. After dem release di change, run Co-op Translator in di target repository.

## Sparse Checkout Advisory

Big course repositories fit turn expensive to clone if dem get plenty translated outputs. You fit include dis advisory in generated language sections:

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