<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a6cddf5e9648ef0bba0de7eb07e74cf1",
  "translation_date": "2025-10-15T03:40:10+00:00",
  "source_file": "getting_started/command-reference.md",
  "language_code": "ms"
}
-->
# Rujukan Perintah

**Co-op Translator** CLI menawarkan beberapa pilihan untuk menyesuaikan proses terjemahan:

Perintah                                       | Penerangan
----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"                 | Menterjemah projek anda ke dalam bahasa yang ditetapkan. Contoh: translate -l "es fr de" akan menterjemah ke dalam bahasa Sepanyol, Perancis, dan Jerman. Guna translate -l "all" untuk menterjemah ke semua bahasa yang disokong.
translate -l "language_codes" -u              | Kemas kini terjemahan dengan memadam terjemahan sedia ada dan mencipta semula. Amaran: Ini akan memadam semua terjemahan semasa untuk bahasa yang dipilih.
translate -l "language_codes" -img            | Hanya menterjemah fail imej.
translate -l "language_codes" -md             | Hanya menterjemah fail Markdown.
translate -l "language_codes" -nb             | Hanya menterjemah fail Jupyter notebook (.ipynb).
translate -l "language_codes" --fix           | Menterjemah semula fail dengan skor keyakinan rendah berdasarkan hasil penilaian sebelum ini.
translate -l "language_codes" -d              | Aktifkan mod debug untuk log terperinci.
translate -l "language_codes" --save-logs, -s | Simpan log tahap DEBUG ke fail di bawah <root_dir>/logs/ (konsol masih dikawal oleh -d)
translate -l "language_codes" -r "root_dir"   | Tetapkan direktori root projek
translate -l "language_codes" -f              | Guna mod pantas untuk terjemahan imej (sehingga 3x lebih laju dengan sedikit pengurangan kualiti dan penjajaran).
translate -l "language_codes" -y              | Sahkan semua prompt secara automatik (sesuai untuk pipeline CI/CD)
translate -l "language_codes" --help          | butiran bantuan dalam CLI yang memaparkan perintah yang tersedia
evaluate -l "language_code"                  | Menilai kualiti terjemahan untuk bahasa tertentu dan memberikan skor keyakinan
evaluate -l "language_code" -c 0.8           | Menilai terjemahan dengan ambang keyakinan tersuai
evaluate -l "language_code" -f               | Mod penilaian pantas (berdasarkan peraturan sahaja, tiada LLM)
evaluate -l "language_code" -D               | Mod penilaian mendalam (hanya LLM, lebih teliti tetapi lebih perlahan)
evaluate -l "language_code" --save-logs, -s  | Simpan log tahap DEBUG ke fail di bawah <root_dir>/logs/
migrate-links -l "language_codes"             | Proses semula fail Markdown yang telah diterjemah untuk mengemas kini pautan ke notebook (.ipynb). Akan memilih notebook yang telah diterjemah jika ada; jika tidak, boleh guna notebook asal.
migrate-links -l "language_codes" -r          | Tetapkan direktori root projek (lalai: direktori semasa).
migrate-links -l "language_codes" --dry-run   | Paparkan fail yang akan berubah tanpa menulis perubahan.
migrate-links -l "language_codes" --no-fallback-to-original | Jangan tukar pautan ke notebook asal jika notebook terjemahan tiada (hanya kemas kini jika terjemahan wujud).
migrate-links -l "language_codes" -d          | Aktifkan mod debug untuk log terperinci.
migrate-links -l "language_codes" --save-logs, -s | Simpan log tahap DEBUG ke fail di bawah <root_dir>/logs/
migrate-links -l "all" -y                      | Proses semua bahasa dan sahkan prompt amaran secara automatik.

## Contoh Penggunaan

  1. Tingkah laku lalai (tambah terjemahan baru tanpa memadam yang sedia ada):   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. Tambah hanya terjemahan imej Korea baru (tiada terjemahan sedia ada dipadam):    translate -l "ko" -img

  3. Kemas kini semua terjemahan Korea (Amaran: Ini akan memadam semua terjemahan Korea sedia ada sebelum menterjemah semula):    translate -l "ko" -u

  4. Kemas kini hanya imej Korea (Amaran: Ini akan memadam semua imej Korea sedia ada sebelum menterjemah semula):    translate -l "ko" -img -u

  5. Tambah terjemahan markdown baru untuk Korea tanpa menjejaskan terjemahan lain:    translate -l "ko" -md

  6. Baiki terjemahan dengan keyakinan rendah berdasarkan hasil penilaian sebelum ini: translate -l "ko" --fix

  7. Baiki terjemahan keyakinan rendah untuk fail tertentu sahaja (markdown): translate -l "ko" --fix -md

  8. Baiki terjemahan keyakinan rendah untuk fail tertentu sahaja (imej): translate -l "ko" --fix -img

  9. Guna mod pantas untuk terjemahan imej:    translate -l "ko" -img -f

  10. Baiki terjemahan keyakinan rendah dengan ambang tersuai: translate -l "ko" --fix -c 0.8

  11. Contoh mod debug: - translate -l "ko" -d: Aktifkan log debug.
  12. Simpan log ke fail: translate -l "ko" -s
  13. DEBUG di konsol dan fail: translate -l "ko" -d -s

  14. Migrasi pautan notebook untuk terjemahan Korea (kemas kini pautan ke notebook terjemahan jika ada):    migrate-links -l "ko"

  15. Migrasi pautan dengan dry-run (tiada penulisan fail):    migrate-links -l "ko" --dry-run

  16. Hanya kemas kini pautan jika notebook terjemahan wujud (jangan guna asal):    migrate-links -l "ko" --no-fallback-to-original

  17. Proses semua bahasa dengan prompt pengesahan:    migrate-links -l "all"

  18. Proses semua bahasa dan sahkan automatik:    migrate-links -l "all" -y
  19. Simpan log ke fail untuk migrate-links:    migrate-links -l "ko ja" -s

### Contoh Penilaian

> [!WARNING]  
> **Ciri Beta**: Fungsi penilaian ini masih dalam peringkat beta. Ciri ini dikeluarkan untuk menilai dokumen yang telah diterjemah, dan kaedah serta pelaksanaan terperinci masih dalam pembangunan dan boleh berubah.

  1. Nilai terjemahan Korea: evaluate -l "ko"

  2. Nilai dengan ambang keyakinan tersuai: evaluate -l "ko" -c 0.8

  3. Penilaian pantas (berdasarkan peraturan sahaja): evaluate -l "ko" -f

  4. Penilaian mendalam (hanya LLM): evaluate -l "ko" -D

---

**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat kritikal, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.