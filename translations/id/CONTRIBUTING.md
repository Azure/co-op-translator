<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "758ca1c5ae0d32c52d2dd59132dcfbf0",
  "translation_date": "2025-11-30T11:48:01+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "id"
}
-->
# Berkontribusi ke Co-op Translator

Proyek ini menerima kontribusi dan saran. Sebagian besar kontribusi mengharuskan Anda menyetujui
Contributor License Agreement (CLA) yang menyatakan bahwa Anda memiliki hak, dan memang memberikan kami
hak untuk menggunakan kontribusi Anda. Untuk detailnya, kunjungi https://cla.opensource.microsoft.com.

Saat Anda mengirimkan pull request, bot CLA akan secara otomatis menentukan apakah Anda perlu memberikan
CLA dan menandai PR dengan tepat (misalnya, pemeriksaan status, komentar). Cukup ikuti instruksi
yang diberikan oleh bot. Anda hanya perlu melakukan ini sekali untuk semua repositori yang menggunakan CLA kami.

## Pengaturan lingkungan pengembangan

Untuk menyiapkan lingkungan pengembangan untuk proyek ini, kami menyarankan menggunakan Poetry untuk mengelola dependensi. Kami menggunakan `pyproject.toml` untuk mengelola dependensi proyek, jadi untuk menginstal dependensi, Anda harus menggunakan Poetry.

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

### Menginstal Paket dan Paket yang dibutuhkan

#### Menggunakan Poetry (dari pyproject.toml)

```bash
poetry install
```

### Pengujian manual

Sebelum mengirimkan PR, penting untuk menguji fungsi terjemahan dengan dokumentasi nyata:

1. Buat direktori test di direktori root:
    ```bash
    mkdir test_docs
    ```

2. Salin beberapa dokumentasi markdown dan gambar yang ingin Anda terjemahkan ke dalam direktori test. Contohnya:
    ```bash
    cp /path/to/your/docs/*.md test_docs/
    cp /path/to/your/images/*.png test_docs/
    ```

3. Instal paket secara lokal:
    ```bash
    pip install -e .
    ```

4. Jalankan Co-op Translator pada dokumen test Anda:
    ```bash
    python -m co_op_translator --language-codes ko --root-dir test_docs
    ```

5. Periksa file terjemahan di `test_docs/translations` dan `test_docs/translated_images` untuk memverifikasi:
   - Kualitas terjemahan
   - Komentar metadata sudah benar
   - Struktur markdown asli tetap terjaga
   - Tautan dan gambar berfungsi dengan baik

Pengujian manual ini membantu memastikan perubahan Anda bekerja dengan baik dalam skenario nyata.

### Variabel lingkungan

1. Buat file `.env` di direktori root dengan menyalin file `.env.template` yang disediakan.
1. Isi variabel lingkungan sesuai panduan.

> [!TIP]
>
> ### Opsi tambahan untuk lingkungan pengembangan
>
> Selain menjalankan proyek secara lokal, Anda juga dapat menggunakan GitHub Codespaces atau VS Code Dev Containers sebagai alternatif pengaturan lingkungan pengembangan.
>
> #### GitHub Codespaces
>
> Anda dapat menjalankan contoh ini secara virtual menggunakan GitHub Codespaces tanpa perlu pengaturan tambahan.
>
> Tombol ini akan membuka instance VS Code berbasis web di browser Anda:
>
> 1. Buka template (ini mungkin memakan waktu beberapa menit):
>
>     [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/azure/co-op-translator)
>
> #### Menjalankan secara Lokal menggunakan VS Code Dev Containers
>
> ⚠️ Opsi ini hanya akan berfungsi jika Docker Desktop Anda dialokasikan minimal 16 GB RAM. Jika Anda memiliki kurang dari 16 GB RAM, Anda bisa mencoba opsi [GitHub Codespaces](../..) atau [mengaturnya secara lokal](../..).
>
> Opsi terkait adalah VS Code Dev Containers, yang akan membuka proyek di VS Code lokal Anda menggunakan [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers):
>
> 1. Mulai Docker Desktop (instal jika belum terpasang)
> 2. Buka proyek:
>
>    [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator)


### Gaya Kode

