<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0788d7ebe4876c9be89132f48e09b26d",
  "translation_date": "2025-05-06T17:51:17+00:00",
  "source_file": "getting_started/troubleshooting.md",
  "language_code": "id"
}
-->
# Microsoft Co-op Translator Troubleshooting Guide


## Ikhtisar
Microsoft Co-Op Translator adalah alat yang kuat untuk menerjemahkan dokumen Markdown dengan mulus. Panduan ini akan membantu Anda mengatasi masalah umum yang ditemui saat menggunakan alat ini.

## Masalah Umum dan Solusinya

### 1. Masalah Tag Markdown
**Masalah:** Dokumen Markdown yang diterjemahkan menyertakan tag `markdown` di bagian atas, menyebabkan masalah rendering.

**Solusi:** Untuk mengatasinya, cukup hapus tag `markdown` di bagian atas file. Ini akan memungkinkan file Markdown dirender dengan benar.

**Langkah-langkah:**
1. Buka file Markdown yang diterjemahkan (`.md`).
2. Temukan tag `markdown` di bagian atas dokumen.
3. Hapus tag `markdown`.
4. Simpan perubahan pada file.
5. Buka kembali file untuk memastikan file dirender dengan benar.

### 2. Masalah URL Gambar Tersemat
**Masalah:** URL gambar tersemat tidak sesuai dengan lokal bahasa, sehingga gambar menjadi salah atau tidak muncul.

**Solusi:** Periksa URL gambar tersemat dan pastikan sesuai dengan lokal bahasa. Semua gambar berada di folder `translated_images` dan setiap gambar memiliki tag lokal bahasa pada nama file gambar.

**Langkah-langkah:**
1. Buka dokumen Markdown yang diterjemahkan.
2. Identifikasi gambar tersemat dan URL-nya.
3. Verifikasi bahwa lokal bahasa pada nama file gambar sesuai dengan bahasa dokumen.
4. Perbarui URL jika diperlukan.
5. Simpan perubahan dan buka kembali dokumen untuk memastikan gambar muncul dengan benar.

### 3. Akurasi Terjemahan
**Masalah:** Konten yang diterjemahkan tidak akurat atau memerlukan pengeditan lebih lanjut.

**Solusi:** Tinjau dokumen terjemahan dan lakukan pengeditan yang diperlukan untuk meningkatkan akurasi dan keterbacaan.

**Langkah-langkah:**
1. Buka dokumen terjemahan.
2. Tinjau isi dengan teliti.
3. Lakukan pengeditan yang diperlukan untuk meningkatkan akurasi terjemahan.
4. Simpan perubahan.

### 4. Masalah Format File
**Masalah:** Format dokumen terjemahan tidak benar. Ini bisa terjadi pada tabel, di sini tambahan ``` are added.

**Solution:** Adjust the formatting of the document to match the original structure. Simply deleting the ``` akan mengatasi masalah tabel.

**Langkah-langkah:**
1. Buka dokumen terjemahan.
2. Bandingkan dengan dokumen asli untuk mengidentifikasi masalah format.
3. Sesuaikan format agar sesuai dengan dokumen asli.
4. Simpan perubahan.

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berusaha untuk akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau salah tafsir yang timbul dari penggunaan terjemahan ini.