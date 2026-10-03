# Pelayan MCP

Co-op Translator termasuk pelayan Model Context Protocol untuk ejen, penyunting, dan klien yang serasi dengan MCP.

Untuk konfigurasi tempatan lalai, pengguna tidak menjalankan pelayan berasingan secara manual. Mereka mengkonfigurasi pelanggan MCP mereka, dan pelanggan itu memulakan `co-op-translator-mcp` secara automatik melalui `stdio` apabila ia memerlukan Co-op Translator.

Jika anda sedang membuat keputusan antara CLI, Python API, dan MCP, mulakan dengan [Pilih Aliran Kerja Anda](workflows.md).

Gunakan MCP apabila ejen atau penyunting perlu memanggil Co-op Translator secara langsung:

| Matlamat pengguna | MCP tools |
| --- | --- |
| Menterjemah satu dokumen Markdown, notebook, atau imej | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content` |
| Menterjemah kandungan Markdown atau notebook dengan model ejen hos | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Menulis semula pautan Markdown atau notebook yang diterjemah selepas memilih laluan output | `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Menterjemah keseluruhan repositori seperti CLI | `run_translation`, `translate_project` |
| Mengkaji output yang diterjemah tanpa kelayakan LLM | `run_review` |
| Memeriksa kemampuan dan status persekitaran | `get_api_overview`, `list_supported_languages`, `get_configuration_status` |

Pelayan MCP membalut API Python awam yang sama yang didokumentasikan dalam [Python API](api.md). Alat yang disokong penyedia menggunakan penyedia yang sama yang dikonfigurasikan seperti CLI dan Python API. Alat berbantukan ejen menyediakan kepingan untuk diterjemahkan oleh ejen hos MCP, kemudian menggunakan Co-op Translator untuk menyusun semula Markdown atau buku nota akhir.

## Langkah 1: Pasang dan Konfigurasikan Co-op Translator

Pasang Co-op Translator dalam persekitaran Python yang akan digunakan oleh klien MCP anda:

```bash
pip install co-op-translator
```

Untuk pembangunan tempatan daripada repositori ini, pasang pakej dalam mod boleh sunting:

```bash
pip install -e .
```

Pilih mod terjemahan yang akan digunakan oleh klien MCP anda:

