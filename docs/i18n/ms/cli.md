# Rujukan CLI

Co-op Translator memasang titik masuk baris perintah berikut:

- `translate`
- `evaluate`
- `migrate-links`
- `co-op-review`
- `co-op-translator-mcp`

Perintah `translate`, `evaluate`, `migrate-links`, dan `co-op-review` dihantar melalui `co_op_translator.__main__`, yang memilih pelaksanaan perintah berdasarkan nama skrip yang dipanggil. Pelayan MCP menggunakan `co_op_translator.mcp.server` secara langsung.

Jika anda sedang memutuskan antara CLI, Python API, dan MCP, mulakan dengan [Pilih Aliran Kerja Anda](workflows.md).

## Aliran CLI Kali Pertama

Mulakan di sini jika anda menggunakan Co-op Translator dari terminal:

1. Konfigurasikan pembekal LLM seperti yang diterangkan dalam [Konfigurasi](configuration.md).
2. Pilih jenis kandungan yang anda mahu terjemahkan.
3. Jalankan perintah tertumpu terlebih dahulu, seperti terjemahan Markdown sahaja.
4. Gunakan `--dry-run` sebelum perubahan repositori besar.
5. Gunakan `co-op-review` selepas terjemahan untuk memeriksa struktur dan kesegaran.

| Matlamat | Perintah untuk mula |
| --- | --- |
| Terjemah dokumen Markdown | `translate -l "ko" -md` |
| Terjemah notebook | `translate -l "ko" -nb` |
| Terjemah teks imej | `translate -l "ko" -img` |
| Pratonton kerja tanpa menulis fail | `translate -l "ko" -md --dry-run` |
| Semak terjemahan sedia ada | `co-op-review -l "ko"` |
| Kemas kini pautan notebook dan Markdown | `migrate-links -l "ko" --dry-run` |
| Dedahkan alat kepada klien MCP | Konfigurasikan [Pelayan MCP](mcp.md) dan bukannya menjalankan arahan CLI secara langsung. |

## translate

Terjemahkan fail Markdown, notebook, dan teks imej ke dalam satu atau lebih bahasa sasaran.

```bash
translate -l "ko ja fr"
```

### Contoh Lazim

Terjemah hanya Markdown:

```bash
translate -l "de" -md
```

Terjemah hanya notebook:

```bash
translate -l "zh-CN" -nb
```

Terjemah Markdown dan imej:

```bash
translate -l "pt-BR" -md -img
```

Kemas kini terjemahan sedia ada dengan memadam dan membuat semula:

```bash
translate -l "ko" -u
```

Jalankan tanpa arahan interaktif:

```bash
translate -l "ko ja" -md -y
```

Simpan log:

```bash
translate -l "ko" -s
```

### Pilihan

| Pilihan | Diperlukan | Penerangan |
| --- | --- | --- |
| `-l`, `--language-codes` | Ya | Kod bahasa yang dipisahkan oleh ruang, seperti `"es fr de"`, atau `"all"`. |
| `-r`, `--root-dir` | Tidak | Akar projek. Secara lalai kepada direktori semasa. |
| `-u`, `--update` | Tidak | Padam terjemahan sedia ada untuk bahasa yang dipilih dan buat semula. |
| `-img`, `--images` | Tidak | Terjemah hanya fail imej. |
| `-md`, `--markdown` | Tidak | Terjemah hanya fail Markdown. |
| `-nb`, `--notebook` | Tidak | Terjemah hanya fail Jupyter notebook. |
| `-d`, `--debug` | Tidak | Dayakan log debugging di konsol. |
| `-s`, `--save-logs` | Tidak | Simpan log peringkat DEBUG di bawah `<root-dir>/logs/`. |
| `-x`, `--fix` | Tidak | Terjemah semula fail Markdown berkeyakinan rendah berdasarkan keputusan penilaian terdahulu. |
| `-c`, `--min-confidence` | Tidak | Ambang keyakinan untuk `--fix`. Secara lalai `0.7`. |
| `--add-disclaimer`, `--no-disclaimer` | Tidak | Tambah atau sembunyikan penafian terjemahan mesin. Secara lalai diaktifkan dalam CLI. |
| `-f`, `--fast` | Tidak | Mod imej pantas yang usang. |
| `-y`, `--yes` | Tidak | Sahkan arahan secara automatik, berguna dalam CI. |
| `--repo-url` | Tidak | URL repositori yang digunakan dalam nasihat sparse-checkout jadual bahasa dalam README. |
| `--migrate-language-folders` | Tidak | Namakan semula folder alias lama, seperti `cn` atau `tw`, kepada folder BCP 47 kanonik. |
| `--dry-run` | Tidak | Pratonton migrasi folder bahasa dan anggaran terjemahan tanpa menulis fail. |

