<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9fac847815936ef6e6c8bfde6d191571",
  "translation_date": "2025-10-15T03:41:16+00:00",
  "source_file": "getting_started/github-actions-guide/github-actions-guide-org.md",
  "language_code": "ms"
}
-->
# Menggunakan Co-op Translator GitHub Action (Panduan Organisasi)

**Sasaran Pembaca:** Panduan ini ditujukan untuk **pengguna dalaman Microsoft** atau **pasukan yang mempunyai akses kepada kelayakan yang diperlukan untuk Co-op Translator GitHub App yang telah dibina** atau boleh mencipta GitHub App tersuai mereka sendiri.

Automatikkan terjemahan dokumentasi repositori anda dengan mudah menggunakan Co-op Translator GitHub Action. Panduan ini akan membimbing anda untuk menyediakan action supaya secara automatik mencipta pull request dengan terjemahan yang dikemas kini setiap kali fail Markdown sumber atau imej anda berubah.

> [!IMPORTANT]
>
> **Memilih Panduan yang Betul:**
>
> Panduan ini menerangkan cara penyediaan menggunakan **GitHub App ID dan Private Key**. Anda biasanya memerlukan kaedah "Panduan Organisasi" ini jika: **`GITHUB_TOKEN` Dihadkan:** Tetapan organisasi atau repositori anda mengehadkan kebenaran lalai yang diberikan kepada `GITHUB_TOKEN` standard. Khususnya, jika `GITHUB_TOKEN` tidak dibenarkan kebenaran `write` yang diperlukan (seperti `contents: write` atau `pull-requests: write`), workflow dalam [Panduan Awam](./github-actions-guide-public.md) akan gagal kerana kebenaran tidak mencukupi. Menggunakan GitHub App khusus dengan kebenaran yang diberikan secara eksplisit akan mengatasi had ini.
>
> **Jika perkara di atas tidak terpakai kepada anda:**
>
> Jika `GITHUB_TOKEN` standard mempunyai kebenaran yang mencukupi dalam repositori anda (iaitu, anda tidak dihalang oleh sekatan organisasi), sila gunakan **[Panduan Awam menggunakan GITHUB_TOKEN](./github-actions-guide-public.md)**. Panduan awam tidak memerlukan anda mendapatkan atau mengurus App ID atau Private Key dan hanya bergantung pada `GITHUB_TOKEN` standard dan kebenaran repositori.

## Prasyarat

Sebelum mengkonfigurasi GitHub Action, pastikan anda telah menyediakan kelayakan perkhidmatan AI yang diperlukan.

**1. Diperlukan: Kelayakan Model Bahasa AI**
Anda memerlukan kelayakan untuk sekurang-kurangnya satu Model Bahasa yang disokong:

- **Azure OpenAI**: Memerlukan Endpoint, API Key, Nama Model/Deployment, Versi API.
- **OpenAI**: Memerlukan API Key, (Pilihan: Org ID, Base URL, Model ID).
- Lihat [Model dan Perkhidmatan yang Disokong](../../../../README.md) untuk maklumat lanjut.
- Panduan Penyediaan: [Sediakan Azure OpenAI](../set-up-resources/set-up-azure-openai.md).

**2. Pilihan: Kelayakan Computer Vision (untuk Terjemahan Imej)**

- Hanya diperlukan jika anda ingin menterjemah teks dalam imej.
- **Azure Computer Vision**: Memerlukan Endpoint dan Subscription Key.
- Jika tidak disediakan, action akan menggunakan [mod Markdown sahaja](../markdown-only-mode.md).
- Panduan Penyediaan: [Sediakan Azure Computer Vision](../set-up-resources/set-up-azure-computer-vision.md).

## Penyediaan dan Konfigurasi

Ikuti langkah-langkah berikut untuk mengkonfigurasi Co-op Translator GitHub Action dalam repositori anda:

### Langkah 1: Pasang dan Konfigurasi Pengesahan GitHub App

Workflow ini menggunakan pengesahan GitHub App untuk berinteraksi dengan selamat dengan repositori anda (cth., mencipta pull request) bagi pihak anda. Pilih satu pilihan:

#### **Pilihan A: Pasang Co-op Translator GitHub App yang Telah Dibina (untuk Penggunaan Dalaman Microsoft)**

1. Pergi ke halaman [Co-op Translator GitHub App](https://github.com/apps/co-op-translator).

1. Pilih **Install** dan pilih akaun atau organisasi di mana repositori sasaran anda berada.

    ![Install app](../../../../translated_images/install-app.d0f0a24cbb1d6c93f293f002eb34e633f7bc8f5caaba46b97806ba7bdc958f27.ms.png)

1. Pilih **Only select repositories** dan pilih repositori sasaran anda (cth., `PhiCookBook`). Klik **Install**. Anda mungkin diminta untuk mengesahkan.

    ![Install authorize](../../../../translated_images/install-authorize.29df6238c3eb8f707e7fc6f97a946cb654b328530c4aeddce28b874693f076a0.ms.png)

1. **Dapatkan Kelayakan App (Proses Dalaman Diperlukan):** Untuk membolehkan workflow mengesahkan sebagai app, anda memerlukan dua maklumat yang diberikan oleh pasukan Co-op Translator:
   - **App ID:** Pengenal unik untuk Co-op Translator app. App ID ialah: `1164076`.
   - **Private Key:** Anda mesti mendapatkan **keseluruhan kandungan** fail private key `.pem` daripada kontak penyelenggara. **Layan kunci ini seperti kata laluan dan pastikan ia selamat.**

1. Teruskan ke Langkah 2.

#### **Pilihan B: Gunakan GitHub App Tersuai Anda Sendiri**

- Jika anda mahu, anda boleh mencipta dan mengkonfigurasi GitHub App anda sendiri. Pastikan ia mempunyai akses Read & write kepada Contents dan Pull requests. Anda akan memerlukan App ID dan Private Key yang dijana.

### Langkah 2: Konfigurasi Secrets Repositori

Anda perlu menambah kelayakan GitHub App dan kelayakan perkhidmatan AI anda sebagai secrets yang disulitkan dalam tetapan repositori anda.

1. Pergi ke repositori GitHub sasaran anda (cth., `PhiCookBook`).

1. Pergi ke **Settings** > **Secrets and variables** > **Actions**.

1. Di bawah **Repository secrets**, klik **New repository secret** untuk setiap secret yang disenaraikan di bawah.

   ![Select setting action](../../../../translated_images/select-setting-action.3b95c915d60311592ca51ecb91b3a7bbe0ae45438a2ee872c1520dc90b677780.ms.png)

**Secrets Diperlukan (untuk Pengesahan GitHub App):**

| Nama Secret          | Penerangan                                      | Sumber Nilai                                     |
| :------------------- | :---------------------------------------------- | :----------------------------------------------- |
| `GH_APP_ID`          | App ID untuk GitHub App (dari Langkah 1).       | Tetapan GitHub App                               |
| `GH_APP_PRIVATE_KEY` | **Keseluruhan kandungan** fail `.pem` yang dimuat turun. | Fail `.pem` (dari Langkah 1)                  |

**Secrets Perkhidmatan AI (Tambah SEMUA yang berkaitan mengikut Prasyarat anda):**

| Nama Secret                         | Penerangan                               | Sumber Nilai                     |
| :---------------------------------- | :---------------------------------------- | :------------------------------- |
| `AZURE_AI_SERVICE_API_KEY`            | Kunci untuk Azure AI Service (Computer Vision)  | Azure AI Foundry                    |
| `AZURE_AI_SERVICE_ENDPOINT`         | Endpoint untuk Azure AI Service (Computer Vision) | Azure AI Foundry                     |
| `AZURE_OPENAI_API_KEY`              | Kunci untuk perkhidmatan Azure OpenAI              | Azure AI Foundry                     |
| `AZURE_OPENAI_ENDPOINT`             | Endpoint untuk perkhidmatan Azure OpenAI         | Azure AI Foundry                     |
| `AZURE_OPENAI_MODEL_NAME`           | Nama Model Azure OpenAI anda              | Azure AI Foundry                     |
| `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` | Nama Deployment Azure OpenAI anda         | Azure AI Foundry                     |
| `AZURE_OPENAI_API_VERSION`          | Versi API untuk Azure OpenAI              | Azure AI Foundry                     |
| `OPENAI_API_KEY`                    | API Key untuk OpenAI                        | OpenAI Platform                  |
| `OPENAI_ORG_ID`                     | OpenAI Organization ID                    | OpenAI Platform                  |
| `OPENAI_CHAT_MODEL_ID`              | ID model OpenAI tertentu                  | OpenAI Platform                    |
| `OPENAI_BASE_URL`                   | Custom OpenAI API Base URL                | OpenAI Platform                    |

![Enter environment variable name](../../../../translated_images/add-secrets-done.444861ce6956d5cb20781ead1237fcc12805078349bb0d4e95bb9540ee192227.ms.png)

### Langkah 3: Cipta Fail Workflow

Akhir sekali, cipta fail YAML yang mentakrifkan workflow automatik.

1. Dalam direktori root repositori anda, cipta direktori `.github/workflows/` jika belum wujud.

1. Di dalam `.github/workflows/`, cipta fail bernama `co-op-translator.yml`.

1. Tampal kandungan berikut ke dalam co-op-translator.yml.

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

4.  **Sesuaikan Workflow:**
   - **[!IMPORTANT] Bahasa Sasaran:** Dalam langkah `Run Co-op Translator`, anda **MESTI semak dan ubah senarai kod bahasa** dalam arahan `translate -l "..." -y` supaya sesuai dengan keperluan projek anda. Senarai contoh (`ar de es...`) perlu diganti atau dilaraskan.
   - **Trigger (`on:`):** Trigger semasa berjalan pada setiap push ke `main`. Untuk repositori besar, pertimbangkan untuk menambah penapis `paths:` (lihat contoh yang dikomen dalam YAML) supaya workflow hanya berjalan apabila fail berkaitan (cth., dokumentasi sumber) berubah, menjimatkan masa runner.
   - **Butiran PR:** Sesuaikan `commit-message`, `title`, `body`, nama `branch`, dan `labels` dalam langkah `Create Pull Request` jika perlu.

## Pengurusan dan Pembaharuan Kelayakan

- **Keselamatan:** Sentiasa simpan kelayakan sensitif (API key, private key) sebagai secrets GitHub Actions. Jangan dedahkan dalam fail workflow atau kod repositori anda.
- **[!IMPORTANT] Pembaharuan Kunci (Pengguna Dalaman Microsoft):** Sila ambil maklum bahawa kunci Azure OpenAI yang digunakan dalam Microsoft mungkin tertakluk kepada polisi pembaharuan mandatori (cth., setiap 5 bulan). Pastikan anda mengemas kini secrets GitHub yang berkaitan (`AZURE_OPENAI_...`) **sebelum ia tamat tempoh** untuk mengelakkan kegagalan workflow.

## Menjalankan Workflow

> [!WARNING]  
> **Had Masa Runner GitHub-hosted:**  
> Runner yang dihoskan GitHub seperti `ubuntu-latest` mempunyai **had masa maksimum 6 jam** untuk setiap pelaksanaan.  
> Untuk repositori dokumentasi yang besar, jika proses terjemahan melebihi 6 jam, workflow akan ditamatkan secara automatik.  
> Untuk mengelakkan ini, pertimbangkan:  
> - Menggunakan **self-hosted runner** (tiada had masa)  
> - Mengurangkan bilangan bahasa sasaran setiap kali run

Sebaik sahaja fail `co-op-translator.yml` digabungkan ke dalam cawangan utama anda (atau cawangan yang ditentukan dalam trigger `on:`), workflow akan berjalan secara automatik setiap kali perubahan ditolak ke cawangan tersebut (dan sepadan dengan penapis `paths`, jika dikonfigurasi).

Jika terjemahan dijana atau dikemas kini, action akan secara automatik mencipta Pull Request yang mengandungi perubahan tersebut, sedia untuk semakan dan penggabungan anda.

---

**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk memastikan ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat kritikal, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.