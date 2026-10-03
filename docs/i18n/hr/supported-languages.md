# Podržani jezici

Co-op Translator podržava sljedeće šifre jezika za tekstualne, bilježničke i slikovne prijevode.

Ako želite dodati novi jezik, ažurirajte mapiranja jezika i fontova u `src/co_op_translator/fonts/` i testirajte jezik prije otvaranja pull requesta.

| Language Code | Language Name | Font | RTL Support | Known Issues |
| --- | --- | --- | --- | --- |
| en | Engleski | NotoSans-Medium.ttf | Ne | Ne |
| fr | Francuski | NotoSans-Medium.ttf | Ne | Ne |
| es | Španjolski | NotoSans-Medium.ttf | Ne | Ne |
| de | Njemački | NotoSans-Medium.ttf | Ne | Ne |
| ru | Ruski | NotoSans-Medium.ttf | Ne | Ne |
| ar | Arapski | NotoSansArabic-Medium.ttf | Da | Ne |
| fa | Perzijski (Farsi) | NotoSansArabic-Medium.ttf | Da | Ne |
| ur | Urdu | NotoSansArabic-Medium.ttf | Da | Ne |
| zh-CN | Kineski (pojednostavljeni) | NotoSansCJK-Medium.ttc | Ne | Ne |
| zh-MO | Kineski (tradicionalni, Makao) | NotoSansCJK-Medium.ttc | Ne | Ne |
| zh-HK | Kineski (tradicionalni, Hong Kong) | NotoSansCJK-Medium.ttc | Ne | Ne |
| zh-TW | Kineski (tradicionalni, Tajvan) | NotoSansCJK-Medium.ttc | Ne | Ne |
| ja | Japanski | NotoSansCJK-Medium.ttc | Ne | Ne |
| ko | Korejski | NotoSansCJK-Medium.ttc | Ne | Ne |
| hi | Hindi | NotoSansDevanagari-Medium.ttf | Ne | Ne |
| bn | Bengalski | NotoSansBengali-Medium.ttf | Ne | Ne |
| mr | Marathi | NotoSansDevanagari-Medium.ttf | Ne | Ne |
| ne | Nepalski | NotoSansDevanagari-Medium.ttf | Ne | Ne |
| pa | Pandžapski (Gurmukhi) | NotoSansGurmukhi-Medium.ttf | Ne | Ne |
| pt-PT | Portugalski (Portugal) | NotoSans-Medium.ttf | Ne | Ne |
| pt-BR | Portugalski (Brazil) | NotoSans-Medium.ttf | Ne | Ne |
| it | Talijanski | NotoSans-Medium.ttf | Ne | Ne |
| lt | Litavski | NotoSans-Medium.ttf | Ne | Ne |
| pl | Poljski | NotoSans-Medium.ttf | Ne | Ne |
| tr | Turski | NotoSans-Medium.ttf | Ne | Ne |
| el | Grčki | NotoSans-Medium.ttf | Ne | Ne |
| th | Tajlandski | NotoSansThai-Medium.ttf | Ne | Ne |
| sv | Švedski | NotoSans-Medium.ttf | Ne | Ne |
| da | Danski | NotoSans-Medium.ttf | Ne | Ne |
| no | Norveški | NotoSans-Medium.ttf | Ne | Ne |
| fi | Finski | NotoSans-Medium.ttf | Ne | Ne |
| nl | Nizozemski | NotoSans-Medium.ttf | Ne | Ne |
| he | Hebrejski | NotoSansHebrew-Medium.ttf | Da | Ne |
| vi | Vijetnamski | NotoSans-Medium.ttf | Ne | Ne |
| id | Indonezijski | NotoSans-Medium.ttf | Ne | Ne |
| ms | Malajski | NotoSans-Medium.ttf | Ne | Ne |
| tl | Tagalog (filipinski) | NotoSans-Medium.ttf | Ne | Ne |
| sw | Svahili | NotoSans-Medium.ttf | Ne | Ne |
| hu | Mađarski | NotoSans-Medium.ttf | Ne | Ne |
| cs | Češki | NotoSans-Medium.ttf | Ne | Ne |
| sk | Slovački | NotoSans-Medium.ttf | Ne | Ne |
| ro | Rumunjski | NotoSans-Medium.ttf | Ne | Ne |
| bg | Bugarski | NotoSans-Medium.ttf | Ne | Ne |
| sr | Srpski (ćirilica) | NotoSans-Medium.ttf | Ne | Ne |
| hr | Hrvatski | NotoSans-Medium.ttf | Ne | Ne |
| sl | Slovenski | NotoSans-Medium.ttf | Ne | Ne |
| uk | Ukrajinski | NotoSans-Medium.ttf | Ne | Ne |
| my | Burmanski (Mjanmar) | NotoSansMyanmar-Medium.ttf | Ne | Ne |
| ta | Tamilski | NotoSansTamil-Medium.ttf | Ne | Ne |
| et | Estonski | NotoSans-Medium.ttf | Ne | Ne |
| pcm | Nigerijski pidžin | NotoSans-Medium.ttf | Ne | Ne |
| te | Telugu | NotoSans-Medium.ttf | Ne | Ne |
| ml | Malayalam | NotoSans-Medium.ttf | Ne | Ne |
| kn | Kannada | NotoSans-Medium.ttf | Ne | Ne |
| km | Kmerski | NotoSansKhmer-Medium.ttf | Ne | Ne |
| mni | Manipuri (Meitei Mayek) | NotoSansMeeteiMayek-Medium.ttf | Ne | Ne |

## Dodajte jezik

Za dodavanje podrške za novi jezik:

1. Dodajte šifru jezika i prikazni naziv u jezične alate.
2. Dodajte ili mapirajte font u `src/co_op_translator/fonts/font_language_mappings.yml`.
3. Testirajte izlaz prijevoda Markdowna i slika.
4. Otvorite pull request s mapiranjem i bilješkama o validaciji.