Jika tiada bendera jenis disediakan, `translate` memproses Markdown, notebook, dan imej. Terjemahan imej memerlukan konfigurasi Azure AI Vision.

## evaluate

Menilai kualiti terjemahan Markdown untuk satu bahasa.

!!! warning "Experimental"
    `evaluate` is experimental. It can use rule-based and LLM-based quality checks, writes evaluation results into translation metadata, and its scoring model and metadata behavior may change.

```bash
evaluate -l "ko"
```

### Contoh Lazim

Gunakan ambang keyakinan rendah yang lebih ketat:

```bash
evaluate -l "es" -c 0.8
```

Jalankan pemeriksaan berasaskan peraturan sahaja:

```bash
evaluate -l "fr" -f
```

Jalankan pemeriksaan berasaskan LLM sahaja:

```bash
evaluate -l "ja" -D
```

### Pilihan

| Pilihan | Diperlukan | Penerangan |
| --- | --- | --- |
| `-l`, `--language-code` | Ya | Kod bahasa tunggal untuk dinilai. Kod alias dinormalisasikan. |
| `-r`, `--root-dir` | Tidak | Akar projek. Secara lalai kepada direktori semasa. |
| `-c`, `--min-confidence` | Tidak | Ambang digunakan apabila menyenaraikan terjemahan berkeyakinan rendah. Secara lalai `0.7`. |
| `-d`, `--debug` | Tidak | Dayakan log debugging. |
| `-s`, `--save-logs` | Tidak | Simpan log peringkat DEBUG di bawah `<root-dir>/logs/`. |
| `-f`, `--fast` | Tidak | Hanya penilaian berasaskan peraturan. |
| `-D`, `--deep` | Tidak | Hanya penilaian berasaskan LLM. |

Secara lalai, `evaluate` menggunakan kedua-dua penilaian berasaskan peraturan dan berasaskan LLM. Keputusan ditulis ke dalam metadata terjemahan dan diringkaskan di konsol.

## co-op-review

Jalankan pemeriksaan penyelenggaraan terjemahan deterministik tanpa kelayakan API.

!!! note "Beta"
    `co-op-review` is a beta deterministic review command. It does not call model providers or write files, but its checks and issue output schema may evolve.

```bash
co-op-review -l "ko"
```

### Contoh Lazim

Semak terjemahan Korea dan Jepun dari direktori semasa:

```bash
co-op-review -l "ko ja"
```

Semak akar projek tertentu:

```bash
co-op-review -l "fr" -r ./my-course
```

Semak hanya fail sumber yang diubah berbanding ref asas:

```bash
co-op-review -l "ko" --changed-from origin/main
```

Cetak output Markdown gaya GitHub untuk ringkasan CI:

```bash
co-op-review -l "ko ja" --changed-from origin/main --format github
```

### Pilihan

| Pilihan | Diperlukan | Penerangan |
| --- | --- | --- |
| `-l`, `--language-code` | Tidak | Kod bahasa untuk disemak. Boleh diberikan berulang kali atau sebagai nilai dipisahkan ruang. Secara lalai untuk semua bahasa terjemahan yang ditemui. |
| `-r`, `--root-dir` | Tidak | Akar projek. Secara lalai kepada direktori semasa. |
| `--changed-from` | Tidak | Ref Git yang digunakan untuk mengehadkan semakan kepada fail sumber yang diubah. |
| `--format` | Tidak | Format output: `text` atau `github`. Secara lalai `text`. |

