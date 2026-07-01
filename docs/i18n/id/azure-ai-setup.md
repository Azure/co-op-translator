# Penyiapan Azure AI

Gunakan panduan ini ketika Anda ingin mengonfigurasi Azure OpenAI untuk terjemahan teks dan Azure AI Vision untuk ekstraksi teks dari gambar.

## Prasyarat

- Langganan Azure.
- Izin untuk membuat atau menggunakan sumber daya Azure AI dan penerapan model.
- Sebuah proyek di Azure AI Foundry atau akses setara ke sumber daya Azure OpenAI dan Azure AI Vision.

## Buat Proyek Azure AI

1. Buka [Azure AI Foundry](https://ai.azure.com).
2. Buat atau pilih proyek.
3. Buat atau pilih AI hub untuk proyek tersebut.
4. Buka ikhtisar proyek setelah dibuat.

## Terapkan Model Azure OpenAI

1. Dalam proyek, buka **Models + endpoints**.
2. Pilih **Deploy model**.
3. Pilih model GPT seperti `gpt-4o`.
4. Terapkan model.
5. Catat endpoint, nama deployment, nama model, API key, dan versi API.

!!! note
    Versi API Azure OpenAI terpisah dari versi model yang ditampilkan di Azure AI Foundry. Pilih versi API yang didukung untuk penerapan Anda.

## Konfigurasikan Azure AI Vision

Terjemahan gambar menggunakan Azure AI Vision untuk mengekstrak teks dari gambar sumber sebelum teks diterjemahkan.

Dalam proyek Azure AI Anda, temukan kunci dan endpoint Azure AI Services.

![Temukan informasi layanan Azure AI](../../assets/find-azure-ai-info.png)

Catat:

- Endpoint Layanan Azure AI
- Kunci API Layanan Azure AI

## Variabel Lingkungan

Tambahkan kredensial ke file `.env` Anda atau rahasia CI.

```bash
# Azure AI Vision, diperlukan untuk penerjemahan gambar
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"

# Azure OpenAI, diperlukan untuk penerjemahan teks
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Co-op Translator juga mendukung set kredensial fallback opsional. Gandakan satu set penyedia lengkap dengan sufiks seperti `_1` atau `_2`; semua variabel dalam set fallback harus memiliki sufiks yang sama.

```bash
AZURE_OPENAI_API_KEY_1="..."
AZURE_OPENAI_ENDPOINT_1="https://<resource-1>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME_1="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME_1="<deployment-1>"
AZURE_OPENAI_API_VERSION_1="2024-12-01-preview"
```

## Langkah Selanjutnya

- Kembali ke [Konfigurasi](configuration.md) untuk menyiapkan variabel lingkungan lokal atau CI.
- Gunakan [Referensi CLI](cli.md) untuk perintah terjemahan.
- Gunakan [GitHub Actions](github-actions.md) untuk mengotomatiskan permintaan tarik (pull request) terjemahan.