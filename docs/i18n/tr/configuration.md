# Yapılandırma

Co-op Translator bir dil modeli sağlayıcısı gerektirir. Görsel çeviri için ek olarak Azure AI Vision gerekir.

Yapılandırma ortam değişkenlerinden okunur. Yerel projeler için bunları proje kökünde bir `.env` dosyasına koyun.

Azure kaynak kurulumu için bkz. [Azure AI Kurulumu](azure-ai-setup.md).

## Yerel çalışma zamanı kurulumu

CLI'yi yerel olarak çalıştırmadan önce bir sanal ortam kullanın. Co-op Translator Python 3.11 ile 3.14 arasını destekler.

Normal CLI kullanımı için yayımlanmış paketi bir sanal ortam içine yükleyin:

### Windows (PowerShell)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install co-op-translator
translate --help
```

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install co-op-translator
translate --help
```

### Depo geliştirme

Depo geliştirme için bağımlılıkları bunun yerine proje kökünden yükleyin:

```bash
poetry install
poetry run translate --help
```

CLI kullanılabilir olduktan sonra `.env` içinde bir dil modeli sağlayıcısı yapılandırın.

## Sağlayıcı seçimi

Araç sağlayıcıları şu sırayla otomatik algılar:

1. Azure OpenAI
2. OpenAI
3. Anthropic

Çeviri sağlayıcı kimlik bilgileri gerektirir, `translate -l "ko" -md --dry-run` gibi önizlemeler hariç. `migrate-links`, `co-op-review` ve `run_review` deterministik bakım işlemleridir ve sağlayıcı kimlik bilgileri gerektirmez.

## Model istemci arka ucu

Co-op Translator 0.22.0'dan itibaren Azure OpenAI, OpenAI ve Anthropic varsayılan olarak Microsoft Agent Framework kullanır. Normal kullanım için herhangi bir arka uç ayarı gerekli değildir.

Uyumluluk için Semantic Kernel geçici olarak kullanılabilir durumda kalır. Açıkça seçmek için şunu ayarlayın:

```bash
CO_OP_TRANSLATOR_MODEL_CLIENT="semantic-kernel"
```

Semantic Kernel kullanımı bir kullanım dışı bırakma uyarısı verir. Paketin Semantic Kernel'i 0.23.0 sürümünde isteğe bağlı bir bağımlılık haline getirmesi ve 0.24.0'te entegrasyonu kaldırması planlanıyor; bu, uyumluluk sonuçlarına ve kullanıcı geri bildirimlerine bağlıdır. Anthropic `agent-framework` gerektirir; Anthropic ile `semantic-kernel`'i açıkça seçmek yapılandırma hatasıyla başarısız olur. Geçersiz değerler, sessizce geri dönüş yapmak yerine sağlayıcı destekli çeviri başlatılırken hata verir. Yayılımı takip edin ve engelleyicileri [GitHub sorun #543](https://github.com/Azure/co-op-translator/issues/543) üzerinde bildirin.

## Azure OpenAI

Modeliniz Azure AI Foundry veya Azure OpenAI Service içinde dağıtıldığında Azure OpenAI kullanın.

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Bağlantı denetimi, çeviri başlamadan önce uç nokta, API anahtarı, API sürümü ve dağıtım adını kullanır.

## OpenAI

OpenAI API'sini doğrudan çağırırken OpenAI kullanın.

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

`OPENAI_CHAT_MODEL_ID` gereklidir çünkü çevirmenin API çağrıları için açık bir sohbet modeline ihtiyacı vardır.

`OPENAI_ORG_ID` ve `OPENAI_BASE_URL`'i varsayılan kurulum için boş bırakın. Yalnızca hesabınız bir kuruluş kimliği gerektiriyorsa bir kuruluş kimliği ekleyin veya yalnızca özel bir uç nokta kullanıyorsanız bir base URL ekleyin. İsteğe bağlı ayarlar için yer tutucu değerleri kopyalamayın.

