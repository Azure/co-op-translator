# Mga Sinusuportang Wika

Sinusuportahan ng Co-op Translator ang sumusunod na mga language code para sa output ng pagsasalin ng teksto, notebook, at imahe.

Kung nais mong magdagdag ng bagong wika, i-update ang mga mapping ng wika at font sa ilalim ng `src/co_op_translator/fonts/` at subukan ang wika bago magbukas ng pull request.

| Language Code | Language Name | Font | RTL Support | Known Issues |
| --- | --- | --- | --- | --- |
| en | English | NotoSans-Medium.ttf | Hindi | Hindi |
| fr | French | NotoSans-Medium.ttf | Hindi | Hindi |
| es | Spanish | NotoSans-Medium.ttf | Hindi | Hindi |
| de | German | NotoSans-Medium.ttf | Hindi | Hindi |
| ru | Russian | NotoSans-Medium.ttf | Hindi | Hindi |
| ar | Arabic | NotoSansArabic-Medium.ttf | Oo | Hindi |
| fa | Persian (Farsi) | NotoSansArabic-Medium.ttf | Oo | Hindi |
| ur | Urdu | NotoSansArabic-Medium.ttf | Oo | Hindi |
| zh-CN | Chinese (Simplified) | NotoSansCJK-Medium.ttc | Hindi | Hindi |
| zh-MO | Chinese (Traditional, Macau) | NotoSansCJK-Medium.ttc | Hindi | Hindi |
| zh-HK | Chinese (Traditional, Hong Kong) | NotoSansCJK-Medium.ttc | Hindi | Hindi |
| zh-TW | Chinese (Traditional, Taiwan) | NotoSansCJK-Medium.ttc | Hindi | Hindi |
| ja | Japanese | NotoSansCJK-Medium.ttc | Hindi | Hindi |
| ko | Korean | NotoSansCJK-Medium.ttc | Hindi | Hindi |
| hi | Hindi | NotoSansDevanagari-Medium.ttf | Hindi | Hindi |
| bn | Bengali | NotoSansBengali-Medium.ttf | Hindi | Hindi |
| mr | Marathi | NotoSansDevanagari-Medium.ttf | Hindi | Hindi |
| ne | Nepali | NotoSansDevanagari-Medium.ttf | Hindi | Hindi |
| pa | Punjabi (Gurmukhi) | NotoSansGurmukhi-Medium.ttf | Hindi | Hindi |
| pt-PT | Portuguese (Portugal) | NotoSans-Medium.ttf | Hindi | Hindi |
| pt-BR | Portuguese (Brazil) | NotoSans-Medium.ttf | Hindi | Hindi |
| it | Italian | NotoSans-Medium.ttf | Hindi | Hindi |
| lt | Lithuanian | NotoSans-Medium.ttf | Hindi | Hindi |
| pl | Polish | NotoSans-Medium.ttf | Hindi | Hindi |
| tr | Turkish | NotoSans-Medium.ttf | Hindi | Hindi |
| el | Greek | NotoSans-Medium.ttf | Hindi | Hindi |
| th | Thai | NotoSansThai-Medium.ttf | Hindi | Hindi |
| sv | Swedish | NotoSans-Medium.ttf | Hindi | Hindi |
| da | Danish | NotoSans-Medium.ttf | Hindi | Hindi |
| no | Norwegian | NotoSans-Medium.ttf | Hindi | Hindi |
| fi | Finnish | NotoSans-Medium.ttf | Hindi | Hindi |
| nl | Dutch | NotoSans-Medium.ttf | Hindi | Hindi |
| he | Hebrew | NotoSansHebrew-Medium.ttf | Oo | Hindi |
| vi | Vietnamese | NotoSans-Medium.ttf | Hindi | Hindi |
| id | Indonesian | NotoSans-Medium.ttf | Hindi | Hindi |
| ms | Malay | NotoSans-Medium.ttf | Hindi | Hindi |
| tl | Tagalog (Filipino) | NotoSans-Medium.ttf | Hindi | Hindi |
| sw | Swahili | NotoSans-Medium.ttf | Hindi | Hindi |
| hu | Hungarian | NotoSans-Medium.ttf | Hindi | Hindi |
| cs | Czech | NotoSans-Medium.ttf | Hindi | Hindi |
| sk | Slovak | NotoSans-Medium.ttf | Hindi | Hindi |
| ro | Romanian | NotoSans-Medium.ttf | Hindi | Hindi |
| bg | Bulgarian | NotoSans-Medium.ttf | Hindi | Hindi |
| sr | Serbian (Cyrillic) | NotoSans-Medium.ttf | Hindi | Hindi |
| hr | Croatian | NotoSans-Medium.ttf | Hindi | Hindi |
| sl | Slovenian | NotoSans-Medium.ttf | Hindi | Hindi |
| uk | Ukrainian | NotoSans-Medium.ttf | Hindi | Hindi |
| my | Burmese (Myanmar) | NotoSansMyanmar-Medium.ttf | Hindi | Hindi |
| ta | Tamil | NotoSansTamil-Medium.ttf | Hindi | Hindi |
| et | Estonian | NotoSans-Medium.ttf | Hindi | Hindi |
| pcm | Nigerian Pidgin | NotoSans-Medium.ttf | Hindi | Hindi |
| te | Telugu | NotoSans-Medium.ttf | Hindi | Hindi |
| ml | Malayalam | NotoSans-Medium.ttf | Hindi | Hindi |
| kn | Kannada | NotoSans-Medium.ttf | Hindi | Hindi |
| km | Khmer | NotoSansKhmer-Medium.ttf | Hindi | Hindi |
| mni | Manipuri (Meitei Mayek) | NotoSansMeeteiMayek-Medium.ttf | Hindi | Hindi |

## Magdagdag ng Wika

Upang magdagdag ng suporta para sa bagong wika:

1. Idagdag ang code ng wika at ipinapakitang pangalan sa mga utility ng wika.
2. Magdagdag o i-map ang isang font sa `src/co_op_translator/fonts/font_language_mappings.yml`.
3. Subukan ang output ng pagsasalin ng Markdown at imahe.
4. Magbukas ng pull request na may kasamang mapping at mga tala ng pagpapatunay.