# Pilih Aliran Kerja Anda

Co-op Translator boleh digunakan dalam tiga cara: CLI, API Python, dan pelayan MCP. Mereka berkongsi kebolehan terjemahan yang sama, tetapi setiap satu sesuai untuk aliran kerja yang berbeza.

Gunakan halaman ini apabila anda memutuskan di mana untuk bermula.

**Jika anda menyunting terjemahan secara manual:** aliran kerja CLI dan Actions lalai menterjemah semula fail sumber yang diubah sepenuhnya, jadi ayat anda dalam fail tersebut boleh ditimpakan. Semak diff sebelum menerima kemas kini. Untuk pemeliharaan blok-level Markdown bagi suntingan yang diterima, gunakan pilihan [Python API translation state provider](api.md#preserve-accepted-human-edits-with-a-translation-state-provider).

## Keputusan Pantas

| Jika anda mahu... | Gunakan | Mula di sini |
| --- | --- | --- |
| Terjemah atau semak repositori dari terminal | CLI | [Rujukan CLI](cli.md) |
| Tambah terjemahan ke skrip Python, perkhidmatan, notebook, atau tugas CI | Python API | [Rujukan API Python](api.md) |
| Biarkan agen, penyunting, atau klien yang serasi MCP menterjemah kandungan untuk anda | MCP Server | [Pelayan MCP](mcp.md) |
| Terjemah satu dokumen Markdown, notebook, atau imej yang aplikasi anda sudah muatkan | API Python atau Pelayan MCP | [API Python](api.md) atau [Pelayan MCP](mcp.md) |
| Terjemah seluruh repositori dengan folder output standard dan metadata | CLI atau `run_translation` | [Rujukan CLI](cli.md) atau [Rujukan API Python](api.md) |

## Gunakan CLI apabila

Pilih CLI apabila seorang pengguna atau tugas CI menggerakkan terjemahan repositori dari shell.

CLI adalah laluan paling langsung apabila anda mahu Co-op Translator menemui fail projek, menghasilkan output terjemahan, mengekalkan susunan projek, mengemaskini metadata, dan menjalankan arahan semakan.

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -md -nb
co-op-review -l "ko"
migrate-links -l "ko" --dry-run
```

Contoh ini menterjemah Markdown dan notebook. Tambah `-img` hanya selepas mengkonfigurasi [Azure AI Vision](configuration.md#azure-ai-vision). Untuk larian pertama hanya Markdown, ikuti [Terjemahan pertama anda](first-translation.md).

Sesuai untuk:

- Anda sedang menterjemah repositori dari terminal anda.
- Anda mahukan perintah yang boleh diulang untuk aliran kerja CI atau pelepasan.
- Anda mahukan penemuan projek terbina dalam, laluan output, metadata, pembersihan, dan semakan.
- Anda lebih suka antara muka perintah berbanding menulis kod Python.

## Gunakan API Python apabila

Pilih API Python apabila kod anda sendiri perlu mengawal aliran kerja.

API berguna untuk aplikasi, skrip automasi, notebook, perkhidmatan, dan saluran paip tersuai. Ia membolehkan anda memanggil API terjemahan kandungan aras rendah untuk fail individu, atau menjalankan orkestrasi peringkat repositori yang sama seperti yang digunakan oleh CLI.

Terjemah satu dokumen Markdown dan tentukan di mana untuk menyimpannya:

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

Sesuai untuk:

- Aplikasi anda sudah membaca fail, buffer, notebook, atau bait imej.
- Anda memerlukan pengesahan tersuai, storan, logging, cubaan semula, atau aliran kelulusan.
- Anda mahu menterjemah satu dokumen, notebook, atau imej tanpa memproses keseluruhan repositori.
- Anda mahu terjemahan repositori, tetapi melalui automasi Python dan bukannya arahan shell.

## Gunakan Pelayan MCP apabila

Pilih pelayan MCP apabila agen, penyunting, atau klien yang serasi MCP harus memanggil alat Co-op Translator.

Dalam pemasangan tempatan biasa, pengguna tidak mengekalkan server berjalan secara manual. Klien MCP memulakan `co-op-translator-mcp` melalui `stdio` apabila ia memerlukan alat tersebut.

Contoh permintaan pengguna yang boleh ditangani oleh agen:

- "Terjemahkan fail Markdown ini ke bahasa Korea dan pastikan pautan betul."
- "Terjemahkan fail Markdown ini ke bahasa Korea dengan aliran kerja MCP dibantu agen, menggunakan model anda sendiri untuk cebisan terjemahan."
- "Terjemahkan notebook ini ke bahasa Korea, pelihara sel kod, dan gunakan Co-op Translator MCP untuk menyusun semula notebook."
- "Terjemahkan teks dalam imej ini ke bahasa Jepun dan simpan hasilnya."
- "Jalankan simulasi terjemahan repositori ke bahasa Sepanyol dan beritahu saya apa yang akan berubah."
- "Semak sama ada output terjemahan bahasa Korea adalah terkini."

Untuk Markdown dan notebook, MCP boleh berfungsi dalam dua mod:

| Mod | Gunakan apabila | Alat utama |
| --- | --- | --- |
| Dibantu agen | Agen hos MCP harus menterjemah cebisan dengan modelnya sendiri, tanpa kelayakan pembekal LLM Co-op Translator. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Disokong pembekal | Co-op Translator harus memanggil Azure OpenAI, OpenAI, atau Anthropic secara langsung. | `translate_markdown_content`, `translate_notebook_content` |

Bentuk panggilan alat Markdown yang disokong pembekal MCP:

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

Terjemahan repositori dijalankan sebagai simulasi secara lalai melalui MCP:

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

Sesuai untuk:

- Anda mahukan aliran kerja terjemahan berbahasa semula jadi dalam agen atau penyunting.
- Anda mahukan terjemahan Markdown atau notebook di mana model agen hos menterjemah cebisan yang disediakan.
- Anda mahu agen menterjemah kandungan yang dipilih dan bukannya seluruh repositori.
- Anda mahu langkah kelulusan sebelum penulisan seluruh repositori.
- Anda mahu satu antara muka yang mendedahkan alat untuk Markdown, notebook, imej, semakan, dan penulisan semula laluan.

## Bagaimana Mereka Saling Melengkapi

CLI adalah pilihan lalai terbaik untuk manusia yang menterjemah repositori. API Python adalah terbaik apabila kod anda mengurus aliran kerja. Pelayan MCP adalah terbaik apabila agen atau penyunting mengurus aliran kerja.

Ketiga-tiga laluan menggunakan API awam Co-op Translator yang sama, jadi anda boleh mula dengan CLI, mengautomasikan dengan Python kemudian, dan mendedahkan kebolehan yang sama kepada klien MCP apabila anda memerlukan aliran kerja dipacu agen.