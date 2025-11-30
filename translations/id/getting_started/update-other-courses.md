<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "93a7150216aa3c2d191135358fa6dd21",
  "translation_date": "2025-11-30T13:47:25+00:00",
  "source_file": "getting_started/update-other-courses.md",
  "language_code": "id"
}
-->
# Perbarui bagian "Kursus Lainnya" (repos Microsoft Beginners)

Panduan ini menjelaskan cara membuat bagian "Kursus Lainnya" tersinkronisasi otomatis menggunakan Co-op Translator, serta cara memperbarui template global untuk semua repositori.

- Berlaku untuk: hanya repositori Microsoft Beginners
- Bekerja dengan: Co-op Translator CLI dan GitHub Actions
- Sumber template: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## Mulai cepat: Aktifkan auto-sync di repo Anda

Tambahkan penanda berikut di sekitar bagian "Kursus Lainnya" di README Anda. Co-op Translator akan mengganti semua konten di antara penanda ini setiap kali dijalankan.

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

Setiap kali Co-op Translator dijalankan—melalui CLI (misalnya, `translate -l "<language codes>"`) atau GitHub Actions—bagian "Kursus Lainnya" yang dibungkus oleh penanda ini akan diperbarui secara otomatis.

> [!NOTE]
> Jika Anda sudah memiliki daftar yang ada, cukup bungkus dengan penanda yang sama. Pada proses berikutnya, daftar tersebut akan diganti dengan konten standar terbaru.

---

## Cara mengubah konten global

Jika Anda ingin memperbarui konten standar yang muncul di semua repositori Beginners:

1. Edit templatenya: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)
2. Buka pull request ke repositori Co-op Translator dengan perubahan Anda
3. Setelah PR digabungkan, versi Co-op Translator akan diperbarui
4. Saat Co-op Translator dijalankan berikutnya (CLI atau GitHub Action) di repositori target, bagian yang diperbarui akan otomatis tersinkronisasi

Ini memastikan sumber kebenaran tunggal untuk konten "Kursus Lainnya" di semua repositori Beginners.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berusaha untuk akurasi, harap diingat bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sahih. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau salah tafsir yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->