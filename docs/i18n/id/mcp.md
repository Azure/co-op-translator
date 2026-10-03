# Server MCP

Co-op Translator menyertakan server Model Context Protocol untuk agen, editor, dan klien yang kompatibel dengan MCP.

Untuk pengaturan lokal default, pengguna tidak perlu menjalankan server terpisah secara manual. Mereka mengonfigurasi klien MCP mereka, dan klien akan memulai `co-op-translator-mcp` secara otomatis melalui `stdio` ketika memerlukan alat Co-op Translator.

Jika Anda sedang memilih antara CLI, Python API, dan MCP, mulailah dengan [Pilih Alur Kerja Anda](workflows.md).

Gunakan MCP ketika sebuah agen atau editor harus memanggil Co-op Translator secara langsung:

| Tujuan pengguna | Alat MCP |
| --- | --- |
| Menerjemahkan satu dokumen Markdown, notebook, atau gambar | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content` |
| Menerjemahkan konten Markdown atau notebook dengan model agen host | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Menulis ulang tautan Markdown atau notebook yang diterjemahkan setelah memilih jalur keluaran | `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Menerjemahkan seluruh repositori seperti CLI | `run_translation`, `translate_project` |
| Meninjau output terjemahan tanpa kredensial LLM | `run_review` |
| Memeriksa kemampuan dan status lingkungan | `get_api_overview`, `list_supported_languages`, `get_configuration_status` |

Server MCP membungkus API Python publik yang sama yang didokumentasikan di [Python API](api.md). Alat yang didukung penyedia menggunakan penyedia yang dikonfigurasi sama seperti CLI dan Python API. Alat yang dibantu agen menyiapkan potongan untuk diterjemahkan oleh agen host MCP, lalu menggunakan Co-op Translator untuk merekonstruksi Markdown atau notebook akhir.

## Langkah 1: Instal dan Konfigurasikan Co-op Translator

Instal Co-op Translator di lingkungan Python yang akan digunakan klien MCP Anda:

```bash
pip install co-op-translator
```

Untuk pengembangan lokal dari repositori ini, instal paket dalam mode dapat-diedit:

```bash
pip install -e .
```

Pilih mode terjemahan yang akan digunakan klien MCP Anda:

| Mode | Gunakan ini untuk | Kredensial |
| --- | --- | --- |
| Berbasis penyedia | Co-op Translator memanggil `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, atau `run_translation`. | Terjemahan membutuhkan Azure OpenAI, OpenAI, atau Anthropic. Terjemahan gambar juga membutuhkan Azure AI Vision. |
| Dibantu agen | Agen host MCP menerjemahkan potongan yang dikembalikan oleh `start_markdown_agent_translation` atau `start_notebook_agent_translation`. | Tidak diperlukan kredensial penyedia LLM Co-op Translator untuk potongan Markdown atau notebook. Terjemahan gambar belum dibahas oleh mode dibantu agen. |

Jika Anda memulai dengan terjemahan Markdown atau notebook di dalam agen seperti Codex atau Claude Code, mulailah dengan mode dibantu agen. Gunakan mode berbasis penyedia ketika Anda ingin Co-op Translator sendiri memanggil penyedia yang dikonfigurasi, ketika Anda menerjemahkan gambar, atau ketika Anda menjalankan terjemahan tingkat repositori seperti CLI.

Konfigurasikan satu penyedia untuk alur kerja berbasis penyedia:

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

Terjemahan gambar berbasis penyedia juga membutuhkan:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

!!! note
    Mode dibantu agen saat ini mencakup Markdown dan sel Markdown pada notebook. Terjemahan gambar masih menggunakan pipeline gambar berbasis penyedia dan membutuhkan Azure AI Vision untuk OCR dan rendering yang peka tata letak.

## Langkah 2: Konfigurasikan Klien MCP Anda

Untuk pengaturan lokal `stdio` biasa, tambahkan Co-op Translator ke konfigurasi klien MCP Anda. Klien akan memulai dan menghentikan proses secara otomatis.

Konfigurasi paket terinstal:

```json
{
  "mcpServers": {
    "co-op-translator": {
      "command": "co-op-translator-mcp",
      "args": []
    }
  }
}
```

Konfigurasi checkout sumber di Windows:

```json
{
  "mcpServers": {
    "co-op-translator": {
      "command": "C:\\Users\\you\\dev\\co-op-translator\\.venv\\Scripts\\python.exe",
      "args": ["-m", "co_op_translator.mcp.server"],
      "cwd": "C:\\Users\\you\\dev\\co-op-translator"
    }
  }
}
```

Konfigurasi checkout sumber di macOS atau Linux:

```json
{
  "mcpServers": {
    "co-op-translator": {
      "command": "/Users/you/dev/co-op-translator/.venv/bin/python",
      "args": ["-m", "co_op_translator.mcp.server"],
      "cwd": "/Users/you/dev/co-op-translator"
    }
  }
}
```

Setelah mengubah konfigurasi klien MCP, mulai ulang atau muat ulang klien agar dapat menemukan server baru.

## Langkah 3: Verifikasi Server di Klien

Minta klien MCP untuk menampilkan daftar alat yang tersedia, atau panggil salah satu helper hanya-baca terlebih dahulu:

```json
{
  "tool": "get_api_overview",
  "arguments": {}
}
```

Pemeriksaan awal yang berguna:

| Alat | Yang perlu diperiksa |
| --- | --- |
| `get_api_overview` | Mengonfirmasi server dapat dijangkau dan menampilkan alur kerja yang tersedia. |
| `list_supported_languages` | Mengonfirmasi data bahasa yang dikemas dapat dimuat. |
| `get_configuration_status` | Mengonfirmasi ketersediaan penyedia LLM dan Vision tanpa mengekspos nilai rahasia. |

## Langkah 4: Pilih Alur Kerja

### Menerjemahkan File atau Dokumen Individu

Gunakan alat konten berbasis penyedia ketika klien MCP sudah memiliki konten dokumen atau jalur gambar dan Co-op Translator harus memanggil penyedia terjemahan yang dikonfigurasikan.

Untuk Markdown:

1. Panggil `translate_markdown_content` dengan `document`, `language_code`, dan opsional `source_path`.
2. Jika hasil terjemahan akan ditulis ke tata letak keluaran Co-op Translator, panggil `rewrite_markdown_paths`.
3. Biarkan klien menulis atau mengembalikan `content` akhir.

Untuk notebook:

1. Panggil `translate_notebook_content` dengan JSON notebook dan `language_code`.
2. Panggil `rewrite_notebook_paths` jika tautan notebook yang diterjemahkan perlu disesuaikan untuk jalur target.
3. Tulis atau kembalikan JSON notebook akhir.

Untuk gambar:

1. Panggil `translate_image_content` dengan `image_path`, `language_code`, dan opsional `root_dir` atau `fast_mode`.
2. Baca `data_base64` dan `mime_type` yang dikembalikan.
3. Jika `output_path` disediakan, gambar yang diterjemahkan juga disimpan ke jalur itu.

Alat konten tidak melakukan penemuan proyek, pembaruan metadata, disclaimer, atau penulisan ulang jalur otomatis. Jika Anda ingin agen host menerjemahkan potongan Markdown atau notebook tanpa kredensial penyedia LLM Co-op Translator, gunakan alur kerja dibantu agen di bawah.

### Menerjemahkan dengan Model Agen Host

Gunakan alat dibantu agen ketika Anda ingin agen host MCP, seperti asisten pengkodean, menghasilkan teks terjemahan daripada mengonfigurasi penyedia LLM untuk Co-op Translator.

Dalam klien MCP berbasis obrolan, biasanya Anda tidak perlu menulis JSON alat sendiri. Minta agen untuk menggunakan alur kerja dibantu agen:

```text
Translate this Markdown file to Korean with Co-op Translator MCP.
Use agent-assisted mode: call start_markdown_agent_translation, translate the returned chunks with your own model, then call finish_markdown_agent_translation.
Keep Markdown formatting, code blocks, and links intact.
```

Untuk notebook, gunakan pola yang sama:

```text
Translate this notebook to Korean with Co-op Translator MCP.
Use start_notebook_agent_translation, translate the returned Markdown-cell chunks with your own model, then call finish_notebook_agent_translation.
Preserve code cells, outputs, and notebook metadata.
```

Jika klien MCP Anda mendukung server prompts, gunakan `agent_assisted_markdown_translation_prompt` agar klien memuat instruksi alur kerja yang sama.

Untuk Markdown:

1. Panggil `start_markdown_agent_translation` dengan `document`, `language_code`, dan opsional `source_path`.
2. Terjemahkan setiap potongan yang dikembalikan dalam agen host dengan mengikuti `prompt` potongan tersebut.
3. Panggil `finish_markdown_agent_translation` dengan `job` asli dan potongan yang diterjemahkan menggunakan `chunk_id` dan `translated_text`.
4. Jika konten akan ditulis ke jalur target yang diterjemahkan, panggil `rewrite_markdown_paths`.

Untuk notebook:

1. Panggil `start_notebook_agent_translation` dengan JSON notebook dan `language_code`.
2. Terjemahkan setiap potongan yang dikembalikan di agen host.
3. Panggil `finish_notebook_agent_translation` dengan `job` asli dan potongan yang diterjemahkan.
4. Panggil `rewrite_notebook_paths` jika tautan notebook yang diterjemahkan perlu penyesuaian jalur target.

Alat dibantu agen tidak memanggil penyedia LLM yang dikonfigurasi dari Co-op Translator. Agen host bertanggung jawab untuk menerjemahkan potongan yang dikembalikan. Co-op Translator menangani pemecahan Markdown menjadi potongan, pelestarian placeholder, rekonstruksi frontmatter, penggantian sel notebook, dan normalisasi pasca-terjemahan.

### Menerjemahkan Seluruh Repositori

Gunakan `run_translation` ketika pengguna ingin Co-op Translator berperilaku seperti CLI `translate`.

Terjemahan repositori default ke `dry_run=true` sehingga agen dapat memeriksa cakupan sebelum perubahan file:

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "dry_run": true
}
```

