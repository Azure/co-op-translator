<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "510827ad22a2031a50838919c3594828",
  "translation_date": "2025-10-15T03:38:29+00:00",
  "source_file": "getting_started/command-line-guide/install-package.md",
  "language_code": "id"
}
-->
# Instal paket Co-op translator

**Co-op Translator** adalah alat antarmuka baris perintah (CLI) yang dirancang untuk membantu Anda menerjemahkan semua file markdown dan gambar di proyek Anda ke berbagai bahasa. Tutorial ini akan memandu Anda dalam mengonfigurasi translator dan menjalankannya untuk berbagai kasus penggunaan.

### Membuat virtual environment

Anda dapat membuat virtual environment menggunakan `pip` atau `Poetry`. Ketik salah satu perintah berikut di terminal Anda.

#### Menggunakan pip

```bash
python -m venv .venv
```

#### Menggunakan Poetry

```bash
poetry init
```

### Aktifkan virtual environment

Setelah membuat virtual environment, Anda perlu mengaktifkannya. Langkah-langkahnya berbeda tergantung sistem operasi Anda. Ketik perintah berikut di terminal Anda.

#### Untuk pip dan Poetry

- Windows:

    ```bash
    .venv\Scripts\activate
    ```

- Mac/Linux:

    ```bash
    source .venv/bin/activate
    ```

#### Menggunakan Poetry

1. Jika Anda membuat environment dengan Poetry, ketik perintah berikut di terminal Anda untuk mengaktifkannya.

    ```bash
    poetry shell
    ```

### Instalasi Paket dan Paket yang Dibutuhkan

Setelah virtual environment Anda siap dan diaktifkan, langkah selanjutnya adalah menginstal dependensi yang diperlukan.

### Instalasi cepat

Instal Co-Op Translator melalui pip

```
pip install co-op-translator
```
Atau

Instal melalui poetry
```
poetry add co-op-translator
```

#### Menggunakan pip (dari requirements.txt) jika Anda mengkloning repo ini

> [!NOTE]
> Jangan lakukan ini jika Anda menginstal co-op translator melalui instalasi cepat.

1. Jika Anda menggunakan pip, ketik perintah berikut di terminal Anda. Ini akan secara otomatis menginstal paket yang diperlukan yang sudah ditentukan di file `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```

#### Menggunakan Poetry (dari pyproject.toml)

1. Jika Anda menggunakan Poetry, ketik perintah berikut di terminal Anda. Ini akan secara otomatis menginstal paket yang diperlukan yang sudah ditentukan di file `pyproject.toml`:

    ```bash
    poetry install
    ```

---

**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk memberikan terjemahan yang akurat, harap diketahui bahwa terjemahan otomatis dapat mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang berwenang. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa penerjemah profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang timbul dari penggunaan terjemahan ini.