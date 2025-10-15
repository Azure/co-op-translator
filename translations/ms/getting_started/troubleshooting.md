<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6e626bef5ed78a1cc55b0dbf44f01d47",
  "translation_date": "2025-10-15T03:40:34+00:00",
  "source_file": "getting_started/troubleshooting.md",
  "language_code": "ms"
}
-->
# Panduan Penyelesaian Masalah Microsoft Co-op Translator

## Gambaran Keseluruhan
Microsoft Co-Op Translator ialah alat yang berkuasa untuk menterjemah dokumen Markdown dengan lancar. Panduan ini akan membantu anda menyelesaikan masalah biasa yang dihadapi semasa menggunakan alat ini.

## Masalah Biasa dan Penyelesaiannya

### 1. Isu Tag Markdown
**Masalah:** Dokumen Markdown yang diterjemah mengandungi tag `markdown` di bahagian atas, menyebabkan masalah paparan.

**Penyelesaian:** Untuk mengatasinya, padam sahaja tag `markdown` di bahagian atas fail. Ini akan membolehkan fail Markdown dipaparkan dengan betul.

**Langkah-langkah:**
1. Buka fail Markdown (`.md`) yang telah diterjemah.
2. Cari tag `markdown` di bahagian atas dokumen.
3. Padam tag `markdown`.
4. Simpan perubahan pada fail.
5. Buka semula fail untuk pastikan ia dipaparkan dengan betul.

### 2. Isu URL Imej Tertanam
**Masalah:** URL imej tertanam tidak sepadan dengan lokal bahasa, menyebabkan imej tidak betul atau hilang.

**Penyelesaian:** Semak URL imej tertanam dan pastikan ia sepadan dengan lokal bahasa. Semua imej terletak dalam folder `translated_images` dan setiap imej mempunyai tag lokal bahasa dalam nama fail imej.

**Langkah-langkah:**
1. Buka dokumen Markdown yang telah diterjemah.
2. Kenal pasti imej tertanam dan URL mereka.
3. Sahkan bahawa lokal bahasa dalam nama fail imej sepadan dengan bahasa dokumen.
4. Kemas kini URL jika perlu.
5. Simpan perubahan dan buka semula dokumen untuk pastikan imej dipaparkan dengan betul.

### 3. Ketepatan Terjemahan
**Masalah:** Kandungan yang diterjemah tidak tepat atau memerlukan suntingan lanjut.

**Penyelesaian:** Semak dokumen yang diterjemah dan lakukan suntingan yang diperlukan untuk meningkatkan ketepatan dan kefahaman.

**Langkah-langkah:**
1. Buka dokumen yang telah diterjemah.
2. Semak kandungan dengan teliti.
3. Lakukan suntingan yang perlu untuk meningkatkan ketepatan terjemahan.
4. Simpan perubahan.

## 4. Ralat Kebenaran Disunting atau 404

Jika imej atau teks tidak diterjemah ke bahasa yang betul dan apabila dijalankan dalam mod debug -d anda mengalami ralat 401. Ini adalah kegagalan pengesahan klasik—sama ada kunci tidak sah, telah tamat tempoh, atau tidak dipautkan ke rantau endpoint.

