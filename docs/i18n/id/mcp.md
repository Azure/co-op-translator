# Server MCP

Co-op Translator menyertakan server Model Context Protocol untuk agen, editor, dan klien yang kompatibel dengan MCP.

Untuk pengaturan lokal bawaan, pengguna tidak perlu menjalankan server terpisah secara manual. Mereka mengonfigurasi klien MCP mereka, dan klien akan memulai `co-op-translator-mcp` secara otomatis melalui `stdio` ketika memerlukan alat Co-op Translator.

Jika Anda sedang memutuskan antara CLI, Python API, dan MCP, mulai dengan [Pilih Alur Kerja](workflows.md).

Gunakan MCP ketika sebuah agen atau editor harus memanggil Co-op Translator secara langsung:

| Tujuan pengguna | Alat MCP |
| --- | --- |
| Menerjemahkan satu dokumen Markdown, notebook, atau gambar | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content` |
| Menerjemahkan konten Markdown atau notebook dengan model agen host | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Menulis ulang tautan Markdown atau notebook yang diterjemahkan setelah memilih jalur keluaran | `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Menerjemahkan seluruh repositori seperti CLI | `run_translation`, `translate_project` |
| Meninjau output terjemahan tanpa kredensial LLM | `run_review` |
| Memeriksa kemampuan dan status lingkungan | `get_api_overview`, `list_supported_languages`, `get_configuration_status` |

Server MCP membungkus API publik Python yang sama yang didokumentasikan di [Python API](api.md). Alat berbasis provider menggunakan provider yang sama yang dikonfigurasi untuk CLI dan Python API. Alat berbasis agen menyiapkan potongan untuk agen host MCP agar diterjemahkan, lalu menggunakan Co-op Translator untuk merekonstruksi Markdown atau notebook akhir.

## Langkah 1: Instal dan Konfigurasikan Co-op Translator

Instal Co-op Translator di lingkungan Python yang akan digunakan oleh klien MCP Anda:

```bash
pip install co-op-translator
```

Untuk pengembangan lokal dari repositori ini, instal paket dalam mode editable:

```bash
pip install -e .
```

Pilih mode terjemahan yang akan digunakan oleh klien MCP Anda:

