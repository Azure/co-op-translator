# API Python

API publik stabil Python diekspor dari `co_op_translator.api`. Sebagian besar integrasi menggunakan salah satu alur kerja ini:

| Skenario | Gunakan ini ketika | API Utama |
| --- | --- | --- |
| Menerjemahkan berkas atau dokumen individual | Aplikasi Anda membaca konten sumber, memanggil Co-op Translator untuk terjemahan, dan menentukan di mana menyimpan hasilnya. | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Mempersiapkan konten untuk terjemahan oleh host-agent | Host MCP Anda atau model aplikasi akan menerjemahkan potongan, sementara Co-op Translator menangani pemecahan dan rekonstruksi. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Menerjemahkan seluruh repositori | Anda ingin API Python berperilaku seperti CLI dan menangani penemuan, jalur keluaran, metadata, pembersihan, dan penulisan. | `run_translation` |

Sebagian besar modul tingkat rendah di bawah `core`, `config`, `review`, dan `utils` adalah rincian implementasi yang digunakan oleh titik masuk API ini.

Klien MCP menggunakan API publik yang sama melalui [MCP Server](mcp.md). Gunakan halaman ini saat memanggil Python secara langsung, dan panduan MCP saat mengekspos Co-op Translator ke agen atau editor. Jika Anda sedang memutuskan antara CLI, Python API, dan MCP, mulailah dengan [Choose Your Workflow](workflows.md).

## Alur API Pertama Kali

Mulai di sini jika Anda memanggil Co-op Translator dari kode Python:

1. Konfigurasikan penyedia LLM seperti yang dijelaskan di [Configuration](configuration.md), kecuali Anda hanya menyiapkan potongan Markdown atau notebook untuk terjemahan host-agent.
2. Tentukan apakah aplikasi Anda yang menangani I/O berkas.
3. Gunakan API konten ketika aplikasi Anda membaca dan menulis berkas individual.
4. Gunakan `run_translation` ketika Co-op Translator harus memproses repositori seperti CLI.
5. Gunakan `run_review` setelah terjemahan jika Anda memerlukan pemeriksaan deterministik dalam otomasi.

| Tujuan | API untuk memulai |
| --- | --- |
| Menerjemahkan satu string atau berkas Markdown | `translate_markdown_content` |
| Menerjemahkan satu payload notebook | `translate_notebook_content` |
| Menerjemahkan satu gambar | `translate_image_content` |
| Membiarkan agen host menerjemahkan potongan Markdown atau notebook | `start_markdown_agent_translation` atau `start_notebook_agent_translation` |
| Menulis ulang tautan yang diterjemahkan setelah memilih jalur keluaran | `rewrite_markdown_paths` atau `rewrite_notebook_paths` |
| Menerjemahkan seluruh repositori | `run_translation` |
| Meninjau output terjemahan | `run_review` |

## Skenario 1: Menerjemahkan Berkas atau Dokumen Individual

Gunakan alur kerja ini ketika Anda sudah memiliki berkas, buffer editor, payload notebook, permintaan MCP, atau input pipeline kustom. Kode Anda menangani I/O berkas:

1. Baca konten sumber.
2. Panggil API terjemahan konten.
3. Opsional: panggil API penulisan ulang jalur jika konten yang diterjemahkan akan ditulis ke folder terjemahan proyek.
4. Simpan atau kembalikan hasil dari aplikasi Anda.

API terjemahan konten tidak menjalankan penemuan proyek, tidak menulis metadata, tidak menambahkan penyangkalan, dan tidak menulis ulang tautan secara otomatis.

### Berkas Markdown

```python
import asyncio
from pathlib import Path

from co_op_translator.api import (
    rewrite_markdown_paths,
    translate_markdown_content,
)


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
        policy={
            "language_code": "ko",
            "root_dir": ".",
            "translations_dir": "translations",
            "translated_images_dir": "translated_images",
            "translation_types": ["markdown", "images"],
        },
    )

    target_path.parent.mkdir(parents=True, exist_ok=True)
    target_path.write_text(rewritten, encoding="utf-8")


asyncio.run(main())
```

