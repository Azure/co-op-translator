# Microsoft ప్రారంభికుల రిపోజిటరీలు

ఈ పేజీ Microsoft "For Beginners" రిపోజిటరీలను నిర్వహించే వారికి, అవి పంచుకున్న "Other Courses" README విభాగాన్ని ఉపయోగిస్తున్న సందర్భాల్లో ఉపయోగపడుతుంది.

బహుశా Co-op Translator వినియోగదారులకు ఈ పేజీ అవసరం లేదు.

## Other Courses విభాగాన్ని ఆటో-సింక్ చేయండి

మీ READMEలోని "Other Courses" విభాగం చుట్టూ ఈ మార్కర్లను జత చేయండి:

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

Co-op Translator CLI లేదా GitHub Actions ద్వారా ప్రతిసారి నడిచినప్పుడు, అది మార్కర్ల మధ్య ఉన్న విషయాన్ని ప్యాకేజ్డ్ టెంప్లేట్‌తో మార్చేస్తుంది.

## పంచుకున్న టెంప్లేట్‌ను నవీకరించండి

టెంప్లేట్ మూలం ఈ స్థలంలో ఉంది:

```text
src/co_op_translator/templates/other_courses.md
```

పంచుకున్న విషయాన్ని నవీకరించడానికి:

1. టెంప్లేట్‌ను సవరించండి.
2. Co-op Translator‌కు ఒక pull request తెరవండి.
3. మార్పు విడుదలైన తర్వాత, లక్ష్య రిపోజిటరీలో Co-op Translator నడిపండి.

## Sparse Checkout సలహా

అనేక అనువదించిన అవుట్పుట్‌లను కలిగి ఉన్న పెద్ద కోర్సు రిపోజిటరీలను క్లోన్ చేయడం ఖరీదైనదిగా మారవచ్చు. మీరు రూపొందించిన భాషా విభాగాలలో ఈ సలహాను చేర్చవచ్చు:

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