# Hifadhi za Microsoft kwa Waanzilishi

Ukurasa huu ni kwa watunzaji wa hifadhi za Microsoft "For Beginners" ambazo zinatumia sehemu ya README ya "Other Courses" iliyoshirikiwa.

Watumiaji wengi wa Co-op Translator hawahitaji ukurasa huu.

## Ulandanishaji otomatiki wa sehemu ya "Other Courses"

Ongeza alama hizi kuzunguka sehemu ya "Other Courses" katika README yako:

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

Kila wakati Co-op Translator inapoendesha kupitia CLI au GitHub Actions, inabadilisha yaliyomo kati ya alama na kiolezo kilichopakiwa.

## Sasisha kiolezo kilichoshirikiwa

Chanzo cha kiolezo kiko katika:

```text
src/co_op_translator/templates/other_courses.md
```

Ili kusasisha maudhui yaliyoshirikiwa:

1. Hariri kiolezo.
2. Fungua pull request kwa Co-op Translator.
3. Baada ya mabadiliko kutolewa, endesha Co-op Translator katika hifadhi lengwa.

## Ushauri wa Sparse Checkout

Hifadhi kubwa za kozi zinaweza kuwa ghali kukopa (clone) wakati zinajumuisha matokeo mengi yaliyotafsiriwa. Unaweza kujumuisha ushauri huu katika sehemu za lugha zilizotengenezwa:

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