Jika Markdown yang diterjemahkan tidak akan berada dalam tata letak proyek Co-op Translator, lewati `rewrite_markdown_paths` dan simpan string yang diterjemahkan secara langsung.

### Berkas Notebook

```python
import asyncio
from pathlib import Path

from co_op_translator.api import (
    rewrite_notebook_paths,
    translate_notebook_content,
)


async def main() -> None:
    source_path = Path("docs/tutorial.ipynb")
    target_path = Path("translations/ja/docs/tutorial.ipynb")

    translated_json = await translate_notebook_content(
        source_path.read_text(encoding="utf-8"),
        "ja",
        {"source_path": source_path},
    )

    rewritten_json = rewrite_notebook_paths(
        translated_json,
        source_path=source_path,
        target_path=target_path,
        policy={
            "language_code": "ja",
            "root_dir": ".",
            "translations_dir": "translations",
            "translated_images_dir": "translated_images",
            "translation_types": ["notebook", "images"],
        },
    )

    target_path.parent.mkdir(parents=True, exist_ok=True)
    target_path.write_text(rewritten_json, encoding="utf-8")


asyncio.run(main())
```

`translate_notebook_content` menerjemahkan sel Markdown dan mempertahankan sel non-Markdown. Penulisan ulang jalur hanya diterapkan pada sel Markdown.

### Berkas Gambar

```python
from pathlib import Path

from co_op_translator.api import translate_image_content

source_path = Path("docs/images/hero.png")
target_path = Path("translated_images/fr/hero.png")

translated_image = translate_image_content(
    source_path,
    "fr",
    {
        "root_dir": ".",
        "fast_mode": False,
    },
)

target_path.parent.mkdir(parents=True, exist_ok=True)
translated_image.save(target_path)
```

`translate_image_content` membaca gambar sumber dan mengembalikan `PIL.Image.Image` yang dirender. Ini tidak menulis metadata gambar yang diterjemahkan.

## Skenario 2: Menerjemahkan Seluruh Repositori

Gunakan alur kerja ini ketika Anda ingin API Python berperilaku seperti CLI `translate`. `run_translation` menemukan berkas yang didukung, menerjemahkan jenis konten yang dipilih, menulis ulang jalur, menulis berkas keluaran, memperbarui metadata, dan melakukan tugas pemeliharaan terjemahan seperti pembersihan.

`run_translation` adalah titik masuk orkestrasi proyek yang direkomendasikan. `translate_project` diekspor sebagai alias kompatibilitas dengan perilaku yang sama.

Menerjemahkan berkas Markdown dalam repositori saat ini ke dalam Korean dan Japanese:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    markdown=True,
)
```

Menerjemahkan hanya notebook dari root proyek tertentu:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="fr",
    root_dir="./my-course",
    notebook=True,
)
```

Pratinjau volume terjemahan tanpa menulis berkas:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="es de",
    root_dir="./my-course",
    markdown=True,
    dry_run=True,
)
```

Menerjemahkan beberapa root konten dalam satu panggilan:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    root_dirs=["./docs", "./labs"],
)
```

Menulis terjemahan ke dalam grup keluaran eksplisit:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ja",
    markdown=True,
    groups=[
        ("./course-a", "./localized/course-a"),
        ("./course-b", "./localized/course-b"),
    ],
)
```

Gunakan placeholder per-bahasa ketika setiap bahasa harus berisi subdirektori bertingkat:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    groups=[
        ("./course", "./translations/<lang>/course"),
    ],
)
```

Jika tidak ada `markdown`, `notebook`, atau `images` yang disetel, API menerjemahkan semua jenis yang didukung: Markdown, notebook, dan gambar.

## Meninjau Output Terjemahan

`run_review` menjalankan pemeriksaan terjemahan deterministik tanpa kredensial LLM atau Vision.

