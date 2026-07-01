# Mga Repositoryo ng Microsoft para sa mga Nagsisimula

Ang pahinang ito ay para sa mga tagapanatili ng Microsoft "For Beginners" na mga repositoryo na gumagamit ng pinagsasaluhang seksyon na "Other Courses" sa README.

Karamihan sa mga gumagamit ng Co-op Translator ay hindi nangangailangan ng pahinang ito.

## Awtomatikong Pag-sync ng Seksyon na "Other Courses"

Idagdag ang mga marker na ito sa paligid ng seksyon na "Other Courses" sa iyong README:

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

Sa bawat pagtakbo ng Co-op Translator sa pamamagitan ng CLI o GitHub Actions, pinapalitan nito ang nilalaman sa pagitan ng mga marker ng naka-package na template.

## I-update ang Pinagsasaluhang Template

Matatagpuan ang pinagmulan ng template sa:

```text
src/co_op_translator/templates/other_courses.md
```

Upang i-update ang pinagsasaluhang nilalaman:

1. I-edit ang template.
2. Magbukas ng pull request sa Co-op Translator.
3. Pagkatapos mailabas ang pagbabago, patakbuhin ang Co-op Translator sa target na repositoryo.

## Paalala tungkol sa Sparse Checkout

Ang malalaking repositoryo ng kurso ay maaaring maging magastos i-clone kapag naglalaman ang mga ito ng maraming isinaling output. Maaari mong isama ang paalalang ito sa mga nabuong seksyon ng wika:

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