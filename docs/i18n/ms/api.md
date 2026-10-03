# API Python

API awam Python yang stabil dieksport daripada `co_op_translator.api`. Kebanyakan integrasi menggunakan salah satu aliran kerja ini:

| Senario | Gunakan ini apabila | API Utama |
| --- | --- | --- |
| Translate individual files or documents | Aplikasi anda membaca kandungan sumber, memanggil Co-op Translator untuk terjemahan, dan memutuskan di mana menyimpan hasilnya. | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Sediakan kandungan untuk penterjemahan hos ejen | Hos MCP anda atau model aplikasi akan menterjemah pecahan, manakala Co-op Translator mengendalikan pemecahan dan pembinaan semula. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Translate an entire repository | Anda mahu API Python berfungsi seperti CLI dan mengendalikan penemuan, laluan output, metadata, pembersihan, dan penulisan. | `run_translation` |

Kebanyakan modul aras rendah di bawah `core`, `config`, `review`, dan `utils` adalah butiran pelaksanaan yang digunakan oleh titik kemasukan API ini.

Klien MCP menggunakan API awam yang sama melalui [Pelayan MCP](mcp.md). Gunakan halaman ini apabila memanggil Python secara langsung, dan panduan MCP apabila mendedahkan Co-op Translator kepada ejen atau penyunting. Jika anda sedang memilih antara CLI, API Python, dan MCP, mulakan dengan [Pilih Aliran Kerja Anda](workflows.md).

## Aliran API Kali Pertama

Mulakan di sini jika anda memanggil Co-op Translator dari kod Python:

1. Konfigurasikan pembekal LLM seperti yang diterangkan dalam [Konfigurasi](configuration.md), melainkan anda hanya menyediakan potongan Markdown atau notebook untuk terjemahan hos-ejen.
2. Tentukan sama ada aplikasi anda memiliki I/O fail.
3. Gunakan API kandungan apabila aplikasi anda membaca dan menulis fail individu.
4. Gunakan `run_translation` apabila Co-op Translator sepatutnya memproses repositori seperti CLI.
5. Gunakan `run_review` selepas terjemahan jika anda memerlukan pemeriksaan deterministik dalam automasi.

| Matlamat | API untuk mula dengan |
| --- | --- |
| Terjemahkan satu rentetan atau fail Markdown | `translate_markdown_content` |
| Translate one notebook payload | `translate_notebook_content` |
| Translate one image | `translate_image_content` |
| Biarkan hos ejen menterjemah pecahan Markdown atau buku nota | `start_markdown_agent_translation` or `start_notebook_agent_translation` |
| Tulis semula pautan yang telah diterjemah selepas memilih laluan keluaran | `rewrite_markdown_paths` or `rewrite_notebook_paths` |
| Translate a full repository | `run_translation` |
| Review translated output | `run_review` |

## Senario 1: Terjemah Fail atau Dokumen Individu

Gunakan aliran kerja ini apabila anda sudah mempunyai fail, buffer editor, muatan notebook, permintaan MCP, atau input saluran tersuai. Kod anda mengendalikan I/O fail:

1. Baca kandungan sumber.
2. Panggil API terjemahan kandungan.
3. Secara pilihan panggil API penulisan semula laluan jika kandungan yang diterjemah akan ditulis ke dalam folder terjemahan projek.
4. Simpan atau pulangkan hasil daripada aplikasi anda.

API terjemahan kandungan tidak menjalankan penemuan projek, tidak menulis metadata, tidak menambah penafian, dan tidak menulis semula pautan secara automatik.

### Fail Markdown

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

Jika Markdown yang diterjemah tidak akan berada dalam susun atur projek Co-op Translator, langkau `rewrite_markdown_paths` dan simpan rentetan yang diterjemah secara terus.

### Fail Notebook

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

`translate_notebook_content` menterjemah sel Markdown dan mengekalkan sel bukan-Markdown. Penulisan semula laluan hanya digunakan pada sel Markdown.

