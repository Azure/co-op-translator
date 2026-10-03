# Sorun Giderme

Bu sayfayı, bir çeviri çalışması beklenmedik şekilde başarılı olduğunda, yapılandırma sırasında başarısız olduğunda veya incelenmesi gereken çıktı ürettiğinde kullanın.

## Buradan Başlayın

1. Önce odaklanmış bir komut çalıştırın, örneğin `translate -l "ko" -md`.
2. Konsol hata ayıklama günlükleri için `-d` ekleyin.
3. Hata ayıklama günlüklerini `<root-dir>/logs/` altında kaydetmek için `-s` ekleyin.
4. Tazelik, yapı ve yerel bağlantıları kontrol etmek için çeviriden sonra `co-op-review` çalıştırın.

```bash
translate -l "ko" -md -d -s
co-op-review -l "ko"
```

## Yapılandırma Hataları

### Dil Modeli Sağlayıcısı Yok

Hata:

```text
No language model configuration found.
```

Düzeltme:

- Azure OpenAI, OpenAI veya Anthropic'i yapılandırın.
- Değişkenlerin komutun çalıştığı ortamda olduğundan emin olun.
- Yerel kullanım için, bunları proje kökündeki `.env` içine koyun.

Bkz. [Yapılandırma](configuration.md).

### Azure AI Vision olmadan Görüntü Çevirisi

Hata:

```text
Image translation requested but Azure AI Service is not configured.
```

Düzeltme:

- `AZURE_AI_SERVICE_API_KEY` ekleyin.
- `AZURE_AI_SERVICE_ENDPOINT` ekleyin.
- Veya `translate -l "ko" -md` gibi yalnızca metin komutu çalıştırın.

### Geçersiz Anahtar veya Uç Nokta

Belirtiler `401`, yetki hatalarıyla ilgili gizlenmiş mesajlar veya uç nokta erişim hatalarını içerebilir.

Düzeltme:

- Anahtarın uç nokta ile aynı Azure kaynağına ait olduğunu doğrulayın.
- `-img` kullanırken kaynağın Vision'ı desteklediğini doğrulayın.
- Azure OpenAI dağıtım adının ve API sürümünün dağıtımınızla eşleştiğini doğrulayın.
- Hata ayıklama günlükleriyle çalıştırın: `translate -l "ko" -md -d -s`.

## Hiçbir Dosya Çevrilmedi

Yaygın nedenler:

- Seçilen bayraklar dosyalarınızla eşleşmiyor.
- Zaten mevcut çevrilmiş dosyalar var.
- Kaynak dosyalar hariç tutulan dizinlerin altında.
- Komut yanlış proje kökünden çalışıyor.

Kontroller:

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -nb --dry-run
translate -l "ko" -img --dry-run
```

Komut proje kökünün dışından çalıştırıldığında `--root-dir` kullanın.

## Beklenmeyen Bağlantı Davranışı

Bağlantı yeniden yazımı seçili içerik türlerine bağlıdır:

- `-nb` dahil: notebook bağlantıları çevrilmiş notebook'lara yönlendirebilir.
- `-nb` hariç: notebook bağlantıları kaynak notebook'lara işaret etmeye devam edebilir.
- `-img` dahil: görsel bağlantıları çevrilmiş görsellere yönlendirebilir.
- `-img` hariç: görsel bağlantıları kaynak görsellere işaret etmeye devam edebilir.

Tüm dahili bağlantıların çevrilmiş çıktıları tercih etmesi gerektiğinde tam içerik çevirisi çalıştırın:

```bash
translate -l "ko" -md -nb -img
```

Çeviriden sonra bağlantı incelemesi çalıştırın:

```bash
co-op-review -l "ko"
```

## Markdown İşleme Sorunları

Çevrilmiş Markdown yanlış görüntüleniyorsa:

- Frontmatter'ın `---` ile başlayıp bittiğini kontrol edin.
- Kod çitlerinin sayısının kaynak ve çevrilmiş dosyalar arasında eşleştiğini kontrol edin.
- Yaygın yapı sorunlarını yakalamak için `co-op-review` çalıştırın.
- Çıktı bozulduysa ilgili dosyayı yeniden çevirin.

```bash
co-op-review -l "ko" --format github
```

## GitHub Action Çalıştı ancak Pull Request Oluşturulmadı

Eğer `peter-evans/create-pull-request` dalın base'den ileride olmadığını raporluyorsa, iş akışı commitlenecek dosya bulamadı.

Muhtemel nedenler:

- Çeviri çalışması herhangi bir değişiklik üretmedi.
- `.gitignore` `translations/`, `translated_images/` veya çevrilmiş notebook'ları hariç tutuyor olabilir.
- `add-paths` oluşturulan çıktı dizinleriyle eşleşmiyor.
- Çeviri adımı erken sonlandı.

Düzeltmeler:

1. Oluşturulan dosyaların `translations/` veya `translated_images/` içinde bulunduğunu doğrulayın.
2. `.gitignore` dosyasının oluşturulan çıktıları yok saymadığından emin olun.
3. Eşleşen `add-paths` kullanın:

   ```yaml
   with:
     add-paths: |
       translations/
       translated_images/
   ```

4. Geçici olarak translate komutuna hata ayıklama bayrakları ekleyin:

   ```bash
   translate -l "ko" -md -d -s
   ```

5. İş akışı izinlerinin şunları içerdiğini doğrulayın:

   ```yaml
   permissions:
     contents: write
     pull-requests: write
   ```

## Çeviri Kalitesi

Makine çevirileri insan incelemesine ihtiyaç duyabilir. Deneysel kalite puanlaması ve düşük güvenceli onarım iş akışları istediğinizde yalnızca `evaluate` kullanın.

!!! warning "Experimental"
    `evaluate` kural tabanlı ve LLM tabanlı kontroller kullanabilir; puanlama modeli ve meta veri davranışı değişebilir. İş akışınız değişikliklere hazır değilse bunu zorunlu CI kapılarının dışında tutun.

Kararlı CI kontrolleri için bunun yerine `co-op-review` kullanın.