# Obsługiwane języki

Co-op Translator obsługuje następujące kody języków dla tłumaczeń tekstu, notatników i obrazów.

Jeśli chcesz dodać nowy język, zaktualizuj mapowania języka i czcionek w `src/co_op_translator/fonts/` i przetestuj język przed otwarciem pull requesta.

| Language Code | Language Name | Font | RTL Support | Known Issues |
| --- | --- | --- | --- | --- |
| en | Angielski | NotoSans-Medium.ttf | Nie | Brak |
| fr | Francuski | NotoSans-Medium.ttf | Nie | Brak |
| es | Hiszpański | NotoSans-Medium.ttf | Nie | Brak |
| de | Niemiecki | NotoSans-Medium.ttf | Nie | Brak |
| ru | Rosyjski | NotoSans-Medium.ttf | Nie | Brak |
| ar | Arabski | NotoSansArabic-Medium.ttf | Tak | Brak |
| fa | Perski (Farsi) | NotoSansArabic-Medium.ttf | Tak | Brak |
| ur | Urdu | NotoSansArabic-Medium.ttf | Tak | Brak |
| zh-CN | Chiński (uproszczony) | NotoSansCJK-Medium.ttc | Nie | Brak |
| zh-MO | Chiński (tradycyjny, Makau) | NotoSansCJK-Medium.ttc | Nie | Brak |
| zh-HK | Chiński (tradycyjny, Hongkong) | NotoSansCJK-Medium.ttc | Nie | Brak |
| zh-TW | Chiński (tradycyjny, Tajwan) | NotoSansCJK-Medium.ttc | Nie | Brak |
| ja | Japoński | NotoSansCJK-Medium.ttc | Nie | Brak |
| ko | Koreański | NotoSansCJK-Medium.ttc | Nie | Brak |
| hi | Hindi | NotoSansDevanagari-Medium.ttf | Nie | Brak |
| bn | Bengalski | NotoSansBengali-Medium.ttf | Nie | Brak |
| mr | Marathi | NotoSansDevanagari-Medium.ttf | Nie | Brak |
| ne | Nepalski | NotoSansDevanagari-Medium.ttf | Nie | Brak |
| pa | Pendżabski (Gurmukhi) | NotoSansGurmukhi-Medium.ttf | Nie | Brak |
| pt-PT | Portugalski (Portugalia) | NotoSans-Medium.ttf | Nie | Brak |
| pt-BR | Portugalski (Brazylia) | NotoSans-Medium.ttf | Nie | Brak |
| it | Włoski | NotoSans-Medium.ttf | Nie | Brak |
| lt | Litewski | NotoSans-Medium.ttf | Nie | Brak |
| pl | Polski | NotoSans-Medium.ttf | Nie | Brak |
| tr | Turecki | NotoSans-Medium.ttf | Nie | Brak |
| el | Grecki | NotoSans-Medium.ttf | Nie | Brak |
| th | Tajski | NotoSansThai-Medium.ttf | Nie | Brak |
| sv | Szwedzki | NotoSans-Medium.ttf | Nie | Brak |
| da | Duński | NotoSans-Medium.ttf | Nie | Brak |
| no | Norweski | NotoSans-Medium.ttf | Nie | Brak |
| fi | Fiński | NotoSans-Medium.ttf | Nie | Brak |
| nl | Holenderski | NotoSans-Medium.ttf | Nie | Brak |
| he | Hebrajski | NotoSansHebrew-Medium.ttf | Tak | Brak |
| vi | Wietnamski | NotoSans-Medium.ttf | Nie | Brak |
| id | Indonezyjski | NotoSans-Medium.ttf | Nie | Brak |
| ms | Malajski | NotoSans-Medium.ttf | Nie | Brak |
| tl | Tagalog (Filipiński) | NotoSans-Medium.ttf | Nie | Brak |
| sw | Suahili | NotoSans-Medium.ttf | Nie | Brak |
| hu | Węgierski | NotoSans-Medium.ttf | Nie | Brak |
| cs | Czeski | NotoSans-Medium.ttf | Nie | Brak |
| sk | Słowacki | NotoSans-Medium.ttf | Nie | Brak |
| ro | Rumuński | NotoSans-Medium.ttf | Nie | Brak |
| bg | Bułgarski | NotoSans-Medium.ttf | Nie | Brak |
| sr | Serbski (Cyrillic) | NotoSans-Medium.ttf | Nie | Brak |
| hr | Chorwacki | NotoSans-Medium.ttf | Nie | Brak |
| sl | Słoweński | NotoSans-Medium.ttf | Nie | Brak |
| uk | Ukraiński | NotoSans-Medium.ttf | Nie | Brak |
| my | Birmański (Myanmar) | NotoSansMyanmar-Medium.ttf | Nie | Brak |
| ta | Tamil | NotoSansTamil-Medium.ttf | Nie | Brak |
| et | Estoński | NotoSans-Medium.ttf | Nie | Brak |
| pcm | Nigeryjski Pidgin | NotoSans-Medium.ttf | Nie | Brak |
| te | Telugu | NotoSans-Medium.ttf | Nie | Brak |
| ml | Malayalam | NotoSans-Medium.ttf | Nie | Brak |
| kn | Kannada | NotoSans-Medium.ttf | Nie | Brak |
| km | Khmerski | NotoSansKhmer-Medium.ttf | Nie | Brak |

## Dodaj język

Aby dodać obsługę nowego języka:

1. Dodaj kod języka i nazwę wyświetlaną do narzędzi językowych.
2. Dodaj lub odwzoruj czcionkę w `src/co_op_translator/fonts/font_language_mappings.yml`.
3. Przetestuj wyjście tłumaczenia Markdown i obrazów.
4. Otwórz pull request z mapowaniem i notatkami walidacyjnymi.