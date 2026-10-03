# Bahasa Disokong

Co-op Translator menyokong kod bahasa berikut untuk keluaran terjemahan teks, notebook, dan imej.

Jika anda ingin menambah bahasa baharu, kemas kini pemetaan bahasa dan fon di bawah `src/co_op_translator/fonts/` dan uji bahasa tersebut sebelum membuka pull request.

| Kod Bahasa | Nama Bahasa | Fon | Sokongan RTL | Isu Dikenali |
| --- | --- | --- | --- | --- |
| en | English | NotoSans-Medium.ttf | Tidak | Tiada |
| fr | French | NotoSans-Medium.ttf | Tidak | Tiada |
| es | Spanish | NotoSans-Medium.ttf | Tidak | Tiada |
| de | German | NotoSans-Medium.ttf | Tidak | Tiada |
| ru | Russian | NotoSans-Medium.ttf | Tidak | Tiada |
| ar | Arabic | NotoSansArabic-Medium.ttf | Ya | Tiada |
| fa | Persian (Farsi) | NotoSansArabic-Medium.ttf | Ya | Tiada |
| ur | Urdu | NotoSansArabic-Medium.ttf | Ya | Tiada |
| zh-CN | Chinese (Simplified) | NotoSansCJK-Medium.ttc | Tidak | Tiada |
| zh-MO | Chinese (Traditional, Macau) | NotoSansCJK-Medium.ttc | Tidak | Tiada |
| zh-HK | Chinese (Traditional, Hong Kong) | NotoSansCJK-Medium.ttc | Tidak | Tiada |
| zh-TW | Chinese (Traditional, Taiwan) | NotoSansCJK-Medium.ttc | Tidak | Tiada |
| ja | Japanese | NotoSansCJK-Medium.ttc | Tidak | Tiada |
| ko | Korean | NotoSansCJK-Medium.ttc | Tidak | Tiada |
| hi | Hindi | NotoSansDevanagari-Medium.ttf | Tidak | Tiada |
| bn | Bengali | NotoSansBengali-Medium.ttf | Tidak | Tiada |
| mr | Marathi | NotoSansDevanagari-Medium.ttf | Tidak | Tiada |
| ne | Nepali | NotoSansDevanagari-Medium.ttf | Tidak | Tiada |
| pa | Punjabi (Gurmukhi) | NotoSansGurmukhi-Medium.ttf | Tidak | Tiada |
| pt-PT | Portuguese (Portugal) | NotoSans-Medium.ttf | Tidak | Tiada |
| pt-BR | Portuguese (Brazil) | NotoSans-Medium.ttf | Tidak | Tiada |
| it | Italian | NotoSans-Medium.ttf | Tidak | Tiada |
| lt | Lithuanian | NotoSans-Medium.ttf | Tidak | Tiada |
| pl | Polish | NotoSans-Medium.ttf | Tidak | Tiada |
| tr | Turkish | NotoSans-Medium.ttf | Tidak | Tiada |
| el | Greek | NotoSans-Medium.ttf | Tidak | Tiada |
| th | Thai | NotoSansThai-Medium.ttf | Tidak | Tiada |
| sv | Swedish | NotoSans-Medium.ttf | Tidak | Tiada |
| da | Danish | NotoSans-Medium.ttf | Tidak | Tiada |
| no | Norwegian | NotoSans-Medium.ttf | Tidak | Tiada |
| fi | Finnish | NotoSans-Medium.ttf | Tidak | Tiada |
| nl | Dutch | NotoSans-Medium.ttf | Tidak | Tiada |
| he | Hebrew | NotoSansHebrew-Medium.ttf | Ya | Tiada |
| vi | Vietnamese | NotoSans-Medium.ttf | Tidak | Tiada |
| id | Indonesian | NotoSans-Medium.ttf | Tidak | Tiada |
| ms | Malay | NotoSans-Medium.ttf | Tidak | Tiada |
| tl | Tagalog (Filipino) | NotoSans-Medium.ttf | Tidak | Tiada |
| sw | Swahili | NotoSans-Medium.ttf | Tidak | Tiada |
| hu | Hungarian | NotoSans-Medium.ttf | Tidak | Tiada |
| cs | Czech | NotoSans-Medium.ttf | Tidak | Tiada |
| sk | Slovak | NotoSans-Medium.ttf | Tidak | Tiada |
| ro | Romanian | NotoSans-Medium.ttf | Tidak | Tiada |
| bg | Bulgarian | NotoSans-Medium.ttf | Tidak | Tiada |
| sr | Serbian (Cyrillic) | NotoSans-Medium.ttf | Tidak | Tiada |
| hr | Croatian | NotoSans-Medium.ttf | Tidak | Tiada |
| sl | Slovenian | NotoSans-Medium.ttf | Tidak | Tiada |
| uk | Ukrainian | NotoSans-Medium.ttf | Tidak | Tiada |
| my | Burmese (Myanmar) | NotoSansMyanmar-Medium.ttf | Tidak | Tiada |
| ta | Tamil | NotoSansTamil-Medium.ttf | Tidak | Tiada |
| et | Estonian | NotoSans-Medium.ttf | Tidak | Tiada |
| pcm | Nigerian Pidgin | NotoSans-Medium.ttf | Tidak | Tiada |
| te | Telugu | NotoSans-Medium.ttf | Tidak | Tiada |
| ml | Malayalam | NotoSans-Medium.ttf | Tidak | Tiada |
| kn | Kannada | NotoSans-Medium.ttf | Tidak | Tiada |
| km | Khmer | NotoSansKhmer-Medium.ttf | Tidak | Tiada |
| mni | Manipuri (Meitei Mayek) | NotoSansMeeteiMayek-Medium.ttf | Tidak | Tiada |

## Tambah Bahasa

Untuk menambah sokongan bagi bahasa baharu:

1. Tambahkan kod bahasa dan nama paparan kepada utiliti bahasa.
2. Tambah atau petakan fon dalam `src/co_op_translator/fonts/font_language_mappings.yml`.
3. Uji keluaran terjemahan Markdown dan imej.
4. Buka pull request dengan pemetaan dan nota pengesahan.