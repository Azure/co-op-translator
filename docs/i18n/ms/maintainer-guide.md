# Panduan Penyelenggara

Halaman ini meringkaskan bagaimana API, CLI, dan laman dokumentasi disambungkan bersama.

## Sempadan API Awam

API Python stabil dieksport dari:

```python
co_op_translator.api
```

API awam diatur kepada pembantu terjemahan kandungan, pembantu penulisan semula laluan, penyelarasan projek, dan semakan:

```python
from co_op_translator.api import (
    ImageTranslationOptions,
    MarkdownTranslationOptions,
    NotebookTranslationOptions,
    TranslationBaseline,
    TranslationStateProvider,
    TranslationUpdate,
    run_review,
    run_translation,
    rewrite_markdown_paths,
    rewrite_notebook_paths,
    translate_image_content,
    translate_markdown_content,
    translate_notebook_content,
    translate_project,
)
```

`TranslationStateProvider` adalah sempadan persistensi untuk integrasi yang dihoskan.
Ia mesti memastikan calon yang dijana dipisahkan daripada garis asas yang diterima supaya
terjemahan yang belum digabungkan tidak menjadi sumber kebenaran.

Apabila menambah API awam baru, kemas kini:

- `src/co_op_translator/api/__init__.py`
- `docs/api.md`
- relevant API tests under `tests/co_op_translator/`, such as `test_api.py` or `test_review_api.py`

Elakkan mendokumentasikan modul `core` peringkat rendah sebagai API stabil melainkan projek berniat menyokongnya secara langsung.

## Titik masuk CLI

Pakej ini mentakrifkan skrip Poetry berikut:

```toml
[tool.poetry.scripts]
translate = "co_op_translator.__main__:main"
evaluate = "co_op_translator.__main__:main"
migrate-links = "co_op_translator.__main__:main"
co-op-review = "co_op_translator.__main__:main"
co-op-translator-mcp = "co_op_translator.mcp.server:main"
```

`src/co_op_translator/__main__.py` mengagihkan berdasarkan nama skrip:

- `translate` calls `co_op_translator.cli.translate.translate_command`
- `evaluate` calls `co_op_translator.cli.evaluate.evaluate_command`
- `migrate-links` calls `co_op_translator.cli.migrate_links.migrate_links_command`
- `co-op-review` calls `co_op_translator.cli.review.review_command`

`co-op-translator-mcp` memintas `__main__.py` dan memanggil `co_op_translator.mcp.server:main` secara langsung.

Apabila menambah atau mengubah pilihan CLI, kemas kini:

- arahan `src/co_op_translator/cli/*.py` yang berkaitan
- `docs/cli.md`
- ujian berkaitan CLI, jika tingkah laku berubah

## Pelayan MCP

Pelayan MCP diimplementasikan dalam:

```python
co_op_translator.mcp.server
```

Pelayan dengan sengaja membalut API Python awam daripada memanggil modul `core` peringkat lebih rendah. Kekalkan sempadan ini supaya klien MCP, pemanggil Python, dan CLI berkongsi tingkah laku yang sama.

Apabila menambah atau mengubah alat MCP, kemas kini:

- `src/co_op_translator/mcp/server.py`
- `tests/co_op_translator/test_mcp_server.py`
- `docs/mcp.md`
- `docs/api.md` if the public API surface changes

Alat terjemahan repositori boleh dipanggil model melalui MCP dan boleh menulis banyak fail. Kekalkan `dry_run=True` sebagai lalai dan memerlukan `confirm_write=True` sebelum terjemahan projek bukan dry-run.

## Aliran terjemahan

Aliran terjemahan projek peringkat tinggi ialah:

1. Huraikan argumen CLI atau parameter API.
2. Sahkan konfigurasi LLM dengan `LLMConfig`.
3. Sahkan Azure AI Vision apabila terjemahan imej dipilih.
4. Normalisasikan kod bahasa.
5. Mengesan alias folder bahasa lama.
6. Anggarkan jumlah terjemahan.
7. Kemas kini bahagian bahasa/kursus dalam README apabila berkenaan.
8. Serahkan terjemahan projek kepada `ProjectTranslator`.
9. `ProjectTranslator` menyerahkan pemprosesan fail kepada `TranslationManager`.