### Fail Imej

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

`translate_image_content` membaca imej sumber dan mengembalikan `PIL.Image.Image` yang dirender. Ia tidak menulis metadata imej yang diterjemah.

## Senario 2: Terjemah Keseluruhan Repositori

Gunakan aliran kerja ini apabila anda mahu API Python berfungsi seperti CLI `translate`. `run_translation` menemui fail yang disokong, menterjemah jenis kandungan yang dipilih, menulis semula laluan, menulis fail output, mengemaskini metadata, dan menjalankan tugas penyelenggaraan terjemahan seperti pembersihan.

`run_translation` adalah titik kemasukan pengurusan projek yang disyorkan. `translate_project` dieksport sebagai alias keserasian dengan tingkah laku yang sama.

Terjemah fail Markdown dalam repositori semasa ke dalam bahasa Korea dan Jepun:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    markdown=True,
)
```

Terjemah hanya notebook dari akar projek tertentu:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="fr",
    root_dir="./my-course",
    notebook=True,
)
```

Pratonton jumlah terjemahan tanpa menulis fail:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="es de",
    root_dir="./my-course",
    markdown=True,
    dry_run=True,
)
```

Rakaman acara kemajuan berstruktur untuk satu integrasi:

```python
from co_op_translator.api import TranslationEvent, run_translation


def on_event(event: TranslationEvent) -> None:
    payload = event.to_dict()
    # Simpan muatan dalam jadual acara kerja anda atau alirkannya ke antara muka pengguna anda.


run_translation(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
    progress_callback=on_event,
)
```

Acara menggunakan skema berversi `co-op.translation.event.v1`. Integrasi harus
bergantung pada medan stabil seperti `type` dan `stage_key`, bukan pada teks yang ditujukan kepada manusia
konsol atau `stage_label`.

Terjemah berbilang akar kandungan dalam satu panggilan:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    root_dirs=["./docs", "./labs"],
)
```

Tulis terjemahan ke dalam kumpulan output yang jelas:

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

Gunakan tempat letak per-bahasa apabila setiap bahasa harus mengandungi subdirektori bersarang:

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

Jika tiada `markdown`, `notebook`, atau `images` disetkan, API akan menterjemah semua jenis yang disokong: Markdown, notebook, dan imej.

### Mengekalkan suntingan manusia yang diterima dengan pembekal keadaan terjemahan

Secara lalai, Co-op Translator mengekalkan tingkah laku aras-fail sedia ada: apabila sebuah
sumber Markdown menjadi lapuk, keseluruhan fail yang diterjemah dihasilkan semula. Integrasi yang dihoskan
boleh secara pilihan menghantar `TranslationStateProvider` untuk mengekalkan suntingan manusia
dalam blok sumber yang tidak berubah.

Penyedia menyediakan pasangan sumber/sasaran yang diterima terakhir dan merekod setiap calon baru
calon. Penerimaan kekal tanggungjawab integrasi—contohnya,
selepas permintaan tarik terjemahan digabungkan:

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

Untuk fail Markdown dengan garis asas penerimaan yang sah, Co-op Translator menyelaraskan
blok Markdown peringkat atas. Blok sumber yang tidak berubah menggunakan semula blok diterjemah semasa
tersebut, termasuk suntingan yang dibuat oleh manusia; blok sumber yang diubah atau ditambah dihantar
untuk terjemahan; blok sumber yang dipadam dikeluarkan. Jika penjajaran tidak jelas,
struktur sasaran berubah, terjemahan blok tidak sah, atau tiada garis asas
yang tersedia, Co-op Translator dengan selamat kembali kepada laluan terjemahan keseluruhan-fail sedia ada
laluan terjemahan.

