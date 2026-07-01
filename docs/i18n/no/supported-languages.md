# Støttede språk

Co-op Translator støtter følgende språkkoder for tekst-, notatbok- og bildeoversettelser.

Hvis du vil legge til et nytt språk, oppdater språk- og fontkartleggingene under `src/co_op_translator/fonts/` og test språket før du åpner en pull request.

| Språkkode | Språknavn | Font | Støtte for RTL | Kjente problemer |
| --- | --- | --- | --- | --- |
| en | Engelsk | NotoSans-Medium.ttf | Nei | Nei |
| fr | Fransk | NotoSans-Medium.ttf | Nei | Nei |
| es | Spansk | NotoSans-Medium.ttf | Nei | Nei |
| de | Tysk | NotoSans-Medium.ttf | Nei | Nei |
| ru | Russisk | NotoSans-Medium.ttf | Nei | Nei |
| ar | Arabisk | NotoSansArabic-Medium.ttf | Ja | Nei |
| fa | Persisk (Farsi) | NotoSansArabic-Medium.ttf | Ja | Nei |
| ur | Urdu | NotoSansArabic-Medium.ttf | Ja | Nei |
| zh-CN | Kinesisk (forenklet) | NotoSansCJK-Medium.ttc | Nei | Nei |
| zh-MO | Kinesisk (tradisjonell, Macau) | NotoSansCJK-Medium.ttc | Nei | Nei |
| zh-HK | Kinesisk (tradisjonell, Hongkong) | NotoSansCJK-Medium.ttc | Nei | Nei |
| zh-TW | Kinesisk (tradisjonell, Taiwan) | NotoSansCJK-Medium.ttc | Nei | Nei |
| ja | Japansk | NotoSansCJK-Medium.ttc | Nei | Nei |
| ko | Koreansk | NotoSansCJK-Medium.ttc | Nei | Nei |
| hi | Hindi | NotoSansDevanagari-Medium.ttf | Nei | Nei |
| bn | Bengali | NotoSansBengali-Medium.ttf | Nei | Nei |
| mr | Marathi | NotoSansDevanagari-Medium.ttf | Nei | Nei |
| ne | Nepali | NotoSansDevanagari-Medium.ttf | Nei | Nei |
| pa | Punjabi (Gurmukhi) | NotoSansGurmukhi-Medium.ttf | Nei | Nei |
| pt-PT | Portugisisk (Portugal) | NotoSans-Medium.ttf | Nei | Nei |
| pt-BR | Portugisisk (Brasil) | NotoSans-Medium.ttf | Nei | Nei |
| it | Italiensk | NotoSans-Medium.ttf | Nei | Nei |
| lt | Litauisk | NotoSans-Medium.ttf | Nei | Nei |
| pl | Polsk | NotoSans-Medium.ttf | Nei | Nei |
| tr | Tyrkisk | NotoSans-Medium.ttf | Nei | Nei |
| el | Gresk | NotoSans-Medium.ttf | Nei | Nei |
| th | Thailandsk | NotoSansThai-Medium.ttf | Nei | Nei |
| sv | Svensk | NotoSans-Medium.ttf | Nei | Nei |
| da | Dansk | NotoSans-Medium.ttf | Nei | Nei |
| no | Norsk | NotoSans-Medium.ttf | Nei | Nei |
| fi | Finsk | NotoSans-Medium.ttf | Nei | Nei |
| nl | Nederlandsk | NotoSans-Medium.ttf | Nei | Nei |
| he | Hebraisk | NotoSansHebrew-Medium.ttf | Ja | Nei |
| vi | Vietnamesisk | NotoSans-Medium.ttf | Nei | Nei |
| id | Indonesisk | NotoSans-Medium.ttf | Nei | Nei |
| ms | Malayisk | NotoSans-Medium.ttf | Nei | Nei |
| tl | Tagalog (Filipino) | NotoSans-Medium.ttf | Nei | Nei |
| sw | Swahili | NotoSans-Medium.ttf | Nei | Nei |
| hu | Ungarsk | NotoSans-Medium.ttf | Nei | Nei |
| cs | Tsjekkisk | NotoSans-Medium.ttf | Nei | Nei |
| sk | Slovakisk | NotoSans-Medium.ttf | Nei | Nei |
| ro | Rumensk | NotoSans-Medium.ttf | Nei | Nei |
| bg | Bulgarsk | NotoSans-Medium.ttf | Nei | Nei |
| sr | Serbisk (kyrillisk) | NotoSans-Medium.ttf | Nei | Nei |
| hr | Kroatisk | NotoSans-Medium.ttf | Nei | Nei |
| sl | Slovensk | NotoSans-Medium.ttf | Nei | Nei |
| uk | Ukrainsk | NotoSans-Medium.ttf | Nei | Nei |
| my | Burmesisk (Myanmar) | NotoSansMyanmar-Medium.ttf | Nei | Nei |
| ta | Tamil | NotoSansTamil-Medium.ttf | Nei | Nei |
| et | Estisk | NotoSans-Medium.ttf | Nei | Nei |
| pcm | Nigeriansk pidgin | NotoSans-Medium.ttf | Nei | Nei |
| te | Telugu | NotoSans-Medium.ttf | Nei | Nei |
| ml | Malayalam | NotoSans-Medium.ttf | Nei | Nei |
| kn | Kannada | NotoSans-Medium.ttf | Nei | Nei |
| km | Khmer | NotoSansKhmer-Medium.ttf | Nei | Nei |

## Legg til et språk

For å legge til støtte for et nytt språk:

1. Legg til språkkoden og visningsnavnet i språkverktøyene.
2. Legg til eller tilordne en font i `src/co_op_translator/fonts/font_language_mappings.yml`.
3. Test Markdown- og bildeoversettelsesutdata.
4. Åpne en pull request med kartleggingen og valideringsnotater.