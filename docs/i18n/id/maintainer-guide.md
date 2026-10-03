# Panduan Pemelihara

Halaman ini merangkum bagaimana API, CLI, dan situs dokumentasi saling terhubung.

## Batas API Publik

API Python yang stabil diekspor dari:

```python
co_op_translator.api
```

API publik diatur menjadi pembantu terjemahan konten, pembantu penulisan ulang jalur, orkestrasi proyek, dan peninjauan:

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

`TranslationStateProvider` adalah batas persistensi untuk integrasi yang dihosting.
Ia harus menjaga kandidat yang dihasilkan tetap terpisah dari baseline yang diterima sehingga sebuah
terjemahan yang belum digabung tidak dapat menjadi sumber kebenaran.

Saat menambahkan API publik baru, perbarui:

- `src/co_op_translator/api/__init__.py`
- `docs/api.md`
- tes API terkait di `tests/co_op_translator/`, seperti `test_api.py` atau `test_review_api.py`

Hindari mendokumentasikan modul `core` tingkat rendah sebagai API stabil kecuali proyek bermaksud mendukungnya secara langsung.

## Titik masuk CLI

Paket mendefinisikan skrip Poetry berikut:

```toml
[tool.poetry.scripts]
translate = "co_op_translator.__main__:main"
evaluate = "co_op_translator.__main__:main"
migrate-links = "co_op_translator.__main__:main"
co-op-review = "co_op_translator.__main__:main"
co-op-translator-mcp = "co_op_translator.mcp.server:main"
```

`src/co_op_translator/__main__.py` memanggil berdasarkan nama skrip:

- `translate` memanggil `co_op_translator.cli.translate.translate_command`
- `evaluate` memanggil `co_op_translator.cli.evaluate.evaluate_command`
- `migrate-links` memanggil `co_op_translator.cli.migrate_links.migrate_links_command`
- `co-op-review` memanggil `co_op_translator.cli.review.review_command`

`co-op-translator-mcp` melewati `__main__.py` dan memanggil `co_op_translator.mcp.server:main` secara langsung.

Saat menambahkan atau mengubah opsi CLI, perbarui:

- perintah terkait di `src/co_op_translator/cli/*.py`
- `docs/cli.md`
- tes terkait CLI, jika perilaku berubah

## Server MCP

Server MCP diimplementasikan di:

```python
co_op_translator.mcp.server
```

Server sengaja membungkus API Python publik alih-alih memanggil modul `core` tingkat rendah. Pertahankan batas ini agar klien MCP, pemanggil Python, dan CLI berbagi perilaku yang sama.

Saat menambahkan atau mengubah alat MCP, perbarui:

- `src/co_op_translator/mcp/server.py`
- `tests/co_op_translator/test_mcp_server.py`
- `docs/mcp.md`
- `docs/api.md` jika permukaan API publik berubah

Alat terjemahan repositori dapat dipanggil oleh model melalui MCP dan dapat menulis banyak file. Tetap gunakan `dry_run=True` sebagai default dan minta `confirm_write=True` sebelum terjemahan proyek non-dry-run.

## Alur terjemahan

Alur terjemahan proyek tingkat tinggi adalah:

1. Mengurai argumen CLI atau parameter API.
2. Memvalidasi konfigurasi LLM dengan `LLMConfig`.
3. Memvalidasi Azure AI Vision ketika penerjemahan gambar dipilih.
4. Menormalkan kode bahasa.
5. Mendeteksi alias folder bahasa warisan.
6. Memperkirakan volume terjemahan.
7. Memperbarui bagian bahasa/kursus README jika berlaku.
8. Mendelegasikan terjemahan proyek ke `ProjectTranslator`.
9. `ProjectTranslator` mendelegasikan pemrosesan file ke `TranslationManager`.

`TranslationManager` tersusun dari mixin fokus per jenis file:

- `ProjectMarkdownTranslationMixin` menangani pembacaan file Markdown, terjemahan konten, penulisan ulang jalur, metadata, penafian, dan penulisan.
- `ProjectNotebookTranslationMixin` menangani pembacaan file notebook, terjemahan sel Markdown, penulisan ulang jalur, metadata, penafian, dan penulisan.
- `ProjectImageTranslationMixin` menangani penemuan gambar, ekstraksi/terjemahan teks, penulisan gambar yang dirender, dan metadata.

API konten tingkat rendah melewati alur kerja proyek:

1. `translate_markdown_content` dan `translate_notebook_content` menerjemahkan konten di memori saja.
2. `translate_image_content` menerjemahkan teks dalam satu gambar dan mengembalikan objek gambar yang telah dirender.
3. `rewrite_markdown_paths` dan `rewrite_notebook_paths` adalah pembantu pasca-pemrosesan eksplisit. Mereka tidak melakukan terjemahan dan tidak melakukan penulisan proyek.

## Alur peninjauan

Alur peninjauan deterministik adalah:

1. Mengurai argumen CLI atau parameter API.
2. Menormalkan kode bahasa yang diminta.
3. Membangun satu atau lebih target peninjauan dari `root_dir`, `root_dirs`, atau `groups`.
4. Secara opsional batasi file sumber dengan `--changed-from`.
5. Jalankan pemeriksaan deterministik untuk struktur, kesegaran terjemahan, integritas Markdown, dan jalur tautan/gambar lokal.
6. Mencetak keluaran teks atau Markdown bergaya GitHub.
7. Keluar dengan kegagalan saat ditemukan kesalahan peninjauan.

Alur peninjauan tidak memerlukan kunci API dan tetap tersedia untuk pemeriksaan lokal atau CI konsumen yang bersifat opt-in. Repositori ini tidak menjalankan `co-op-review` secara otomatis pada setiap pull request.

## Situs dokumentasi

Situs dokumentasi dikonfigurasi oleh:

```text
mkdocs.yml
requirements-docs.txt
docs/
```

Direktori `docs/` adalah sumber dokumentasi kanonik. Jangan menambahkan panduan pengguna akhir baru di luar direktori ini kecuali proyek sengaja memperkenalkan permukaan dokumentasi lain yang dipublikasikan.

Build secara lokal:

```bash
python -m pip install -r requirements-docs.txt
python -m mkdocs build --strict
```

Preview secara lokal:

```bash
python -m mkdocs serve
```

Situs yang dihasilkan ditulis ke `site/`, yang diabaikan oleh git.

## Alur kerja GitHub Pages

`.github/workflows/docs.yml` membangun situs pada pull request dan menerapkannya pada push ke `main`.

Alur kerja menginstal:

```bash
pip install -r requirements-docs.txt
```

Alur kerja docs hanya menginstal rangkaian alat dokumentasi. `mkdocs.yml` mengarahkan `mkdocstrings` ke `src/` sehingga halaman API publik dapat dirender dari tree sumber tanpa menginstal semua dependensi runtime. Jika dokumentasi API di masa depan memerlukan impor penyedia runtime opsional selama proses build, perbarui baik `.github/workflows/docs.yml` maupun panduan ini bersama-sama.

## Standar kualitas dokumentasi

Sebelum menggabungkan perubahan dokumentasi, jalankan:

```bash
python -m mkdocs build --strict
git diff --check
```

Gunakan build ketat sehingga tautan yang rusak, entri navigasi yang tidak valid, dan masalah perenderan API gagal sedini mungkin.