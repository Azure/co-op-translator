<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "87bf95d45e684475ef1e67d8dae5f6eb",
  "translation_date": "2025-05-06T18:12:20+00:00",
  "source_file": "getting_started/github-actions-guide/github-actions-guide-public.md",
  "language_code": "tr"
}
-->
# Co-op Translator GitHub Action Kullanımı (Herkese Açık Kurulum)

**Hedef Kitle:** Bu rehber, standart GitHub Actions izinlerinin yeterli olduğu çoğu herkese açık veya özel depo kullanıcıları için hazırlanmıştır. Yerleşik `GITHUB_TOKEN` kullanılır.

Depo dokümantasyonunuzun çevirisini Co-op Translator GitHub Action ile zahmetsizce otomatikleştirin. Bu rehber, kaynak Markdown dosyalarınız veya resimleriniz değiştiğinde güncellenmiş çevirilerle otomatik olarak pull request oluşturan aksiyonu kurmanızı adım adım anlatır.

> [!IMPORTANT]
>
> **Doğru Rehberi Seçmek:**
>
> Bu rehber, **standart `GITHUB_TOKEN` kullanarak daha basit kurulumu** detaylandırır. Çoğu kullanıcı için önerilen yöntemdir çünkü hassas GitHub App Özel Anahtarlarını yönetmeyi gerektirmez.
>

## Ön Koşullar

GitHub Action’ı yapılandırmadan önce gerekli AI servis kimlik bilgilerine sahip olduğunuzdan emin olun.

**1. Gerekli: AI Dil Modeli Kimlik Bilgileri**  
Desteklenen en az bir Dil Modeli için kimlik bilgilerine ihtiyacınız var:

- **Azure OpenAI**: Endpoint, API Anahtarı, Model/Kurulum İsimleri, API Sürümü gerektirir.
- **OpenAI**: API Anahtarı, (İsteğe bağlı: Org ID, Temel URL, Model ID).
- Ayrıntılar için [Supported Models and Services](../../../../README.md) sayfasına bakın.  
- Kurulum Rehberi: [Azure OpenAI Kurulumu](../set-up-resources/set-up-azure-openai.md).

**2. İsteğe Bağlı: Bilgisayarlı Görü Kimlik Bilgileri (Görüntü Çevirisi için)**

- Yalnızca resimlerdeki metni çevirmek istiyorsanız gereklidir.
- **Azure Computer Vision**: Endpoint ve Abonelik Anahtarı gerektirir.
- Sağlanmazsa aksiyon varsayılan olarak [Markdown-only modu](../markdown-only-mode.md) kullanır.
- Kurulum Rehberi: [Azure Computer Vision Kurulumu](../set-up-resources/set-up-azure-computer-vision.md).

## Kurulum ve Yapılandırma

Depo içinde standart `GITHUB_TOKEN` kullanarak Co-op Translator GitHub Action’ı yapılandırmak için aşağıdaki adımları izleyin.

### Adım 1: Kimlik Doğrulamayı Anlayın (Standart `GITHUB_TOKEN` Kullanımı)

Bu iş akışı, GitHub Actions tarafından sağlanan yerleşik `GITHUB_TOKEN`’u kullanır. Bu token, **Adım 3**’te yapılandırılan ayarlara bağlı olarak iş akışının deponuzla etkileşim kurmasına otomatik olarak izin verir.

### Adım 2: Depo Gizli Değişkenlerini Yapılandırın

Sadece **AI servis kimlik bilgilerinizi** depo ayarlarında şifreli gizli değişkenler olarak eklemeniz yeterlidir.

1.  Hedef GitHub deponuza gidin.
2.  **Settings** > **Secrets and variables** > **Actions** menüsüne tıklayın.
3.  **Repository secrets** altında, aşağıdaki gerekli AI servis gizli değişkenlerinin her biri için **New repository secret** butonuna tıklayın.

    ![Select setting action](../../../../getting_started/github-actions-guide/imgs/select-setting-action.png) *(Görsel Referans: Gizli değişkenlerin nereden ekleneceğini gösterir)*

**Gerekli AI Servis Gizli Değişkenleri (Ön Koşullarınıza göre UYGULANAN TÜMÜNÜ ekleyin):**

| Gizli Değişken Adı                 | Açıklama                               | Değer Kaynağı                   |
| :-------------------------------- | :------------------------------------ | :------------------------------ |
| `AZURE_SUBSCRIPTION_KEY`            | Azure AI Servisi (Bilgisayarlı Görü) Anahtarı  | Azure AI Foundry’niz             |
| `AZURE_AI_SERVICE_ENDPOINT`         | Azure AI Servisi (Bilgisayarlı Görü) Endpoint  | Azure AI Foundry’niz             |
| `AZURE_OPENAI_API_KEY`              | Azure OpenAI servisi Anahtarı              | Azure AI Foundry’niz             |
| `AZURE_OPENAI_ENDPOINT`             | Azure OpenAI servisi Endpoint               | Azure AI Foundry’niz             |
| `AZURE_OPENAI_MODEL_NAME`           | Azure OpenAI Model Adınız                   | Azure AI Foundry’niz             |
| `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` | Azure OpenAI Kurulum Adınız                   | Azure AI Foundry’niz             |
| `AZURE_OPENAI_API_VERSION`          | Azure OpenAI API Sürümü                      | Azure AI Foundry’niz             |
| `OPENAI_API_KEY`                    | OpenAI API Anahtarı                         | OpenAI Platformunuz              |
| `OPENAI_ORG_ID`                     | OpenAI Organizasyon ID (İsteğe bağlı)       | OpenAI Platformunuz              |
| `OPENAI_CHAT_MODEL_ID`              | Belirli OpenAI model ID (İsteğe bağlı)       | OpenAI Platformunuz              |
| `OPENAI_BASE_URL`                   | Özel OpenAI API Temel URL (İsteğe bağlı)     | OpenAI Platformunuz              |

