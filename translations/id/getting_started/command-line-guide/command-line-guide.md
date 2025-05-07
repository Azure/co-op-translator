<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d8eec418d6325416b9fab19a2dfcbf41",
  "translation_date": "2025-05-06T17:53:07+00:00",
  "source_file": "getting_started/command-line-guide/command-line-guide.md",
  "language_code": "id"
}
-->
# Cara menggunakan antarmuka baris perintah Co-op Translator (CLI)

## Prasyarat

- **Python 3.10 atau lebih tinggi**: Dibutuhkan untuk menjalankan Co-op Translator.  
- **Sumber Daya Model Bahasa**:  
  - **Azure OpenAI** atau LLM lainnya. Detail dapat ditemukan di [supported models and services](../../../../README.md).  
- **Sumber Daya Computer Vision** (opsional):  
  - Untuk penerjemahan gambar. Jika tidak tersedia, penerjemah akan menggunakan [Markdown-only mode](../markdown-only-mode.md).  
  - **Azure Computer Vision**

### Pengaturan Awal

Sebelum memulai, pastikan untuk menyiapkan sumber daya berikut:

- [Set up Azure OpenAI](../set-up-resources/set-up-azure-openai.md)  
- [Set up Azure Computer Vision](../set-up-resources/set-up-azure-computer-vision.md) (opsional)

## Daftar Isi

1. [Buat file '.env' di direktori root](./create-env-file.md)  
   - Sertakan kunci yang diperlukan untuk layanan model bahasa yang dipilih.  
   - Jika kunci Azure Computer Vision tidak disertakan atau `-md` ditentukan, penerjemah akan beroperasi dalam mode Markdown-only.  
3. [Pasang paket Co-op translator](./install-package.md)  
4. [Terjemahkan proyek Anda menggunakan Co-op Translator](./translator-your-project.md)

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berusaha untuk akurasi, harap diperhatikan bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sahih. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau salah tafsir yang timbul dari penggunaan terjemahan ini.