| Mode | Digunakan untuk | Kelayakan |
| --- | --- | --- |
| Provider-backed | Co-op Translator calls `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, or `run_translation`. | Terjemahan memerlukan Azure OpenAI, OpenAI, atau Anthropic. Terjemahan imej juga memerlukan Azure AI Vision. |
| Agent-assisted | Ejen hos MCP menterjemah kepingan yang dikembalikan oleh `start_markdown_agent_translation` atau `start_notebook_agent_translation`. | Tiada kredensial penyedia LLM Co-op Translator diperlukan untuk kepingan Markdown atau buku nota. Terjemahan imej belum diliputi oleh mod berbantukan ejen. |

Jika anda memulakan dengan terjemahan Markdown atau buku nota di dalam ejen seperti Codex atau Claude Code, mulakan dengan mod berbantukan ejen. Gunakan mod disokong-penyedia apabila anda mahu Co-op Translator itu sendiri memanggil penyedia yang telah anda konfigurasikan, apabila anda menterjemah imej, atau apabila anda menjalankan terjemahan peringkat repositori seperti CLI.

Konfigurasikan satu penyedia untuk aliran kerja yang disokong oleh penyedia:

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

Terjemahan imej berasaskan penyedia juga memerlukan:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

!!! note
    Mod berbantukan ejen kini merangkumi Markdown dan sel Markdown buku nota. Terjemahan imej masih menggunakan saluran imej disokong-penyedia dan memerlukan Azure AI Vision untuk OCR dan render yang peka kepada susun atur.

## Langkah 2: Konfigurasikan Klien MCP Anda

Untuk tetapan `stdio` tempatan biasa, tambah Co-op Translator ke konfigurasi klien MCP anda. Klien akan memulakan dan menghentikan proses secara automatik.

Konfigurasi pakej yang dipasang:

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

Source checkout configuration on Windows:

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

Konfigurasi checkout sumber pada macOS atau Linux:

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

Selepas menukar konfigurasi klien MCP, mulakan semula atau muat semula klien supaya ia boleh mengesan pelayan baru.

## Langkah 3: Sahkan Pelayan dalam Klien

Minta klien MCP menyenaraikan alat yang tersedia, atau panggil salah satu pembantu baca sahaja terlebih dahulu:

```json
{
  "tool": "get_api_overview",
  "arguments": {}
}
```

Semakan pertama yang berguna:

| Alat | Apa yang diperiksa |
| --- | --- |
| `get_api_overview` | Mengesahkan pelayan boleh dicapai dan menunjukkan aliran kerja yang tersedia. |
| `list_supported_languages` | Mengesahkan data bahasa yang dibungkus boleh dimuat. |
| `get_configuration_status` | Mengesahkan ketersediaan pembekal LLM dan Vision tanpa mendedahkan nilai rahsia. |

## Langkah 4: Pilih Aliran Kerja

### Menterjemah Fail atau Dokumen Individu

Gunakan alat kandungan disokong penyedia apabila klien MCP sudah mempunyai kandungan dokumen atau laluan imej dan Co-op Translator harus memanggil penyedia terjemahan yang dikonfigurasi.

Untuk Markdown:

1. Panggil `translate_markdown_content` dengan `document`, `language_code`, dan pilihan `source_path`.
2. Jika hasil terjemahan akan ditulis ke dalam susun atur output Co-op Translator, panggil `rewrite_markdown_paths`.
3. Biarkan klien menulis atau mengembalikan `content` akhir.

Untuk notebook:

1. Panggil `translate_notebook_content` dengan JSON notebook dan `language_code`.
2. Panggil `rewrite_notebook_paths` jika pautan notebook yang diterjemah perlu dilaraskan untuk laluan sasaran.
3. Tulis atau kembalikan JSON notebook akhir.

Untuk imej:

1. Panggil `translate_image_content` dengan `image_path`, `language_code`, dan pilihan `root_dir` atau `fast_mode`.
2. Baca `data_base64` dan `mime_type` yang dikembalikan.
3. Jika `output_path` disediakan, imej yang diterjemah juga disimpan ke laluan itu.

Alat kandungan tidak melakukan penemuan projek, kemas kini metadata, penafian, atau penulisan semula jalan secara automatik. Jika anda mahu ejen hos menterjemah kepingan Markdown atau buku nota tanpa kredensial penyedia LLM Co-op Translator, gunakan aliran kerja berbantukan ejen di bawah.

### Terjemah dengan Model Ejen Hos

Gunakan alat dibantu-ejen apabila anda mahu ejen hos MCP, seperti pembantu pengekodan, menghasilkan teks yang diterjemah dan bukannya mengkonfigurasi pembekal LLM untuk Co-op Translator.

Dalam klien MCP berasaskan sembang, anda biasanya tidak perlu menulis JSON alat sendiri. Minta ejen menggunakan aliran kerja dibantu-ejen:

```text
Translate this Markdown file to Korean with Co-op Translator MCP.
Use agent-assisted mode: call start_markdown_agent_translation, translate the returned chunks with your own model, then call finish_markdown_agent_translation.
Keep Markdown formatting, code blocks, and links intact.
```

Untuk notebook, gunakan corak yang sama:

```text
Translate this notebook to Korean with Co-op Translator MCP.
Use start_notebook_agent_translation, translate the returned Markdown-cell chunks with your own model, then call finish_notebook_agent_translation.
Preserve code cells, outputs, and notebook metadata.
```

Jika pelanggan MCP anda menyokong prompt pelayan, gunakan `agent_assisted_markdown_translation_prompt` untuk membolehkan pelanggan memuat arahan aliran kerja yang sama.

Untuk Markdown:

1. Panggil `start_markdown_agent_translation` dengan `document`, `language_code`, dan pilihan `source_path`.
2. Terjemah setiap serpihan yang dikembalikan dalam ejen hos dengan mengikuti `prompt` serpihan.
3. Panggil `finish_markdown_agent_translation` dengan `job` asal dan serpihan yang diterjemah menggunakan `chunk_id` dan `translated_text`.
4. Jika kandungan akan ditulis ke laluan sasaran yang diterjemah, panggil `rewrite_markdown_paths`.

Untuk notebook:

1. Panggil `start_notebook_agent_translation` dengan JSON notebook dan `language_code`.
2. Terjemah setiap serpihan yang dikembalikan dalam ejen hos.
3. Panggil `finish_notebook_agent_translation` dengan `job` asal dan serpihan yang diterjemah.
4. Panggil `rewrite_notebook_paths` jika pautan notebook yang diterjemah memerlukan pelarasan laluan sasaran.

Alat berbantukan ejen tidak memanggil penyedia LLM yang dikonfigurasikan dari Co-op Translator. Ejen hos bertanggungjawab untuk menterjemah kepingan yang dikembalikan. Co-op Translator mengendalikan pemecahan Markdown kepada kepingan, pemeliharaan pemegang tempat, pembinaan semula frontmatter, penggantian sel buku nota, dan penormalan selepas terjemahan.

### Menterjemah Seluruh Repositori

Gunakan `run_translation` apabila pengguna mahu Co-op Translator berkelakuan seperti CLI `translate`.

Terjemahan repositori lalai kepada `dry_run=true` supaya ejen boleh memeriksa skop sebelum perubahan fail:

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "dry_run": true
}
```

