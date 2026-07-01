# Panduan Pemelihara

Halaman ini merangkum bagaimana API, CLI, dan situs dokumentasi dihubungkan bersama.

## Batas API publik

API Python yang stabil diekspor dari:

```python
co_op_translator.api
```

API publik diatur ke dalam pembantu terjemahan konten, pembantu penulisan ulang jalur, orkestrasi proyek, dan tinjauan:

```python
from co_op_translator.api import (
    ImageTranslationOptions,
    MarkdownTranslationOptions,
    NotebookTranslationOptions,
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

Saat menambahkan API publik baru, perbarui:

- `src/co_op_translator/api/__init__.py`
- `docs/api.md`
- pengujian API terkait di bawah `tests/co_op_translator/`, seperti `test_api.py` atau `test_review_api.py`

Hindari mendokumentasikan modul `core` tingkat rendah sebagai API stabil kecuali proyek berniat mendukungnya secara langsung.

## Titik masuk CLI

Paket ini mendefinisikan skrip Poetry ini:

```toml
[tool.poetry.scripts]
translate = "co_op_translator.__main__:main"
evaluate = "co_op_translator.__main__:main"
migrate-links = "co_op_translator.__main__:main"
co-op-review = "co_op_translator.__main__:main"
co-op-translator-mcp = "co_op_translator.mcp.server:main"
```

`src/co_op_translator/__main__.py` menjalankan berdasarkan nama skrip:

- `translate` calls `co_op_translator.cli.translate.translate_command`
- `evaluate` calls `co_op_translator.cli.evaluate.evaluate_command`
- `migrate-links` calls `co_op_translator.cli.migrate_links.migrate_links_command`
- `co-op-review` calls `co_op_translator.cli.review.review_command`

`co-op-translator-mcp` bypasses `__main__.py` and calls `co_op_translator.mcp.server:main` directly.

Saat menambahkan atau mengubah opsi CLI, perbarui:

- perintah `src/co_op_translator/cli/*.py` yang relevan
- `docs/cli.md`
- tes terkait CLI, jika perilaku berubah

## Server MCP

Server MCP diimplementasikan di:

```python
co_op_translator.mcp.server
```

Server sengaja membungkus API Python publik alih-alih memanggil modul `core` yang lebih rendah. Jaga batas ini tetap utuh agar klien MCP, pemanggil Python, dan CLI berbagi perilaku yang sama.

Saat menambahkan atau mengubah alat MCP, perbarui:

- `src/co_op_translator/mcp/server.py`
- `tests/co_op_translator/test_mcp_server.py`
- `docs/mcp.md`
- `docs/api.md` jika permukaan API publik berubah

Alat terjemahan repositori dapat dipanggil model melalui MCP dan dapat menulis banyak berkas. Tetap gunakan `dry_run=True` sebagai default dan minta `confirm_write=True` sebelum terjemahan proyek non-dry-run.

## Alur terjemahan

Alur terjemahan proyek tingkat tinggi adalah:

1. Mengurai argumen CLI atau parameter API.
2. Memvalidasi konfigurasi LLM dengan `LLMConfig`.
3. Memvalidasi Azure AI Vision ketika terjemahan gambar dipilih.
4. Menormalkan kode bahasa.
5. Mendeteksi alias folder bahasa warisan.
6. Memperkirakan volume terjemahan.
7. Memperbarui bagian bahasa/kursus README bila berlaku.
8. Mendelegasikan terjemahan proyek ke `ProjectTranslator`.
9. `ProjectTranslator` mendelegasikan pemrosesan berkas ke `TranslationManager`.

`TranslationManager` disusun dari mixin yang berfokus pada tipe berkas:

- `ProjectMarkdownTranslationMixin` menangani pembacaan berkas Markdown, terjemahan konten, penulisan ulang jalur, metadata, penyangkalan, dan penulisan.
- `ProjectNotebookTranslationMixin` menangani pembacaan berkas notebook, terjemahan sel Markdown, penulisan ulang jalur, metadata, penyangkalan, dan penulisan.
- `ProjectImageTranslationMixin` menangani penemuan gambar, ekstraksi/terjemahan teks, penulisan gambar hasil render, dan metadata.

API konten tingkat rendah melewatkan alur kerja proyek:

1. `translate_markdown_content` and `translate_notebook_content` translate in-memory content only.
2. `translate_image_content` translates text in a single image and returns a rendered image object.
3. `rewrite_markdown_paths` and `rewrite_notebook_paths` are explicit post-processing helpers. They perform no translation and no project writes.

## Alur peninjauan

Alur peninjauan deterministik adalah:

1. Mengurai argumen CLI atau parameter API.
2. Menormalkan kode bahasa yang diminta.
3. Membangun satu atau lebih target tinjauan dari `root_dir`, `root_dirs`, atau `groups`.
4. Secara opsional batasi berkas sumber dengan `--changed-from`.
5. Jalankan pemeriksaan deterministik untuk struktur, kesegaran terjemahan, integritas Markdown, dan jalur tautan/gambar lokal.
6. Cetak keluaran teks atau Markdown bergaya GitHub.
7. Keluar dengan kegagalan ketika ditemukan kesalahan peninjauan.

Alur peninjauan tidak memerlukan kunci API dan harus tetap sesuai untuk CI pull request. Alur kerja pull request menulis ringkasan pemeriksaan pada setiap jalankan dan hanya memposting komentar PR ketika `co-op-review` gagal.

## Situs dokumentasi

Situs dokumentasi dikonfigurasi oleh:

```text
mkdocs.yml
requirements-docs.txt
docs/
```

Direktori `docs/` adalah sumber dokumentasi yang kanonik. Jangan menambahkan panduan pengguna akhir baru di luar direktori ini kecuali proyek secara sengaja memperkenalkan permukaan dokumentasi terpublikasi lain.

Bangun secara lokal:

```bash
python -m pip install -r requirements-docs.txt
python -m mkdocs build --strict
```

Pratinjau secara lokal:

```bash
python -m mkdocs serve
```

Situs yang dihasilkan ditulis ke `site/`, yang diabaikan oleh git.

## Alur kerja GitHub Pages

`.github/workflows/docs.yml` membangun situs pada pull request dan mendeploynya pada push ke `main`.

Alur kerja menginstal:

```bash
pip install -r requirements-docs.txt
```

Alur kerja docs hanya menginstal rangkaian alat dokumentasi. `mkdocs.yml` mengarahkan `mkdocstrings` ke `src/` sehingga halaman API publik dapat dirender dari pohon sumber tanpa menginstal seluruh set dependensi runtime. Jika dokumentasi API di masa depan memerlukan impor penyedia runtime opsional selama proses build, perbarui baik `.github/workflows/docs.yml` maupun panduan ini bersama-sama.

## Ambang kualitas dokumentasi

Sebelum menggabungkan perubahan dokumentasi, jalankan:

```bash
python -m mkdocs build --strict
git diff --check
```

Gunakan build yang ketat sehingga tautan rusak, entri navigasi yang tidak valid, dan masalah perenderan API gagal lebih awal.