Kami menggunakan [Black](https://github.com/psf/black) sebagai formatter kode Python untuk menjaga konsistensi gaya kode di seluruh proyek. Black adalah formatter kode yang tegas yang secara otomatis memformat ulang kode Python agar sesuai dengan gaya kode Black.

#### Konfigurasi

Konfigurasi Black ditentukan dalam `pyproject.toml` kami:

```toml
[tool.black]
line-length = 88
target-version = ['py310']
include = '\.pyi?$'
```

#### Menginstal Black

Anda dapat menginstal Black menggunakan Poetry (disarankan) atau pip:

##### Menggunakan Poetry

Black otomatis terinstal saat Anda menyiapkan lingkungan pengembangan:
```bash
poetry install
```

##### Menggunakan pip

Jika menggunakan pip, Anda dapat menginstal Black secara langsung:
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

2. Jalankan perintah berikut. Ganti `-l ko` dengan kode bahasa yang ingin Anda terjemahkan. Flag `-d` menunjukkan mode debug.

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> [!NOTE]
> Pastikan lingkungan Poetry Anda sudah aktif (poetry shell) sebelum menjalankan perintah.

## Berkontribusi bahasa baru

Kami menyambut kontribusi yang menambahkan dukungan untuk bahasa baru. Sebelum membuka PR, harap selesaikan langkah-langkah berikut untuk memastikan proses review berjalan lancar.

1. Tambahkan bahasa ke pemetaan font
   - Edit `src/co_op_translator/fonts/font_language_mappings.yml`
   - Tambahkan entri dengan:
     - `code`: kode bahasa mirip ISO (misalnya, `vi`)
     - `name`: nama tampilan yang mudah dipahami
     - `font`: font yang disertakan di `src/co_op_translator/fonts/` yang mendukung skrip tersebut
     - `rtl`: `true` jika bahasa ditulis dari kanan ke kiri, jika tidak `false`

2. Sertakan file font yang diperlukan (jika perlu)
   - Jika font baru diperlukan, pastikan lisensi kompatibel untuk distribusi open source
   - Tambahkan file font ke `src/co_op_translator/fonts/`

3. Verifikasi lokal
   - Jalankan terjemahan untuk contoh kecil (Markdown, gambar, dan notebook sesuai kebutuhan)
   - Verifikasi hasil output tampil dengan benar, termasuk font dan tata letak RTL jika berlaku

4. Perbarui dokumentasi
   - Pastikan bahasa muncul di `getting_started/supported-languages.md`
   - Tidak perlu mengubah `getting_started/README_languages_template.md`; file ini dihasilkan dari daftar bahasa yang didukung

5. Buka PR
   - Jelaskan bahasa yang ditambahkan dan pertimbangan font/lisensi jika ada
   - Lampirkan tangkapan layar hasil render jika memungkinkan

Contoh entri YAML:

```yaml
new_lang(code):
  name: "New Language"
  font: "NotoSans-Medium.ttf"
  rtl: false
```

### Uji bahasa baru

Anda dapat menguji bahasa baru dengan menjalankan perintah berikut:

```bash
# Buat dan aktifkan lingkungan virtual
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
# Instal paket pengembangan
pip install -e .
# Jalankan terjemahan
translate -l "new_lang"
```

## Pemelihara

### Pesan commit dan strategi Merge

Untuk memastikan konsistensi dan kejelasan dalam riwayat commit proyek kami, kami mengikuti format pesan commit tertentu **untuk pesan commit akhir** saat menggunakan strategi **Squash and Merge**.

Saat pull request (PR) digabungkan, commit individual akan digabung menjadi satu commit. Pesan commit akhir harus mengikuti format di bawah ini untuk menjaga riwayat yang bersih dan konsisten.

#### Format pesan commit (untuk squash and merge)

Kami menggunakan format berikut untuk pesan commit:

```bash
<type>: <description> (#<nomor PR>)
```

- **type**: Menentukan kategori commit. Kami menggunakan tipe berikut:
  - `Docs`: Untuk pembaruan dokumentasi.
  - `Build`: Untuk perubahan terkait sistem build atau dependensi, termasuk pembaruan file konfigurasi, workflow CI, atau Dockerfile.
  - `Core`: Untuk modifikasi fungsi inti proyek atau fitur, terutama yang melibatkan file di direktori `src/co_op_translator/core`.

- **description**: Ringkasan singkat perubahan.
- **PR number**: Nomor pull request terkait commit.

**Contoh**:

- `Docs: Perbarui instruksi instalasi agar lebih jelas (#50)`
- `Core: Tingkatkan penanganan terjemahan gambar (#60)`

> [!NOTE]
> Saat ini, prefix **`Docs`**, **`Core`**, dan **`Build`** secara otomatis ditambahkan ke judul PR berdasarkan label yang diterapkan pada kode sumber yang diubah. Selama label yang benar diterapkan, biasanya Anda tidak perlu memperbarui judul PR secara manual. Anda hanya perlu memeriksa bahwa semuanya benar dan prefix sudah dihasilkan dengan tepat.

#### Strategi Merge

Kami menggunakan **Squash and Merge** sebagai strategi default untuk pull request. Strategi ini memastikan pesan commit mengikuti format kami, meskipun commit individual tidak.

**Alasan**:

- Riwayat proyek yang bersih dan linear.
- Konsistensi dalam pesan commit.
- Mengurangi kebisingan dari commit kecil (misalnya, "perbaiki typo").

Saat menggabungkan, pastikan pesan commit akhir mengikuti format pesan commit yang dijelaskan di atas.

**Contoh Squash and Merge**
Jika sebuah PR berisi commit berikut:

- `perbaiki typo`
- `perbarui README`
- `sesuaikan format`

Maka akan digabung menjadi:
`Docs: Tingkatkan kejelasan dan format dokumentasi (#65)`

### Proses rilis

Bagian ini menjelaskan cara termudah bagi pemelihara untuk menerbitkan rilis baru Co-op Translator.

#### 1. Tingkatkan versi di `pyproject.toml`

1. Tentukan nomor versi berikutnya (kami mengikuti semantic versioning: `MAJOR.MINOR.PATCH`).
2. Edit `pyproject.toml` dan perbarui field `version` di bawah `[tool.poetry]`.
3. Buka pull request khusus yang hanya mengubah versi (dan file lock/metadata yang diperbarui otomatis, jika ada).
4. Setelah review, gunakan **Squash and Merge** dan pastikan pesan commit akhir mengikuti format yang dijelaskan di atas.

#### 2. Buat Rilis GitHub

1. Buka halaman repositori GitHub dan buka **Releases** → **Draft a new release**.
2. Buat tag baru (misalnya, `v0.13.0`) dari cabang `main`.
3. Setel judul rilis sama dengan versi (misalnya, `v0.13.0`).
4. Klik **Generate release notes** untuk mengisi changelog secara otomatis.
5. Opsional: edit teks (misalnya, untuk menyoroti bahasa baru yang didukung atau perubahan penting).
6. Publikasikan rilis.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berusaha untuk akurasi, harap diingat bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sahih. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau salah tafsir yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->