# Pilih Alur Kerja Anda

Co-op Translator dapat digunakan dalam tiga cara: CLI, Python API, dan MCP server. Ketiganya menggunakan kemampuan terjemahan yang sama, tetapi masing-masing cocok untuk alur kerja yang berbeda.

Gunakan halaman ini ketika Anda memutuskan dari mana memulai.

**Jika Anda mengedit terjemahan secara manual:** alur kerja default CLI dan Actions akan menerjemahkan ulang berkas sumber yang diubah secara penuh, sehingga redaksi Anda di berkas-berkas tersebut dapat ditimpa. Tinjau diff sebelum menerima pembaruan. Untuk pelestarian tingkat-blok Markdown dari suntingan yang diterima, gunakan opsional [Penyedia status terjemahan Python API](api.md#preserve-accepted-human-edits-with-a-translation-state-provider).

## Keputusan Singkat

| Jika Anda ingin... | Gunakan | Mulai di sini |
| --- | --- | --- |
| Menerjemahkan atau meninjau repositori dari terminal | CLI | [Referensi CLI](cli.md) |
| Menambahkan terjemahan ke skrip Python, layanan, notebook, atau pekerjaan CI | Python API | [Python API](api.md) |
| Meminta agen, editor, atau klien yang kompatibel MCP menerjemahkan konten untuk Anda | MCP Server | [MCP Server](mcp.md) |
| Menerjemahkan satu dokumen Markdown, notebook, atau gambar yang sudah dimuat aplikasi Anda | Python API or MCP Server | [Python API](api.md) or [MCP Server](mcp.md) |
| Menerjemahkan seluruh repositori dengan folder keluaran standar dan metadata | CLI or `run_translation` | [CLI Reference](cli.md) or [Python API](api.md) |

## Gunakan CLI ketika

Pilih CLI ketika seseorang atau pekerjaan CI menjalankan terjemahan repositori dari shell.

CLI adalah jalur paling langsung ketika Anda ingin Co-op Translator menemukan berkas proyek, membuat keluaran terjemahan, mempertahankan tata letak proyek, memperbarui metadata, dan menjalankan perintah peninjauan.

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -md -nb
co-op-review -l "ko"
migrate-links -l "ko" --dry-run
```

Contoh ini menerjemahkan Markdown dan notebook. Tambahkan `-img` hanya setelah mengonfigurasi [Azure AI Vision](configuration.md#azure-ai-vision). Untuk run pertama yang hanya Markdown, ikuti [Terjemahan pertama Anda](first-translation.md).

Cocok untuk:

- Anda sedang menerjemahkan repositori dari terminal Anda.
- Anda menginginkan perintah yang dapat diulang untuk alur kerja CI atau rilis.
- Anda menginginkan penemuan proyek bawaan, jalur keluaran, metadata, pembersihan, dan peninjauan.
- Anda lebih memilih antarmuka perintah daripada menulis kode Python.

## Gunakan Python API ketika

Pilih Python API ketika kode Anda sendiri yang harus mengontrol alur kerja.

API berguna untuk aplikasi, skrip otomatisasi, notebook, layanan, dan pipeline kustom. Ini memungkinkan Anda memanggil API terjemahan konten tingkat-rendah untuk berkas individual, atau menjalankan orkestrasi tingkat repositori yang sama seperti yang digunakan oleh CLI.

Terjemahkan satu dokumen Markdown dan tentukan di mana menyimpannya:

```python
import asyncio
from pathlib import Path

from co_op_translator.api import rewrite_markdown_paths, translate_markdown_content


async def main() -> None:
    source_path = Path("docs/guide.md")
    target_path = Path("translations/ko/docs/guide.md")

    translated = await translate_markdown_content(
        source_path.read_text(encoding="utf-8"),
        "ko",
        {"source_path": source_path},
    )

    rewritten = rewrite_markdown_paths(
        translated,
        source_path=source_path,
        target_path=target_path,
    )

    target_path.parent.mkdir(parents=True, exist_ok=True)
    target_path.write_text(rewritten, encoding="utf-8")


asyncio.run(main())
```

Jalankan terjemahan repositori dari Python:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    notebook=True,
    images=False,
    dry_run=True,
)
```

Cocok untuk:

- Aplikasi Anda sudah membaca berkas, buffer, notebook, atau byte gambar.
- Anda membutuhkan validasi kustom, penyimpanan, logging, percobaan ulang, atau alur persetujuan.
- Anda ingin menerjemahkan satu dokumen, notebook, atau gambar tanpa memproses seluruh repositori.
- Anda menginginkan terjemahan repositori, tetapi melalui otomatisasi Python alih-alih perintah shell.

## Gunakan MCP Server ketika

Pilih MCP server ketika agen, editor, atau klien yang kompatibel MCP harus memanggil alat Co-op Translator.

Dalam pengaturan lokal normal, pengguna tidak perlu menjalankan server secara manual. Klien MCP memulai `co-op-translator-mcp` melalui `stdio` ketika membutuhkan alat tersebut.

Contoh permintaan pengguna yang dapat ditangani oleh agen:

- "Terjemahkan berkas Markdown ini ke bahasa Korea dan pastikan tautannya benar."
- "Terjemahkan berkas Markdown ini ke bahasa Korea dengan alur kerja MCP yang dibantu agen, menggunakan model Anda sendiri untuk potongan terjemahan."
- "Terjemahkan notebook ini ke bahasa Korea, pertahankan sel kode, dan gunakan Co-op Translator MCP untuk merekonstruksi notebook."
- "Terjemahkan teks dalam gambar ini ke bahasa Jepang dan simpan hasilnya."
- "Lakukan dry-run terjemahan repositori ke bahasa Spanyol dan beri tahu saya apa yang akan berubah."
- "Tinjau apakah keluaran terjemahan bahasa Korea sudah terbaru."

Untuk Markdown dan notebook, MCP dapat bekerja dalam dua mode:

| Mode | Gunakan ketika | Alat utama |
| --- | --- | --- |
| Agent-assisted | Agen host MCP harus menerjemahkan potongan dengan modelnya sendiri, tanpa kredensial penyedia LLM Co-op Translator. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Provider-backed | Co-op Translator harus memanggil Azure OpenAI, OpenAI, atau Anthropic secara langsung. | `translate_markdown_content`, `translate_notebook_content` |

Bentuk pemanggilan alat Markdown yang didukung oleh penyedia MCP:

```json
{
  "tool": "translate_markdown_content",
  "arguments": {
    "document": "# Setup\n\nInstall Co-op Translator first.",
    "language_code": "ko",
    "options": {
      "source_path": "docs/setup.md"
    }
  }
}
```

MCP image tool call shape:

```json
{
  "tool": "translate_image_content",
  "arguments": {
    "image_path": "assets/architecture.png",
    "language_code": "ko",
    "output_path": "translated_images/ko/assets/architecture.png"
  }
}
```

Terjemahan repositori bersifat dry-run secara default melalui MCP:

```json
{
  "tool": "run_translation",
  "arguments": {
    "language_codes": ["ko"],
    "translate_markdown": true,
    "translate_notebooks": true,
    "translate_images": false,
    "dry_run": true
  }
}
```

Cocok untuk:

- Anda menginginkan alur kerja terjemahan berbahasa alami di dalam agen atau editor.
- Anda menginginkan terjemahan Markdown atau notebook di mana model agen host menerjemahkan potongan yang telah disiapkan.
- Anda ingin agen menerjemahkan konten yang dipilih, bukan seluruh repositori.
- Anda menginginkan langkah persetujuan sebelum penulisan ke seluruh repositori.
- Anda menginginkan satu antarmuka yang memaparkan alat-alat untuk Markdown, notebook, gambar, tinjauan, dan penulisan ulang jalur.

## Bagaimana Mereka Bekerja Bersama

CLI adalah pilihan default terbaik untuk manusia yang menerjemahkan repositori. Python API paling cocok ketika kode Anda yang mengendalikan alur kerja. MCP server paling cocok ketika agen atau editor yang mengendalikan alur kerja.

Ketiga jalur tersebut menggunakan API Co-op Translator publik yang sama, jadi Anda dapat memulai dengan CLI, mengotomatiskan dengan Python nanti, dan menyediakan kemampuan yang sama untuk klien MCP ketika Anda membutuhkan alur kerja yang digerakkan oleh agen.