`co-op-review` pada masa ini memeriksa fail terjemahan yang hilang, metadata terjemahan yang hilang atau ketinggalan, integriti frontmatter Markdown dan pagar kod, JSON notebook terjemahan yang tidak sah, dan sasaran pautan Markdown atau imej tempatan yang hilang. Pautan yang hilang adalah amaran secara lalai; masalah struktur dan kesegaran akan menyebabkan arahan gagal.

## co-op-translator-mcp

Jalankan pelayan MCP Co-op Translator untuk agen, penyunting, dan klien yang serasi MCP.

```bash
co-op-translator-mcp
```

Pengangkutan lalai ialah `stdio`. Lihat panduan [Pelayan MCP](mcp.md) untuk konfigurasi klien, alat, sumber, dan nota keselamatan.

### Pilihan

| Pilihan | Diperlukan | Penerangan |
| --- | --- | --- |
| `--transport` | Tidak | Pengangkutan MCP: `stdio`, `streamable-http`, atau `sse`. Secara lalai `stdio`. |

## migrate-links

Proses semula fail Markdown terjemahan dan kemas kini pautan notebook supaya mereka menunjuk kepada notebook terjemahan apabila tersedia.

```bash
migrate-links -l "ko ja"
```

### Contoh Lazim

Pratonton kemas kini pautan:

```bash
migrate-links -l "ko" --dry-run
```

Proses semua bahasa yang disokong tanpa pengesahan:

```bash
migrate-links -l "all" -y
```

Tulis semula pautan hanya apabila notebook terjemahan wujud:

```bash
migrate-links -l "ko" --no-fallback-to-original
```

### Pilihan

| Pilihan | Diperlukan | Penerangan |
| --- | --- | --- |
| `-l`, `--language-codes` | Ya | Kod bahasa dipisahkan ruang, atau `"all"`. |
| `-r`, `--root-dir` | Tidak | Akar projek. Secara lalai kepada direktori semasa. |
| `--image-dir` | Tidak | Direktori imej terjemahan relatif kepada akar. Secara lalai `translated_images`. |
| `--dry-run` | Tidak | Tunjukkan fail yang akan berubah tanpa menulis kemas kini. |
| `--fallback-to-original`, `--no-fallback-to-original` | Tidak | Gunakan pautan notebook asal apabila notebook terjemahan tiada. Diaktifkan secara lalai. |
| `-d`, `--debug` | Tidak | Dayakan log debugging. |
| `-s`, `--save-logs` | Tidak | Simpan log peringkat DEBUG di bawah `<root-dir>/logs/`. |
| `-y`, `--yes` | Tidak | Sahkan arahan secara automatik apabila memproses semua bahasa. |

## Persekitaran

Semua arahan memerlukan satu pembekal LLM yang dikonfigurasikan:

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

Terjemahan imej juga memerlukan Azure AI Vision:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

## Susunan output

Terjemahan teks ditulis di bawah:

```text
translations/<language-code>/<original-path>
```

Keluaran imej terjemahan ditulis di bawah:

```text
translated_images/<language-code>/<original-path>
```

Sebagai contoh, menterjemah `README.md` dan `docs/setup.md` ke dalam Bahasa Korea menghasilkan:

```text
translations/ko/README.md
translations/ko/docs/setup.md
```

## Contoh CLI Salin-Tampal

Terjemah Markdown ke dalam tiga bahasa:

```bash
translate -l "ko ja fr" -md
```

Terjemah notebook sahaja:

```bash
translate -l "zh-CN" -nb
```

Terjemah imej sahaja:

```bash
translate -l "pt-BR" -img
```

Pratonton terjemahan Markdown tanpa menulis fail:

```bash
translate -l "de es" -md --dry-run
```

Baiki terjemahan Markdown berkeyakinan rendah:

```bash
evaluate -l "ko" -c 0.8
translate -l "ko" --fix -c 0.8 -md
```

Jalankan terjemahan Markdown mesra CI:

```bash
translate -l "ko ja" -md -y -s
```

Semak output terjemahan:

```bash
co-op-review -l "ko ja"
```

Pratonton migrasi pautan:

```bash
migrate-links -l "ko" --dry-run
```