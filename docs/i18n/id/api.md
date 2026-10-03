# API Python

API Python publik yang stabil diekspor dari `co_op_translator.api`. Sebagian besar integrasi menggunakan salah satu alur kerja berikut:

| Skenario | Gunakan ini ketika | API Utama |
| --- | --- | --- |
| Menerjemahkan file atau dokumen individual | Aplikasi Anda membaca konten sumber, memanggil Co-op Translator untuk penerjemahan, dan menentukan tempat menyimpan hasil. | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Mempersiapkan konten untuk penerjemahan oleh agen host | Host MCP atau model aplikasi Anda akan menerjemahkan potongan-potongan, sementara Co-op Translator menangani pemotongan dan rekonstruksi. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Menerjemahkan seluruh repositori | Anda ingin API Python berperilaku seperti CLI dan menangani penemuan berkas, jalur keluaran, metadata, pembersihan, dan penulisan. | `run_translation` |

Sebagian besar modul tingkat rendah di bawah `core`, `config`, `review`, dan `utils` adalah rincian implementasi yang digunakan oleh titik masuk API ini.

Klien MCP menggunakan API publik yang sama melalui [MCP Server](mcp.md). Gunakan halaman ini saat memanggil Python secara langsung, dan panduan MCP saat mengekspos Co-op Translator ke agen atau editor. Jika Anda memutuskan antara CLI, API Python, dan MCP, mulailah dengan [Pilih Alur Kerja Anda](workflows.md).

## Alur API untuk Pertama Kali

Mulai di sini jika Anda memanggil Co-op Translator dari kode Python:

1. Konfigurasikan penyedia LLM seperti dijelaskan di [Konfigurasi](configuration.md), kecuali Anda hanya menyiapkan potongan Markdown atau notebook untuk penerjemahan oleh agen host.
2. Tentukan apakah aplikasi Anda bertanggung jawab atas I/O berkas.
3. Gunakan API konten ketika aplikasi Anda membaca dan menulis berkas individual.
4. Gunakan `run_translation` ketika Co-op Translator harus memproses repositori seperti CLI.
5. Gunakan `run_review` setelah penerjemahan jika Anda memerlukan pemeriksaan deterministik dalam otomasi.

| Tujuan | API untuk memulai |
| --- | --- |
| Menerjemahkan satu string atau berkas Markdown | `translate_markdown_content` |
| Menerjemahkan satu payload notebook | `translate_notebook_content` |
| Menerjemahkan satu gambar | `translate_image_content` |
| Biarkan agen host menerjemahkan potongan Markdown atau notebook | `start_markdown_agent_translation` atau `start_notebook_agent_translation` |
| Menulis ulang tautan terjemahan setelah memilih jalur keluaran | `rewrite_markdown_paths` atau `rewrite_notebook_paths` |
| Menerjemahkan seluruh repositori | `run_translation` |
| Meninjau keluaran terjemahan | `run_review` |

## Skenario 1: Menerjemahkan File atau Dokumen Individual

Gunakan alur kerja ini ketika Anda sudah memiliki berkas, buffer editor, payload notebook, permintaan MCP, atau input pipeline kustom. Kode Anda bertanggung jawab atas I/O berkas:

1. Baca konten sumber.
2. Panggil API penerjemahan konten.
3. Opsional: panggil API penulisan ulang jalur jika konten terjemahan akan ditulis ke folder terjemahan proyek.
4. Simpan atau kembalikan hasil dari aplikasi Anda.

API penerjemahan konten tidak menjalankan penemuan proyek, tidak menulis metadata, tidak menambahkan penyangkalan, dan tidak menulis ulang tautan secara otomatis.

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

Jika Markdown hasil terjemahan tidak akan berada dalam tata letak proyek Co-op Translator, lewati `rewrite_markdown_paths` dan simpan string terjemahan secara langsung.

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

`translate_image_content` membaca gambar sumber dan mengembalikan `PIL.Image.Image` yang telah dirender. Ia tidak menulis metadata gambar terjemahan.

## Skenario 2: Menerjemahkan Seluruh Repositori

