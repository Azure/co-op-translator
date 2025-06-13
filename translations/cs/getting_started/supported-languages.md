<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b4ed48f23ec418b31e90a02fe629fcde",
  "translation_date": "2025-06-12T12:17:32+00:00",
  "source_file": "getting_started/supported-languages.md",
  "language_code": "cs"
}
-->
# Podporované jazyky

Tabulka níže uvádí jazyky, které jsou aktuálně podporovány **Co-op Translator**. Obsahuje kódy jazyků, názvy jazyků a známé problémy spojené s jednotlivými jazyky. Pokud chcete přidat podporu pro nový jazyk, přidejte odpovídající kód jazyka, název a vhodné písmo do souboru `font_language_mappings.yml` umístěného v `src/co_op_translator/fonts/` a po otestování odešlete pull request.

| Language Code | Language Name        | Font                              | RTL Support | Known Issues |
|---------------|----------------------|-----------------------------------|-------------|--------------|
| en            | Angličtina           | NotoSans-Medium.ttf               | Ne          | Ne           |
| fr            | Francouzština        | NotoSans-Medium.ttf               | Ne          | Ne           |
| es            | Španělština          | NotoSans-Medium.ttf               | Ne          | Ne           |
| de            | Němčina              | NotoSans-Medium.ttf               | Ne          | Ne           |
| ru            | Ruština              | NotoSans-Medium.ttf               | Ne          | Ne           |
| ar            | Arabština            | NotoSansArabic-Medium.ttf         | Ano         | Ne           |
| fa            | Perština (Fársí)     | NotoSansArabic-Medium.ttf         | Ne          | Ne           |
| ur            | Urdu                 | NotoSansArabic-Medium.ttf         | Ne          | Ne           |
| zh            | Čínština (zjednodušená) | NotoSansCJK-Medium.ttc          | Ne          | Ne           |
| mo            | Čínština (tradiční, Macau) | NotoSansCJK-Medium.ttc       | Ne          | Ne           |
| hk            | Čínština (tradiční, Hong Kong) | NotoSansCJK-Medium.ttc    | Ne          | Ne           |
| tw            | Čínština (tradiční, Taiwan) | NotoSansCJK-Medium.ttc        | Ne          | Ne           |
| ja            | Japonština           | NotoSansCJK-Medium.ttc            | Ne          | Ne           |
| ko            | Korejština           | NotoSansCJK-Medium.ttc            | Ne          | Ne           |
| hi            | Hindština            | NotoSansDevanagari-Medium.ttf     | Ne          | Ne           |
| bn            | Bengálština          | NotoSansBengali-Medium.ttf        | Ne          | Ne           |
| mr            | Maráthština          | NotoSansDevanagari-Medium.ttf     | Ne          | Ne           |
| ne            | Nepálština           | NotoSansDevanagari-Medium.ttf     | Ne          | Ne           |
| pa            | Paňdžábština (Gurmukhi) | NotoSansGurmukhi-Medium.ttf    | Ne          | Ne           |
| pt            | Portugalština        | NotoSans-Medium.ttf               | Ne          | Ne           |
| br            | Brazilská portugalština | NotoSans-Medium.ttf             | Ne          | Ne           |
| it            | Italština            | NotoSans-Medium.ttf               | Ne          | Ne           |
| pl            | Polština             | NotoSans-Medium.ttf               | Ne          | Ne           |
| tr            | Turečtina            | NotoSans-Medium.ttf               | Ne          | Ne           |
| el            | Řečtina              | NotoSans-Medium.ttf               | Ne          | Ne           |
| th            | Thajština            | NotoSansThai-Medium.ttf           | Ne          | Ne           |
| sv            | Švédština            | NotoSans-Medium.ttf               | Ne          | Ne           |
| da            | Dánština             | NotoSans-Medium.ttf               | Ne          | Ne           |
| no            | Norština             | NotoSans-Medium.ttf               | Ne          | Ne           |
| fi            | Finština             | NotoSans-Medium.ttf               | Ne          | Ne           |
| nl            | Nizozemština         | NotoSans-Medium.ttf               | Ne          | Ne           |
| he            | Hebrejština          | NotoSansHebrew-Medium.ttf         | Ne          | Ne           |
| vi            | Vietnamština         | NotoSans-Medium.ttf               | Ne          | Ne           |
| id            | Indonéština          | NotoSans-Medium.ttf               | Ne          | Ne           |
| ms            | Malajština           | NotoSans-Medium.ttf               | Ne          | Ne           |
| tl            | Tagalog (Filipínština) | NotoSans-Medium.ttf             | Ne          | Ne           |
| sw            | Svahilština          | NotoSans-Medium.ttf               | Ne          | Ne           |
| hu            | Maďarština           | NotoSans-Medium.ttf               | Ne          | Ne           |
| cs            | Čeština              | NotoSans-Medium.ttf               | Ne          | Ne           |
| sk            | Slovenština          | NotoSans-Medium.ttf               | Ne          | Ne           |
| ro            | Rumunština           | NotoSans-Medium.ttf               | Ne          | Ne           |
| bg            | Bulharština          | NotoSans-Medium.ttf               | Ne          | Ne           |
| sr            | Srbština (cyrilice)  | NotoSans-Medium.ttf               | Ne          | Ne           |
| hr            | Chorvatština         | NotoSans-Medium.ttf               | Ne          | Ne           |
| sl            | Slovinština          | NotoSans-Medium.ttf               | Ne          | Ne           |
| uk            | Ukrajinština         | NotoSans-Medium.ttf               | Ne          | Ne           |
| my            | Barmsky (Myanmar)    | NotoSans-Medium.ttf               | Ne          | Ne           |

## Přidání nového jazyka

Pro přidání podpory nového jazyka:

1. Přejděte na [src/co_op_translator/fonts/font_language_mappings.yml](https://github.com/Azure/co-op-translator/blob/main/src/co_op_translator/fonts/font_language_mappings.yml).
2. Přidejte kód jazyka, název a odpovídající název souboru písma. Nezapomeňte zahrnout atribut `rtl`, pokud je jazyk psán zprava doleva.
3. Pokud potřebujete použít nové písmo, ujistěte se, že je zdarma k použití v open-source projektech, a to kontrolou licenčních a autorských podmínek. Po ověření přidejte soubor písma do adresáře `src/co_op_translator/fonts/`.
4. Lokálně otestujte své změny, aby bylo zajištěno správné fungování nového jazyka.
5. Odešlete Pull Request se svými změnami a ve zprávě PR uveďte přidání nového jazyka.

Příklad:

```yaml
new_lang:
  name: "New Language"
  font: "NotoSans-Medium.ttf"
  rtl: false
```

**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo mylné výklady vyplývající z použití tohoto překladu.