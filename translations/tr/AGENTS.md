<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3fd2055f97f093b6fe102ea24df4458b",
  "translation_date": "2025-10-15T04:27:04+00:00",
  "source_file": "AGENTS.md",
  "language_code": "tr"
}
-->
## Proje Genel Bakış

Co‑op Translator, Markdown dosyalarını, Jupyter defterlerini ve görsel metinlerini birden fazla dile çeviren bir Python komut satırı aracı ve GitHub Actions iş akışıdır. Çıktıları dil‑bazlı klasörlerde düzenler ve çevirileri kaynak içerikle senkronize tutar. Proje, CLI giriş noktaları olan, Poetry ile yönetilen bir kütüphane olarak yapılandırılmıştır.

### Mimari genel bakış

- CLI giriş noktaları (`translate`, `migrate-links`, `evaluate`) birleşik bir CLI'yi çağırır ve çeviri, bağlantı taşıma ve değerlendirme akışlarına yönlendirir.
- Yapılandırma yükleyici `.env` dosyasını okur ve LLM sağlayıcısını (Azure OpenAI veya OpenAI) otomatik olarak algılar; istenirse görsel sağlayıcıyı (Azure AI Service) da algılar ve görsel metni çıkarmak için kullanır.
- Çeviri çekirdeği Markdown ve defterleri işler; görsel hattı, `-img` kullanıldığında görsellerden metin çıkarır.
- Çıktılar, metin için `translations/<lang>/` ve görseller için `translated_images/` klasörlerinde, orijinal yapıyı koruyarak düzenlenir.

### Temel teknolojiler ve çerçeveler

- Python 3.10–3.12, paketleme için Poetry
- CLI: `click`
- LLM/AI SDK'ları: Azure OpenAI, OpenAI
- Görsel: Azure AI Service (Computer Vision)
- HTTP ve veri: `httpx`, `pydantic`
- Görselleştirme: `pillow`, `opencv-python`, `matplotlib`
- Araçlar: `pytest`, `black`, `ruff`

## Kurulum Komutları

### Ön Gereksinimler

- Python 3.10–3.12
- Azure aboneliği (isteğe bağlı, Azure AI servisleri için)
- LLM/Görsel API'leri için internet erişimi (örn. Azure OpenAI/OpenAI, Azure AI Vision)

### Seçenek A: Poetry (önerilen)

```bash
# From repository root
pip install poetry
poetry install

# Run any command via Poetry
poetry run translate --help
```

### Seçenek B: pip/venv

```bash
# Create & activate virtual environment
python -m venv .venv
# Windows
.venv\\Scripts\\activate
# Linux/macOS
# source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# (Optional) Editable install for local development
pip install -e .
```

## Son Kullanıcı Kullanımı

### Docker (yayınlanmış imaj)

```bash
# Pull public image from GHCR
docker pull ghcr.io/azure/co-op-translator:latest

# Run with current folder mounted and .env provided (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "fr es" -md

# PowerShell
docker run --rm -it --env-file .env -v ${PWD}:/work ghcr.io/azure/co-op-translator:latest -l "fr es" -md
```

Notlar:
- Varsayılan giriş noktası `translate`'dir. Bağlantı taşıma için `--entrypoint migrate-links` ile geçersiz kılabilirsiniz.
- Anonim çekmeler için GHCR paket görünürlüğünün Public olduğundan emin olun.

### CLI (pip)

```bash
pip install co-op-translator
translate -l "fr es" -md
```

### Ortam yapılandırması

Depo kökünde bir `.env` dosyası oluşturun ve seçtiğiniz dil modeli ve (isteğe bağlı) görsel servisi için kimlik bilgilerini/endpoint'leri girin. Sağlayıcıya özel kurulum için `getting_started/set-up-azure-ai.md` dosyasına bakın.

### Gerekli Ortam Değişkenleri

En az bir LLM sağlayıcısı yapılandırılmalıdır. Görsel çeviri için ayrıca Azure AI Service yapılandırılmalıdır.

- Azure OpenAI (metin çevirisi):
  - `AZURE_OPENAI_API_KEY`
  - `AZURE_OPENAI_ENDPOINT`
  - `AZURE_OPENAI_MODEL_NAME`
  - `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME`
  - `AZURE_OPENAI_API_VERSION`