Gunakan alur kerja ini ketika Anda ingin API Python berperilaku seperti CLI `translate`. `run_translation` menemukan berkas yang didukung, menerjemahkan tipe konten yang dipilih, menulis ulang jalur, menulis berkas keluaran, memperbarui metadata, dan melakukan tugas pemeliharaan penerjemahan seperti pembersihan.

`run_translation` adalah titik masuk orkestrasi proyek yang disarankan. `translate_project` diekspor sebagai alias kompatibilitas dengan perilaku yang sama.

Terjemahkan berkas Markdown di repositori saat ini ke dalam bahasa Korea dan Jepang:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    markdown=True,
)
```

Terjemahkan hanya notebook dari root proyek tertentu:

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

Catat peristiwa kemajuan terstruktur untuk sebuah integrasi:

```python
from co_op_translator.api import TranslationEvent, run_translation


def on_event(event: TranslationEvent) -> None:
    payload = event.to_dict()
    # Simpan payload di tabel job-event Anda atau alirkan ke UI Anda.


run_translation(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
    progress_callback=on_event,
)
```

Peristiwa menggunakan skema versi `co-op.translation.event.v1`. Integrasi harus
bergantung pada field yang stabil seperti `type` dan `stage_key`, bukan pada teks antarmuka manusia
konsol atau `stage_label`.

Terjemahkan beberapa root konten dalam satu panggilan:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    root_dirs=["./docs", "./labs"],
)
```

Tulis terjemahan ke dalam grup keluaran yang eksplisit:

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

Gunakan placeholder per-bahasa ketika setiap bahasa harus berisi subdirektori bersarang:

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

Jika tidak ada dari `markdown`, `notebook`, atau `images` yang diatur, API menerjemahkan semua tipe yang didukung: Markdown, notebook, dan gambar.

### Mempertahankan suntingan manusia yang diterima dengan penyedia status terjemahan

Secara default, Co-op Translator mempertahankan perilaku tingkat berkas saat ini: ketika sebuah
sumber Markdown kedaluwarsa, seluruh berkas terjemahan dihasilkan ulang. Integrasi yang dihosting
dapat secara opsional mengoper `TranslationStateProvider` untuk mempertahankan suntingan manusia
pada blok sumber yang tidak berubah.

Penyedia menyediakan pasangan sumber/target terakhir yang diterima dan merekam setiap
kandidat baru. Penerimaan tetap merupakan tanggung jawab integrasi—misalnya,
setelah pull request terjemahan digabungkan:

```python
from pathlib import Path

from co_op_translator.api import (
    TranslationBaseline,
    TranslationUpdate,
    run_translation,
)


class DatabaseTranslationState:
    def load_baseline(
        self,
        *,
        source_path: Path,
        translation_path: Path,
        language_code: str,
    ) -> TranslationBaseline | None:
        row = load_accepted_translation(
            source_path=source_path,
            translation_path=translation_path,
            language_code=language_code,
        )
        if row is None:
            return None
        return TranslationBaseline(
            source_text=row.source_text,
            target_text=row.target_text,
            revision=row.accepted_revision,
        )

    def record_candidate(
        self,
        *,
        source_path: Path,
        translation_path: Path,
        language_code: str,
        source_text: str,
        target_text: str,
        update: TranslationUpdate,
    ) -> None:
        save_translation_candidate(
            source_path=source_path,
            translation_path=translation_path,
            language_code=language_code,
            source_text=source_text,
            target_text=target_text,
            mode=update.mode,
            fallback_reason=update.fallback_reason,
        )


run_translation(
    language_codes="ko",
    root_dir="./course",
    markdown=True,
    translation_state_provider=DatabaseTranslationState(),
)
```

Untuk berkas Markdown dengan baseline yang diterima valid, Co-op Translator menyelaraskan
blok Markdown tingkat atas. Blok sumber yang tidak berubah menggunakan kembali blok terjemahan saat ini,
termasuk suntingan yang dibuat oleh manusia; blok sumber yang berubah atau ditambahkan dikirim
untuk penerjemahan; blok sumber yang dihapus dihapus. Jika penyelarasan tidak jelas,
struktur target berubah, terjemahan blok tidak valid, atau tidak ada baseline yang
tersedia, Co-op Translator dengan aman kembali ke jalur
terjemahan seluruh-berkas yang ada.

