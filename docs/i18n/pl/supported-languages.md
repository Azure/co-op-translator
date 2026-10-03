# Obsługiwane języki

Co-op Translator obsługuje następujące kody języków dla tłumaczeń tekstu, notatników oraz obrazów.

Jeśli chcesz dodać nowy język, zaktualizuj mapowania języka i czcionek w `src/co_op_translator/fonts/` i przetestuj język przed otwarciem pull requesta.

| Language Code | Language Name | Font | RTL Support | Known Issues |
| --- | --- | --- | --- | --- |
| en | angielski | NotoSans-Medium.ttf | Nie | Nie |
| fr | francuski | NotoSans-Medium.ttf | Nie | Nie |
| es | hiszpański | NotoSans-Medium.ttf | Nie | Nie |
| de | niemiecki | NotoSans-Medium.ttf | Nie | Nie |
| ru | rosyjski | NotoSans-Medium.ttf | Nie | Nie |
| ar | arabski | NotoSansArabic-Medium.ttf | Tak | Nie |
| fa | perski (farsi) | NotoSansArabic-Medium.ttf | Tak | Nie |
| ur | urdu | NotoSansArabic-Medium.ttf | Tak | Nie |
| zh-CN | chiński (uproszczony) | NotoSansCJK-Medium.ttc | Nie | Nie |
| zh-MO | chiński (tradycyjny, Makau) | NotoSansCJK-Medium.ttc | Nie | Nie |
| zh-HK | chiński (tradycyjny, Hongkong) | NotoSansCJK-Medium.ttc | Nie | Nie |
| zh-TW | chiński (tradycyjny, Tajwan) | NotoSansCJK-Medium.ttc | Nie | Nie |
| ja | japoński | NotoSansCJK-Medium.ttc | Nie | Nie |
| ko | koreański | NotoSansCJK-Medium.ttc | Nie | Nie |
| hi | hindi | NotoSansDevanagari-Medium.ttf | Nie | Nie |
| bn | bengalski | NotoSansBengali-Medium.ttf | Nie | Nie |
| mr | marathi | NotoSansDevanagari-Medium.ttf | Nie | Nie |
| ne | nepalski | NotoSansDevanagari-Medium.ttf | Nie | Nie |
| pa | pendżabski (Gurmukhi) | NotoSansGurmukhi-Medium.ttf | Nie | Nie |
| pt-PT | portugalski (Portugalia) | NotoSans-Medium.ttf | Nie | Nie |
| pt-BR | portugalski (Brazylia) | NotoSans-Medium.ttf | Nie | Nie |
| it | włoski | NotoSans-Medium.ttf | Nie | Nie |
| lt | litewski | NotoSans-Medium.ttf | Nie | Nie |
| pl | polski | NotoSans-Medium.ttf | Nie | Nie |
| tr | turecki | NotoSans-Medium.ttf | Nie | Nie |
| el | grecki | NotoSans-Medium.ttf | Nie | Nie |
| th | tajski | NotoSansThai-Medium.ttf | Nie | Nie |
| sv | szwedzki | NotoSans-Medium.ttf | Nie | Nie |
| da | duński | NotoSans-Medium.ttf | Nie | Nie |
| no | norweski | NotoSans-Medium.ttf | Nie | Nie |
| fi | fiński | NotoSans-Medium.ttf | Nie | Nie |
| nl | niderlandzki | NotoSans-Medium.ttf | Nie | Nie |
| he | hebrajski | NotoSansHebrew-Medium.ttf | Tak | Nie |
| vi | wietnamski | NotoSans-Medium.ttf | Nie | Nie |
| id | indonezyjski | NotoSans-Medium.ttf | Nie | Nie |
| ms | malajski | NotoSans-Medium.ttf | Nie | Nie |
| tl | tagalog (filipiński) | NotoSans-Medium.ttf | Nie | Nie |
| sw | suahili | NotoSans-Medium.ttf | Nie | Nie |
| hu | węgierski | NotoSans-Medium.ttf | Nie | Nie |
| cs | czeski | NotoSans-Medium.ttf | Nie | Nie |
| sk | słowacki | NotoSans-Medium.ttf | Nie | Nie |
| ro | rumuński | NotoSans-Medium.ttf | Nie | Nie |
| bg | bułgarski | NotoSans-Medium.ttf | Nie | Nie |
| sr | serbski (cyrylica) | NotoSans-Medium.ttf | Nie | Nie |
| hr | chorwacki | NotoSans-Medium.ttf | Nie | Nie |
| sl | słoweński | NotoSans-Medium.ttf | Nie | Nie |
| uk | ukraiński | NotoSans-Medium.ttf | Nie | Nie |
| my | birmański (Myanmar) | NotoSansMyanmar-Medium.ttf | Nie | Nie |
| ta | tamilski | NotoSansTamil-Medium.ttf | Nie | Nie |
| et | estoński | NotoSans-Medium.ttf | Nie | Nie |
| pcm | pidżin nigeryjski | NotoSans-Medium.ttf | Nie | Nie |
| te | telugu | NotoSans-Medium.ttf | Nie | Nie |
| ml | malajalam | NotoSans-Medium.ttf | Nie | Nie |
| kn | kannada | NotoSans-Medium.ttf | Nie | Nie |
| km | khmerski | NotoSansKhmer-Medium.ttf | Nie | Nie |
| mni | manipuri (Meitei Mayek) | NotoSansMeeteiMayek-Medium.ttf | Nie | Nie |

## Dodaj język

Aby dodać obsługę nowego języka:

1. Dodaj kod języka i nazwę wyświetlaną do narzędzi językowych.
2. Dodaj lub przypisz czcionkę w pliku `src/co_op_translator/fonts/font_language_mappings.yml`.
3. Przetestuj wynik tłumaczenia Markdown i obrazów.
4. Otwórz pull request z mapowaniem i notatkami walidacyjnymi.