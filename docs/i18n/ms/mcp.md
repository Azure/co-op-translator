# Pelayan MCP

Co-op Translator termasuk pelayan Model Context Protocol untuk ejen, penyunting, dan klien yang serasi dengan MCP.

Untuk tetapan tempatan lalai, pengguna tidak menjalankan pelayan berasingan secara manual. Mereka mengkonfigurasi klien MCP mereka, dan klien memulakan `co-op-translator-mcp` secara automatik melalui `stdio` apabila ia memerlukan alat Co-op Translator.

Jika anda sedang membuat keputusan antara CLI, Python API, dan MCP, mulakan dengan [Pilih Aliran Kerja Anda](workflows.md).

Gunakan MCP apabila ejen atau penyunting perlu memanggil Co-op Translator secara terus:

| Tujuan pengguna | Alat MCP |
| --- | --- |
| Terjemahkan satu dokumen Markdown, buku nota, atau imej | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content` |
| Terjemahkan kandungan Markdown atau buku nota dengan model ejen hos | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Tulis semula pautan Markdown atau buku nota yang diterjemahkan selepas memilih laluan output | `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Terjemahkan keseluruhan repositori seperti CLI | `run_translation`, `translate_project` |
| Semak output yang diterjemahkan tanpa kelayakan LLM | `run_review` |
| Periksa keupayaan dan status persekitaran | `get_api_overview`, `list_supported_languages`, `get_configuration_status` |

Pelayan MCP membalut API Python awam yang sama yang didokumentasikan dalam [Python API](api.md). Alat yang disokong penyedia menggunakan penyedia yang sama yang dikonfigurasi seperti CLI dan Python API. Alat yang dibantu ejen menyediakan kepingan untuk ejen hos MCP menterjemah, kemudian menggunakan Co-op Translator untuk menyusun semula Markdown atau buku nota akhir.

## Langkah 1: Pasang dan Konfigurasikan Co-op Translator

Pasang Co-op Translator dalam persekitaran Python yang akan digunakan oleh klien MCP anda:

```bash
pip install co-op-translator
```

Untuk pembangunan tempatan dari repositori ini, pasang pakej dalam mod boleh sunting:

```bash
pip install -e .
```

Pilih mod penterjemahan yang akan digunakan oleh klien MCP anda:

| Mod | Gunakan untuk | Kredensial |
| --- | --- | --- |
| Provider-backed | Co-op Translator memanggil `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, atau `run_translation`. | Penterjemahan Markdown dan buku nota memerlukan Azure OpenAI atau OpenAI. Penterjemahan imej juga memerlukan Azure AI Vision. |
| Agent-assisted | Ejen hos MCP menterjemah kepingan yang dikembalikan oleh `start_markdown_agent_translation` atau `start_notebook_agent_translation`. | Tiada kredensial pembekal LLM Co-op Translator diperlukan untuk kepingan Markdown atau buku nota. Penterjemahan imej belum diliputi oleh mod yang dibantu ejen. |

Jika anda bermula dengan penterjemahan Markdown atau buku nota di dalam ejen seperti Codex atau Claude Code, mulakan dengan mod yang dibantu ejen. Gunakan mod provider-backed apabila anda mahu Co-op Translator sendiri memanggil penyedia yang dikonfigurasi, apabila anda menterjemah imej, atau apabila anda menjalankan penterjemahan peringkat repositori seperti CLI.

Konfigurasikan kredensial penyedia hanya untuk aliran kerja provider-backed:

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Penterjemahan imej yang disokong penyedia juga memerlukan:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

!!! note
    Mod yang dibantu ejen kini merangkumi Markdown dan sel Markdown dalam buku nota. Penterjemahan imej masih menggunakan saluran imej yang disokong penyedia dan memerlukan Azure AI Vision untuk OCR dan rendering yang peka susun atur.

## Langkah 2: Konfigurasikan Klien MCP Anda

Untuk tetapan `stdio` tempatan biasa, tambahkan Co-op Translator ke konfigurasi klien MCP anda. Klien akan memulakan dan menghentikan proses itu secara automatik.

Konfigurasi pakej terpasang:

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

Konfigurasi checkout sumber pada Windows:

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

Selepas menukar konfigurasi klien MCP, mulakan semula atau muat semula klien supaya ia dapat mengesan pelayan baru.

## Langkah 3: Sahkan Pelayan dalam Klien

Minta klien MCP menyenaraikan alat yang tersedia, atau panggil salah satu pembantu baca-sahaja terlebih dahulu:

```json
{
  "tool": "get_api_overview",
  "arguments": {}
}
```

Pemeriksaan awal yang berguna:

| Alat | Apa yang perlu disemak |
| --- | --- |
| `get_api_overview` | Mengesahkan pelayan boleh dicapai dan menunjukkan aliran kerja yang tersedia. |
| `list_supported_languages` | Mengesahkan data bahasa yang dibungkus boleh dimuatkan. |
| `get_configuration_status` | Mengesahkan ketersediaan penyedia LLM dan Vision tanpa mendedahkan nilai rahsia. |

## Langkah 4: Pilih Aliran Kerja

### Terjemahkan Fail atau Dokumen Individu

Gunakan alat kandungan provider-backed apabila klien MCP sudah mempunyai kandungan dokumen atau laluan imej dan Co-op Translator sepatutnya memanggil penyedia penterjemahan yang dikonfigurasi.

Untuk Markdown:

1. Panggil `translate_markdown_content` dengan `document`, `language_code`, dan secara pilihan `source_path`.
2. Jika hasil terjemahan akan ditulis ke susun atur output Co-op Translator, panggil `rewrite_markdown_paths`.
3. Biarkan klien menulis atau memulangkan `content` akhir.

Untuk buku nota:

1. Panggil `translate_notebook_content` dengan JSON buku nota dan `language_code`.
2. Panggil `rewrite_notebook_paths` jika pautan buku nota yang diterjemahkan perlu disesuaikan untuk laluan sasaran.
3. Tulis atau pulangkan JSON buku nota akhir.

Untuk imej:

1. Panggil `translate_image_content` dengan `image_path`, `language_code`, dan pilihan `root_dir` atau `fast_mode`.
2. Baca `data_base64` dan `mime_type` yang dikembalikan.
3. Jika `output_path` disediakan, imej yang diterjemahkan juga disimpan ke laluan tersebut.

Alat kandungan tidak melakukan penemuan projek, kemas kini metadata, kenyataan pemberitahuan, atau penulisan semula laluan automatik. Jika anda mahu ejen hos menterjemah kepingan Markdown atau buku nota tanpa kredensial pembekal LLM Co-op Translator, gunakan aliran kerja yang dibantu ejen di bawah.

### Terjemahkan dengan Model Ejen Hos

Gunakan alat yang dibantu ejen apabila anda mahu ejen hos MCP, seperti pembantu pengekodan, menghasilkan teks yang diterjemah dan bukannya mengkonfigurasi Azure OpenAI atau OpenAI untuk Co-op Translator.

Dalam klien MCP berasaskan sembang, biasanya anda tidak perlu menulis JSON alat sendiri. Minta ejen menggunakan aliran kerja yang dibantu ejen:

```text
Translate this Markdown file to Korean with Co-op Translator MCP.
Use agent-assisted mode: call start_markdown_agent_translation, translate the returned chunks with your own model, then call finish_markdown_agent_translation.
Keep Markdown formatting, code blocks, and links intact.
```

Untuk buku nota, gunakan corak yang sama:

```text
Translate this notebook to Korean with Co-op Translator MCP.
Use start_notebook_agent_translation, translate the returned Markdown-cell chunks with your own model, then call finish_notebook_agent_translation.
Preserve code cells, outputs, and notebook metadata.
```

Jika klien MCP anda menyokong prompt pelayan, gunakan `agent_assisted_markdown_translation_prompt` supaya klien memuat arahan aliran kerja yang sama.

Untuk Markdown:

1. Panggil `start_markdown_agent_translation` dengan `document`, `language_code`, dan secara pilihan `source_path`.
2. Terjemahkan setiap kepingan yang dikembalikan dalam ejen hos dengan mengikuti `prompt` kepingan.
3. Panggil `finish_markdown_agent_translation` dengan `job` asal dan kepingan yang diterjemahkan menggunakan `chunk_id` dan `translated_text`.
4. Jika kandungan akan ditulis ke laluan sasaran yang diterjemahkan, panggil `rewrite_markdown_paths`.

Untuk buku nota:

1. Panggil `start_notebook_agent_translation` dengan JSON buku nota dan `language_code`.
2. Terjemahkan setiap kepingan yang dikembalikan dalam ejen hos.
3. Panggil `finish_notebook_agent_translation` dengan `job` asal dan kepingan yang diterjemahkan.
4. Panggil `rewrite_notebook_paths` jika pautan buku nota yang diterjemahkan memerlukan pelarasan laluan sasaran.

Alat yang dibantu ejen tidak memanggil Azure OpenAI atau OpenAI dari Co-op Translator. Ejen hos bertanggungjawab untuk menterjemah kepingan yang dikembalikan. Co-op Translator mengendalikan pemecahan kepingan Markdown, pemeliharaan pemegang tempat, pembinaan semula frontmatter, penggantian sel buku nota, dan normalisasi pasca-terjemahan.

### Terjemahkan Seluruh Repositori

Gunakan `run_translation` apabila pengguna mahu Co-op Translator berfungsi seperti CLI `translate`.

Penterjemahan repositori lalai kepada `dry_run=true` supaya ejen boleh memeriksa skop sebelum perubahan fail:

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "dry_run": true
}
```

