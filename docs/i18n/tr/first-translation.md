# Küçük bir projeyi çevirin, düzenleyin ve gözden geçirin

İki kısa Markdown dosyası ve bir hedef dil ile başlayın. Çevirilerin nereye yazıldığını, kaynak değiştiğinde neler olduğunu ve sonucu nasıl kontrol edeceğinizi göreceksiniz.

## Kayıtlı sonuçlar

Bu örnek 19 Eylül 2026 tarihinde Co-op Translator 0.21.0 ve Azure OpenAI (`gpt-5-mini`) ile çalıştırıldı. Değiştirilmemiş CLI komutları, oluşturulmuş wheel ve mevcut Python bağımlılıkları kullanılarak Click'in `CliRunner` aracılığıyla çağrıldı.

| Adım | Sonuç |
| --- | --- |
| Önizleme | Çıkış 0; model çevirisi istenmedi |
| İlk çeviri | Çıkış 0; 27.36 saniye |
| İlk inceleme | Çıkış 0 |
| README'i düzenle ve incele | Çıkış 1; güncelliğini yitirmiş çeviri tespit edildi |
| Çeviriyi güncelle | Çıkış 0; 22.17 saniye |
| Güncelleme sonrası inceleme | Çıkış 0; hata veya uyarı yok |
| Değişmemiş kılavuz | README güncellemesi öncesi ve sonrası aynı baytlar |
| Tekrar çalıştır | Çıkış 0; tüm çeviri dosyaları için aynı hash'ler |

Bunlar bireysel çalıştırma ölçümleridir, performans garantisi değildir. Kurulum süresi hariç tutuldu; sağlayıcı faturalaması ölçülmedi. Değişmeyen bir çalıştırma yine de sağlayıcı sağlık kontrolü yapabilir.

İnceleyin: [ilk çeviri](../../assets/demo/before.txt), [güncellenmiş çeviri](../../assets/demo/after.txt), [tam çeviri farkı](../../assets/demo/update.diff), [eski inceleme](../../assets/demo/review-stale.txt), [nihai inceleme](../../assets/demo/review-after.txt) ve [çalıştırma ayrıntıları](../../assets/demo/results.json). Tam dosya çevirisi, yakalanan farkın gösterdiği gibi diğer ifadeleri değiştirebilir. Her iki metin öğesi de üretilmiş feragatnameyi korur.

İnsan incelemesi hala önemlidir: kaydedilen güncelleme `[사용 가이드](guide.md)을` ifadesini kullanıyor; Korece parçacık `[사용 가이드](guide.md)를` olmalıydı. Metin öğeleri bu çıktıyı değiştirilmiş bir model çıktısı olarak sunmak yerine olduğu gibi tutar. Yapısal inceleme bu ifade sorununa rağmen geçer.

## 1. Küçük bir klasör hazırlayın

