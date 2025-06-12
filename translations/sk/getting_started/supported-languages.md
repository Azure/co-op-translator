<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b4ed48f23ec418b31e90a02fe629fcde",
  "translation_date": "2025-06-12T12:18:16+00:00",
  "source_file": "getting_started/supported-languages.md",
  "language_code": "sk"
}
-->
# Podporované jazyky

Tabuľka nižšie uvádza jazyky, ktoré sú momentálne podporované **Co-op Translator**. Obsahuje kódy jazykov, názvy jazykov a prípadné známe problémy spojené s každým jazykom. Ak chcete pridať podporu pre nový jazyk, pridajte príslušný kód jazyka, názov a vhodné písmo do súboru `font_language_mappings.yml`, ktorý sa nachádza v `src/co_op_translator/fonts/`, a po otestovaní odošlite pull request.

| Language Code | Language Name        | Font                              | RTL Support | Known Issues |
|---------------|----------------------|-----------------------------------|-------------|--------------|
| en            | Angličtina           | NotoSans-Medium.ttf               | Nie         | Nie          |
| fr            | Francúzština         | NotoSans-Medium.ttf               | Nie         | Nie          |
| es            | Španielčina          | NotoSans-Medium.ttf               | Nie         | Nie          |
| de            | Nemčina              | NotoSans-Medium.ttf               | Nie         | Nie          |
| ru            | Ruština              | NotoSans-Medium.ttf               | Nie         | Nie          |
| ar            | Arabčina             | NotoSansArabic-Medium.ttf         | Áno         | Nie          |
| fa            | Perzština (Farsi)    | NotoSansArabic-Medium.ttf         | Nie         | Nie          |
| ur            | Urdu                 | NotoSansArabic-Medium.ttf         | Nie         | Nie          |
| zh            | Čínština (zjednodušená) | NotoSansCJK-Medium.ttc          | Nie         | Nie          |
| mo            | Čínština (tradičná, Macau) | NotoSansCJK-Medium.ttc       | Nie         | Nie          |
| hk            | Čínština (tradičná, Hong Kong) | NotoSansCJK-Medium.ttc   | Nie         | Nie          |
| tw            | Čínština (tradičná, Taiwan) | NotoSansCJK-Medium.ttc       | Nie         | Nie          |
| ja            | Japončina            | NotoSansCJK-Medium.ttc            | Nie         | Nie          |
| ko            | Kórejčina            | NotoSansCJK-Medium.ttc            | Nie         | Nie          |
| hi            | Hindčina             | NotoSansDevanagari-Medium.ttf     | Nie         | Nie          |
| bn            | Bengálčina           | NotoSansBengali-Medium.ttf        | Nie         | Nie          |
| mr            | Maráthčina           | NotoSansDevanagari-Medium.ttf     | Nie         | Nie          |
| ne            | Nepálčina            | NotoSansDevanagari-Medium.ttf     | Nie         | Nie          |
| pa            | Pandžábčina (Gurmukhi) | NotoSansGurmukhi-Medium.ttf     | Nie         | Nie          |
| pt            | Portugalčina (portugalská) | NotoSans-Medium.ttf           | Nie         | Nie          |
| br            | Portugalčina (brazílska) | NotoSans-Medium.ttf             | Nie         | Nie          |
| it            | Taliančina           | NotoSans-Medium.ttf               | Nie         | Nie          |
| pl            | Poľština             | NotoSans-Medium.ttf               | Nie         | Nie          |
| tr            | Turečtina            | NotoSans-Medium.ttf               | Nie         | Nie          |
| el            | Gréčtina             | NotoSans-Medium.ttf               | Nie         | Nie          |
| th            | Thajčina             | NotoSansThai-Medium.ttf           | Nie         | Nie          |
| sv            | Švédčina             | NotoSans-Medium.ttf               | Nie         | Nie          |
| da            | Dánčina              | NotoSans-Medium.ttf               | Nie         | Nie          |
| no            | Nórčina              | NotoSans-Medium.ttf               | Nie         | Nie          |
| fi            | Fínčina              | NotoSans-Medium.ttf               | Nie         | Nie          |
| nl            | Holandčina           | NotoSans-Medium.ttf               | Nie         | Nie          |
| he            | Hebrejčina           | NotoSansHebrew-Medium.ttf         | Nie         | Nie          |
| vi            | Vietnamčina          | NotoSans-Medium.ttf               | Nie         | Nie          |
| id            | Indonézština         | NotoSans-Medium.ttf               | Nie         | Nie          |
| ms            | Malajčina            | NotoSans-Medium.ttf               | Nie         | Nie          |
| tl            | Tagalog (filipínčina) | NotoSans-Medium.ttf              | Nie         | Nie          |
| sw            | Swahilčina           | NotoSans-Medium.ttf               | Nie         | Nie          |
| hu            | Maďarčina            | NotoSans-Medium.ttf               | Nie         | Nie          |
| cs            | Čeština              | NotoSans-Medium.ttf               | Nie         | Nie          |
| sk            | Slovenčina           | NotoSans-Medium.ttf               | Nie         | Nie          |
| ro            | Rumunčina            | NotoSans-Medium.ttf               | Nie         | Nie          |
| bg            | Bulharčina           | NotoSans-Medium.ttf               | Nie         | Nie          |
| sr            | Srbčina (cyrilika)   | NotoSans-Medium.ttf               | Nie         | Nie          |
| hr            | Chorvátčina          | NotoSans-Medium.ttf               | Nie         | Nie          |
| sl            | Slovinčina           | NotoSans-Medium.ttf               | Nie         | Nie          |
| uk            | Ukrajinčina          | NotoSans-Medium.ttf               | Nie         | Nie          |
| my            | Barmsčina (Myanmar)  | NotoSans-Medium.ttf               | Nie         | Nie          |

## Pridanie nového jazyka

Ak chcete pridať podporu pre nový jazyk:

1. Prejdite na [src/co_op_translator/fonts/font_language_mappings.yml](https://github.com/Azure/co-op-translator/blob/main/src/co_op_translator/fonts/font_language_mappings.yml).
2. Pridajte kód jazyka, názov a vhodný názov súboru písma. Ak je jazyk pravotočivý, nezabudnite pridať atribút `rtl`.
3. Ak potrebujete použiť nové písmo, overte, či je písmo voľne použiteľné v open-source projektoch, kontrolou licencie a autorských práv. Po overení pridajte súbor písma do priečinka `src/co_op_translator/fonts/`.
4. Lokálne otestujte zmeny, aby ste sa uistili, že nový jazyk je správne podporovaný.
5. Odoslať Pull Request so svojimi zmenami a v popise PR uveďte pridanie nového jazyka.

Príklad:

```yaml
new_lang:
  name: "New Language"
  font: "NotoSans-Medium.ttf"
  rtl: false
```

**Vyhlásenie o zodpovednosti**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, berte prosím na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Originálny dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre dôležité informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.