Untuk membenarkan penulisan, pemanggil mesti menetapkan kedua-dua `dry_run=false` dan `confirm_write=true`:

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

### Semak Output yang Diterjemahkan

Gunakan `run_review` untuk pemeriksaan deterministik yang tidak memerlukan kelayakan LLM atau Vision:

!!! note "Beta"
    MCP mendedahkan API beta `run_review`. Ia selamat untuk aliran kerja semakan baca-sahaja, tetapi pemeriksaan semakan dan skema isu mungkin berubah.

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "notebook": true
}
```

Keputusan termasuk keluaran teks yang ditangkap dan ringkasan semakan berstruktur apabila tersedia.

## Menjalankan Pelayan Secara Manual

Jalankan manual terutamanya untuk penggayaan atau untuk pengangkutan yang berkelakuan seperti pelayan jangka panjang.

Selesaikan masalah pelayan stdio lalai:

```bash
co-op-translator-mcp
```

Jalankan dari checkout sumber:

```bash
python -m co_op_translator.mcp.server
```

Jalankan pelayan HTTP atau SSE jangka panjang:

```bash
co-op-translator-mcp --transport streamable-http
co-op-translator-mcp --transport sse
```

Untuk integrasi editor dan ejen tempatan, utamakan konfigurasi `stdio` yang diuruskan oleh klien dalam Langkah 2.

## Alat

| Alat | Tujuan | Menulis fail |
| --- | --- | --- |
| `translate_markdown_content` | Terjemahkan rentetan Markdown. | Tidak |
| `translate_notebook_content` | Terjemahkan sel Markdown dalam JSON buku nota. | Tidak |
| `translate_image_content` | Terjemahkan teks dalam satu imej dan kembalikan data imej base64. | Pilihan, hanya apabila `output_path` disediakan |
| `start_markdown_agent_translation` | Sediakan kepingan Markdown untuk ejen hos menterjemah tanpa kredensial LLM Co-op Translator. | Tidak |
| `finish_markdown_agent_translation` | Susun semula Markdown daripada kepingan yang diterjemah oleh ejen hos. | Tidak |
| `start_notebook_agent_translation` | Sediakan kepingan sel Markdown buku nota untuk ejen hos menterjemah. | Tidak |
| `finish_notebook_agent_translation` | Susun semula JSON buku nota daripada kepingan yang diterjemah oleh ejen hos. | Tidak |
| `rewrite_markdown_paths` | Tulis semula badan Markdown dan laluan frontmatter untuk sasaran yang diterjemahkan. | Tidak |
| `rewrite_notebook_paths` | Tulis semula laluan dalam sel Markdown buku nota. | Tidak |
| `run_translation` | Jalankan penterjemahan peringkat projek seperti CLI. | Ya apabila `dry_run=false` dan `confirm_write=true` |
| `translate_project` | Alias keserasian untuk `run_translation`. | Ya apabila `dry_run=false` dan `confirm_write=true` |
| `run_review` | Jalankan pemeriksaan semakan deterministik. | Tidak |
| `get_configuration_status` | Laporkan penyedia LLM dan Vision yang dikonfigurasi tanpa mendedahkan rahsia. | Tidak |
| `list_supported_languages` | Senaraikan kod bahasa sasaran yang disokong. | Tidak |
| `get_api_overview` | Terangkan aliran kerja dan alat MCP yang tersedia. | Tidak |

## Sumber

| URI Sumber | Tujuan |
| --- | --- |
| `co-op://api` | Gambaran JSON aliran kerja dan alat. |
| `co-op://supported-languages` | Senarai JSON kod bahasa yang disokong. |
| `co-op://configuration` | Ringkasan ketersediaan penyedia JSON tanpa rahsia. |

