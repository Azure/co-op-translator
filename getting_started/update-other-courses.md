# Update the "Other Courses" section (Microsoft Beginners repos)

This guide explains how to make the "Other Courses" section auto‑synchronize using Co‑op Translator, and how to update the global template for all repos.

- Applies to: Microsoft Beginners repositories only
- Works with: Co‑op Translator CLI and GitHub Actions
- Template source: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## Quick start: Enable auto‑sync in your repo

Add the following markers around the "Other Courses" section in your README. Co‑op Translator will replace everything between these markers on every run.

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

Each time Co‑op Translator runs—via CLI (e.g., `translate -l "<language codes>"`) or GitHub Actions—it automatically updates the "Other Courses" section wrapped by these markers.

> [!NOTE]
> If you have an existing list, just wrap it with the same markers. The next run will replace it with the latest standardized content.

---

## How to change the global content

If you want to update the standardized content that appears in all Beginners repos:

1. Edit the template: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)
2. Open a pull request to the Co-op Translator repo with your changes
3. After the PR is merged, the Co‑op Translator version will be updated
4. The next time Co‑op Translator runs (CLI or GitHub Action) in a target repo, it will automatically sync the updated section

This ensures a single source of truth for the "Other Courses" content across all Beginners repositories.
