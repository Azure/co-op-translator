# Podporované jazyky

Co-op Translator podporuje následující kódy jazyků pro překlad textu, notebooků a obrázků.

Pokud chcete přidat nový jazyk, aktualizujte mapování jazyků a písem ve složce `src/co_op_translator/fonts/` a otestujte jazyk před otevřením pull requestu.

| Language Code | Language Name | Font | RTL Support | Known Issues |
| --- | --- | --- | --- | --- |
| en | angličtina | NotoSans-Medium.ttf | Ne | Ne |
| fr | francouzština | NotoSans-Medium.ttf | Ne | Ne |
| es | španělština | NotoSans-Medium.ttf | Ne | Ne |
| de | němčina | NotoSans-Medium.ttf | Ne | Ne |
| ru | ruština | NotoSans-Medium.ttf | Ne | Ne |
| ar | arabština | NotoSansArabic-Medium.ttf | Ano | Ne |
| fa | perština (Farsi) | NotoSansArabic-Medium.ttf | Ano | Ne |
| ur | urdština | NotoSansArabic-Medium.ttf | Ano | Ne |
| zh-CN | čínština (zjednodušená) | NotoSansCJK-Medium.ttc | Ne | Ne |
| zh-MO | čínština (tradiční, Macau) | NotoSansCJK-Medium.ttc | Ne | Ne |
| zh-HK | čínština (tradiční, Hong Kong) | NotoSansCJK-Medium.ttc | Ne | Ne |
| zh-TW | čínština (tradiční, Taiwan) | NotoSansCJK-Medium.ttc | Ne | Ne |
| ja | japonština | NotoSansCJK-Medium.ttc | Ne | Ne |
| ko | korejština | NotoSansCJK-Medium.ttc | Ne | Ne |
| hi | hindština | NotoSansDevanagari-Medium.ttf | Ne | Ne |
| bn | bengálština | NotoSansBengali-Medium.ttf | Ne | Ne |
| mr | maráthština | NotoSansDevanagari-Medium.ttf | Ne | Ne |
| ne | nepálština | NotoSansDevanagari-Medium.ttf | Ne | Ne |
| pa | paňdžábština (Gurmukhi) | NotoSansGurmukhi-Medium.ttf | Ne | Ne |
| pt-PT | portugalština (Portugalsko) | NotoSans-Medium.ttf | Ne | Ne |
| pt-BR | portugalština (Brazílie) | NotoSans-Medium.ttf | Ne | Ne |
| it | italština | NotoSans-Medium.ttf | Ne | Ne |
| lt | litevština | NotoSans-Medium.ttf | Ne | Ne |
| pl | polština | NotoSans-Medium.ttf | Ne | Ne |
| tr | turečtina | NotoSans-Medium.ttf | Ne | Ne |
| el | řečtina | NotoSans-Medium.ttf | Ne | Ne |
| th | thajština | NotoSansThai-Medium.ttf | Ne | Ne |
| sv | švédština | NotoSans-Medium.ttf | Ne | Ne |
| da | dánština | NotoSans-Medium.ttf | Ne | Ne |
| no | norština | NotoSans-Medium.ttf | Ne | Ne |
| fi | finština | NotoSans-Medium.ttf | Ne | Ne |
| nl | holandština | NotoSans-Medium.ttf | Ne | Ne |
| he | hebrejština | NotoSansHebrew-Medium.ttf | Ano | Ne |
| vi | vietnamština | NotoSans-Medium.ttf | Ne | Ne |
| id | indonéština | NotoSans-Medium.ttf | Ne | Ne |
| ms | malajština | NotoSans-Medium.ttf | Ne | Ne |
| tl | tagalog (filipínština) | NotoSans-Medium.ttf | Ne | Ne |
| sw | svahilština | NotoSans-Medium.ttf | Ne | Ne |
| hu | maďarština | NotoSans-Medium.ttf | Ne | Ne |
| cs | čeština | NotoSans-Medium.ttf | Ne | Ne |
| sk | slovenština | NotoSans-Medium.ttf | Ne | Ne |
| ro | rumunština | NotoSans-Medium.ttf | Ne | Ne |
| bg | bulharština | NotoSans-Medium.ttf | Ne | Ne |
| sr | srbština (cyrilice) | NotoSans-Medium.ttf | Ne | Ne |
| hr | chorvatština | NotoSans-Medium.ttf | Ne | Ne |
| sl | slovinština | NotoSans-Medium.ttf | Ne | Ne |
| uk | ukrajinština | NotoSans-Medium.ttf | Ne | Ne |
| my | barmsky (Myanmar) | NotoSansMyanmar-Medium.ttf | Ne | Ne |
| ta | tamilština | NotoSansTamil-Medium.ttf | Ne | Ne |
| et | estonština | NotoSans-Medium.ttf | Ne | Ne |
| pcm | nigerijský pidžin | NotoSans-Medium.ttf | Ne | Ne |
| te | telugština | NotoSans-Medium.ttf | Ne | Ne |
| ml | malajálam | NotoSans-Medium.ttf | Ne | Ne |
| kn | kannadština | NotoSans-Medium.ttf | Ne | Ne |
| km | khmerština | NotoSansKhmer-Medium.ttf | Ne | Ne |

## Přidání jazyka

Chcete-li přidat podporu pro nový jazyk:

1. Přidejte kód jazyka a zobrazený název do nástrojů pro jazyky.
2. Přidejte nebo namapujte písmo v `src/co_op_translator/fonts/font_language_mappings.yml`.
3. Otestujte výstup překladu Markdownu a obrázků.
4. Otevřete pull request s mapováním a poznámkami o ověření.