## Arahan

| Prompt | Tujuan |
| --- | --- |
| `translate_markdown_document_prompt` | Mengarahkan klien MCP melalui penterjemahan kandungan serta penulisan semula laluan pilihan. |
| `agent_assisted_markdown_translation_prompt` | Mengarahkan klien MCP melalui penterjemahan Markdown oleh ejen hos tanpa kredensial pembekal LLM Co-op Translator. |
| `translate_repository_prompt` | Mengarahkan klien MCP melalui penterjemahan repositori dengan percubaan kering terlebih dahulu. |

## Contoh Salin-Tampal

Terjemahkan kandungan Markdown:

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

Tulis semula pautan Markdown yang diterjemahkan:

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

Terjemahkan Markdown dengan model ejen hos:

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

Selepas ejen hos menterjemah setiap kepingan yang dikembalikan, selesaikan kerja dengan objek `job` lengkap yang dikembalikan oleh `start_markdown_agent_translation`:

```text
tool: finish_markdown_agent_translation
arguments:
  job: <the full job object returned by start_markdown_agent_translation>
  translated_chunks:
    - chunk_id: body:1
      translated_text: "# 안녕하세요\n\n시작하려면 `pip install`을 사용하세요."
```

Pratonton penterjemahan repositori:

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
| Klien MCP tidak dapat mencari `co-op-translator-mcp`. | Gunakan laluan pelaksana Python mutlak dan konfigurasi checkout sumber `["-m", "co_op_translator.mcp.server"]`. |
| Pelayan disenaraikan tetapi penterjemahan gagal. | Panggil `get_configuration_status` dan sahkan penyedia LLM tersedia. |
| Anda mahu penterjemahan Markdown atau buku nota tanpa kunci Azure OpenAI/OpenAI. | Gunakan `start_markdown_agent_translation` / `finish_markdown_agent_translation` atau setara buku nota supaya ejen hos menterjemah kepingan. |
| Penterjemahan imej gagal. | Sahkan pembolehubah Azure AI Vision disetkan dan panggil `get_configuration_status`. |
| Penterjemahan repositori tidak menulis fail. | Tetapkan `dry_run=false` dan `confirm_write=true` hanya selepas kelulusan pengguna yang jelas. |
| Perubahan pada konfigurasi klien tidak muncul. | Mulakan semula atau muat semula klien MCP. |

## Nota Keselamatan

- Panggilan alat MCP dikawal model oleh aplikasi hos, jadi penterjemahan repositori adalah percubaan kering secara lalai.
- Penterjemahan repositori penuh boleh mencipta, mengemas kini, atau memadamkan banyak fail. Memerlukan kelulusan pengguna yang jelas sebelum menetapkan `confirm_write=true`.
- Alat status konfigurasi tidak pernah mengembalikan kunci API, titik akhir, atau nilai rahsia lain.
- Penterjemahan imej mengembalikan data imej base64. Imej besar boleh menghasilkan respons alat yang besar.
- Alat yang dibantu ejen mengembalikan kepingan sumber dan prompt kepada hos MCP. Gunakan mereka hanya dengan kandungan yang pengguna selesa untuk dihantar kepada model ejen hos tersebut.