## Anthropic Claude

Claude API'sini doğrudan çağırırken Anthropic kullanın. Bir [Anthropic API anahtarı](https://platform.claude.com/docs/en/get-started) oluşturun ve desteklenen bir [Claude model ID'si](https://platform.claude.com/docs/en/about-claude/models/model-ids-and-versions) seçin.

```bash
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

`ANTHROPIC_API_KEY` ve `ANTHROPIC_MODEL` gereklidir. `CO_OP_TRANSLATOR_MODEL_CLIENT`'ı ayarlamanıza gerek yoktur; Agent Framework varsayılan arka uçtur.

`ANTHROPIC_BASE_URL`'u Anthropic API için boş bırakın. Sadece özel bir uç nokta kullanıyorsanız ayarlayın.

`ANTHROPIC_MAX_TOKENS` varsayılan olarak `8192`'dir; bu Meitei Mayek gibi token açısından yoğun yazı sistemleri için alan bırakır. Modeliniz veya Anthropic uyumlu uç noktanız çıktıyı bunun altında sınırlandırıyorsa bunu düşürün.

## Azure AI Vision

Görüntü çevirisi, araç yapılandırılmış dil modeli çevirmeden önce görüntülerden metin çıkarabilmesi için Azure AI Vision gerektirir. Anthropic, çıkarılan metni Azure OpenAI veya OpenAI gibi çevirebilir.

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

`-img`, `images=True` ile veya içerik türü filtresi olmadan görüntü çevirisi seçildiyse, araç çeviri başlamadan önce Vision yapılandırmasını doğrular.

## Birden çok kimlik bilgisi seti

Yapılandırma katmanı, değişkenlere aynı indeks son eki ekleyerek birden çok kimlik bilgisi setini destekler:

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

Her kimlik bilgisi seti eksiksiz olmalıdır. Sağlık denetimi, çeviri ilerlemeden önce çalışan bir set seçer.

OpenAI ve Anthropic aynı son ek konvansiyonunu destekler. Bir kimlik bilgisi setindeki her bir değişkeni aynı sonda tutun; `OPENAI_BASE_URL_1` veya `ANTHROPIC_BASE_URL_1` gibi isteğe bağlı değerler dahil.

## Komut gereksinimleri

| Komut veya API | LLM gerekli | Vision gerekli | Notlar |
| --- | --- | --- | --- |
| `translate -md` | Evet | Hayır | Sadece Markdown'u çevirir. |
| `translate -nb` | Evet | Hayır | Sadece notebook'ları çevirir. |
| `translate -img` | Evet | Evet | Sadece görüntüleri çevirir. |
| `translate` tür bayrakları olmadan | Evet | Evet | Varsayılan mod Markdown, notebook'ları ve görüntüleri içerir. |
| `evaluate` | Evet | Hayır | `--fast` seçilmedikçe LLM değerlendirmesi kullanır. |
| `migrate-links` | Hayır | Hayır | Sağlayıcı çağrısı olmadan yerel bağlantı göçü gerçekleştirir. |
| `co-op-review` | Hayır | Hayır | Deterministik çeviri yapı, tazelik, Markdown, notebook ve yerel bağlantı kontrollerini çalıştırır. |
| `run_translation(markdown=True)` | Evet | Hayır | Programatik Markdown çevirisi. |
| `run_translation(images=True)` | Evet | Evet | Programatik görüntü çevirisi. |
| `run_review(...)` | Hayır | Hayır | Programatik deterministik inceleme. |

## Çıktı dizinleri

Varsayılan metin çeviri çıktısı:

```text
translations/<language-code>/<source-relative-path>
```

Varsayılan çevrilmiş görüntü çıktısı:

```text
translated_images/<language-code>/<source-relative-path>
```

Python API bu dizinleri `translations_dir` ve `image_dir` ile geçersiz kılabilir.