Hasil `run_translation` menyertakan array `events` dengan event progres berversi
`co-op.translation.event.v1`. Klien MCP harus menggunakan field-field seperti
`type`, `stage_key`, `completed`, `total`, dan `current_path` daripada
mengurai teks konsol yang ditangkap. Berikan `json_events_path` untuk juga menulis event-event tersebut
ke file NDJSON.

Untuk mengizinkan penulisan, pemanggil harus mengatur `dry_run=false` dan `confirm_write=true`:

```json
{
  "language_codes": "ko",
  "root_dir": ".",
  "markdown": true,
  "dry_run": false,
  "confirm_write": true
}
```

`translate_project` diekspos sebagai alias kompatibilitas untuk `run_translation`.

### Tinjau Output Terjemahan

Gunakan `run_review` untuk pemeriksaan deterministik yang tidak memerlukan kredensial LLM atau Vision:

!!! note "Beta"
    MCP mengekspos API beta `run_review`. Aman untuk alur kerja peninjauan hanya-baca, tetapi pemeriksaan peninjauan dan skema masalah dapat berkembang.

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "notebook": true
}
```

Hasilnya mencakup keluaran teks yang ditangkap dan ringkasan tinjauan terstruktur jika tersedia.

## Menjalankan Server secara Manual

Penjalankan manual terutama untuk debugging atau untuk transport yang berperilaku seperti server jangka panjang.

Debug server stdio default:

```bash
co-op-translator-mcp
```

Jalankan dari checkout sumber:

```bash
python -m co_op_translator.mcp.server
```

Jalankan server HTTP atau SSE jangka panjang:

```bash
co-op-translator-mcp --transport streamable-http
co-op-translator-mcp --transport sse
```

Untuk integrasi editor dan agen lokal, utamakan konfigurasi `stdio` yang dikelola klien pada Langkah 2.

## Alat

| Alat | Tujuan | Menulis file |
| --- | --- | --- |
| `translate_markdown_content` | Menerjemahkan string Markdown. | Tidak |
| `translate_notebook_content` | Menerjemahkan sel Markdown dalam JSON notebook. | Tidak |
| `translate_image_content` | Menerjemahkan teks dalam satu gambar dan mengembalikan data gambar base64. | Opsional, hanya ketika `output_path` disediakan |
| `start_markdown_agent_translation` | Menyiapkan potongan Markdown untuk diterjemahkan oleh agen host tanpa kredensial LLM Co-op Translator. | Tidak |
| `finish_markdown_agent_translation` | Merekonstruksi Markdown dari potongan yang diterjemahkan oleh agen host. | Tidak |
| `start_notebook_agent_translation` | Menyiapkan potongan sel Markdown notebook untuk diterjemahkan oleh agen host. | Tidak |
| `finish_notebook_agent_translation` | Merekonstruksi JSON notebook dari potongan yang diterjemahkan oleh agen host. | Tidak |
| `rewrite_markdown_paths` | Menulis ulang jalur badan Markdown dan frontmatter untuk target yang diterjemahkan. | Tidak |
| `rewrite_notebook_paths` | Menulis ulang jalur di dalam sel Markdown notebook. | Tidak |
| `run_translation` | Menjalankan terjemahan tingkat proyek seperti CLI. | Ya ketika `dry_run=false` dan `confirm_write=true` |
| `translate_project` | Alias kompatibilitas untuk `run_translation`. | Ya ketika `dry_run=false` dan `confirm_write=true` |
| `run_review` | Menjalankan pemeriksaan tinjauan deterministik. | Tidak |
| `get_configuration_status` | Melaporkan penyedia LLM dan Vision yang dikonfigurasi tanpa mengekspos rahasia. | Tidak |
| `list_supported_languages` | Mendaftar kode bahasa target yang didukung. | Tidak |
| `get_api_overview` | Menjabarkan alur kerja dan alat MCP yang tersedia. | Tidak |

## Sumber Daya

| URI Sumber Daya | Tujuan |
| --- | --- |
| `co-op://api` | Gambaran JSON tentang alur kerja dan alat. |
| `co-op://supported-languages` | Daftar JSON kode bahasa yang didukung. |
| `co-op://configuration` | Ringkasan ketersediaan penyedia dalam JSON tanpa menyertakan rahasia. |

