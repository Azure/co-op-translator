# Rujukan CLI

Co-op Translator memasang titik masuk baris perintah berikut:

- `translate`
- `evaluate`
- `migrate-links`
- `co-op-review`
- `co-op-translator-mcp`

Perintah `translate`, `evaluate`, `migrate-links`, dan `co-op-review` dihantar melalui `co_op_translator.__main__`, yang memilih pelaksanaan perintah berdasarkan nama skrip yang dipanggil. Pelayan MCP menggunakan `co_op_translator.mcp.server` secara langsung.

Jika anda sedang memilih antara CLI, API Python, dan MCP, mulakan dengan [Pilih Aliran Kerja Anda](workflows.md).

## Keluaran Konsol

Terminal interaktif menggunakan pemformatan Rich untuk tajuk perintah, kemajuan, dan ringkasan. CI dan keluaran bukan interaktif secara automatik beralih kepada teks biasa.

Tetapkan `CO_OP_TRANSLATOR_OUTPUT_STYLE=plain` untuk memaksa keluaran teks biasa, atau `CO_OP_TRANSLATOR_OUTPUT_STYLE=rich` untuk memaksa keluaran Rich. Tetapkan `CO_OP_TRANSLATOR_NO_PROGRESS=1` untuk mengekalkan ringkasan sambil menyekat bar kemajuan langsung.

Gunakan `translate --json-events progress.ndjson` apabila sistem lain memerlukan kemajuan yang boleh dibaca mesin. CLI terus menghasilkan keluaran mesra-manusia, sementara fail NDJSON menerima acara berversi `co-op.translation.event.v1` dengan medan stabil seperti `type`, `stage_key`, `completed`, `total`, dan `current_path`.





## Aliran CLI Kali Pertama

Mulakan di sini jika anda menggunakan Co-op Translator dari terminal:

1. Konfigurasikan penyedia LLM seperti yang diterangkan dalam [Konfigurasi](configuration.md).
2. Pilih jenis kandungan yang anda ingin terjemahkan.
3. Jalankan perintah yang fokus terlebih dahulu, seperti terjemahan khusus Markdown.
4. Gunakan `--dry-run` sebelum membuat perubahan besar pada repositori.
5. Gunakan `co-op-review` selepas terjemahan untuk memeriksa struktur dan kesegaran.

| Matlamat | Perintah untuk dimulakan |
| --- | --- |
| Terjemahkan dokumen Markdown | `translate -l "ko" -md` |
| Terjemahkan notebook | `translate -l "ko" -nb` |
| Terjemahkan teks imej | `translate -l "ko" -img` |
| Pratonton kerja tanpa menulis fail | `translate -l "ko" -md --dry-run` |
| Semak terjemahan sedia ada | `co-op-review -l "ko"` |
| Kemas kini pautan notebook dan Markdown | `migrate-links -l "ko" --dry-run` |
| Dedahkan alat kepada klien MCP | Konfigurasikan [Pelayan MCP](mcp.md) dan bukannya menjalankan perintah CLI secara langsung. |

## translate

Terjemahkan fail Markdown, notebook, dan teks imej ke dalam satu atau lebih bahasa sasaran.

```bash
translate -l "ko ja fr"
```

### Contoh biasa

Terjemahkan hanya Markdown:

```bash
translate -l "de" -md
```

Terjemahkan hanya notebook:

```bash
translate -l "zh-CN" -nb
```

Terjemahkan Markdown dan imej:

```bash
translate -l "pt-BR" -md -img
```

Kemas kini terjemahan sedia ada dengan memadam dan mencipta semula:

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

Tulis acara kemajuan berstruktur:

```bash
translate -l "ko ja" -md --json-events progress.ndjson
```

### Pilihan

