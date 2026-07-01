# API Python

API Python awam yang stabil dieksport dari `co_op_translator.api`. Kebanyakan integrasi menggunakan salah satu aliran kerja ini:

| Senario | Gunakan ini apabila | API Utama |
| --- | --- | --- |
| Terjemah fail atau dokumen individu | Aplikasi anda membaca kandungan sumber, memanggil Co-op Translator untuk penterjemahan, dan memutuskan di mana menyimpan hasilnya. | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Sediakan kandungan untuk terjemahan oleh agen hos | Hos MCP atau model aplikasi anda akan menterjemah pecahan, manakala Co-op Translator mengendalikan pemecahan dan pembinaan semula. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Terjemah keseluruhan repositori | Anda mahu API Python berkelakuan seperti CLI dan mengendalikan penemuan, laluan output, metadata, pembersihan, dan penulisan. | `run_translation` |

Kebanyakan modul peringkat rendah di bawah `core`, `config`, `review`, dan `utils` adalah perincian pelaksanaan yang digunakan oleh titik masuk API ini.

Pelanggan MCP menggunakan API awam yang sama melalui [Pelayan MCP](mcp.md). Gunakan halaman ini apabila memanggil Python secara langsung, dan panduan MCP apabila mendedahkan Co-op Translator kepada agen atau penyunting. Jika anda sedang memutuskan antara CLI, API Python, dan MCP, mulakan dengan [Pilih Aliran Kerja Anda](workflows.md).

## Aliran API Kali Pertama

Mula di sini jika anda memanggil Co-op Translator dari kod Python:

1. Konfigurasikan pembekal LLM seperti yang diterangkan dalam [Configuration](configuration.md), melainkan anda hanya menyediakan pecahan Markdown atau buku nota untuk terjemahan agen hos.
2. Tentukan sama ada aplikasi anda memiliki I/O fail.
3. Gunakan API kandungan apabila aplikasi anda membaca dan menulis fail individu.
4. Gunakan `run_translation` apabila Co-op Translator harus memproses repositori seperti CLI.
5. Gunakan `run_review` selepas terjemahan jika anda memerlukan pemeriksaan deterministik dalam automasi.

| Matlamat | API untuk mula dengan |
| --- | --- |
| Terjemah satu rentetan atau fail Markdown | `translate_markdown_content` |
| Terjemah satu payload buku nota | `translate_notebook_content` |
| Terjemah satu imej | `translate_image_content` |
| Benarkan agen hos menterjemah pecahan Markdown atau buku nota | `start_markdown_agent_translation` atau `start_notebook_agent_translation` |
| Tulis semula pautan yang diterjemah selepas memilih laluan output | `rewrite_markdown_paths` atau `rewrite_notebook_paths` |
| Terjemah keseluruhan repositori | `run_translation` |
| Semak output terjemahan | `run_review` |

## Senario 1: Terjemah Fail atau Dokumen Individu

Gunakan aliran kerja ini apabila anda sudah mempunyai fail, buffer penyunting, payload buku nota, permintaan MCP, atau input saluran tersuai. Kod anda memiliki I/O fail:

1. Baca kandungan sumber.
2. Panggil API terjemahan kandungan.
3. Pilihan: panggil API penulisan semula laluan jika kandungan yang diterjemah akan ditulis ke dalam folder terjemahan projek.
4. Simpan atau kembalikan hasil dari aplikasi anda.

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

Jika Markdown yang diterjemah tidak akan berada dalam susun atur projek Co-op Translator, langkau `rewrite_markdown_paths` dan simpan rentetan yang diterjemah terus.

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

`translate_notebook_content` menterjemah sel Markdown dan mengekalkan sel bukan-Markdown. Penulisan semula laluan hanya dikenakan kepada sel Markdown.

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

`translate_image_content` membaca imej sumber dan mengembalikan `PIL.Image.Image` yang telah dirender. Ia tidak menulis metadata imej yang diterjemah.

## Senario 2: Terjemah Seluruh Repositori

Gunakan aliran kerja ini apabila anda mahu API Python berkelakuan seperti CLI `translate`. `run_translation` mengesan fail yang disokong, menterjemah jenis kandungan yang dipilih, menulis semula laluan, menulis fail output, mengemas kini metadata, dan melaksanakan tugas penyelenggaraan terjemahan seperti pembersihan.

