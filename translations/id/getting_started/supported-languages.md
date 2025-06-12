<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b4ed48f23ec418b31e90a02fe629fcde",
  "translation_date": "2025-06-12T12:15:00+00:00",
  "source_file": "getting_started/supported-languages.md",
  "language_code": "id"
}
-->
# Bahasa yang Didukung

Tabel di bawah ini mencantumkan bahasa-bahasa yang saat ini didukung oleh **Co-op Translator**. Tabel ini mencakup kode bahasa, nama bahasa, dan masalah yang diketahui terkait masing-masing bahasa. Jika Anda ingin menambahkan dukungan untuk bahasa baru, silakan tambahkan kode bahasa, nama, dan font yang sesuai di file `font_language_mappings.yml` yang terletak di `src/co_op_translator/fonts/` dan kirimkan pull request setelah melakukan pengujian.

| Kode Bahasa | Nama Bahasa          | Font                              | Dukungan RTL | Masalah Diketahui |
|-------------|---------------------|----------------------------------|--------------|-------------------|
| en          | English             | NotoSans-Medium.ttf              | Tidak        | Tidak             |
| fr          | French              | NotoSans-Medium.ttf              | Tidak        | Tidak             |
| es          | Spanish             | NotoSans-Medium.ttf              | Tidak        | Tidak             |
| de          | German              | NotoSans-Medium.ttf              | Tidak        | Tidak             |
| ru          | Russian             | NotoSans-Medium.ttf              | Tidak        | Tidak             |
| ar          | Arabic              | NotoSansArabic-Medium.ttf        | Ya           | Tidak             |
| fa          | Persian (Farsi)     | NotoSansArabic-Medium.ttf        | Tidak        | Tidak             |
| ur          | Urdu                | NotoSansArabic-Medium.ttf        | Tidak        | Tidak             |
| zh          | Chinese (Simplified)| NotoSansCJK-Medium.ttc           | Tidak        | Tidak             |
| mo          | Chinese (Traditional, Macau) | NotoSansCJK-Medium.ttc   | Tidak        | Tidak             |
| hk          | Chinese (Traditional, Hong Kong) | NotoSansCJK-Medium.ttc | Tidak        | Tidak             |
| tw          | Chinese (Traditional, Taiwan) | NotoSansCJK-Medium.ttc    | Tidak        | Tidak             |
| ja          | Japanese            | NotoSansCJK-Medium.ttc           | Tidak        | Tidak             |
| ko          | Korean              | NotoSansCJK-Medium.ttc           | Tidak        | Tidak             |
| hi          | Hindi               | NotoSansDevanagari-Medium.ttf    | Tidak        | Tidak             |
| bn          | Bengali             | NotoSansBengali-Medium.ttf       | Tidak        | Tidak             |
| mr          | Marathi             | NotoSansDevanagari-Medium.ttf    | Tidak        | Tidak             |
| ne          | Nepali              | NotoSansDevanagari-Medium.ttf    | Tidak        | Tidak             |
| pa          | Punjabi (Gurmukhi)  | NotoSansGurmukhi-Medium.ttf      | Tidak        | Tidak             |
| pt          | Portuguese (Portugal)| NotoSans-Medium.ttf              | Tidak        | Tidak             |
| br          | Portuguese (Brazil) | NotoSans-Medium.ttf              | Tidak        | Tidak             |
| it          | Italian             | NotoSans-Medium.ttf              | Tidak        | Tidak             |
| pl          | Polish              | NotoSans-Medium.ttf              | Tidak        | Tidak             |
| tr          | Turkish             | NotoSans-Medium.ttf              | Tidak        | Tidak             |
| el          | Greek               | NotoSans-Medium.ttf              | Tidak        | Tidak             |
| th          | Thai                | NotoSansThai-Medium.ttf          | Tidak        | Tidak             |
| sv          | Swedish             | NotoSans-Medium.ttf              | Tidak        | Tidak             |
| da          | Danish              | NotoSans-Medium.ttf              | Tidak        | Tidak             |
| no          | Norwegian           | NotoSans-Medium.ttf              | Tidak        | Tidak             |
| fi          | Finnish             | NotoSans-Medium.ttf              | Tidak        | Tidak             |
| nl          | Dutch               | NotoSans-Medium.ttf              | Tidak        | Tidak             |
| he          | Hebrew              | NotoSansHebrew-Medium.ttf        | Tidak        | Tidak             |
| vi          | Vietnamese          | NotoSans-Medium.ttf              | Tidak        | Tidak             |
| id          | Indonesian          | NotoSans-Medium.ttf              | Tidak        | Tidak             |
| ms          | Malay               | NotoSans-Medium.ttf              | Tidak        | Tidak             |
| tl          | Tagalog (Filipino)  | NotoSans-Medium.ttf              | Tidak        | Tidak             |
| sw          | Swahili             | NotoSans-Medium.ttf              | Tidak        | Tidak             |
| hu          | Hungarian           | NotoSans-Medium.ttf              | Tidak        | Tidak             |
| cs          | Czech               | NotoSans-Medium.ttf              | Tidak        | Tidak             |
| sk          | Slovak              | NotoSans-Medium.ttf              | Tidak        | Tidak             |
| ro          | Romanian            | NotoSans-Medium.ttf              | Tidak        | Tidak             |
| bg          | Bulgarian           | NotoSans-Medium.ttf              | Tidak        | Tidak             |
| sr          | Serbian (Cyrillic)  | NotoSans-Medium.ttf              | Tidak        | Tidak             |
| hr          | Croatian            | NotoSans-Medium.ttf              | Tidak        | Tidak             |
| sl          | Slovenian           | NotoSans-Medium.ttf              | Tidak        | Tidak             |
| uk          | Ukrainian           | NotoSans-Medium.ttf              | Tidak        | Tidak             |
| my          | Burmese (Myanmar)   | NotoSans-Medium.ttf              | Tidak        | Tidak             |

## Menambahkan bahasa baru

Untuk menambahkan dukungan bahasa baru:

1. Buka [src/co_op_translator/fonts/font_language_mappings.yml](https://github.com/Azure/co-op-translator/blob/main/src/co_op_translator/fonts/font_language_mappings.yml).
2. Tambahkan kode bahasa, nama, dan nama file font yang sesuai. Pastikan untuk menyertakan atribut `rtl` jika bahasa tersebut menggunakan arah kanan-ke-kiri.
3. Jika Anda perlu menggunakan font baru, pastikan font tersebut bebas digunakan dalam proyek open-source dengan memeriksa lisensi dan ketentuan hak cipta. Setelah diverifikasi, tambahkan file font ke direktori `src/co_op_translator/fonts/`.
4. Uji perubahan Anda secara lokal untuk memastikan bahasa baru didukung dengan benar.
5. Kirimkan Pull Request dengan perubahan Anda dan cantumkan penambahan bahasa baru dalam deskripsi PR.

Contoh:

```yaml
new_lang:
  name: "New Language"
  font: "NotoSans-Medium.ttf"
  rtl: false
```

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berusaha untuk akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang otoritatif. Untuk informasi yang sangat penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau salah tafsir yang timbul dari penggunaan terjemahan ini.