API ini menyimpan status terjemahan dokumen, bukan memori frase atau
segmen lintas-dokumen. Saat ini berlaku untuk proyek terjemahan Markdown.
Perilaku notebook dan gambar tidak berubah. Mengoper `update=True`
masih meminta regenerasi penuh.

Jika satu atau lebih berkas tidak dapat diterjemahkan, `run_translation` akan memunculkan
`RuntimeError` setelah alur kerja proyek selesai alih-alih melaporkan a
jalannya berhasil dengan keluaran yang hilang. Integrasi harus memperlakukan ini sebagai pekerjaan yang gagal
dan mempertahankan status terjemahan yang diterima sebelumnya.

## Meninjau Keluaran Terjemahan

`run_review` menjalankan pemeriksaan terjemahan deterministik tanpa kredensial LLM atau Vision.

!!! note "Beta"
    `run_review` adalah API review deterministik beta. Ia tidak memanggil penyedia model atau menulis berkas, tetapi skema pemeriksaan dan isu dapat berkembang.

```python
from co_op_translator.api import run_review

run_review(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
)
```

Setelah terjemahan hanya README, gunakan ruang lingkup yang sama untuk peninjauan:

```python
run_review(language_codes="ko", root_dir="./my-course", readme_only=True)
```

`readme_only=True` hanya meninjau `README.md` di bawah setiap root sumber yang dikonfigurasi,
termasuk `groups` kustom dan direktori keluaran. Dokumen lain dan README bersarang
dikecualikan. Hilangnya README sumber memunculkan `ValueError`; pemeriksaan
terjemahan yang gagal memunculkan `RuntimeError`.

Tinjau hanya berkas yang berubah terhadap base ref dan cetak keluaran bergaya GitHub:

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

## Contoh API untuk Salin-Tempel

Terjemahkan konten Markdown tanpa menulis berkas:

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

Terjemahkan dan tulis ulang tautan Markdown:

```python
import asyncio

from co_op_translator.api import rewrite_markdown_paths, translate_markdown_content


async def main() -> None:
    translated = await translate_markdown_content(
        "[Setup](../setup.md)\n\n![Hero](images/hero.png)",
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

Terjemahkan sebuah repositori dari Python:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    root_dir="./course",
    markdown=True,
    yes=True,
)
```

Terjemahkan beberapa root:

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

Pertahankan istilah glosarium:

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
    TranslationBaseline,
    TranslationStateProvider,
    TranslationUpdate,
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

::: co_op_translator.api.TranslationBaseline

::: co_op_translator.api.TranslationStateProvider

::: co_op_translator.api.TranslationUpdate

::: co_op_translator.api.run_translation

::: co_op_translator.api.translate_project

::: co_op_translator.api.run_review

## API Penerjemahan Konten

API penerjemahan konten ditujukan untuk integrasi yang sudah memiliki konten dalam memori, seperti ekstensi editor, alat MCP, pemroses notebook, atau pipeline kustom.

| Fungsi | Input | Output | I/O Berkas | Catatan |
| --- | --- | --- | --- | --- |
| `translate_markdown_content` | Markdown `str` | Markdown `str` | Tidak | Async. Menerjemahkan hanya konten Markdown. Ia tidak menulis ulang tautan, menulis metadata, atau menambahkan penyangkalan. |
| `translate_notebook_content` | Notebook JSON `str` atau `dict` | Notebook JSON `str` | Tidak | Async. Menerjemahkan sel Markdown dan mempertahankan sel non-Markdown. Ia tidak menulis ulang tautan, menulis metadata, atau menambahkan penyangkalan. |
| `translate_image_content` | Path gambar | `PIL.Image.Image` | Hanya membaca gambar sumber | Sinkron. Mengekstrak dan menerjemahkan teks gambar, lalu mengembalikan gambar yang dirender. Ia tidak menyimpan metadata gambar terjemahan. |

