<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "93a7150216aa3c2d191135358fa6dd21",
  "translation_date": "2025-11-30T13:49:53+00:00",
  "source_file": "getting_started/update-other-courses.md",
  "language_code": "sk"
}
-->
# Aktualizácia sekcie „Iné kurzy“ (Microsoft Beginners repozitáre)

Tento návod vysvetľuje, ako automaticky synchronizovať sekciu „Iné kurzy“ pomocou Co-op Translator a ako aktualizovať globálnu šablónu pre všetky repozitáre.

- Platí pre: iba Microsoft Beginners repozitáre
- Funguje s: Co-op Translator CLI a GitHub Actions
- Zdroj šablóny: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## Rýchly štart: Povolenie automatickej synchronizácie vo vašom repozitári

Pridajte nasledujúce značky okolo sekcie „Iné kurzy“ vo vašom README. Co-op Translator pri každom spustení nahradí všetko medzi týmito značkami.

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

Pri každom spustení Co-op Translatora – cez CLI (napr. `translate -l "<language codes>"`) alebo GitHub Actions – sa automaticky aktualizuje sekcia „Iné kurzy“ uzavretá medzi týmito značkami.

> [!NOTE]
> Ak už máte existujúci zoznam, jednoducho ho obalte rovnakými značkami. Pri ďalšom spustení bude nahradený najnovším štandardizovaným obsahom.

---

## Ako zmeniť globálny obsah

Ak chcete aktualizovať štandardizovaný obsah, ktorý sa zobrazuje vo všetkých Beginners repozitároch:

1. Upravte šablónu: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)
2. Otvorte pull request do repozitára Co-op Translator so svojimi zmenami
3. Po zlúčení PR sa aktualizuje verzia Co-op Translatora
4. Pri ďalšom spustení Co-op Translatora (CLI alebo GitHub Action) v cieľovom repozitári sa automaticky synchronizuje aktualizovaná sekcia

Týmto spôsobom je zabezpečený jednotný zdroj pravdy pre obsah sekcie „Iné kurzy“ vo všetkých Beginners repozitároch.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zrieknutie sa zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, majte prosím na pamäti, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->