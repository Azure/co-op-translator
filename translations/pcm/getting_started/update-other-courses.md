<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "93a7150216aa3c2d191135358fa6dd21",
  "translation_date": "2025-11-06T17:31:28+00:00",
  "source_file": "getting_started/update-other-courses.md",
  "language_code": "pcm"
}
-->
# Update di "Other Courses" section (Microsoft Beginners repos)

Dis guide dey explain how you fit make di "Other Courses" section dey auto‑synchronize wit Co‑op Translator, and how you go fit update di global template for all repos.

- E dey apply to: Microsoft Beginners repositories only
- E dey work wit: Co‑op Translator CLI and GitHub Actions
- Template source: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## Quick start: Enable auto‑sync for your repo

Put di markers wey dey below around di "Other Courses" section for your README. Co‑op Translator go replace everything wey dey between di markers anytime e run.

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

Anytime wey Co‑op Translator run—whether na CLI (e.g., `translate -l "<language codes>"`) or GitHub Actions—e go automatically update di "Other Courses" section wey dey inside di markers.

> [!NOTE]
> If you get list wey don dey already, just put di markers around am. Di next time wey e run, e go replace am wit di latest standardized content.

---

## How you fit change di global content

If you wan update di standardized content wey dey show for all Beginners repos:

1. Edit di template: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)
2. Open pull request for di Co-op Translator repo wit di changes wey you make
3. After dem merge di PR, dem go update di Co‑op Translator version
4. Di next time wey Co‑op Translator run (CLI or GitHub Action) for di target repo, e go automatically sync di updated section

Dis one dey make sure say di "Other Courses" content get one single source of truth for all Beginners repositories.

---

**Disclaimer**:  
Dis dokyument don use AI translet service [Co-op Translator](https://github.com/Azure/co-op-translator) do di translet. Even as we dey try make am accurate, abeg sabi say AI translet fit get mistake or no dey correct well. Di original dokyument wey dey for im native language na di main source wey you go fit trust. For important mata, e good make professional human translet am. We no go fit take blame for any misunderstanding or wrong interpretation wey fit happen because you use dis translet.