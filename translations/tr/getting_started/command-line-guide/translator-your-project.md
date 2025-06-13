<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d238206c3503631e32774716d11d1868",
  "translation_date": "2025-06-12T18:48:31+00:00",
  "source_file": "getting_started/command-line-guide/translator-your-project.md",
  "language_code": "tr"
}
-->
# Projenizi Co-op Translator ile Çevirin

**Co-op Translator**, projenizdeki markdown ve resim dosyalarını birden fazla dile çevirmeye yardımcı olan bir komut satırı arayüzü (CLI) aracıdır. Bu bölüm, aracın nasıl kullanılacağını açıklar, çeşitli CLI seçeneklerini kapsar ve farklı kullanım senaryoları için örnekler sunar.

> [!NOTE]
> Komutların tam listesi ve detaylı açıklamaları için lütfen [Command reference](./command-reference.md) sayfasına bakınız.

---

## Örnek Senaryolar ve Komutlar

İşte **Co-op Translator** için birkaç yaygın kullanım durumu ve çalıştırılacak uygun komutlar.

### 1. Temel Çeviri (Tek Dil)

Tüm projenizi (markdown dosyaları ve resimler) tek bir dile, örneğin Koreceye çevirmek için aşağıdaki komutu kullanın:

```bash
translate -l "ko"
```

Bu komut, tüm markdown ve resim dosyalarını Koreceye çevirecek ve mevcut çevirileri silmeden yeni çeviriler ekleyecektir.

