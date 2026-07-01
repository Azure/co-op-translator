# CLI Reference

Co-op Translator menginstal titik masuk baris perintah ini:

- `translate`
- `evaluate`
- `migrate-links`
- `co-op-review`
- `co-op-translator-mcp`

Perintah `translate`, `evaluate`, `migrate-links`, dan `co-op-review` meneruskan melalui `co_op_translator.__main__`, yang memilih implementasi perintah berdasarkan nama skrip yang dipanggil. Server MCP menggunakan `co_op_translator.mcp.server` secara langsung.

Jika Anda sedang memutuskan antara CLI, Python API, dan MCP, mulailah dengan [Pilih Alur Kerja Anda](workflows.md).

## First-Time CLI Flow

Mulai di sini jika Anda menggunakan Co-op Translator dari terminal:

1. Konfigurasikan penyedia LLM seperti dijelaskan di [Configuration](configuration.md).
2. Pilih jenis konten yang ingin Anda terjemahkan.
3. Jalankan perintah yang fokus terlebih dahulu, seperti terjemahan khusus Markdown.
4. Gunakan `--dry-run` sebelum perubahan besar pada repositori.
5. Gunakan `co-op-review` setelah terjemahan untuk memeriksa struktur dan kebaruan.

| Tujuan | Perintah untuk memulai |
| --- | --- |
| Terjemahkan dokumen Markdown | `translate -l "ko" -md` |
| Terjemahkan notebook | `translate -l "ko" -nb` |
| Terjemahkan teks gambar | `translate -l "ko" -img` |
| Pratinjau pekerjaan tanpa menulis file | `translate -l "ko" -md --dry-run` |
| Tinjau terjemahan yang ada | `co-op-review -l "ko"` |
| Perbarui tautan notebook dan Markdown | `migrate-links -l "ko" --dry-run` |
| Mengekspos alat ke klien MCP | Konfigurasikan [Server MCP](mcp.md) alih-alih menjalankan perintah CLI secara langsung. |

## translate

Menerjemahkan file Markdown, notebook, dan teks gambar ke satu atau lebih bahasa target.

```bash
translate -l "ko ja fr"
```

### Contoh umum

Terjemahkan hanya Markdown:

```bash
translate -l "de" -md
```

Terjemahkan hanya notebook:

```bash
translate -l "zh-CN" -nb
```

Terjemahkan Markdown dan gambar:

```bash
translate -l "pt-BR" -md -img
```

Perbarui terjemahan yang ada dengan menghapus dan membuat ulang:

```bash
translate -l "ko" -u
```

Jalankan tanpa prompt interaktif:

```bash
translate -l "ko ja" -md -y
```

Simpan log:

```bash
translate -l "ko" -s
```

### Opsi

| Opsi | Diperlukan | Deskripsi |
| --- | --- | --- |
| `-l`, `--language-codes` | Ya | Kode bahasa dipisahkan spasi, seperti `"es fr de"`, atau `"all"`. |
| `-r`, `--root-dir` | Tidak | Root proyek. Default ke direktori saat ini. |
| `-u`, `--update` | Tidak | Hapus terjemahan yang ada untuk bahasa yang dipilih dan buat ulang. |
| `-img`, `--images` | Tidak | Terjemahkan hanya file gambar. |
| `-md`, `--markdown` | Tidak | Terjemahkan hanya file Markdown. |
| `-nb`, `--notebook` | Tidak | Terjemahkan hanya file Jupyter notebook. |
| `-d`, `--debug` | Tidak | Aktifkan logging debug di konsol. |
| `-s`, `--save-logs` | Tidak | Simpan log level DEBUG di bawah `<root-dir>/logs/`. |
| `-x`, `--fix` | Tidak | Terjemahkan ulang file Markdown dengan kepercayaan rendah berdasarkan hasil evaluasi sebelumnya. |
| `-c`, `--min-confidence` | Tidak | Ambang kepercayaan untuk `--fix`. Defaultnya `0.7`. |
| `--add-disclaimer`, `--no-disclaimer` | Tidak | Tambahkan atau hentikan penyangkalan terjemahan mesin. Defaultnya diaktifkan di CLI. |
| `-f`, `--fast` | Tidak | Mode gambar cepat yang sudah usang. |
| `-y`, `--yes` | Tidak | Otomatis mengonfirmasi prompt, berguna di CI. |
| `--repo-url` | Tidak | URL repositori yang digunakan dalam nasihat sparse-checkout pada tabel bahasa di README. |
| `--migrate-language-folders` | Tidak | Ganti nama folder alias lama, seperti `cn` atau `tw`, menjadi folder BCP 47 kanonik. |
| `--dry-run` | Tidak | Pratinjau migrasi folder bahasa dan perkiraan terjemahan tanpa menulis file. |

