# Ondersteunde talen

Co-op Translator ondersteunt de volgende taalcodes voor tekst-, notebook- en afbeeldingsvertalingen.

Als je een nieuwe taal wilt toevoegen, werk dan de taal- en lettertypekoppelingen bij onder `src/co_op_translator/fonts/` en test de taal voordat je een pull request opent.

| Taalcode | Taalnaam | Lettertype | RTL-ondersteuning | Bekende problemen |
| --- | --- | --- | --- | --- |
| en | Engels | NotoSans-Medium.ttf | Nee | Nee |
| fr | Frans | NotoSans-Medium.ttf | Nee | Nee |
| es | Spaans | NotoSans-Medium.ttf | Nee | Nee |
| de | Duits | NotoSans-Medium.ttf | Nee | Nee |
| ru | Russisch | NotoSans-Medium.ttf | Nee | Nee |
| ar | Arabisch | NotoSansArabic-Medium.ttf | Ja | Nee |
| fa | Perzisch (Farsi) | NotoSansArabic-Medium.ttf | Ja | Nee |
| ur | Urdu | NotoSansArabic-Medium.ttf | Ja | Nee |
| zh-CN | Chinees (vereenvoudigd) | NotoSansCJK-Medium.ttc | Nee | Nee |
| zh-MO | Chinees (traditioneel, Macau) | NotoSansCJK-Medium.ttc | Nee | Nee |
| zh-HK | Chinees (traditioneel, Hongkong) | NotoSansCJK-Medium.ttc | Nee | Nee |
| zh-TW | Chinees (traditioneel, Taiwan) | NotoSansCJK-Medium.ttc | Nee | Nee |
| ja | Japans | NotoSansCJK-Medium.ttc | Nee | Nee |
| ko | Koreaans | NotoSansCJK-Medium.ttc | Nee | Nee |
| hi | Hindi | NotoSansDevanagari-Medium.ttf | Nee | Nee |
| bn | Bengaals | NotoSansBengali-Medium.ttf | Nee | Nee |
| mr | Marathi | NotoSansDevanagari-Medium.ttf | Nee | Nee |
| ne | Nepalees | NotoSansDevanagari-Medium.ttf | Nee | Nee |
| pa | Punjabi (Gurmukhi) | NotoSansGurmukhi-Medium.ttf | Nee | Nee |
| pt-PT | Portugees (Portugal) | NotoSans-Medium.ttf | Nee | Nee |
| pt-BR | Portugees (Brazilië) | NotoSans-Medium.ttf | Nee | Nee |
| it | Italiaans | NotoSans-Medium.ttf | Nee | Nee |
| lt | Litouws | NotoSans-Medium.ttf | Nee | Nee |
| pl | Pools | NotoSans-Medium.ttf | Nee | Nee |
| tr | Turks | NotoSans-Medium.ttf | Nee | Nee |
| el | Grieks | NotoSans-Medium.ttf | Nee | Nee |
| th | Thais | NotoSansThai-Medium.ttf | Nee | Nee |
| sv | Zweeds | NotoSans-Medium.ttf | Nee | Nee |
| da | Deens | NotoSans-Medium.ttf | Nee | Nee |
| no | Noors | NotoSans-Medium.ttf | Nee | Nee |
| fi | Fins | NotoSans-Medium.ttf | Nee | Nee |
| nl | Nederlands | NotoSans-Medium.ttf | Nee | Nee |
| he | Hebreeuws | NotoSansHebrew-Medium.ttf | Ja | Nee |
| vi | Vietnamees | NotoSans-Medium.ttf | Nee | Nee |
| id | Indonesisch | NotoSans-Medium.ttf | Nee | Nee |
| ms | Maleis | NotoSans-Medium.ttf | Nee | Nee |
| tl | Tagalog (Filipijns) | NotoSans-Medium.ttf | Nee | Nee |
| sw | Swahili | NotoSans-Medium.ttf | Nee | Nee |
| hu | Hongaars | NotoSans-Medium.ttf | Nee | Nee |
| cs | Tsjechisch | NotoSans-Medium.ttf | Nee | Nee |
| sk | Slowaaks | NotoSans-Medium.ttf | Nee | Nee |
| ro | Roemeens | NotoSans-Medium.ttf | Nee | Nee |
| bg | Bulgaars | NotoSans-Medium.ttf | Nee | Nee |
| sr | Servisch (Cyrillisch) | NotoSans-Medium.ttf | Nee | Nee |
| hr | Kroatisch | NotoSans-Medium.ttf | Nee | Nee |
| sl | Sloveens | NotoSans-Medium.ttf | Nee | Nee |
| uk | Oekraïens | NotoSans-Medium.ttf | Nee | Nee |
| my | Birmaans (Myanmar) | NotoSansMyanmar-Medium.ttf | Nee | Nee |
| ta | Tamil | NotoSansTamil-Medium.ttf | Nee | Nee |
| et | Ests | NotoSans-Medium.ttf | Nee | Nee |
| pcm | Nigeriaans Pidgin | NotoSans-Medium.ttf | Nee | Nee |
| te | Telugu | NotoSans-Medium.ttf | Nee | Nee |
| ml | Malayalam | NotoSans-Medium.ttf | Nee | Nee |
| kn | Kannada | NotoSans-Medium.ttf | Nee | Nee |
| km | Khmer | NotoSansKhmer-Medium.ttf | Nee | Nee |
| mni | Manipuri (Meitei Mayek) | NotoSansMeeteiMayek-Medium.ttf | Nee | Nee |

## Voeg een taal toe

Om ondersteuning voor een nieuwe taal toe te voegen:

1. Voeg de taalcode en de weergavenaam toe aan de taalhulpmiddelen.
2. Voeg een lettertype toe of koppel er een in `src/co_op_translator/fonts/font_language_mappings.yml`.
3. Test de uitvoer van de Markdown- en afbeeldingsvertalingen.
4. Open een pull request met de mapping en validatienotities.