# Terjemahkan, sunting, dan tinjau proyek kecil

Mulailah dengan dua berkas Markdown pendek dan satu bahasa target. Anda akan melihat di mana terjemahan ditulis, apa yang terjadi ketika sumber berubah, dan bagaimana memeriksa hasilnya.

## Hasil yang dicatat

Contoh dijalankan pada 19 September 2026 dengan Co-op Translator 0.21.0 dan Azure OpenAI (`gpt-5-mini`). Perintah CLI yang tidak dimodifikasi dipanggil melalui `CliRunner` milik Click menggunakan wheel yang dibangun dan dependensi Python yang ada.

| Langkah | Hasil |
| --- | --- |
| Pratinjau | Exit 0; tidak ada permintaan terjemahan model |
| Terjemahan awal | Exit 0; 27.36 detik |
| Tinjauan awal | Exit 0 |
| Sunting README dan tinjau | Exit 1; terjemahan usang terdeteksi |
| Perbarui terjemahan | Exit 0; 22.17 detik |
| Tinjauan setelah pembaruan | Exit 0; tidak ada kesalahan atau peringatan |
| Panduan tidak berubah | Byte identik sebelum dan setelah pembaruan README |
| Jalankan lagi | Exit 0; hash identik untuk semua berkas terjemahan |

Ini adalah pengukuran tiap kali dijalankan, bukan jaminan kinerja. Waktu penyiapan dikecualikan; penagihan penyedia tidak diukur. Jalankan tanpa perubahan tetap bisa melakukan pemeriksaan kesehatan penyedia.

Periksa [terjemahan awal](../../assets/demo/before.txt), [terjemahan yang diperbarui](../../assets/demo/after.txt), [diff terjemahan lengkap](../../assets/demo/update.diff), [tinjauan usang](../../assets/demo/review-stale.txt), [tinjauan akhir](../../assets/demo/review-after.txt), dan [rincian run](../../assets/demo/results.json). Terjemahan seluruh berkas mungkin mengubah kata-kata lain, seperti yang ditunjukkan oleh diff yang diambil. Kedua artefak teks mempertahankan penafian yang dihasilkan.

Tinjauan manusia tetap penting: pembaruan yang diambil menggunakan `[사용 가이드](guide.md)을`; partikel bahasa Korea seharusnya `[사용 가이드](guide.md)를`. Artefak teks mempertahankan keluaran ini apa adanya daripada menampilkan terjemahan yang diedit sebagai keluaran model. Tinjauan struktural lulus meskipun ada masalah pemilihan kata ini.

## 1. Siapkan sebuah folder kecil

Gunakan Python 3.11–3.14 dan [pengaturan lingkungan virtual](configuration.md#local-runtime-setup). Instal versi yang digunakan untuk contoh ini:

```bash
python -m pip install co-op-translator==0.21.0
mkdir translation-demo
cd translation-demo
git init
```

Unduh [README.txt](../../assets/demo/README.txt) dan [guide.txt](../../assets/demo/guide.txt) ke dalam folder ini, simpan sebagai `README.md` dan `guide.md`. Mereka adalah dokumen proyek fiksi kecil; tidak diperlukan pemasangan aplikasi.

README berisi blok kode dan tautan ke `guide.md`. Kalimat terakhirnya adalah:

```text
Notes are saved locally.
```

Pertahankan hanya kedua dokumen sumber ini di folder ini. Semua perintah berikut dijalankan di dalam `translation-demo` dan bekerja di Bash serta PowerShell.

## 2. Pratinjau tanpa kredensial

```bash
translate -l "ko" -md --dry-run
```

Pratinjau memperkirakan pekerjaan terjemahan tanpa memanggil model atau menulis terjemahan. Perkiraan token bukan merupakan kutipan penagihan. Jalankan pertama kali seharusnya mengidentifikasi kedua berkas Markdown sebagai pekerjaan baru.

## 3. Pilih penyedia dan terjemahkan

Konfigurasikan satu penyedia menggunakan [panduan konfigurasi](configuration.md): Azure OpenAI, OpenAI, atau Anthropic. Terjemahan teks OpenAI dan Anthropic tidak memerlukan akun Azure. Layanan gambar tidak diperlukan untuk contoh ini.

Jika Anda menggunakan berkas `.env` lokal, tambahkan `.env` ke `.gitignore` folder ini. Panggilan terjemahan menggunakan akun penyedia Anda dan mungkin dikenai biaya.

```bash
translate -l "ko" -md
co-op-review -l "ko"
```

Buka `translations/ko/README.md` dan `translations/ko/guide.md`. Periksa pemilihan kata dalam bahasa Korea, blok kode, dan tautan dari README yang diterjemahkan ke panduan yang diterjemahkan. Pilihan kata keluaran bervariasi menurut model.

`co-op-review` memeriksa kebaruan, struktur, dan tautan lokal. Hasil yang lulus tidak menjamin ketepatan linguistik. Selesaikan semua kesalahan yang dilaporkan sebelum melanjutkan.

Catat baseline yang berhasil dengan Git (konfigurasikan identitas Git Anda terlebih dahulu jika perlu):

```bash
git add README.md guide.md translations
git commit -m "Record initial Korean translation"
```

## 4. Ubah sumber

Di `README.md`, gantikan `Notes are saved locally.` dengan:

```text
Notes are saved locally as Markdown files.
```

Biarkan `guide.md` tidak berubah. Kemudian jalankan:

```bash
co-op-review -l "ko"
translate -l "ko" -md --dry-run
```

Tinjauan harus melaporkan terjemahan README sebagai usang dan keluar dengan gagal. Ini adalah keadaan menengah yang diharapkan. Pratinjau harus mengidentifikasi pekerjaan untuk README yang diubah.

## 5. Perbarui dan periksa diff

```bash
translate -l "ko" -md
git diff -- README.md translations/ko/README.md
git diff -- translations/ko/guide.md
co-op-review -l "ko"
```

Periksa diff nyata: CLI default menerjemahkan ulang berkas yang diubah, sehingga model juga dapat merevisi kata-kata lain dalam berkas itu. Panduan yang tidak diubah seharusnya tidak memiliki diff. Tinjauan tidak lagi harus melaporkan README sebagai usang; selidiki temuan lain daripada mengabaikannya.

Pelestarian tingkat-blok terhadap suntingan Markdown manusia memerlukan penyedia status terjemahan opsional di [Python API](api.md). Ini tidak diaktifkan oleh perintah CLI ini.

## 6. Jalankan lagi tanpa perubahan

Commit sumber yang diperbarui dan terjemahan:

```bash
git add README.md translations
git commit -m "Update Korean translation after source edit"
translate -l "ko" -md
git diff --exit-code -- translations
```

Dengan terjemahan saat ini dan konfigurasi yang tidak berubah, penerjemah melewatkan berkas-berkas tersebut. Perintah Git terakhir seharusnya tidak menghasilkan diff dan keluar dengan sukses.

## Langkah selanjutnya

- [Terjemahkan hanya README dan buka pull request](github-actions.md#your-first-readme-translation-pr).
- [Pilih CLI, Python API, atau MCP](workflows.md).
- [Laporkan masalah terjemahan tanpa menulis kode](https://github.com/Azure/co-op-translator/issues/new?template=translation_feedback.yml).