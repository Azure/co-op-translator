# Menyumbang penambahbaikan bahasa

Pengetahuan bahasa anda boleh membantu memperbaiki Co-op Translator. Mula dengan contoh, pembetulan yang dicadangkan, dan penjelasan menggunakan [borang maklum balas terjemahan](https://github.com/Azure/co-op-translator/issues/new?template=translation_feedback.yml). Anda tidak perlu menulis kod atau membayar untuk menjalankan model.

## Dari laporan kepada penambahbaikan bersama

1. Penyumbang menyediakan petikan sumber, terjemahannya, dan konteks.
2. Penyemak bahasa memeriksa makna, kelancaran semula jadi, dan sama ada cadangan bergantung pada sesuatu lokal atau kursus tertentu.
3. Penyelenggara memutuskan sama ada pembetulan patut dimasukkan dalam kursus sumber, arahan bahasa berkongsi, konfigurasi istilah, atau kod terjemahan.
4. Untuk peraturan berkongsi, penyelenggara membandingkan output sebelum dan selepas perubahan pada contoh yang dilaporkan dan contoh yang tidak berkaitan. Penyumbang boleh menyemak output ini tanpa menjalankan alat itu sendiri.
5. PR yang terhasil memautkan laporan dan memberi penghargaan kepada orang yang menyediakan contoh dan ulasan. Penggunaan atau penjanaan semula dalam repositori pengguna adalah langkah berasingan.

Satu laporan tidak secara automatik mengubah prompt atau menjana semula terjemahan kursus. Pembetulan khusus kursus harus kekal berkaitan dengan repositori kursus. Jangan anggap suntingan manual akan kekal selepas penerjemahan semula kemudian; sahkan kelakuan untuk aliran kerja itu.

## Contoh sedia ada: Pautan Markdown Jepun

[Fail arahan Jepun](https://github.com/Azure/co-op-translator/blob/main/src/co_op_translator/templates/language/ja.md) memberitahu model untuk menterjemah teks pautan sambil mengekalkan sintaks Markdown dan destinasi pautan. Sebagai contoh, pautan yang ditulis sebagai `[text](URL)` tidak boleh menjadi `「text」（URL）`.

Ini adalah contoh terfokus bagi peraturan bahasa yang disokong oleh ilustrasi output yang betul dan tidak betul. Ia bukan bukti bahawa arahan prompt sahaja menjamin Markdown yang betul.

[Pembina prompt Markdown](https://github.com/Azure/co-op-translator/blob/main/src/co_op_translator/utils/markdown/prompts.py) memuat `templates/language/<language_code>.md` menggunakan kod bahasa yang diturunkan huruf kecil dan dipangkas. Jika tiada fail wujud, ia menggunakan arahan umum. Ini menerangkan laluan prompt Markdown; jangan anggap setiap imej atau laluan terjemahan lain menggunakan arahan yang sama.

[Ujian prompt](https://github.com/Azure/co-op-translator/blob/main/tests/co_op_translator/utils/markdown/test_prompts.py) memeriksa bahawa arahan Jepun disertakan. Itu mengesahkan pemasangan prompt, bukan kualiti terjemahan.

## Apa yang patut ada dalam peraturan bahasa?

Cadangkan pembetulan yang sempit dan boleh diulang dengan contoh sumber, kelakuan yang dijangka, dan contoh tandingan di mana peraturan itu tidak boleh digunakan. Pelihara makna, pemegang tempat, kod, URL, dan struktur dokumen. Elakkan menukar keutamaan gaya seseorang atau istilah sesuatu kursus kepada peraturan universal.

[Pelaksanaan glosari](https://github.com/Azure/co-op-translator/blob/main/src/co_op_translator/glossary.py) semasa melindungi istilah daripada terjemahan. Ia bukan kamus terminologi sumber-ke-sasaran. Bincangkan kelakuan terminologi baru sebelum menjanjikannya kepada penyumbang.

## Contoh komuniti: laporan nama produk Jepun

Dalam [laporan #527](https://github.com/Azure/co-op-translator/issues/527), @hyoshioka0128 mengenal pasti terjemahan Jepun yang menukar nama produk `Co-op Translator` kepada `Co-op 翻訳`. Laporan itu menyertakan pautan ke dokumen yang terjejas dan tangkapan skrin, menjadikan masalah itu mudah ditemui.

Penyumbang itu juga memautkan [PR kursus berkaitan](https://github.com/microsoft/AZD-for-beginners/pull/109). Dalam perbincangan isu, penyelenggara mengakui laporan dan mencadangkan menyiasat mengapa nama berubah, termasuk perlindungan terminologi, kelakuan glosari, dan laluan terjemahan.

Ini menunjukkan bagaimana laporan kecil boleh menyokong penyiasatan melebihi pembetulan redaksi individu. Ia bukan keputusan sebelum/selepas yang disahkan atau bukti bahawa arahan pautan Markdown Jepun di atas membetulkan isu nama produk ini.

Anda boleh menyumbang dengan cara yang sama: kongsi teks asal, terjemahan semasa, pembetulan yang dicadangkan, dan mengapa ia penting. Tambah pautan dokumen atau tangkapan skrin apabila berguna. Anda tidak perlu mendiagnosis punca atau menulis prompt sebelum melaporkannya.

## Pengesahan sebelum menerima sesuatu peraturan

Gunakan sampel sumber yang sama, semakan penterjemah, penyedia/model, dan tetapan penjanaan untuk larian asas dan calon, menukar hanya arahan yang dicadangkan. Rekod perubahan prompt sebenar dan output; ulangi contoh apabila perlu untuk membezakan kesan konsisten daripada variasi output. Sertakan kegagalan yang dilaporkan, konteks yang berbeza, dan contoh yang sudah diterjemah dengan betul.

| Sampel | Sumber/konteks | Output asas | Output calon | Penilaian penyemak |
| --- | --- | --- | --- | --- |
| Kegagalan yang dilaporkan | Untuk dikumpul | Belum dijalankan | Belum dijalankan | Menunggu |
| Contoh tandingan | Untuk dikumpul | Belum dijalankan | Belum dijalankan | Menunggu |
| Contoh yang tidak terjejas | Untuk dikumpul | Belum dijalankan | Belum dijalankan | Menunggu |

Periksa invarian struktur secara berasingan daripada penghakiman linguistik. Ujian pemuatan prompt yang berjaya bukanlah penilaian kualiti, dan satu ayat tepat yang dijangka bukan satu-satunya terjemahan yang sah. Jika konteks, larian model, atau semakan bahasa hilang, biarkan cadangan itu menunggu daripada mendakwa isu itu diperbaiki.