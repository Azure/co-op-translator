<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b6d85d887d2664539a438dae5d0dfa50",
  "translation_date": "2025-06-12T18:36:15+00:00",
  "source_file": "getting_started/command-line-guide/install-package.md",
  "language_code": "id"
}
-->
# Instal paket Co-op translator

**Co-op Translator** adalah alat antarmuka baris perintah (CLI) yang dirancang untuk membantu Anda menerjemahkan semua file markdown dan gambar dalam proyek Anda ke dalam berbagai bahasa. Tutorial ini akan memandu Anda dalam mengonfigurasi translator dan menjalankannya untuk berbagai kasus penggunaan.

### Buat lingkungan virtual

Anda dapat membuat lingkungan virtual menggunakan `pip` atau `Poetry`. Ketik salah satu perintah berikut di terminal Anda.

#### Menggunakan pip

```bash
python -m venv .venv
```

#### Menggunakan Poetry

```bash
poetry init
```

### Aktifkan lingkungan virtual

Setelah membuat lingkungan virtual, Anda perlu mengaktifkannya. Langkah-langkahnya berbeda tergantung pada sistem operasi Anda. Ketik perintah berikut di terminal Anda.

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

1. Jika Anda membuat lingkungan dengan Poetry, ketik perintah berikut di terminal untuk mengaktifkannya.

    ```bash
    poetry shell
    ```

### Instal Paket dan paket yang dibutuhkan

Setelah lingkungan virtual Anda siap dan aktif, langkah berikutnya adalah menginstal dependensi yang diperlukan.

### Instal cepat

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

![NOTE] Harap JANGAN lakukan ini jika Anda menginstal co-op translator melalui instalasi cepat.

1. Jika Anda menggunakan pip, ketik perintah berikut di terminal Anda. Ini akan secara otomatis menginstal paket yang dibutuhkan yang tercantum dalam file `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```

#### Menggunakan Poetry (dari pyproject.toml)

1. Jika Anda menggunakan Poetry, ketik perintah berikut di terminal Anda. Ini akan secara otomatis menginstal paket yang dibutuhkan yang tercantum dalam file `pyproject.toml`:

    ```bash
    poetry install
    ```

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berusaha untuk akurasi, harap diperhatikan bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang salah yang timbul dari penggunaan terjemahan ini.