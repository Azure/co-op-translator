<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "758ca1c5ae0d32c52d2dd59132dcfbf0",
  "translation_date": "2025-11-30T11:51:36+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "ms"
}
-->
# Menyumbang kepada Co-op Translator

Projek ini mengalu-alukan sumbangan dan cadangan. Kebanyakan sumbangan memerlukan anda bersetuju dengan Perjanjian Lesen Penyumbang (CLA) yang menyatakan bahawa anda mempunyai hak untuk, dan benar-benar memberikan kami hak untuk menggunakan sumbangan anda. Untuk maklumat lanjut, lawati https://cla.opensource.microsoft.com.

Apabila anda menghantar permintaan tarik (pull request), bot CLA akan secara automatik menentukan sama ada anda perlu menyediakan CLA dan menghias PR dengan sewajarnya (contohnya, pemeriksaan status, komen). Ikuti sahaja arahan yang diberikan oleh bot. Anda hanya perlu melakukan ini sekali sahaja untuk semua repositori yang menggunakan CLA kami.

## Persediaan persekitaran pembangunan

Untuk menyediakan persekitaran pembangunan bagi projek ini, kami mengesyorkan menggunakan Poetry untuk menguruskan kebergantungan. Kami menggunakan `pyproject.toml` untuk mengurus kebergantungan projek, oleh itu, untuk memasang kebergantungan, anda harus menggunakan Poetry.

### Membuat persekitaran maya

#### Menggunakan pip

```bash
python -m venv .venv
```

#### Menggunakan Poetry

```bash
poetry init
```

### Mengaktifkan persekitaran maya

#### Untuk kedua-dua pip dan Poetry

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

### Memasang Pakej dan Pakej yang diperlukan

#### Menggunakan Poetry (dari pyproject.toml)

```bash
poetry install
```

### Ujian manual

Sebelum menghantar PR, adalah penting untuk menguji fungsi terjemahan dengan dokumentasi sebenar:

1. Buat direktori ujian di direktori utama:
    ```bash
    mkdir test_docs
    ```

2. Salin beberapa dokumentasi markdown dan imej yang anda ingin terjemahkan ke dalam direktori ujian. Contohnya:
    ```bash
    cp /path/to/your/docs/*.md test_docs/
    cp /path/to/your/images/*.png test_docs/
    ```

3. Pasang pakej secara tempatan:
    ```bash
    pip install -e .
    ```

4. Jalankan Co-op Translator pada dokumen ujian anda:
    ```bash
    python -m co_op_translator --language-codes ko --root-dir test_docs
    ```

5. Semak fail terjemahan dalam `test_docs/translations` dan `test_docs/translated_images` untuk mengesahkan:
   - Kualiti terjemahan
   - Komen metadata adalah betul
   - Struktur markdown asal dikekalkan
   - Pautan dan imej berfungsi dengan baik

Ujian manual ini membantu memastikan perubahan anda berfungsi dengan baik dalam senario dunia sebenar.

### Pembolehubah persekitaran

1. Buat fail `.env` di direktori utama dengan menyalin fail `.env.template` yang disediakan.
1. Isikan pembolehubah persekitaran seperti yang diarahkan.

> [!TIP]
>
> ### Pilihan tambahan untuk persekitaran pembangunan
>
> Selain menjalankan projek secara tempatan, anda juga boleh menggunakan GitHub Codespaces atau VS Code Dev Containers sebagai alternatif penyediaan persekitaran pembangunan.
>
> #### GitHub Codespaces
>
> Anda boleh menjalankan contoh ini secara maya menggunakan GitHub Codespaces tanpa perlu tetapan atau persediaan tambahan.
>
> Butang ini akan membuka instans VS Code berasaskan web dalam pelayar anda:
>
> 1. Buka templat (ini mungkin mengambil masa beberapa minit):
>
>     [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/azure/co-op-translator)
>
> #### Menjalankan secara Tempatan menggunakan VS Code Dev Containers
>
> ⚠️ Pilihan ini hanya berfungsi jika Docker Desktop anda diperuntukkan sekurang-kurangnya 16 GB RAM. Jika anda mempunyai kurang daripada 16 GB RAM, anda boleh cuba pilihan [GitHub Codespaces](../..) atau [sediakan secara tempatan](../..).
>
> Pilihan berkaitan ialah VS Code Dev Containers, yang akan membuka projek dalam VS Code tempatan anda menggunakan [sambungan Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers):
>
> 1. Mulakan Docker Desktop (pasang jika belum dipasang)
> 2. Buka projek:
>
>    [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator)


