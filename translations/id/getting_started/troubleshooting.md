<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6e626bef5ed78a1cc55b0dbf44f01d47",
  "translation_date": "2025-10-15T03:38:13+00:00",
  "source_file": "getting_started/troubleshooting.md",
  "language_code": "id"
}
-->
# Panduan Pemecahan Masalah Microsoft Co-op Translator

## Gambaran Umum
Microsoft Co-Op Translator adalah alat canggih untuk menerjemahkan dokumen Markdown secara mulus. Panduan ini akan membantu Anda mengatasi masalah umum yang sering ditemui saat menggunakan alat ini.

## Masalah Umum dan Solusinya

### 1. Masalah Tag Markdown
**Masalah:** Dokumen Markdown hasil terjemahan terdapat tag `markdown` di bagian atas, sehingga menyebabkan masalah saat ditampilkan.

**Solusi:** Untuk mengatasinya, cukup hapus tag `markdown` di bagian atas file. Setelah itu, file Markdown akan bisa ditampilkan dengan benar.

**Langkah-langkah:**
1. Buka file Markdown (`.md`) hasil terjemahan.
2. Temukan tag `markdown` di bagian paling atas dokumen.
3. Hapus tag `markdown`.
4. Simpan perubahan pada file.
5. Buka kembali file untuk memastikan tampilannya sudah benar.

### 2. Masalah URL Gambar Tertanam
**Masalah:** URL gambar yang tertanam tidak sesuai dengan lokal bahasa, sehingga gambar menjadi salah atau tidak muncul.

**Solusi:** Periksa URL gambar yang tertanam dan pastikan sudah sesuai dengan lokal bahasa. Semua gambar berada di folder `translated_images` dan setiap gambar memiliki tag lokal bahasa pada nama file gambarnya.

**Langkah-langkah:**
1. Buka dokumen Markdown hasil terjemahan.
2. Identifikasi gambar yang tertanam beserta URL-nya.
3. Pastikan tag lokal bahasa pada nama file gambar sudah sesuai dengan bahasa dokumen.
4. Perbarui URL jika diperlukan.
5. Simpan perubahan dan buka kembali dokumen untuk memastikan gambar tampil dengan benar.

### 3. Akurasi Terjemahan
**Masalah:** Konten hasil terjemahan kurang akurat atau perlu diedit lebih lanjut.

**Solusi:** Tinjau dokumen hasil terjemahan dan lakukan edit seperlunya agar lebih akurat dan mudah dibaca.

**Langkah-langkah:**
1. Buka dokumen hasil terjemahan.
2. Tinjau isi dokumen dengan teliti.
3. Lakukan edit seperlunya untuk meningkatkan akurasi terjemahan.
4. Simpan perubahan.

## 4. Error Izin Redacted atau 404

Jika gambar atau teks tidak diterjemahkan ke bahasa yang benar dan saat menjalankan mode debug (-d) muncul error 401. Ini adalah kegagalan autentikasi klasik—kuncinya tidak valid, sudah kadaluarsa, atau tidak terhubung ke region endpoint yang benar.

