<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "93a7150216aa3c2d191135358fa6dd21",
  "translation_date": "2025-11-30T13:48:10+00:00",
  "source_file": "getting_started/update-other-courses.md",
  "language_code": "tl"
}
-->
# I-update ang seksyon na "Other Courses" (Microsoft Beginners repos)

Ipinaliwanag sa gabay na ito kung paano gawing auto‑synchronize ang seksyon na "Other Courses" gamit ang Co‑op Translator, at kung paano i-update ang global template para sa lahat ng repos.

- Para sa: Microsoft Beginners repositories lamang
- Gumagana sa: Co‑op Translator CLI at GitHub Actions
- Pinagmulan ng template: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## Mabilisang pagsisimula: Paganahin ang auto‑sync sa iyong repo

Idagdag ang mga sumusunod na marker sa paligid ng seksyon na "Other Courses" sa iyong README. Papalitan ng Co‑op Translator ang lahat ng nasa pagitan ng mga marker na ito sa bawat pagtakbo.

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

Sa bawat pagtakbo ng Co‑op Translator—sa pamamagitan ng CLI (hal., `translate -l "<language codes>"`) o GitHub Actions—awtomatikong ina-update nito ang seksyon na "Other Courses" na nakapaloob sa mga marker na ito.

> [!NOTE]
> Kung mayroon ka nang umiiral na listahan, balutin mo lang ito gamit ang parehong mga marker. Sa susunod na pagtakbo, papalitan ito ng pinakabagong standardized na nilalaman.

---

## Paano baguhin ang global na nilalaman

Kung nais mong i-update ang standardized na nilalaman na lumalabas sa lahat ng Beginners repos:

1. I-edit ang template: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)
2. Magbukas ng pull request sa Co-op Translator repo kasama ang iyong mga pagbabago
3. Kapag na-merge na ang PR, maa-update ang bersyon ng Co‑op Translator
4. Sa susunod na pagtakbo ng Co‑op Translator (CLI o GitHub Action) sa target na repo, awtomatikong isi-sync nito ang na-update na seksyon

Tinitiyak nito ang iisang pinagkukunan ng katotohanan para sa nilalaman ng "Other Courses" sa lahat ng Beginners repositories.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Paunawa**:
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat nagsusumikap kami para sa katumpakan, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o di-tumpak na impormasyon. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->