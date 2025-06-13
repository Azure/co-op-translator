<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d95d7ec0097c5569ac16dd42840787a2",
  "translation_date": "2025-06-12T09:39:22+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "id"
}
-->
# Berkontribusi pada Co-op Translator

Proyek ini menerima kontribusi dan saran. Sebagian besar kontribusi mengharuskan Anda menyetujui  
Contributor License Agreement (CLA) yang menyatakan bahwa Anda memiliki hak, dan memang memberikan,  
izin kepada kami untuk menggunakan kontribusi Anda. Untuk detailnya, kunjungi https://cla.opensource.microsoft.com.

Saat Anda mengirim pull request, bot CLA akan secara otomatis menentukan apakah Anda perlu menyediakan  
CLA dan menghias PR dengan tepat (misalnya, pemeriksaan status, komentar). Cukup ikuti instruksi yang  
diberikan oleh bot. Anda hanya perlu melakukan ini sekali untuk semua repositori yang menggunakan CLA kami.

## Pengaturan lingkungan pengembangan

Untuk mengatur lingkungan pengembangan proyek ini, kami merekomendasikan menggunakan Poetry untuk mengelola dependensi. Kami menggunakan `pyproject.toml` untuk mengelola dependensi proyek, jadi untuk memasang dependensi, Anda harus menggunakan Poetry.

### Membuat lingkungan virtual

#### Menggunakan pip

```bash
python -m venv .venv
```

#### Menggunakan Poetry

```bash
poetry init
```

### Mengaktifkan lingkungan virtual

#### Untuk pip dan Poetry

- Windows:

    ```bash
    .venv\Scripts\activate.bat
    ```

- Mac/Linux:

    ```bash
    source .venv/bin/activate
    ```

#### Menggunakan Poetry

```bash
poetry shell
```

### Memasang Paket dan Paket yang diperlukan

#### Menggunakan Poetry (dari pyproject.toml)

```bash
poetry install
```

### Pengujian manual

Sebelum mengirim PR, penting untuk menguji fungsi terjemahan dengan dokumentasi nyata:

1. Buat direktori test di direktori root:  
    ```bash
    mkdir test_docs
    ```

2. Salin beberapa dokumentasi markdown dan gambar yang ingin Anda terjemahkan ke direktori test. Misalnya:  
    ```bash
    cp /path/to/your/docs/*.md test_docs/
    cp /path/to/your/images/*.png test_docs/
    ```

3. Pasang paket secara lokal:  
    ```bash
    pip install -e .
    ```

4. Jalankan Co-op Translator pada dokumen test Anda:  
    ```bash
    python -m co_op_translator --language-codes ko --root-dir test_docs
    ```

5. Periksa file terjemahan di `test_docs/translations` and `test_docs/translated_images` to verify:
   - The translation quality
   - The metadata comments are correct
   - The original markdown structure is preserved
   - Links and images are working properly

This manual testing helps ensure that your changes work well in real-world scenarios.

### Environment variables

1. Create an `.env` file in the root directory by copying the provided `.env.template`.  
1. Isi variabel lingkungan sesuai panduan.

> [!TIP]
>
> ### Pilihan tambahan untuk lingkungan pengembangan
>
> Selain menjalankan proyek secara lokal, Anda juga dapat menggunakan GitHub Codespaces atau VS Code Dev Containers sebagai alternatif pengaturan lingkungan pengembangan.
>
> #### GitHub Codespaces
>
> Anda dapat menjalankan contoh ini secara virtual dengan menggunakan GitHub Codespaces tanpa perlu pengaturan tambahan.
>
> Tombol ini akan membuka instance VS Code berbasis web di browser Anda:
>
> 1. Buka template (ini mungkin memerlukan beberapa menit):
>
>     [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/azure/co-op-translator)
>
> #### Menjalankan secara lokal menggunakan VS Code Dev Containers
>
> ⚠️ Opsi ini hanya akan berfungsi jika Docker Desktop Anda dialokasikan minimal 16 GB RAM. Jika RAM Anda kurang dari 16 GB, Anda bisa mencoba opsi [GitHub Codespaces](../..) atau [mengaturnya secara lokal](../..).
>
> Opsi terkait adalah VS Code Dev Containers, yang akan membuka proyek di VS Code lokal Anda menggunakan [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers):
>
> 1. Mulai Docker Desktop (pasang jika belum terpasang)  
> 2. Buka proyek:  
>
>    [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator)


