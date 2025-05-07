<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "10d8cb07ad0d2ee6705439d4e382ecc9",
  "translation_date": "2025-05-06T18:16:14+00:00",
  "source_file": "getting_started/set-up-resources/set-up-azure-openai.md",
  "language_code": "id"
}
-->
# Menyiapkan Azure OpenAI untuk terjemahan bahasa

## Membuat sumber daya Azure OpenAI di Azure AI Foundry

Untuk menyiapkan Azure OpenAI di Azure AI Foundry, ikuti langkah-langkah berikut:

### Membuat Hub

1. Masuk ke [portal Azure AI Foundry](https://ai.azure.com): Pastikan Anda sudah masuk dengan akun Azure Anda.

2. Arahkan ke Management Center: Dari halaman utama, pilih "Management Center" dari menu sebelah kiri.

3. Buat Hub Baru: Klik "+ New hub" dan masukkan detail yang diperlukan seperti Subscription, Resource Group, dan Hub Name, kami menyarankan untuk menempatkan hub di East US karena wilayah ini mendukung Cognitive vision dan model GPT.

4. Tinjau dan Buat: Periksa kembali detailnya dan klik "Create" untuk menyiapkan hub Anda.

### Membuat Proyek

1. Pergi ke Halaman Utama: Jika belum di sana, pilih "Azure AI Foundry" di kiri atas halaman untuk kembali ke halaman utama.

2. Buat Proyek: Klik "+ Create project" dan masukkan nama untuk proyek Anda.

3. Pilih Hub: Jika Anda memiliki beberapa hub, pilih yang ingin digunakan. Jika ingin membuat hub baru, Anda dapat melakukannya pada langkah ini.

4. Konfigurasikan Proyek: Ikuti petunjuk untuk mengatur proyek sesuai kebutuhan Anda.

5. Buat Proyek: Klik "Create" untuk menyelesaikan pengaturan.

### Men-deploy Model dan Endpoint untuk model OpenAI

1. Masuk ke [portal Azure AI Foundry](https://ai.azure.com): Pastikan Anda sudah masuk dengan subscription Azure yang memiliki sumber daya Azure OpenAI Service Anda.

2. Arahkan ke Models and Endpoint: Dari halaman utama Azure AI Foundry, cari tile yang bertuliskan " dan pilih "Let's go." atau Models and Endpoints di menu sebelah kiri.

3. Jika Anda belum memiliki model GPT yang sudah dideploy, pilih deploy model: pilih model GPT, kami merekomendasikan GPT-4o, GPT-4o-mini, atau o3-mini.

4. Akses sumber daya Anda: Anda akan melihat sumber daya Azure OpenAI Service yang sudah ada. Jika Anda memiliki beberapa sumber daya, gunakan selector untuk memilih yang ingin Anda gunakan.

Untuk instruksi lebih rinci, Anda dapat merujuk ke dokumentasi resmi Azure AI Foundry.

[How to Create a project](https://learn.microsoft.com/azure/ai-studio/how-to/create-project)

[How to Create resources](https://learn.microsoft.com/azure/ai-studio/how-to/create-azure-ai-resource)

[How to use OpenAI Model in AI Foundry](https://learn.microsoft.com/azure/ai-studio/ai-services/how-to/connect-azure-openai)

[OpenAI Services in Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/azure-openai-in-ai-studio)

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berusaha untuk akurasi, harap diingat bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sahih. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau salah tafsir yang timbul dari penggunaan terjemahan ini.