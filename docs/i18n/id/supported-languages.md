# Bahasa yang Didukung

Co-op Translator mendukung kode bahasa berikut untuk keluaran terjemahan teks, notebook, dan gambar.

Jika Anda ingin menambahkan bahasa baru, perbarui pemetaan bahasa dan font di bawah `src/co_op_translator/fonts/` dan uji bahasa tersebut sebelum membuka pull request.

| Kode Bahasa | Nama Bahasa | Font | Dukungan RTL | Masalah Dikenal |
| --- | --- | --- | --- | --- |
| en | Inggris | NotoSans-Medium.ttf | Tidak | Tidak |
| fr | Prancis | NotoSans-Medium.ttf | Tidak | Tidak |
| es | Spanyol | NotoSans-Medium.ttf | Tidak | Tidak |
| de | Jerman | NotoSans-Medium.ttf | Tidak | Tidak |
| ru | Rusia | NotoSans-Medium.ttf | Tidak | Tidak |
| ar | Arab | NotoSansArabic-Medium.ttf | Ya | Tidak |
| fa | Persia (Farsi) | NotoSansArabic-Medium.ttf | Ya | Tidak |
| ur | Urdu | NotoSansArabic-Medium.ttf | Ya | Tidak |
| zh-CN | Cina (Sederhana) | NotoSansCJK-Medium.ttc | Tidak | Tidak |
| zh-MO | Cina (Tradisional, Makau) | NotoSansCJK-Medium.ttc | Tidak | Tidak |
| zh-HK | Cina (Tradisional, Hong Kong) | NotoSansCJK-Medium.ttc | Tidak | Tidak |
| zh-TW | Cina (Tradisional, Taiwan) | NotoSansCJK-Medium.ttc | Tidak | Tidak |
| ja | Jepang | NotoSansCJK-Medium.ttc | Tidak | Tidak |
| ko | Korea | NotoSansCJK-Medium.ttc | Tidak | Tidak |
| hi | Hindi | NotoSansDevanagari-Medium.ttf | Tidak | Tidak |
| bn | Benggali | NotoSansBengali-Medium.ttf | Tidak | Tidak |
| mr | Marathi | NotoSansDevanagari-Medium.ttf | Tidak | Tidak |
| ne | Nepali | NotoSansDevanagari-Medium.ttf | Tidak | Tidak |
| pa | Punjabi (Gurmukhi) | NotoSansGurmukhi-Medium.ttf | Tidak | Tidak |
| pt-PT | Portugis (Portugal) | NotoSans-Medium.ttf | Tidak | Tidak |
| pt-BR | Portugis (Brasil) | NotoSans-Medium.ttf | Tidak | Tidak |
| it | Italia | NotoSans-Medium.ttf | Tidak | Tidak |
| lt | Lituania | NotoSans-Medium.ttf | Tidak | Tidak |
| pl | Polandia | NotoSans-Medium.ttf | Tidak | Tidak |
| tr | Turki | NotoSans-Medium.ttf | Tidak | Tidak |
| el | Yunani | NotoSans-Medium.ttf | Tidak | Tidak |
| th | Thai | NotoSansThai-Medium.ttf | Tidak | Tidak |
| sv | Swedia | NotoSans-Medium.ttf | Tidak | Tidak |
| da | Denmark | NotoSans-Medium.ttf | Tidak | Tidak |
| no | Norwegia | NotoSans-Medium.ttf | Tidak | Tidak |
| fi | Finlandia | NotoSans-Medium.ttf | Tidak | Tidak |
| nl | Belanda | NotoSans-Medium.ttf | Tidak | Tidak |
| he | Ibrani | NotoSansHebrew-Medium.ttf | Ya | Tidak |
| vi | Vietnam | NotoSans-Medium.ttf | Tidak | Tidak |
| id | Indonesia | NotoSans-Medium.ttf | Tidak | Tidak |
| ms | Melayu | NotoSans-Medium.ttf | Tidak | Tidak |
| tl | Tagalog (Filipina) | NotoSans-Medium.ttf | Tidak | Tidak |
| sw | Swahili | NotoSans-Medium.ttf | Tidak | Tidak |
| hu | Hungaria | NotoSans-Medium.ttf | Tidak | Tidak |
| cs | Ceko | NotoSans-Medium.ttf | Tidak | Tidak |
| sk | Slowakia | NotoSans-Medium.ttf | Tidak | Tidak |
| ro | Rumania | NotoSans-Medium.ttf | Tidak | Tidak |
| bg | Bulgaria | NotoSans-Medium.ttf | Tidak | Tidak |
| sr | Serbia (Sirilik) | NotoSans-Medium.ttf | Tidak | Tidak |
| hr | Kroasia | NotoSans-Medium.ttf | Tidak | Tidak |
| sl | Slovenia | NotoSans-Medium.ttf | Tidak | Tidak |
| uk | Ukraina | NotoSans-Medium.ttf | Tidak | Tidak |
| my | Birma (Myanmar) | NotoSansMyanmar-Medium.ttf | Tidak | Tidak |
| ta | Tamil | NotoSansTamil-Medium.ttf | Tidak | Tidak |
| et | Estonia | NotoSans-Medium.ttf | Tidak | Tidak |
| pcm | Pidgin Nigeria | NotoSans-Medium.ttf | Tidak | Tidak |
| te | Telugu | NotoSans-Medium.ttf | Tidak | Tidak |
| ml | Malayalam | NotoSans-Medium.ttf | Tidak | Tidak |
| kn | Kannada | NotoSans-Medium.ttf | Tidak | Tidak |
| km | Khmer | NotoSansKhmer-Medium.ttf | Tidak | Tidak |
| mni | Manipuri (Meitei Mayek) | NotoSansMeeteiMayek-Medium.ttf | Tidak | Tidak |

## Menambahkan Bahasa

Untuk menambahkan dukungan untuk bahasa baru:

1. Tambahkan kode bahasa dan nama tampilan ke utilitas bahasa.
2. Tambahkan atau petakan font di `src/co_op_translator/fonts/font_language_mappings.yml`.
3. Uji keluaran terjemahan Markdown dan gambar.
4. Buka pull request dengan pemetaan dan catatan validasi.