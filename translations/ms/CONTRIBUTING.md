<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "bd4704f50c55da7d572b691484aa0b30",
  "translation_date": "2025-10-15T03:39:24+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "ms"
}
-->
# Menyumbang kepada Co-op Translator

Projek ini mengalu-alukan sumbangan dan cadangan. Kebanyakan sumbangan memerlukan anda bersetuju dengan
Perjanjian Lesen Penyumbang (CLA) yang mengesahkan anda mempunyai hak untuk, dan benar-benar memberikan kami
hak untuk menggunakan sumbangan anda. Untuk maklumat lanjut, lawati https://cla.opensource.microsoft.com.

Apabila anda menghantar pull request, bot CLA akan secara automatik menentukan sama ada anda perlu menyediakan
CLA dan menghias PR dengan sewajarnya (contohnya, status check, komen). Ikuti sahaja arahan
yang diberikan oleh bot. Anda hanya perlu melakukannya sekali untuk semua repo yang menggunakan CLA kami.

## Persediaan persekitaran pembangunan

Untuk menyediakan persekitaran pembangunan bagi projek ini, kami mengesyorkan menggunakan Poetry untuk mengurus kebergantungan. Kami menggunakan `pyproject.toml` untuk mengurus kebergantungan projek, jadi untuk memasang kebergantungan, anda perlu menggunakan Poetry.

### Cipta persekitaran maya

#### Menggunakan pip

```bash
python -m venv .venv
```

#### Menggunakan Poetry

```bash
poetry init
```

### Aktifkan persekitaran maya

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

### Memasang Pakej dan Pakej yang diperlukan

#### Menggunakan Poetry (daripada pyproject.toml)

```bash
poetry install
```

### Ujian manual

Sebelum menghantar PR, adalah penting untuk menguji fungsi terjemahan dengan dokumentasi sebenar:

1. Cipta direktori ujian di direktori root:
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

5. Semak fail terjemahan dalam `test_docs/translations` dan `test_docs/translated_images` untuk memastikan:
   - Kualiti terjemahan
   - Komen metadata adalah betul
   - Struktur markdown asal dikekalkan
   - Pautan dan imej berfungsi dengan baik

Ujian manual ini membantu memastikan perubahan anda berfungsi dengan baik dalam situasi sebenar.

### Pembolehubah persekitaran

1. Cipta fail `.env` di direktori root dengan menyalin fail `.env.template` yang disediakan.
1. Isikan pembolehubah persekitaran seperti yang diarahkan.

> [!TIP]
>
> ### Pilihan tambahan untuk persekitaran pembangunan
>
> Selain menjalankan projek secara tempatan, anda juga boleh menggunakan GitHub Codespaces atau VS Code Dev Containers sebagai pilihan alternatif untuk persediaan persekitaran pembangunan.
>
> #### GitHub Codespaces
>
> Anda boleh menjalankan contoh ini secara maya menggunakan GitHub Codespaces tanpa sebarang tetapan tambahan.
>
> Butang ini akan membuka VS Code berasaskan web dalam pelayar anda:
>
> 1. Buka templat (ini mungkin mengambil masa beberapa minit):
>
>     <a href="https://codespaces.new/azure/co-op-translator"><img src="https://github.com/codespaces/badge.svg" alt="Open in GitHub Codespaces"></a>
>
> #### Jalankan Secara Tempatan menggunakan VS Code Dev Containers
>
> ⚠️ Pilihan ini hanya berfungsi jika Docker Desktop anda diperuntukkan sekurang-kurangnya 16 GB RAM. Jika anda mempunyai kurang daripada 16 GB RAM, anda boleh cuba [pilihan GitHub Codespaces](../..) atau [sediakan secara tempatan](../..).
>
> Pilihan berkaitan ialah VS Code Dev Containers, yang akan membuka projek dalam VS Code tempatan anda menggunakan [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers):
>
> 1. Mulakan Docker Desktop (pasang jika belum dipasang)
> 2. Buka projek:
>
>    <a href="https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator"><img src="https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode" alt="Open in Dev Containers"></a>


### Gaya Kod