API ini menyimpan keadaan terjemahan dokumen, bukan memori terjemahan frasa atau
segmen merentasi dokumen. Ia kini terpakai kepada terjemahan projek Markdown
. Tingkah laku notebook dan imej tidak berubah. Menghantar `update=True`
masih meminta penjanaan semula penuh.

Jika satu atau lebih fail tidak dapat diterjemahkan, `run_translation` membangkitkan sebuah
`RuntimeError` selepas aliran kerja projek selesai dan bukannya melaporkan sebuah
larian berjaya dengan output yang hilang. Integrasi harus menganggap ini sebagai kerja yang gagal
dan mengekalkan keadaan terjemahan yang diterima sebelum ini.

## Semak Output yang Diterjemah

`run_review` menjalankan pemeriksaan terjemahan deterministik tanpa kelayakan LLM atau Vision.

!!! note "Beta"
    `run_review` adalah API semakan deterministik beta. Ia tidak memanggil penyedia model atau menulis fail, tetapi skema pemeriksaan dan isu mungkin berubah.

```python
from co_op_translator.api import run_review

run_review(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
)
```

Selepas terjemahan hanya README, gunakan skop yang sama untuk semakan:

```python
run_review(language_codes="ko", root_dir="./my-course", readme_only=True)
```

`readme_only=True` hanya menyemak `README.md` di bawah setiap root sumber yang dikonfigurasi,
termasuk `groups` tersuai dan direktori keluaran. Dokumen lain dan README bersarang
README dikecualikan. Ketiadaan README sumber akan menaikkan `ValueError`; pemeriksaan yang gagal
pemeriksaan terjemahan akan menaikkan `RuntimeError`.

Semak hanya fail yang diubah berbanding ref asas dan cetak output bergaya GitHub:

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

## Contoh API Salin-Tampal

Terjemahkan kandungan Markdown tanpa menulis fail:

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

Terjemahkan dan tulis semula pautan Markdown:

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

Terjemahkan repositori dari Python:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    root_dir="./course",
    markdown=True,
    yes=True,
)
```

Terjemahkan berbilang root:

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

Mengekalkan istilah glosari:

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

## Titik Masuk Awam

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

## API Terjemahan Kandungan

API terjemahan kandungan bertujuan untuk integrasi yang sudah mempunyai kandungan dalam memori, seperti sambungan penyunting, alat MCP, pemproses notebook, atau saluran tersuai.

| Fungsi | Input | Output | I/O Fail | Nota |
| --- | --- | --- | --- | --- |
| `translate_markdown_content` | Markdown `str` | Markdown `str` | Tidak | Tak segerak. Menterjemah kandungan Markdown sahaja. Ia tidak menulis semula pautan, menulis metadata, atau menambah penafian. |
| `translate_notebook_content` | Notebook JSON `str` atau `dict` | Notebook JSON `str` | Tidak | Tak segerak. Menterjemah sel Markdown dan mengekalkan sel bukan-Markdown. Ia tidak menulis semula pautan, menulis metadata, atau menambah penafian. |
| `translate_image_content` | Laluan imej | `PIL.Image.Image` | Membaca imej sumber sahaja | Segerak. Mengekstrak dan menterjemah teks imej, kemudian mengembalikan imej terhasil. Ia tidak menyimpan metadata imej yang diterjemah. |

`translate_markdown_content` dan `translate_notebook_content` menerima `source_path` pilihan melalui opsyen mereka. Laluan itu dihantar sebagai konteks kepada penterjemah; pemanggil kekal bertanggungjawab untuk sebarang penulisan semula laluan khusus projek selepas terjemahan.

```python
from co_op_translator.api import MarkdownTranslationOptions, translate_markdown_content