`translate_markdown_content` dan `translate_notebook_content` menerima `source_path` opsional melalui opsi mereka. Path tersebut diberikan sebagai konteks kepada penerjemah; pemanggil tetap bertanggung jawab atas penulisan ulang jalur spesifik proyek setelah penerjemahan.

```python
from co_op_translator.api import MarkdownTranslationOptions, translate_markdown_content

translated = await translate_markdown_content(
    document,
    "ko",
    MarkdownTranslationOptions(source_path="docs/guide.md"),
)
```

Opsi yang sama dapat diberikan sebagai kamus:

```python
translated = await translate_markdown_content(
    document,
    "ko",
    {"source_path": "docs/guide.md"},
)
```

## API Penerjemahan dengan Bantuan Agen

API yang dibantu agen tidak memanggil penyedia LLM yang dikonfigurasi dari Co-op Translator. Mereka menyiapkan potongan Markdown atau notebook untuk diterjemahkan oleh agen host, lalu merekonstruksi konten akhir dari potongan yang diterjemahkan.

| Fungsi | Tujuan |
| --- | --- |
| `start_markdown_agent_translation` | Mengembalikan pekerjaan Markdown yang mandiri dengan potongan, prompt, dan status rekonstruksi. |
| `finish_markdown_agent_translation` | Merekonstruksi Markdown dari sebuah job dan potongan yang diterjemahkan oleh agen host. |
| `start_notebook_agent_translation` | Mengembalikan job notebook dengan potongan sel Markdown untuk penerjemahan oleh agen host. |
| `finish_notebook_agent_translation` | Merekonstruksi JSON notebook sambil mempertahankan sel kode, output, dan metadata. |

Alur kerja ini terutama ditujukan untuk host MCP. Jika Anda memerlukan penerjemahan repositori produksi dengan Co-op Translator mengelola pemanggilan penyedia, gunakan `translate_markdown_content`, `translate_notebook_content`, atau `run_translation`.

## API Penulisan Ulang Jalur

API penulisan ulang jalur tidak melakukan penerjemahan. Mereka memperbarui tautan dan jalur frontmatter setelah pemanggil mengetahui path sumber, path target terjemahan, dan tata letak proyek.

| Fungsi | Ruang Lingkup | Catatan |
| --- | --- | --- |
| `rewrite_markdown_paths` | Isi Markdown dan frontmatter | Menulis ulang tautan Markdown dan field frontmatter jalur yang didukung untuk target terjemahan. |
| `rewrite_notebook_paths` | Sel Markdown dalam JSON notebook | Menerapkan penulisan ulang jalur Markdown ke setiap sel Markdown dan membiarkan sel non-Markdown tidak berubah. |

Argumen `policy` dapat berupa kamus dengan field-field berikut:

| Field | Diperlukan | Tujuan |
| --- | --- | --- |
| `language_code` | Ya | Kode bahasa target, seperti `"ko"` atau `"pt-BR"`. |
| `root_dir` | Tidak | Root proyek sumber. Default `"."`. |
| `translations_dir` | Tidak | Direktori keluaran terjemahan teks. Default ke `translations` di bawah `root_dir`. |
| `translated_images_dir` | Tidak | Direktori keluaran gambar terjemahan. Default ke `translated_images` di bawah `root_dir`. |
| `translation_types` | Tidak | Tipe terjemahan yang diaktifkan. Default ke Markdown, notebook, dan gambar. |
| `lang_subdir` | Tidak | Subdirektori opsional di bawah setiap folder bahasa. |

## Parameter Terjemahan Proyek

