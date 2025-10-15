<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "510827ad22a2031a50838919c3594828",
  "translation_date": "2025-10-15T03:40:53+00:00",
  "source_file": "getting_started/command-line-guide/install-package.md",
  "language_code": "ms"
}
-->
# Pasang pakej Co-op Translator

**Co-op Translator** ialah alat antara muka baris arahan (CLI) yang direka untuk membantu anda menterjemah semua fail markdown dan imej dalam projek anda ke pelbagai bahasa. Tutorial ini akan membimbing anda untuk mengkonfigurasi penterjemah dan menjalankannya untuk pelbagai kegunaan.

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

Selepas mencipta persekitaran maya, anda perlu mengaktifkannya. Langkah-langkahnya berbeza mengikut sistem operasi anda. Taip arahan berikut dalam terminal anda.

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

1. Jika anda mencipta persekitaran dengan Poetry, taip arahan berikut dalam terminal anda untuk mengaktifkannya.

    ```bash
    poetry shell
    ```

### Memasang Pakej dan Pakej yang diperlukan

Setelah persekitaran maya anda disediakan dan diaktifkan, langkah seterusnya ialah memasang kebergantungan yang diperlukan.

### Pemasangan pantas

Pasang Co-Op Translator melalui pip

```
pip install co-op-translator
```
Atau

Pasang melalui poetry
```
poetry add co-op-translator
```

#### Menggunakan pip (daripada requirements.txt) jika anda klon repo ini

> [!NOTE]
> Sila JANGAN lakukan ini jika anda memasang co-op translator melalui pemasangan pantas.

1. Jika anda menggunakan pip, taip arahan berikut dalam terminal anda. Ia akan memasang secara automatik pakej yang diperlukan seperti yang dinyatakan dalam fail `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```

#### Menggunakan Poetry (daripada pyproject.toml)

1. Jika anda menggunakan Poetry, taip arahan berikut dalam terminal anda. Ia akan memasang secara automatik pakej yang diperlukan seperti yang dinyatakan dalam fail `pyproject.toml`:

    ```bash
    poetry install
    ```

---

**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat kritikal, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.