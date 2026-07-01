# Pilih Alur Kerja Anda

Co-op Translator dapat digunakan dengan tiga cara: CLI, Python API, dan server MCP. Ketiganya memiliki kemampuan terjemahan yang sama, tetapi masing-masing cocok untuk alur kerja yang berbeda.

Gunakan halaman ini saat Anda memutuskan dari mana memulai.

## Keputusan Cepat

| Jika Anda ingin... | Gunakan | Mulai di sini |
| --- | --- | --- |
| Menerjemahkan atau meninjau repositori dari terminal | CLI | [Referensi CLI](cli.md) |
| Menambahkan terjemahan ke skrip Python, layanan, notebook, atau pekerjaan CI | Python API | [Python API](api.md) |
| Biarkan agen, editor, atau klien yang kompatibel dengan MCP menerjemahkan konten untuk Anda | MCP Server | [MCP Server](mcp.md) |
| Menerjemahkan satu dokumen Markdown, notebook, atau gambar yang sudah dimuat aplikasi Anda | Python API atau MCP Server | [Python API](api.md) atau [MCP Server](mcp.md) |
| Menerjemahkan seluruh repositori dengan folder output dan metadata standar | CLI atau `run_translation` | [CLI Reference](cli.md) atau [Python API](api.md) |

## Gunakan CLI ketika

Pilih CLI ketika seseorang atau pekerjaan CI menjalankan terjemahan repositori dari shell.

CLI adalah jalur paling langsung ketika Anda ingin Co-op Translator menemukan file proyek, membuat output terjemahan, mempertahankan tata letak proyek, memperbarui metadata, dan menjalankan perintah tinjauan.

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -md -nb -img
co-op-review -l "ko" -md -nb
migrate-links -l "ko" --dry-run
```

Cocok untuk:

- Anda sedang menerjemahkan repositori dari terminal Anda.
- Anda menginginkan perintah yang dapat diulang untuk alur kerja CI atau rilis.
- Anda menginginkan penemuan proyek bawaan, jalur output, metadata, pembersihan, dan tinjauan.
- Anda lebih memilih antarmuka perintah daripada menulis kode Python.

## Gunakan Python API ketika

Pilih Python API ketika kode Anda sendiri harus mengendalikan alur kerja.

API berguna untuk aplikasi, skrip otomatisasi, notebook, layanan, dan pipeline kustom. Ini memungkinkan Anda memanggil API terjemahan konten tingkat rendah untuk file individual, atau menjalankan orkestrasi tingkat repositori yang sama seperti yang digunakan oleh CLI.

Terjemahkan satu dokumen Markdown dan tentukan tempat menyimpannya:

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
import asyncio

from co_op_translator.api import run_translation


async def main() -> None:
    await run_translation(
        language_codes=["ko"],
        translate_markdown=True,
        translate_notebooks=True,
        translate_images=False,
        dry_run=True,
    )


asyncio.run(main())
```

Cocok untuk:

- Aplikasi Anda sudah membaca file, buffer, notebook, atau byte gambar.
- Anda membutuhkan validasi kustom, penyimpanan, pencatatan, percobaan ulang, atau alur persetujuan.
- Anda ingin menerjemahkan satu dokumen, notebook, atau gambar tanpa memproses seluruh repositori.
- Anda menginginkan terjemahan repositori, tetapi dari otomatisasi Python daripada perintah shell.

## Gunakan Server MCP ketika

Pilih server MCP ketika agen, editor, atau klien yang kompatibel dengan MCP perlu memanggil alat Co-op Translator.

Dalam pengaturan lokal normal, pengguna tidak secara manual menjaga server tetap berjalan. Klien MCP memulai `co-op-translator-mcp` melalui `stdio` saat membutuhkan alat tersebut.

Contoh permintaan pengguna yang dapat ditangani agen:

- "Terjemahkan file Markdown ini ke bahasa Korea dan pertahankan tautan agar tetap benar."
- "Terjemahkan file Markdown ini ke bahasa Korea dengan alur kerja MCP berbantuan agen, menggunakan model Anda sendiri untuk potongan yang diterjemahkan."
- "Terjemahkan notebook ini ke bahasa Korea, pertahankan sel kode, dan gunakan Co-op Translator MCP untuk merekonstruksi notebook."
- "Terjemahkan teks dalam gambar ini ke bahasa Jepang dan simpan hasilnya."
- "Lakukan dry-run terjemahan repositori ke bahasa Spanyol dan beri tahu saya apa yang akan berubah."
- "Tinjau apakah keluaran terjemahan bahasa Korea sudah mutakhir."

Untuk Markdown dan notebook, MCP dapat bekerja dalam dua mode:

| Mode | Gunakan ketika | Alat utama |
| --- | --- | --- |
| Agent-assisted | Agen host MCP harus menerjemahkan potongan dengan modelnya sendiri, tanpa kredensial penyedia LLM Co-op Translator. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Provider-backed | Co-op Translator harus memanggil Azure OpenAI atau OpenAI secara langsung. | `translate_markdown_content`, `translate_notebook_content` |

MCP provider-backed Markdown tool call shape:

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

Terjemahan repositori secara default adalah dry-run melalui MCP:

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
- Anda menginginkan terjemahan Markdown atau notebook di mana model agen host menerjemahkan potongan yang disiapkan.
- Anda ingin agen menerjemahkan konten yang dipilih alih-alih seluruh repositori.
- Anda menginginkan langkah persetujuan sebelum penulisan ke seluruh repositori.
- Anda menginginkan satu antarmuka yang menampilkan alat Markdown, notebook, gambar, tinjauan, dan penulisan ulang jalur.

## Bagaimana Mereka Cocok Bersama

CLI adalah pilihan default terbaik untuk manusia yang menerjemahkan repositori. Python API paling baik ketika kode Anda mengelola alur kerja. Server MCP paling baik ketika agen atau editor yang mengelola alur kerja.

Ketiga jalur menggunakan API publik Co-op Translator yang sama, jadi Anda dapat memulai dengan CLI, mengotomatisasi dengan Python nanti, dan mengekspos kemampuan yang sama ke klien MCP ketika Anda membutuhkan alur kerja yang digerakkan agen.