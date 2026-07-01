# Ondersteunde talen

Co-op Translator ondersteunt de volgende taalcodes voor tekst-, notebook- en afbeeldingsvertaaluitvoer.

Als je een nieuwe taal wilt toevoegen, werk dan de taal- en fonttoewijzingen bij onder `src/co_op_translator/fonts/` en test de taal voordat je een pull request opent.

| Language Code | Language Name | Font | RTL Support | Known Issues |
| --- | --- | --- | --- | --- |
| en | Engels | NotoSans-Medium.ttf | Nee | Geen |
| fr | Frans | NotoSans-Medium.ttf | Nee | Geen |
| es | Spaans | NotoSans-Medium.ttf | Nee | Geen |
| de | Duits | NotoSans-Medium.ttf | Nee | Geen |
| ru | Russisch | NotoSans-Medium.ttf | Nee | Geen |
| ar | Arabisch | NotoSansArabic-Medium.ttf | Ja | Geen |
| fa | Perzisch (Farsi) | NotoSansArabic-Medium.ttf | Ja | Geen |
| ur | Urdu | NotoSansArabic-Medium.ttf | Ja | Geen |
| zh-CN | Chinees (vereenvoudigd) | NotoSansCJK-Medium.ttc | Nee | Geen |
| zh-MO | Chinees (traditioneel, Macau) | NotoSansCJK-Medium.ttc | Nee | Geen |
| zh-HK | Chinees (traditioneel, Hongkong) | NotoSansCJK-Medium.ttc | Nee | Geen |
| zh-TW | Chinees (traditioneel, Taiwan) | NotoSansCJK-Medium.ttc | Nee | Geen |
| ja | Japans | NotoSansCJK-Medium.ttc | Nee | Geen |
| ko | Koreaans | NotoSansCJK-Medium.ttc | Nee | Geen |
| hi | Hindi | NotoSansDevanagari-Medium.ttf | Nee | Geen |
| bn | Bengalees | NotoSansBengali-Medium.ttf | Nee | Geen |
| mr | Marathi | NotoSansDevanagari-Medium.ttf | Nee | Geen |
| ne | Nepalees | NotoSansDevanagari-Medium.ttf | Nee | Geen |
| pa | Punjabi (Gurmukhi) | NotoSansGurmukhi-Medium.ttf | Nee | Geen |
| pt-PT | Portugees (Portugal) | NotoSans-Medium.ttf | Nee | Geen |
| pt-BR | Portugees (Brazilië) | NotoSans-Medium.ttf | Nee | Geen |
| it | Italiaans | NotoSans-Medium.ttf | Nee | Geen |
| lt | Litouws | NotoSans-Medium.ttf | Nee | Geen |
| pl | Pools | NotoSans-Medium.ttf | Nee | Geen |
| tr | Turks | NotoSans-Medium.ttf | Nee | Geen |
| el | Grieks | NotoSans-Medium.ttf | Nee | Geen |
| th | Thais | NotoSansThai-Medium.ttf | Nee | Geen |
| sv | Zweeds | NotoSans-Medium.ttf | Nee | Geen |
| da | Deens | NotoSans-Medium.ttf | Nee | Geen |
| no | Noors | NotoSans-Medium.ttf | Nee | Geen |
| fi | Fins | NotoSans-Medium.ttf | Nee | Geen |
| nl | Nederlands | NotoSans-Medium.ttf | Nee | Geen |
| he | Hebreeuws | NotoSansHebrew-Medium.ttf | Ja | Geen |
| vi | Vietnamees | NotoSans-Medium.ttf | Nee | Geen |
| id | Indonesisch | NotoSans-Medium.ttf | Nee | Geen |
| ms | Maleis | NotoSans-Medium.ttf | Nee | Geen |
| tl | Tagalog (Filipijns) | NotoSans-Medium.ttf | Nee | Geen |
| sw | Swahili | NotoSans-Medium.ttf | Nee | Geen |
| hu | Hongaars | NotoSans-Medium.ttf | Nee | Geen |
| cs | Tsjechisch | NotoSans-Medium.ttf | Nee | Geen |
| sk | Slowaaks | NotoSans-Medium.ttf | Nee | Geen |
| ro | Roemeens | NotoSans-Medium.ttf | Nee | Geen |
| bg | Bulgaars | NotoSans-Medium.ttf | Nee | Geen |
| sr | Servisch (Cyrillisch) | NotoSans-Medium.ttf | Nee | Geen |
| hr | Kroatisch | NotoSans-Medium.ttf | Nee | Geen |
| sl | Sloveens | NotoSans-Medium.ttf | Nee | Geen |
| uk | Oekraïens | NotoSans-Medium.ttf | Nee | Geen |
| my | Burmees (Myanmar) | NotoSansMyanmar-Medium.ttf | Nee | Geen |
| ta | Tamil | NotoSansTamil-Medium.ttf | Nee | Geen |
| et | Ests | NotoSans-Medium.ttf | Nee | Geen |
| pcm | Nigeriaans Pidgin | NotoSans-Medium.ttf | Nee | Geen |
| te | Telugu | NotoSans-Medium.ttf | Nee | Geen |
| ml | Malayalam | NotoSans-Medium.ttf | Nee | Geen |
| kn | Kannada | NotoSans-Medium.ttf | Nee | Geen |
| km | Khmer | NotoSansKhmer-Medium.ttf | Nee | Geen |

## Een taal toevoegen

Om ondersteuning voor een nieuwe taal toe te voegen:

1. Voeg de taalcode en weergavenaam toe aan de taalhulpmiddelen.
2. Voeg een lettertype toe of wijs er een toe in `src/co_op_translator/fonts/font_language_mappings.yml`.
3. Test de Markdown- en afbeeldingsvertaaluitvoer.
4. Open een pull request met de mapping en validatienotities.