- OpenAI (alternatif metin çevirisi):
  - `OPENAI_API_KEY`
  - `OPENAI_ORG_ID` (isteğe bağlı)
  - `OPENAI_CHAT_MODEL_ID` (OpenAI sağlayıcısı kullanılırken zorunlu)
  - `OPENAI_BASE_URL` (isteğe bağlı; varsayılan `https://api.openai.com/v1`)

- Görsel metin çıkarımı için Azure AI Service (`-img` kullanılırken zorunlu):
  - `AZURE_AI_SERVICE_API_KEY` (tercih edilir) veya eski `AZURE_SUBSCRIPTION_KEY`
  - `AZURE_AI_SERVICE_ENDPOINT`

Örnek `.env` parçası:

```bash
# Azure AI Service (for image translation)
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<your-ai-service>.cognitiveservices.azure.com/"

# Azure OpenAI (primary option)
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<your-azure-openai>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<your-deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"

# OpenAI (alternative option)
OPENAI_API_KEY="..."
OPENAI_ORG_ID="..."            # optional
OPENAI_CHAT_MODEL_ID="gpt-4o"   # required when using OpenAI
OPENAI_BASE_URL="https://api.openai.com/v1" # optional
```

Notlar:

- Araç, mevcut LLM sağlayıcısını otomatik olarak algılar; Azure OpenAI veya OpenAI'dan birini yapılandırın.
- Görsel çeviri için hem `AZURE_AI_SERVICE_API_KEY` hem de `AZURE_AI_SERVICE_ENDPOINT` gereklidir.
- Gerekli değişkenler eksikse CLI açık bir hata verir.

## Geliştirme Akışı

- Kaynak kodu `src/co_op_translator` altında, testler ise `tests/` altında bulunur.
- Ana CLI'ler (giriş noktaları ile kurulur):

```bash
# Translate content to one or more languages (space‑separated codes)
translate -l "fr es de"

# Restrict by content type
translate -l "ja" -md            # only Markdown
translate -l "ko" -nb            # only notebooks
translate -l "zh" -md -img       # Markdown + images

# Update links in previously translated notebooks/Markdown
migrate-links -l "all" -y
```

Ek kullanım belgeleri için `getting_started/` klasörüne bakın.

## Test Talimatları

Testleri depo kökünden çalıştırın. Bazı testler API kimlik bilgileri gerektirebilir; gerekirse bu testleri atlayın.

```bash
# Run full test suite
pytest

# Skip tests that require live API keys
pytest -m "not api_key_required"

# Run a subset
pytest tests/co_op_translator -k "name_substring"
```

İsteğe bağlı kapsam (coverage gerektirir):

```bash
coverage run -m pytest -m "not api_key_required"
coverage html  # outputs to ./htmlcov
```

## Kod Stili Kuralları