translated = await translate_markdown_content(
    document,
    "ko",
    MarkdownTranslationOptions(source_path="docs/guide.md"),
)
```

Opsyen yang sama boleh dihantar sebagai kamus:

```python
translated = await translate_markdown_content(
    document,
    "ko",
    {"source_path": "docs/guide.md"},
)
```

## API Terjemahan dengan Bantuan Ejen

API yang dibantu ejen tidak memanggil penyedia LLM yang dikonfigurasi dari Co-op Translator. Mereka menyediakan bahagian Markdown atau notebook untuk ejen hos menterjemah, kemudian menyusun semula kandungan akhir daripada bahagian yang diterjemah.

| Fungsi | Tujuan |
| --- | --- |
| `start_markdown_agent_translation` | Mengembalikan kerja Markdown berdikari dengan bahagian, arahan (prompts), dan keadaan penyusunan semula. |
| `finish_markdown_agent_translation` | Menyusun semula Markdown daripada kerja dan bahagian yang diterjemah oleh ejen hos. |
| `start_notebook_agent_translation` | Mengembalikan kerja notebook dengan bahagian sel Markdown untuk terjemahan ejen hos. |
| `finish_notebook_agent_translation` | Menyusun semula JSON notebook sambil mengekalkan sel kod, output, dan metadata. |

Aliran kerja ini terutamanya bertujuan untuk hos MCP. Jika anda memerlukan terjemahan repositori produksi dengan Co-op Translator mengurus panggilan penyedia, gunakan `translate_markdown_content`, `translate_notebook_content`, atau `run_translation`.

## API Penulisan Semula Laluan

API penulisan semula laluan tidak melakukan terjemahan. Ia mengemas kini pautan dan laluan frontmatter selepas pemanggil mengetahui laluan sumber, laluan sasaran yang diterjemah, dan susun atur projek.

| Fungsi | Skop | Nota |
| --- | --- | --- |
| `rewrite_markdown_paths` | Badan Markdown dan frontmatter | Menulis semula pautan Markdown dan medan laluan frontmatter yang disokong untuk sasaran yang diterjemah. |
| `rewrite_notebook_paths` | Sel Markdown dalam JSON notebook | Menerapkan penulisan semula laluan Markdown kepada setiap sel Markdown dan membiarkan sel bukan-Markdown tidak berubah. |

Argumen `policy` mungkin sebuah kamus dengan medan-medan ini:

| Medan | Diperlukan | Tujuan |
| --- | --- | --- |
| `language_code` | Ya | Kod bahasa sasaran, seperti `"ko"` atau `"pt-BR"`. |
| `root_dir` | Tidak | Root projek sumber. Lalai kepada `"."`. |
| `translations_dir` | Tidak | Direktori output terjemahan teks. Lalai kepada `translations` di bawah `root_dir`. |
| `translated_images_dir` | Tidak | Direktori output imej yang diterjemah. Lalai kepada `translated_images` di bawah `root_dir`. |
| `translation_types` | Tidak | Jenis terjemahan yang diaktifkan. Lalai kepada Markdown, notebook, dan imej. |
| `lang_subdir` | Tidak | Subdirektori pilihan di bawah setiap folder bahasa. |

## Parameter Terjemahan Projek

| Parameter | Jenis | Lalai | Tujuan |
| --- | --- | --- | --- |
| `language_codes` | `str` | Diperlukan | Kod bahasa sasaran yang dipisahkan oleh ruang, seperti `"ko ja fr"`, atau `"all"`. Kod alias dinormalisasikan kepada nilai BCP 47 kanonik. |
| `root_dir` | `str` | `"."` | Root projek untuk satu sasaran terjemahan. Diabaikan apabila `root_dirs` atau `groups` dibekalkan. |
| `update` | `bool` | `False` | Padam dan cipta semula terjemahan sedia ada untuk bahasa terpilih. |
| `images` | `bool` | `False` | Sertakan terjemahan imej. Memerlukan konfigurasi Azure AI Vision. |
| `markdown` | `bool` | `False` | Sertakan terjemahan Markdown. |
| `notebook` | `bool` | `False` | Sertakan terjemahan Jupyter notebook. |
| `debug` | `bool` | `False` | Dayakan log debug. |
| `save_logs` | `bool` | `False` | Simpan fail log pada tahap DEBUG di bawah direktori root `logs/`. |
| `yes` | `bool` | `True` | Sahkan arahan secara automatik untuk penggunaan berprogram dan CI. |
| `add_disclaimer` | `bool` | `False` | Tambahkan penafian terjemahan mesin ke Markdown dan notebook yang diterjemahkan. |
| `translations_dir` | `str \| None` | `None` | Direktori keluaran terjemahan teks tersuai. Laluan relatif diselesaikan berbanding setiap root. |
| `image_dir` | `str \| None` | `None` | Direktori keluaran imej terjemahan tersuai. Laluan relatif diselesaikan berbanding setiap root. |
| `root_dirs` | `Iterable[str] \| None` | `None` | Beberapa root yang berkongsi tetapan keluaran yang sama. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | Pasangan tersurat `(root_dir, translations_dir)`. Mempunyai keutamaan berbanding `root_dirs`. |
| `repo_url` | `str \| None` | `None` | URL repositori yang digunakan ketika menghasilkan panduan jadual bahasa README. |
| `glossaries` | `Iterable[str] \| None` | `None` | Istilah glosari untuk dipelihara semasa terjemahan. Duplikasi dan istilah kosong dinormalisasikan. |
| `dry_run` | `bool` | `False` | Anggarkan volum terjemahan dan pratonton tingkah laku migrasi tanpa menulis fail. |
| `translation_state_provider` | `TranslationStateProvider \| None` | `None` | Adapter penyimpanan pilihan untuk accepted-baseline dan calon bagi kemas kini Markdown beransur. Mengabaikannya mengekalkan tingkah laku fail-penuh sedia ada. |

## Parameter Semakan

`run_review` secara sengaja mencerminkan tandatangan `run_translation` di mana mungkin supaya automasi dapat bertukar antara aliran kerja terjemahan dan semakan dengan percabangan minimum.

| Parameter | Jenis | Lalai | Tujuan |
| --- | --- | --- | --- |
| `language_codes` | `str \| Iterable[str]` | `"all"` | Folder bahasa sasaran untuk disemak. Rentetan berpisah-ruang dan iterable diterima. `"all"` menyemak setiap bahasa terjemahan yang ditemui. |
| `root_dir` | `str` | `"."` | Root projek untuk satu sasaran semakan. Diabaikan apabila `root_dirs` atau `groups` diberikan. |
| `markdown` | `bool` | `False` | Sertakan fail sumber Markdown dan MDX. |
| `notebook` | `bool` | `False` | Sertakan fail sumber Jupyter notebook. |
| `images` | `bool` | `False` | Dikhaskan untuk keseimbangan dengan pilihan terjemahan. Rujukan pautan ke imej disemak dari Markdown. |
| `translations_dir` | `str \| None` | `None` | Direktori keluaran terjemahan teks tersuai. Laluan relatif diselesaikan berbanding setiap root. |
| `root_dirs` | `Iterable[str] \| None` | `None` | Beberapa root yang berkongsi tetapan keluaran yang sama. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | Pasangan tersurat `(root_dir, translations_dir)`. Mempunyai keutamaan berbanding `root_dirs`. |
| `changed_from` | `str \| None` | `None` | Rujukan Git yang digunakan untuk mengehadkan semakan kepada fail sumber yang diubah. |
| `readme_only` | `bool` | `False` | Semak hanya `README.md` di bawah setiap root sumber. Ketiadaan README sumber akan menaikkan `ValueError`. |
| `output_format` | `str` | `"text"` | Format keluaran semakan. Nilai yang disokong adalah `"text"` dan `"github"`. |
| `fail_on_warnings` | `bool` | `False` | Anggap amaran sebagai kegagalan sebagai tambahan kepada ralat. |
| `debug` | `bool` | `False` | Dayakan log debug. |
| `save_logs` | `bool` | `False` | Simpan fail log peringkat DEBUG di bawah direktori root `logs/`. |

Jika tiada antara `markdown`, `notebook`, atau `images` ditetapkan, API menyemak Markdown, notebook, dan rujukan pautan imej di mana berkenaan. Semakan tidak memanggil penyedia LLM dan tidak memerlukan kunci API.

## Keperluan Konfigurasi

API terjemahan berasaskan pembekal memerlukan konfigurasi pembekal sebelum menterjemah:

- Terjemahan Markdown dan notebook memerlukan penyedia LLM. Konfigurasikan Azure OpenAI, OpenAI, atau Anthropic.
- Terjemahan imej memerlukan Azure AI Vision selain penyedia LLM.
- `run_translation` menjalankan pemeriksaan sambungan ringan sebelum terjemahan projek bermula.
- API `start_*_agent_translation` dan `finish_*_agent_translation` yang dibantu ejen tidak memanggil pembekal LLM Co-op Translator. Aplikasi hos atau ejen MCP menterjemahkan bahagian yang disediakan.
- `rewrite_markdown_paths`, `rewrite_notebook_paths`, dan `run_review` adalah deterministik dan tidak memerlukan kredensial pembekal.

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

Required Anthropic variables:

```bash
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

