# Supported Languages

Co-op Translator toetab järgmisi keelekoode teksti, märkmiku ja pilditõlke väljundite jaoks.

Kui soovite lisada uue keele, värskendage keel- ja fondi kaardistusi kataloogis `src/co_op_translator/fonts/` ning testige keelt enne pull requesti avamist.

| Language Code | Language Name | Font | RTL Support | Known Issues |
| --- | --- | --- | --- | --- |
| en | Inglise | NotoSans-Medium.ttf | Ei | Ei |
| fr | Prantsuse | NotoSans-Medium.ttf | Ei | Ei |
| es | Hispaania | NotoSans-Medium.ttf | Ei | Ei |
| de | Saksa | NotoSans-Medium.ttf | Ei | Ei |
| ru | Vene | NotoSans-Medium.ttf | Ei | Ei |
| ar | Araabia | NotoSansArabic-Medium.ttf | Jah | Ei |
| fa | Pärsia (Farsi) | NotoSansArabic-Medium.ttf | Jah | Ei |
| ur | Urdu | NotoSansArabic-Medium.ttf | Jah | Ei |
| zh-CN | Hiina (lihtsustatud) | NotoSansCJK-Medium.ttc | Ei | Ei |
| zh-MO | Hiina (traditsiooniline, Macau) | NotoSansCJK-Medium.ttc | Ei | Ei |
| zh-HK | Hiina (traditsiooniline, Hongkong) | NotoSansCJK-Medium.ttc | Ei | Ei |
| zh-TW | Hiina (traditsiooniline, Taiwan) | NotoSansCJK-Medium.ttc | Ei | Ei |
| ja | Jaapani | NotoSansCJK-Medium.ttc | Ei | Ei |
| ko | Korea | NotoSansCJK-Medium.ttc | Ei | Ei |
| hi | Hindi | NotoSansDevanagari-Medium.ttf | Ei | Ei |
| bn | Bengali | NotoSansBengali-Medium.ttf | Ei | Ei |
| mr | Marathi | NotoSansDevanagari-Medium.ttf | Ei | Ei |
| ne | Nepali | NotoSansDevanagari-Medium.ttf | Ei | Ei |
| pa | Pandžabi (Gurmukhi) | NotoSansGurmukhi-Medium.ttf | Ei | Ei |
| pt-PT | Portugali (Portugal) | NotoSans-Medium.ttf | Ei | Ei |
| pt-BR | Portugali (Brasiilia) | NotoSans-Medium.ttf | Ei | Ei |
| it | Itaalia | NotoSans-Medium.ttf | Ei | Ei |
| lt | Leedu | NotoSans-Medium.ttf | Ei | Ei |
| pl | Poola | NotoSans-Medium.ttf | Ei | Ei |
| tr | Türgi | NotoSans-Medium.ttf | Ei | Ei |
| el | Kreeka | NotoSans-Medium.ttf | Ei | Ei |
| th | Tai | NotoSansThai-Medium.ttf | Ei | Ei |
| sv | Rootsi | NotoSans-Medium.ttf | Ei | Ei |
| da | Taani | NotoSans-Medium.ttf | Ei | Ei |
| no | Norra | NotoSans-Medium.ttf | Ei | Ei |
| fi | Soome | NotoSans-Medium.ttf | Ei | Ei |
| nl | Hollandi | NotoSans-Medium.ttf | Ei | Ei |
| he | Heebrea | NotoSansHebrew-Medium.ttf | Jah | Ei |
| vi | Vietnami | NotoSans-Medium.ttf | Ei | Ei |
| id | Indoneesia | NotoSans-Medium.ttf | Ei | Ei |
| ms | Malai | NotoSans-Medium.ttf | Ei | Ei |
| tl | Tagalogi (Filipino) | NotoSans-Medium.ttf | Ei | Ei |
| sw | Suahiili | NotoSans-Medium.ttf | Ei | Ei |
| hu | Ungari | NotoSans-Medium.ttf | Ei | Ei |
| cs | Tšehhi | NotoSans-Medium.ttf | Ei | Ei |
| sk | Slovaki | NotoSans-Medium.ttf | Ei | Ei |
| ro | Rumeenia | NotoSans-Medium.ttf | Ei | Ei |
| bg | Bulgaaria | NotoSans-Medium.ttf | Ei | Ei |
| sr | Serbia (kirilitsa) | NotoSans-Medium.ttf | Ei | Ei |
| hr | Horvaatia | NotoSans-Medium.ttf | Ei | Ei |
| sl | Sloveenia | NotoSans-Medium.ttf | Ei | Ei |
| uk | Ukraina | NotoSans-Medium.ttf | Ei | Ei |
| my | Birma (Myanmar) | NotoSansMyanmar-Medium.ttf | Ei | Ei |
| ta | Tamil | NotoSansTamil-Medium.ttf | Ei | Ei |
| et | Eesti | NotoSans-Medium.ttf | Ei | Ei |
| pcm | Nigeeria pidžin | NotoSans-Medium.ttf | Ei | Ei |
| te | Telugu | NotoSans-Medium.ttf | Ei | Ei |
| ml | Malayalam | NotoSans-Medium.ttf | Ei | Ei |
| kn | Kannada | NotoSans-Medium.ttf | Ei | Ei |
| km | Khmer | NotoSansKhmer-Medium.ttf | Ei | Ei |

## Add a Language

To add support for a new language:

1. Lisage keelekood ja kuvav nimi keele utiliitidesse.
2. Lisage või seostage font failis `src/co_op_translator/fonts/font_language_mappings.yml`.
3. Testige Markdowni ja pilditõlke väljundit.
4. Avage pull request, lisades kaardistuse ja valideerimismärkused.