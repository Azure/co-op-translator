<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b38d8f042530a4bc872def7cb2c141cd",
  "translation_date": "2025-05-06T17:42:46+00:00",
  "source_file": "getting_started/command-reference.md",
  "language_code": "id"
}
-->
# Command reference
CLI **Co-op Translator** menawarkan beberapa opsi untuk menyesuaikan proses terjemahan:

Command                                       | Deskripsi
----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"                 | Menerjemahkan proyek Anda ke bahasa yang ditentukan. Contoh: translate -l "es fr de" menerjemahkan ke bahasa Spanyol, Prancis, dan Jerman. Gunakan translate -l "all" untuk menerjemahkan ke semua bahasa yang didukung.
translate -l "language_codes" -u              | Memperbarui terjemahan dengan menghapus yang sudah ada dan membuat ulang. Peringatan: Ini akan menghapus semua terjemahan saat ini untuk bahasa yang ditentukan.
translate -l "language_codes" -img            | Menerjemahkan hanya file gambar.
translate -l "language_codes" -md             | Menerjemahkan hanya file Markdown.
translate -l "language_codes" -chk            | Memeriksa file terjemahan untuk kesalahan dan mencoba ulang terjemahan jika perlu.
translate -l "language_codes" -d              | Mengaktifkan mode debug untuk pencatatan yang lebih rinci.
translate -l "language_codes" -r "root_dir"   | Menentukan direktori root dari proyek
translate -l "language_codes" -f              | Menggunakan mode cepat untuk terjemahan gambar (hingga 3x lebih cepat dengan sedikit pengorbanan kualitas dan penyesuaian).
translate -l "language_codes" -y              | Secara otomatis mengonfirmasi semua prompt (berguna untuk pipeline CI/CD)
translate -l "language_codes" --help          | detail bantuan dalam CLI yang menampilkan perintah yang tersedia

### Contoh penggunaan:

  1. Perilaku default (menambahkan terjemahan baru tanpa menghapus yang sudah ada):   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. Menambahkan hanya terjemahan gambar Korea baru (tidak menghapus terjemahan yang sudah ada):    translate -l "ko" -img

  3. Memperbarui semua terjemahan Korea (Peringatan: Ini menghapus semua terjemahan Korea yang ada sebelum menerjemahkan ulang):    translate -l "ko" -u

  4. Memperbarui hanya gambar Korea (Peringatan: Ini menghapus semua gambar Korea yang ada sebelum menerjemahkan ulang):    translate -l "ko" -img -u

  5. Menambahkan terjemahan markdown baru untuk bahasa Korea tanpa memengaruhi terjemahan lain:    translate -l "ko" -md

  6. Memeriksa file terjemahan untuk kesalahan dan mencoba ulang terjemahan jika perlu: translate -l "ko" -chk

  7. Memeriksa file terjemahan untuk kesalahan dan mencoba ulang terjemahan (hanya markdown): translate -l "ko" -chk -md

  8. Memeriksa file terjemahan untuk kesalahan dan mencoba ulang terjemahan (hanya gambar): translate -l "ko" -chk -img

  9. Menggunakan mode cepat untuk terjemahan gambar:    translate -l "ko" -img -f

  10. Contoh mode debug: - translate -l "ko" -d: Mengaktifkan pencatatan debug.

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk akurasi, harap diingat bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sahih. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau salah tafsir yang timbul dari penggunaan terjemahan ini.