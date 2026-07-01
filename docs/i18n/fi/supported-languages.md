# Tuetut kielet

Co-op Translator tukee seuraavia kielikoodeja tekstin, muistiinpanojen ja kuvien käännöstulosten osalta.

Jos haluat lisätä uuden kielen, päivitä kieli- ja fonttikartoitukset hakemistossa `src/co_op_translator/fonts/` ja testaa kieli ennen pull requestin avaamista.

| Kielikoodi | Kielen nimi | Fontti | RTL-tuki | Tunnetut ongelmat |
| --- | --- | --- | --- | --- |
| en | englanti | NotoSans-Medium.ttf | Ei | Ei |
| fr | ranska | NotoSans-Medium.ttf | Ei | Ei |
| es | espanja | NotoSans-Medium.ttf | Ei | Ei |
| de | saksa | NotoSans-Medium.ttf | Ei | Ei |
| ru | venäjä | NotoSans-Medium.ttf | Ei | Ei |
| ar | arabia | NotoSansArabic-Medium.ttf | Kyllä | Ei |
| fa | persia (farsi) | NotoSansArabic-Medium.ttf | Kyllä | Ei |
| ur | urdu | NotoSansArabic-Medium.ttf | Kyllä | Ei |
| zh-CN | kiina (yksinkertaistettu) | NotoSansCJK-Medium.ttc | Ei | Ei |
| zh-MO | kiina (perinteinen, Macau) | NotoSansCJK-Medium.ttc | Ei | Ei |
| zh-HK | kiina (perinteinen, Hong Kong) | NotoSansCJK-Medium.ttc | Ei | Ei |
| zh-TW | kiina (perinteinen, Taiwan) | NotoSansCJK-Medium.ttc | Ei | Ei |
| ja | japani | NotoSansCJK-Medium.ttc | Ei | Ei |
| ko | korea | NotoSansCJK-Medium.ttc | Ei | Ei |
| hi | hindi | NotoSansDevanagari-Medium.ttf | Ei | Ei |
| bn | bengali | NotoSansBengali-Medium.ttf | Ei | Ei |
| mr | marathi | NotoSansDevanagari-Medium.ttf | Ei | Ei |
| ne | nepali | NotoSansDevanagari-Medium.ttf | Ei | Ei |
| pa | pandžabi (Gurmukhi) | NotoSansGurmukhi-Medium.ttf | Ei | Ei |
| pt-PT | portugali (Portugali) | NotoSans-Medium.ttf | Ei | Ei |
| pt-BR | portugali (Brasilia) | NotoSans-Medium.ttf | Ei | Ei |
| it | italia | NotoSans-Medium.ttf | Ei | Ei |
| lt | liettua | NotoSans-Medium.ttf | Ei | Ei |
| pl | puola | NotoSans-Medium.ttf | Ei | Ei |
| tr | turkki | NotoSans-Medium.ttf | Ei | Ei |
| el | kreikka | NotoSans-Medium.ttf | Ei | Ei |
| th | thai | NotoSansThai-Medium.ttf | Ei | Ei |
| sv | ruotsi | NotoSans-Medium.ttf | Ei | Ei |
| da | tanska | NotoSans-Medium.ttf | Ei | Ei |
| no | norja | NotoSans-Medium.ttf | Ei | Ei |
| fi | suomi | NotoSans-Medium.ttf | Ei | Ei |
| nl | hollanti | NotoSans-Medium.ttf | Ei | Ei |
| he | heprea | NotoSansHebrew-Medium.ttf | Kyllä | Ei |
| vi | vietnami | NotoSans-Medium.ttf | Ei | Ei |
| id | indonesia | NotoSans-Medium.ttf | Ei | Ei |
| ms | malaiji | NotoSans-Medium.ttf | Ei | Ei |
| tl | tagalog (filipino) | NotoSans-Medium.ttf | Ei | Ei |
| sw | swahili | NotoSans-Medium.ttf | Ei | Ei |
| hu | unkari | NotoSans-Medium.ttf | Ei | Ei |
| cs | tšekki | NotoSans-Medium.ttf | Ei | Ei |
| sk | slovakki | NotoSans-Medium.ttf | Ei | Ei |
| ro | romania | NotoSans-Medium.ttf | Ei | Ei |
| bg | bulgaria | NotoSans-Medium.ttf | Ei | Ei |
| sr | serbia (kyrillinen) | NotoSans-Medium.ttf | Ei | Ei |
| hr | kroatia | NotoSans-Medium.ttf | Ei | Ei |
| sl | slovenia | NotoSans-Medium.ttf | Ei | Ei |
| uk | ukraina | NotoSans-Medium.ttf | Ei | Ei |
| my | burmalainen (Myanmar) | NotoSansMyanmar-Medium.ttf | Ei | Ei |
| ta | tamili | NotoSansTamil-Medium.ttf | Ei | Ei |
| et | viro | NotoSans-Medium.ttf | Ei | Ei |
| pcm | nigerialainen pidgin | NotoSans-Medium.ttf | Ei | Ei |
| te | telugu | NotoSans-Medium.ttf | Ei | Ei |
| ml | malayalam | NotoSans-Medium.ttf | Ei | Ei |
| kn | kannada | NotoSans-Medium.ttf | Ei | Ei |
| km | khmer | NotoSansKhmer-Medium.ttf | Ei | Ei |

## Lisää kieli

Lisätäksesi tuen uudelle kielelle:

1. Lisää kielikoodi ja näyttönimi kielityökaluihin.
2. Lisää tai yhdistä fontti tiedostoon `src/co_op_translator/fonts/font_language_mappings.yml`.
3. Testaa Markdown- ja kuvan käännöstulokset.
4. Avaa pull request, johon sisällytät kartoituksen ja validointimuistiinpanot.