| Pilihan | Diperlukan | Penerangan |
| --- | --- | --- |
| `-l`, `--language-codes` | Ya | Kod bahasa yang dipisahkan oleh ruang, seperti `"es fr de"`, atau `"all"`. |
| `-r`, `--root-dir` | Tidak | Akar projek. Lalai kepada direktori semasa. |
| `-u`, `--update` | Tidak | Padam terjemahan sedia ada untuk bahasa yang dipilih dan cipta semula. |
| `-img`, `--images` | Tidak | Terjemahkan hanya fail imej. |
| `-md`, `--markdown` | Tidak | Terjemahkan hanya fail Markdown. |
| `-nb`, `--notebook` | Tidak | Terjemahkan hanya fail Jupyter notebook. |
| `-d`, `--debug` | Tidak | Aktifkan logging debug di konsol. |
| `-s`, `--save-logs` | Tidak | Simpan log peringkat DEBUG di bawah `<root-dir>/logs/`. |
| `--json-events` | Tidak | Tulis acara kemajuan terjemahan yang boleh dibaca mesin sebagai NDJSON. |
| `-x`, `--fix` | Tidak | Terjemah semula fail Markdown berkeyakinan rendah berdasarkan keputusan penilaian sebelumnya. |
| `-c`, `--min-confidence` | Tidak | Ambang keyakinan untuk `--fix`. Lalai kepada `0.7`. |
| `--add-disclaimer`, `--no-disclaimer` | Tidak | Tambah atau halang penafian terjemahan mesin. Lalai diaktifkan dalam CLI. |
| `-f`, `--fast` | Tidak | Mod imej pantas yang telah usang. |
| `-y`, `--yes` | Tidak | Auto-sahkan arahan, berguna dalam CI. |
| `--repo-url` | Tidak | URL repositori yang digunakan dalam jadual bahasa README untuk nasihat sparse-checkout. |
| `--migrate-language-folders` | Tidak | Namakan semula folder alias lama, seperti `cn` atau `tw`, kepada folder BCP 47 kanonik. |
| `--dry-run` | Tidak | Pratonton migrasi folder bahasa dan anggaran terjemahan tanpa menulis fail. |

Jika tiada flag jenis diberikan, `translate` memproses Markdown, notebook, dan imej. Terjemahan imej memerlukan konfigurasi Azure AI Vision.

## evaluate

Menilai kualiti terjemahan Markdown untuk satu bahasa.

!!! warning "Eksperimental"
    `evaluate` adalah eksperimental. Ia boleh menggunakan pemeriksaan kualiti berasaskan peraturan dan berasaskan LLM, menulis keputusan penilaian ke dalam metadata terjemahan, dan model pemarkahan serta kelakuan metadata mungkin berubah.

```bash
evaluate -l "ko"
```

### Contoh biasa

Gunakan ambang keyakinan rendah yang lebih ketat:

```bash
evaluate -l "es" -c 0.8
```

Jalankan hanya pemeriksaan berasaskan peraturan:

```bash
evaluate -l "fr" -f
```

Jalankan hanya pemeriksaan berasaskan LLM:

```bash
evaluate -l "ja" -D
```

### Pilihan

| Pilihan | Diperlukan | Penerangan |
| --- | --- | --- |
| `-l`, `--language-code` | Ya | Kod bahasa tunggal untuk dinilai. Kod alias dinormalkan. |
| `-r`, `--root-dir` | Tidak | Akar projek. Lalai kepada direktori semasa. |
| `-c`, `--min-confidence` | Tidak | Ambang yang digunakan apabila menyenaraikan terjemahan berkeyakinan rendah. Lalai kepada `0.7`. |
| `-d`, `--debug` | Tidak | Aktifkan logging debug. |
| `-s`, `--save-logs` | Tidak | Simpan log peringkat DEBUG di bawah `<root-dir>/logs/`. |
| `-f`, `--fast` | Tidak | Hanya penilaian berasaskan peraturan. |
| `-D`, `--deep` | Tidak | Hanya penilaian berasaskan LLM. |

Secara lalai, `evaluate` menggunakan kedua-dua penilaian berasaskan peraturan dan berasaskan LLM. Keputusan ditulis ke dalam metadata terjemahan dan diringkaskan di konsol.

## co-op-review

Jalankan pemeriksaan penyelenggaraan terjemahan deterministik tanpa kelayakan API.

!!! note "Beta"
    `co-op-review` adalah perintah semakan deterministik beta. Ia tidak memanggil penyedia model atau menulis fail, tetapi pemeriksaannya dan skema keluaran isu mungkin berubah.

```bash
co-op-review -l "ko"
```

### Contoh biasa

Semak terjemahan Korea dan Jepun dari direktori semasa:

```bash
co-op-review -l "ko ja"
```

Semak akar projek tertentu:

```bash
co-op-review -l "fr" -r ./my-course
```

Semak hanya README selepas terjemahan hanya README:

```bash
translate -l "ko" --readme-only -y
co-op-review -l "ko" --readme-only --format github
```

`--readme-only` mengabaikan dokumen lain dan README bersarang. Ia gagal jika `README.md` akar hilang. Digabungkan dengan `--changed-from`, ia menyemak README sahaja apabila fail sumber itu berubah. Terjemahan hanya README meninggalkan README sumber tidak berubah, termasuk mana-mana penanda bahagian dikongsi.




Semak hanya fail sumber yang berubah berbanding ref asas:

```bash
co-op-review -l "ko" --changed-from origin/main
```

Cetak keluaran Markdown bercitarasa GitHub untuk ringkasan CI:

```bash
co-op-review -l "ko ja" --changed-from origin/main --format github
```

### Pilihan

