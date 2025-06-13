<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "66029e3b67a3eb980ab8740367e91283",
  "translation_date": "2025-06-12T18:28:19+00:00",
  "source_file": "getting_started/command-line-guide/create-env-file.md",
  "language_code": "ms"
}
-->
# Cipta fail *.env* di direktori akar

Dalam tutorial ini, kami akan membimbing anda untuk menyediakan pembolehubah persekitaran bagi perkhidmatan Azure menggunakan fail *.env*. Pembolehubah persekitaran membolehkan anda menguruskan kelayakan sensitif dengan selamat, seperti kunci API, tanpa perlu menulisnya terus ke dalam kod anda.

> [!IMPORTANT]
> - Hanya satu perkhidmatan model bahasa (Azure OpenAI atau OpenAI) perlu dikonfigurasikan. Isikan pembolehubah persekitaran untuk perkhidmatan pilihan anda. Jika pembolehubah persekitaran untuk pelbagai model bahasa ditetapkan, penterjemah bersama akan memilih satu berdasarkan keutamaan.
> - Jika pembolehubah persekitaran Computer Vision tidak ditetapkan, penterjemah akan secara automatik bertukar ke [mod Markdown sahaja](./markdown-only-mode.md).

> [!NOTE]
> Panduan ini memberi tumpuan terutamanya kepada perkhidmatan Azure, tetapi anda boleh memilih mana-mana model bahasa yang disokong daripada [senarai model dan perkhidmatan yang disokong](../README.md#-supported-models-and-services).

## Cipta fail *.env*

Di direktori akar projek anda, cipta fail bernama *.env*. Fail ini akan menyimpan semua pembolehubah persekitaran anda dalam format yang ringkas.

> [!WARNING]
> Jangan komit fail *.env* anda ke sistem kawalan versi seperti Git. Tambahkan *.env* ke dalam fail .gitignore anda untuk mengelakkan komit tidak sengaja.

1. Pergi ke direktori akar projek anda.

1. Cipta fail *.env* di direktori akar projek anda.

1. Buka fail *.env* dan tampal templat berikut:

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
> Jika anda ingin mencari kunci API dan titik akhir anda, anda boleh rujuk kepada [set-up-azure-ai.md](../set-up-azure-ai.md).

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya hendaklah dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh penterjemah manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau tafsiran yang salah yang timbul daripada penggunaan terjemahan ini.