Jalankan co-op translator dengan [switch -d debug](https://github.com/Azure/co-op-translator/blob/main/getting_started/command-reference.md) untuk memahami akar masalahnya.

- **Pesan Error**: `Access denied due to invalid subscription key or wrong API endpoint.`
- **Kemungkinan Penyebab**:
  - Subscription key disembunyikan atau salah dalam permintaan.
  - AI Services Key atau Subscription Key mungkin milik resource Azure lain (seperti Translator atau OpenAI) bukan **Azure AI Vision**.

 **Tipe Resource**
  - Buka [Azure Portal](https://portal.azure.com) atau [Azure AI Foundry](https://ai.azure.com) dan pastikan resource bertipe `Azure AI services` → `Vision`.
  - Validasi kunci dan pastikan kunci yang digunakan sudah benar.

## 5. Error Konfigurasi (Penanganan Error Baru)

Mulai dari sistem terjemahan selektif yang baru, Co-op Translator kini memberikan pesan error yang jelas jika layanan yang dibutuhkan belum dikonfigurasi.

### 5.1. Azure AI Service Belum Dikonfigurasi untuk Terjemahan Gambar

**Masalah:** Anda meminta terjemahan gambar (flag `-img`) tapi Azure AI Service belum dikonfigurasi dengan benar.

**Pesan Error:**
```
Error: Image translation requested but Azure AI Service is not configured.
Please add AZURE_AI_SERVICE_API_KEY and AZURE_AI_SERVICE_ENDPOINT to your .env file.
Check Azure AI Service availability and configuration.
```

**Solusi:**
1. **Opsi 1**: Konfigurasi Azure AI Service
   - Tambahkan `AZURE_AI_SERVICE_API_KEY` ke file `.env`
   - Tambahkan `AZURE_AI_SERVICE_ENDPOINT` ke file `.env`
   - Pastikan layanan dapat diakses

2. **Opsi 2**: Hapus permintaan terjemahan gambar
   ```bash
   # Instead of: translate -l "ko" -img
   # Use: translate -l "ko" -md
   ```

### 5.2. Konfigurasi Wajib Hilang

**Masalah:** Konfigurasi LLM penting belum tersedia.

**Pesan Error:**
```
Error: No language model configuration found.
Please configure either Azure OpenAI or OpenAI in your .env file.
```

**Solusi:**
1. Pastikan file `.env` Anda memiliki setidaknya salah satu konfigurasi LLM berikut:
   - **Azure OpenAI**: `AZURE_OPENAI_API_KEY` dan `AZURE_OPENAI_ENDPOINT`
   - **OpenAI**: `OPENAI_API_KEY`
   
   Anda hanya perlu mengonfigurasi salah satu, Azure OpenAI ATAU OpenAI, tidak keduanya.

### 5.3. Kebingungan Terjemahan Selektif

**Masalah:** Tidak ada file yang diterjemahkan meskipun perintah berhasil dijalankan.

**Kemungkinan Penyebab:**
- Flag tipe file salah (`-md`, `-img`, `-nb`)
- Tidak ada file yang cocok di proyek
- Struktur direktori salah

**Solusi:**
1. **Gunakan mode debug** untuk melihat apa yang terjadi:
   ```bash
   translate -l "ko" -md -d
   ```

2. **Cek tipe file** di proyek Anda:
   ```bash
   # For markdown files
   find . -name "*.md" -not -path "./translations/*"
   
   # For notebooks
   find . -name "*.ipynb" -not -path "./translations/*"
   
   # For images
   find . -name "*.png" -o -name "*.jpg" -o -name "*.jpeg" -not -path "./translations/*"
   ```

3. **Verifikasi kombinasi flag**:
   ```bash
   # Translate everything (default)
   translate -l "ko"
   
   # Translate specific types
   translate -l "ko" -md -img
   ```

## 6. Migrasi dari Sistem Lama

### 6.1. Mode Markdown Saja Dihapus

**Masalah:** Perintah yang mengandalkan fallback otomatis markdown saja tidak lagi berfungsi seperti sebelumnya.

**Perilaku Lama:**
```bash
# This used to automatically switch to markdown-only mode
translate -l "ko"  # (when Azure AI Vision was not configured)
```

**Perilaku Baru:**
```bash
# This now produces an error if image translation is requested but not configured
translate -l "ko" -img
```

**Solusi:**
- **Jelaskan secara eksplisit** apa yang ingin Anda terjemahkan:
  ```bash
  translate -l "ko" -md        # Only markdown
  translate -l "ko" -md -img   # Markdown and images
  translate -l "ko"            # Everything (if all services configured)
  ```

### 6.2. Perilaku Link Tidak Terduga

**Masalah:** Link di file hasil terjemahan mengarah ke lokasi yang tidak diharapkan.

**Penyebab:** Proses link dinamis berubah sesuai tipe file yang dipilih.

**Solusi:**
1. **Pahami perilaku link yang baru**:
   - `-nb` disertakan: Link notebook mengarah ke versi terjemahan
   - `-nb` tidak disertakan: Link notebook mengarah ke file asli
   - `-img` disertakan: Link gambar mengarah ke versi terjemahan
   - `-img` tidak disertakan: Link gambar mengarah ke file asli

2. **Pilih kombinasi yang tepat** sesuai kebutuhan Anda:
   ```bash
   # All internal links point to translated versions
   translate -l "ko" -md -img -nb
   
   # Only markdown translated, other links point to originals
   translate -l "ko" -md
   ```

## 7. GitHub Action berjalan tapi tidak membuat Pull Request (PR)

**Gejala:** Log workflow untuk `peter-evans/create-pull-request` menunjukkan:

> Branch 'update-translations' is not ahead of base 'main' and will not be created

**Kemungkinan penyebab:**
- **Tidak ada perubahan terdeteksi:** Langkah terjemahan tidak menghasilkan perbedaan (repo sudah up to date).
- **Output diabaikan:** `.gitignore` mengecualikan file yang ingin Anda commit (misal, `*.ipynb`, `translations/`, `translated_images/`).
- **add-paths tidak cocok:** Path yang diberikan ke action tidak sesuai dengan lokasi output sebenarnya.
- **Logika/ketentuan workflow:** Langkah terjemahan keluar lebih awal atau menulis ke direktori yang tidak diharapkan.

**Cara memperbaiki / verifikasi:**
1. **Pastikan output ada:** Setelah terjemahan, cek workspace apakah ada file baru/berubah di `translations/` dan/atau `translated_images/`.
   - Jika menerjemahkan notebook, pastikan file `.ipynb` benar-benar ditulis di bawah `translations/<lang>/...`.
2. **Tinjau `.gitignore`:** Jangan abaikan output yang dihasilkan. Pastikan Anda TIDAK mengabaikan:
   - `translations/`
   - `translated_images/`
   - `*.ipynb` (jika menerjemahkan notebook)
3. **Pastikan add-paths sesuai output:** Gunakan nilai multiline dan sertakan kedua folder jika perlu:
   ```yaml
   with:
     add-paths: |
       translations/
       translated_images/
   ```
4. **Paksa PR untuk debugging:** Sementara, izinkan commit kosong untuk memastikan wiring sudah benar:
   ```yaml
   with:
     commit-empty: true
   ```
5. **Jalankan dengan debug:** Tambahkan `-d` ke perintah translate untuk mencetak file apa saja yang ditemukan dan ditulis.
6. **Izin (GITHUB_TOKEN):** Pastikan workflow memiliki izin menulis untuk membuat commit dan PR:
   ```yaml
   permissions:
     contents: write
     pull-requests: write
   ```

## Daftar Periksa Debug Cepat

Saat mengatasi masalah terjemahan:

1. **Gunakan mode debug**: Tambahkan flag `-d` untuk melihat log detail
2. **Cek flag Anda**: Pastikan `-md`, `-img`, `-nb` sesuai dengan tujuan Anda
3. **Verifikasi konfigurasi**: Pastikan file `.env` Anda memiliki kunci yang dibutuhkan
4. **Uji secara bertahap**: Mulai dengan `-md` saja, lalu tambahkan tipe lain
5. **Cek struktur file**: Pastikan file sumber ada dan bisa diakses

Untuk informasi lebih detail tentang perintah dan flag yang tersedia, lihat [Command Reference](./command-reference.md).

---

**Disclaimer**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk memberikan terjemahan yang akurat, harap diketahui bahwa terjemahan otomatis dapat mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang berwenang. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa penerjemah profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang timbul dari penggunaan terjemahan ini.