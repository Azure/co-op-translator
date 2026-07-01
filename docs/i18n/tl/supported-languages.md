# Sinusuportahang Mga Wika

Sinusuportahan ng Co-op Translator ang mga sumusunod na language codes para sa mga output ng pagsasalin ng teksto, notebook, at imahe.

Kung nais mong magdagdag ng bagong wika, i-update ang language and font mappings sa ilalim ng `src/co_op_translator/fonts/` at subukan ang wika bago magbukas ng pull request.

| Language Code | Language Name | Font | RTL Support | Known Issues |
| --- | --- | --- | --- | --- |
| en | English | NotoSans-Medium.ttf | Hindi | Wala |
| fr | French | NotoSans-Medium.ttf | Hindi | Wala |
| es | Spanish | NotoSans-Medium.ttf | Hindi | Wala |
| de | German | NotoSans-Medium.ttf | Hindi | Wala |
| ru | Russian | NotoSans-Medium.ttf | Hindi | Wala |
| ar | Arabic | NotoSansArabic-Medium.ttf | Oo | Wala |
| fa | Persian (Farsi) | NotoSansArabic-Medium.ttf | Oo | Wala |
| ur | Urdu | NotoSansArabic-Medium.ttf | Oo | Wala |
| zh-CN | Chinese (Simplified) | NotoSansCJK-Medium.ttc | Hindi | Wala |
| zh-MO | Chinese (Traditional, Macau) | NotoSansCJK-Medium.ttc | Hindi | Wala |
| zh-HK | Chinese (Traditional, Hong Kong) | NotoSansCJK-Medium.ttc | Hindi | Wala |
| zh-TW | Chinese (Traditional, Taiwan) | NotoSansCJK-Medium.ttc | Hindi | Wala |
| ja | Japanese | NotoSansCJK-Medium.ttc | Hindi | Wala |
| ko | Korean | NotoSansCJK-Medium.ttc | Hindi | Wala |
| hi | Hindi | NotoSansDevanagari-Medium.ttf | Hindi | Wala |
| bn | Bengali | NotoSansBengali-Medium.ttf | Hindi | Wala |
| mr | Marathi | NotoSansDevanagari-Medium.ttf | Hindi | Wala |
| ne | Nepali | NotoSansDevanagari-Medium.ttf | Hindi | Wala |
| pa | Punjabi (Gurmukhi) | NotoSansGurmukhi-Medium.ttf | Hindi | Wala |
| pt-PT | Portuguese (Portugal) | NotoSans-Medium.ttf | Hindi | Wala |
| pt-BR | Portuguese (Brazil) | NotoSans-Medium.ttf | Hindi | Wala |
| it | Italian | NotoSans-Medium.ttf | Hindi | Wala |
| lt | Lithuanian | NotoSans-Medium.ttf | Hindi | Wala |
| pl | Polish | NotoSans-Medium.ttf | Hindi | Wala |
| tr | Turkish | NotoSans-Medium.ttf | Hindi | Wala |
| el | Greek | NotoSans-Medium.ttf | Hindi | Wala |
| th | Thai | NotoSansThai-Medium.ttf | Hindi | Wala |
| sv | Swedish | NotoSans-Medium.ttf | Hindi | Wala |
| da | Danish | NotoSans-Medium.ttf | Hindi | Wala |
| no | Norwegian | NotoSans-Medium.ttf | Hindi | Wala |
| fi | Finnish | NotoSans-Medium.ttf | Hindi | Wala |
| nl | Dutch | NotoSans-Medium.ttf | Hindi | Wala |
| he | Hebrew | NotoSansHebrew-Medium.ttf | Oo | Wala |
| vi | Vietnamese | NotoSans-Medium.ttf | Hindi | Wala |
| id | Indonesian | NotoSans-Medium.ttf | Hindi | Wala |
| ms | Malay | NotoSans-Medium.ttf | Hindi | Wala |
| tl | Tagalog (Filipino) | NotoSans-Medium.ttf | Hindi | Wala |
| sw | Swahili | NotoSans-Medium.ttf | Hindi | Wala |
| hu | Hungarian | NotoSans-Medium.ttf | Hindi | Wala |
| cs | Czech | NotoSans-Medium.ttf | Hindi | Wala |
| sk | Slovak | NotoSans-Medium.ttf | Hindi | Wala |
| ro | Romanian | NotoSans-Medium.ttf | Hindi | Wala |
| bg | Bulgarian | NotoSans-Medium.ttf | Hindi | Wala |
| sr | Serbian (Cyrillic) | NotoSans-Medium.ttf | Hindi | Wala |
| hr | Croatian | NotoSans-Medium.ttf | Hindi | Wala |
| sl | Slovenian | NotoSans-Medium.ttf | Hindi | Wala |
| uk | Ukrainian | NotoSans-Medium.ttf | Hindi | Wala |
| my | Burmese (Myanmar) | NotoSansMyanmar-Medium.ttf | Hindi | Wala |
| ta | Tamil | NotoSansTamil-Medium.ttf | Hindi | Wala |
| et | Estonian | NotoSans-Medium.ttf | Hindi | Wala |
| pcm | Nigerian Pidgin | NotoSans-Medium.ttf | Hindi | Wala |
| te | Telugu | NotoSans-Medium.ttf | Hindi | Wala |
| ml | Malayalam | NotoSans-Medium.ttf | Hindi | Wala |
| kn | Kannada | NotoSans-Medium.ttf | Hindi | Wala |
| km | Khmer | NotoSansKhmer-Medium.ttf | Hindi | Wala |

## Magdagdag ng Wika

Para magdagdag ng suporta para sa bagong wika:

1. Idagdag ang code ng wika at pangalan na ipapakita sa mga utility ng wika.
2. Idagdag o i-map ang isang font sa `src/co_op_translator/fonts/font_language_mappings.yml`.
3. Subukan ang Markdown at output ng pagsasalin ng imahe.
4. Buksan ang isang pull request na may mapping at mga tala ng beripikasyon.