| Mode | Gunakan ini untuk | Kredensial |
| --- | --- | --- |
| Provider-backed | Co-op Translator memanggil `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, atau `run_translation`. | Terjemahan Markdown dan notebook memerlukan Azure OpenAI atau OpenAI. Terjemahan gambar juga memerlukan Azure AI Vision. |
| Agent-assisted | Agen host MCP menerjemahkan potongan yang dikembalikan oleh `start_markdown_agent_translation` atau `start_notebook_agent_translation`. | Tidak diperlukan kredensial penyedia LLM Co-op Translator untuk potongan Markdown atau notebook. Terjemahan gambar belum tercakup oleh mode agent-assisted. |

Jika Anda memulai dengan terjemahan Markdown atau notebook di dalam agen seperti Codex atau Claude Code, mulai dengan mode agent-assisted. Gunakan mode provider-backed ketika Anda ingin Co-op Translator itu sendiri memanggil provider yang telah Anda konfigurasi, ketika Anda menerjemahkan gambar, atau ketika Anda menjalankan terjemahan tingkat repositori seperti CLI.

Konfigurasikan kredensial provider hanya untuk alur kerja provider-backed:

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Terjemahan gambar berbasis provider juga membutuhkan:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

!!! note
    Mode agent-assisted saat ini mencakup sel Markdown di Markdown dan notebook. Terjemahan gambar masih menggunakan pipeline gambar berbasis provider dan memerlukan Azure AI Vision untuk OCR dan rendering yang menyadari tata letak.

## Langkah 2: Konfigurasikan Klien MCP Anda

Untuk pengaturan `stdio` lokal normal, tambahkan Co-op Translator ke konfigurasi klien MCP Anda. Klien akan memulai dan menghentikan proses secara otomatis.

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

Konfigurasi source checkout di Windows:

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

Konfigurasi source checkout di macOS atau Linux:

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

Minta klien MCP untuk mencantumkan alat yang tersedia, atau panggil salah satu pembantu hanya-baca terlebih dahulu:

```json
{
  "tool": "get_api_overview",
  "arguments": {}
}
```

Pemeriksaan awal yang berguna:

| Alat | Yang diperiksa |
| --- | --- |
| `get_api_overview` | Mengonfirmasi server dapat dijangkau dan menunjukkan alur kerja yang tersedia. |
| `list_supported_languages` | Mengonfirmasi data bahasa yang dipaketkan dapat dimuat. |
| `get_configuration_status` | Mengonfirmasi ketersediaan provider LLM dan Vision tanpa mengekspos nilai rahasia. |

## Langkah 4: Pilih Alur Kerja

### Menerjemahkan File atau Dokumen Individu

Gunakan alat konten berbasis provider ketika klien MCP sudah memiliki konten dokumen atau jalur gambar dan Co-op Translator harus memanggil provider terjemahan yang dikonfigurasi.

Untuk Markdown:

1. Panggil `translate_markdown_content` dengan `document`, `language_code`, dan opsional `source_path`.
2. Jika hasil terjemahan akan ditulis ke layout keluaran Co-op Translator, panggil `rewrite_markdown_paths`.
3. Biarkan klien menulis atau mengembalikan `content` akhir.

Untuk notebook:

1. Panggil `translate_notebook_content` dengan JSON notebook dan `language_code`.
2. Panggil `rewrite_notebook_paths` jika tautan notebook yang diterjemahkan perlu disesuaikan untuk jalur target.
3. Tulis atau kembalikan JSON notebook akhir.

Untuk gambar:

1. Panggil `translate_image_content` dengan `image_path`, `language_code`, dan opsional `root_dir` atau `fast_mode`.
2. Baca `data_base64` dan `mime_type` yang dikembalikan.
3. Jika `output_path` disediakan, gambar yang diterjemahkan juga disimpan ke jalur tersebut.

Alat konten tidak melakukan penemuan proyek, pembaruan metadata, penyangkalan, atau penulisan ulang jalur otomatis. Jika Anda ingin agen host menerjemahkan potongan Markdown atau notebook tanpa kredensial provider LLM Co-op Translator, gunakan alur kerja agent-assisted di bawah.

### Menerjemahkan dengan Model Agen Host

Gunakan alat agent-assisted ketika Anda ingin agen host MCP, seperti asisten pengkodean, menghasilkan teks terjemahan alih-alih mengonfigurasi Azure OpenAI atau OpenAI untuk Co-op Translator.

Dalam klien MCP berbasis chat, biasanya Anda tidak perlu menulis JSON alat sendiri. Minta agen untuk menggunakan alur kerja agent-assisted:

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

Jika klien MCP Anda mendukung server prompt, gunakan `agent_assisted_markdown_translation_prompt` agar klien memuat instruksi alur kerja yang sama.

Untuk Markdown:

1. Panggil `start_markdown_agent_translation` dengan `document`, `language_code`, dan opsional `source_path`.
2. Terjemahkan setiap potongan yang dikembalikan di agen host dengan mengikuti `prompt` potongan tersebut.
3. Panggil `finish_markdown_agent_translation` dengan `job` asli dan potongan yang diterjemahkan menggunakan `chunk_id` dan `translated_text`.
4. Jika konten akan ditulis ke jalur target terjemahan, panggil `rewrite_markdown_paths`.

Untuk notebook:

1. Panggil `start_notebook_agent_translation` dengan JSON notebook dan `language_code`.
2. Terjemahkan setiap potongan yang dikembalikan di agen host.
3. Panggil `finish_notebook_agent_translation` dengan `job` asli dan potongan yang diterjemahkan.
4. Panggil `rewrite_notebook_paths` jika tautan notebook yang diterjemahkan perlu penyesuaian jalur target.

Alat agent-assisted tidak memanggil Azure OpenAI atau OpenAI dari Co-op Translator. Agen host bertanggung jawab untuk menerjemahkan potongan yang dikembalikan. Co-op Translator menangani pemotongan Markdown, pelestarian placeholder, rekonstruksi frontmatter, penggantian sel notebook, dan normalisasi pasca-terjemahan.

### Menerjemahkan Seluruh Repositori

Gunakan `run_translation` ketika pengguna ingin Co-op Translator berperilaku seperti CLI `translate`.

Terjemahan repositori defaultnya adalah `dry_run=true` sehingga agen dapat memeriksa cakupan sebelum perubahan file:

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "dry_run": true
}
```

Untuk mengizinkan penulisan, pemanggil harus mengatur kedua `dry_run=false` dan `confirm_write=true`:

```json
{
  "language_codes": "ko",
  "root_dir": ".",
  "markdown": true,
  "dry_run": false,
  "confirm_write": true
}
```

`translate_project` dipublikasikan sebagai alias kompatibilitas untuk `run_translation`.

### Meninjau Hasil Terjemahan

Gunakan `run_review` untuk pemeriksaan deterministik yang tidak memerlukan kredensial LLM atau Vision:

!!! note "Beta"
    MCP mengekspos API beta `run_review`. Ini aman untuk alur kerja peninjauan hanya-baca, tetapi pemeriksaan peninjauan dan skema masalah dapat berkembang.

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "notebook": true
}
```

Hasilnya mencakup keluaran teks yang ditangkap dan ringkasan peninjauan terstruktur saat tersedia.

## Menjalankan Server Secara Manual

Penjalankan manual terutama untuk debugging atau untuk transport yang berperilaku seperti server jangka panjang.

Debug server stdio bawaan:

```bash
co-op-translator-mcp
```

Jalankan dari source checkout:

```bash
python -m co_op_translator.mcp.server
```

Jalankan server HTTP atau SSE yang berumur panjang:

```bash
co-op-translator-mcp --transport streamable-http
co-op-translator-mcp --transport sse
```

Untuk integrasi editor lokal dan agen, lebih disarankan konfigurasi `stdio` yang dikelola klien pada Langkah 2.

## Alat

| Alat | Tujuan | Menulis file |
| --- | --- | --- |
| `translate_markdown_content` | Menerjemahkan string Markdown. | Tidak |
| `translate_notebook_content` | Menerjemahkan sel Markdown dalam JSON notebook. | Tidak |
| `translate_image_content` | Menerjemahkan teks dalam satu gambar dan mengembalikan data gambar base64. | Opsional, hanya ketika `output_path` disediakan |
| `start_markdown_agent_translation` | Menyiapkan potongan Markdown agar agen host menerjemahkan tanpa kredensial LLM Co-op Translator. | Tidak |
| `finish_markdown_agent_translation` | Merekonstruksi Markdown dari potongan yang diterjemahkan oleh agen host. | Tidak |
| `start_notebook_agent_translation` | Menyiapkan potongan sel Markdown notebook agar agen host menerjemahkan. | Tidak |
| `finish_notebook_agent_translation` | Merekonstruksi JSON notebook dari potongan yang diterjemahkan oleh agen host. | Tidak |
| `rewrite_markdown_paths` | Menulis ulang jalur badan Markdown dan frontmatter untuk target terjemahan. | Tidak |
| `rewrite_notebook_paths` | Menulis ulang jalur di dalam sel Markdown notebook. | Tidak |
| `run_translation` | Menjalankan terjemahan tingkat proyek seperti CLI. | Ya ketika `dry_run=false` dan `confirm_write=true` |
| `translate_project` | Alias kompatibilitas untuk `run_translation`. | Ya ketika `dry_run=false` dan `confirm_write=true` |
| `run_review` | Menjalankan pemeriksaan peninjauan deterministik. | Tidak |
| `get_configuration_status` | Melaporkan provider LLM dan Vision yang dikonfigurasi tanpa mengekspos rahasia. | Tidak |
| `list_supported_languages` | Mencantumkan kode bahasa target yang didukung. | Tidak |
| `get_api_overview` | Menjelaskan alur kerja MCP dan alat yang tersedia. | Tidak |

## Sumber Daya

| Resource URI | Tujuan |
| --- | --- |
| `co-op://api` | Ikhtisar JSON tentang alur kerja dan alat. |
| `co-op://supported-languages` | Daftar JSON kode bahasa yang didukung. |
| `co-op://configuration` | Ringkasan ketersediaan provider dalam JSON tanpa rahasia. |

## Prompt

| Prompt | Tujuan |
| --- | --- |
| `translate_markdown_document_prompt` | Membimbing klien MCP melalui terjemahan konten ditambah penulisan ulang jalur opsional. |
| `agent_assisted_markdown_translation_prompt` | Membimbing klien MCP melalui terjemahan Markdown oleh agen host tanpa kredensial provider LLM Co-op Translator. |
| `translate_repository_prompt` | Membimbing klien MCP melalui terjemahan repositori yang memulai dengan dry-run. |

## Contoh Salin-Tempel

Menerjemahkan konten Markdown:

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

Menulis ulang tautan Markdown yang diterjemahkan:

```json
{
  "tool": "rewrite_markdown_paths",
  "arguments": {
    "content": "[Setup](../setup.md)\n\n![Hero](../../images/hero.png)",
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

Menerjemahkan Markdown dengan model agen host:

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

| Masalah | Yang dicoba |
| --- | --- |
| Klien MCP tidak dapat menemukan `co-op-translator-mcp`. | Gunakan path eksekutabel Python absolut dan konfigurasi source checkout `["-m", "co_op_translator.mcp.server"]`. |
| Server terdaftar tetapi terjemahan gagal. | Panggil `get_configuration_status` dan konfirmasikan provider LLM tersedia. |
| Anda ingin terjemahan Markdown atau notebook tanpa kunci Azure OpenAI/OpenAI. | Gunakan `start_markdown_agent_translation` / `finish_markdown_agent_translation` atau padanan notebook sehingga agen host menerjemahkan potongan. |
| Terjemahan gambar gagal. | Konfirmasikan variabel Azure AI Vision disetel dan panggil `get_configuration_status`. |
| Terjemahan repositori tidak menulis file. | Atur `dry_run=false` dan `confirm_write=true` hanya setelah persetujuan eksplisit dari pengguna. |
| Perubahan pada konfigurasi klien tidak muncul. | Mulai ulang atau muat ulang klien MCP. |

## Catatan Keamanan

- Panggilan alat MCP dikendalikan model oleh aplikasi host, sehingga terjemahan repositori bersifat dry-run secara default.
- Terjemahan repositori penuh dapat membuat, memperbarui, atau menghapus banyak file. Meminta persetujuan eksplisit pengguna sebelum mengatur `confirm_write=true`.
- Alat status konfigurasi tidak pernah mengembalikan kunci API, endpoint, atau nilai rahasia lainnya.
- Terjemahan gambar mengembalikan data gambar base64. Gambar besar dapat menghasilkan respons alat yang besar.
- Alat agent-assisted mengembalikan potongan sumber dan prompt ke host MCP. Gunakan hanya dengan konten yang pengguna merasa nyaman untuk dikirim ke model agen host tersebut.