`run_translation` adalah titik masuk orkestrasi projek yang disyorkan. `translate_project` dieksport sebagai alias keserasian dengan kelakuan yang sama.

Terjemah fail Markdown dalam repositori semasa ke dalam Korea dan Jepun:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    markdown=True,
)
```

Terjemah hanya buku nota dari akar projek tertentu:

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

Terjemah berbilang akar kandungan dalam satu panggilan:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    root_dirs=["./docs", "./labs"],
)
```

Tulis terjemahan ke dalam kumpulan output yang eksplisit:

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

Gunakan pemegang tempat per-bahasa apabila setiap bahasa harus mengandungi subdirektori bertingkat:

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

Jika tiada `markdown`, `notebook`, atau `images` disetkan, API akan menterjemah semua jenis yang disokong: Markdown, buku nota, dan imej.

## Semak Output Terjemahan

`run_review` menjalankan pemeriksaan terjemahan deterministik tanpa kelayakan LLM atau Vision.

!!! note "Beta"
    `run_review` is a beta deterministic review API. It does not call model providers or write files, but checks and issue schemas may evolve.

```python
from co_op_translator.api import run_review

run_review(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
)
```

Semak hanya fail yang diubah berbanding ref asas dan cetak output gaya GitHub:

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

Terjemah kandungan Markdown tanpa penulisan fail:

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

Terjemah dan tulis semula pautan Markdown:

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

Terjemah repositori dari Python:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    root_dir="./course",
    markdown=True,
    yes=True,
)
```

Terjemah berbilang akar:

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

Kekalkan istilah glosari:

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

## API Penterjemahan Kandungan

API penterjemahan kandungan bertujuan untuk integrasi yang sudah mempunyai kandungan dalam memori, seperti peluasan penyunting, alat MCP, pemproses buku nota, atau saluran tersuai.

| Fungsi | Input | Output | I/O Fail | Nota |
| --- | --- | --- | --- | --- |
| `translate_markdown_content` | Markdown `str` | Markdown `str` | Tidak | Async. Menterjemah kandungan Markdown sahaja. Ia tidak menulis semula pautan, menulis metadata, atau menambah penafian. |
| `translate_notebook_content` | Notebook JSON `str` atau `dict` | Notebook JSON `str` | Tidak | Async. Menterjemah sel Markdown dan mengekalkan sel bukan-Markdown. Ia tidak menulis semula pautan, menulis metadata, atau menambah penafian. |
| `translate_image_content` | Laluan imej | `PIL.Image.Image` | Membaca imej sumber sahaja | Synchronous. Mengekstrak dan menterjemah teks imej, kemudian mengembalikan imej yang telah dirender. Ia tidak menyimpan metadata imej yang diterjemah. |

`translate_markdown_content` dan `translate_notebook_content` menerima pilihan `source_path` pilihan melalui opsyen mereka. Laluan itu dihantar sebagai konteks kepada penterjemah; pemanggil kekal bertanggungjawab untuk sebarang penulisan semula laluan khusus projek selepas terjemahan.

```python
from co_op_translator.api import MarkdownTranslationOptions, translate_markdown_content

