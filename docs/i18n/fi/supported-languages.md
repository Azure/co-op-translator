# Tuetut kielet

Co-op Translator tukee seuraavia kielikoodeja tekstin, notebookin ja kuvien käännöstulosteissa.

Jos haluat lisätä uuden kielen, päivitä kieli- ja fonttikartoitukset hakemistossa `src/co_op_translator/fonts/` ja testaa kieli ennen pull requestin avaamista.

| Kielikoodi | Kielen nimi | Fontti | RTL-tuki | Tunnetut ongelmat |
| --- | --- | --- | --- | --- |
| en | Englanti | NotoSans-Medium.ttf | Ei | Ei |
| fr | Ranska | NotoSans-Medium.ttf | Ei | Ei |
| es | Espanja | NotoSans-Medium.ttf | Ei | Ei |
| de | Saksa | NotoSans-Medium.ttf | Ei | Ei |
| ru | Venäjä | NotoSans-Medium.ttf | Ei | Ei |
| ar | Arabia | NotoSansArabic-Medium.ttf | Kyllä | Ei |
| fa | Persia (farsi) | NotoSansArabic-Medium.ttf | Kyllä | Ei |
| ur | Urdu | NotoSansArabic-Medium.ttf | Kyllä | Ei |
| zh-CN | Kiina (yksinkertaistettu) | NotoSansCJK-Medium.ttc | Ei | Ei |
| zh-MO | Kiina (perinteinen, Makao) | NotoSansCJK-Medium.ttc | Ei | Ei |
| zh-HK | Kiina (perinteinen, Hongkong) | NotoSansCJK-Medium.ttc | Ei | Ei |
| zh-TW | Kiina (perinteinen, Taiwan) | NotoSansCJK-Medium.ttc | Ei | Ei |
| ja | Japani | NotoSansCJK-Medium.ttc | Ei | Ei |
| ko | Korea | NotoSansCJK-Medium.ttc | Ei | Ei |
| hi | Hindi | NotoSansDevanagari-Medium.ttf | Ei | Ei |
| bn | Bengali | NotoSansBengali-Medium.ttf | Ei | Ei |
| mr | Marathi | NotoSansDevanagari-Medium.ttf | Ei | Ei |
| ne | Nepali | NotoSansDevanagari-Medium.ttf | Ei | Ei |
| pa | Pandžabi (Gurmukhi) | NotoSansGurmukhi-Medium.ttf | Ei | Ei |
| pt-PT | Portugali (Portugali) | NotoSans-Medium.ttf | Ei | Ei |
| pt-BR | Portugali (Brasilia) | NotoSans-Medium.ttf | Ei | Ei |
| it | Italia | NotoSans-Medium.ttf | Ei | Ei |
| lt | Liettua | NotoSans-Medium.ttf | Ei | Ei |
| pl | Puola | NotoSans-Medium.ttf | Ei | Ei |
| tr | Turkki | NotoSans-Medium.ttf | Ei | Ei |
| el | Kreikka | NotoSans-Medium.ttf | Ei | Ei |
| th | Thai | NotoSansThai-Medium.ttf | Ei | Ei |
| sv | Ruotsi | NotoSans-Medium.ttf | Ei | Ei |
| da | Tanska | NotoSans-Medium.ttf | Ei | Ei |
| no | Norja | NotoSans-Medium.ttf | Ei | Ei |
| fi | Suomi | NotoSans-Medium.ttf | Ei | Ei |
| nl | Hollanti | NotoSans-Medium.ttf | Ei | Ei |
| he | Heprea | NotoSansHebrew-Medium.ttf | Kyllä | Ei |
| vi | Vietnami | NotoSans-Medium.ttf | Ei | Ei |
| id | Indonesia | NotoSans-Medium.ttf | Ei | Ei |
| ms | Malaiji | NotoSans-Medium.ttf | Ei | Ei |
| tl | Tagalog (filippiino) | NotoSans-Medium.ttf | Ei | Ei |
| sw | Suahili | NotoSans-Medium.ttf | Ei | Ei |
| hu | Unkari | NotoSans-Medium.ttf | Ei | Ei |
| cs | Tšekki | NotoSans-Medium.ttf | Ei | Ei |
| sk | Slovakki | NotoSans-Medium.ttf | Ei | Ei |
| ro | Romania | NotoSans-Medium.ttf | Ei | Ei |
| bg | Bulgaria | NotoSans-Medium.ttf | Ei | Ei |
| sr | Serbi (kyrillinen) | NotoSans-Medium.ttf | Ei | Ei |
| hr | Kroatia | NotoSans-Medium.ttf | Ei | Ei |
| sl | Sloveeni | NotoSans-Medium.ttf | Ei | Ei |
| uk | Ukraina | NotoSans-Medium.ttf | Ei | Ei |
| my | Burmankieli (Myanmar) | NotoSansMyanmar-Medium.ttf | Ei | Ei |
| ta | Tamil | NotoSansTamil-Medium.ttf | Ei | Ei |
| et | Viro | NotoSans-Medium.ttf | Ei | Ei |
| pcm | Nigerian Pidgin | NotoSans-Medium.ttf | Ei | Ei |
| te | Telugu | NotoSans-Medium.ttf | Ei | Ei |
| ml | Malayalam | NotoSans-Medium.ttf | Ei | Ei |
| kn | Kannada | NotoSans-Medium.ttf | Ei | Ei |
| km | Khmer | NotoSansKhmer-Medium.ttf | Ei | Ei |
| mni | Manipuri (Meitei Mayek) | NotoSansMeeteiMayek-Medium.ttf | Ei | Ei |

## Lisää kieli

Uuden kielen lisäämiseksi:

1. Lisää kielikoodi ja näyttönimi kielityökaluihin.
2. Lisää tai kartoita fontti tiedostoon `src/co_op_translator/fonts/font_language_mappings.yml`.
3. Testaa Markdown- ja kuvien käännöstulosteet.
4. Avaa pull request, joka sisältää kartoituksen ja validointimuistiinpanot.