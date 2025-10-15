<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9fac847815936ef6e6c8bfde6d191571",
  "translation_date": "2025-10-15T03:38:49+00:00",
  "source_file": "getting_started/github-actions-guide/github-actions-guide-org.md",
  "language_code": "id"
}
-->
# Menggunakan Co-op Translator GitHub Action (Panduan Organisasi)

**Audiens Target:** Panduan ini ditujukan untuk **pengguna internal Microsoft** atau **tim yang memiliki akses ke kredensial yang diperlukan untuk Co-op Translator GitHub App yang sudah dibuat** atau dapat membuat GitHub App kustom sendiri.

Otomatiskan penerjemahan dokumentasi repository Anda dengan mudah menggunakan Co-op Translator GitHub Action. Panduan ini akan memandu Anda dalam menyiapkan action agar secara otomatis membuat pull request dengan pembaruan terjemahan setiap kali file Markdown sumber atau gambar Anda berubah.

> [!IMPORTANT]
>
> **Memilih Panduan yang Tepat:**
>
> Panduan ini menjelaskan pengaturan menggunakan **GitHub App ID dan Private Key**. Anda biasanya memerlukan metode "Panduan Organisasi" ini jika: **`GITHUB_TOKEN` Memiliki Izin Terbatas:** Pengaturan organisasi atau repository Anda membatasi izin default yang diberikan ke `GITHUB_TOKEN` standar. Khususnya, jika `GITHUB_TOKEN` tidak diizinkan memiliki izin `write` yang diperlukan (seperti `contents: write` atau `pull-requests: write`), workflow di [Panduan Setup Publik](./github-actions-guide-public.md) akan gagal karena kekurangan izin. Menggunakan GitHub App khusus dengan izin yang diberikan secara eksplisit akan mengatasi batasan ini.
>
> **Jika hal di atas tidak berlaku untuk Anda:**
>
> Jika `GITHUB_TOKEN` standar memiliki izin yang cukup di repository Anda (yaitu, Anda tidak dibatasi oleh aturan organisasi), silakan gunakan **[Panduan Setup Publik menggunakan GITHUB_TOKEN](./github-actions-guide-public.md)**. Panduan publik tidak memerlukan App ID atau Private Key, dan hanya mengandalkan `GITHUB_TOKEN` standar serta izin repository.

## Prasyarat

Sebelum mengonfigurasi GitHub Action, pastikan Anda sudah memiliki kredensial layanan AI yang diperlukan.

**1. Wajib: Kredensial Model Bahasa AI**
Anda memerlukan kredensial untuk setidaknya satu Model Bahasa yang didukung:

- **Azure OpenAI**: Membutuhkan Endpoint, API Key, Nama Model/Deployment, Versi API.
- **OpenAI**: Membutuhkan API Key, (Opsional: Org ID, Base URL, Model ID).
- Lihat [Model dan Layanan yang Didukung](../../../../README.md) untuk detailnya.
- Panduan Setup: [Set up Azure OpenAI](../set-up-resources/set-up-azure-openai.md).

**2. Opsional: Kredensial Computer Vision (untuk Terjemahan Gambar)**

- Hanya diperlukan jika Anda ingin menerjemahkan teks di dalam gambar.
- **Azure Computer Vision**: Membutuhkan Endpoint dan Subscription Key.
- Jika tidak disediakan, action akan berjalan dalam [mode Markdown-only](../markdown-only-mode.md).
- Panduan Setup: [Set up Azure Computer Vision](../set-up-resources/set-up-azure-computer-vision.md).

## Pengaturan dan Konfigurasi

Ikuti langkah-langkah berikut untuk mengonfigurasi Co-op Translator GitHub Action di repository Anda:

### Langkah 1: Instal dan Konfigurasi Autentikasi GitHub App

Workflow menggunakan autentikasi GitHub App untuk berinteraksi secara aman dengan repository Anda (misal, membuat pull request) atas nama Anda. Pilih salah satu opsi:

#### **Opsi A: Instal Co-op Translator GitHub App yang Sudah Dibuat (untuk Penggunaan Internal Microsoft)**

