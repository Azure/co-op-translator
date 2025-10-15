<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6e626bef5ed78a1cc55b0dbf44f01d47",
  "translation_date": "2025-10-15T03:10:52+00:00",
  "source_file": "getting_started/troubleshooting.md",
  "language_code": "tr"
}
-->
# Microsoft Co-op Translator Sorun Giderme Rehberi

## Genel Bakış
Microsoft Co-Op Translator, Markdown belgelerini sorunsuz bir şekilde çevirmek için güçlü bir araçtır. Bu rehber, aracı kullanırken karşılaşabileceğiniz yaygın sorunları nasıl çözebileceğinizi anlatır.

## Yaygın Sorunlar ve Çözümleri

### 1. Markdown Etiketi Sorunu
**Sorun:** Çevrilen Markdown belgesinin en üstünde bir `markdown` etiketi var ve bu, dosyanın doğru görüntülenmemesine neden oluyor.

**Çözüm:** Bunu düzeltmek için dosyanın en üstündeki `markdown` etiketini silmeniz yeterli. Böylece Markdown dosyası düzgün şekilde görüntülenecektir.

**Adımlar:**
1. Çevrilen Markdown (`.md`) dosyasını açın.
2. Belgenin en üstündeki `markdown` etiketini bulun.
3. `markdown` etiketini silin.
4. Dosyayı kaydedin.
5. Dosyayı tekrar açarak düzgün görüntülendiğinden emin olun.

### 2. Gömülü Görsellerin URL Sorunu
**Sorun:** Gömülü görsellerin URL’leri dil yerel ayarıyla eşleşmiyor, bu da yanlış veya eksik görsellere yol açıyor.

**Çözüm:** Gömülü görsellerin URL’lerini kontrol edin ve dil yerel ayarıyla uyumlu olduğundan emin olun. Tüm görseller `translated_images` klasöründe bulunur ve her görselin dosya adında bir dil etiketi vardır.

**Adımlar:**
1. Çevrilen Markdown belgesini açın.
2. Gömülü görselleri ve URL’lerini tespit edin.
3. Görsel dosya adındaki dil etiketinin belgenin diliyle eşleştiğini doğrulayın.
4. Gerekirse URL’leri güncelleyin.
5. Değişiklikleri kaydedin ve görsellerin doğru şekilde görüntülendiğini kontrol edin.

### 3. Çeviri Doğruluğu
**Sorun:** Çevrilen içerik yeterince doğru değil veya düzenleme gerektiriyor.

**Çözüm:** Çevrilen belgeyi gözden geçirin ve doğruluğu ile okunabilirliğini artırmak için gerekli düzenlemeleri yapın.

**Adımlar:**
1. Çevrilen belgeyi açın.
2. İçeriği dikkatlice inceleyin.
3. Çeviri doğruluğunu artırmak için gerekli düzenlemeleri yapın.
4. Dosyayı kaydedin.

## 4. İzin Hatası Redakte Edildi veya 404

Görseller veya metin doğru dile çevrilmiyorsa ve -d debug modunda çalıştırırken 401 hatası alıyorsanız, bu klasik bir kimlik doğrulama hatasıdır—anahtar geçersiz, süresi dolmuş veya endpoint’in bölgesiyle eşleşmiyor olabilir.