## Prompt

| Prompt | Tujuan |
| --- | --- |
| `translate_markdown_document_prompt` | Memandu klien MCP melalui terjemahan konten plus penulisan ulang jalur opsional. |
| `agent_assisted_markdown_translation_prompt` | Memandu klien MCP melalui terjemahan Markdown oleh agen host tanpa kredensial penyedia LLM Co-op Translator. |
| `translate_repository_prompt` | Memandu klien MCP melalui terjemahan repositori yang memulai dengan dry-run. |

## Contoh Salin-Tempel

Terjemahkan konten Markdown:

```json
{
  "tool": "translate_markdown_content",
  "arguments": {
    "document": "# Hello\n\nWelcome to the course.",
    "language_code": "ko",
    "source_path": "docs/guide.md"
  }
}
```

Tulis ulang tautan Markdown yang diterjemahkan:

```json
{
  "tool": "rewrite_markdown_paths",
  "arguments": {
    "content": "[Setup](../setup.md)\n\n![Hero](images/hero.png)",
    "source_path": "docs/guide.md",
    "target_path": "translations/ko/docs/guide.md",
    "policy": {
      "language_code": "ko",
      "root_dir": ".",
      "translations_dir": "translations",
      "translated_images_dir": "translated_images",
      "translation_types": ["markdown", "images"]
    }
  }
}
```

Terjemahkan Markdown dengan model agen host:

```json
{
  "tool": "start_markdown_agent_translation",
  "arguments": {
    "document": "# Hello\n\nUse `pip install` to get started.",
    "language_code": "ko",
    "source_path": "docs/guide.md"
  }
}
```

Setelah agen host menerjemahkan setiap potongan yang dikembalikan, selesaikan pekerjaan dengan objek `job` lengkap yang dikembalikan oleh `start_markdown_agent_translation`:

```text
tool: finish_markdown_agent_translation
arguments:
  job: <the full job object returned by start_markdown_agent_translation>
  translated_chunks:
    - chunk_id: body:1
      translated_text: "# 안녕하세요\n\n시작하려면 `pip install`을 사용하세요."
```

Pratinjau terjemahan repositori:

```json
{
  "tool": "run_translation",
  "arguments": {
    "language_codes": "ko",
    "root_dir": ".",
    "markdown": true,
    "dry_run": true
  }
}
```

## Pemecahan Masalah

| Masalah | Yang bisa dicoba |
| --- | --- |
| Klien MCP tidak dapat menemukan `co-op-translator-mcp`. | Gunakan path eksekutabel Python absolut dan konfigurasi checkout sumber `["-m", "co_op_translator.mcp.server"]`. |
| Server terdaftar tetapi terjemahan gagal. | Panggil `get_configuration_status` dan konfirmasi bahwa penyedia LLM tersedia. |
| Anda ingin terjemahan Markdown atau notebook tanpa kredensial penyedia. | Gunakan `start_markdown_agent_translation` / `finish_markdown_agent_translation` atau ekivalen pada notebook sehingga agen host menerjemahkan potongan-potongan tersebut. |
| Terjemahan gambar gagal. | Konfirmasi variabel Azure AI Vision telah disetel dan panggil `get_configuration_status`. |
| Terjemahan repositori tidak menulis file. | Atur `dry_run=false` dan `confirm_write=true` hanya setelah persetujuan pengguna yang eksplisit. |
| Perubahan pada konfigurasi klien tidak muncul. | Mulai ulang atau muat ulang klien MCP. |

## Catatan Keamanan

- Panggilan alat MCP dikendalikan model oleh aplikasi host, jadi terjemahan repositori bersifat dry-run secara default.
- Terjemahan repositori penuh dapat membuat, memperbarui, atau menghapus banyak file. Minta persetujuan pengguna yang eksplisit sebelum mengatur `confirm_write=true`.
- Alat status konfigurasi tidak pernah mengembalikan kunci API, endpoint, atau nilai rahasia lainnya.
- Terjemahan gambar mengembalikan data gambar base64. Gambar besar dapat menghasilkan respons alat yang besar.
- Alat dibantu agen mengembalikan potongan sumber dan prompt ke host MCP. Gunakan hanya dengan konten yang pengguna merasa nyaman mengirimkan ke model agen host tersebut.