1. Buka halaman [Co-op Translator GitHub App](https://github.com/apps/co-op-translator).

1. Pilih **Install** dan pilih akun atau organisasi tempat repository target Anda berada.

    ![Install app](../../../../translated_images/install-app.d0f0a24cbb1d6c93f293f002eb34e633f7bc8f5caaba46b97806ba7bdc958f27.id.png)

1. Pilih **Only select repositories** dan pilih repository target Anda (misal, `PhiCookBook`). Klik **Install**. Anda mungkin diminta untuk melakukan autentikasi.

    ![Install authorize](../../../../translated_images/install-authorize.29df6238c3eb8f707e7fc6f97a946cb654b328530c4aeddce28b874693f076a0.id.png)

1. **Dapatkan Kredensial App (Proses Internal Diperlukan):** Agar workflow dapat melakukan autentikasi sebagai app, Anda memerlukan dua informasi dari tim Co-op Translator:
   - **App ID:** Identifikasi unik untuk Co-op Translator app. App ID-nya adalah: `1164076`.
   - **Private Key:** Anda harus mendapatkan **seluruh isi** file private key `.pem` dari kontak maintainer. **Perlakukan key ini seperti password dan jaga kerahasiaannya.**

1. Lanjutkan ke Langkah 2.

#### **Opsi B: Gunakan GitHub App Kustom Anda Sendiri**

- Jika Anda ingin, Anda dapat membuat dan mengonfigurasi GitHub App sendiri. Pastikan memiliki akses Read & write ke Contents dan Pull requests. Anda akan memerlukan App ID dan Private Key yang dihasilkan.

### Langkah 2: Konfigurasi Repository Secrets

Anda perlu menambahkan kredensial GitHub App dan kredensial layanan AI Anda sebagai secrets terenkripsi di pengaturan repository.

1. Buka repository GitHub target Anda (misal, `PhiCookBook`).

1. Masuk ke **Settings** > **Secrets and variables** > **Actions**.

1. Di bawah **Repository secrets**, klik **New repository secret** untuk setiap secret yang tercantum di bawah ini.

   ![Select setting action](../../../../translated_images/select-setting-action.3b95c915d60311592ca51ecb91b3a7bbe0ae45438a2ee872c1520dc90b677780.id.png)

**Secrets Wajib (untuk Autentikasi GitHub App):**

| Nama Secret          | Deskripsi                                         | Sumber Nilai                                      |
| :------------------- | :------------------------------------------------ | :------------------------------------------------ |
| `GH_APP_ID`          | App ID dari GitHub App (dari Langkah 1).          | Pengaturan GitHub App                             |
| `GH_APP_PRIVATE_KEY` | **Seluruh isi** file `.pem` yang diunduh.         | File `.pem` (dari Langkah 1)                      |

**Secrets Layanan AI (Tambahkan SEMUA yang berlaku sesuai Prasyarat Anda):**

| Nama Secret                         | Deskripsi                                   | Sumber Nilai                        |
| :---------------------------------- | :------------------------------------------ | :---------------------------------- |
| `AZURE_AI_SERVICE_API_KEY`            | Key untuk Azure AI Service (Computer Vision)  | Azure AI Foundry                    |
| `AZURE_AI_SERVICE_ENDPOINT`         | Endpoint untuk Azure AI Service (Computer Vision) | Azure AI Foundry                 |
| `AZURE_OPENAI_API_KEY`              | Key untuk layanan Azure OpenAI              | Azure AI Foundry                     |
| `AZURE_OPENAI_ENDPOINT`             | Endpoint untuk layanan Azure OpenAI         | Azure AI Foundry                     |
| `AZURE_OPENAI_MODEL_NAME`           | Nama Model Azure OpenAI Anda                | Azure AI Foundry                     |
| `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` | Nama Deployment Azure OpenAI Anda           | Azure AI Foundry                     |
| `AZURE_OPENAI_API_VERSION`          | Versi API untuk Azure OpenAI                | Azure AI Foundry                     |
| `OPENAI_API_KEY`                    | API Key untuk OpenAI                        | OpenAI Platform                      |
| `OPENAI_ORG_ID`                     | OpenAI Organization ID                      | OpenAI Platform                      |
| `OPENAI_CHAT_MODEL_ID`              | ID model OpenAI spesifik                    | OpenAI Platform                      |
| `OPENAI_BASE_URL`                   | Custom OpenAI API Base URL                  | OpenAI Platform                      |

![Enter environment variable name](../../../../translated_images/add-secrets-done.444861ce6956d5cb20781ead1237fcc12805078349bb0d4e95bb9540ee192227.id.png)

### Langkah 3: Buat File Workflow

Terakhir, buat file YAML yang mendefinisikan workflow otomatis.

1. Di direktori root repository Anda, buat direktori `.github/workflows/` jika belum ada.

1. Di dalam `.github/workflows/`, buat file bernama `co-op-translator.yml`.

1. Tempelkan konten berikut ke dalam co-op-translator.yml.

```
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
          # Azure AI Service Credentials
          AZURE_AI_SERVICE_API_KEY: ${{ secrets.AZURE_AI_SERVICE_API_KEY }}
          AZURE_AI_SERVICE_ENDPOINT: ${{ secrets.AZURE_AI_SERVICE_ENDPOINT }}

          # Azure OpenAI Credentials
          AZURE_OPENAI_API_KEY: ${{ secrets.AZURE_OPENAI_API_KEY }}
          AZURE_OPENAI_ENDPOINT: ${{ secrets.AZURE_OPENAI_ENDPOINT }}
          AZURE_OPENAI_MODEL_NAME: ${{ secrets.AZURE_OPENAI_MODEL_NAME }}
          AZURE_OPENAI_CHAT_DEPLOYMENT_NAME: ${{ secrets.AZURE_OPENAI_CHAT_DEPLOYMENT_NAME }}
          AZURE_OPENAI_API_VERSION: ${{ secrets.AZURE_OPENAI_API_VERSION }}

          # OpenAI Credentials
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

      - name: Authenticate GitHub App
        id: generate_token
        uses: tibdex/github-app-token@v1
        with:
          app_id: ${{ secrets.GH_APP_ID }}
          private_key: ${{ secrets.GH_APP_PRIVATE_KEY }}

      - name: Create Pull Request with translations
        uses: peter-evans/create-pull-request@v5
        with:
          token: ${{ steps.generate_token.outputs.token }}
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
   - **Trigger (`on:`):** Trigger saat ini berjalan pada setiap push ke `main`. Untuk repository besar, pertimbangkan menambahkan filter `paths:` (lihat contoh yang dikomentari di YAML) agar workflow hanya berjalan saat file relevan (misal, dokumentasi sumber) berubah, sehingga menghemat waktu runner.
   - **Detail PR:** Kustomisasi `commit-message`, `title`, `body`, nama `branch`, dan `labels` pada langkah `Create Pull Request` jika diperlukan.

## Manajemen dan Pembaruan Kredensial

- **Keamanan:** Selalu simpan kredensial sensitif (API key, private key) sebagai secrets GitHub Actions. Jangan pernah menuliskannya di file workflow atau kode repository Anda.
- **[!IMPORTANT] Pembaruan Key (Pengguna Internal Microsoft):** Perlu diketahui bahwa key Azure OpenAI yang digunakan di lingkungan Microsoft mungkin memiliki kebijakan pembaruan wajib (misal, setiap 5 bulan). Pastikan Anda memperbarui secrets GitHub terkait (`AZURE_OPENAI_...`) **sebelum kedaluwarsa** untuk mencegah kegagalan workflow.

## Menjalankan Workflow

> [!WARNING]  
> **Batas Waktu Runner yang Dihosting GitHub:**  
> Runner yang dihosting GitHub seperti `ubuntu-latest` memiliki **batas waktu eksekusi maksimum 6 jam**.  
> Untuk repository dokumentasi yang besar, jika proses terjemahan melebihi 6 jam, workflow akan otomatis dihentikan.  
> Untuk mencegah hal ini, pertimbangkan:  
> - Menggunakan **self-hosted runner** (tanpa batas waktu)  
> - Mengurangi jumlah target bahasa per sekali jalan

Setelah file `co-op-translator.yml` digabungkan ke branch utama Anda (atau branch yang ditentukan di trigger `on:`), workflow akan otomatis berjalan setiap kali ada perubahan yang didorong ke branch tersebut (dan sesuai filter `paths` jika dikonfigurasi).

Jika terjemahan dihasilkan atau diperbarui, action akan otomatis membuat Pull Request yang berisi perubahan tersebut, siap untuk Anda tinjau dan gabungkan.

---

**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk memberikan terjemahan yang akurat, harap diketahui bahwa terjemahan otomatis dapat mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang berwenang. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa penerjemah profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang timbul dari penggunaan terjemahan ini.