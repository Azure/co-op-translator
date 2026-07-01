# Sorun Giderme

Bir çeviri çalışması beklenmedik şekilde başarılı olduğunda, yapılandırma sırasında başarısız olduğunda veya gözden geçirilmesi gereken çıktı ürettiğinde bu sayfayı kullanın.

## Buradan Başlayın

1. Önce şu gibi odaklanmış bir komutu çalıştırın: `translate -l "ko" -md`.
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

- Azure OpenAI veya OpenAI yapılandırın.
- Değişkenlerin komutun çalıştığı ortamda bulunduğunu doğrulayın.
- Yerel kullanım için, proje kökünde `.env` içine koyun.

Bakınız [Yapılandırma](configuration.md).

### Azure AI Vision Olmadan Görsel Çevirisi

Hata:

```text
Image translation requested but Azure AI Service is not configured.
```

Düzeltme:

- `AZURE_AI_SERVICE_API_KEY` ekleyin.
- `AZURE_AI_SERVICE_ENDPOINT` ekleyin.
- Veya `translate -l "ko" -md` gibi sadece metin komutu çalıştırın.

### Geçersiz Anahtar veya Uç Nokta

Belirtiler `401`, gizlenmiş izin hataları veya uç nokta erişim hatalarını içerebilir.

Düzeltme:

- Anahtarın uç nokta ile aynı Azure kaynağına ait olduğunu doğrulayın.
- `-img` kullanıldığında kaynağın Vision'ı desteklediğini doğrulayın.
- Azure OpenAI dağıtım adının ve API sürümünün dağıtımınızla eşleştiğini doğrulayın.
- Hata ayıklama günlükleriyle çalıştırın: `translate -l "ko" -md -d -s`.

## Hiç Dosya Çevrilmedi

Yaygın nedenler:

- Seçilen bayraklar dosyalarınızla eşleşmiyor.
- Zaten mevcut çevrilmiş dosyalar var.
- Kaynak dosyalar hariç tutulan dizinlerin altında olabilir.
- Komut yanlış proje kökünden çalıştırılıyor.

Kontroller:

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -nb --dry-run
translate -l "ko" -img --dry-run
```

Komut proje kökü dışında çalıştırıldığında `--root-dir` kullanın.

## Beklenmeyen Bağlantı Davranışı

Bağlantı yeniden yazımı seçilen içerik türlerine bağlıdır:

- `-nb` dahil: notebook bağlantıları çevrilmiş notebook'lara işaret edebilir.
- `-nb` hariç: notebook bağlantıları kaynak notebook'lara işaret etmeye devam edebilir.
- `-img` dahil: resim bağlantıları çevrilmiş resimlere işaret edebilir.
- `-img` hariç: resim bağlantıları kaynak resimlere işaret etmeye devam edebilir.

Tüm dahili bağlantıların çevrilmiş çıktıları tercih etmesini istiyorsanız tam bir içerik çevirisi çalıştırın:

```bash
translate -l "ko" -md -nb -img
```

Çeviriden sonra bağlantı incelemesi çalıştırın:

```bash
co-op-review -l "ko"
```

## Markdown İşleme Sorunları

Çevrilmiş Markdown yanlış görüntüleniyorsa:

- frontmatter'ın `---` ile başlayıp bittiğini kontrol edin.
- Kod çitlerinin sayısının kaynak ve çevrilmiş dosyalar arasında eşleştiğini kontrol edin.
- Yaygın yapı sorunlarını yakalamak için `co-op-review` çalıştırın.
- Çıktı bozulduysa belirli dosyayı yeniden çevirin.

```bash
co-op-review -l "ko" --format github
```

## GitHub Action Çalıştı ama Pull Request Oluşturulmadı

Eğer `peter-evans/create-pull-request` dalın base'den önde olmadığını bildiriyorsa, iş akışı commit edilecek dosya bulamamıştır.

Olası nedenler:

- Çeviri çalışması herhangi bir değişiklik üretmedi.
- `.gitignore` `translations/`, `translated_images/` veya çevrilmiş notebook'ları hariç tutuyor.
- `add-paths`, oluşturulan çıktı dizinleriyle eşleşmiyor.
- Çeviri adımı erken sonlandı.

Çözümler:

1. Oluşturulan dosyaların `translations/` veya `translated_images/` içinde olduğunu doğrulayın.
2. `.gitignore`'in oluşturulan çıktıları yoksaymadığını doğrulayın.
3. Uyumlu `add-paths` kullanın:

   ```yaml
   with:
     add-paths: |
       translations/
       translated_images/
   ```

4. Geçici olarak çeviri komutuna hata ayıklama bayrakları ekleyin:

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

Makine çevirileri insan incelemesine ihtiyaç duyabilir. Deneysel kalite puanlaması ve düşük güvenli onarım iş akışlarını istediğinizde yalnızca `evaluate` kullanın.

!!! warning "Experimental"
    `evaluate` kural tabanlı ve LLM tabanlı kontroller kullanabilir ve puanlama modeli ile meta veri davranışı değişebilir. İş akışınız değişikliklere hazır değilse bunu gerekli CI kapılarının dışında tutun.

Deterministik CI kontrolleri için bunun yerine `co-op-review` kullanın.