# Konfigurasi

Co-op Translator memerlukan satu penyedia model bahasa. Terjemahan imej juga memerlukan Azure AI Vision.

Konfigurasi dibaca daripada pembolehubah persekitaran. Untuk projek tempatan, letakkan mereka dalam fail `.env` di akar projek.

Untuk penyediaan sumber Azure, lihat [Persediaan Azure AI](azure-ai-setup.md).

## Persediaan runtime tempatan

Gunakan persekitaran maya sebelum menjalankan CLI secara tempatan. Co-op Translator menyokong Python 3.10 hingga 3.12.

Untuk penggunaan CLI biasa, pasang pakej yang diterbitkan di dalam persekitaran maya:

=== "Windows"

    ```powershell
    python -m venv .venv
    .venv\Scripts\activate
    pip install co-op-translator
    translate --help
    ```

=== "macOS / Linux"

    ```bash
    python -m venv .venv
    source .venv/bin/activate
    pip install co-op-translator
    translate --help
    ```

Untuk pembangunan repositori, pasang kebergantungan dari akar projek sebaliknya:

```bash
poetry install
poetry run translate --help
```

Selepas CLI tersedia, konfigurasikan satu penyedia model bahasa dalam `.env`.

## Pemilihan penyedia

Alat ini mengesan penyedia secara automatik mengikut susunan berikut:

1. Azure OpenAI
2. OpenAI

Jika tiada penyedia dikonfigurasikan, `translate`, `evaluate`, `migrate-links`, dan `run_translation` gagal semasa pemeriksaan konfigurasi. `co-op-review` dan `run_review` adalah pemeriksaan penyelenggaraan deterministik dan tidak memerlukan kredensial penyedia.

## Azure OpenAI

Gunakan Azure OpenAI apabila model anda disebarkan dalam Azure AI Foundry atau Azure OpenAI Service.

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Pemeriksaan kesambungan menggunakan endpoint, kunci API, versi API, dan nama penyebaran sebelum terjemahan bermula.

## OpenAI

Gunakan OpenAI apabila memanggil OpenAI API secara langsung.

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
OPENAI_ORG_ID="..."          # pilihan
OPENAI_BASE_URL="..."        # pilihan
```

`OPENAI_CHAT_MODEL_ID` diperlukan kerana penterjemah memerlukan model perbualan yang jelas untuk panggilan API.

## Azure AI Vision

Terjemahan imej memerlukan Azure AI Vision supaya alat dapat mengekstrak teks dari imej sebelum menterjemahkannya.

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

Jika terjemahan imej dipilih dengan `-img`, `images=True`, atau tiada penapis jenis-kandungan, alat mengesahkan konfigurasi Vision sebelum terjemahan bermula.

## Beberapa set kredensial

Lapisan konfigurasi menyokong beberapa set kredensial dengan menambah sufiks pada pembolehubah menggunakan indeks yang sama:

```bash
AZURE_OPENAI_API_KEY_1="..."
AZURE_OPENAI_ENDPOINT_1="https://<resource-1>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME_1="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME_1="<deployment-1>"
AZURE_OPENAI_API_VERSION_1="2024-12-01-preview"

AZURE_OPENAI_API_KEY_2="..."
AZURE_OPENAI_ENDPOINT_2="https://<resource-2>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME_2="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME_2="<deployment-2>"
AZURE_OPENAI_API_VERSION_2="2024-12-01-preview"
```

Setiap set mesti lengkap. Pemeriksaan kesihatan memilih set yang berfungsi sebelum terjemahan diteruskan.

## Keperluan arahan

| Perintah atau API | Perlukan LLM | Perlukan Vision | Nota |
| --- | --- | --- | --- |
| `translate -md` | Ya | Tidak | Menterjemah Markdown sahaja. |
| `translate -nb` | Ya | Tidak | Menterjemah buku nota sahaja. |
| `translate -img` | Ya | Ya | Menterjemah imej sahaja. |
| `translate` with no type flags | Ya | Ya | Mod lalai merangkumi Markdown, buku nota, dan imej. |
| `evaluate` | Ya | Tidak | Menggunakan penilaian LLM kecuali `--fast` dipilih. |
| `migrate-links` | Ya | Tidak | Melaksanakan migrasi pautan, tetapi masih menjalankan pemeriksaan konfigurasi berkongsi. |
| `co-op-review` | Tidak | Tidak | Menjalankan pemeriksaan struktur terjemahan deterministik, kesegaran, Markdown, buku nota, dan pautan tempatan. |
| `run_translation(markdown=True)` | Ya | Tidak | Terjemahan Markdown secara programatik. |
| `run_translation(images=True)` | Ya | Ya | Terjemahan imej secara programatik. |
| `run_review(...)` | Tidak | Tidak | Semakan deterministik secara programatik. |

## Direktori keluaran

Output terjemahan teks lalai:

```text
translations/<language-code>/<source-relative-path>
```

Output imej yang diterjemah lalai:

```text
translated_images/<language-code>/<source-relative-path>
```

Python API boleh menulis ganti direktori ini dengan `translations_dir` dan `image_dir`.