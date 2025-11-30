<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "93a7150216aa3c2d191135358fa6dd21",
  "translation_date": "2025-11-30T13:51:10+00:00",
  "source_file": "getting_started/update-other-courses.md",
  "language_code": "sr"
}
-->
# Ажурирање секције „Остали курсеви“ (Microsoft Beginners репозиторијуми)

Овај водич објашњава како да омогућите аутоматску синхронизацију секције „Остали курсеви“ користећи Co-op Translator, као и како да ажурирате глобални шаблон за све репозиторијуме.

- Односи се на: само Microsoft Beginners репозиторијуме
- Ради са: Co-op Translator CLI и GitHub Actions
- Извор шаблона: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## Брзи почетак: Омогућите аутоматску синхронизацију у вашем репозиторијуму

Додајте следеће маркере око секције „Остали курсеви“ у вашем README-у. Co-op Translator ће сваки пут заменити све што се налази између ових маркера.

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

Сваки пут када Co-op Translator покренете — преко CLI (нпр. `translate -l "<language codes>"`) или GitHub Actions — он аутоматски ажурира секцију „Остали курсеви“ обухваћену овим маркерима.

> [!NOTE]
> Ако већ имате постојећу листу, само је обавијте истим маркерима. Следеће покретање ће је заменити најновијим стандардизованим садржајем.

---

## Како променити глобални садржај

Ако желите да ажурирате стандардизовани садржај који се појављује у свим Beginners репозиторијумима:

1. Измените шаблон: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)
2. Отворите pull request у Co-op Translator репозиторијуму са вашим изменама
3. Након што се PR прихвати, верзија Co-op Translator-а ће бити ажурирана
4. Следећи пут када Co-op Translator покренете (CLI или GitHub Action) у циљаном репозиторијуму, аутоматски ће се синхронизовати ажурирана секција

Ово обезбеђује један извор истине за садржај „Остали курсеви“ у свим Beginners репозиторијумима.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Одрицање од одговорности**:
Овај документ је преведен коришћењем AI услуге за превођење [Co-op Translator](https://github.com/Azure/co-op-translator). Иако се трудимо да превод буде тачан, молимо вас да имате у виду да аутоматизовани преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитетним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->