| Pilihan | Diperlukan | Penerangan |
| --- | --- | --- |
| `-l`, `--language-code` | Tidak | Kod bahasa untuk disemak. Boleh diberikan beberapa kali atau sebagai nilai yang dipisahkan oleh ruang. Lalai kepada semua bahasa terjemahan yang ditemui. |
| `-r`, `--root-dir` | Tidak | Akar projek. Lalai kepada direktori semasa. |
| `--changed-from` | Tidak | Git ref yang digunakan untuk mengehadkan semakan kepada fail sumber yang berubah. |
| `--readme-only` | Tidak | Semak hanya terjemahan `README.md` akar. |
| `--format` | Tidak | Format keluaran: `text` atau `github`. Lalai kepada `text`. |

`co-op-review` pada masa ini memeriksa fail terjemahan yang hilang, metadata terjemahan yang hilang atau lapuk, integriti frontmatter Markdown dan pagar kod, JSON notebook terjemahan yang tidak sah, dan sasaran pautan Markdown atau imej tempatan yang hilang. Pautan yang hilang adalah amaran secara lalai; masalah struktur dan kesegaran menyebabkan perintah gagal.

## co-op-translator-mcp

Jalankan pelayan Co-op Translator MCP untuk agen, penyunting, dan klien yang serasi MCP.

```bash
co-op-translator-mcp
```

Pengangkutan lalai ialah `stdio`. Lihat panduan [Pelayan MCP](mcp.md) untuk konfigurasi klien, alat, sumber, dan nota keselamatan.

### Pilihan

| Pilihan | Diperlukan | Penerangan |
| --- | --- | --- |
| `--transport` | Tidak | Pengangkutan MCP: `stdio`, `streamable-http`, atau `sse`. Lalai kepada `stdio`. |

## migrate-links

Memproses semula fail Markdown yang diterjemahkan dan mengemas kini pautan notebook supaya menunjuk kepada notebook yang diterjemahkan apabila tersedia.

```bash
migrate-links -l "ko ja"
```

### Contoh biasa

Pratonton kemas kini pautan:

```bash
migrate-links -l "ko" --dry-run
```

Proses semua bahasa yang disokong tanpa pengesahan:

```bash
migrate-links -l "all" -y
```

Tulis semula pautan hanya apabila notebook yang diterjemahkan wujud:

```bash
migrate-links -l "ko" --no-fallback-to-original
```

### Pilihan

| Pilihan | Diperlukan | Penerangan |
| --- | --- | --- |
| `-l`, `--language-codes` | Ya | Kod bahasa yang dipisahkan ruang, atau `"all"`. |
| `-r`, `--root-dir` | Tidak | Akar projek. Lalai kepada direktori semasa. |
| `--image-dir` | Tidak | Direktori imej terjemahan relatif kepada akar. Lalai kepada `translated_images`. |
| `--dry-run` | Tidak | Tunjukkan fail yang akan berubah tanpa menulis kemas kini. |
| `--fallback-to-original`, `--no-fallback-to-original` | Tidak | Gunakan pautan notebook asal apabila notebook terjemahan tiada. Diaktifkan secara lalai. |
| `-d`, `--debug` | Tidak | Aktifkan logging debug. |
| `-s`, `--save-logs` | Tidak | Simpan log peringkat DEBUG di bawah `<root-dir>/logs/`. |
| `-y`, `--yes` | Tidak | Auto-sahkan arahan apabila memproses semua bahasa. |

## Persekitaran

Apabila sesuatu perintah memerlukan kelayakan penyedia, konfigurasikan salah satu set penyedia ini. `translate --dry-run` dan `co-op-review` tidak memerlukan kelayakan penyedia:

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

# Atau Anthropic
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

Terjemahan imej juga memerlukan Azure AI Vision:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

## Susunan keluaran

Terjemahan teks ditulis di bawah:

```text
translations/<language-code>/<original-path>
```

Keluaran imej terjemahan ditulis di bawah:

```text
translated_images/<language-code>/<original-path>
```

Sebagai contoh, menterjemah `README.md` dan `docs/setup.md` ke dalam bahasa Korea menghasilkan:

```text
translations/ko/README.md
translations/ko/docs/setup.md
```

## Contoh CLI Salin-Tampal

Terjemahkan Markdown ke dalam tiga bahasa:

```bash
translate -l "ko ja fr" -md
```

Terjemahkan hanya notebook:

```bash
translate -l "zh-CN" -nb
```

Terjemahkan hanya imej:

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

Jalankan terjemahan Markdown mesra-CI:

```bash
translate -l "ko ja" -md -y -s
```

Semak keluaran terjemahan:

```bash
co-op-review -l "ko ja"
```

Pratonton migrasi pautan:

```bash
migrate-links -l "ko" --dry-run
```