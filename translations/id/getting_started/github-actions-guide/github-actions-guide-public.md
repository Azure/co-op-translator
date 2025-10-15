<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "527ca4d0a8d3f51087ec3317279e36ee",
  "translation_date": "2025-10-15T03:39:10+00:00",
  "source_file": "getting_started/github-actions-guide/github-actions-guide-public.md",
  "language_code": "id"
}
-->
# Menggunakan Co-op Translator GitHub Action (Pengaturan Publik)

**Target Pengguna:** Panduan ini ditujukan untuk pengguna di sebagian besar repositori publik atau privat di mana izin standar GitHub Actions sudah cukup. Panduan ini menggunakan `GITHUB_TOKEN` bawaan.

Otomatisasi penerjemahan dokumentasi repositori Anda dengan mudah menggunakan Co-op Translator GitHub Action. Panduan ini akan memandu Anda dalam mengatur action agar secara otomatis membuat pull request dengan pembaruan terjemahan setiap kali file Markdown sumber atau gambar Anda berubah.

> [!IMPORTANT]
>
> **Memilih Panduan yang Tepat:**
>
> Panduan ini menjelaskan **pengaturan yang lebih sederhana menggunakan `GITHUB_TOKEN` standar**. Metode ini direkomendasikan untuk sebagian besar pengguna karena tidak perlu mengelola Private Key GitHub App yang sensitif.
>

## Prasyarat

Sebelum mengonfigurasi GitHub Action, pastikan Anda sudah menyiapkan kredensial layanan AI yang diperlukan.

**1. Wajib: Kredensial Model Bahasa AI**
Anda membutuhkan kredensial untuk setidaknya satu Model Bahasa yang didukung:

- **Azure OpenAI**: Memerlukan Endpoint, API Key, Nama Model/Deployment, Versi API.
- **OpenAI**: Memerlukan API Key, (Opsional: Org ID, Base URL, Model ID).
- Lihat [Model dan Layanan yang Didukung](../../../../README.md) untuk detailnya.

**2. Opsional: Kredensial AI Vision (untuk Terjemahan Gambar)**

- Hanya diperlukan jika Anda ingin menerjemahkan teks dalam gambar.
- **Azure AI Vision**: Memerlukan Endpoint dan Subscription Key.
- Jika tidak disediakan, action akan menggunakan [mode Markdown saja](../markdown-only-mode.md).

## Pengaturan dan Konfigurasi

Ikuti langkah-langkah berikut untuk mengonfigurasi Co-op Translator GitHub Action di repositori Anda menggunakan `GITHUB_TOKEN` standar.

### Langkah 1: Pahami Autentikasi (Menggunakan `GITHUB_TOKEN`)

Workflow ini menggunakan `GITHUB_TOKEN` bawaan yang disediakan oleh GitHub Actions. Token ini secara otomatis memberikan izin kepada workflow untuk berinteraksi dengan repositori Anda sesuai pengaturan yang dikonfigurasi di **Langkah 3**.

### Langkah 2: Konfigurasi Secrets di Repositori

Anda hanya perlu menambahkan **kredensial layanan AI** sebagai secrets terenkripsi di pengaturan repositori Anda.

1.  Buka repositori GitHub yang ingin Anda gunakan.
2.  Masuk ke **Settings** > **Secrets and variables** > **Actions**.
3.  Di bawah **Repository secrets**, klik **New repository secret** untuk setiap secret layanan AI yang diperlukan di bawah ini.

    <img src="../../../../translated_images/select-setting-action.3b95c915d60311592ca51ecb91b3a7bbe0ae45438a2ee872c1520dc90b677780.id.png" alt="Select setting action"> *(Referensi Gambar: Menunjukkan lokasi penambahan secrets)*

**Secrets Layanan AI yang Diperlukan (Tambahkan SEMUA yang sesuai dengan Prasyarat Anda):**

| Nama Secret                         | Deskripsi                                 | Sumber Nilai                      |
| :---------------------------------- | :---------------------------------------- | :------------------------------- |
| `AZURE_AI_SERVICE_API_KEY`            | Kunci untuk Azure AI Service (Computer Vision)  | Azure AI Foundry Anda               |
| `AZURE_AI_SERVICE_ENDPOINT`         | Endpoint untuk Azure AI Service (Computer Vision) | Azure AI Foundry Anda               |
| `AZURE_OPENAI_API_KEY`              | Kunci untuk layanan Azure OpenAI          | Azure AI Foundry Anda               |
| `AZURE_OPENAI_ENDPOINT`             | Endpoint untuk layanan Azure OpenAI       | Azure AI Foundry Anda               |
| `AZURE_OPENAI_MODEL_NAME`           | Nama Model Azure OpenAI Anda              | Azure AI Foundry Anda               |
| `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` | Nama Deployment Azure OpenAI Anda         | Azure AI Foundry Anda               |
| `AZURE_OPENAI_API_VERSION`          | Versi API untuk Azure OpenAI              | Azure AI Foundry Anda               |
| `OPENAI_API_KEY`                    | API Key untuk OpenAI                      | Platform OpenAI Anda              |
| `OPENAI_ORG_ID`                     | OpenAI Organization ID (Opsional)         | Platform OpenAI Anda              |
| `OPENAI_CHAT_MODEL_ID`              | ID model OpenAI spesifik (Opsional)       | Platform OpenAI Anda              |
| `OPENAI_BASE_URL`                   | Custom OpenAI API Base URL (Opsional)     | Platform OpenAI Anda              |

### Langkah 3: Konfigurasi Izin Workflow

GitHub Action membutuhkan izin yang diberikan melalui `GITHUB_TOKEN` untuk checkout kode dan membuat pull request.