Jika tidak ada flag tipe yang diberikan, `translate` memproses Markdown, notebook, dan gambar. Penerjemahan gambar memerlukan konfigurasi Azure AI Vision.

## evaluate

Mengevaluasi kualitas terjemahan Markdown untuk satu bahasa.

!!! warning "Eksperimental"
    `evaluate` bersifat eksperimental. Perintah ini dapat menggunakan pemeriksaan kualitas berbasis aturan dan berbasis LLM, menulis hasil evaluasi ke metadata terjemahan, dan model penilaian serta perilaku metadata dapat berubah.

```bash
evaluate -l "ko"
```

### Contoh umum

Gunakan ambang kepercayaan rendah yang lebih ketat:

```bash
evaluate -l "es" -c 0.8
```

Jalankan pemeriksaan berbasis aturan saja:

```bash
evaluate -l "fr" -f
```

Jalankan pemeriksaan berbasis LLM saja:

```bash
evaluate -l "ja" -D
```

### Opsi

| Opsi | Diperlukan | Deskripsi |
| --- | --- | --- |
| `-l`, `--language-code` | Ya | Kode bahasa tunggal untuk dievaluasi. Kode alias dinormalisasi. |
| `-r`, `--root-dir` | Tidak | Root proyek. Default ke direktori saat ini. |
| `-c`, `--min-confidence` | Tidak | Ambang yang digunakan saat mencantumkan terjemahan berkepercayaan rendah. Defaultnya `0.7`. |
| `-d`, `--debug` | Tidak | Aktifkan logging debug. |
| `-s`, `--save-logs` | Tidak | Simpan log level DEBUG di bawah `<root-dir>/logs/`. |
| `-f`, `--fast` | Tidak | Hanya evaluasi berbasis aturan. |
| `-D`, `--deep` | Tidak | Hanya evaluasi berbasis LLM. |

Secara default, `evaluate` menggunakan evaluasi berbasis aturan dan LLM. Hasil ditulis ke metadata terjemahan dan disimpulkan di konsol.

## co-op-review

Jalankan pemeriksaan pemeliharaan terjemahan deterministik tanpa kredensial API.

!!! note "Beta"
    `co-op-review` adalah perintah ulasan deterministik beta. Perintah ini tidak memanggil penyedia model atau menulis file, tetapi pemeriksaan dan skema keluaran isu dapat berkembang.

```bash
co-op-review -l "ko"
```

### Contoh umum

Tinjau terjemahan Korea dan Jepang dari direktori saat ini:

```bash
co-op-review -l "ko ja"
```

Tinjau root proyek tertentu:

```bash
co-op-review -l "fr" -r ./my-course
```

Tinjau hanya file sumber yang berubah terhadap ref dasar:

```bash
co-op-review -l "ko" --changed-from origin/main
```

Cetak keluaran Markdown bergaya GitHub untuk ringkasan CI:

```bash
co-op-review -l "ko ja" --changed-from origin/main --format github
```

### Opsi

| Opsi | Diperlukan | Deskripsi |
| --- | --- | --- |
| `-l`, `--language-code` | Tidak | Kode bahasa untuk ditinjau. Dapat dilewatkan beberapa kali atau sebagai nilai dipisah spasi. Defaultnya semua bahasa terjemahan yang ditemukan. |
| `-r`, `--root-dir` | Tidak | Root proyek. Default ke direktori saat ini. |
| `--changed-from` | Tidak | Ref Git yang digunakan untuk membatasi tinjauan ke file sumber yang berubah. |
| `--format` | Tidak | Format keluaran: `text` atau `github`. Defaultnya `text`. |