Sorunun kök nedenini anlamak için co-op translator’ı [-d debug anahtarıyla](https://github.com/Azure/co-op-translator/blob/main/getting_started/command-reference.md) çalıştırın.

- **Hata Mesajı**: `Access denied due to invalid subscription key or wrong API endpoint.`
- **Olası Nedenler**:
  - Abonelik anahtarı istekte redakte edilmiş veya yanlış.
  - AI Services Key veya Subscription Key, **Azure AI Vision** kaynağı yerine başka bir Azure kaynağına (ör. Translator veya OpenAI) ait olabilir.

 **Kaynak Türü**
  - [Azure Portal](https://portal.azure.com) veya [Azure AI Foundry](https://ai.azure.com) üzerinden kaynağın `Azure AI services` → `Vision` türünde olduğundan emin olun.
  - Anahtarları doğrulayın ve doğru anahtarı kullandığınızdan emin olun.

## 5. Yapılandırma Hataları (Yeni Hata Yönetimi)

Yeni seçmeli çeviri sistemiyle birlikte, Co-op Translator artık gerekli hizmetler yapılandırılmadığında açık hata mesajları verir.

### 5.1. Görsel Çeviri için Azure AI Hizmeti Yapılandırılmamış

**Sorun:** Görsel çevirisi (`-img` bayrağı) istediniz fakat Azure AI Hizmeti düzgün yapılandırılmamış.

**Hata Mesajı:**
```
Error: Image translation requested but Azure AI Service is not configured.
Please add AZURE_AI_SERVICE_API_KEY and AZURE_AI_SERVICE_ENDPOINT to your .env file.
Check Azure AI Service availability and configuration.
```

**Çözüm:**
1. **Seçenek 1**: Azure AI Hizmetini yapılandırın
   - `.env` dosyanıza `AZURE_AI_SERVICE_API_KEY` ekleyin
   - `.env` dosyanıza `AZURE_AI_SERVICE_ENDPOINT` ekleyin
   - Hizmetin erişilebilir olduğunu doğrulayın

2. **Seçenek 2**: Görsel çeviri isteğini kaldırın
   ```bash
   # Instead of: translate -l "ko" -img
   # Use: translate -l "ko" -md
   ```

### 5.2. Gerekli Yapılandırma Eksik

**Sorun:** Temel LLM yapılandırması eksik.

**Hata Mesajı:**
```
Error: No language model configuration found.
Please configure either Azure OpenAI or OpenAI in your .env file.
```

**Çözüm:**
1. `.env` dosyanızda aşağıdaki LLM yapılandırmalarından en az birinin olduğundan emin olun:
   - **Azure OpenAI**: `AZURE_OPENAI_API_KEY` ve `AZURE_OPENAI_ENDPOINT`
   - **OpenAI**: `OPENAI_API_KEY`
   
   Azure OpenAI veya OpenAI’den birini yapılandırmanız gerekir, ikisi birden değil.

### 5.3. Seçmeli Çeviri Karışıklığı

**Sorun:** Komut başarılı olsa da hiçbir dosya çevrilmedi.

**Olası Nedenler:**
- Yanlış dosya türü bayrakları (`-md`, `-img`, `-nb`)
- Projede eşleşen dosya yok
- Yanlış dizin yapısı

**Çözüm:**
1. **Debug modunu kullanın** ve neler olduğunu görün:
   ```bash
   translate -l "ko" -md -d
   ```

2. **Projenizdeki dosya türlerini kontrol edin:**
   ```bash
   # For markdown files
   find . -name "*.md" -not -path "./translations/*"
   
   # For notebooks
   find . -name "*.ipynb" -not -path "./translations/*"
   
   # For images
   find . -name "*.png" -o -name "*.jpg" -o -name "*.jpeg" -not -path "./translations/*"
   ```

3. **Bayrak kombinasyonlarını doğrulayın:**
   ```bash
   # Translate everything (default)
   translate -l "ko"
   
   # Translate specific types
   translate -l "ko" -md -img
   ```

## 6. Eski Sistemden Geçiş

### 6.1. Sadece Markdown Modu Kaldırıldı

**Sorun:** Otomatik markdown-only fallback’a dayanan komutlar artık beklediğiniz gibi çalışmıyor.

**Eski Davranış:**
```bash
# This used to automatically switch to markdown-only mode
translate -l "ko"  # (when Azure AI Vision was not configured)
```

**Yeni Davranış:**
```bash
# This now produces an error if image translation is requested but not configured
translate -l "ko" -img
```

**Çözüm:**
- **Ne çevirmek istediğinizi açıkça belirtin:**
  ```bash
  translate -l "ko" -md        # Only markdown
  translate -l "ko" -md -img   # Markdown and images
  translate -l "ko"            # Everything (if all services configured)
  ```

### 6.2. Beklenmeyen Bağlantı Davranışı

**Sorun:** Çevrilen dosyalardaki bağlantılar beklenmeyen yerlere yönlendiriyor.

**Neden:** Dinamik bağlantı işleme, seçilen dosya türlerine göre değişir.

**Çözüm:**
1. **Yeni bağlantı davranışını anlayın:**
   - `-nb` dahil: Notebook bağlantıları çevrilen sürümlere yönlendirir
   - `-nb` hariç: Notebook bağlantıları orijinal dosyalara yönlendirir
   - `-img` dahil: Görsel bağlantıları çevrilen sürümlere yönlendirir
   - `-img` hariç: Görsel bağlantıları orijinal dosyalara yönlendirir

2. **Kendi kullanımınıza uygun kombinasyonu seçin:**
   ```bash
   # All internal links point to translated versions
   translate -l "ko" -md -img -nb
   
   # Only markdown translated, other links point to originals
   translate -l "ko" -md
   ```

## 7. GitHub Action çalıştı ama Pull Request (PR) oluşmadı

**Belirti:** `peter-evans/create-pull-request` için workflow loglarında şu mesajı görüyorsunuz:

> Branch 'update-translations' is not ahead of base 'main' and will not be created

**Olası nedenler:**
- **Değişiklik yok:** Çeviri adımı fark üretmedi (repo zaten güncel).
- **Yoksayılan çıktılar:** `.gitignore` beklediğiniz dosyaları hariç tutuyor (ör. `*.ipynb`, `translations/`, `translated_images/`).
- **add-paths uyumsuzluğu:** Action’a verilen yollar gerçek çıktı konumlarıyla eşleşmiyor.
- **Workflow mantığı/koşulları:** Çeviri adımı erken çıktı veya beklenmeyen dizinlere yazdı.

**Nasıl düzeltilir / doğrulanır:**
1. **Çıktıların varlığını doğrulayın:** Çeviri sonrası workspace’de `translations/` ve/veya `translated_images/` içinde yeni/değişen dosyalar olduğundan emin olun.
   - Notebook çeviriyorsanız, `.ipynb` dosyalarının gerçekten `translations/<lang>/...` altında yazıldığından emin olun.
2. **`.gitignore`’u gözden geçirin:** Oluşturulan çıktıları hariç tutmayın. Şunları hariç tutmadığınızdan emin olun:
   - `translations/`
   - `translated_images/`
   - `*.ipynb` (notebook çeviriyorsanız)
3. **add-paths çıktılarla eşleşmeli:** Çok satırlı değer kullanın ve gerekirse iki klasörü de ekleyin:
   ```yaml
   with:
     add-paths: |
       translations/
       translated_images/
   ```
4. **Debug için PR’ı zorlayın:** Bağlantıların doğru olduğunu doğrulamak için geçici olarak boş commitlere izin verin:
   ```yaml
   with:
     commit-empty: true
   ```
5. **Debug ile çalıştırın:** Translate komutuna `-d` ekleyerek hangi dosyaların bulunduğunu ve yazıldığını görün.
6. **İzinler (GITHUB_TOKEN):** Workflow’un commit ve PR oluşturmak için yazma izni olduğundan emin olun:
   ```yaml
   permissions:
     contents: write
     pull-requests: write
   ```

## Hızlı Sorun Giderme Kontrol Listesi

Çeviri sorunlarını giderirken:

1. **Debug modunu kullanın:** Ayrıntılı loglar için `-d` bayrağını ekleyin
2. **Bayraklarınızı kontrol edin:** `-md`, `-img`, `-nb` niyetinizle uyumlu mu bakın
3. **Yapılandırmayı doğrulayın:** `.env` dosyanızda gerekli anahtarlar var mı kontrol edin
4. **Adım adım test edin:** Önce sadece `-md` ile başlayın, sonra diğer türleri ekleyin
5. **Dosya yapısını kontrol edin:** Kaynak dosyalar mevcut ve erişilebilir mi bakın

Mevcut komutlar ve bayraklar hakkında daha fazla bilgi için [Komut Referansı](./command-reference.md) sayfasına bakabilirsiniz.

---

**Feragatname**:
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerde hata veya yanlışlıklar olabileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından doğabilecek herhangi bir yanlış anlama veya yanlış yorumlamadan sorumlu değiliz.