translated = await translate_markdown_content(
    document,
    "ko",
    MarkdownTranslationOptions(source_path="docs/guide.md"),
)
```

Pilihan yang sama boleh disampaikan sebagai kamus:

```python
translated = await translate_markdown_content(
    document,
    "ko",
    {"source_path": "docs/guide.md"},
)
```

## API Terjemahan dengan Bantuan Agen

API dengan bantuan agen tidak memanggil Azure OpenAI atau OpenAI dari Co-op Translator. Mereka menyediakan pecahan Markdown atau buku nota untuk diterjemah oleh agen hos, kemudian membina semula kandungan akhir dari pecahan yang telah diterjemah.

| Fungsi | Tujuan |
| --- | --- |
| `start_markdown_agent_translation` | Pulangkan kerja Markdown yang berdiri sendiri dengan pecahan, prompt, dan keadaan pembinaan semula. |
| `finish_markdown_agent_translation` | Bina semula Markdown dari kerja dan pecahan yang telah diterjemah oleh agen hos. |
| `start_notebook_agent_translation` | Pulangkan kerja buku nota dengan pecahan sel-Markdown untuk terjemahan agen hos. |
| `finish_notebook_agent_translation` | Bina semula JSON buku nota sambil mengekalkan sel kod, output, dan metadata. |

Aliran kerja ini terutamanya ditujukan untuk hos MCP. Jika anda memerlukan terjemahan repositori pengeluaran dengan Co-op Translator mengurus panggilan pembekal, gunakan `translate_markdown_content`, `translate_notebook_content`, atau `run_translation`.

## API Penulisan Semula Laluan

API penulisan semula laluan tidak melakukan sebarang terjemahan. Mereka mengemas kini pautan dan laluan frontmatter selepas pemanggil mengetahui laluan sumber, laluan sasaran yang diterjemah, dan susun atur projek.

| Fungsi | Skop | Nota |
| --- | --- | --- |
| `rewrite_markdown_paths` | Badan Markdown dan frontmatter | Menulis semula pautan Markdown dan medan laluan frontmatter yang disokong untuk sasaran yang diterjemah. |
| `rewrite_notebook_paths` | Sel Markdown dalam JSON buku nota | Memohon penulisan semula laluan Markdown kepada setiap sel Markdown dan membiarkan sel bukan-Markdown tidak berubah. |

Argumen `policy` mungkin merupakan sebuah kamus dengan medan-medan berikut:

| Medan | Diperlukan | Tujuan |
| --- | --- | --- |
| `language_code` | Ya | Kod bahasa sasaran, seperti `"ko"` atau `"pt-BR"`. |
| `root_dir` | Tidak | Akar projek sumber. Lalai kepada `"."`. |
| `translations_dir` | Tidak | Direktori output terjemahan teks. Lalai kepada `translations` di bawah `root_dir`. |
| `translated_images_dir` | Tidak | Direktori output imej yang diterjemah. Lalai kepada `translated_images` di bawah `root_dir`. |
| `translation_types` | Tidak | Jenis terjemahan yang diaktifkan. Lalai kepada Markdown, buku nota, dan imej. |
| `lang_subdir` | Tidak | Subdirektori pilihan di bawah setiap folder bahasa. |

## Parameter Terjemahan Projek

| Parameter | Type | Default | Tujuan |
| --- | --- | --- | --- |
| `language_codes` | `str` | Required | Kod bahasa sasaran berasingan oleh ruang, seperti `"ko ja fr"`, atau `"all"`. Kod alias dinormalisasi kepada nilai BCP 47 kanonik. |
| `root_dir` | `str` | `"."` | Akar projek untuk satu sasaran terjemahan. Diabaikan apabila `root_dirs` atau `groups` dibekalkan. |
| `update` | `bool` | `False` | Padam dan buat semula terjemahan sedia ada untuk bahasa yang dipilih. |
| `images` | `bool` | `False` | Sertakan terjemahan imej. Memerlukan konfigurasi Azure AI Vision. |
| `markdown` | `bool` | `False` | Sertakan terjemahan Markdown. |
| `notebook` | `bool` | `False` | Sertakan terjemahan buku nota Jupyter. |
| `debug` | `bool` | `False` | Aktifkan log debug. |
| `save_logs` | `bool` | `False` | Simpan fail log PERINGKAT DEBUG di bawah direktori root `logs/`. |
| `yes` | `bool` | `True` | Auto-pengesahan arahan untuk penggunaan programatik dan CI. |
| `add_disclaimer` | `bool` | `False` | Tambah penafian terjemahan mesin kepada Markdown dan buku nota yang diterjemah. |
| `translations_dir` | `str \| None` | `None` | Direktori output terjemahan teks tersuai. Laluan relatif diselesaikan terhadap setiap akar. |
| `image_dir` | `str \| None` | `None` | Direktori output imej yang diterjemah tersuai. Laluan relatif diselesaikan terhadap setiap akar. |
| `root_dirs` | `Iterable[str] \| None` | `None` | Berbilang akar yang berkongsi tetapan output yang sama. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | Pasangan `(root_dir, translations_dir)` eksplisit. Mengatasi `root_dirs`. |
| `repo_url` | `str \| None` | `None` | URL repositori yang digunakan apabila merender panduan jadual bahasa README. |
| `glossaries` | `Iterable[str] \| None` | `None` | Istilah glosari untuk dikekalkan semasa terjemahan. Duplikasi dan istilah kosong dinormalisasi. |
| `dry_run` | `bool` | `False` | Anggarkan jumlah terjemahan dan pratonton perlakuan migrasi tanpa menulis fail. |

## Parameter Semakan

`run_review` dengan sengaja mencerminkan tanda tangan `run_translation` di mana boleh supaya automasi boleh bertukar antara aliran kerja terjemahan dan semakan dengan percabangan yang minimum.

| Parameter | Type | Default | Tujuan |
| --- | --- | --- | --- |
| `language_codes` | `str \| Iterable[str]` | `"all"` | Folder bahasa sasaran untuk disemak. Rentetan berasingan dengan ruang dan iterable diterima. `"all"` menyemak setiap bahasa terjemahan yang ditemui. |
| `root_dir` | `str` | `"."` | Akar projek untuk satu sasaran semakan. Diabaikan apabila `root_dirs` atau `groups` dibekalkan. |
| `markdown` | `bool` | `False` | Sertakan fail sumber Markdown dan MDX. |
| `notebook` | `bool` | `False` | Sertakan fail sumber buku nota Jupyter. |
| `images` | `bool` | `False` | Ditempatkan untuk keseragaman dengan pilihan terjemahan. Rujukan pautan kepada imej diperiksa dari Markdown. |
| `translations_dir` | `str \| None` | `None` | Direktori output terjemahan teks tersuai. Laluan relatif diselesaikan terhadap setiap root. |
| `root_dirs` | `Iterable[str] \| None` | `None` | Berbilang root yang berkongsi tetapan output yang sama. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | Pasangan eksplisit `(root_dir, translations_dir)`. Mengambil keutamaan berbanding `root_dirs`. |
| `changed_from` | `str \| None` | `None` | Rujukan Git yang digunakan untuk mengehadkan semakan kepada fail sumber yang diubah. |
| `output_format` | `str` | `"text"` | Format output semakan. Nilai yang disokong ialah `"text"` dan `"github"`. |
| `fail_on_warnings` | `bool` | `False` | Layan amaran sebagai kegagalan selain ralat. |
| `debug` | `bool` | `False` | Dayakan log debug. |
| `save_logs` | `bool` | `False` | Simpan fail log peringkat DEBUG di bawah direktori root `logs/`. |

If none of `markdown`, `notebook`, or `images` are set, the API reviews Markdown, notebooks, and image link references where applicable. Review does not call an LLM provider and does not require API keys.

## Keperluan Konfigurasi

Provider-backed translation APIs require provider configuration before translating:

- Markdown and notebook translation require an LLM provider. Configure either Azure OpenAI or OpenAI.
- Image translation requires Azure AI Vision in addition to the LLM provider.
- `run_translation` runs lightweight connectivity checks before project translation begins.
- Agent-assisted `start_*_agent_translation` and `finish_*_agent_translation` APIs do not call Co-op Translator LLM providers. The host application or MCP agent translates the prepared chunks.
- `rewrite_markdown_paths`, `rewrite_notebook_paths`, and `run_review` are deterministic and do not require provider credentials.

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

`run_review` is deterministic and does not require Azure OpenAI, OpenAI, or Azure AI Vision configuration.

## Nota Tingkah Laku

- Content translation APIs keep translation separate from project path rewriting. Call `rewrite_markdown_paths` or `rewrite_notebook_paths` explicitly when translated content needs project-relative links adjusted for a target location.
- Project orchestration APIs add project behavior around content translation, including file discovery, writes, path rewriting, metadata, cleanup, and optional disclaimers.
- `run_translation` prints progress and estimate summaries through Click, matching the CLI user experience.
- `dry_run=True` computes estimates using virtual README updates, but does not write the README or translation files.
- `groups` are processed sequentially. A single aggregate estimate is printed before work begins.
- When image translation is selected, missing Vision configuration raises an error before translation starts.
- Existing alias-based language folders are detected and can be migrated to canonical language folder names as part of the run.
- `run_review` fails on missing translated files, missing or stale translation metadata, malformed Markdown frontmatter/code fences, and invalid translated notebook JSON.
- `run_review` reports missing local Markdown and image link targets as warnings by default.

## Jalur Panggilan Dalaman

The API delegates to the same core implementation used by the CLI:

Translation:

1. `co_op_translator.api.translation.translate_markdown_content`, `translate_notebook_content`, or `translate_image_content` for in-memory translation.
2. `co_op_translator.api.translation.rewrite_markdown_paths` or `rewrite_notebook_paths` for explicit path post-processing.
3. `co_op_translator.api.translation.run_translation` for full project orchestration.
4. `co_op_translator.config.Config`, `LLMConfig`, and `VisionConfig`.
5. `co_op_translator.core.project.ProjectTranslator`.
6. `co_op_translator.core.project.TranslationManager`.
7. Focused project translation mixins for Markdown, notebooks, and images.
8. Markdown, notebook, text, and image translators under `co_op_translator.core`.

Review:

1. `co_op_translator.api.review.run_review`
2. `co_op_translator.review.targets.build_review_targets`
3. `co_op_translator.review.runner.ReviewRunner`
4. Deterministic checks under `co_op_translator.review.checks`

The following classes are useful for maintainers, but are not exported as the package-level stable API.

| Kelas | Modul | Tanggungjawab |
| --- | --- | --- |
| `ProjectTranslator` | `co_op_translator.core.project.project_translator` | Makoordinasikan terjemahan peringkat projek, pengurusan direktori, penormalan metadata per-bahasa, dan delegasi kepada penterjemah Markdown, notebook, dan imej. |
| `TranslationManager` | `co_op_translator.core.project.translation` | Melaksanakan kerja pemprosesan fail async untuk Markdown, notebook, imej, pengesanan lapuk, dan kemas kini metadata terjemahan. |
| `ProjectMarkdownTranslationMixin` | `co_op_translator.core.project.translation.project_markdown_translation` | Mengorkestrakan pembacaan fail Markdown, terjemahan kandungan, penulisan semula laluan, metadata, penafian, dan penulisan. |
| `ProjectNotebookTranslationMixin` | `co_op_translator.core.project.translation.project_notebook_translation` | Mengorkestrakan pembacaan fail notebook, terjemahan sel Markdown, penulisan semula laluan, metadata, penafian, dan penulisan. |
| `ProjectImageTranslationMixin` | `co_op_translator.core.project.translation.project_image_translation` | Mengorkestrakan penemuan imej sumber, terjemahan imej, laluan output, metadata, dan penulisan. |
| `ProjectEvaluator` | `co_op_translator.core.project.project_evaluator` | Menemukan pasangan Markdown yang diterjemah, menilai kualiti terjemahan, dan membaca metadata keyakinan untuk aliran kerja pembaikan berkeyakinan rendah. |
| `ReviewRunner` | `co_op_translator.review.runner` | Menyelaras pemeriksaan semakan deterministik merentas fail sumber, bahasa sasaran, dan root terjemahan yang dikonfigurasi. |
| `ReviewTarget` | `co_op_translator.review.targets` | Menerangkan root sumber dan direktori output terjemahan yang disemak untuk root tersebut. |
| `LanguageFolderMigrator` | `co_op_translator.core.project.language_migrator` | Mengesan folder bahasa alias warisan dan menyediakan pelan migrasi folder kanonik BCP 47. |
| `Config` | `co_op_translator.config.base_config` | Memuat fail `.env` dan memeriksa sama ada pembekal LLM yang diperlukan dan Vision pilihan telah dikonfigurasi. |
| `LLMConfig` | `co_op_translator.config.llm_config.config` | Mengesan secara automatik Azure OpenAI atau OpenAI, mengesahkan pembolehubah persekitaran yang diperlukan, dan menjalankan pemeriksaan kesambungan pembekal. |
| `VisionConfig` | `co_op_translator.config.vision_config.config` | Mengesan konfigurasi Azure AI Vision dan menjalankan pemeriksaan kesambungan untuk terjemahan imej. |