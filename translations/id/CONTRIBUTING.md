<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "bd4704f50c55da7d572b691484aa0b30",
  "translation_date": "2025-10-15T03:37:01+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "id"
}
-->
# Berkontribusi pada Co-op Translator

Proyek ini terbuka untuk kontribusi dan saran. Sebagian besar kontribusi mengharuskan Anda menyetujui
Contributor License Agreement (CLA) yang menyatakan bahwa Anda memiliki hak untuk, dan benar-benar memberikan kami,
hak untuk menggunakan kontribusi Anda. Untuk detailnya, kunjungi https://cla.opensource.microsoft.com.

Saat Anda mengirimkan pull request, bot CLA akan secara otomatis menentukan apakah Anda perlu memberikan
CLA dan menandai PR sesuai (misalnya, status check, komentar). Ikuti saja instruksi
yang diberikan oleh bot. Anda hanya perlu melakukannya sekali untuk semua repo yang menggunakan CLA kami.

## Pengaturan lingkungan pengembangan

Untuk menyiapkan lingkungan pengembangan proyek ini, kami merekomendasikan menggunakan Poetry untuk mengelola dependensi. Kami menggunakan `pyproject.toml` untuk mengelola dependensi proyek, jadi untuk menginstal dependensi, Anda sebaiknya menggunakan Poetry.

### Membuat virtual environment

#### Menggunakan pip

```bash
python -m venv .venv
```

#### Menggunakan Poetry

```bash
poetry init
```

### Mengaktifkan virtual environment

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

### Instalasi Paket dan Paket yang Dibutuhkan

#### Menggunakan Poetry (dari pyproject.toml)

```bash
poetry install
```

### Pengujian manual

Sebelum mengirimkan PR, penting untuk menguji fungsi terjemahan dengan dokumentasi nyata:

1. Buat direktori tes di direktori root:
    ```bash
    mkdir test_docs
    ```

2. Salin beberapa dokumentasi markdown dan gambar yang ingin Anda terjemahkan ke direktori tes. Contohnya:
    ```bash
    cp /path/to/your/docs/*.md test_docs/
    cp /path/to/your/images/*.png test_docs/
    ```

3. Instal paket secara lokal:
    ```bash
    pip install -e .
    ```

4. Jalankan Co-op Translator pada dokumen tes Anda:
    ```bash
    python -m co_op_translator --language-codes ko --root-dir test_docs
    ```

5. Periksa file hasil terjemahan di `test_docs/translations` dan `test_docs/translated_images` untuk memastikan:
   - Kualitas terjemahan
   - Komentar metadata sudah benar
   - Struktur markdown asli tetap terjaga
   - Tautan dan gambar berfungsi dengan baik

Pengujian manual ini membantu memastikan perubahan Anda berjalan baik di skenario nyata.

### Variabel lingkungan

1. Buat file `.env` di direktori root dengan menyalin file `.env.template` yang disediakan.
1. Isi variabel lingkungan sesuai petunjuk.

> [!TIP]
>
> ### Opsi tambahan untuk lingkungan pengembangan
>
> Selain menjalankan proyek secara lokal, Anda juga bisa menggunakan GitHub Codespaces atau VS Code Dev Containers sebagai alternatif pengaturan lingkungan pengembangan.
>
> #### GitHub Codespaces
>
> Anda dapat menjalankan contoh ini secara virtual menggunakan GitHub Codespaces tanpa pengaturan tambahan.
>
> Tombol berikut akan membuka VS Code berbasis web di browser Anda:
>
> 1. Buka template (proses ini mungkin memakan waktu beberapa menit):
>
>     [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/azure/co-op-translator)
>
> #### Menjalankan Secara Lokal menggunakan VS Code Dev Containers
>
> ⚠️ Opsi ini hanya berfungsi jika Docker Desktop Anda dialokasikan minimal 16 GB RAM. Jika RAM Anda kurang dari 16 GB, Anda bisa mencoba [opsi GitHub Codespaces](../..) atau [mengatur secara lokal](../..).
>
> Opsi terkait adalah VS Code Dev Containers, yang akan membuka proyek di VS Code lokal Anda menggunakan [ekstensi Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers):
>
> 1. Jalankan Docker Desktop (instal jika belum terpasang)
> 2. Buka proyek:
>
>    [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator)


### Gaya Kode

