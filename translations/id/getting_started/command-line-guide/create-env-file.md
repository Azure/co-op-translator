<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "66029e3b67a3eb980ab8740367e91283",
  "translation_date": "2025-05-07T14:15:11+00:00",
  "source_file": "getting_started/command-line-guide/create-env-file.md",
  "language_code": "id"
}
-->
# Buat file *.env* di direktori root

Dalam tutorial ini, kami akan membimbing Anda dalam mengatur variabel lingkungan untuk layanan Azure menggunakan file *.env*. Variabel lingkungan memungkinkan Anda mengelola kredensial sensitif dengan aman, seperti kunci API, tanpa harus menuliskannya langsung di kode Anda.

> [!IMPORTANT]
> - Hanya satu layanan model bahasa (Azure OpenAI atau OpenAI) yang perlu dikonfigurasi. Isi variabel lingkungan untuk layanan yang Anda pilih. Jika variabel lingkungan untuk beberapa model bahasa diatur, penerjemah co-op akan memilih salah satu berdasarkan prioritas.
> - Jika variabel lingkungan Computer Vision tidak diatur, penerjemah akan otomatis beralih ke [mode hanya Markdown](./markdown-only-mode.md).

> [!NOTE]
> Panduan ini terutama berfokus pada layanan Azure, tetapi Anda dapat memilih model bahasa mana pun yang didukung dari [daftar model dan layanan yang didukung](../README.md#-supported-models-and-services).

## Buat file *.env*

Di direktori root proyek Anda, buat file bernama *.env*. File ini akan menyimpan semua variabel lingkungan Anda dalam format yang sederhana.

> [!WARNING]
> Jangan melakukan commit file *.env* ke sistem kontrol versi seperti Git. Tambahkan *.env* ke file .gitignore Anda untuk mencegah commit yang tidak disengaja.

1. Arahkan ke direktori root proyek Anda.

1. Buat file *.env* di direktori root proyek Anda.

1. Buka file *.env* dan tempelkan template berikut:

    ```plaintext
    # Azure Credentials
    AZURE_AI_SERVICE_API_KEY="your_azure_ai_service_api_key"
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

> [!NOTE]
> Jika Anda ingin menemukan kunci API dan endpoint Anda, Anda dapat merujuk ke [set-up-azure-ai.md](../set-up-azure-ai.md).

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berusaha untuk akurasi, harap diingat bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sahih. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau salah tafsir yang timbul dari penggunaan terjemahan ini.