Hasil `run_translation` termasuk tatasusunan `events` dengan acara kemajuan berversi
`co-op.translation.event.v1`. Klien MCP harus menggunakan medan seperti
`type`, `stage_key`, `completed`, `total`, dan `current_path` bukannya
mengurai teks konsol yang ditangkap. Serahkan `json_events_path` untuk juga menulis acara-acara tersebut
ke fail NDJSON.

Untuk membenarkan penulisan, pemanggil mesti menetapkan kedua `dry_run=false` dan `confirm_write=true`:

```json
{
  "language_codes": "ko",
  "root_dir": ".",
  "markdown": true,
  "dry_run": false,
  "confirm_write": true
}
```

`translate_project` didedahkan sebagai alias keserasian untuk `run_translation`.

### Semak Output yang Diterjemah

Gunakan `run_review` untuk pemeriksaan deterministik yang tidak memerlukan kelayakan LLM atau Vision:

!!! note "Beta"
    MCP mendedahkan API beta `run_review`. Ia selamat untuk aliran kerja semakan baca sahaja, tetapi pemeriksaan semakan dan skema isu mungkin berubah.

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "notebook": true
}
```

Hasil termasuk keluaran teks yang ditangkap dan ringkasan ulasan berstruktur apabila tersedia.

## Jalankan Pelayan Secara Manual

Pelaksanaan manual adalah terutamanya untuk menyahpepijat atau untuk pengangkutan yang berkelakuan seperti pelayan jangka panjang.

Debug the default stdio server:

```bash
co-op-translator-mcp
```

Run from a source checkout:

```bash
python -m co_op_translator.mcp.server
```

Jalankan pelayan HTTP atau SSE yang berterusan:

```bash
co-op-translator-mcp --transport streamable-http
co-op-translator-mcp --transport sse
```

Untuk integrasi penyunting dan ejen tempatan, utamakan konfigurasi `stdio` yang diuruskan oleh pelanggan dalam Langkah 2.

## Alat

| Alat | Tujuan | Menulis fail |
| --- | --- | --- |
| `translate_markdown_content` | Menterjemah rentetan Markdown. | Tidak |
| `translate_notebook_content` | Menterjemah sel Markdown dalam JSON notebook. | Tidak |
| `translate_image_content` | Menterjemah teks dalam satu imej dan mengembalikan data imej base64. | Pilihan, hanya apabila `output_path` disediakan |
| `start_markdown_agent_translation` | Sediakan serpihan Markdown untuk ejen hos menterjemah tanpa kelayakan LLM Co-op Translator. | Tidak |
| `finish_markdown_agent_translation` | Membina semula Markdown daripada serpihan yang diterjemah oleh ejen hos. | Tidak |
| `start_notebook_agent_translation` | Sediakan serpihan sel Markdown notebook untuk ejen hos menterjemah. | Tidak |
| `finish_notebook_agent_translation` | Membina semula JSON notebook daripada serpihan yang diterjemah oleh ejen hos. | Tidak |
| `rewrite_markdown_paths` | Tulis semula badan Markdown dan laluan frontmatter untuk sasaran yang diterjemah. | Tidak |
| `rewrite_notebook_paths` | Tulis semula laluan di dalam sel Markdown notebook. | Tidak |
| `run_translation` | Jalankan terjemahan peringkat projek seperti CLI. | Ya apabila `dry_run=false` dan `confirm_write=true` |
| `translate_project` | Alias keserasian untuk `run_translation`. | Ya apabila `dry_run=false` dan `confirm_write=true` |
| `run_review` | Jalankan pemeriksaan ulasan deterministik. | Tidak |
| `get_configuration_status` | Laporkan pembekal LLM dan Vision yang dikonfigurasi tanpa mendedahkan rahsia. | Tidak |
| `list_supported_languages` | Senaraikan kod bahasa sasaran yang disokong. | Tidak |
| `get_api_overview` | Terangkan aliran kerja dan alat MCP yang tersedia. | Tidak |

## Sumber

| URI Sumber | Tujuan |
| --- | --- |
| `co-op://api` | Tinjauan JSON tentang aliran kerja dan alat. |
| `co-op://supported-languages` | Senarai JSON kod bahasa sasaran yang disokong. |
| `co-op://configuration` | Ringkasan ketersediaan pembekal dalam JSON tanpa rahsia. |