### Gaya Kode

Kami menggunakan [Black](https://github.com/psf/black) sebagai formatter kode Python untuk menjaga konsistensi gaya kode di seluruh proyek. Black adalah formatter kode tanpa kompromi yang secara otomatis memformat ulang kode Python agar sesuai dengan gaya kode Black.

#### Konfigurasi

Konfigurasi Black ditentukan dalam `pyproject.toml` kami:

```toml
[tool.black]
line-length = 88
target-version = ['py310']
include = '\.pyi?$'
```

#### Memasang Black

Anda dapat memasang Black menggunakan Poetry (direkomendasikan) atau pip:

##### Menggunakan Poetry

Black otomatis terpasang saat Anda mengatur lingkungan pengembangan:  
```bash
poetry install
```

##### Menggunakan pip

Jika menggunakan pip, Anda bisa memasang Black secara langsung:  
```bash
pip install black
```

#### Menggunakan Black

##### Dengan Poetry

1. Format semua file Python dalam proyek:  
    ```bash
    poetry run black .
    ```

2. Format file atau direktori tertentu:  
    ```bash
    poetry run black path/to/file_or_directory
    ```

##### Dengan pip

1. Format semua file Python dalam proyek:  
    ```bash
    black .
    ```

2. Format file atau direktori tertentu:  
    ```bash
    black path/to/file_or_directory
    ```

> [!TIP]
> Kami menyarankan mengatur editor Anda agar secara otomatis memformat kode dengan Black saat menyimpan. Sebagian besar editor modern mendukung ini melalui ekstensi atau plugin.

## Menjalankan Co-op Translator

Untuk menjalankan Co-op Translator menggunakan Poetry di lingkungan Anda, ikuti langkah-langkah berikut:

1. Arahkan ke direktori tempat Anda ingin melakukan pengujian terjemahan atau buat folder sementara untuk tujuan pengujian.

2. Jalankan perintah berikut. Ganti `-l ko` with the language code you wish to translate into. The `-d` menunjukkan mode debug.

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> [!NOTE]
> Pastikan lingkungan Poetry Anda sudah aktif (poetry shell) sebelum menjalankan perintah.

## Pemelihara

### Pesan commit dan strategi Merge

Untuk memastikan konsistensi dan kejelasan dalam riwayat commit proyek kami, kami mengikuti format pesan commit tertentu **untuk pesan commit akhir** saat menggunakan strategi **Squash and Merge**.

Saat pull request (PR) digabungkan, commit individu akan digabung menjadi satu commit. Pesan commit akhir harus mengikuti format di bawah ini untuk menjaga riwayat yang bersih dan konsisten.

#### Format pesan commit (untuk squash dan merge)

Kami menggunakan format berikut untuk pesan commit:

```bash
<type>: <description> (#<PR number>)
```

- **type**: Menentukan kategori commit. Kami menggunakan tipe berikut:  
  - `Docs`: For documentation updates.
  - `Build`: For changes related to the build system or dependencies, including updates to configuration files, CI workflows, or the Dockerfile.
  - `Core`: For modifications to the project's core functionality or features, particularly those involving files in the `src/co_op_translator/core` directory.

- **description**: A concise summary of the change.
- **PR number**: The number of the pull request associated with the commit.

**Examples**:

- `Docs: Update installation instructions for clarity (#50)`
- `Core: Improve handling of image translation (#60)`

> [!NOTE]
> Currently, the **`Docs`**, **`Core`**, and **`Build`** prefixes are automatically added to PR titles based on the labels applied to the modified source code. As long as the correct label is applied, you typically don't need to manually update the PR title. You just need to verify that everything is correct and the prefix has been generated appropriately.

#### Merge strategy

We use **Squash and Merge** as our default strategy for pull requests. This strategy ensures that commit messages follow our format, even if individual commits don't.

**Reasons**:

- A clean, linear project history.
- Consistency in commit messages.
- Reduced noise from minor commits (e.g., "fix typo").

When merging, ensure the final commit message follows the commit message format described above.

**Example of Squash and Merge**
If a PR contains the following commits:

- `fix typo`
- `update README`
- `adjust formatting`

They should be squashed into:
`Docs: Improve documentation clarity and formatting (#65)`

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berusaha untuk akurasi, harap diperhatikan bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sahih. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau kesalahan tafsir yang timbul dari penggunaan terjemahan ini.