### Gaya Kod

Kami menggunakan [Black](https://github.com/psf/black) sebagai pemformat kod Python kami untuk mengekalkan gaya kod yang konsisten di seluruh projek. Black adalah pemformat kod yang tegas yang secara automatik memformat semula kod Python supaya mematuhi gaya kod Black.

#### Konfigurasi

Konfigurasi Black ditentukan dalam `pyproject.toml` kami:

```toml
[tool.black]
line-length = 88
target-version = ['py310']
include = '\.pyi?$'
```

#### Memasang Black

Anda boleh memasang Black menggunakan sama ada Poetry (disyorkan) atau pip:

##### Menggunakan Poetry

Black dipasang secara automatik apabila anda menyediakan persekitaran pembangunan:
```bash
poetry install
```

##### Menggunakan pip

Jika anda menggunakan pip, anda boleh memasang Black secara langsung:
```bash
pip install black
```

#### Menggunakan Black

##### Dengan Poetry

1. Format semua fail Python dalam projek:
    ```bash
    poetry run black .
    ```

2. Format fail atau direktori tertentu:
    ```bash
    poetry run black path/to/file_or_directory
    ```

##### Dengan pip

1. Format semua fail Python dalam projek:
    ```bash
    black .
    ```

2. Format fail atau direktori tertentu:
    ```bash
    black path/to/file_or_directory
    ```

> [!TIP]
> Kami mengesyorkan anda menyediakan editor anda untuk memformat kod secara automatik dengan Black semasa menyimpan. Kebanyakan editor moden menyokong ini melalui sambungan atau plugin.

## Menjalankan Co-op Translator

Untuk menjalankan Co-op Translator menggunakan Poetry dalam persekitaran anda, ikut langkah berikut:

1. Navigasi ke direktori di mana anda ingin melakukan ujian terjemahan atau buat folder sementara untuk tujuan ujian.

2. Jalankan arahan berikut. Gantikan `-l ko` dengan kod bahasa yang anda ingin terjemahkan. Flag `-d` menunjukkan mod debug.

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> [!NOTE]
> Pastikan persekitaran Poetry anda diaktifkan (poetry shell) sebelum menjalankan arahan.

## Menyumbang bahasa baru

Kami mengalu-alukan sumbangan yang menambah sokongan untuk bahasa baru. Sebelum membuka PR, sila lengkapkan langkah di bawah untuk memastikan proses semakan berjalan lancar.

1. Tambah bahasa ke pemetaan fon
   - Edit `src/co_op_translator/fonts/font_language_mappings.yml`
   - Tambah entri dengan:
     - `code`: kod bahasa seperti ISO (contohnya, `vi`)
     - `name`: nama paparan mesra pengguna
     - `font`: Fon yang disertakan dalam `src/co_op_translator/fonts/` yang menyokong skrip tersebut
     - `rtl`: `true` jika kanan ke kiri, jika tidak `false`

2. Sertakan fail fon yang diperlukan (jika perlu)
   - Jika fon baru diperlukan, sahkan keserasian lesen untuk pengedaran sumber terbuka
   - Tambah fail fon ke `src/co_op_translator/fonts/`

3. Pengesahan tempatan
   - Jalankan terjemahan untuk sampel kecil (Markdown, imej, dan notebook jika sesuai)
   - Sahkan output dipaparkan dengan betul, termasuk fon dan sebarang susun atur RTL jika berkenaan

4. Kemas kini dokumentasi
   - Pastikan bahasa tersebut muncul dalam `getting_started/supported-languages.md`
   - Tiada perubahan diperlukan pada `getting_started/README_languages_template.md`; ia dijana dari senarai yang disokong

5. Buka PR
   - Terangkan bahasa yang ditambah dan sebarang pertimbangan fon/lesen
   - Lampirkan tangkapan skrin output yang dipaparkan jika boleh

Contoh entri YAML:

```yaml
new_lang(code):
  name: "New Language"
  font: "NotoSans-Medium.ttf"
  rtl: false
```

### Uji bahasa baru

Anda boleh menguji bahasa baru dengan menjalankan arahan berikut:

```bash
# Cipta dan aktifkan persekitaran maya
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
# Pasang pakej pembangunan
pip install -e .
# Jalankan terjemahan
translate -l "new_lang"
```

## Penyelenggara

### Mesej komit dan Strategi Penggabungan

Untuk memastikan konsistensi dan kejelasan dalam sejarah komit projek kami, kami mengikuti format mesej komit tertentu **untuk mesej komit akhir** apabila menggunakan strategi **Squash and Merge**.

Apabila permintaan tarik (PR) digabungkan, komit individu akan digabungkan menjadi satu komit. Mesej komit akhir harus mengikuti format di bawah untuk mengekalkan sejarah yang kemas dan konsisten.

#### Format mesej komit (untuk squash and merge)

Kami menggunakan format berikut untuk mesej komit:

```bash
<type>: <description> (#<nombor PR>)
```

- **type**: Menentukan kategori komit. Kami menggunakan jenis berikut:
  - `Docs`: Untuk kemas kini dokumentasi.
  - `Build`: Untuk perubahan berkaitan sistem binaan atau kebergantungan, termasuk kemas kini fail konfigurasi, aliran kerja CI, atau Dockerfile.
  - `Core`: Untuk pengubahsuaian fungsi teras projek atau ciri, terutamanya yang melibatkan fail dalam direktori `src/co_op_translator/core`.

- **description**: Ringkasan ringkas perubahan.
- **PR number**: Nombor permintaan tarik yang berkaitan dengan komit.

**Contoh**:

- `Docs: Kemas kini arahan pemasangan untuk kejelasan (#50)`
- `Core: Tingkatkan pengendalian terjemahan imej (#60)`

> [!NOTE]
> Pada masa ini, awalan **`Docs`**, **`Core`**, dan **`Build`** ditambah secara automatik pada tajuk PR berdasarkan label yang digunakan pada kod sumber yang diubah. Selagi label yang betul digunakan, anda biasanya tidak perlu mengemas kini tajuk PR secara manual. Anda hanya perlu mengesahkan bahawa semuanya betul dan awalan telah dijana dengan sewajarnya.

#### Strategi penggabungan

Kami menggunakan **Squash and Merge** sebagai strategi lalai untuk permintaan tarik. Strategi ini memastikan mesej komit mengikuti format kami, walaupun komit individu tidak.

**Sebab**:

- Sejarah projek yang bersih dan linear.
- Konsistensi dalam mesej komit.
- Mengurangkan gangguan dari komit kecil (contohnya, "betulkan typo").

Apabila menggabungkan, pastikan mesej komit akhir mengikuti format mesej komit yang diterangkan di atas.

**Contoh Squash and Merge**
Jika PR mengandungi komit berikut:

- `betulkan typo`
- `kemas kini README`
- `laraskan format`

Ia harus digabungkan menjadi:
`Docs: Tingkatkan kejelasan dan format dokumentasi (#65)`

### Proses pelepasan

Bahagian ini menerangkan cara paling mudah untuk penyelenggara menerbitkan pelepasan baru Co-op Translator.

#### 1. Tingkatkan versi dalam `pyproject.toml`

1. Tentukan nombor versi seterusnya (kami mengikuti penomboran versi semantik: `MAJOR.MINOR.PATCH`).
2. Edit `pyproject.toml` dan kemas kini medan `version` di bawah `[tool.poetry]`.
3. Buka permintaan tarik khusus yang hanya mengubah versi (dan mana-mana fail kunci/metadata yang dikemas kini secara automatik, jika ada).
4. Selepas semakan, gunakan **Squash and Merge** dan pastikan mesej komit akhir mengikuti format yang diterangkan di atas.

#### 2. Buat Pelepasan GitHub

1. Pergi ke halaman repositori GitHub dan buka **Releases** → **Draft a new release**.
2. Buat tag baru (contohnya, `v0.13.0`) dari cawangan `main`.
3. Tetapkan tajuk pelepasan kepada versi yang sama (contohnya, `v0.13.0`).
4. Klik **Generate release notes** untuk mengisi changelog secara automatik.
5. Pilihan untuk mengedit teks (contohnya, untuk menonjolkan bahasa baru yang disokong atau perubahan penting).
6. Terbitkan pelepasan.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->