`TranslationManager` disusun daripada mixin berfokus pada jenis fail:

- `ProjectMarkdownTranslationMixin` mengendalikan pembacaan fail Markdown, terjemahan kandungan, penulisan semula laluan, metadata, penafian, dan penulisan.
- `ProjectNotebookTranslationMixin` mengendalikan pembacaan fail notebook, terjemahan sel Markdown, penulisan semula laluan, metadata, penafian, dan penulisan.
- `ProjectImageTranslationMixin` mengendalikan penemuan imej, pengektrakan/terjemahan teks, penulisan imej yang dirender, dan metadata.

API kandungan peringkat rendah tidak melalui aliran kerja projek:

1. `translate_markdown_content` dan `translate_notebook_content` menterjemah kandungan dalam memori sahaja.
2. `translate_image_content` menterjemah teks dalam satu imej dan memulangkan objek imej yang dirender.
3. `rewrite_markdown_paths` dan `rewrite_notebook_paths` adalah pembantu pemprosesan pasca yang jelas. Mereka tidak melakukan terjemahan dan tidak menulis projek.

## Aliran semakan

Aliran semakan deterministik ialah:

1. Huraikan argumen CLI atau parameter API.
2. Normalisasikan kod bahasa yang diminta.
3. Bina satu atau lebih sasaran semakan daripada `root_dir`, `root_dirs`, atau `groups`.
4. Secara pilihan hadkan fail sumber dengan `--changed-from`.
5. Jalankan pemeriksaan deterministik untuk struktur, kesegaran terjemahan, integriti Markdown, dan laluan pautan/imej tempatan.
6. Cetak sama ada keluaran teks atau Markdown berperisa GitHub.
7. Keluar dengan kegagalan apabila ralat semakan ditemui.

Aliran semakan tidak memerlukan kunci API dan kekal tersedia untuk pemeriksaan tempatan atau CI pengguna pilih masuk. Repositori ini tidak menjalankan `co-op-review` secara automatik pada setiap pull request.

## Laman dokumentasi

Laman dokumentasi dikonfigurasikan oleh:

```text
mkdocs.yml
requirements-docs.txt
docs/
```

Direktori `docs/` adalah sumber dokumentasi kanonik. Jangan tambahkan panduan pengguna akhir baru di luar direktori ini melainkan projek secara sengaja memperkenalkan permukaan dokumentasi yang diterbitkan lain.

Bina secara tempatan:

```bash
python -m pip install -r requirements-docs.txt
python -m mkdocs build --strict
```

Pratonton secara tempatan:

```bash
python -m mkdocs serve
```

Laman yang dijana ditulis ke `site/`, yang diabaikan oleh git.

## Aliran kerja GitHub Pages

`.github/workflows/docs.yml` membina laman pada pull request dan menyebarkannya apabila ada push ke `main`.

Aliran kerja memasang:

```bash
pip install -r requirements-docs.txt
```

Aliran kerja docs memasang hanya rantaian alat dokumentasi. `mkdocs.yml` menunjukkan `mkdocstrings` ke `src/` supaya halaman API awam boleh dihasilkan dari pokok sumber tanpa memasang set pergantungan runtime penuh. Jika dokumen API masa depan memerlukan pengimportan pembekal runtime pilihan semasa binaan, kemas kini kedua-dua `.github/workflows/docs.yml` dan panduan ini bersama-sama.

## Bar kualiti dokumentasi

Sebelum menggabungkan perubahan dokumentasi, jalankan:

```bash
python -m mkdocs build --strict
git diff --check
```

Guna binaan yang ketat supaya pautan rosak, entri navigasi tidak sah, dan isu rendering API gagal awal.