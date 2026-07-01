# Podprti jeziki

Co-op Translator podpira naslednje kode jezikov za besedilo, beležnico (notebook) in izhode prevoda slik.

Če želite dodati nov jezik, posodobite jezikovne in pisavne preslikave v `src/co_op_translator/fonts/` in preizkusite jezik, preden odprete pull request.

| Language Code | Language Name | Font | RTL Support | Known Issues |
| --- | --- | --- | --- | --- |
| en | Angleščina | NotoSans-Medium.ttf | Ne | Ne |
| fr | Francoščina | NotoSans-Medium.ttf | Ne | Ne |
| es | Španščina | NotoSans-Medium.ttf | Ne | Ne |
| de | Nemščina | NotoSans-Medium.ttf | Ne | Ne |
| ru | Ruščina | NotoSans-Medium.ttf | Ne | Ne |
| ar | Arabščina | NotoSansArabic-Medium.ttf | Da | Ne |
| fa | Perzijščina (Farsi) | NotoSansArabic-Medium.ttf | Da | Ne |
| ur | Urdu | NotoSansArabic-Medium.ttf | Da | Ne |
| zh-CN | Kitajščina (poenostavljena) | NotoSansCJK-Medium.ttc | Ne | Ne |
| zh-MO | Kitajščina (tradicionalna, Macau) | NotoSansCJK-Medium.ttc | Ne | Ne |
| zh-HK | Kitajščina (tradicionalna, Hong Kong) | NotoSansCJK-Medium.ttc | Ne | Ne |
| zh-TW | Kitajščina (tradicionalna, Taiwan) | NotoSansCJK-Medium.ttc | Ne | Ne |
| ja | Japonščina | NotoSansCJK-Medium.ttc | Ne | Ne |
| ko | Korejščina | NotoSansCJK-Medium.ttc | Ne | Ne |
| hi | Hindijščina | NotoSansDevanagari-Medium.ttf | Ne | Ne |
| bn | Bengalščina | NotoSansBengali-Medium.ttf | Ne | Ne |
| mr | Maratščina | NotoSansDevanagari-Medium.ttf | Ne | Ne |
| ne | Nepalščina | NotoSansDevanagari-Medium.ttf | Ne | Ne |
| pa | Pandžabščina (Gurmukhi) | NotoSansGurmukhi-Medium.ttf | Ne | Ne |
| pt-PT | Portugalščina (Portugalska) | NotoSans-Medium.ttf | Ne | Ne |
| pt-BR | Portugalščina (Brazilija) | NotoSans-Medium.ttf | Ne | Ne |
| it | Italijanščina | NotoSans-Medium.ttf | Ne | Ne |
| lt | Litovščina | NotoSans-Medium.ttf | Ne | Ne |
| pl | Poljščina | NotoSans-Medium.ttf | Ne | Ne |
| tr | Turščina | NotoSans-Medium.ttf | Ne | Ne |
| el | Grščina | NotoSans-Medium.ttf | Ne | Ne |
| th | Tajščina | NotoSansThai-Medium.ttf | Ne | Ne |
| sv | Švedščina | NotoSans-Medium.ttf | Ne | Ne |
| da | Danščina | NotoSans-Medium.ttf | Ne | Ne |
| no | Norveščina | NotoSans-Medium.ttf | Ne | Ne |
| fi | Finščina | NotoSans-Medium.ttf | Ne | Ne |
| nl | Nizozemščina | NotoSans-Medium.ttf | Ne | Ne |
| he | Hebrejščina | NotoSansHebrew-Medium.ttf | Da | Ne |
| vi | Vietnamščina | NotoSans-Medium.ttf | Ne | Ne |
| id | Indonezijščina | NotoSans-Medium.ttf | Ne | Ne |
| ms | Malajščina | NotoSans-Medium.ttf | Ne | Ne |
| tl | Tagalog (filipinščina) | NotoSans-Medium.ttf | Ne | Ne |
| sw | Svahili | NotoSans-Medium.ttf | Ne | Ne |
| hu | Madžarščina | NotoSans-Medium.ttf | Ne | Ne |
| cs | Češčina | NotoSans-Medium.ttf | Ne | Ne |
| sk | Slovaščina | NotoSans-Medium.ttf | Ne | Ne |
| ro | Romunščina | NotoSans-Medium.ttf | Ne | Ne |
| bg | Bolgarščina | NotoSans-Medium.ttf | Ne | Ne |
| sr | Srbščina (Cirilica) | NotoSans-Medium.ttf | Ne | Ne |
| hr | Hrvaščina | NotoSans-Medium.ttf | Ne | Ne |
| sl | Slovenščina | NotoSans-Medium.ttf | Ne | Ne |
| uk | Ukrajinščina | NotoSans-Medium.ttf | Ne | Ne |
| my | Burmanščina (Myanmar) | NotoSansMyanmar-Medium.ttf | Ne | Ne |
| ta | Tamilščina | NotoSansTamil-Medium.ttf | Ne | Ne |
| et | Estonščina | NotoSans-Medium.ttf | Ne | Ne |
| pcm | Nigerijski pidgin | NotoSans-Medium.ttf | Ne | Ne |
| te | Telugu | NotoSans-Medium.ttf | Ne | Ne |
| ml | Malajalščina | NotoSans-Medium.ttf | Ne | Ne |
| kn | Kannada | NotoSans-Medium.ttf | Ne | Ne |
| km | Khmerščina | NotoSansKhmer-Medium.ttf | Ne | Ne |

## Add a Language

To add support for a new language:

1. Dodajte kodo jezika in prikazno ime v jezikovne pripomočke.
2. Dodajte ali preslikajte pisavo v `src/co_op_translator/fonts/font_language_mappings.yml`.
3. Preizkusite izhod prevoda Markdowna in slik.
4. Odprite pull request z mapiranjem in opombami o validaciji.