# Pilih Aliran Kerja Anda

Co-op Translator boleh digunakan dalam tiga cara: CLI, API Python, dan pelayan MCP. Mereka berkongsi kebolehan terjemahan yang sama, tetapi setiap satu sesuai untuk aliran kerja yang berbeza.

Gunakan halaman ini apabila anda memutuskan di mana untuk bermula.

## Keputusan Pantas

| Jika anda mahu... | Gunakan | Mula di sini |
| --- | --- | --- |
| Terjemah atau semak semula repositori dari terminal | CLI | [Rujukan CLI](cli.md) |
| Tambah terjemahan ke skrip Python, perkhidmatan, notebook, atau tugasan CI | Python API | [API Python](api.md) |
| Biarkan agen, penyunting, atau klien serasi MCP menterjemah kandungan untuk anda | Pelayan MCP | [Pelayan MCP](mcp.md) |
| Terjemah satu dokumen Markdown, notebook, atau imej yang aplikasi anda sudah muatkan | API Python atau Pelayan MCP | [API Python](api.md) atau [Pelayan MCP](mcp.md) |
| Terjemah seluruh repositori dengan folder output standard dan metadata | CLI atau `run_translation` | [Rujukan CLI](cli.md) atau [API Python](api.md) |

## Gunakan CLI apabila

Pilih CLI apabila seseorang atau tugasan CI mengendalikan terjemahan repositori dari shell.

CLI adalah laluan paling langsung apabila anda mahu Co-op Translator menemui fail projek, mencipta output terjemahan, mengekalkan susun atur projek, mengemas kini metadata, dan menjalankan arahan semakan.

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -md -nb -img
co-op-review -l "ko" -md -nb
migrate-links -l "ko" --dry-run
```

Sesuai untuk:

- Anda sedang menterjemah repositori dari terminal anda.
- Anda mahukan arahan yang boleh diulang untuk aliran kerja CI atau pelancaran.
- Anda mahukan penemuan projek terbina dalam, laluan output, metadata, pembersihan, dan semakan.
- Anda mengutamakan antara muka arahan berbanding menulis kod Python.

## Gunakan API Python apabila

Pilih API Python apabila kod anda sendiri harus mengawal aliran kerja.

API berguna untuk aplikasi, skrip automasi, notebook, perkhidmatan, dan saluran paip khusus. Ia membolehkan anda memanggil API terjemahan kandungan aras rendah untuk fail individu, atau menjalankan orkestrasi peringkat repositori yang sama yang digunakan oleh CLI.

Terjemah satu dokumen Markdown dan tentukan tempat menyimpannya:

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

Sesuai untuk:

- Aplikasi anda sudah membaca fail, buffer, notebook, atau bait imej.
- Anda memerlukan pengesahan tersuai, penyimpanan, logging, cubaan semula, atau aliran kelulusan.
- Anda mahu menterjemah satu dokumen, notebook, atau imej tanpa memproses keseluruhan repositori.
- Anda mahu terjemahan repositori, tetapi dari automasi Python dan bukannya arahan shell.

## Gunakan Pelayan MCP apabila

Pilih pelayan MCP apabila agen, penyunting, atau klien serasi MCP perlu memanggil alat Co-op Translator.

Dalam susunan tempatan biasa, pengguna tidak mengekalkan pelayan berjalan secara manual. Klien MCP memulakan `co-op-translator-mcp` melalui `stdio` apabila ia memerlukan alat tersebut.

Contoh permintaan pengguna yang boleh ditangani oleh agen:

- "Terjemah fail Markdown ini ke Bahasa Korea dan pastikan pautan betul."
- "Terjemah fail Markdown ini ke Bahasa Korea dengan aliran kerja MCP dibantu agen, menggunakan model anda sendiri untuk bahagian yang diterjemahkan."
- "Terjemah notebook ini ke Bahasa Korea, kekalkan sel kod, dan gunakan Co-op Translator MCP untuk menyusun semula notebook tersebut."
- "Terjemah teks dalam imej ini ke Bahasa Jepun dan simpan hasilnya."
- "Jalankan uji kering (dry-run) terjemahan repositori ke Bahasa Sepanyol dan beritahu saya apa yang akan berubah."
- "Semak sama ada output terjemahan Bahasa Korea adalah terkini."

Untuk Markdown dan notebook, MCP boleh berfungsi dalam dua mod:

| Mod | Gunakan apabila | Alat utama |
| --- | --- | --- |
| Dibantu agen | Ejen hos MCP harus menterjemah bahagian dengan modelnya sendiri, tanpa kelayakan pembekal LLM Co-op Translator. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Disokong pembekal | Co-op Translator harus memanggil Azure OpenAI atau OpenAI secara langsung. | `translate_markdown_content`, `translate_notebook_content` |

Bentuk panggilan alat Markdown disokong pembekal MCP:

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

Bentuk panggilan alat imej MCP:

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

Terjemahan repositori adalah uji kering secara lalai melalui MCP:

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

- Anda mahu aliran kerja terjemahan berbahasa semula jadi dalam agen atau penyunting.
- Anda mahu terjemahan Markdown atau notebook di mana model agen hos menterjemah bahagian yang telah disediakan.
- Anda mahu agen menterjemah kandungan terpilih dan bukannya keseluruhan repositori.
- Anda mahukan langkah kelulusan sebelum penulisan meliputi seluruh repositori.
- Anda mahu satu antara muka yang mendedahkan alat untuk Markdown, notebook, imej, semakan, dan penulisan semula laluan.

## Bagaimana Mereka Bersesuaian

CLI adalah pilihan lalai terbaik untuk manusia yang menterjemah repositori. API Python terbaik apabila kod anda memiliki aliran kerja. Pelayan MCP terbaik apabila agen atau penyunting memiliki aliran kerja.

Ketiga-tiga laluan menggunakan API awam Co-op Translator yang sama, jadi anda boleh mula dengan CLI, mengautomasikan dengan Python kemudian, dan mendedahkan keupayaan yang sama kepada klien MCP apabila anda memerlukan aliran kerja dipacu agen.