Kami menggunakan [Black](https://github.com/psf/black) sebagai pemformat kod Python untuk mengekalkan gaya kod yang konsisten di seluruh projek. Black ialah pemformat kod yang tegas dan akan memformat semula kod Python secara automatik mengikut gaya Black.

#### Konfigurasi

Konfigurasi Black ditetapkan dalam `pyproject.toml` kami:

```toml
[tool.black]
line-length = 88
target-version = ['py310']
include = '\.pyi?$'
```

#### Memasang Black

Anda boleh memasang Black menggunakan Poetry (disyorkan) atau pip:

##### Menggunakan Poetry

Black akan dipasang secara automatik apabila anda menyediakan persekitaran pembangunan:
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
> Kami mengesyorkan anda menetapkan editor anda untuk memformat kod secara automatik dengan Black setiap kali anda menyimpan. Kebanyakan editor moden menyokong ciri ini melalui sambungan atau plugin.

## Menjalankan Co-op Translator

Untuk menjalankan Co-op Translator menggunakan Poetry dalam persekitaran anda, ikuti langkah berikut:

1. Pergi ke direktori di mana anda ingin melakukan ujian terjemahan atau cipta folder sementara untuk tujuan ujian.

2. Jalankan arahan berikut. Gantikan `-l ko` dengan kod bahasa yang anda ingin terjemahkan. Flag `-d` menandakan mod debug.

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> [!NOTE]
> Pastikan persekitaran Poetry anda telah diaktifkan (poetry shell) sebelum menjalankan arahan.

## Menyumbang bahasa baru

Kami mengalu-alukan sumbangan untuk menambah sokongan bahasa baru. Sebelum membuka PR, sila lengkapkan langkah di bawah untuk memastikan proses semakan berjalan lancar.

1. Tambah bahasa ke pemetaan fon
   - Edit `src/co_op_translator/fonts/font_language_mappings.yml`
   - Tambah entri dengan:
     - `code`: Kod bahasa berformat ISO (contoh: `vi`)
     - `name`: Nama paparan mesra pengguna
     - `font`: Fon yang terdapat dalam `src/co_op_translator/fonts/` dan menyokong skrip tersebut
     - `rtl`: `true` jika kanan-ke-kiri, jika tidak `false`

2. Sertakan fail fon yang diperlukan (jika perlu)
   - Jika fon baru diperlukan, pastikan lesen sesuai untuk pengedaran sumber terbuka
   - Tambah fail fon ke `src/co_op_translator/fonts/`

3. Pengesahan secara tempatan
   - Jalankan terjemahan untuk sampel kecil (Markdown, imej, dan notebook jika berkaitan)
   - Pastikan output dipaparkan dengan betul, termasuk fon dan susun atur RTL jika berkenaan

4. Kemas kini dokumentasi
   - Pastikan bahasa tersebut disenaraikan dalam `getting_started/supported-languages.md`
   - Tiada perubahan diperlukan pada `README_languages_template.md`; ia dijana daripada senarai sokongan

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


## Penyelenggara

### Format mesej komit dan strategi penggabungan

Untuk memastikan konsistensi dan kejelasan dalam sejarah komit projek, kami mengikuti format mesej komit tertentu **untuk mesej komit akhir** apabila menggunakan strategi **Squash and Merge**.

Apabila pull request (PR) digabungkan, semua komit individu akan digabungkan menjadi satu komit. Mesej komit akhir perlu mengikuti format di bawah untuk mengekalkan sejarah yang bersih dan konsisten.

#### Format mesej komit (untuk squash and merge)

Kami menggunakan format berikut untuk mesej komit:

```bash
<type>: <description> (#<PR number>)
```

- **type**: Menentukan kategori komit. Kami menggunakan jenis berikut:
  - `Docs`: Untuk kemas kini dokumentasi.
  - `Build`: Untuk perubahan berkaitan sistem binaan atau kebergantungan, termasuk kemas kini fail konfigurasi, workflow CI, atau Dockerfile.
  - `Core`: Untuk perubahan pada fungsi utama projek atau ciri, terutamanya yang melibatkan fail dalam direktori `src/co_op_translator/core`.

- **description**: Ringkasan perubahan secara padat.
- **PR number**: Nombor pull request yang berkaitan dengan komit.

**Contoh**:

- `Docs: Kemas kini arahan pemasangan untuk lebih jelas (#50)`
- `Core: Penambahbaikan pengendalian terjemahan imej (#60)`

> [!NOTE]
> Pada masa ini, awalan **`Docs`**, **`Core`**, dan **`Build`** akan ditambah secara automatik pada tajuk PR berdasarkan label yang digunakan pada kod sumber yang diubah. Selagi label yang betul digunakan, anda biasanya tidak perlu mengemas kini tajuk PR secara manual. Anda hanya perlu memastikan semuanya betul dan awalan telah dijana dengan betul.

#### Strategi penggabungan

Kami menggunakan **Squash and Merge** sebagai strategi lalai untuk pull request. Strategi ini memastikan mesej komit mengikut format kami, walaupun komit individu tidak.

**Sebab**:

- Sejarah projek yang bersih dan linear.
- Konsistensi dalam mesej komit.
- Mengurangkan gangguan daripada komit kecil (contohnya, "betulkan typo").

Semasa menggabungkan, pastikan mesej komit akhir mengikut format yang diterangkan di atas.

**Contoh Squash and Merge**
Jika PR mengandungi komit berikut:

- `betulkan typo`
- `kemas kini README`
- `ubah suai format`

Ia perlu digabungkan menjadi:
`Docs: Penambahbaikan kejelasan dan format dokumentasi (#65)`

---

**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat kritikal, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.