`ANTHROPIC_BASE_URL` dan `ANTHROPIC_MAX_TOKENS` adalah pilihan. Microsoft Agent Framework adalah klien model lalai untuk semua pembekal bermula dengan Co-op Translator 0.22.0. Semantic Kernel masih boleh dipilih sementara dengan `CO_OP_TRANSLATOR_MODEL_CLIENT="semantic-kernel"`, tetapi melakukan demikian akan mengeluarkan amaran penyahgunaan; lihat [configuration](configuration.md#model-client-backend) untuk pelan penghapusan bertahap.

Pembolehubah Azure AI Vision yang diperlukan untuk terjemahan imej:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

`run_review` adalah deterministik dan tidak memerlukan konfigurasi LLM atau Azure AI Vision.

## Nota Tingkah Laku

- API terjemahan kandungan memisahkan terjemahan daripada penulisan semula laluan projek. Panggil `rewrite_markdown_paths` atau `rewrite_notebook_paths` secara eksplisit apabila kandungan yang diterjemah memerlukan pautan relatif kepada projek diselaraskan untuk lokasi sasaran.
- API orkestrasi projek menambah tingkah laku projek sekitar terjemahan kandungan, termasuk penemuan fail, penulisan, penulisan semula laluan, metadata, pembersihan, dan penafian pilihan.
- `run_translation` mencetak ringkasan kemajuan dan anggaran melalui pelapor berasaskan Rich yang sama yang digunakan oleh CLI. Keluaran bukan interaktif kembali kepada teks biasa.
- `dry_run=True` mengira anggaran menggunakan kemas kini README maya, tetapi tidak menulis README atau fail terjemahan.
- `groups` diproses secara berurutan. Satu anggaran agregat dicetak sebelum kerja bermula.
- Apabila terjemahan imej dipilih, ketiadaan konfigurasi Vision akan menaikkan ralat sebelum terjemahan bermula.
- Folder bahasa berasaskan alias sedia ada dikesan dan boleh dipindahkan kepada nama folder bahasa kanonik sebagai sebahagian daripada larian.
- `run_review` gagal pada fail terjemahan yang hilang, metadata terjemahan yang hilang atau lapuk, frontmatter/fence kod Markdown yang cacat, dan JSON notebook terjemahan yang tidak sah.
- `run_review` melaporkan sasaran pautan Markdown dan imej tempatan yang hilang sebagai amaran secara lalai.

## Laluan Panggilan Dalaman

API ini mendelegasikan kepada pelaksanaan teras yang sama yang digunakan oleh CLI:

Terjemahan:

1. `co_op_translator.api.translation.translate_markdown_content`, `translate_notebook_content`, or `translate_image_content` for in-memory translation.
2. `co_op_translator.api.translation.rewrite_markdown_paths` or `rewrite_notebook_paths` for explicit path post-processing.
3. `co_op_translator.api.translation.run_translation` for full project orchestration.
4. `co_op_translator.config.Config`, `LLMConfig`, and `VisionConfig`.
5. `co_op_translator.core.project.ProjectTranslator`.
6. `co_op_translator.core.project.TranslationManager`.
7. Mixin terjemahan projek fokus untuk Markdown, notebook, dan imej.
8. Penterjemah Markdown, notebook, teks, dan imej di bawah `co_op_translator.core`.

Semakan:

1. `co_op_translator.api.review.run_review`
2. `co_op_translator.review.targets.build_review_targets`
3. `co_op_translator.review.runner.ReviewRunner`
4. Semakan deterministik di bawah `co_op_translator.review.checks`

Kelas berikut berguna untuk penyelenggara, tetapi tidak dieksport sebagai API stabil peringkat pakej.

| Kelas | Modul | Tanggungjawab |
| --- | --- | --- |
| `ProjectTranslator` | `co_op_translator.core.project.project_translator` | Makoordinasikan terjemahan peringkat projek, pengurusan direktori, normalisasi metadata setiap bahasa, dan pendelegasian kepada penterjemah Markdown, notebook, dan imej. |
| `TranslationManager` | `co_op_translator.core.project.translation` | Melaksanakan kerja pemprosesan fail tak segerak untuk Markdown, notebook, imej, pengesanan lapuk, dan kemas kini metadata terjemahan. |
| `ProjectMarkdownTranslationMixin` | `co_op_translator.core.project.translation.project_markdown_translation` | Mengorkestrakan bacaan fail Markdown, terjemahan kandungan, penulisan semula laluan, metadata, penafian, dan penulisan. |
| `ProjectNotebookTranslationMixin` | `co_op_translator.core.project.translation.project_notebook_translation` | Mengorkestrakan bacaan fail notebook, terjemahan sel Markdown, penulisan semula laluan, metadata, penafian, dan penulisan. |
| `ProjectImageTranslationMixin` | `co_op_translator.core.project.translation.project_image_translation` | Mengorkestrakan penemuan imej sumber, terjemahan imej, laluan keluaran, metadata, dan penulisan. |
| `ProjectEvaluator` | `co_op_translator.core.project.project_evaluator` | Menemukan pasangan Markdown yang diterjemah, menilai kualiti terjemahan, dan membaca metadata keyakinan untuk aliran kerja pembaikan berkeyakinan rendah. |
| `ReviewRunner` | `co_op_translator.review.runner` | Mengoordinasikan semakan deterministik merentasi fail sumber, bahasa sasaran, dan root terjemahan yang dikonfigurasi. |
| `ReviewTarget` | `co_op_translator.review.targets` | Menerangkan sebuah root sumber dan direktori keluaran terjemahan yang disemak untuk root tersebut. |
| `LanguageFolderMigrator` | `co_op_translator.core.project.language_migrator` | Mengesan folder bahasa alias warisan dan menyediakan pelan migrasi folder BCP 47 kanonik. |
| `Config` | `co_op_translator.config.base_config` | Memuat fail `.env` dan memeriksa sama ada penyedia LLM yang diperlukan dan Vision pilihan dikonfigurasikan. |
| `LLMConfig` | `co_op_translator.config.llm_config.config` | Mengesan secara automatik Azure OpenAI, OpenAI, atau Anthropic, mengesahkan pembolehubah persekitaran yang diperlukan, dan menjalankan pemeriksaan sambungan penyedia. |
| `VisionConfig` | `co_op_translator.config.vision_config.config` | Mengesan konfigurasi Azure AI Vision dan menjalankan pemeriksaan sambungan untuk terjemahan imej. |