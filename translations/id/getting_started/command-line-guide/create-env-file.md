<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "53c99ea0ead7a3500149d4bb96be5811",
  "translation_date": "2025-05-06T17:55:28+00:00",
  "source_file": "getting_started/command-line-guide/create-env-file.md",
  "language_code": "id"
}
-->
# Buat file *.env* di direktori root

Dalam tutorial ini, kami akan memandu Anda dalam mengatur variabel lingkungan untuk layanan Azure menggunakan file *.env*. Variabel lingkungan memungkinkan Anda mengelola kredensial sensitif dengan aman, seperti kunci API, tanpa harus menuliskannya langsung ke dalam kode.

> [!IMPORTANT]
> - Hanya satu layanan model bahasa (Azure OpenAI atau OpenAI) yang perlu dikonfigurasi. Isi variabel lingkungan untuk layanan yang Anda pilih. Jika variabel lingkungan untuk beberapa model bahasa diatur, penerjemah co-op akan memilih salah satu berdasarkan prioritas.
> - Jika variabel lingkungan Computer Vision tidak diatur, penerjemah akan secara otomatis beralih ke [mode Markdown saja](./markdown-only-mode.md).

> [!NOTE]
> Panduan ini terutama berfokus pada layanan Azure, tetapi Anda dapat memilih model bahasa mana saja yang didukung dari [daftar model dan layanan yang didukung](../README.md#-supported-models-and-services).

## Buat file *.env*

Di direktori root proyek Anda, buat file bernama *.env*. File ini akan menyimpan semua variabel lingkungan Anda dalam format sederhana.

> [!WARNING]
> Jangan commit file *.env* Anda ke sistem kontrol versi seperti Git. Tambahkan *.env* ke file .gitignore Anda untuk mencegah commit yang tidak disengaja.

1. Arahkan ke direktori root proyek Anda.

1. Buat file *.env* di direktori root proyek Anda.

    ![Buat file *.env*.](../../../../imgs/create-env.png)

1. Buka file *.env* dan tempelkan template berikut:

    ```plaintext
    # Azure Credentials
    AZURE_SUBSCRIPTION_KEY="your_azure_AIServices_api_key"
    AZURE_AI_SERVICE_ENDPOINT="https://your_azure_ai_service_endpoint"

    # Azure OpenAI Credentials
    AZURE_OPENAI_API_KEY="your_azure_openai_api_key"
    AZURE_OPENAI_ENDPOINT="https://your_azure_openai_endpoint"
    AZURE_OPENAI_MODEL_NAME="your_model_name"
    AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="your_deployment_name"
    AZURE_OPENAI_API_VERSION="your_api_version"

    # OpenAI Credentials
    OPENAI_API_KEY="your_openai_api_key"
    OPENAI_ORG_ID="your_openai_org_id"
    OPENAI_CHAT_MODEL_ID="your_chat_model_id(ex. gpt-4o)"
    OPENAI_BASE_URL="https://api.openai.com/v1 (If you don't have a custom base URL, you can delete this lin, then it will use the default base URL)"
    ```

## Kumpulkan kredensial Azure Anda

Anda akan membutuhkan kredensial Azure berikut untuk mengonfigurasi lingkungan:

Anda dapat memperoleh semua detail dari halaman overview proyek di dalam [AI Foundry](https://ai.azure.com/build/overview)

![Foundry-overview](../../../../imgs/foundry-overview.png)


### Untuk Layanan Azure AI:

    - Azure Subscription Key: Kunci API Layanan Azure AI Anda, yang memungkinkan Anda mengakses layanan Azure AI.
    - Azure AI Service Endpoint: URL endpoint untuk layanan Azure AI spesifik Anda.

### Untuk Layanan Azure OpenAI:

    - Azure OpenAI API Key: Kunci API untuk mengakses layanan Azure OpenAI.
    - Azure OpenAI Endpoint: URL endpoint untuk layanan Azure OpenAI Anda.


1. Salin dan tempel kunci dan Endpoint Layanan AI Anda ke dalam file *.env*.
2. Salin dan tempel Kunci API dan Endpoint Azure OpenAI Anda ke dalam file *.env*.

### Detail Model

Pilih Model dan Endpoint dari menu sebelah kiri

![FoundryModels](../../../../imgs/gpt-models.png)

Sekarang Anda perlu memilih model yang ingin Anda gunakan untuk mendapatkan detail model

![ModelDetails](../../../../imgs/model-deployment-name.png)

Untuk file .env kita memerlukan detail berikut

    - Azure OpenAI Model Name: Nama model yang akan Anda gunakan.
    - Azure OpenAI Name: Nama deployment Anda untuk model Azure OpenAI.
    - Azure OpenAI API Version: Versi API Azure OpenAI yang Anda gunakan, yang dapat ditemukan di akhir string URL.

Untuk mendapatkan detail ini, pilih deployment model

![FoundryModelinfo](../../../../imgs/foundry-model-info.png)

### Tambahkan variabel lingkungan Azure

3. Salin dan tempel **Name** dan **Version** model Azure OpenAI Anda ke dalam file *.env*.
4. Simpan file *.env*.
5. Sekarang, Anda dapat mengakses variabel lingkungan ini untuk menggunakan **Co-op Translator** dengan layanan Azure Anda.

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berusaha untuk akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang salah yang timbul dari penggunaan terjemahan ini.