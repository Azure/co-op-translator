<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a6cddf5e9648ef0bba0de7eb07e74cf1",
  "translation_date": "2025-10-15T03:37:44+00:00",
  "source_file": "getting_started/command-reference.md",
  "language_code": "id"
}
-->
# Referensi Perintah

**Co-op Translator** CLI menyediakan beberapa opsi untuk menyesuaikan proses penerjemahan:

Perintah                                       | Deskripsi
-----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"                  | Menerjemahkan proyek Anda ke dalam bahasa yang ditentukan. Contoh: translate -l "es fr de" akan menerjemahkan ke Spanyol, Prancis, dan Jerman. Gunakan translate -l "all" untuk menerjemahkan ke semua bahasa yang didukung.
translate -l "language_codes" -u               | Memperbarui terjemahan dengan menghapus terjemahan yang ada dan membuat ulang. Peringatan: Ini akan menghapus semua terjemahan saat ini untuk bahasa yang dipilih.
translate -l "language_codes" -img             | Hanya menerjemahkan file gambar.
translate -l "language_codes" -md              | Hanya menerjemahkan file Markdown.
translate -l "language_codes" -nb              | Hanya menerjemahkan file Jupyter notebook (.ipynb).
translate -l "language_codes" --fix            | Menerjemahkan ulang file dengan skor kepercayaan rendah berdasarkan hasil evaluasi sebelumnya.
translate -l "language_codes" -d               | Mengaktifkan mode debug untuk log detail.
translate -l "language_codes" --save-logs, -s  | Simpan log level DEBUG ke file di <root_dir>/logs/ (konsol tetap dikontrol oleh -d)
translate -l "language_codes" -r "root_dir"    | Menentukan direktori root proyek
translate -l "language_codes" -f               | Menggunakan mode cepat untuk penerjemahan gambar (hingga 3x lebih cepat dengan sedikit penurunan kualitas dan keselarasan).
translate -l "language_codes" -y               | Konfirmasi otomatis semua prompt (berguna untuk pipeline CI/CD)
translate -l "language_codes" --help           | Detail bantuan di dalam CLI yang menampilkan perintah yang tersedia
evaluate -l "language_code"                    | Mengevaluasi kualitas terjemahan untuk bahasa tertentu dan memberikan skor kepercayaan
evaluate -l "language_code" -c 0.8             | Mengevaluasi terjemahan dengan ambang kepercayaan khusus
evaluate -l "language_code" -f                 | Mode evaluasi cepat (hanya berbasis aturan, tanpa LLM)
evaluate -l "language_code" -D                 | Mode evaluasi mendalam (hanya berbasis LLM, lebih menyeluruh namun lebih lambat)
evaluate -l "language_code" --save-logs, -s    | Simpan log level DEBUG ke file di <root_dir>/logs/
migrate-links -l "language_codes"              | Memproses ulang file Markdown yang sudah diterjemahkan untuk memperbarui tautan ke notebook (.ipynb). Mengutamakan notebook yang sudah diterjemahkan jika tersedia; jika tidak, bisa kembali ke notebook asli.
migrate-links -l "language_codes" -r           | Menentukan direktori root proyek (default: direktori saat ini).
migrate-links -l "language_codes" --dry-run    | Menampilkan file mana yang akan berubah tanpa menulis perubahan.
migrate-links -l "language_codes" --no-fallback-to-original | Jangan menulis ulang tautan ke notebook asli jika terjemahan tidak tersedia (hanya perbarui jika terjemahan ada).
migrate-links -l "language_codes" -d           | Aktifkan mode debug untuk log detail.
migrate-links -l "language_codes" --save-logs, -s | Simpan log level DEBUG ke file di <root_dir>/logs/
migrate-links -l "all" -y                      | Proses semua bahasa dan konfirmasi otomatis prompt peringatan.

## Contoh Penggunaan

  1. Perilaku default (menambah terjemahan baru tanpa menghapus yang sudah ada):   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. Hanya menambah terjemahan gambar Korea baru (terjemahan yang sudah ada tidak dihapus):    translate -l "ko" -img

  3. Memperbarui semua terjemahan Korea (Peringatan: Ini akan menghapus semua terjemahan Korea sebelum menerjemahkan ulang):    translate -l "ko" -u

  4. Memperbarui hanya gambar Korea (Peringatan: Ini akan menghapus semua gambar Korea sebelum menerjemahkan ulang):    translate -l "ko" -img -u

  5. Menambah terjemahan markdown baru untuk Korea tanpa memengaruhi terjemahan lain:    translate -l "ko" -md

  6. Memperbaiki terjemahan dengan skor kepercayaan rendah berdasarkan hasil evaluasi sebelumnya: translate -l "ko" --fix

  7. Memperbaiki terjemahan dengan skor kepercayaan rendah hanya untuk file tertentu (markdown): translate -l "ko" --fix -md

  8. Memperbaiki terjemahan dengan skor kepercayaan rendah hanya untuk file tertentu (gambar): translate -l "ko" --fix -img

  9. Menggunakan mode cepat untuk penerjemahan gambar:    translate -l "ko" -img -f

  10. Memperbaiki terjemahan dengan skor kepercayaan rendah dengan ambang khusus: translate -l "ko" --fix -c 0.8

  11. Contoh mode debug: - translate -l "ko" -d: Aktifkan log debug.
  12. Simpan log ke file: translate -l "ko" -s
  13. DEBUG di konsol dan file: translate -l "ko" -d -s

  14. Migrasi tautan notebook untuk terjemahan Korea (perbarui tautan ke notebook yang sudah diterjemahkan jika tersedia):    migrate-links -l "ko"

  15. Migrasi tautan dengan dry-run (tanpa menulis file):    migrate-links -l "ko" --dry-run

  16. Hanya perbarui tautan jika notebook terjemahan ada (jangan kembali ke aslinya):    migrate-links -l "ko" --no-fallback-to-original

  17. Proses semua bahasa dengan prompt konfirmasi:    migrate-links -l "all"

  18. Proses semua bahasa dan konfirmasi otomatis:    migrate-links -l "all" -y
  19. Simpan log ke file untuk migrate-links:    migrate-links -l "ko ja" -s

### Contoh Evaluasi

> [!WARNING]  
> **Fitur Beta**: Fitur evaluasi saat ini masih dalam tahap beta. Fitur ini dirilis untuk mengevaluasi dokumen terjemahan, dan metode evaluasi serta implementasi detailnya masih dalam pengembangan dan dapat berubah sewaktu-waktu.

  1. Evaluasi terjemahan Korea: evaluate -l "ko"

  2. Evaluasi dengan ambang kepercayaan khusus: evaluate -l "ko" -c 0.8

  3. Evaluasi cepat (hanya berbasis aturan): evaluate -l "ko" -f

  4. Evaluasi mendalam (hanya berbasis LLM): evaluate -l "ko" -D

---

**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk memberikan terjemahan yang akurat, harap diketahui bahwa terjemahan otomatis dapat mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang berwenang. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa penerjemah profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang timbul dari penggunaan terjemahan ini.