`co-op-review` saat ini memeriksa file terjemahan yang hilang, metadata terjemahan yang hilang atau usang, integritas frontmatter Markdown dan pagar kode, JSON notebook terjemahan yang tidak valid, dan target tautan lokal Markdown atau gambar yang hilang. Tautan yang hilang merupakan peringatan secara default; masalah struktural dan kebaruan membuat perintah gagal.

## co-op-translator-mcp

Jalankan server MCP Co-op Translator untuk agen, editor, dan klien yang kompatibel dengan MCP.

```bash
co-op-translator-mcp
```

Transport default adalah `stdio`. Lihat panduan [Server MCP](mcp.md) untuk konfigurasi klien, alat, sumber daya, dan catatan keamanan.

### Opsi

| Opsi | Diperlukan | Deskripsi |
| --- | --- | --- |
| `--transport` | Tidak | Transport MCP: `stdio`, `streamable-http`, atau `sse`. Defaultnya `stdio`. |

## migrate-links

Proses ulang file Markdown terjemahan dan perbarui tautan notebook sehingga mengarah ke notebook terjemahan jika tersedia.

```bash
migrate-links -l "ko ja"
```

### Contoh umum

Pratinjau pembaruan tautan:

```bash
migrate-links -l "ko" --dry-run
```

Proses semua bahasa yang didukung tanpa konfirmasi:

```bash
migrate-links -l "all" -y
```

Hanya tulis ulang tautan ketika notebook terjemahan ada:

```bash
migrate-links -l "ko" --no-fallback-to-original
```

### Opsi

| Opsi | Diperlukan | Deskripsi |
| --- | --- | --- |
| `-l`, `--language-codes` | Ya | Kode bahasa dipisahkan spasi, atau `"all"`. |
| `-r`, `--root-dir` | Tidak | Root proyek. Default ke direktori saat ini. |
| `--image-dir` | Tidak | Direktori gambar terjemahan relatif terhadap root. Defaultnya `translated_images`. |
| `--dry-run` | Tidak | Tampilkan file yang akan berubah tanpa menulis pembaruan. |
| `--fallback-to-original`, `--no-fallback-to-original` | Tidak | Gunakan tautan notebook asli ketika notebook terjemahan tidak ada. Diaktifkan secara default. |
| `-d`, `--debug` | Tidak | Aktifkan logging debug. |
| `-s`, `--save-logs` | Tidak | Simpan log level DEBUG di bawah `<root-dir>/logs/`. |
| `-y`, `--yes` | Tidak | Otomatis mengonfirmasi prompt saat memproses semua bahasa. |

## Environment

Semua perintah memerlukan satu penyedia LLM yang dikonfigurasi:

```bash
# Azure OpenAI
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"

# Atau OpenAI
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

Penerjemahan gambar juga membutuhkan Azure AI Vision:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

## Output layout

Terjemahan teks ditulis di bawah:

```text
translations/<language-code>/<original-path>
```

Keluaran gambar terjemahan ditulis di bawah:

```text
translated_images/<language-code>/<original-path>
```

Sebagai contoh, menerjemahkan `README.md` dan `docs/setup.md` ke dalam bahasa Korea menghasilkan:

```text
translations/ko/README.md
translations/ko/docs/setup.md
```

## Copy-Paste CLI Examples

Terjemahkan Markdown ke tiga bahasa:

```bash
translate -l "ko ja fr" -md
```

Terjemahkan notebook saja:

```bash
translate -l "zh-CN" -nb
```

Terjemahkan gambar saja:

```bash
translate -l "pt-BR" -img
```

Pratinjau terjemahan Markdown tanpa menulis file:

```bash
translate -l "de es" -md --dry-run
```

Perbaiki terjemahan Markdown dengan kepercayaan rendah:

```bash
evaluate -l "ko" -c 0.8
translate -l "ko" --fix -c 0.8 -md
```

Jalankan terjemahan Markdown yang ramah CI:

```bash
translate -l "ko ja" -md -y -s
```

Tinjau keluaran terjemahan:

```bash
co-op-review -l "ko ja"
```

Pratinjau migrasi tautan:

```bash
migrate-links -l "ko" --dry-run
```