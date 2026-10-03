# Terjemah, sunting, dan semak projek kecil

Mulakan dengan dua fail Markdown ringkas dan satu bahasa sasaran. Anda akan melihat di mana terjemahan ditulis, apa yang berlaku apabila sumber berubah, dan cara memeriksa keputusan.

## Keputusan yang dirakam

Contoh dijalankan pada 19 September 2026 dengan Co-op Translator 0.21.0 dan Azure OpenAI (`gpt-5-mini`). Perintah CLI yang tidak diubah dipanggil melalui Click's `CliRunner` menggunakan wheel yang dibina dan kebergantungan Python sedia ada.

| Langkah | Keputusan |
| --- | --- |
| Pratonton | Keluar 0; tiada terjemahan model diminta |
| Terjemahan awal | Keluar 0; 27.36 saat |
| Semakan awal | Keluar 0 |
| Sunting README dan semak | Keluar 1; terjemahan usang dikesan |
| Kemas kini terjemahan | Keluar 0; 22.17 saat |
| Semakan selepas kemas kini | Keluar 0; tiada ralat atau amaran |
| Panduan tidak berubah | Byte yang sama sebelum dan selepas kemas kini README |
| Jalankan lagi | Keluar 0; hash yang sama untuk semua fail terjemahan |

Ini adalah pengukuran setiap larian, bukan jaminan prestasi. Masa penyediaan dikecualikan; pengebilan penyedia tidak diukur. Larian yang tidak berubah masih boleh melakukan pemeriksaan kesihatan penyedia.

Periksa [terjemahan awal](../../assets/demo/before.txt), [terjemahan yang dikemas kini](../../assets/demo/after.txt), [perbezaan terjemahan lengkap](../../assets/demo/update.diff), [semakan usang](../../assets/demo/review-stale.txt), [semakan akhir](../../assets/demo/review-after.txt), dan [butiran larian](../../assets/demo/results.json). Terjemahan keseluruhan fail mungkin mengubah ungkapan lain, seperti yang ditunjukkan oleh diff yang dirakam. Kedua-dua artifak teks mengekalkan penafian yang dijana.

Semakan manusia masih penting: kemas kini yang dirakam menggunakan `[사용 가이드](guide.md)을`; partikel Korea sepatutnya `[사용 가이드](guide.md)를`. Artifak teks mengekalkan keluaran ini tanpa menampilkan terjemahan yang disunting sebagai keluaran model. Semakan struktur lulus walaupun terdapat isu penggubahan kata ini.

## 1. Sediakan folder kecil

Gunakan Python 3.11–3.14 dan [tetapan persekitaran maya](configuration.md#local-runtime-setup). Pasang versi yang digunakan untuk contoh ini:

```bash
python -m pip install co-op-translator==0.21.0
mkdir translation-demo
cd translation-demo
git init
```

Muat turun [README.txt](../../assets/demo/README.txt) dan [guide.txt](../../assets/demo/guide.txt) ke dalam folder ini, simpan sebagai `README.md` dan `guide.md`. Mereka adalah dokumen projek fiksyen kecil; tiada pemasangan aplikasi diperlukan.

README termasuk satu blok kod dan pautan ke `guide.md`. Ayat terakhirnya ialah:

```text
Notes are saved locally.
```

Simpan hanya kedua-dua dokumen sumber ini dalam folder ini. Semua perintah berikut dijalankan di dalam `translation-demo` dan berfungsi di Bash dan PowerShell.

## 2. Pratonton tanpa kelayakan

```bash
translate -l "ko" -md --dry-run
```

Pratonton menganggarkan kerja terjemahan tanpa memanggil model atau menulis terjemahan. Anggaran token bukanlah sebut harga pengebilan. Larian pertama sepatutnya mengenal pasti kedua-dua fail Markdown sebagai kerja baru.

## 3. Pilih penyedia dan terjemah

Konfigurasikan satu penyedia menggunakan [panduan konfigurasi](configuration.md): Azure OpenAI, OpenAI, atau Anthropic. Terjemahan teks OpenAI dan Anthropic tidak memerlukan akaun Azure. Perkhidmatan imej tidak diperlukan untuk contoh ini.

Jika anda menggunakan fail `.env` tempatan, tambahkan `.env` ke `.gitignore` folder ini. Panggilan terjemahan menggunakan akaun penyedia anda dan mungkin akan menimbulkan caj.

```bash
translate -l "ko" -md
co-op-review -l "ko"
```

Buka `translations/ko/README.md` dan `translations/ko/guide.md`. Semak penggubahan kata dalam bahasa Korea, blok kod, dan pautan dari README terjemahan ke panduan terjemahan. Ungkapan keluaran berbeza mengikut model.

`co-op-review` memeriksa kesegaran, struktur, dan pautan tempatan. Keputusan lulus tidak mengesahkan ketepatan linguistik. Selesaikan sebarang ralat yang dilaporkan sebelum meneruskan.

Rekod asas yang berjaya dengan Git (konfigurasikan identiti Git anda dahulu jika perlu):

```bash
git add README.md guide.md translations
git commit -m "Record initial Korean translation"
```

## 4. Tukar sumber

Dalam `README.md`, ganti `Notes are saved locally.` dengan:

```text
Notes are saved locally as Markdown files.
```

Biarkan `guide.md` tidak diubah. Kemudian jalankan:

```bash
co-op-review -l "ko"
translate -l "ko" -md --dry-run
```

Semakan harus melaporkan terjemahan README sebagai usang dan keluar dengan tidak berjaya. Ini adalah keadaan antara yang dijangka. Pratonton sepatutnya mengenal pasti kerja untuk README yang diubah.

## 5. Kemas kini dan periksa diff

```bash
translate -l "ko" -md
git diff -- README.md translations/ko/README.md
git diff -- translations/ko/guide.md
co-op-review -l "ko"
```

Periksa diff sebenar: CLI lalai menterjemah semula fail yang diubah, jadi model juga boleh mengubah penggubahan kata lain dalam fail itu. Panduan yang tidak diubah sepatutnya tiada diff. Semakan tidak sepatutnya lagi melaporkan README sebagai usang; siasat sebarang penemuan lain dan jangan mengabaikannya.

Pemeliharaan aras-blok terhadap suntingan Markdown manusia memerlukan penyedia status terjemahan pilihan dalam [Python API](api.md). Ia tidak diaktifkan oleh perintah CLI ini.

## 6. Jalankan lagi tanpa perubahan

Komit sumber dan terjemahan yang dikemas kini:

```bash
git add README.md translations
git commit -m "Update Korean translation after source edit"
translate -l "ko" -md
git diff --exit-code -- translations
```

Dengan terjemahan semasa dan konfigurasi yang tidak berubah, penterjemah melangkau fail tersebut. Perintah Git terakhir sepatutnya menghasilkan tiada diff dan keluar dengan berjaya.

## Langkah seterusnya

- [Terjemahkan hanya README dan buka permintaan tarik](github-actions.md#your-first-readme-translation-pr).
- [Pilih CLI, Python API, atau MCP](workflows.md).
- [Laporkan masalah terjemahan tanpa pengkodan](https://github.com/Azure/co-op-translator/issues/new?template=translation_feedback.yml).