Jalankan co-op translator dengan [-d debug switch](https://github.com/Azure/co-op-translator/blob/main/getting_started/command-reference.md) untuk mendapatkan pemahaman lanjut tentang punca utama.

- **Mesej Ralat**: `Access denied due to invalid subscription key or wrong API endpoint.`
- **Punca Kemungkinan**:
  - Kunci langganan telah disunting atau tidak betul dalam permintaan.
  - AI Services Key atau Subscription Key mungkin milik sumber Azure yang berbeza (seperti Translator atau OpenAI) dan bukannya sumber **Azure AI Vision**.

 **Jenis Sumber**
  - Pergi ke [Azure Portal](https://portal.azure.com) atau [Azure AI Foundry](https://ai.azure.com) dan pastikan sumber adalah jenis `Azure AI services` → `Vision`.
  - Sahkan kunci dan pastikan kunci yang betul digunakan.

## 5. Ralat Konfigurasi (Pengendalian Ralat Baharu)

Bermula dengan sistem terjemahan selektif yang baru, Co-op Translator kini memberikan mesej ralat yang jelas apabila perkhidmatan yang diperlukan tidak dikonfigurasi.

### 5.1. Azure AI Service Tidak Dikonfigurasi untuk Terjemahan Imej

**Masalah:** Anda meminta terjemahan imej (flag `-img`) tetapi Azure AI Service tidak dikonfigurasi dengan betul.

**Mesej Ralat:**
```
Error: Image translation requested but Azure AI Service is not configured.
Please add AZURE_AI_SERVICE_API_KEY and AZURE_AI_SERVICE_ENDPOINT to your .env file.
Check Azure AI Service availability and configuration.
```

**Penyelesaian:**
1. **Pilihan 1**: Konfigurasikan Azure AI Service
   - Tambah `AZURE_AI_SERVICE_API_KEY` ke fail `.env` anda
   - Tambah `AZURE_AI_SERVICE_ENDPOINT` ke fail `.env` anda
   - Sahkan perkhidmatan boleh diakses

2. **Pilihan 2**: Buang permintaan terjemahan imej
   ```bash
   # Instead of: translate -l "ko" -img
   # Use: translate -l "ko" -md
   ```

### 5.2. Konfigurasi Diperlukan Tidak Lengkap

**Masalah:** Konfigurasi LLM penting tiada.

**Mesej Ralat:**
```
Error: No language model configuration found.
Please configure either Azure OpenAI or OpenAI in your .env file.
```

**Penyelesaian:**
1. Sahkan bahawa fail `.env` anda mempunyai sekurang-kurangnya salah satu konfigurasi LLM berikut:
   - **Azure OpenAI**: `AZURE_OPENAI_API_KEY` dan `AZURE_OPENAI_ENDPOINT`
   - **OpenAI**: `OPENAI_API_KEY`
   
   Anda hanya perlu sama ada Azure OpenAI ATAU OpenAI dikonfigurasi, bukan kedua-duanya.

### 5.3. Kekeliruan Terjemahan Selektif

**Masalah:** Tiada fail diterjemah walaupun arahan berjaya dijalankan.

**Punca Kemungkinan:**
- Flag jenis fail salah (`-md`, `-img`, `-nb`)
- Tiada fail yang sepadan dalam projek
- Struktur direktori tidak betul

**Penyelesaian:**
1. **Guna mod debug** untuk lihat apa yang berlaku:
   ```bash
   translate -l "ko" -md -d
   ```

2. **Semak jenis fail** dalam projek anda:
   ```bash
   # For markdown files
   find . -name "*.md" -not -path "./translations/*"
   
   # For notebooks
   find . -name "*.ipynb" -not -path "./translations/*"
   
   # For images
   find . -name "*.png" -o -name "*.jpg" -o -name "*.jpeg" -not -path "./translations/*"
   ```

3. **Sahkan kombinasi flag**:
   ```bash
   # Translate everything (default)
   translate -l "ko"
   
   # Translate specific types
   translate -l "ko" -md -img
   ```

## 6. Migrasi dari Sistem Lama

### 6.1. Mod Markdown Sahaja Tidak Lagi Disokong

**Masalah:** Arahan yang bergantung pada fallback automatik markdown sahaja tidak lagi berfungsi seperti biasa.

**Tingkah Laku Lama:**
```bash
# This used to automatically switch to markdown-only mode
translate -l "ko"  # (when Azure AI Vision was not configured)
```

**Tingkah Laku Baharu:**
```bash
# This now produces an error if image translation is requested but not configured
translate -l "ko" -img
```

**Penyelesaian:**
- **Jelas** tentang apa yang anda mahu terjemah:
  ```bash
  translate -l "ko" -md        # Only markdown
  translate -l "ko" -md -img   # Markdown and images
  translate -l "ko"            # Everything (if all services configured)
  ```

### 6.2. Tingkah Laku Pautan Tidak Dijangka

**Masalah:** Pautan dalam fail yang diterjemah menunjuk ke lokasi yang tidak dijangka.

**Punca:** Pemprosesan pautan dinamik berubah berdasarkan jenis fail yang dipilih.

**Penyelesaian:**
1. **Fahami tingkah laku pautan baharu**:
   - `-nb` disertakan: Pautan notebook menunjuk ke versi yang diterjemah
   - `-nb` tidak disertakan: Pautan notebook menunjuk ke fail asal
   - `-img` disertakan: Pautan imej menunjuk ke versi yang diterjemah
   - `-img` tidak disertakan: Pautan imej menunjuk ke fail asal

2. **Pilih kombinasi yang betul** untuk kegunaan anda:
   ```bash
   # All internal links point to translated versions
   translate -l "ko" -md -img -nb
   
   # Only markdown translated, other links point to originals
   translate -l "ko" -md
   ```

## 7. GitHub Action dijalankan tetapi tiada Pull Request (PR) dicipta

**Simptom:** Log workflow untuk `peter-evans/create-pull-request` menunjukkan:

> Branch 'update-translations' is not ahead of base 'main' and will not be created

**Punca kemungkinan:**
- **Tiada perubahan dikesan:** Langkah terjemahan tidak menghasilkan perbezaan (repo sudah dikemas kini).
- **Output diabaikan:** `.gitignore` mengecualikan fail yang anda jangka untuk commit (cth, `*.ipynb`, `translations/`, `translated_images/`).
- **add-paths tidak sepadan:** Laluan yang diberikan kepada action tidak sepadan dengan lokasi output sebenar.
- **Logik/keadaan workflow:** Langkah terjemahan keluar awal atau menulis ke direktori yang tidak dijangka.

**Cara membaiki / mengesahkan:**
1. **Sahkan output wujud:** Selepas terjemahan, semak workspace mempunyai fail baru/diubah dalam `translations/` dan/atau `translated_images/`.
   - Jika menterjemah notebook, pastikan fail `.ipynb` benar-benar ditulis di bawah `translations/<lang>/...`.
2. **Semak `.gitignore`:** Jangan abaikan output yang dijana. Pastikan anda TIDAK mengabaikan:
   - `translations/`
   - `translated_images/`
   - `*.ipynb` (jika menterjemah notebook)
3. **Pastikan add-paths sepadan dengan output:** Guna nilai berbilang baris dan sertakan kedua-dua folder jika berkaitan:
   ```yaml
   with:
     add-paths: |
       translations/
       translated_images/
   ```
4. **Paksa PR untuk debug:** Benarkan commit kosong buat sementara waktu untuk sahkan sambungan betul:
   ```yaml
   with:
     commit-empty: true
   ```
5. **Jalankan dengan debug:** Tambah `-d` pada arahan translate untuk cetak fail yang ditemui dan ditulis.
6. **Kebenaran (GITHUB_TOKEN):** Pastikan workflow mempunyai kebenaran menulis untuk mencipta commit dan PR:
   ```yaml
   permissions:
     contents: write
     pull-requests: write
   ```


## Senarai Semak Debug Pantas

Semasa menyelesaikan masalah terjemahan:

1. **Guna mod debug**: Tambah flag `-d` untuk lihat log terperinci
2. **Semak flag anda**: Pastikan `-md`, `-img`, `-nb` sepadan dengan niat anda
3. **Sahkan konfigurasi**: Semak fail `.env` anda mempunyai kunci yang diperlukan
4. **Uji secara berperingkat**: Mulakan dengan `-md` sahaja, kemudian tambah jenis lain
5. **Semak struktur fail**: Pastikan fail sumber wujud dan boleh diakses

Untuk maklumat lebih terperinci tentang arahan dan flag yang tersedia, lihat [Command Reference](./command-reference.md).

---

**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk memastikan ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat kritikal, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.