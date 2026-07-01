# Stödda språk

Co-op Translator stöder följande språkkoder för text-, notebook- och bildöversättningsutdata.

Om du vill lägga till ett nytt språk, uppdatera språk- och fontmappningarna under `src/co_op_translator/fonts/` och testa språket innan du öppnar en pull request.

| Language Code | Language Name | Font | RTL Support | Known Issues |
| --- | --- | --- | --- | --- |
| en | Engelska | NotoSans-Medium.ttf | Nej | Nej |
| fr | Franska | NotoSans-Medium.ttf | Nej | Nej |
| es | Spanska | NotoSans-Medium.ttf | Nej | Nej |
| de | Tyska | NotoSans-Medium.ttf | Nej | Nej |
| ru | Ryska | NotoSans-Medium.ttf | Nej | Nej |
| ar | Arabiska | NotoSansArabic-Medium.ttf | Ja | Nej |
| fa | Persiska (Farsi) | NotoSansArabic-Medium.ttf | Ja | Nej |
| ur | Urdu | NotoSansArabic-Medium.ttf | Ja | Nej |
| zh-CN | Kinesiska (förenklad) | NotoSansCJK-Medium.ttc | Nej | Nej |
| zh-MO | Kinesiska (traditionell, Macau) | NotoSansCJK-Medium.ttc | Nej | Nej |
| zh-HK | Kinesiska (traditionell, Hong Kong) | NotoSansCJK-Medium.ttc | Nej | Nej |
| zh-TW | Kinesiska (traditionell, Taiwan) | NotoSansCJK-Medium.ttc | Nej | Nej |
| ja | Japanska | NotoSansCJK-Medium.ttc | Nej | Nej |
| ko | Koreanska | NotoSansCJK-Medium.ttc | Nej | Nej |
| hi | Hindi | NotoSansDevanagari-Medium.ttf | Nej | Nej |
| bn | Bengali | NotoSansBengali-Medium.ttf | Nej | Nej |
| mr | Marathi | NotoSansDevanagari-Medium.ttf | Nej | Nej |
| ne | Nepali | NotoSansDevanagari-Medium.ttf | Nej | Nej |
| pa | Punjabi (Gurmukhi) | NotoSansGurmukhi-Medium.ttf | Nej | Nej |
| pt-PT | Portugisiska (Portugal) | NotoSans-Medium.ttf | Nej | Nej |
| pt-BR | Portugisiska (Brasilien) | NotoSans-Medium.ttf | Nej | Nej |
| it | Italienska | NotoSans-Medium.ttf | Nej | Nej |
| lt | Litauiska | NotoSans-Medium.ttf | Nej | Nej |
| pl | Polska | NotoSans-Medium.ttf | Nej | Nej |
| tr | Turkiska | NotoSans-Medium.ttf | Nej | Nej |
| el | Grekiska | NotoSans-Medium.ttf | Nej | Nej |
| th | Thailändska | NotoSansThai-Medium.ttf | Nej | Nej |
| sv | Svenska | NotoSans-Medium.ttf | Nej | Nej |
| da | Danska | NotoSans-Medium.ttf | Nej | Nej |
| no | Norska | NotoSans-Medium.ttf | Nej | Nej |
| fi | Finska | NotoSans-Medium.ttf | Nej | Nej |
| nl | Nederländska | NotoSans-Medium.ttf | Nej | Nej |
| he | Hebreiska | NotoSansHebrew-Medium.ttf | Ja | Nej |
| vi | Vietnamesiska | NotoSans-Medium.ttf | Nej | Nej |
| id | Indonesiska | NotoSans-Medium.ttf | Nej | Nej |
| ms | Malaysiska | NotoSans-Medium.ttf | Nej | Nej |
| tl | Tagalog (Filippinska) | NotoSans-Medium.ttf | Nej | Nej |
| sw | Swahili | NotoSans-Medium.ttf | Nej | Nej |
| hu | Ungerska | NotoSans-Medium.ttf | Nej | Nej |
| cs | Tjeckiska | NotoSans-Medium.ttf | Nej | Nej |
| sk | Slovakiska | NotoSans-Medium.ttf | Nej | Nej |
| ro | Rumänska | NotoSans-Medium.ttf | Nej | Nej |
| bg | Bulgariska | NotoSans-Medium.ttf | Nej | Nej |
| sr | Serbiska (kyrilliska) | NotoSans-Medium.ttf | Nej | Nej |
| hr | Kroatiska | NotoSans-Medium.ttf | Nej | Nej |
| sl | Slovenska | NotoSans-Medium.ttf | Nej | Nej |
| uk | Ukrainska | NotoSans-Medium.ttf | Nej | Nej |
| my | Burmesiska (Myanmar) | NotoSansMyanmar-Medium.ttf | Nej | Nej |
| ta | Tamil | NotoSansTamil-Medium.ttf | Nej | Nej |
| et | Estniska | NotoSans-Medium.ttf | Nej | Nej |
| pcm | Nigeriansk Pidgin | NotoSans-Medium.ttf | Nej | Nej |
| te | Telugu | NotoSans-Medium.ttf | Nej | Nej |
| ml | Malayalam | NotoSans-Medium.ttf | Nej | Nej |
| kn | Kannada | NotoSans-Medium.ttf | Nej | Nej |
| km | Khmer | NotoSansKhmer-Medium.ttf | Nej | Nej |

## Lägg till ett språk

För att lägga till stöd för ett nytt språk:

1. Lägg till språkkoden och visningsnamnet i språkverktygen.
2. Lägg till eller mappa en font i `src/co_op_translator/fonts/font_language_mappings.yml`.
3. Testa Markdown- och bildöversättningsutdata.
4. Öppna en pull request med mappningen och valideringsanteckningarna.