!!! note "Beta"
    `run_review` adalah API tinjauan deterministik beta. Ia tidak memanggil penyedia model atau menulis berkas, tetapi pemeriksaan dan skema issue dapat berkembang.

```python
from co_op_translator.api import run_review

run_review(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
)
```

Tinjau hanya berkas yang berubah dibandingkan ref dasar dan cetak output bergaya GitHub:

```python
from co_op_translator.api import run_review

run_review(
    language_codes="ko",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
    changed_from="origin/main",
    output_format="github",
)
```

## Contoh Salin-Tempel API

Menerjemahkan konten Markdown tanpa penulisan berkas:

```python
import asyncio

from co_op_translator.api import translate_markdown_content


async def main() -> None:
    translated = await translate_markdown_content(
        "# Hello\n\nWelcome to the course.",
        "ko",
    )
    print(translated)


asyncio.run(main())
```

Menerjemahkan dan menulis ulang tautan Markdown:

```python
import asyncio

from co_op_translator.api import rewrite_markdown_paths, translate_markdown_content


async def main() -> None:
    translated = await translate_markdown_content(
        "[Setup](../setup.md)\n\n![Hero](../../images/hero.png)",
        "ko",
        {"source_path": "docs/guide.md"},
    )
    rewritten = rewrite_markdown_paths(
        translated,
        source_path="docs/guide.md",
        target_path="translations/ko/docs/guide.md",
        policy={
            "language_code": "ko",
            "root_dir": ".",
            "translations_dir": "translations",
            "translated_images_dir": "translated_images",
            "translation_types": ["markdown", "images"],
        },
    )
    print(rewritten)


asyncio.run(main())
```

Menerjemahkan sebuah repositori dari Python:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    root_dir="./course",
    markdown=True,
    yes=True,
)
```

Menerjemahkan beberapa root:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    root_dirs=[
        "./docs",
        "./labs",
    ],
)
```

Mempertahankan istilah glosarium:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="fr",
    markdown=True,
    glossaries=[
        "Co-op Translator",
        "Azure AI Foundry",
        "GitHub Actions",
    ],
)
```

## Titik Masuk Publik

```python
from co_op_translator.api import (
    ImageTranslationOptions,
    MarkdownTranslationOptions,
    NotebookTranslationOptions,
    finish_markdown_agent_translation,
    finish_notebook_agent_translation,
    run_review,
    run_translation,
    rewrite_markdown_paths,
    rewrite_notebook_paths,
    start_markdown_agent_translation,
    start_notebook_agent_translation,
    translate_image_content,
    translate_markdown_content,
    translate_notebook_content,
    translate_project,
)
```

::: co_op_translator.api.translate_markdown_content

::: co_op_translator.api.translate_notebook_content

::: co_op_translator.api.translate_image_content

::: co_op_translator.api.start_markdown_agent_translation

::: co_op_translator.api.finish_markdown_agent_translation

::: co_op_translator.api.start_notebook_agent_translation

::: co_op_translator.api.finish_notebook_agent_translation

::: co_op_translator.api.rewrite_markdown_paths

::: co_op_translator.api.rewrite_notebook_paths

::: co_op_translator.api.MarkdownTranslationOptions

::: co_op_translator.api.NotebookTranslationOptions

::: co_op_translator.api.ImageTranslationOptions

::: co_op_translator.api.run_translation

::: co_op_translator.api.translate_project

::: co_op_translator.api.run_review

## API Penerjemahan Konten

API penerjemahan konten ditujukan untuk integrasi yang sudah memiliki konten dalam memori, seperti ekstensi editor, alat MCP, pemroses notebook, atau pipeline kustom.

| Fungsi | Input | Output | I/O Berkas | Catatan |
| --- | --- | --- | --- | --- |
| `translate_markdown_content` | Markdown `str` | Markdown `str` | Tidak | Async. Menerjemahkan konten Markdown saja. Ini tidak menulis ulang tautan, menulis metadata, atau menambahkan penyangkalan. |
| `translate_notebook_content` | Notebook JSON `str` atau `dict` | Notebook JSON `str` | Tidak | Async. Menerjemahkan sel Markdown dan mempertahankan sel non-Markdown. Ini tidak menulis ulang tautan, menulis metadata, atau menambahkan penyangkalan. |
| `translate_image_content` | Image path | `PIL.Image.Image` | Membaca gambar sumber saja | Sinkron. Mengekstrak dan menerjemahkan teks gambar, lalu mengembalikan gambar yang dirender. Ini tidak menyimpan metadata gambar yang diterjemahkan. |

`translate_markdown_content` dan `translate_notebook_content` menerima `source_path` opsional melalui opsi mereka. Jalur tersebut diteruskan sebagai konteks ke penerjemah; pemanggil tetap bertanggung jawab atas penulisan ulang jalur spesifik proyek setelah terjemahan.

```python
from co_op_translator.api import MarkdownTranslationOptions, translate_markdown_content

