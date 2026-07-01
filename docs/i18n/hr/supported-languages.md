# Podržani jezici

Co-op Translator podržava sljedeće kodove jezika za prijevode teksta, bilježnica i slika.

Ako želite dodati novi jezik, ažurirajte mapiranja jezika i fontova u `src/co_op_translator/fonts/` i testirajte jezik prije otvaranja pull requesta.

| Language Code | Naziv jezika | Font | Podrška za RTL | Poznati problemi |
| --- | --- | --- | --- | --- |
| en | Engleski | NotoSans-Medium.ttf | Ne | Nema |
| fr | Francuski | NotoSans-Medium.ttf | Ne | Nema |
| es | Španjolski | NotoSans-Medium.ttf | Ne | Nema |
| de | Njemački | NotoSans-Medium.ttf | Ne | Nema |
| ru | Ruski | NotoSans-Medium.ttf | Ne | Nema |
| ar | Arapski | NotoSansArabic-Medium.ttf | Da | Nema |
| fa | Perzijski (Farsi) | NotoSansArabic-Medium.ttf | Da | Nema |
| ur | Urdu | NotoSansArabic-Medium.ttf | Da | Nema |
| zh-CN | Kineski (pojednostavljeni) | NotoSansCJK-Medium.ttc | Ne | Nema |
| zh-MO | Kineski (tradicionalni, Makao) | NotoSansCJK-Medium.ttc | Ne | Nema |
| zh-HK | Kineski (tradicionalni, Hong Kong) | NotoSansCJK-Medium.ttc | Ne | Nema |
| zh-TW | Kineski (tradicionalni, Tajvan) | NotoSansCJK-Medium.ttc | Ne | Nema |
| ja | Japanski | NotoSansCJK-Medium.ttc | Ne | Nema |
| ko | Korejski | NotoSansCJK-Medium.ttc | Ne | Nema |
| hi | Hindi | NotoSansDevanagari-Medium.ttf | Ne | Nema |
| bn | Bengalski | NotoSansBengali-Medium.ttf | Ne | Nema |
| mr | Marathi | NotoSansDevanagari-Medium.ttf | Ne | Nema |
| ne | Nepalski | NotoSansDevanagari-Medium.ttf | Ne | Nema |
| pa | Punjabi (Gurmukhi) | NotoSansGurmukhi-Medium.ttf | Ne | Nema |
| pt-PT | Portugalski (Portugal) | NotoSans-Medium.ttf | Ne | Nema |
| pt-BR | Portugalski (Brazil) | NotoSans-Medium.ttf | Ne | Nema |
| it | Talijanski | NotoSans-Medium.ttf | Ne | Nema |
| lt | Litvanski | NotoSans-Medium.ttf | Ne | Nema |
| pl | Poljski | NotoSans-Medium.ttf | Ne | Nema |
| tr | Turski | NotoSans-Medium.ttf | Ne | Nema |
| el | Grčki | NotoSans-Medium.ttf | Ne | Nema |
| th | Tajlandski | NotoSansThai-Medium.ttf | Ne | Nema |
| sv | Švedski | NotoSans-Medium.ttf | Ne | Nema |
| da | Danski | NotoSans-Medium.ttf | Ne | Nema |
| no | Norveški | NotoSans-Medium.ttf | Ne | Nema |
| fi | Finski | NotoSans-Medium.ttf | Ne | Nema |
| nl | Nizozemski | NotoSans-Medium.ttf | Ne | Nema |
| he | Hebrejski | NotoSansHebrew-Medium.ttf | Da | Nema |
| vi | Vijetnamski | NotoSans-Medium.ttf | Ne | Nema |
| id | Indonezijski | NotoSans-Medium.ttf | Ne | Nema |
| ms | Malajski | NotoSans-Medium.ttf | Ne | Nema |
| tl | Tagalog (Filipinski) | NotoSans-Medium.ttf | Ne | Nema |
| sw | Svahili | NotoSans-Medium.ttf | Ne | Nema |
| hu | Mađarski | NotoSans-Medium.ttf | Ne | Nema |
| cs | Češki | NotoSans-Medium.ttf | Ne | Nema |
| sk | Slovački | NotoSans-Medium.ttf | Ne | Nema |
| ro | Rumunjski | NotoSans-Medium.ttf | Ne | Nema |
| bg | Bugarski | NotoSans-Medium.ttf | Ne | Nema |
| sr | Srpski (ćirilica) | NotoSans-Medium.ttf | Ne | Nema |
| hr | Hrvatski | NotoSans-Medium.ttf | Ne | Nema |
| sl | Slovenski | NotoSans-Medium.ttf | Ne | Nema |
| uk | Ukrajinski | NotoSans-Medium.ttf | Ne | Nema |
| my | Burmanski (Myanmar) | NotoSansMyanmar-Medium.ttf | Ne | Nema |
| ta | Tamilski | NotoSansTamil-Medium.ttf | Ne | Nema |
| et | Estonski | NotoSans-Medium.ttf | Ne | Nema |
| pcm | Nigerijski pidžin | NotoSans-Medium.ttf | Ne | Nema |
| te | Telugu | NotoSans-Medium.ttf | Ne | Nema |
| ml | Malayalam | NotoSans-Medium.ttf | Ne | Nema |
| kn | Kannada | NotoSans-Medium.ttf | Ne | Nema |
| km | Khmer | NotoSansKhmer-Medium.ttf | Ne | Nema |

## Dodavanje jezika

To add support for a new language:

1. Dodajte kod jezika i naziv prikaza u jezične utilitete.
2. Dodajte ili mapirajte font u `src/co_op_translator/fonts/font_language_mappings.yml`.
3. Testirajte izlaz prijevoda Markdowna i slika.
4. Otvorite pull request s mapiranjem i bilješkama o provjeri.