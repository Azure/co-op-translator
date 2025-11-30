<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "822238e4451d04bb152cebb1be6f13c2",
  "translation_date": "2025-11-30T11:50:00+00:00",
  "source_file": "getting_started/command-reference.md",
  "language_code": "id"
}
-->
# Referensi Perintah

CLI **Co-op Translator** menawarkan beberapa opsi untuk menyesuaikan proses terjemahan:

Perintah                                      | Deskripsi
----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"                 | Menerjemahkan proyek Anda ke bahasa yang ditentukan. Contoh: translate -l "es fr de" menerjemahkan ke bahasa Spanyol, Prancis, dan Jerman. Gunakan translate -l "all" untuk menerjemahkan ke semua bahasa yang didukung.
translate -l "language_codes" -u              | Memperbarui terjemahan dengan menghapus yang sudah ada dan membuat ulang. Peringatan: Ini akan menghapus semua terjemahan saat ini untuk bahasa yang ditentukan.
translate -l "language_codes" -img            | Menerjemahkan hanya file gambar.
translate -l "language_codes" -md             | Menerjemahkan hanya file Markdown.
translate -l "language_codes" -nb             | Menerjemahkan hanya file Jupyter notebook (.ipynb).
translate -l "language_codes" --fix           | Menerjemahkan ulang file dengan skor kepercayaan rendah berdasarkan hasil evaluasi sebelumnya.
translate -l "language_codes" -d              | Mengaktifkan mode debug untuk pencatatan detail.
translate -l "language_codes" --save-logs, -s | Menyimpan log level DEBUG ke file di bawah <root_dir>/logs/ (kontrol konsol tetap menggunakan -d)
translate -l "language_codes" -r "root_dir"   | Menentukan direktori root proyek
translate -l "language_codes" -f              | Menggunakan mode cepat untuk terjemahan gambar (hingga 3x lebih cepat dengan sedikit pengorbanan kualitas dan penyelarasan).
translate -l "language_codes" -y              | Otomatis mengonfirmasi semua prompt (berguna untuk pipeline CI/CD)
translate -l "language_codes" --add-disclaimer/--no-disclaimer | Mengaktifkan atau menonaktifkan penambahan bagian penafian terjemahan mesin pada markdown dan notebook yang diterjemahkan (default: aktif).
translate -l "language_codes" --help          | Menampilkan bantuan dalam CLI yang menunjukkan perintah yang tersedia
evaluate -l "language_code"                  | Mengevaluasi kualitas terjemahan untuk bahasa tertentu dan memberikan skor kepercayaan
evaluate -l "language_code" -c 0.8           | Mengevaluasi terjemahan dengan ambang batas kepercayaan khusus
evaluate -l "language_code" -f               | Mode evaluasi cepat (hanya berbasis aturan, tanpa LLM)
evaluate -l "language_code" -D               | Mode evaluasi mendalam (hanya berbasis LLM, lebih menyeluruh tapi lebih lambat)
evaluate -l "language_code" --save-logs, -s  | Menyimpan log level DEBUG ke file di bawah <root_dir>/logs/
migrate-links -l "language_codes"             | Memproses ulang file Markdown yang diterjemahkan untuk memperbarui tautan ke notebook (.ipynb). Mengutamakan notebook terjemahan jika tersedia; jika tidak, dapat kembali ke notebook asli.
migrate-links -l "language_codes" -r          | Menentukan direktori root proyek (default: direktori saat ini).
migrate-links -l "language_codes" --dry-run   | Menampilkan file mana yang akan berubah tanpa menulis perubahan.
migrate-links -l "language_codes" --no-fallback-to-original | Tidak menulis ulang tautan ke notebook asli saat versi terjemahan tidak ada (hanya memperbarui jika terjemahan ada).
migrate-links -l "language_codes" -d          | Mengaktifkan mode debug untuk pencatatan detail.
migrate-links -l "language_codes" --save-logs, -s | Menyimpan log level DEBUG ke file di bawah <root_dir>/logs/
migrate-links -l "all" -y                      | Memproses semua bahasa dan otomatis mengonfirmasi prompt peringatan.

## Contoh Penggunaan

  1. Perilaku default (menambahkan terjemahan baru tanpa menghapus yang sudah ada):   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. Menambahkan hanya terjemahan gambar Korea baru (tidak menghapus terjemahan yang ada):    translate -l "ko" -img

  3. Memperbarui semua terjemahan Korea (Peringatan: Ini menghapus semua terjemahan Korea yang ada sebelum menerjemahkan ulang):    translate -l "ko" -u

  4. Memperbarui hanya gambar Korea (Peringatan: Ini menghapus semua gambar Korea yang ada sebelum menerjemahkan ulang):    translate -l "ko" -img -u

  5. Menambahkan terjemahan markdown baru untuk Korea tanpa memengaruhi terjemahan lain:    translate -l "ko" -md

  6. Memperbaiki terjemahan dengan skor kepercayaan rendah berdasarkan hasil evaluasi sebelumnya: translate -l "ko" --fix

  7. Memperbaiki terjemahan dengan skor kepercayaan rendah untuk file tertentu saja (markdown): translate -l "ko" --fix -md

  8. Memperbaiki terjemahan dengan skor kepercayaan rendah untuk file tertentu saja (gambar): translate -l "ko" --fix -img

  9. Menggunakan mode cepat untuk terjemahan gambar:    translate -l "ko" -img -f

  10. Memperbaiki terjemahan dengan skor kepercayaan rendah dengan ambang batas khusus: translate -l "ko" --fix -c 0.8

  11. Contoh mode debug: - translate -l "ko" -d: Mengaktifkan pencatatan debug.
  12. Menyimpan log ke file: translate -l "ko" -s
  13. DEBUG di konsol dan file: translate -l "ko" -d -s
  14. Menerjemahkan tanpa menambahkan penafian terjemahan mesin ke output: translate -l "ko" --no-disclaimer

  15. Migrasi tautan notebook untuk terjemahan Korea (memperbarui tautan ke notebook terjemahan jika tersedia):    migrate-links -l "ko"

  15. Migrasi tautan dengan dry-run (tanpa menulis file):    migrate-links -l "ko" --dry-run

  16. Hanya memperbarui tautan jika notebook terjemahan ada (tidak kembali ke versi asli):    migrate-links -l "ko" --no-fallback-to-original

  17. Memproses semua bahasa dengan prompt konfirmasi:    migrate-links -l "all"

  18. Memproses semua bahasa dan otomatis mengonfirmasi:    migrate-links -l "all" -y
  19. Menyimpan log ke file untuk migrate-links:    migrate-links -l "ko ja" -s

### Contoh Evaluasi

> [!WARNING]  
> **Fitur Beta**: Fungsi evaluasi saat ini masih dalam tahap beta. Fitur ini dirilis untuk mengevaluasi dokumen terjemahan, dan metode evaluasi serta implementasi detailnya masih dalam pengembangan dan dapat berubah.

  1. Mengevaluasi terjemahan Korea: evaluate -l "ko"

  2. Mengevaluasi dengan ambang batas kepercayaan khusus: evaluate -l "ko" -c 0.8

  3. Evaluasi cepat (hanya berbasis aturan): evaluate -l "ko" -f

  4. Evaluasi mendalam (hanya berbasis LLM): evaluate -l "ko" -D

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diingat bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sahih. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau salah tafsir yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->