1.  Di repositori Anda, buka **Settings** > **Actions** > **General**.
2.  Gulir ke bagian **Workflow permissions**.
3.  Pilih **Read and write permissions**. Ini memberikan `GITHUB_TOKEN` izin `contents: write` dan `pull-requests: write` yang diperlukan untuk workflow ini.
4.  Pastikan kotak **Allow GitHub Actions to create and approve pull requests** sudah **dicentang**.
5.  Klik **Save**.

<img src="../../../../translated_images/permission-setting.ae2f02748b0579e7dc3633f14dad67005b533ea8f69890818857de058089a7f5.id.png" alt="Permission setting">

### Langkah 4: Buat File Workflow

Terakhir, buat file YAML yang mendefinisikan workflow otomatis menggunakan `GITHUB_TOKEN`.

1.  Di direktori root repositori Anda, buat folder `.github/workflows/` jika belum ada.
2.  Di dalam `.github/workflows/`, buat file bernama `co-op-translator.yml`.
3.  Tempelkan konten berikut ke dalam `co-op-translator.yml`.

```yaml
name: Co-op Translator

on:
  push:
    branches:
      - main

jobs:
  co-op-translator:
    runs-on: ubuntu-latest

    permissions:
      contents: write
      pull-requests: write

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      - name: Install Co-op Translator
        run: |
          python -m pip install --upgrade pip
          pip install co-op-translator

      - name: Run Co-op Translator
        env:
          PYTHONIOENCODING: utf-8
          # === AI Service Credentials ===
          AZURE_AI_SERVICE_API_KEY: ${{ secrets.AZURE_AI_SERVICE_API_KEY }}
          AZURE_AI_SERVICE_ENDPOINT: ${{ secrets.AZURE_AI_SERVICE_ENDPOINT }}
          AZURE_OPENAI_API_KEY: ${{ secrets.AZURE_OPENAI_API_KEY }}
          AZURE_OPENAI_ENDPOINT: ${{ secrets.AZURE_OPENAI_ENDPOINT }}
          AZURE_OPENAI_MODEL_NAME: ${{ secrets.AZURE_OPENAI_MODEL_NAME }}
          AZURE_OPENAI_CHAT_DEPLOYMENT_NAME: ${{ secrets.AZURE_OPENAI_CHAT_DEPLOYMENT_NAME }}
          AZURE_OPENAI_API_VERSION: ${{ secrets.AZURE_OPENAI_API_VERSION }}
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
          OPENAI_ORG_ID: ${{ secrets.OPENAI_ORG_ID }}
          OPENAI_CHAT_MODEL_ID: ${{ secrets.OPENAI_CHAT_MODEL_ID }}
          OPENAI_BASE_URL: ${{ secrets.OPENAI_BASE_URL }}
        run: |
          # =====================================================================
          # IMPORTANT: Set your target languages here (REQUIRED CONFIGURATION)
          # =====================================================================
          # Example: Translate to Spanish, French, German. Add -y to auto-confirm.
          translate -l "es fr de" -y  # <--- MODIFY THIS LINE with your desired languages

      - name: Create Pull Request with translations
        uses: peter-evans/create-pull-request@v5
        with:
          token: ${{ secrets.GITHUB_TOKEN }}
          commit-message: "🌐 Update translations via Co-op Translator"
          title: "🌐 Update translations via Co-op Translator"
          body: |
            This PR updates translations for recent changes to the main branch.

            ### 📋 Changes included
            - Translated contents are available in the `translations/` directory
            - Translated images are available in the `translated_images/` directory

            ---
            🌐 Automatically generated by the [Co-op Translator](https://github.com/Azure/co-op-translator) GitHub Action.
          branch: update-translations
          base: main
          labels: translation, automated-pr
          delete-branch: true
          add-paths: |
            translations/
            translated_images/
```
4.  **Kustomisasi Workflow:**
  - **[!IMPORTANT] Target Bahasa:** Pada langkah `Run Co-op Translator`, Anda **WAJIB meninjau dan mengubah daftar kode bahasa** di dalam perintah `translate -l "..." -y` agar sesuai dengan kebutuhan proyek Anda. Daftar contoh (`ar de es...`) harus diganti atau disesuaikan.
  - **Trigger (`on:`):** Trigger saat ini berjalan setiap kali ada push ke `main`. Untuk repositori besar, pertimbangkan menambahkan filter `paths:` (lihat contoh komentar di YAML) agar workflow hanya berjalan saat file relevan (misal: dokumentasi sumber) berubah, sehingga menghemat waktu runner.
  - **Detail PR:** Kustomisasi `commit-message`, `title`, `body`, nama `branch`, dan `labels` pada langkah `Create Pull Request` jika diperlukan.

## Menjalankan Workflow

> [!WARNING]  
> **Batas Waktu Runner GitHub-hosted:**  
> Runner GitHub-hosted seperti `ubuntu-latest` memiliki **batas waktu eksekusi maksimal 6 jam**.  
> Untuk repositori dokumentasi yang besar, jika proses terjemahan melebihi 6 jam, workflow akan otomatis dihentikan.  
> Untuk mencegah hal ini, pertimbangkan:  
> - Menggunakan **self-hosted runner** (tanpa batas waktu)  
> - Mengurangi jumlah target bahasa per run

Setelah file `co-op-translator.yml` digabungkan ke branch utama Anda (atau branch yang ditentukan di trigger `on:`), workflow akan otomatis berjalan setiap kali ada perubahan yang didorong ke branch tersebut (dan sesuai filter `paths`, jika dikonfigurasi).

---

**Disclaimer**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk memberikan terjemahan yang akurat, harap diketahui bahwa terjemahan otomatis dapat mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang berwenang. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa penerjemah profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang timbul dari penggunaan terjemahan ini.