| Parameter | Tipe | Default | Tujuan |
| --- | --- | --- | --- |
| `language_codes` | `str` | Diperlukan | Kode bahasa target dipisahkan spasi, seperti `"ko ja fr"`, atau `"all"`. Kode alias dinormalisasi ke nilai BCP 47 kanonik. |
| `root_dir` | `str` | `"."` | Root proyek untuk satu target terjemahan. Diabaikan ketika `root_dirs` atau `groups` disediakan. |
| `update` | `bool` | `False` | Hapus dan buat ulang terjemahan yang ada untuk bahasa yang dipilih. |
| `images` | `bool` | `False` | Sertakan terjemahan gambar. Memerlukan konfigurasi Azure AI Vision. |
| `markdown` | `bool` | `False` | Sertakan terjemahan Markdown. |
| `notebook` | `bool` | `False` | Sertakan terjemahan Jupyter notebook. |
| `debug` | `bool` | `False` | Aktifkan logging debug. |
| `save_logs` | `bool` | `False` | Simpan berkas log tingkat DEBUG di bawah direktori root `logs/`. |
| `yes` | `bool` | `True` | Secara otomatis mengonfirmasi prompt untuk penggunaan programatik dan CI. |
| `add_disclaimer` | `bool` | `False` | Tambahkan penyangkalan terjemahan mesin ke Markdown dan notebook yang diterjemahkan. |
| `translations_dir` | `str \| None` | `None` | Direktori keluaran terjemahan teks khusus. Jalur relatif diselesaikan terhadap setiap root. |
| `image_dir` | `str \| None` | `None` | Direktori keluaran gambar terjemahan khusus. Jalur relatif diselesaikan terhadap setiap root. |
| `root_dirs` | `Iterable[str] \| None` | `None` | Beberapa root yang berbagi pengaturan keluaran yang sama. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | Pasangan `(root_dir, translations_dir)` eksplisit. Memiliki prioritas atas `root_dirs`. |
| `repo_url` | `str \| None` | `None` | URL repositori yang digunakan saat merender panduan tabel bahasa README. |
| `glossaries` | `Iterable[str] \| None` | `None` | Istilah glosarium yang dipertahankan selama terjemahan. Duplikat dan istilah kosong dinormalisasi. |
| `dry_run` | `bool` | `False` | Perkirakan volume terjemahan dan pratinjau perilaku migrasi tanpa menulis file. |
| `translation_state_provider` | `TranslationStateProvider \| None` | `None` | Adaptor persistensi opsional untuk accepted-baseline dan kandidat untuk pembaruan Markdown inkremental. Mengabaikannya mempertahankan perilaku file-penuh yang ada. |

## Parameter Tinjauan

`run_review` sengaja mencerminkan tanda tangan `run_translation` bila memungkinkan sehingga otomasi dapat beralih antara alur kerja terjemahan dan tinjauan dengan percabangan minimal.

| Parameter | Tipe | Default | Tujuan |
| --- | --- | --- | --- |
| `language_codes` | `str \| Iterable[str]` | `"all"` | Folder bahasa target untuk ditinjau. String yang dipisahkan spasi dan iterable diterima. `"all"` meninjau setiap bahasa terjemahan yang ditemukan. |
| `root_dir` | `str` | `"."` | Root proyek untuk satu target tinjauan. Diabaikan ketika `root_dirs` atau `groups` disediakan. |
| `markdown` | `bool` | `False` | Sertakan Markdown dan file sumber MDX. |
| `notebook` | `bool` | `False` | Sertakan file sumber notebook Jupyter. |
| `images` | `bool` | `False` | Dicadangkan untuk kesetaraan dengan opsi terjemahan. Referensi tautan ke gambar diperiksa dari Markdown. |
| `translations_dir` | `str \| None` | `None` | Direktori keluaran terjemahan teks khusus. Jalur relatif diselesaikan terhadap setiap root. |
| `root_dirs` | `Iterable[str] \| None` | `None` | Beberapa root yang berbagi pengaturan keluaran yang sama. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | Pasangan `(root_dir, translations_dir)` eksplisit. Memiliki prioritas atas `root_dirs`. |
| `changed_from` | `str \| None` | `None` | Ref Git yang digunakan untuk membatasi tinjauan ke file sumber yang diubah. |
| `readme_only` | `bool` | `False` | Hanya meninjau `README.md` di setiap sumber root. README sumber yang hilang memicu `ValueError`. |
| `output_format` | `str` | `"text"` | Format keluaran tinjauan. Nilai yang didukung adalah `"text"` dan `"github"`. |
| `fail_on_warnings` | `bool` | `False` | Perlakukan peringatan sebagai kegagalan selain kesalahan. |
| `debug` | `bool` | `False` | Aktifkan logging debug. |
| `save_logs` | `bool` | `False` | Simpan file log level DEBUG di bawah direktori root `logs/`. |

