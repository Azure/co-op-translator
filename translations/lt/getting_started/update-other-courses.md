<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "93a7150216aa3c2d191135358fa6dd21",
  "translation_date": "2025-11-30T13:53:20+00:00",
  "source_file": "getting_started/update-other-courses.md",
  "language_code": "lt"
}
-->
# Atnaujinkite skiltį „Kiti kursai“ (Microsoft pradedančiųjų saugyklos)

Šiame vadove paaiškinama, kaip automatiškai sinchronizuoti skiltį „Kiti kursai“ naudojant Co-op Translator ir kaip atnaujinti bendrą šabloną visoms saugykloms.

- Taikoma: tik Microsoft pradedančiųjų saugykloms
- Veikia su: Co-op Translator CLI ir GitHub Actions
- Šablono šaltinis: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## Greitas pradėjimas: įgalinkite automatinę sinchronizaciją savo saugykloje

Pridėkite šiuos žymeklius aplink skiltį „Kiti kursai“ savo README faile. Co-op Translator kiekvieno paleidimo metu pakeis viską, kas yra tarp šių žymeklių.

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

Kiekvieną kartą, kai Co-op Translator paleidžiamas – per CLI (pvz., `translate -l "<language codes>"`) arba GitHub Actions – jis automatiškai atnaujina skiltį „Kiti kursai“, esančią tarp šių žymeklių.

> [!NOTE]
> Jei jau turite esamą sąrašą, tiesiog apvyniokite jį tais pačiais žymekliais. Kitas paleidimas jį pakeis naujausiu standartizuotu turiniu.

---

## Kaip pakeisti bendrą turinį

Jei norite atnaujinti standartizuotą turinį, kuris rodomas visuose pradedančiųjų saugyklose:

1. Redaguokite šabloną: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)
2. Atidarykite pull request Co-op Translator saugykloje su savo pakeitimais
3. Kai PR bus sujungtas, Co-op Translator versija bus atnaujinta
4. Kitą kartą, kai Co-op Translator bus paleistas (CLI arba GitHub Action) tiksline saugykla, jis automatiškai sinchronizuos atnaujintą skiltį

Tai užtikrina vieningą „Kiti kursai“ turinio šaltinį visuose pradedančiųjų saugyklose.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojamas profesionalus žmogaus vertimas. Mes neatsakome už bet kokius nesusipratimus ar neteisingus aiškinimus, kylančius dėl šio vertimo naudojimo.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->