translated = await translate_markdown_content(
    document,
    "ko",
    MarkdownTranslationOptions(source_path="docs/guide.md"),
)
```

Pilihan yang sama dapat diteruskan sebagai kamus:

```python
translated = await translate_markdown_content(
    document,
    "ko",
    {"source_path": "docs/guide.md"},
)
```

## API Terjemahan dengan Bantuan Agen

API berbantuan agen tidak memanggil Azure OpenAI atau OpenAI dari Co-op Translator. Mereka menyiapkan potongan Markdown atau notebook untuk diterjemahkan oleh agen host, kemudian merekonstruksi konten akhir dari potongan yang diterjemahkan.

| Fungsi | Tujuan |
| --- | --- |
| `start_markdown_agent_translation` | Mengembalikan pekerjaan Markdown yang berdiri sendiri dengan potongan, prompt, dan status rekonstruksi. |
| `finish_markdown_agent_translation` | Merekonstuksi Markdown dari sebuah job dan potongan yang diterjemahkan oleh agen host. |
| `start_notebook_agent_translation` | Mengembalikan job notebook dengan potongan sel-Markdown untuk terjemahan agen host. |
| `finish_notebook_agent_translation` | Merekonstuksi JSON notebook sambil mempertahankan sel kode, output, dan metadata. |

Alur kerja ini terutama ditujukan untuk host MCP. Jika Anda memerlukan terjemahan repositori produksi dengan Co-op Translator yang mengelola panggilan penyedia, gunakan `translate_markdown_content`, `translate_notebook_content`, atau `run_translation`.

## API Penulisan Ulang Jalur

API penulisan ulang jalur tidak melakukan terjemahan. Mereka memperbarui tautan dan jalur frontmatter setelah pemanggil mengetahui jalur sumber, jalur target yang diterjemahkan, dan tata letak proyek.

| Fungsi | Ruang Lingkup | Catatan |
| --- | --- | --- |
| `rewrite_markdown_paths` | Body Markdown dan frontmatter | Menulis ulang tautan Markdown dan field path frontmatter yang didukung untuk target yang diterjemahkan. |
| `rewrite_notebook_paths` | Sel Markdown dalam JSON notebook | Menerapkan penulisan ulang jalur Markdown ke setiap sel Markdown dan membiarkan sel non-Markdown tidak berubah. |

Argumen `policy` dapat berupa kamus dengan field-field ini:

| Field | Wajib | Tujuan |
| --- | --- | --- |
| `language_code` | Ya | Kode bahasa target, seperti `"ko"` atau `"pt-BR"`. |
| `root_dir` | Tidak | Root proyek sumber. Default ke `"."`. |
| `translations_dir` | Tidak | Direktori keluaran terjemahan teks. Default ke `translations` di bawah `root_dir`. |
| `translated_images_dir` | Tidak | Direktori keluaran gambar yang diterjemahkan. Default ke `translated_images` di bawah `root_dir`. |
| `translation_types` | Tidak | Jenis terjemahan yang diaktifkan. Default ke Markdown, notebook, dan gambar. |
| `lang_subdir` | Tidak | Subdirektori opsional di bawah setiap folder bahasa. |

## Parameter Terjemahan Proyek

| Parameter | Tipe | Default | Tujuan |
| --- | --- | --- | --- |
| `language_codes` | `str` | Required | Kode bahasa target yang dipisahkan spasi, seperti `"ko ja fr"`, atau `"all"`. Alias kode dinormalisasi ke nilai BCP 47 kanonik. |
| `root_dir` | `str` | `"."` | Root proyek untuk satu target terjemahan. Diabaikan ketika `root_dirs` atau `groups` disediakan. |
| `update` | `bool` | `False` | Menghapus dan membuat ulang terjemahan yang ada untuk bahasa yang dipilih. |
| `images` | `bool` | `False` | Sertakan terjemahan gambar. Memerlukan konfigurasi Azure AI Vision. |
| `markdown` | `bool` | `False` | Sertakan terjemahan Markdown. |
| `notebook` | `bool` | `False` | Sertakan terjemahan Jupyter notebook. |
| `debug` | `bool` | `False` | Aktifkan logging debug. |
| `save_logs` | `bool` | `False` | Simpan berkas log level DEBUG di bawah direktori `logs/` root. |
| `yes` | `bool` | `True` | Konfirmasi otomatis prompt untuk penggunaan programatik dan CI. |
| `add_disclaimer` | `bool` | `False` | Tambahkan penyangkalan terjemahan mesin ke Markdown dan notebook yang diterjemahkan. |
| `translations_dir` | `str \| None` | `None` | Direktori keluaran terjemahan teks kustom. Path relatif diselesaikan terhadap setiap root. |
| `image_dir` | `str \| None` | `None` | Direktori keluaran gambar yang diterjemahkan kustom. Path relatif diselesaikan terhadap setiap root. |
| `root_dirs` | `Iterable[str] \| None` | `None` | Beberapa root yang berbagi pengaturan keluaran yang sama. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | Pasangan eksplisit `(root_dir, translations_dir)`. Memiliki prioritas atas `root_dirs`. |
| `repo_url` | `str \| None` | `None` | URL repositori yang digunakan saat merender panduan tabel bahasa README. |
| `glossaries` | `Iterable[str] \| None` | `None` | Istilah glosarium yang dipertahankan selama terjemahan. Duplikasi dan istilah kosong dinormalisasi. |
| `dry_run` | `bool` | `False` | Perkirakan volume terjemahan dan pratinjau perilaku migrasi tanpa menulis berkas. |

## Parameter Review

`run_review` sengaja mencerminkan tanda tangan `run_translation` bila memungkinkan sehingga otomasi dapat beralih antara alur kerja terjemahan dan review dengan cabang minimal.

| Parameter | Tipe | Default | Tujuan |
| --- | --- | --- | --- |
| `language_codes` | `str \| Iterable[str]` | `"all"` | Folder bahasa target untuk ditinjau. String yang dipisahkan spasi dan iterable diterima. `"all"` meninjau setiap bahasa terjemahan yang ditemukan. |
| `root_dir` | `str` | `"."` | Root proyek untuk satu target review. Diabaikan ketika `root_dirs` atau `groups` disediakan. |
| `markdown` | `bool` | `False` | Sertakan berkas sumber Markdown dan MDX. |
| `notebook` | `bool` | `False` | Sertakan berkas sumber Jupyter notebook. |
| `images` | `bool` | `False` | Cadangan untuk kesetaraan dengan opsi terjemahan. Referensi tautan ke gambar diperiksa dari Markdown. |
| `translations_dir` | `str \| None` | `None` | Direktori keluaran terjemahan teks kustom. Jalur relatif diselesaikan terhadap setiap root. |
| `root_dirs` | `Iterable[str] \| None` | `None` | Beberapa root yang berbagi pengaturan keluaran yang sama. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | Pasangan eksplisit `(root_dir, translations_dir)`. Memiliki prioritas dibandingkan `root_dirs`. |
| `changed_from` | `str \| None` | `None` | Git ref yang digunakan untuk membatasi peninjauan ke berkas sumber yang berubah. |
| `output_format` | `str` | `"text"` | Format keluaran peninjauan. Nilai yang didukung adalah `"text"` dan `"github"`. |
| `fail_on_warnings` | `bool` | `False` | Perlakukan peringatan sebagai kegagalan selain kesalahan. |
| `debug` | `bool` | `False` | Aktifkan logging debug. |
| `save_logs` | `bool` | `False` | Simpan berkas log level DEBUG di bawah direktori root `logs/`. |

Jika tidak ada `markdown`, `notebook`, atau `images` yang disetel, API meninjau Markdown, notebook, dan referensi tautan gambar jika berlaku. Peninjauan tidak memanggil penyedia LLM dan tidak memerlukan kunci API.

## Persyaratan Konfigurasi

API terjemahan berbasis penyedia memerlukan konfigurasi penyedia sebelum menerjemahkan:

- Terjemahan Markdown dan notebook memerlukan penyedia LLM. Konfigurasikan salah satu Azure OpenAI atau OpenAI.
- Terjemahan gambar memerlukan Azure AI Vision selain penyedia LLM.
- `run_translation` menjalankan pemeriksaan konektivitas ringan sebelum penerjemahan proyek dimulai.
- API berbasiskan agen yang dibantu `start_*_agent_translation` dan `finish_*_agent_translation` tidak memanggil penyedia LLM Co-op Translator. Aplikasi host atau agen MCP menerjemahkan potongan yang telah disiapkan.
- `rewrite_markdown_paths`, `rewrite_notebook_paths`, dan `run_review` bersifat deterministik dan tidak memerlukan kredensial penyedia.

Required Azure OpenAI variables:

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Required OpenAI variables:

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

Required Azure AI Vision variables for image translation:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

`run_review` bersifat deterministik dan tidak memerlukan konfigurasi Azure OpenAI, OpenAI, atau Azure AI Vision.

## Catatan Perilaku

- API terjemahan konten memisahkan terjemahan dari penulisan ulang jalur proyek. Panggil `rewrite_markdown_paths` atau `rewrite_notebook_paths` secara eksplisit ketika konten yang diterjemahkan perlu menyesuaikan tautan relatif proyek untuk lokasi target.
- API orkestrasi proyek menambahkan perilaku proyek di sekitar terjemahan konten, termasuk penemuan berkas, penulisan, penulisan ulang jalur, metadata, pembersihan, dan penyangkalan opsional.
- `run_translation` mencetak ringkasan kemajuan dan estimasi melalui Click, menyesuaikan pengalaman pengguna CLI.
- `dry_run=True` menghitung estimasi menggunakan pembaruan README virtual, tetapi tidak menulis README atau berkas terjemahan.
- `groups` diproses secara berurutan. Satu estimasi agregat dicetak sebelum pekerjaan dimulai.
- Ketika terjemahan gambar dipilih, konfigurasi Vision yang hilang akan memicu kesalahan sebelum terjemahan dimulai.
- Folder bahasa berbasis alias yang ada terdeteksi dan dapat dimigrasikan ke nama folder bahasa BCP 47 kanonik sebagai bagian dari proses.
- `run_review` gagal jika berkas terjemahan hilang, metadata terjemahan hilang atau usang, frontmatter/fence kode Markdown yang rusak, dan JSON notebook terjemahan yang tidak valid.
- `run_review` melaporkan target tautan Markdown lokal dan gambar yang hilang sebagai peringatan secara default.

## Jalur Panggilan Internal

API mendelegasikan ke implementasi inti yang sama yang digunakan oleh CLI:

Terjemahan:

1. `co_op_translator.api.translation.translate_markdown_content`, `translate_notebook_content`, or `translate_image_content` untuk terjemahan in-memory.
2. `co_op_translator.api.translation.rewrite_markdown_paths` atau `rewrite_notebook_paths` untuk pemrosesan jalur pasca-eksplicit.
3. `co_op_translator.api.translation.run_translation` untuk orkestrasi proyek penuh.
4. `co_op_translator.config.Config`, `LLMConfig`, dan `VisionConfig`.
5. `co_op_translator.core.project.ProjectTranslator`.
6. `co_op_translator.core.project.TranslationManager`.
7. Mixin orkestrasi terfokus proyek untuk Markdown, notebook, dan gambar.
8. Penerjemah Markdown, notebook, teks, dan gambar di bawah `co_op_translator.core`.

Tinjauan:

1. `co_op_translator.api.review.run_review`
2. `co_op_translator.review.targets.build_review_targets`
3. `co_op_translator.review.runner.ReviewRunner`
4. Pemeriksaan deterministik di bawah `co_op_translator.review.checks`

Kelas berikut berguna bagi pemelihara, tetapi tidak diekspor sebagai API stabil tingkat paket.

| Kelas | Modul | Tanggung Jawab |
| --- | --- | --- |
| `ProjectTranslator` | `co_op_translator.core.project.project_translator` | Mengoordinasikan terjemahan tingkat proyek, manajemen direktori, normalisasi metadata per-bahasa, dan pendelegasian ke penerjemah Markdown, notebook, dan gambar. |
| `TranslationManager` | `co_op_translator.core.project.translation` | Melakukan pekerjaan pemrosesan berkas async untuk Markdown, notebook, gambar, deteksi usang, dan pembaruan metadata terjemahan. |
| `ProjectMarkdownTranslationMixin` | `co_op_translator.core.project.translation.project_markdown_translation` | Mengorkestrasi pembacaan berkas Markdown, terjemahan konten, penulisan ulang jalur, metadata, penyangkalan, dan penulisan berkas. |
| `ProjectNotebookTranslationMixin` | `co_op_translator.core.project.translation.project_notebook_translation` | Mengorkestrasi pembacaan berkas notebook, terjemahan sel Markdown, penulisan ulang jalur, metadata, penyangkalan, dan penulisan berkas. |
| `ProjectImageTranslationMixin` | `co_op_translator.core.project.translation.project_image_translation` | Mengorkestrasi penemuan gambar sumber, terjemahan gambar, jalur keluaran, metadata, dan penulisan berkas. |
| `ProjectEvaluator` | `co_op_translator.core.project.project_evaluator` | Menemukan pasangan Markdown terjemahan, mengevaluasi kualitas terjemahan, dan membaca metadata kepercayaan untuk alur kerja perbaikan dengan kepercayaan rendah. |
| `ReviewRunner` | `co_op_translator.review.runner` | Mengoordinasikan pemeriksaan deterministik di seluruh berkas sumber, bahasa target, dan root terjemahan yang dikonfigurasi. |
| `ReviewTarget` | `co_op_translator.review.targets` | Mendeskripsikan root sumber dan direktori keluaran terjemahan yang ditinjau untuk root tersebut. |
| `LanguageFolderMigrator` | `co_op_translator.core.project.language_migrator` | Mendeteksi folder bahasa alias warisan dan menyiapkan rencana migrasi folder kanonik BCP 47. |
| `Config` | `co_op_translator.config.base_config` | Memuat berkas `.env` dan memeriksa apakah penyedia LLM yang diperlukan dan Vision opsional dikonfigurasi. |
| `LLMConfig` | `co_op_translator.config.llm_config.config` | Mendeteksi otomatis Azure OpenAI atau OpenAI, memvalidasi variabel lingkungan yang diperlukan, dan menjalankan pemeriksaan konektivitas penyedia. |
| `VisionConfig` | `co_op_translator.config.vision_config.config` | Mendeteksi konfigurasi Azure AI Vision dan menjalankan pemeriksaan konektivitas untuk terjemahan gambar. |