> [!TIP]
>
> **Co-op Translator**’da hangi dil kodlarının mevcut olduğunu görmek ister misiniz? Daha fazla bilgi için depodaki [Supported Languages](https://github.com/Azure/co-op-translator#supported-languages) bölümünü ziyaret edin.

#### Phi-3 CookBook Üzerinde Örnek

**Phi-3 CookBook**’ta, mevcut markdown dosyaları ve resimler için Korece çeviriyi eklemek için aşağıdaki yöntemi kullandım.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko"
Translating images: 100%|███████████████████████████████████████████████████| 276/276 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 153/153 [1:43:07<00:00, 241.31s/it]
```

### 2. Birden Fazla Dil Çevirisi

Projenizi birden fazla dile (örneğin İspanyolca, Fransızca ve Almanca) çevirmek için şu komutu kullanın:

```bash
translate -l "es fr de"
```

Bu komut, projeyi İspanyolca, Fransızca ve Almancaya çevirecek ve mevcut çevirileri üzerine yazmadan yeni çeviriler ekleyecektir.

#### Phi-3 CookBook Üzerinde Örnek

**Phi-3 CookBook**’ta, en son commitleri yansıtmak için değişiklikleri çektikten sonra, yeni eklenen markdown dosyaları ve resimleri çevirmek için aşağıdaki yöntemi kullandım.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko ja zh tw es fr" -a
Translating images: 100%|███████████████████████████████████████████████████| 273/273 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 6/6 [24:07<00:00, 241.31s/it]
```

> [!NOTE]
> Genellikle bir dili bir seferde çevirmek önerilir, ancak belirli değişikliklerin eklenmesi gereken durumlarda, birden fazla dili aynı anda çevirmek daha verimli olabilir.

### 3. Çevirileri Güncelleme (Mevcut Çevirileri Siler)

Mevcut çevirileri güncellemek (yani mevcut çevirileri silip yenileriyle değiştirmek) için `-u` seçeneğini kullanın. Bu, belirtilen diller için tüm mevcut çevirileri silecek ve yeniden çevirecektir.

```bash
translate -l "ko" -u
```

Uyarı: Bu komut, mevcut çevirileri silmeden önce onayınızı isteyecektir.

#### Phi-3 CookBook Üzerinde Örnek

**Phi-3 CookBook**’ta, İspanyolca çevrilmiş tüm dosyaları güncellemek için aşağıdaki yöntemi kullandım. Orijinal içerikte birden fazla markdown dosyasında önemli değişiklikler varsa bu yöntemi kullanmanızı öneririm. Sadece birkaç çevrilmiş markdown dosyasını güncellemeniz gerekiyorsa, bu dosyaları manuel olarak silip ardından `-a` yöntemini kullanarak güncellenmiş çevirileri eklemek daha verimlidir.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "es" -u
Warning: The update command will delete all existing translations for 'es' and re-translate everything.
Do you want to continue? Type 'yes' to proceed: yes
Proceeding with update...
Translating images: 100%|████████████████████████████████████████████| 150/150 [43:46<00:00, 15.55s/it]
Translating markdown files: 100%|███████████████████████████████████| 95/95 [1:40:27<00:00, 125.62s/it]
```

### 5. Sadece Resimleri Çevirme

Projede sadece resim dosyalarını çevirmek için `-img` seçeneğini kullanın:

```bash
translate -l "ko" -img
```

Bu komut, sadece resimleri Koreceye çevirecek, markdown dosyalarına dokunmayacaktır.

### 6. Sadece Markdown Dosyalarını Çevirme

Projede sadece markdown dosyalarını çevirmek için `-md` seçeneğini kullanın:

```bash
translate -l "ko" -md
```

### 7. Çevrilmiş Dosyalarda Hata Kontrolü

Çevrilmiş dosyaları hatalar için kontrol etmek ve gerekirse çeviriyi yeniden denemek istiyorsanız `-chk` seçeneğini kullanın:

```bash
translate -l "ko" -chk
```

Bu komut, çevrilmiş markdown dosyalarını tarar ve hata bulunan dosyalar için çeviriyi tekrar dener.

#### Phi-3 CookBook Üzerinde Örnek

**Phi-3 CookBook**’ta, Korece dosyalarda çeviri hatalarını kontrol etmek ve sorunlu dosyalar için otomatik olarak çeviriyi tekrar denemek için aşağıdaki yöntemi kullandım.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko" -chk 
Checking translated files for errors in ko...
Checking files for ko: 100%|██████████████████████████████████████████████████| 95/95 [00:01<00:00, 65.47file/s]
Retrying vsc-extension-quickstart.md for ko:   0%|                                     | 0/17 [00:00<?, ?file/s] 
```

Bu seçenek çeviri hatalarını kontrol eder. Şu anda, orijinal ve çevrilmiş dosyalar arasındaki satır sonu farkı altıdan fazla ise dosya çeviri hatası olarak işaretleniyor. Gelecekte daha esnek bir kriterle bunu geliştirmeyi planlıyorum.

Örneğin, bu yöntem eksik parçaları veya bozuk çevirileri tespit etmek için faydalıdır ve bu dosyalar için otomatik olarak çeviriyi yeniden dener.

Ancak hangi dosyaların sorunlu olduğunu zaten biliyorsanız, bu dosyaları manuel olarak silmek ve ardından `-a` option to re-translate them.

### 8. Debug Mode

To enable detailed logging for troubleshooting, use the `-d` seçeneğini kullanmak daha verimlidir:

```bash
translate -l "ko" -d
```

Bu komut, çeviriyi hata ayıklama modunda çalıştırır ve çeviri sürecinde karşılaşabileceğiniz sorunları tespit etmenize yardımcı olacak ek günlük bilgileri sağlar.

#### Phi-3 CookBook Üzerinde Örnek

**Phi-3 CookBook**’ta, markdown dosyalarındaki çok sayıda bağlantı içeren çevirilerde biçimlendirme hataları (bozuk çeviriler ve göz ardı edilen satır sonları gibi) yaşadım. Bu sorunu teşhis etmek için `-d` seçeneğini kullanarak çeviri sürecinin nasıl işlediğini inceledim.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "ko" -d
DEBUG:openai._base_client:Request options: {'method': 'post', 'url': '/chat/completions', 'headers': {'api-key': 'af04e0bea45747d8a7b8c131c1971044'}, 'files': None, 'json_data': {'messages': [{'role': 'user', 'content': "Translate the following text to ko. NEVER ADD ANY EXTRA CONTENT OUTSIDE THE TRANSLATION. TRANSLATE ONLY WHAT IS GIVEN TO YOU.. MAINTAIN MARKDOWN FORMAT\n\n# Phi-3 Cookbook: Hands-On Examples with Microsoft's Phi-3 Models [![Open and use the samples in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phi-3cookbook) [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%
...
```

### 9. Tüm Dillerde Çeviri

Projeyi desteklenen tüm dillere çevirmek istiyorsanız, all anahtar kelimesini kullanın.

> [!WARNING]
> Tüm dillerde aynı anda çeviri yapmak, projenin büyüklüğüne bağlı olarak ciddi zaman alabilir. Örneğin, **Phi-3 CookBook**’un İspanyolcaya çevrilmesi yaklaşık 2 saat sürdü. Ölçek göz önüne alındığında, 20 dili tek bir kişinin yönetmesi pratik değildir. Çalışmanın birden fazla katılımcıya bölünmesi, her birinin bir veya iki dili yönetmesi ve çevirilerin kademeli olarak güncellenmesi önerilir.

```bash
translate -l "all"
```

Bu komut, projeyi mevcut tüm dillere çevirecektir. Devam ederseniz, projenin büyüklüğüne bağlı olarak çeviri önemli ölçüde zaman alabilir.

> [!TIP]
>
> ### Çevrilmiş Dosyaları Manuel Olarak Silme (İsteğe Bağlı)
> Kaynak dosya güncellendiğinde çevrilmiş dosyalar artık otomatik olarak algılanıp temizleniyor.
>
> Ancak, belirli bir dosyayı yeniden yapmak veya sistem davranışını geçersiz kılmak gibi manuel bir güncelleme yapmak istiyorsanız, dosyanın tüm dil klasörlerindeki sürümlerini silmek için aşağıdaki komutu kullanabilirsiniz.
>
> ### Windows’ta:
> 1. **Komut İstemi Kullanarak**:
>    - Komut İstemi’ni açın.
>    - `cd` komutunu kullanarak dosyaların bulunduğu klasöre gidin.
>    - Dosyaları silmek için aşağıdaki komutu kullanın:
>      ```
>      del /s *filename*
>      ```
>      `filename` with the specific part of the file name you're looking for. The `/s` seçeneği alt dizinlerde de arama yapar.
>
> 2. **PowerShell Kullanarak**:
>    - PowerShell’i açın.
>    - Bu komutu çalıştırın:
>      ```powershell
>      Get-ChildItem -Path "C:\YourPath" -Filter "*filename*" -Recurse | Remove-Item -Force
>      ```
>      `"C:\YourPath"` with the folder path and `filename` with the specific name.
>
> ### On macOS/Linux:
> 1. **Using Terminal**:
>   - Open Terminal.
>   - Navigate to the directory with `cd`.
>   - Use the `find` komutunu değiştirin:
>     ```bash
>     find . -type f -name "*filename*" -delete
>     ```
>     En güncel dosya değişikliklerini güncellemek için `filename` with the specific name.
>
> Always double-check the files before deleting to avoid accidental loss. 
>
> Once you have deleted the files which need to be replace simply rerun your `translate -l` komutunu değiştirin.

**Feragatname**:  
Bu belge, AI çeviri servisi [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba gösterilse de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucunda ortaya çıkabilecek herhangi bir yanlış anlama veya yorumlama nedeniyle sorumluluk kabul edilmemektedir.