### Adım 3: İş Akışı İzinlerini Yapılandırın

GitHub Action, kodu çekmek ve pull request oluşturmak için `GITHUB_TOKEN` üzerinden izinlere ihtiyaç duyar.

1.  Deponuzda **Settings** > **Actions** > **General** bölümüne gidin.
2.  **Workflow permissions** kısmına ilerleyin.
3.  **Read and write permissions** seçeneğini işaretleyin. Bu, `GITHUB_TOKEN`’a bu iş akışı için gerekli `contents: write` ve `pull-requests: write` izinlerini verir.
4.  **Allow GitHub Actions to create and approve pull requests** seçeneğinin işaretli olduğundan emin olun.
5.  **Save** butonuna tıklayın.

![Permission setting](../../../../getting_started/github-actions-guide/imgs/permission-setting.png)

### Adım 4: İş Akışı Dosyasını Oluşturun

Son olarak, otomatik iş akışını tanımlayan YAML dosyasını `GITHUB_TOKEN` kullanarak oluşturun.

1.  Depo kök dizininde, `.github/workflows/` dizini yoksa oluşturun.
2.  `.github/workflows/` içinde `co-op-translator.yml` adlı bir dosya oluşturun.
3.  Aşağıdaki içeriği `co-op-translator.yml` dosyasına yapıştırın.

```yaml
name: Co-op Translator

on:
  push:
    branches:
      - main

jobs:
  co-op-translator:
    runs-on: ubuntu-latest

    permissions:
      contents: write
      pull-requests: write

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      - name: Install Co-op Translator
        run: |
          python -m pip install --upgrade pip
          pip install co-op-translator

      - name: Run Co-op Translator
        env:
          PYTHONIOENCODING: utf-8
          # === AI Service Credentials ===
          AZURE_SUBSCRIPTION_KEY: ${{ secrets.AZURE_SUBSCRIPTION_KEY }}
          AZURE_AI_SERVICE_ENDPOINT: ${{ secrets.AZURE_AI_SERVICE_ENDPOINT }}
          AZURE_OPENAI_API_KEY: ${{ secrets.AZURE_OPENAI_API_KEY }}
          AZURE_OPENAI_ENDPOINT: ${{ secrets.AZURE_OPENAI_ENDPOINT }}
          AZURE_OPENAI_MODEL_NAME: ${{ secrets.AZURE_OPENAI_MODEL_NAME }}
          AZURE_OPENAI_CHAT_DEPLOYMENT_NAME: ${{ secrets.AZURE_OPENAI_CHAT_DEPLOYMENT_NAME }}
          AZURE_OPENAI_API_VERSION: ${{ secrets.AZURE_OPENAI_API_VERSION }}
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
          OPENAI_ORG_ID: ${{ secrets.OPENAI_ORG_ID }}
          OPENAI_CHAT_MODEL_ID: ${{ secrets.OPENAI_CHAT_MODEL_ID }}
          OPENAI_BASE_URL: ${{ secrets.OPENAI_BASE_URL }}
        run: |
          # =====================================================================
          # IMPORTANT: Set your target languages here (REQUIRED CONFIGURATION)
          # =====================================================================
          # Example: Translate to Spanish, French, German. Add -y to auto-confirm.
          translate -l "es fr de" -y  # <--- MODIFY THIS LINE with your desired languages

      - name: Create Pull Request with translations
        uses: peter-evans/create-pull-request@v5
        with:
          token: ${{ secrets.GITHUB_TOKEN }}
          commit-message: "🌐 Update translations via Co-op Translator"
          title: "🌐 Update translations via Co-op Translator"
          body: |
            This PR updates translations for recent changes to the main branch.

            ### 📋 Changes included
            - Translated contents are available in the `translations/` directory
            - Translated images are available in the `translated_images/` directory

            ---
            🌐 Automatically generated by the [Co-op Translator](https://github.com/Azure/co-op-translator) GitHub Action.
          branch: update-translations
          base: main
          labels: translation, automated-pr
          delete-branch: true
          add-paths: |
            translations/
            translated_images/
```
4.  **İş Akışını Özelleştirin:**  
  - **[!IMPORTANT] Hedef Diller:** Gerekirse `Run Co-op Translator` step, you **MUST review and modify the list of language codes** within the `translate -l "..." -y` command to match your project's requirements. The example list (`ar de es...`) needs to be replaced or adjusted.
  - **Trigger (`on:`):** The current trigger runs on every push to `main`. For large repositories, consider adding a `paths:` filter (see commented example in the YAML) to run the workflow only when relevant files (e.g., source documentation) change, saving runner minutes.
  - **PR Details:** Customize the `commit-message`, `title`, `body`, `branch` name, and `labels` in the `Create Pull Request` adımında hedef dilleri değiştirin.

**Feragatname**:  
Bu belge, [Co-op Translator](https://github.com/Azure/co-op-translator) adlı yapay zeka çeviri hizmeti kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilindeki haliyle yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalar veya yorumlamalardan dolayı sorumluluk kabul edilmemektedir.