- Biçimlendirici: Black (`pyproject.toml`'da yapılandırılmış, satır uzunluğu 88)
- Linter: Ruff (`pyproject.toml`'da yapılandırılmış, satır uzunluğu 120)
- Tip kontrolü: mypy (yapılandırma mevcut; kuruluysa etkinleştirin)

Komutlar:

```bash
# Via Poetry
poetry run black .
poetry run ruff check .
poetry run ruff check . --fix   # safe auto‑fixes

# Or with global tools
black .
ruff check .
```

Python kaynaklarını `src/` altında, testleri `tests/` altında tutun ve paket ad alanı içinde açık ithalatları (`co_op_translator.*`) tercih edin.

## Derleme ve Dağıtım

Derleme çıktıları `dist/` klasörüne yayınlanır.

```bash
# Build (Poetry)
poetry build

# Local install of the built wheel
pip install dist/*.whl
```

GitHub Actions ile otomasyon desteklenir; bakınız:

- `getting_started/github-actions-guide/github-actions-guide-public.md`
- `getting_started/github-actions-guide/github-actions-guide-org.md`

### Konteyner İmajı (GHCR)

- Resmi imaj: `ghcr.io/azure/co-op-translator:<tag>`
- Etiketler: `latest` (main'de), semantik etiketler `vX.Y.Z` gibi ve bir `sha` etiketi
- Çoklu mimari: Buildx ile `linux/amd64, linux/arm64` desteklenir
- Dockerfile deseni: bağımlılık tekerleklerini builder'da oluşturun (`build-essential` ve `python3-dev` ile) ve çalışma zamanında yerel wheelhouse'dan kurun (`pip install --no-index --find-links=/wheels`)
- İş akışı: `.github/workflows/docker-publish.yml` GHCR'ye oluşturur ve gönderir

## Güvenlik Hususları

- API anahtarlarını ve endpoint'leri `.env` dosyasında veya CI gizli anahtar deposunda tutun; asla gizli bilgileri commit etmeyin.
- Görsel çeviri için Azure AI Vision anahtarları/endpoint'leri gereklidir; aksi halde `-img` kullanmayın.
- Büyük çeviri işlemlerinde sağlayıcı kota/sınırlamalarını doğrulayın.

## Pull Request Kuralları

### Göndermeden Önce

1. **Değişikliklerinizi test edin:**
   - Etkilenen defterleri tamamen çalıştırın
   - Tüm hücrelerin hatasız çalıştığını doğrulayın
   - Çıktıların uygunluğunu kontrol edin

2. **Dokümantasyon güncellemeleri:**
   - Yeni kavramlar ekliyorsanız `README.md` dosyasını güncelleyin
   - Karmaşık kodlar için defterlerde yorum ekleyin
   - Markdown hücrelerinde amacını açıklayın

3. **Dosya değişiklikleri:**
   - `.env` dosyalarını commit etmeyin (`.env.example` kullanın)
   - `venv/` veya `__pycache__/` dizinlerini commit etmeyin
   - Kavramları gösteren defter çıktıları kalabilir
   - Geçici dosyaları ve yedek defterleri (`*-backup.ipynb`) kaldırın

4. **Stil ve biçimlendirme:**
   - Stil ve biçimlendirme kurallarına uyun
   - Stil ve biçimlendirme sorunları için `poetry run black .` ve `poetry run ruff check .` komutlarını çalıştırın

5. **Test ve CLI yardımını ekleyin/güncelleyin:**
   - Davranış değiştiriyorsanız test ekleyin veya güncelleyin
   - CLI yardımını yapılan değişikliklerle tutarlı tutun


### Commit mesajı ve birleştirme stratejisi

Varsayılan olarak Squash and Merge kullanıyoruz. Son squash commit mesajı şu şekilde olmalı:

```bash
<type>: <description> (#<PR number>)
```

İzin verilen türler:
- `Docs` — dokümantasyon güncellemeleri
- `Build` — derleme sistemi, bağımlılıklar, yapılandırma/CI
- `Core` — temel işlevsellik ve özellikler (örn. `src/co_op_translator/core`)

Örnekler:
- `Docs: Kurulum talimatlarını netleştir (#50)`
- `Core: Görsel çevirisinde iyileştirme (#60)`

Notlar:
- PR başlıkları genellikle etiketlere göre otomatik öneklenir; oluşturulan önekin doğru olduğundan emin olun.

### PR Başlık Formatı

Açık ve öz başlıklar kullanın. Son squash commit ile aynı yapıyı tercih edin:
- `Docs: Kurulum talimatlarını netleştir`
- `Core: Görsel çevirisinde iyileştirme`

## Hata Ayıklama ve Sorun Giderme

- Sık karşılaşılan sorunlar ve çözümler: `getting_started/troubleshooting.md`
- Desteklenen diller ve notlar (fontlar/bilinen sorunlar dahil): `getting_started/supported-languages.md`
- Defterlerde bağlantı sorunları için tekrar çalıştırın: `migrate-links -l "all" -y`

## Ajanlar için Notlar

- Tekrar üretilebilir ortamlar için Poetry'yi tercih edin; aksi halde `requirements.txt` kullanın.
- CI'da CLI'leri çağırırken gerekli gizli anahtarları ortam değişkenleri veya `.env` ile sağlayın.
- Monorepo kullanıcıları için bu depo bağımsız bir paket olarak çalışır; alt paket koordinasyonu gerekmez.

- Çoklu mimari için: ARM kullanıcıları (Apple Silicon/ARM sunucuları) hedefleniyorsa `linux/arm64`'ı koruyun; aksi halde sadelik için sadece `linux/amd64` yeterlidir.
- Konteyner kullanmak isteyenlere `README.md`'deki Docker Hızlı Başlangıç bölümünü gösterin; alıntı farkları nedeniyle Bash ve PowerShell varyantlarını ekleyin.

---

**Feragatname**:
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerde hata veya yanlışlıklar olabileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından doğabilecek herhangi bir yanlış anlama veya yanlış yorumdan sorumlu değiliz.