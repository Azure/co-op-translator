<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0788d7ebe4876c9be89132f48e09b26d",
  "translation_date": "2025-06-12T12:29:00+00:00",
  "source_file": "getting_started/troubleshooting.md",
  "language_code": "id"
}
-->
# Microsoft Co-op Translator Troubleshooting Guide


## Overview
Microsoft Co-Op Translator adalah alat yang kuat untuk menerjemahkan dokumen Markdown dengan mulus. Panduan ini akan membantu Anda mengatasi masalah umum yang ditemui saat menggunakan alat ini.

## Common Issues and Solutions

### 1. Markdown Tag Issue
**Problem:** Dokumen Markdown yang diterjemahkan menyertakan tag `markdown` di bagian atas, menyebabkan masalah rendering.

**Solution:** Untuk mengatasinya, cukup hapus tag `markdown` di bagian atas file. Ini akan memungkinkan file Markdown ditampilkan dengan benar.

**Steps:**
1. Buka file Markdown yang diterjemahkan (`.md`).
2. Temukan tag `markdown` di bagian atas dokumen.
3. Hapus tag `markdown`.
4. Simpan perubahan pada file.
5. Buka kembali file untuk memastikan tampilannya sudah benar.

### 2. Embedded Images URL Issue
**Problem:** URL gambar yang disematkan tidak sesuai dengan lokal bahasa, sehingga gambar tampil salah atau hilang.

**Solution:** Periksa URL gambar yang disematkan dan pastikan sesuai dengan lokal bahasa. Semua gambar berada di folder `translated_images` dan setiap gambar memiliki tag lokal bahasa dalam nama file gambarnya.

**Steps:**
1. Buka dokumen Markdown yang diterjemahkan.
2. Identifikasi gambar yang disematkan dan URL-nya.
3. Pastikan lokal bahasa dalam nama file gambar sesuai dengan bahasa dokumen.
4. Perbarui URL jika diperlukan.
5. Simpan perubahan dan buka kembali dokumen untuk memastikan gambar tampil dengan benar.

### 3. Translation Accuracy
**Problem:** Konten terjemahan tidak akurat atau memerlukan penyuntingan lebih lanjut.

**Solution:** Tinjau dokumen terjemahan dan lakukan penyuntingan yang diperlukan untuk meningkatkan akurasi dan keterbacaan.

**Steps:**
1. Buka dokumen terjemahan.
2. Tinjau isi dengan teliti.
3. Lakukan penyuntingan yang diperlukan untuk meningkatkan akurasi terjemahan.
4. Simpan perubahan.

### 4. File Formatting Issues
**Problem:** Format dokumen terjemahan tidak benar. Ini bisa terjadi pada tabel, di sini tambahan ``` are added.

**Solution:** Adjust the formatting of the document to match the original structure. Simply deleting the ``` akan mengatasi masalah tabel.

**Steps:**
1. Buka dokumen terjemahan.
2. Bandingkan dengan dokumen asli untuk mengidentifikasi masalah format.
3. Sesuaikan format agar sesuai dengan dokumen asli.
4. Simpan perubahan.

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berusaha untuk akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sahih. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang salah yang timbul dari penggunaan terjemahan ini.