Kami menggunakan [Black](https://github.com/psf/black) sebagai formatter kode Python untuk menjaga konsistensi gaya kode di seluruh proyek. Black adalah formatter kode yang tegas dan otomatis memformat kode Python agar sesuai dengan gaya Black.

#### Konfigurasi

Konfigurasi Black ditentukan di `pyproject.toml` kami:

```toml
[tool.black]
line-length = 88
target-version = ['py310']
include = '\.pyi?$'
```

#### Instalasi Black

Anda dapat menginstal Black menggunakan Poetry (disarankan) atau pip:

##### Menggunakan Poetry

Black akan otomatis terinstal saat Anda menyiapkan lingkungan pengembangan:
```bash
poetry install
```

##### Menggunakan pip

Jika Anda menggunakan pip, Anda bisa menginstal Black secara langsung:
```bash
pip install black
```

#### Menggunakan Black

##### Dengan Poetry

1. Format semua file Python di proyek:
    ```bash
    poetry run black .
    ```

2. Format file atau direktori tertentu:
    ```bash
    poetry run black path/to/file_or_directory
    ```

##### Dengan pip

1. Format semua file Python di proyek:
    ```bash
    black .
    ```

2. Format file atau direktori tertentu:
    ```bash
    black path/to/file_or_directory
    ```

> [!TIP]
> Kami menyarankan Anda mengatur editor agar otomatis memformat kode dengan Black saat menyimpan. Sebagian besar editor modern mendukung ini melalui ekstensi atau plugin.

## Menjalankan Co-op Translator

Untuk menjalankan Co-op Translator menggunakan Poetry di lingkungan Anda, ikuti langkah-langkah berikut:

1. Masuk ke direktori tempat Anda ingin melakukan tes terjemahan atau buat folder sementara untuk keperluan tes.

2. Jalankan perintah berikut. Ganti `-l ko` dengan kode bahasa yang ingin Anda gunakan. Flag `-d` menandakan mode debug.

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> [!NOTE]
> Pastikan lingkungan Poetry Anda sudah aktif (poetry shell) sebelum menjalankan perintah.

## Kontribusi bahasa baru

Kami menerima kontribusi untuk menambah dukungan bahasa baru. Sebelum membuka PR, silakan selesaikan langkah-langkah berikut agar proses review berjalan lancar.

1. Tambahkan bahasa ke pemetaan font
   - Edit `src/co_op_translator/fonts/font_language_mappings.yml`
   - Tambahkan entri dengan:
     - `code`: kode bahasa mirip ISO (misal, `vi`)
     - `name`: nama tampilan yang mudah dibaca
     - `font`: font yang tersedia di `src/co_op_translator/fonts/` dan mendukung skrip tersebut
     - `rtl`: `true` jika kanan-ke-kiri, jika tidak `false`

2. Sertakan file font yang dibutuhkan (jika perlu)
   - Jika font baru diperlukan, pastikan lisensinya kompatibel untuk distribusi open source
   - Tambahkan file font ke `src/co_op_translator/fonts/`

3. Verifikasi lokal
   - Jalankan terjemahan untuk sampel kecil (Markdown, gambar, dan notebook sesuai kebutuhan)
   - Pastikan hasil output tampil dengan benar, termasuk font dan layout RTL jika berlaku

4. Perbarui dokumentasi
   - Pastikan bahasa muncul di `getting_started/supported-languages.md`
   - Tidak perlu mengubah `README_languages_template.md`; file ini dihasilkan dari daftar bahasa yang didukung

5. Buka PR
   - Jelaskan bahasa yang ditambahkan dan pertimbangan font/lisensi
   - Lampirkan screenshot hasil render jika memungkinkan

Contoh entri YAML:

```yaml
new_lang(code):
  name: "New Language"
  font: "NotoSans-Medium.ttf"
  rtl: false
```


## Maintainer

### Format pesan commit dan strategi merge

Untuk menjaga konsistensi dan kejelasan riwayat commit proyek, kami mengikuti format pesan commit khusus **untuk pesan commit akhir** saat menggunakan strategi **Squash and Merge**.

Saat pull request (PR) digabungkan, commit individual akan digabung menjadi satu commit. Pesan commit akhir harus mengikuti format di bawah ini agar riwayat tetap bersih dan konsisten.

#### Format pesan commit (untuk squash and merge)

Kami menggunakan format berikut untuk pesan commit:

```bash
<type>: <description> (#<PR number>)
```

- **type**: Menentukan kategori commit. Kami menggunakan tipe berikut:
  - `Docs`: Untuk pembaruan dokumentasi.
  - `Build`: Untuk perubahan terkait sistem build atau dependensi, termasuk pembaruan file konfigurasi, workflow CI, atau Dockerfile.
  - `Core`: Untuk modifikasi pada fungsi inti atau fitur proyek, terutama yang melibatkan file di direktori `src/co_op_translator/core`.

- **description**: Ringkasan singkat perubahan.
- **PR number**: Nomor pull request yang terkait dengan commit.

**Contoh**:

- `Docs: Update installation instructions for clarity (#50)`
- `Core: Improve handling of image translation (#60)`

> [!NOTE]
> Saat ini, prefix **`Docs`**, **`Core`**, dan **`Build`** otomatis ditambahkan ke judul PR berdasarkan label yang diterapkan pada kode sumber yang diubah. Selama label yang benar sudah diterapkan, Anda biasanya tidak perlu mengubah judul PR secara manual. Anda hanya perlu memastikan semuanya sudah benar dan prefix sudah dihasilkan dengan tepat.

#### Strategi merge

Kami menggunakan **Squash and Merge** sebagai strategi default untuk pull request. Strategi ini memastikan pesan commit mengikuti format kami, meskipun commit individual tidak.

**Alasan**:

- Riwayat proyek yang bersih dan linear.
- Konsistensi dalam pesan commit.
- Mengurangi noise dari commit kecil (misal, "fix typo").

Saat menggabungkan, pastikan pesan commit akhir mengikuti format yang dijelaskan di atas.

**Contoh Squash and Merge**
Jika PR berisi commit berikut:

- `fix typo`
- `update README`
- `adjust formatting`

Maka semuanya digabung menjadi:
`Docs: Improve documentation clarity and formatting (#65)`

---

**Disclaimer**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk memberikan terjemahan yang akurat, harap diketahui bahwa terjemahan otomatis dapat mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang berwenang. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa penerjemah profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang timbul dari penggunaan terjemahan ini.