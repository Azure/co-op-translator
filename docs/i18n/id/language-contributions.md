# Menyumbangkan perbaikan bahasa

Pengetahuan bahasa Anda dapat membantu meningkatkan Co-op Translator. Mulailah dengan sebuah contoh, koreksi yang disarankan, dan penjelasan menggunakan [formulir umpan balik terjemahan](https://github.com/Azure/co-op-translator/issues/new?template=translation_feedback.yml). Anda tidak perlu menulis kode atau membayar untuk menjalankan model.

## Dari laporan ke perbaikan bersama

1. Seorang kontributor memberikan kutipan sumber, terjemahannya, dan konteks.
2. Seorang peninjau bahasa memeriksa makna, kealamian, dan apakah saran tergantung pada lokal atau kursus tertentu.
3. Seorang pemelihara memutuskan apakah perbaikan tersebut termasuk dalam kursus sumber, instruksi bahasa bersama, konfigurasi terminologi, atau kode terjemahan.
4. Untuk aturan bersama, seorang pemelihara membandingkan keluaran sebelum dan sesudah perubahan pada contoh yang dilaporkan dan contoh lain yang tidak terkait. Kontributor dapat meninjau keluaran ini tanpa menjalankan alat itu sendiri.
5. PR yang dihasilkan menautkan laporan dan memberi kredit kepada orang-orang yang memberikan contoh dan peninjauan. Penyebaran atau regenerasi di repositori yang mengonsumsi adalah langkah terpisah.

Sebuah laporan tidak otomatis mengubah prompt atau meregenerasi terjemahan kursus. Koreksi yang spesifik untuk kursus harus tetap terhubung ke repositori kursus. Jangan berasumsi bahwa suntingan manual akan bertahan setelah penerjemahan ulang; konfirmasikan perilaku untuk alur kerja tersebut.

## Contoh yang ada: tautan Markdown bahasa Jepang

File [file instruksi bahasa Jepang](https://github.com/Azure/co-op-translator/blob/main/src/co_op_translator/templates/language/ja.md) memberi tahu model untuk menerjemahkan teks tautan sambil mempertahankan sintaks Markdown dan tujuan tautan. Misalnya, tautan yang ditulis sebagai `[text](URL)` tidak boleh menjadi `「text」（URL）`.

Ini adalah contoh terfokus dari sebuah aturan bahasa yang didukung oleh ilustrasi keluaran yang benar dan salah. Ini bukan bukti bahwa instruksi prompt saja menjamin Markdown yang benar.

[Pembuat prompt Markdown](https://github.com/Azure/co-op-translator/blob/main/src/co_op_translator/utils/markdown/prompts.py) memuat `templates/language/<language_code>.md` menggunakan kode bahasa yang dikonversi menjadi huruf kecil dan dipangkas. Jika tidak ada file, ia menggunakan instruksi umum. Ini menjelaskan jalur prompt Markdown; jangan berasumsi setiap gambar atau jalur terjemahan lain menggunakan instruksi yang sama.

[pengujian prompt](https://github.com/Azure/co-op-translator/blob/main/tests/co_op_translator/utils/markdown/test_prompts.py) memeriksa bahwa instruksi bahasa Jepang disertakan. Itu memverifikasi penyusunan prompt, bukan kualitas terjemahan.

## Apa yang termasuk dalam aturan bahasa?

Usulkan koreksi yang sempit dan dapat diulang dengan contoh sumber, perilaku yang diharapkan, dan kontra-contoh di mana aturan tidak boleh berlaku. Pertahankan makna, placeholders, kode, URLs, dan struktur dokumen. Hindari mengubah preferensi gaya satu orang atau terminologi satu kursus menjadi aturan universal.

Saat ini, [implementasi glosarium](https://github.com/Azure/co-op-translator/blob/main/src/co_op_translator/glossary.py) melindungi istilah dari terjemahan. Ini bukan kamus terminologi sumber-ke-target. Diskusikan perilaku terminologi baru sebelum menjanjikannya kepada kontributor.

## Contoh komunitas: laporan nama produk bahasa Jepang

Dalam [laporan #527](https://github.com/Azure/co-op-translator/issues/527), @hyoshioka0128 mengidentifikasi terjemahan bahasa Jepang yang mengubah nama produk `Co-op Translator` menjadi `Co-op 翻訳`. Laporan tersebut menyertakan tautan ke dokumen yang terpengaruh dan tangkapan layar, sehingga masalah mudah ditemukan.

Kontributor tersebut juga menautkan [PR kursus terkait](https://github.com/microsoft/AZD-for-beginners/pull/109). Dalam diskusi isu, pemelihara mengakui laporan tersebut dan mengusulkan penyelidikan mengapa nama tersebut berubah, termasuk perlindungan terminologi, perilaku glosarium, dan jalur terjemahan.

Ini menunjukkan bagaimana laporan kecil dapat mendukung penyelidikan di luar koreksi kata tunggal. Ini bukan hasil sebelum/sesudah yang terverifikasi atau bukti bahwa instruksi tautan Markdown bahasa Jepang di atas memperbaiki masalah nama produk ini.

Anda dapat berkontribusi dengan cara yang sama: bagikan teks asli, terjemahan saat ini, koreksi yang disarankan, dan mengapa itu penting. Tambahkan tautan dokumen atau tangkapan layar jika berguna. Anda tidak perlu mendiagnosis penyebabnya atau menulis prompt sebelum melaporkannya.

## Validasi sebelum mengadopsi aturan

Gunakan sampel sumber, revisi penerjemah, penyedia/model, dan pengaturan generasi yang sama untuk run baseline dan kandidat, hanya mengubah instruksi yang diusulkan. Catat perubahan prompt aktual dan keluaran; ulangi contoh bila perlu untuk membedakan efek yang konsisten dari variabilitas keluaran. Sertakan kegagalan yang dilaporkan, konteks yang kontras, dan contoh yang sudah diterjemahkan dengan benar.

| Sampel | Sumber/konteks | Keluaran baseline | Keluaran kandidat | Penilaian peninjau |
| --- | --- | --- | --- | --- |
| Kegagalan yang dilaporkan | Untuk dikumpulkan | Belum dijalankan | Belum dijalankan | Tertunda |
| Kontra-contoh | Untuk dikumpulkan | Belum dijalankan | Belum dijalankan | Tertunda |
| Contoh yang tidak terpengaruh | Untuk dikumpulkan | Belum dijalankan | Belum dijalankan | Tertunda |

Periksa invarian struktural secara terpisah dari penilaian linguistik. Tes pemuatan prompt yang berhasil bukanlah evaluasi kualitas, dan satu kalimat yang diharapkan secara tepat bukanlah satu-satunya terjemahan yang valid. Jika konteks, jalannya model, atau peninjauan bahasa hilang, biarkan proposal tertunda alih-alih mengklaim masalah telah diperbaiki.