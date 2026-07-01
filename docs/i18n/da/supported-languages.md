# Understøttede sprog

Co-op Translator understøtter følgende sprogkoder til tekst-, notebook- og billedoversættelsesoutput.

Hvis du vil tilføje et nyt sprog, opdater sprog- og skrifttypekortlægningerne under `src/co_op_translator/fonts/` og test sproget, før du åbner en pull request.

| Language Code | Language Name | Font | RTL Support | Known Issues |
| --- | --- | --- | --- | --- |
| en | Engelsk | NotoSans-Medium.ttf | Nej | Nej |
| fr | Fransk | NotoSans-Medium.ttf | Nej | Nej |
| es | Spansk | NotoSans-Medium.ttf | Nej | Nej |
| de | Tysk | NotoSans-Medium.ttf | Nej | Nej |
| ru | Russisk | NotoSans-Medium.ttf | Nej | Nej |
| ar | Arabisk | NotoSansArabic-Medium.ttf | Ja | Nej |
| fa | Persisk (Farsi) | NotoSansArabic-Medium.ttf | Ja | Nej |
| ur | Urdu | NotoSansArabic-Medium.ttf | Ja | Nej |
| zh-CN | Kinesisk (forenklet) | NotoSansCJK-Medium.ttc | Nej | Nej |
| zh-MO | Kinesisk (traditionel, Macau) | NotoSansCJK-Medium.ttc | Nej | Nej |
| zh-HK | Kinesisk (traditionel, Hongkong) | NotoSansCJK-Medium.ttc | Nej | Nej |
| zh-TW | Kinesisk (traditionel, Taiwan) | NotoSansCJK-Medium.ttc | Nej | Nej |
| ja | Japansk | NotoSansCJK-Medium.ttc | Nej | Nej |
| ko | Koreansk | NotoSansCJK-Medium.ttc | Nej | Nej |
| hi | Hindi | NotoSansDevanagari-Medium.ttf | Nej | Nej |
| bn | Bengalsk | NotoSansBengali-Medium.ttf | Nej | Nej |
| mr | Marathi | NotoSansDevanagari-Medium.ttf | Nej | Nej |
| ne | Nepalesisk | NotoSansDevanagari-Medium.ttf | Nej | Nej |
| pa | Punjabi (Gurmukhi) | NotoSansGurmukhi-Medium.ttf | Nej | Nej |
| pt-PT | Portugisisk (Portugal) | NotoSans-Medium.ttf | Nej | Nej |
| pt-BR | Portugisisk (Brasilien) | NotoSans-Medium.ttf | Nej | Nej |
| it | Italiensk | NotoSans-Medium.ttf | Nej | Nej |
| lt | Litauisk | NotoSans-Medium.ttf | Nej | Nej |
| pl | Polsk | NotoSans-Medium.ttf | Nej | Nej |
| tr | Tyrkisk | NotoSans-Medium.ttf | Nej | Nej |
| el | Græsk | NotoSans-Medium.ttf | Nej | Nej |
| th | Thai | NotoSansThai-Medium.ttf | Nej | Nej |
| sv | Svensk | NotoSans-Medium.ttf | Nej | Nej |
| da | Dansk | NotoSans-Medium.ttf | Nej | Nej |
| no | Norsk | NotoSans-Medium.ttf | Nej | Nej |
| fi | Finsk | NotoSans-Medium.ttf | Nej | Nej |
| nl | Hollandsk | NotoSans-Medium.ttf | Nej | Nej |
| he | Hebraisk | NotoSansHebrew-Medium.ttf | Ja | Nej |
| vi | Vietnamesisk | NotoSans-Medium.ttf | Nej | Nej |
| id | Indonesisk | NotoSans-Medium.ttf | Nej | Nej |
| ms | Malaysisk | NotoSans-Medium.ttf | Nej | Nej |
| tl | Tagalog (Filippinsk) | NotoSans-Medium.ttf | Nej | Nej |
| sw | Swahili | NotoSans-Medium.ttf | Nej | Nej |
| hu | Ungarsk | NotoSans-Medium.ttf | Nej | Nej |
| cs | Tjekkisk | NotoSans-Medium.ttf | Nej | Nej |
| sk | Slovakisk | NotoSans-Medium.ttf | Nej | Nej |
| ro | Rumænsk | NotoSans-Medium.ttf | Nej | Nej |
| bg | Bulgarsk | NotoSans-Medium.ttf | Nej | Nej |
| sr | Serbisk (kyrillisk) | NotoSans-Medium.ttf | Nej | Nej |
| hr | Kroatisk | NotoSans-Medium.ttf | Nej | Nej |
| sl | Slovensk | NotoSans-Medium.ttf | Nej | Nej |
| uk | Ukrainsk | NotoSans-Medium.ttf | Nej | Nej |
| my | Burmesisk (Myanmar) | NotoSansMyanmar-Medium.ttf | Nej | Nej |
| ta | Tamil | NotoSansTamil-Medium.ttf | Nej | Nej |
| et | Estisk | NotoSans-Medium.ttf | Nej | Nej |
| pcm | Nigeriansk Pidgin | NotoSans-Medium.ttf | Nej | Nej |
| te | Telugu | NotoSans-Medium.ttf | Nej | Nej |
| ml | Malayalam | NotoSans-Medium.ttf | Nej | Nej |
| kn | Kannada | NotoSans-Medium.ttf | Nej | Nej |
| km | Khmer | NotoSansKhmer-Medium.ttf | Nej | Nej |

## Tilføj et sprog

For at tilføje understøttelse af et nyt sprog:

1. Tilføj sprogkoden og visningsnavnet til sprogværktøjerne.
2. Tilføj eller kortlæg en skrifttype i `src/co_op_translator/fonts/font_language_mappings.yml`.
3. Test Markdown- og billedoversættelsesoutput.
4. Åbn en pull request med kortlægningen og valideringsnoterne.