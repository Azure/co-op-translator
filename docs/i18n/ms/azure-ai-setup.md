# Persediaan Azure AI

Gunakan panduan ini apabila anda ingin mengkonfigurasi Azure OpenAI untuk terjemahan teks dan Azure AI Vision untuk pengekstrakan teks dari imej.

## Prasyarat

- Langganan Azure.
- Kebenaran untuk membuat atau menggunakan sumber Azure AI dan penyebaran model.
- Projek dalam Azure AI Foundry atau akses setara kepada sumber Azure OpenAI dan Azure AI Vision.

## Buat Projek Azure AI

1. Buka [Azure AI Foundry](https://ai.azure.com).
2. Buat atau pilih projek.
3. Buat atau pilih hab AI untuk projek.
4. Buka gambaran keseluruhan projek selepas penciptaan.

## Menerapkan Model Azure OpenAI

1. Dalam projek, buka **Models + endpoints**.
2. Pilih **Deploy model**.
3. Pilih model GPT seperti `gpt-4o`.
4. Terapkan model tersebut.
5. Catat endpoint, nama penyebaran, nama model, kunci API, dan versi API.

!!! note
    Versi API Azure OpenAI adalah berasingan daripada versi model yang dipaparkan dalam Azure AI Foundry. Pilih versi API yang disokong untuk penyebaran anda.

## Konfigurasi Azure AI Vision

Terjemahan imej menggunakan Azure AI Vision untuk mengekstrak teks daripada imej sumber sebelum teks diterjemahkan.

Dalam projek Azure AI anda, cari kunci dan endpoint Azure AI Services.

![Cari maklumat perkhidmatan Azure AI](../../assets/find-azure-ai-info.png)

Record:

- Endpoint Perkhidmatan Azure AI
- Kunci API Perkhidmatan Azure AI

## Pembolehubah Persekitaran

Tambah kredensial ke dalam fail `.env` anda atau rahsia CI.

```bash
# Azure AI Vision, diperlukan untuk terjemahan imej
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"

# Azure OpenAI, diperlukan untuk terjemahan teks
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Co-op Translator juga menyokong set kredensial fallback pilihan. Gandakan satu set pembekal lengkap dengan sufiks seperti `_1` atau `_2`; semua pembolehubah dalam set fallback mesti berkongsi sufiks yang sama.

```bash
AZURE_OPENAI_API_KEY_1="..."
AZURE_OPENAI_ENDPOINT_1="https://<resource-1>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME_1="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME_1="<deployment-1>"
AZURE_OPENAI_API_VERSION_1="2024-12-01-preview"
```

## Langkah Seterusnya

- Kembali ke [Konfigurasi](configuration.md) untuk menyediakan pembolehubah persekitaran tempatan atau CI.
- Gunakan [Rujukan CLI](cli.md) untuk arahan terjemahan.
- Gunakan [GitHub Actions](github-actions.md) untuk mengautomatikkan permintaan tarik terjemahan.