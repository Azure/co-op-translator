<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "93a7150216aa3c2d191135358fa6dd21",
  "translation_date": "2025-11-30T13:47:47+00:00",
  "source_file": "getting_started/update-other-courses.md",
  "language_code": "ms"
}
-->
# Kemas kini bahagian "Kursus Lain" (repos Pemula Microsoft)

Panduan ini menerangkan cara untuk menjadikan bahagian "Kursus Lain" diselaraskan secara automatik menggunakan Co-op Translator, dan cara mengemas kini templat global untuk semua repos.

- Terpakai untuk: repositori Pemula Microsoft sahaja
- Berfungsi dengan: Co-op Translator CLI dan GitHub Actions
- Sumber templat: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## Mula cepat: Aktifkan auto-selaraskan dalam repo anda

Tambah penanda berikut di sekeliling bahagian "Kursus Lain" dalam README anda. Co-op Translator akan menggantikan segala yang berada di antara penanda ini setiap kali dijalankan.

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

Setiap kali Co-op Translator dijalankan—melalui CLI (contohnya, `translate -l "<language codes>"`) atau GitHub Actions—ia secara automatik mengemas kini bahagian "Kursus Lain" yang dibungkus oleh penanda ini.

> [!NOTE]
> Jika anda sudah mempunyai senarai sedia ada, cuma bungkuskan dengan penanda yang sama. Larian seterusnya akan menggantikannya dengan kandungan standard terkini.

---

## Cara mengubah kandungan global

Jika anda ingin mengemas kini kandungan standard yang muncul dalam semua repos Pemula:

1. Sunting templat: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)
2. Buka pull request ke repo Co-op Translator dengan perubahan anda
3. Selepas PR digabungkan, versi Co-op Translator akan dikemas kini
4. Kali seterusnya Co-op Translator dijalankan (CLI atau GitHub Action) dalam repo sasaran, ia akan secara automatik menyelaraskan bahagian yang dikemas kini

Ini memastikan satu sumber kebenaran tunggal untuk kandungan "Kursus Lain" di semua repositori Pemula.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->