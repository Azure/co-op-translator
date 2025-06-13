<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b6d85d887d2664539a438dae5d0dfa50",
  "translation_date": "2025-06-12T18:36:23+00:00",
  "source_file": "getting_started/command-line-guide/install-package.md",
  "language_code": "ms"
}
-->
# Pasang pakej penterjemah Co-op

**Co-op Translator** adalah alat antara muka baris perintah (CLI) yang direka untuk membantu anda menterjemah semua fail markdown dan imej dalam projek anda ke dalam pelbagai bahasa. Tutorial ini akan membimbing anda cara mengkonfigurasi penterjemah dan menjalankannya untuk pelbagai kegunaan.

### Cipta persekitaran maya

Anda boleh mencipta persekitaran maya menggunakan sama ada `pip` atau `Poetry`. Taip salah satu arahan berikut dalam terminal anda.

#### Menggunakan pip

```bash
python -m venv .venv
```

#### Menggunakan Poetry

```bash
poetry init
```

### Aktifkan persekitaran maya

Selepas mencipta persekitaran maya, anda perlu mengaktifkannya. Langkah-langkah berbeza mengikut sistem operasi anda. Taip arahan berikut dalam terminal anda.

#### Untuk kedua-dua pip dan Poetry

- Windows:

    ```bash
    .venv\Scripts\activate
    ```

- Mac/Linux:

    ```bash
    source .venv/bin/activate
    ```

#### Menggunakan Poetry

1. Jika anda mencipta persekitaran dengan Poetry, taip arahan berikut dalam terminal untuk mengaktifkannya.

    ```bash
    poetry shell
    ```

### Pasang Pakej dan pakej yang diperlukan

Setelah persekitaran maya anda disediakan dan diaktifkan, langkah seterusnya ialah memasang kebergantungan yang diperlukan.

### Pasang dengan cepat

Pasang melalui Co-Op Translator menggunakan pip

```
pip install co-op-translator
```
Atau

Pasang menggunakan poetry
```
poetry add co-op-translator
```

#### Menggunakan pip (dari requirements.txt) jika anda klon repo ini

![NOTE] Sila JANGAN lakukan ini jika anda memasang co-op translator melalui pemasangan cepat.

1. Jika anda menggunakan pip, taip arahan berikut dalam terminal anda. Ia akan memasang secara automatik pakej yang diperlukan yang dinyatakan dalam fail `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```

#### Menggunakan Poetry (dari pyproject.toml)

1. Jika anda menggunakan Poetry, taip arahan berikut dalam terminal anda. Ia akan memasang secara automatik pakej yang diperlukan yang dinyatakan dalam fail `pyproject.toml`:

    ```bash
    poetry install
    ```

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.