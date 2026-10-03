# Podporované jazyky

Co-op Translator podporuje následující kódy jazyků pro výstupy překladu textu, notebooků a obrázků.

Pokud chcete přidat nový jazyk, aktualizujte mapování jazyka a písma v `src/co_op_translator/fonts/` a otestujte jazyk před otevřením pull requestu.

| Kód jazyka | Název jazyka | Písmo | Podpora RTL | Známé problémy |
| --- | --- | --- | --- | --- |
| en | Angličtina | NotoSans-Medium.ttf | Ne | Ne |
| fr | Francouzština | NotoSans-Medium.ttf | Ne | Ne |
| es | Španělština | NotoSans-Medium.ttf | Ne | Ne |
| de | Němčina | NotoSans-Medium.ttf | Ne | Ne |
| ru | Ruština | NotoSans-Medium.ttf | Ne | Ne |
| ar | Arabština | NotoSansArabic-Medium.ttf | Ano | Ne |
| fa | Perština (fársí) | NotoSansArabic-Medium.ttf | Ano | Ne |
| ur | Urdština | NotoSansArabic-Medium.ttf | Ano | Ne |
| zh-CN | Čínština (zjednodušená) | NotoSansCJK-Medium.ttc | Ne | Ne |
| zh-MO | Čínština (tradiční, Macao) | NotoSansCJK-Medium.ttc | Ne | Ne |
| zh-HK | Čínština (tradiční, Hongkong) | NotoSansCJK-Medium.ttc | Ne | Ne |
| zh-TW | Čínština (tradiční, Tchaj-wan) | NotoSansCJK-Medium.ttc | Ne | Ne |
| ja | Japonština | NotoSansCJK-Medium.ttc | Ne | Ne |
| ko | Korejština | NotoSansCJK-Medium.ttc | Ne | Ne |
| hi | Hindština | NotoSansDevanagari-Medium.ttf | Ne | Ne |
| bn | Bengálština | NotoSansBengali-Medium.ttf | Ne | Ne |
| mr | Maráthština | NotoSansDevanagari-Medium.ttf | Ne | Ne |
| ne | Nepálština | NotoSansDevanagari-Medium.ttf | Ne | Ne |
| pa | Paňdžábština (Gurmukhi) | NotoSansGurmukhi-Medium.ttf | Ne | Ne |
| pt-PT | Portugalština (Portugalsko) | NotoSans-Medium.ttf | Ne | Ne |
| pt-BR | Portugalština (Brazílie) | NotoSans-Medium.ttf | Ne | Ne |
| it | Italština | NotoSans-Medium.ttf | Ne | Ne |
| lt | Litevština | NotoSans-Medium.ttf | Ne | Ne |
| pl | Polština | NotoSans-Medium.ttf | Ne | Ne |
| tr | Turečtina | NotoSans-Medium.ttf | Ne | Ne |
| el | Řečtina | NotoSans-Medium.ttf | Ne | Ne |
| th | Thajština | NotoSansThai-Medium.ttf | Ne | Ne |
| sv | Švédština | NotoSans-Medium.ttf | Ne | Ne |
| da | Dánština | NotoSans-Medium.ttf | Ne | Ne |
| no | Norština | NotoSans-Medium.ttf | Ne | Ne |
| fi | Finština | NotoSans-Medium.ttf | Ne | Ne |
| nl | Nizozemština | NotoSans-Medium.ttf | Ne | Ne |
| he | Hebrejština | NotoSansHebrew-Medium.ttf | Ano | Ne |
| vi | Vietnamština | NotoSans-Medium.ttf | Ne | Ne |
| id | Indonéština | NotoSans-Medium.ttf | Ne | Ne |
| ms | Malajština | NotoSans-Medium.ttf | Ne | Ne |
| tl | Tagalog (filipínština) | NotoSans-Medium.ttf | Ne | Ne |
| sw | Svahilština | NotoSans-Medium.ttf | Ne | Ne |
| hu | Maďarština | NotoSans-Medium.ttf | Ne | Ne |
| cs | Čeština | NotoSans-Medium.ttf | Ne | Ne |
| sk | Slovenština | NotoSans-Medium.ttf | Ne | Ne |
| ro | Rumunština | NotoSans-Medium.ttf | Ne | Ne |
| bg | Bulharština | NotoSans-Medium.ttf | Ne | Ne |
| sr | Srbština (cyrilice) | NotoSans-Medium.ttf | Ne | Ne |
| hr | Chorvatština | NotoSans-Medium.ttf | Ne | Ne |
| sl | Slovinština | NotoSans-Medium.ttf | Ne | Ne |
| uk | Ukrajinština | NotoSans-Medium.ttf | Ne | Ne |
| my | Barmsština (Myanmar) | NotoSansMyanmar-Medium.ttf | Ne | Ne |
| ta | Tamilština | NotoSansTamil-Medium.ttf | Ne | Ne |
| et | Estonština | NotoSans-Medium.ttf | Ne | Ne |
| pcm | Nigérijský pidžin | NotoSans-Medium.ttf | Ne | Ne |
| te | Telugština | NotoSans-Medium.ttf | Ne | Ne |
| ml | Malajálamština | NotoSans-Medium.ttf | Ne | Ne |
| kn | Kannadština | NotoSans-Medium.ttf | Ne | Ne |
| km | Khmerština | NotoSansKhmer-Medium.ttf | Ne | Ne |
| mni | Manipuri (Meitei Mayek) | NotoSansMeeteiMayek-Medium.ttf | Ne | Ne |

## Přidat jazyk

Chcete-li přidat podporu pro nový jazyk:

1. Přidejte kód jazyka a zobrazovaný název do nástrojů pro jazyky.
2. Přidejte nebo mapujte písmo v `src/co_op_translator/fonts/font_language_mappings.yml`.
3. Otestujte výstup překladu Markdownu a obrázků.
4. Otevřete pull request s mapováním a poznámkami o ověření.