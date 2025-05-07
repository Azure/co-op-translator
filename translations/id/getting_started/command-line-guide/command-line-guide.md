<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a5eb9b53c81804f04bc9456160e79940",
  "translation_date": "2025-05-07T14:15:05+00:00",
  "source_file": "getting_started/command-line-guide/command-line-guide.md",
  "language_code": "id"
}
-->
# Cara menggunakan antarmuka baris perintah (CLI) Co-op Translator

## Prasyarat

- **Python 3.10 atau lebih tinggi**: Diperlukan untuk menjalankan Co-op Translator.
- **Sumber Daya Model Bahasa**: 
  - **Azure OpenAI** atau LLM lainnya. Detail dapat ditemukan di [model dan layanan yang didukung](../../../../README.md).
- **Sumber Daya Computer Vision** (opsional):
  - Untuk terjemahan gambar. Jika tidak tersedia, penerjemah akan menggunakan [mode hanya Markdown](../markdown-only-mode.md).
  - **Azure Computer Vision**

## Daftar Isi

1. [Buat file '.env' di direktori root](./create-env-file.md)
   - Sertakan kunci yang diperlukan untuk layanan model bahasa yang dipilih.
   - Jika kunci Azure Computer Vision dihilangkan atau `-md` ditentukan, penerjemah akan berjalan dalam mode hanya Markdown.
1. [Pasang paket Co-op translator](./install-package.md)
1. [Terjemahkan proyek Anda menggunakan Co-op Translator](./translator-your-project.md)

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berusaha untuk akurasi, harap diingat bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang salah yang timbul dari penggunaan terjemahan ini.