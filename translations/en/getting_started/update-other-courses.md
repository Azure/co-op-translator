<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "93a7150216aa3c2d191135358fa6dd21",
  "translation_date": "2025-11-30T13:34:27+00:00",
  "source_file": "getting_started/update-other-courses.md",
  "language_code": "en"
}
-->
# Update the "Other Courses" section (Microsoft Beginners repos)

This guide explains how to make the "Other Courses" section auto-sync using Co-op Translator, and how to update the global template for all repositories.

- Applies to: Microsoft Beginners repositories only
- Works with: Co-op Translator CLI and GitHub Actions
- Template source: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## Quick start: Enable auto-sync in your repo

Add the following markers around the "Other Courses" section in your README. Co-op Translator will replace everything between these markers on every run.

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

Each time Co-op Translator runs—via CLI (e.g., `translate -l "<language codes>"`) or GitHub Actions—it automatically updates the "Other Courses" section wrapped by these markers.

> [!NOTE]
> If you already have a list, just wrap it with the same markers. The next run will replace it with the latest standardized content.

---

## How to change the global content

If you want to update the standardized content that appears in all Beginners repos:

1. Edit the template: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)
2. Open a pull request to the Co-op Translator repo with your changes
3. After the PR is merged, the Co-op Translator version will be updated
4. The next time Co-op Translator runs (CLI or GitHub Action) in a target repo, it will automatically sync the updated section

This ensures a single source of truth for the "Other Courses" content across all Beginners repositories.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we strive for accuracy, please be aware that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not liable for any misunderstandings or misinterpretations arising from the use of this translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->