Jika tidak satu pun dari `markdown`, `notebook`, atau `images` disetel, API meninjau Markdown, notebook, dan referensi tautan gambar bila berlaku. Tinjauan tidak memanggil penyedia LLM dan tidak memerlukan kunci API.

## Persyaratan Konfigurasi

API terjemahan yang bergantung pada penyedia memerlukan konfigurasi penyedia sebelum menerjemahkan:

- Terjemahan Markdown dan notebook memerlukan penyedia LLM. Konfigurasikan Azure OpenAI, OpenAI, atau Anthropic.
- Terjemahan gambar memerlukan Azure AI Vision selain penyedia LLM.
- `run_translation` menjalankan pemeriksaan konektivitas ringan sebelum terjemahan proyek dimulai.
- API berasistensi agen `start_*_agent_translation` dan `finish_*_agent_translation` tidak memanggil penyedia LLM Co-op Translator. Aplikasi host atau agen MCP yang menerjemahkan potongan yang disiapkan.
- `rewrite_markdown_paths`, `rewrite_notebook_paths`, dan `run_review` bersifat deterministik dan tidak memerlukan kredensial penyedia.

Variabel Azure OpenAI yang diperlukan:

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Variabel OpenAI yang diperlukan:

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

Variabel Anthropic yang diperlukan:

