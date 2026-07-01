# Limbi acceptate

Co-op Translator acceptă următoarele coduri de limbă pentru ieșirile de traducere pentru text, notebook și imagini.

Dacă doriți să adăugați o limbă nouă, actualizați mapările limbii și ale fontului din `src/co_op_translator/fonts/` și testați limba înainte de a deschide un pull request.

| Cod limbă | Nume limbă | Font | Suport RTL | Probleme cunoscute |
| --- | --- | --- | --- | --- |
| en | Engleză | NotoSans-Medium.ttf | Nu | Nu |
| fr | Franceză | NotoSans-Medium.ttf | Nu | Nu |
| es | Spaniolă | NotoSans-Medium.ttf | Nu | Nu |
| de | Germană | NotoSans-Medium.ttf | Nu | Nu |
| ru | Rusă | NotoSans-Medium.ttf | Nu | Nu |
| ar | Arabă | NotoSansArabic-Medium.ttf | Da | Nu |
| fa | Persană (Farsi) | NotoSansArabic-Medium.ttf | Da | Nu |
| ur | Urdu | NotoSansArabic-Medium.ttf | Da | Nu |
| zh-CN | Chineză (simplificată) | NotoSansCJK-Medium.ttc | Nu | Nu |
| zh-MO | Chineză (Tradițională, Macao) | NotoSansCJK-Medium.ttc | Nu | Nu |
| zh-HK | Chineză (Tradițională, Hong Kong) | NotoSansCJK-Medium.ttc | Nu | Nu |
| zh-TW | Chineză (Tradițională, Taiwan) | NotoSansCJK-Medium.ttc | Nu | Nu |
| ja | Japoneză | NotoSansCJK-Medium.ttc | Nu | Nu |
| ko | Coreeană | NotoSansCJK-Medium.ttc | Nu | Nu |
| hi | Hindi | NotoSansDevanagari-Medium.ttf | Nu | Nu |
| bn | Bengaleză | NotoSansBengali-Medium.ttf | Nu | Nu |
| mr | Marathi | NotoSansDevanagari-Medium.ttf | Nu | Nu |
| ne | Nepaleză | NotoSansDevanagari-Medium.ttf | Nu | Nu |
| pa | Punjabi (Gurmukhi) | NotoSansGurmukhi-Medium.ttf | Nu | Nu |
| pt-PT | Portugheză (Portugalia) | NotoSans-Medium.ttf | Nu | Nu |
| pt-BR | Portugheză (Brazilia) | NotoSans-Medium.ttf | Nu | Nu |
| it | Italiană | NotoSans-Medium.ttf | Nu | Nu |
| lt | Lituaniană | NotoSans-Medium.ttf | Nu | Nu |
| pl | Poloneză | NotoSans-Medium.ttf | Nu | Nu |
| tr | Turcă | NotoSans-Medium.ttf | Nu | Nu |
| el | Greacă | NotoSans-Medium.ttf | Nu | Nu |
| th | Thailandeză | NotoSansThai-Medium.ttf | Nu | Nu |
| sv | Suedeză | NotoSans-Medium.ttf | Nu | Nu |
| da | Daneză | NotoSans-Medium.ttf | Nu | Nu |
| no | Norvegiană | NotoSans-Medium.ttf | Nu | Nu |
| fi | Finlandeză | NotoSans-Medium.ttf | Nu | Nu |
| nl | Olandeză | NotoSans-Medium.ttf | Nu | Nu |
| he | Ebraică | NotoSansHebrew-Medium.ttf | Da | Nu |
| vi | Vietnameză | NotoSans-Medium.ttf | Nu | Nu |
| id | Indoneziană | NotoSans-Medium.ttf | Nu | Nu |
| ms | Malaieză | NotoSans-Medium.ttf | Nu | Nu |
| tl | Tagalog (Filipineză) | NotoSans-Medium.ttf | Nu | Nu |
| sw | Swahili | NotoSans-Medium.ttf | Nu | Nu |
| hu | Maghiară | NotoSans-Medium.ttf | Nu | Nu |
| cs | Cehă | NotoSans-Medium.ttf | Nu | Nu |
| sk | Slovacă | NotoSans-Medium.ttf | Nu | Nu |
| ro | Română | NotoSans-Medium.ttf | Nu | Nu |
| bg | Bulgară | NotoSans-Medium.ttf | Nu | Nu |
| sr | Sârbă (Chirilic) | NotoSans-Medium.ttf | Nu | Nu |
| hr | Croată | NotoSans-Medium.ttf | Nu | Nu |
| sl | Slovenă | NotoSans-Medium.ttf | Nu | Nu |
| uk | Ucraineană | NotoSans-Medium.ttf | Nu | Nu |
| my | Birmană (Myanmar) | NotoSansMyanmar-Medium.ttf | Nu | Nu |
| ta | Tamilă | NotoSansTamil-Medium.ttf | Nu | Nu |
| et | Estonă | NotoSans-Medium.ttf | Nu | Nu |
| pcm | Pidgin nigerian | NotoSans-Medium.ttf | Nu | Nu |
| te | Telugu | NotoSans-Medium.ttf | Nu | Nu |
| ml | Malayalam | NotoSans-Medium.ttf | Nu | Nu |
| kn | Kannada | NotoSans-Medium.ttf | Nu | Nu |
| km | Khmer | NotoSansKhmer-Medium.ttf | Nu | Nu |

## Adăugați o limbă

Pentru a adăuga suport pentru o limbă nouă:

1. Adăugați codul limbii și denumirea afișată în utilitarele de limbă.
2. Adăugați sau mapați un font în `src/co_op_translator/fonts/font_language_mappings.yml`.
3. Testați rezultatul traducerii pentru Markdown și imagini.
4. Deschideți un pull request cu maparea și notele de validare.