# Podporované jazyky

Co-op Translator podporuje nasledujúce kódy jazykov pre výstupy prekladu textu, poznámkových blokov a obrázkov.

Ak chcete pridať nový jazyk, aktualizujte mapovania jazyka a fontu v priečinku `src/co_op_translator/fonts/` a otestujte jazyk pred otvorením pull requestu.

| Kód jazyka | Názov jazyka | Písmo | Podpora RTL | Známe problémy |
| --- | --- | --- | --- | --- |
| en | Angličtina | NotoSans-Medium.ttf | Nie | Nie |
| fr | Francúzština | NotoSans-Medium.ttf | Nie | Nie |
| es | Španielčina | NotoSans-Medium.ttf | Nie | Nie |
| de | Nemčina | NotoSans-Medium.ttf | Nie | Nie |
| ru | Ruština | NotoSans-Medium.ttf | Nie | Nie |
| ar | Arabčina | NotoSansArabic-Medium.ttf | Áno | Nie |
| fa | Perzština (fársí) | NotoSansArabic-Medium.ttf | Áno | Nie |
| ur | Urdčina | NotoSansArabic-Medium.ttf | Áno | Nie |
| zh-CN | Čínština (zjednodušená) | NotoSansCJK-Medium.ttc | Nie | Nie |
| zh-MO | Čínština (tradičná, Macao) | NotoSansCJK-Medium.ttc | Nie | Nie |
| zh-HK | Čínština (tradičná, Hongkong) | NotoSansCJK-Medium.ttc | Nie | Nie |
| zh-TW | Čínština (tradičná, Taiwan) | NotoSansCJK-Medium.ttc | Nie | Nie |
| ja | Japončina | NotoSansCJK-Medium.ttc | Nie | Nie |
| ko | Kórejčina | NotoSansCJK-Medium.ttc | Nie | Nie |
| hi | Hindčina | NotoSansDevanagari-Medium.ttf | Nie | Nie |
| bn | Bengálčina | NotoSansBengali-Medium.ttf | Nie | Nie |
| mr | Maráthčina | NotoSansDevanagari-Medium.ttf | Nie | Nie |
| ne | Nepálčina | NotoSansDevanagari-Medium.ttf | Nie | Nie |
| pa | Pandžábčina (Gurmukhi) | NotoSansGurmukhi-Medium.ttf | Nie | Nie |
| pt-PT | Portugalčina (Portugalsko) | NotoSans-Medium.ttf | Nie | Nie |
| pt-BR | Portugalčina (Brazília) | NotoSans-Medium.ttf | Nie | Nie |
| it | Taliančina | NotoSans-Medium.ttf | Nie | Nie |
| lt | Litovčina | NotoSans-Medium.ttf | Nie | Nie |
| pl | Poľština | NotoSans-Medium.ttf | Nie | Nie |
| tr | Turečtina | NotoSans-Medium.ttf | Nie | Nie |
| el | Gréčtina | NotoSans-Medium.ttf | Nie | Nie |
| th | Thajčina | NotoSansThai-Medium.ttf | Nie | Nie |
| sv | Švédčina | NotoSans-Medium.ttf | Nie | Nie |
| da | Dánčina | NotoSans-Medium.ttf | Nie | Nie |
| no | Nórčina | NotoSans-Medium.ttf | Nie | Nie |
| fi | Fínčina | NotoSans-Medium.ttf | Nie | Nie |
| nl | Nízozemčina | NotoSans-Medium.ttf | Nie | Nie |
| he | Hebrejčina | NotoSansHebrew-Medium.ttf | Áno | Nie |
| vi | Vietnamčina | NotoSans-Medium.ttf | Nie | Nie |
| id | Indonézština | NotoSans-Medium.ttf | Nie | Nie |
| ms | Malajčina | NotoSans-Medium.ttf | Nie | Nie |
| tl | Tagalog (Filipínčina) | NotoSans-Medium.ttf | Nie | Nie |
| sw | Svahilčina | NotoSans-Medium.ttf | Nie | Nie |
| hu | Maďarčina | NotoSans-Medium.ttf | Nie | Nie |
| cs | Čeština | NotoSans-Medium.ttf | Nie | Nie |
| sk | Slovenčina | NotoSans-Medium.ttf | Nie | Nie |
| ro | Rumunčina | NotoSans-Medium.ttf | Nie | Nie |
| bg | Bulharčina | NotoSans-Medium.ttf | Nie | Nie |
| sr | Srbčina (cyrilika) | NotoSans-Medium.ttf | Nie | Nie |
| hr | Chorvátčina | NotoSans-Medium.ttf | Nie | Nie |
| sl | Slovinčina | NotoSans-Medium.ttf | Nie | Nie |
| uk | Ukrajinčina | NotoSans-Medium.ttf | Nie | Nie |
| my | Burmčina (Myanmar) | NotoSansMyanmar-Medium.ttf | Nie | Nie |
| ta | Tamilčina | NotoSansTamil-Medium.ttf | Nie | Nie |
| et | Estónčina | NotoSans-Medium.ttf | Nie | Nie |
| pcm | Nigérijský pidžin | NotoSans-Medium.ttf | Nie | Nie |
| te | Telugčina | NotoSans-Medium.ttf | Nie | Nie |
| ml | Malajálamčina | NotoSans-Medium.ttf | Nie | Nie |
| kn | Kannadčina | NotoSans-Medium.ttf | Nie | Nie |
| km | Khmerčina | NotoSansKhmer-Medium.ttf | Nie | Nie |

## Pridať jazyk

Ak chcete pridať podporu pre nový jazyk:

1. Pridajte kód jazyka a zobrazovaný názov do jazykových utilít.
2. Pridajte alebo namapujte písmo v `src/co_op_translator/fonts/font_language_mappings.yml`.
3. Otestujte výstup prekladu Markdownu a obrázkov.
4. Otvorte pull request s mapovaním a poznámkami o overení.