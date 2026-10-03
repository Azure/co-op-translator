# GitHub Actions

Depodaki değişen belgelerin otomatik olarak çevrilmesini ve oluşturulan çıktılarla bir pull request açılmasını istiyorsanız GitHub Actions kullanın.

Önce standart `GITHUB_TOKEN` yapılandırmasıyla başlayın; politika izin verdiği organizasyon depoları için de bunu yapın. Organizasyonunuz bir Uygulama kimliği gerektiriyorsa veya otomatik alt iş akışı çalıştırmaları gerekiyorsa [GitHub Uygulaması Kurulumu](#github-app-setup)'a bakın.

**İnsan düzenlemeleri:** bu iş akışları değişen kaynak dosyaları tamamen yeniden çevirir ve çevirilerde yapılan sözcük değişikliklerini üzerine yazabilir. Birleştirmeden önce her PR'ı gözden geçirin. Kabul edilen düzenlemelerin Markdown blok-düzeyinde korunması, [Python API çeviri durum sağlayıcısı](api.md#preserve-accepted-human-edits-with-a-translation-state-provider) ile özel bir entegrasyon gerektirir.

## İlk README çeviri PR'iniz

Bir kök `README.md` ve bir hedef dil ile başlayın. Bu iş akışı yalnızca Markdown çevirir, bu yüzden Azure AI Vision gerekmez.

1. [translate-readme.yml](../../assets/workflows/translate-readme.yml) dosyasını ([şablonu GitHub'da görüntüleyin](https://github.com/Azure/co-op-translator/blob/main/docs/assets/workflows/translate-readme.yml)) çeviri yapmak istediğiniz depoda `.github/workflows/translate-readme.yml` konumuna kopyalayın ve bu deponun varsayılan dalına commit edin. Şablon, aynı kaynak referansından CLI'yi kuran `Azure/co-op-translator@main` kök Action'ını kullanır. Yeniden üretilebilir çalıştırmalar için gözden geçirilmiş bir commit'e sabitleyin.
2. **Actions > Translate README > Run workflow** öğesini açın, bir dil seçin ve **Sadece Önizleme** işaretli kalsın. Önizleme adımındaki token tahminini gözden geçirin. Önizleme model sağlayıcıları çağırmaz, çevirileri yazmaz veya PR oluşturmaz.
3. Bir [metin sağlayıcısı](#prerequisites) için gizli anahtarları ekleyin ve **Settings > Actions > General** altında **GitHub Actions'ın pull request oluşturmasına ve onaylamasına izin ver** seçeneğini etkinleştirin. Şablon, işi için `contents: write` ve `pull-requests: write` izinlerini ister; her iş akışı için varsayılan izinleri değiştirmenize gerek yoktur. Organizasyon politikası bu izinleri veya bu ayarı engelliyorsa, onaylı bir [GitHub Uygulaması](#github-app-setup) hakkında bir yöneticiye danışın.
4. **Sadece Önizleme** işaretini kaldırarak iş akışını tekrar çalıştırın. İş akışı önizleme yapar, çevirir, `co-op-review --readme-only` komutunu çalıştırır ve çeviri ile inceleme başarılı olduktan sonra bir çeviri PR'si oluşturur veya günceller. İş akışı özetinde PR'ye bağlantı bulunur.
5. PR içindeki metin ve dosya değişikliklerini inceleyin, ardından hazır olduğunuzda birleştirin. İş akışı otomatik olarak birleştirme yapmaz.

PR yalnızca `translations/<language>/README.md` ve onun dil meta veri dosyasını içerir. Kaynak README değişmeden kalır ve diğer belgelere verilen bağlantılar kaynak belgeleri işaret etmeye devam eder. PR gövdesi değişen dosyaları ve yapısal inceleme sonuçlarını listeler. Eğer çeviri veya inceleme başarısız olursa, iş akışı özetini ve başarısız adım günlüklerini inceleyin; PR oluşturulmaz. Değişiklik yoksa yeni bir PR gerekli değildir.

**Organizasyon ve CI notu:** Bir GitHub Uygulaması isteğe bağlıdır, organizasyon sahipliği için bir gereklilik değildir. `GITHUB_TOKEN` ile bir PR açma, güncelleme veya yeniden açma iş akışları için, iş akışlarının çalıştırılmasına onay vermesi için yazma erişimine sahip bir kullanıcı gerekir. Push iş akışları bu token ile tetiklenmez. Gözetimsiz alt CI için, [GitHub Uygulaması Kurulumu](#github-app-setup) ve GitHub'ın [workflow triggering rules](https://docs.github.com/en/actions/how-tos/writing-workflows/choosing-when-your-workflow-runs/triggering-a-workflow) sayfasına bakın.

## Önkoşullar

İş akışını oluşturmadan önce çeviri çalıştırmanızın ihtiyaç duyduğu AI servis gizli anahtarlarını yapılandırın.

Metin çevirisi için bir dil modeli sağlayıcısı gerekir:

- Azure OpenAI: `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_MODEL_NAME`, `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME`, `AZURE_OPENAI_API_VERSION`
- OpenAI: `OPENAI_API_KEY`, `OPENAI_CHAT_MODEL_ID`, plus optional `OPENAI_ORG_ID` and `OPENAI_BASE_URL`
- Anthropic: `ANTHROPIC_API_KEY`, `ANTHROPIC_MODEL`, plus optional `ANTHROPIC_BASE_URL`

Görüntü çevirisi ek olarak Azure AI Vision gerektirir:

- `AZURE_AI_SERVICE_API_KEY`
- `AZURE_AI_SERVICE_ENDPOINT`

Yerel yapılandırma ayrıntıları için [Yapılandırma](configuration.md) ve [Azure AI Kurulumu](azure-ai-setup.md) sayfalarına bakın.

## Standart Kurulum

README iş akışını denedikten sonra, bu yapılandırmayı kullanarak bir deponun Markdown dosyalarını birden çok dile çevirin. PR açmadan önce bir Markdown incelemesi çalıştırır ve Azure AI Vision gerektirmez.

### Adım 1: Depo Gizli Anahtarlarını Ekle

Hedef deponuzda **Settings** > **Secrets and variables** > **Actions** öğesini açın, ardından iş akışınızın kullanacağı sağlayıcı gizli anahtarlarını ekleyin.

![Eylemler gizli anahtarlarını seçin](../../assets/github-actions/select-setting-action.png)

### Adım 2: İş Akışı İzinlerini Etkinleştirin

**Settings** > **Actions** > **General** öğesini açın.

**İş Akışı izinleri** altında:

1. **GitHub Actions'ın pull request oluşturmasına ve onaylamasına izin ver** seçeneğini etkinleştirin.
2. Ayarı kaydedin.

Aşağıdaki iş açıkça `contents: write` ve `pull-requests: write` ister. Depo varsayılan iş akışı izinlerini değiştirmeyin. Organizasyon politikası PR oluşturmayı engelliyorsa, onaylı bir [GitHub Uygulaması](#github-app-setup) hakkında bir yöneticiden bilgi alın.

### Adım 3: İş Akışını Ekle

`.github/workflows/co-op-translator.yml` dosyasını oluşturun:

```yaml
name: Co-op Translator

on:
  push:
    branches:
      - main

jobs:
  co-op-translator:
    runs-on: ubuntu-latest
    env:
      TARGET_LANGUAGES: "es fr de"

    permissions:
      contents: write
      pull-requests: write

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Set up Python
        uses: actions/setup-python@v7
        with:
          python-version: "3.11"

      - name: Install Co-op Translator
        run: |
          python -m pip install --upgrade pip
          pip install co-op-translator

      - name: Run Co-op Translator
        env:
          PYTHONIOENCODING: utf-8
          AZURE_OPENAI_API_KEY: ${{ secrets.AZURE_OPENAI_API_KEY }}
          AZURE_OPENAI_ENDPOINT: ${{ secrets.AZURE_OPENAI_ENDPOINT }}
          AZURE_OPENAI_MODEL_NAME: ${{ secrets.AZURE_OPENAI_MODEL_NAME }}
          AZURE_OPENAI_CHAT_DEPLOYMENT_NAME: ${{ secrets.AZURE_OPENAI_CHAT_DEPLOYMENT_NAME }}
          AZURE_OPENAI_API_VERSION: ${{ secrets.AZURE_OPENAI_API_VERSION }}
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
          OPENAI_ORG_ID: ${{ secrets.OPENAI_ORG_ID }}
          OPENAI_CHAT_MODEL_ID: ${{ secrets.OPENAI_CHAT_MODEL_ID }}
          OPENAI_BASE_URL: ${{ secrets.OPENAI_BASE_URL }}
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
          ANTHROPIC_MODEL: ${{ secrets.ANTHROPIC_MODEL }}
          ANTHROPIC_BASE_URL: ${{ secrets.ANTHROPIC_BASE_URL }}
        run: |
          translate -l "$TARGET_LANGUAGES" -md -y

      - name: Review Markdown translations
        run: |
          python - <<'PY'
          import os
          from co_op_translator.api import run_review

          run_review(
              language_codes=os.environ["TARGET_LANGUAGES"].split(),
              markdown=True,
              notebook=False,
              output_format="github",
          )
          PY

      - name: Create Pull Request with translations
        uses: peter-evans/create-pull-request@v5
        with:
          token: ${{ secrets.GITHUB_TOKEN }}
          commit-message: "Update translations via Co-op Translator"
          title: "Update translations via Co-op Translator"
          body: |
            This PR updates translations for recent changes to the main branch.
            Markdown structure, freshness, and local links were reviewed.
            Review translation wording before merging.

            Generated by Co-op Translator.
          branch: update-translations
          base: main
          labels: translation, automated-pr
          delete-branch: true
          add-paths: |
            translations/
```

`TARGET_LANGUAGES` değerini projenizin ihtiyaç duyduğu dillere göre değiştirin. İnceleme, çeviri adımıyla eşleşecek şekilde yalnızca Markdown'u kontrol etmek için Python API'sini kullanır. Bir çeviri veya inceleme hatası, PR oluşturulmadan önce işi durdurur. İş akışı PR'yi otomatik olarak birleştirmez. Büyük depolar için, iş akışının yalnızca dokümantasyon değiştiğinde çalışması için `on.push` altına bir `paths:` filtresi ekleyin.

### İsteğe Bağlı: notebook'lar ve resimler

Notebook'lar için, çeviri komutuna `-nb` ekleyin ve inceleme adımında `notebook=True` olarak ayarlayın. Görüntü metni için iki [Azure AI Vision gizli anahtarını](#prerequisites) yapılandırın, bunları çeviri adımının `env`'ine iletin, komuta `-img` ekleyin ve PR adımının `add-paths`'ine `translated_images/` öğesini ekleyin. Çevrilen görselleri görsel olarak gözden geçirin; deterministik inceleme görüntü metnini veya dilsel doğruluğu onaylamaz.

## GitHub Uygulaması Kurulumu

Organizasyonunuz bir Uygulama kimliği gerektirdiğinde veya oluşturulan PR'nin `GITHUB_TOKEN` onay adımı olmadan alt CI'yi tetiklemesi gerektiğinde onaylı bir GitHub Uygulaması kullanın. Bir Uygulama organizasyon politikasını aşmaz; yöneticiler yine de kurulumunu ve izinlerini kontrol eder.

### Adım 1: Bir GitHub Uygulaması Oluşturun veya Yükleyin

Mevcutsa organizasyon tarafından sağlanan bir Uygulamayı kullanın veya **Contents** ve **Pull requests** için okuma/yazma erişimine sahip bir tane oluşturun. Gerekli organizasyon onayı ile hedef depoya kurun.

Kaydedin:

- Uygulama Kimliği
- Özel anahtar içeriği

Bunları depo gizli anahtarları olarak saklayın:

- `GH_APP_ID`
- `GH_APP_PRIVATE_KEY`

### Adım 2: Bir Uygulama Jetonu Oluşturun

Bu adımı mevcut pull request adımından hemen önce ekleyin. README şablonu için, önizlemeler ve başarısız çeviriler bir Uygulama jetonu talep etmesin diye aynı başarı koşulunu kullanın:

```yaml
      - name: Authenticate GitHub App
        id: generate_token
        if: ${{ !inputs.preview && steps.translate.outcome == 'success' && steps.review.outcome == 'success' }}
        uses: actions/create-github-app-token@v2
        with:
          app-id: ${{ secrets.GH_APP_ID }}
          private-key: ${{ secrets.GH_APP_PRIVATE_KEY }}
          permission-contents: write
          permission-pull-requests: write
```

Ardından yalnızca mevcut pull request adımının `token` girdisini `${{ steps.generate_token.outputs.token }}` olarak değiştirin. Başarı koşulunu, dalı, PR gövdesini ve `add-paths`'i değiştirmeyin. Jeton varsayılan olarak geçerli depo ile sınırlandırılır. Standart kurulumu README şablonu yerine uyarlarken yukarıdaki `if`'i atlayın: o iş akışı varsayılan başarı koşulunu kullandığından, jeton oluşturma ve PR oluşturma yalnızca çeviri ve inceleme başarılı olduktan sonra çalışır.

Kurulum ve jeton izinleri için resmi [create-github-app-token Action'ına](https://github.com/actions/create-github-app-token/tree/v2) bakın.

## Runner Sınırları

GitHub tarafından barındırılan runner'ların bir maksimum iş süresi vardır. Büyük depolar veya çok sayıda hedef dil bu sınırı aşabilir.

Büyük çeviri iş yükleri için:

- Her çalıştırmada daha az dil çevirin.
- `-md`, `-nb` veya `-img` gibi içerik bayrakları kullanın.
- Depo boyutu veya model gecikmesi barındırılan runner'ları güvenilmez hale getiriyorsa kendi barındırdığınız bir runner kullanın.

## CI'de İnceleme

LLM veya Vision sağlayıcılarını çağırmadan oluşturulmuş çevirilerin doğrulanması gereken bir pull request için `co-op-review` kullanın.

```yaml
      - name: Review translated outputs
        run: |
          co-op-review --changed-from "origin/${{ github.base_ref }}" --format github
```

`co-op-review` beta aşamasında deterministik bir inceleme komutudur. Kontrolleri ve çıktı şeması değişebilir, ancak dosya yazmadığı ve model sağlayıcılarını çağırmadığı için CI için güvenli olması amaçlanmıştır.