## Arahan

| Arahan | Tujuan |
| --- | --- |
| `translate_markdown_document_prompt` | Membimbing klien MCP melalui terjemahan kandungan serta penulisan semula laluan pilihan. |
| `agent_assisted_markdown_translation_prompt` | Membimbing klien MCP melalui terjemahan Markdown oleh ejen hos tanpa kelayakan pembekal LLM Co-op Translator. |
| `translate_repository_prompt` | Membimbing klien MCP melalui terjemahan repositori yang bermula dengan dry-run. |

## Contoh Salin-Tampal

Terjemah kandungan Markdown:

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

Tulis semula pautan Markdown yang diterjemah:

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

Terjemah Markdown dengan model ejen hos:

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

Selepas ejen hos menterjemah setiap serpihan yang dikembalikan, selesaikan kerja dengan objek `job` lengkap yang dikembalikan oleh `start_markdown_agent_translation`:

```text
tool: finish_markdown_agent_translation
arguments:
  job: <the full job object returned by start_markdown_agent_translation>
  translated_chunks:
    - chunk_id: body:1
      translated_text: "# 안녕하세요\n\n시작하려면 `pip install`을 사용하세요."
```

Pratonton terjemahan repositori:

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

## Penyelesaian Masalah

| Masalah | Apa yang perlu dicuba |
| --- | --- |
| Klien MCP tidak dapat menemui `co-op-translator-mcp`. | Gunakan laluan boleh laksana Python mutlak dan konfigurasi checkout sumber `["-m", "co_op_translator.mcp.server"]`. |
| Pelayan disenaraikan tetapi terjemahan gagal. | Panggil `get_configuration_status` dan sahkan penyedia LLM tersedia. |
| Anda mahukan terjemahan Markdown atau buku nota tanpa kredensial penyedia. | Gunakan `start_markdown_agent_translation` / `finish_markdown_agent_translation` atau setara buku nota supaya ejen hos menterjemah kepingan tersebut. |
| Terjemahan imej gagal. | Sahkan pembolehubah Azure AI Vision ditetapkan dan panggil `get_configuration_status`. |
| Terjemahan repositori tidak menulis fail. | Tetapkan `dry_run=false` dan `confirm_write=true` hanya selepas kelulusan pengguna yang jelas. |
| Perubahan pada konfigurasi klien tidak muncul. | Mulakan semula atau muat semula klien MCP. |

## Nota Keselamatan

- Panggilan alat MCP dikawal oleh model aplikasi hos, jadi terjemahan repositori adalah ujian kering secara lalai.
- Terjemahan repositori penuh boleh mencipta, mengemas kini, atau membuang banyak fail. Perlukan kelulusan pengguna secara eksplisit sebelum menetapkan `confirm_write=true`.
- Alat status konfigurasi tidak pernah memulangkan kunci API, titik akhir, atau nilai rahsia lain.
- Terjemahan imej mengembalikan data imej base64. Imej bersaiz besar boleh menghasilkan respons alat yang besar.
- Alat berbantukan ejen mengembalikan kepingan sumber dan prompt kepada hos MCP. Gunakan ia hanya dengan kandungan yang pengguna selesa untuk dihantar kepada model ejen hos tersebut.