```bash
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

`ANTHROPIC_BASE_URL` dan `ANTHROPIC_MAX_TOKENS` bersifat opsional. Microsoft Agent Framework adalah klien model default untuk semua penyedia mulai dari Co-op Translator 0.22.0. Semantic Kernel masih dapat dipilih sementara dengan `CO_OP_TRANSLATOR_MODEL_CLIENT="semantic-kernel"`, tetapi melakukan itu menghasilkan peringatan deprecasi; lihat [konfigurasi](configuration.md#model-client-backend) untuk rencana penghapusan bertahap.

Variabel Azure AI Vision yang diperlukan untuk terjemahan gambar:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

`run_review` bersifat deterministik dan tidak memerlukan konfigurasi LLM atau Azure AI Vision.

## Catatan Perilaku

- API terjemahan konten memisahkan terjemahan dari penulisan ulang jalur proyek. Panggil `rewrite_markdown_paths` atau `rewrite_notebook_paths` secara eksplisit ketika konten yang diterjemahkan membutuhkan penyesuaian tautan relatif terhadap proyek untuk lokasi target.
- API orkestrasi proyek menambahkan perilaku proyek seputar terjemahan konten, termasuk penemuan file, penulisan, penulisan ulang jalur, metadata, pembersihan, dan penyangkalan opsional.
- `run_translation` mencetak ringkasan kemajuan dan perkiraan melalui reporter berbasis Rich yang sama yang digunakan oleh CLI. Keluaran non-interaktif kembali ke teks biasa.
- `dry_run=True` menghitung perkiraan menggunakan pembaruan README virtual, tetapi tidak menulis README atau file terjemahan.
- `groups` diproses secara berurutan. Satu perkiraan agregat dicetak sebelum pekerjaan dimulai.
- Ketika terjemahan gambar dipilih, konfigurasi Vision yang hilang memicu kesalahan sebelum terjemahan dimulai.
- Folder bahasa berbasis alias yang ada terdeteksi dan dapat dimigrasikan ke nama folder bahasa kanonik sebagai bagian dari proses.
- `run_review` gagal pada file terjemahan yang hilang, metadata terjemahan yang hilang atau usang, frontmatter/fence kode Markdown yang rusak, dan JSON notebook terjemahan yang tidak valid.
- `run_review` melaporkan target tautan Markdown dan gambar lokal yang hilang sebagai peringatan secara default.

## Jalur Panggilan Internal

API mendelegasikan ke implementasi inti yang sama yang digunakan oleh CLI:

Terjemahan:

1. `co_op_translator.api.translation.translate_markdown_content`, `translate_notebook_content`, or `translate_image_content` for in-memory translation.
2. `co_op_translator.api.translation.rewrite_markdown_paths` or `rewrite_notebook_paths` for explicit path post-processing.
3. `co_op_translator.api.translation.run_translation` for full project orchestration.
4. `co_op_translator.config.Config`, `LLMConfig`, and `VisionConfig`.
5. `co_op_translator.core.project.ProjectTranslator`.
6. `co_op_translator.core.project.TranslationManager`.
7. Mixin terjemahan proyek yang terfokus untuk Markdown, notebook, dan gambar.
8. Penerjemah Markdown, notebook, teks, dan gambar di bawah `co_op_translator.core`.

Tinjauan:

1. `co_op_translator.api.review.run_review`
2. `co_op_translator.review.targets.build_review_targets`
3. `co_op_translator.review.runner.ReviewRunner`
4. Pemeriksaan deterministik di bawah `co_op_translator.review.checks`

Kelas-kelas berikut berguna bagi pemelihara, tetapi tidak diekspor sebagai API stabil tingkat paket.

| Kelas | Modul | Tanggung Jawab |
| --- | --- | --- |
| `ProjectTranslator` | `co_op_translator.core.project.project_translator` | Mengkoordinasikan terjemahan tingkat proyek, manajemen direktori, normalisasi metadata per-bahasa, dan delegasi ke penerjemah Markdown, notebook, dan gambar. |
| `TranslationManager` | `co_op_translator.core.project.translation` | Melakukan pekerjaan pemrosesan file asinkron untuk Markdown, notebook, gambar, deteksi usang, dan pembaruan metadata terjemahan. |
| `ProjectMarkdownTranslationMixin` | `co_op_translator.core.project.translation.project_markdown_translation` | Mengorkestrasi pembacaan file Markdown, terjemahan konten, penulisan ulang jalur, metadata, penyangkalan, dan penulisan. |
| `ProjectNotebookTranslationMixin` | `co_op_translator.core.project.translation.project_notebook_translation` | Mengorkestrasi pembacaan file notebook, terjemahan sel Markdown, penulisan ulang jalur, metadata, penyangkalan, dan penulisan. |
| `ProjectImageTranslationMixin` | `co_op_translator.core.project.translation.project_image_translation` | Mengorkestrasi penemuan gambar sumber, terjemahan gambar, jalur keluaran, metadata, dan penulisan. |
| `ProjectEvaluator` | `co_op_translator.core.project.project_evaluator` | Menemukan pasangan Markdown terjemahan, mengevaluasi kualitas terjemahan, dan membaca metadata tingkat kepercayaan untuk alur kerja perbaikan dengan kepercayaan rendah. |
| `ReviewRunner` | `co_op_translator.review.runner` | Mengkoordinasikan pemeriksaan tinjauan deterministik di seluruh file sumber, bahasa target, dan root terjemahan yang dikonfigurasi. |
| `ReviewTarget` | `co_op_translator.review.targets` | Menjelaskan sebuah root sumber dan direktori keluaran terjemahan yang ditinjau untuk root tersebut. |
| `LanguageFolderMigrator` | `co_op_translator.core.project.language_migrator` | Mendeteksi folder bahasa alias warisan dan menyiapkan rencana migrasi folder BCP 47 kanonik. |
| `Config` | `co_op_translator.config.base_config` | Memuat file `.env` dan memeriksa apakah penyedia LLM yang diperlukan dan Vision opsional dikonfigurasi. |
| `LLMConfig` | `co_op_translator.config.llm_config.config` | Mendeteksi otomatis Azure OpenAI, OpenAI, atau Anthropic, memvalidasi variabel lingkungan yang diperlukan, dan menjalankan pemeriksaan konektivitas penyedia. |
| `VisionConfig` | `co_op_translator.config.vision_config.config` | Mendeteksi konfigurasi Azure AI Vision dan menjalankan pemeriksaan konektivitas untuk terjemahan gambar. |