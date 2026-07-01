# Yapılandırma

Co-op Translator bir dil modeli sağlayıcısı gerektirir. Görsel çevirileri ayrıca Azure AI Vision gerektirir.

Yapılandırma çevresel değişkenlerden okunur. Yerel projeler için bunları proje kökünde bir `.env` dosyasına yerleştirin.

Azure kaynak kurulumu için bkz. [Azure AI Kurulumu](azure-ai-setup.md).

## Yerel runtime kurulumu

CLI'yi yerelde çalıştırmadan önce bir sanal ortam kullanın. Co-op Translator Python 3.10 ile 3.12 sürümlerini destekler.

Normal CLI kullanımı için yayımlanmış paketi bir sanal ortam içine kurun:

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

Depoda geliştirme yapıyorsanız, bunun yerine proje kökünden bağımlılıkları kurun:

```bash
poetry install
poetry run translate --help
```

CLI kullanılabilir hale geldikten sonra `.env` içinde bir dil modeli sağlayıcısı yapılandırın.

## Sağlayıcı seçimi

Araç sağlayıcıları aşağıdaki sırayla otomatik algılar:

1. Azure OpenAI
2. OpenAI

Hiçbir sağlayıcı yapılandırılmamışsa, `translate`, `evaluate`, `migrate-links`, ve `run_translation` yapılandırma kontrolleri sırasında başarısız olur. `co-op-review` ve `run_review` deterministik bakım kontrolleridir ve sağlayıcı kimlik bilgileri gerektirmez.

## Azure OpenAI

Modeliniz Azure AI Foundry veya Azure OpenAI Service üzerinde dağıtıldıysa Azure OpenAI kullanın.

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Bağlantı kontrolü çeviri başlamadan önce uç noktayı, API anahtarını, API sürümünü ve dağıtım adını kullanır.

## OpenAI

OpenAI API'sini doğrudan çağırırken OpenAI kullanın.

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
OPENAI_ORG_ID="..."          # isteğe bağlı
OPENAI_BASE_URL="..."        # isteğe bağlı
```

`OPENAI_CHAT_MODEL_ID` gereklidir çünkü çevirmen API çağrıları için açık bir sohbet modeline ihtiyaç duyar.

## Azure AI Vision

Görsel çevirisi, aracın çeviri öncesinde görüntülerden metin çıkarması için Azure AI Vision gerektirir.

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

Görsel çevirisi `-img`, `images=True` ile seçildiğinde veya içerik türü filtresi yoksa, araç çeviri başlamadan önce Vision yapılandırmasını doğrular.

## Birden çok kimlik bilgisi seti

Yapılandırma katmanı, değişkenlere aynı indeksin eklenmesiyle birden çok kimlik bilgisi setini destekler:

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

Her set eksiksiz olmalıdır. Sağlık kontrolü çeviri ilerlemeden önce çalışan bir set seçer.

## Komut gereksinimleri

| Komut veya API | LLM gerekli | Vision gerekli | Notlar |
| --- | --- | --- | --- |
| `translate -md` | Evet | Hayır | Sadece Markdown'u çevirir. |
| `translate -nb` | Evet | Hayır | Sadece notebook'ları çevirir. |
| `translate -img` | Evet | Evet | Sadece görselleri çevirir. |
| `translate` with no type flags | Evet | Evet | Varsayılan mod Markdown, notebook'lar ve görselleri içerir. |
| `evaluate` | Evet | Hayır | LLM değerlendirmesini kullanır, `--fast` seçilmedikçe. |
| `migrate-links` | Evet | Hayır | Bağlantı göçünü gerçekleştirir, ancak yine de paylaşılan yapılandırma kontrollerini çalıştırır. |
| `co-op-review` | Hayır | Hayır | Deterministik çeviri yapısı, tazelik, Markdown, notebook ve yerel bağlantı kontrollerini çalıştırır. |
| `run_translation(markdown=True)` | Evet | Hayır | Programatik Markdown çevirisi. |
| `run_translation(images=True)` | Evet | Evet | Programatik görsel çevirisi. |
| `run_review(...)` | Hayır | Hayır | Programatik deterministik inceleme. |

## Çıktı dizinleri

Varsayılan metin çeviri çıktısı:

```text
translations/<language-code>/<source-relative-path>
```

Varsayılan çevrilmiş görsel çıktısı:

```text
translated_images/<language-code>/<source-relative-path>
```

Python API'si bu dizinleri `translations_dir` ve `image_dir` ile geçersiz kılabilir.