Python 3.11–3.14 kullanın ve [sanal ortam kurulumu](configuration.md#local-runtime-setup). Bu örnek için kullanılan sürümü yükleyin:

```bash
python -m pip install co-op-translator==0.21.0
mkdir translation-demo
cd translation-demo
git init
```

Bu klasöre [README.txt](../../assets/demo/README.txt) ve [guide.txt](../../assets/demo/guide.txt) dosyalarını indirip `README.md` ve `guide.md` olarak kaydedin. Bunlar küçük kurgusal proje belgeleridir; herhangi bir uygulama kurulumu gerekli değildir.

README bir kod bloğu ve `guide.md`'ye bir bağlantı içerir. Son cümlesi şudur:

```text
Notes are saved locally.
```

Bu klasörde yalnızca bu iki kaynak belgeyi tutun. Aşağıdaki tüm komutlar `translation-demo` içinde çalıştırılır ve Bash ile PowerShell'de çalışır.

## 2. Kimlik bilgileri olmadan önizleme

```bash
translate -l "ko" -md --dry-run
```

Önizleme, bir modele çağrı yapmadan veya çevirileri yazmadan çeviri işini tahmin eder. Token tahminleri faturalama teklifi değildir. İlk çalıştırma, her iki Markdown dosyasını yeni iş olarak tanımlamalıdır.

## 3. Bir sağlayıcı seçin ve çevirin

Bir sağlayıcıyı [yapılandırma kılavuzu](configuration.md) kullanarak yapılandırın: Azure OpenAI, OpenAI veya Anthropic. OpenAI ve Anthropic metin çevirisi için bir Azure hesabı gerekmez. Görüntü hizmetleri bu örnek için gerekli değildir.

Yerel bir `.env` dosyası kullanıyorsanız, `.env`'yi bu klasörün `.gitignore` dosyasına ekleyin. Çeviri çağrıları sağlayıcı hesabınızı kullanır ve ücretlendirmeye yol açabilir.

```bash
translate -l "ko" -md
co-op-review -l "ko"
```

Açın `translations/ko/README.md` ve `translations/ko/guide.md`. Korece ifadeyi, kod bloğunu ve çevrilmiş README'den çevrilmiş kılavuza olan bağlantıyı kontrol edin. Çıktı ifadeleri modele göre değişir.

`co-op-review` tazeliği, yapıyı ve yerel bağlantıları kontrol eder. Geçen bir sonuç dilbilimsel doğruluğu garantilemez. Devam etmeden önce raporlanan hataları giderin.

Başarılı temel sürümü Git ile kaydedin (gerekirse önce Git kimliğinizi yapılandırın):

```bash
git add README.md guide.md translations
git commit -m "Record initial Korean translation"
```

## 4. Kaynağı değiştirin

`README.md` içinde `Notes are saved locally.` ifadesini şu ile değiştirin:

```text
Notes are saved locally as Markdown files.
```

`guide.md`'i değişmeden bırakın. Sonra şunu çalıştırın:

```bash
co-op-review -l "ko"
translate -l "ko" -md --dry-run
```

İnceleme, README çevirisini güncelliğini yitirmiş olarak raporlamalı ve başarısız şekilde çıkmalıdır. Bu beklenen ara durumdur. Önizleme, değiştirilen README için iş belirlemelidir.

## 5. Güncelleyin ve farkı inceleyin

```bash
translate -l "ko" -md
git diff -- README.md translations/ko/README.md
git diff -- translations/ko/guide.md
co-op-review -l "ko"
```

Gerçek farkı inceleyin: varsayılan CLI değiştirilen dosyayı yeniden çevirir, bu nedenle model ayrıca o dosyadaki diğer ifadeleri de düzeltebilir. Değişmemiş kılavuzda fark olmamalıdır. İnceleme artık README'yi güncelliğini yitirmiş olarak rapor etmemelidir; diğer bulguları görmezden gelmek yerine araştırın.

İnsan tarafından yapılan Markdown düzenlemelerinin blok düzeyinde korunması, [Python API](api.md) içinde isteğe bağlı bir çeviri durum sağlayıcısı gerektirir. Bu, bu CLI komutlarıyla etkinleştirilmemiştir.

## 6. Değişiklik olmadan tekrar çalıştırın

Güncellenmiş kaynak ve çeviriyi commit edin:

```bash
git add README.md translations
git commit -m "Update Korean translation after source edit"
translate -l "ko" -md
git diff --exit-code -- translations
```

Mevcut çeviriler ve değişmeyen yapılandırma ile çevirmen dosyaları atlar. Son Git komutu hiçbir fark üretmemeli ve başarılı şekilde çıkmalıdır.

## Sonraki adımlar

- [Yalnızca README'yi çevirin ve bir pull request açın](github-actions.md#your-first-readme-translation-pr).
- [CLI, Python API veya MCP'yi seçin](workflows.md).
- [Kodlama yapmadan bir çeviri sorununu bildirin](https://github.com/Azure/co-op-translator/issues/new?template=translation_feedback.yml).