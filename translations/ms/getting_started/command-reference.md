<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "822238e4451d04bb152cebb1be6f13c2",
  "translation_date": "2025-11-30T11:53:51+00:00",
  "source_file": "getting_started/command-reference.md",
  "language_code": "ms"
}
-->
# Rujukan arahan

CLI **Co-op Translator** menawarkan beberapa pilihan untuk menyesuaikan proses terjemahan:

Arahan                                      | Penerangan
--------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"               | Menterjemah projek anda ke dalam bahasa yang ditetapkan. Contoh: translate -l "es fr de" menterjemah ke Sepanyol, Perancis, dan Jerman. Gunakan translate -l "all" untuk menterjemah ke semua bahasa yang disokong.
translate -l "language_codes" -u            | Mengemas kini terjemahan dengan memadam yang sedia ada dan membuat semula. Amaran: Ini akan memadam semua terjemahan semasa untuk bahasa yang ditetapkan.
translate -l "language_codes" -img          | Menterjemah hanya fail imej.
translate -l "language_codes" -md           | Menterjemah hanya fail Markdown.
translate -l "language_codes" -nb           | Menterjemah hanya fail buku nota Jupyter (.ipynb).
translate -l "language_codes" --fix         | Menterjemah semula fail dengan skor keyakinan rendah berdasarkan keputusan penilaian sebelumnya.
translate -l "language_codes" -d            | Mengaktifkan mod debug untuk log terperinci.
translate -l "language_codes" --save-logs, -s | Simpan log tahap DEBUG ke fail di bawah <root_dir>/logs/ (konsol dikawal oleh -d)
translate -l "language_codes" -r "root_dir" | Menentukan direktori akar projek
translate -l "language_codes" -f            | Menggunakan mod pantas untuk terjemahan imej (sehingga 3x lebih pantas dengan sedikit pengorbanan kualiti dan penjajaran).
translate -l "language_codes" -y            | Mengesahkan semua arahan secara automatik (berguna untuk saluran CI/CD)
translate -l "language_codes" --add-disclaimer/--no-disclaimer | Mengaktifkan atau mematikan penambahan seksyen penafian terjemahan mesin pada markdown dan buku nota yang diterjemah (lalai: diaktifkan).
translate -l "language_codes" --help        | butiran bantuan dalam CLI yang menunjukkan arahan yang tersedia
evaluate -l "language_code"                  | Menilai kualiti terjemahan untuk bahasa tertentu dan memberikan skor keyakinan
evaluate -l "language_code" -c 0.8           | Menilai terjemahan dengan ambang keyakinan tersuai
evaluate -l "language_code" -f               | Mod penilaian pantas (berdasarkan peraturan sahaja, tanpa LLM)
evaluate -l "language_code" -D               | Mod penilaian mendalam (berdasarkan LLM sahaja, lebih teliti tetapi lebih perlahan)
evaluate -l "language_code" --save-logs, -s  | Simpan log tahap DEBUG ke fail di bawah <root_dir>/logs/
migrate-links -l "language_codes"             | Memproses semula fail Markdown yang diterjemah untuk mengemas kini pautan ke buku nota (.ipynb). Mengutamakan buku nota yang diterjemah jika ada; jika tidak, boleh kembali ke buku nota asal.
migrate-links -l "language_codes" -r          | Menentukan direktori akar projek (lalai: direktori semasa).
migrate-links -l "language_codes" --dry-run   | Menunjukkan fail mana yang akan berubah tanpa menulis perubahan.
migrate-links -l "language_codes" --no-fallback-to-original | Tidak menulis semula pautan ke buku nota asal apabila buku nota terjemahan tiada (hanya kemas kini apabila terjemahan wujud).
migrate-links -l "language_codes" -d          | Mengaktifkan mod debug untuk log terperinci.
migrate-links -l "language_codes" --save-logs, -s | Simpan log tahap DEBUG ke fail di bawah <root_dir>/logs/
migrate-links -l "all" -y                      | Memproses semua bahasa dan mengesahkan amaran secara automatik.

## Contoh penggunaan

  1. Tingkah laku lalai (menambah terjemahan baru tanpa memadam yang sedia ada):   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. Menambah hanya terjemahan imej Korea baru (tiada terjemahan sedia ada dipadam):    translate -l "ko" -img

  3. Mengemas kini semua terjemahan Korea (Amaran: Ini memadam semua terjemahan Korea sedia ada sebelum menterjemah semula):    translate -l "ko" -u

  4. Mengemas kini hanya imej Korea (Amaran: Ini memadam semua imej Korea sedia ada sebelum menterjemah semula):    translate -l "ko" -img -u

  5. Menambah terjemahan markdown baru untuk Korea tanpa menjejaskan terjemahan lain:    translate -l "ko" -md

  6. Memperbaiki terjemahan dengan keyakinan rendah berdasarkan keputusan penilaian sebelumnya: translate -l "ko" --fix

  7. Memperbaiki terjemahan keyakinan rendah untuk fail tertentu sahaja (markdown): translate -l "ko" --fix -md

  8. Memperbaiki terjemahan keyakinan rendah untuk fail tertentu sahaja (imej): translate -l "ko" --fix -img

  9. Menggunakan mod pantas untuk terjemahan imej:    translate -l "ko" -img -f

  10. Memperbaiki terjemahan keyakinan rendah dengan ambang tersuai: translate -l "ko" --fix -c 0.8

  11. Contoh mod debug: - translate -l "ko" -d: Mengaktifkan log debug.
  12. Simpan log ke fail: translate -l "ko" -s
  13. DEBUG konsol dan DEBUG fail: translate -l "ko" -d -s
  14. Terjemah tanpa menambah penafian terjemahan mesin pada output: translate -l "ko" --no-disclaimer

  15. Migrasi pautan buku nota untuk terjemahan Korea (kemas kini pautan ke buku nota terjemahan apabila ada):    migrate-links -l "ko"

  15. Migrasi pautan dengan dry-run (tiada penulisan fail):    migrate-links -l "ko" --dry-run

  16. Kemas kini pautan hanya apabila buku nota terjemahan wujud (tidak kembali ke asal):    migrate-links -l "ko" --no-fallback-to-original

  17. Proses semua bahasa dengan pengesahan:    migrate-links -l "all"

  18. Proses semua bahasa dan sahkan automatik:    migrate-links -l "all" -y
  19. Simpan log ke fail untuk migrate-links:    migrate-links -l "ko ja" -s

### Contoh Penilaian

> [!WARNING]  
> **Ciri Beta**: Fungsi penilaian kini dalam versi beta. Ciri ini dikeluarkan untuk menilai dokumen terjemahan, dan kaedah penilaian serta pelaksanaan terperinci masih dalam pembangunan dan boleh berubah.

  1. Menilai terjemahan Korea: evaluate -l "ko"

  2. Menilai dengan ambang keyakinan tersuai: evaluate -l "ko" -c 0.8

  3. Penilaian pantas (berdasarkan peraturan sahaja): evaluate -l "ko" -f

  4. Penilaian mendalam (berdasarkan LLM sahaja): evaluate -l "ko" -D

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->