# Bahasa yang Didukung

Co-op Translator mendukung kode bahasa berikut untuk keluaran terjemahan teks, notebook, dan gambar.

Jika Anda ingin menambahkan bahasa baru, perbarui pemetaan bahasa dan font di bawah `src/co_op_translator/fonts/` dan uji bahasa tersebut sebelum membuka pull request.

| Language Code | Language Name | Font | RTL Support | Known Issues |
| --- | --- | --- | --- | --- |
| en | English | NotoSans-Medium.ttf | Tidak | Tidak |
| fr | French | NotoSans-Medium.ttf | Tidak | Tidak |
| es | Spanish | NotoSans-Medium.ttf | Tidak | Tidak |
| de | German | NotoSans-Medium.ttf | Tidak | Tidak |
| ru | Russian | NotoSans-Medium.ttf | Tidak | Tidak |
| ar | Arabic | NotoSansArabic-Medium.ttf | Ya | Tidak |
| fa | Persian (Farsi) | NotoSansArabic-Medium.ttf | Ya | Tidak |
| ur | Urdu | NotoSansArabic-Medium.ttf | Ya | Tidak |
| zh-CN | Chinese (Simplified) | NotoSansCJK-Medium.ttc | Tidak | Tidak |
| zh-MO | Chinese (Traditional, Macau) | NotoSansCJK-Medium.ttc | Tidak | Tidak |
| zh-HK | Chinese (Traditional, Hong Kong) | NotoSansCJK-Medium.ttc | Tidak | Tidak |
| zh-TW | Chinese (Traditional, Taiwan) | NotoSansCJK-Medium.ttc | Tidak | Tidak |
| ja | Japanese | NotoSansCJK-Medium.ttc | Tidak | Tidak |
| ko | Korean | NotoSansCJK-Medium.ttc | Tidak | Tidak |
| hi | Hindi | NotoSansDevanagari-Medium.ttf | Tidak | Tidak |
| bn | Bengali | NotoSansBengali-Medium.ttf | Tidak | Tidak |
| mr | Marathi | NotoSansDevanagari-Medium.ttf | Tidak | Tidak |
| ne | Nepali | NotoSansDevanagari-Medium.ttf | Tidak | Tidak |
| pa | Punjabi (Gurmukhi) | NotoSansGurmukhi-Medium.ttf | Tidak | Tidak |
| pt-PT | Portuguese (Portugal) | NotoSans-Medium.ttf | Tidak | Tidak |
| pt-BR | Portuguese (Brazil) | NotoSans-Medium.ttf | Tidak | Tidak |
| it | Italian | NotoSans-Medium.ttf | Tidak | Tidak |
| lt | Lithuanian | NotoSans-Medium.ttf | Tidak | Tidak |
| pl | Polish | NotoSans-Medium.ttf | Tidak | Tidak |
| tr | Turkish | NotoSans-Medium.ttf | Tidak | Tidak |
| el | Greek | NotoSans-Medium.ttf | Tidak | Tidak |
| th | Thai | NotoSansThai-Medium.ttf | Tidak | Tidak |
| sv | Swedish | NotoSans-Medium.ttf | Tidak | Tidak |
| da | Danish | NotoSans-Medium.ttf | Tidak | Tidak |
| no | Norwegian | NotoSans-Medium.ttf | Tidak | Tidak |
| fi | Finnish | NotoSans-Medium.ttf | Tidak | Tidak |
| nl | Dutch | NotoSans-Medium.ttf | Tidak | Tidak |
| he | Hebrew | NotoSansHebrew-Medium.ttf | Ya | Tidak |
| vi | Vietnamese | NotoSans-Medium.ttf | Tidak | Tidak |
| id | Indonesian | NotoSans-Medium.ttf | Tidak | Tidak |
| ms | Malay | NotoSans-Medium.ttf | Tidak | Tidak |
| tl | Tagalog (Filipino) | NotoSans-Medium.ttf | Tidak | Tidak |
| sw | Swahili | NotoSans-Medium.ttf | Tidak | Tidak |
| hu | Hungarian | NotoSans-Medium.ttf | Tidak | Tidak |
| cs | Czech | NotoSans-Medium.ttf | Tidak | Tidak |
| sk | Slovak | NotoSans-Medium.ttf | Tidak | Tidak |
| ro | Romanian | NotoSans-Medium.ttf | Tidak | Tidak |
| bg | Bulgarian | NotoSans-Medium.ttf | Tidak | Tidak |
| sr | Serbian (Cyrillic) | NotoSans-Medium.ttf | Tidak | Tidak |
| hr | Croatian | NotoSans-Medium.ttf | Tidak | Tidak |
| sl | Slovenian | NotoSans-Medium.ttf | Tidak | Tidak |
| uk | Ukrainian | NotoSans-Medium.ttf | Tidak | Tidak |
| my | Burmese (Myanmar) | NotoSansMyanmar-Medium.ttf | Tidak | Tidak |
| ta | Tamil | NotoSansTamil-Medium.ttf | Tidak | Tidak |
| et | Estonian | NotoSans-Medium.ttf | Tidak | Tidak |
| pcm | Nigerian Pidgin | NotoSans-Medium.ttf | Tidak | Tidak |
| te | Telugu | NotoSans-Medium.ttf | Tidak | Tidak |
| ml | Malayalam | NotoSans-Medium.ttf | Tidak | Tidak |
| kn | Kannada | NotoSans-Medium.ttf | Tidak | Tidak |
| km | Khmer | NotoSansKhmer-Medium.ttf | Tidak | Tidak |

## Menambahkan Bahasa

Untuk menambahkan dukungan untuk bahasa baru:

1. Tambahkan kode bahasa dan nama tampilan ke utilitas bahasa.
2. Tambahkan atau petakan font di `src/co_op_translator/fonts/font_language_mappings.yml`.
3. Uji keluaran terjemahan Markdown dan gambar.
4. Buka pull request dengan pemetaan dan catatan validasi.