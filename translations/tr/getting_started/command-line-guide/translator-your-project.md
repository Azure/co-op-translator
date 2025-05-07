<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d238206c3503631e32774716d11d1868",
  "translation_date": "2025-05-07T14:12:27+00:00",
  "source_file": "getting_started/command-line-guide/translator-your-project.md",
  "language_code": "tr"
}
-->
# Projenizi Co-op Translator ile Çevirin

**Co-op Translator**, projenizdeki markdown ve resim dosyalarını birden fazla dile çevirmenize yardımcı olan bir komut satırı arayüzü (CLI) aracıdır. Bu bölüm, aracın nasıl kullanılacağını açıklar, çeşitli CLI seçeneklerini kapsar ve farklı kullanım senaryoları için örnekler sunar.

> [!NOTE]
> Komutların tam listesi ve detaylı açıklamaları için lütfen [Command reference](./command-reference.md) sayfasına bakınız.

---

## Örnek Senaryolar ve Komutlar

İşte **Co-op Translator** için birkaç yaygın kullanım durumu ve çalıştırılacak uygun komutlar.

### 1. Temel Çeviri (Tek Dil)

Tüm projenizi (markdown dosyaları ve resimler) tek bir dile, örneğin Korece'ye çevirmek için aşağıdaki komutu kullanın:

```bash
translate -l "ko"
```

Bu komut, tüm markdown ve resim dosyalarını Korece'ye çevirecek, mevcut çevirileri silmeden yeni çeviriler ekleyecektir.

> [!TIP]
>
> **Co-op Translator**'da hangi dil kodlarının mevcut olduğunu görmek ister misiniz? Daha fazla bilgi için depodaki [Supported Languages](https://github.com/Azure/co-op-translator#supported-languages) bölümünü ziyaret edin.

#### Phi-3 CookBook Üzerinde Örnek

**Phi-3 CookBook**'ta, mevcut markdown dosyaları ve resimler için Korece çeviri eklemek amacıyla aşağıdaki yöntemi kullandım.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko"
Translating images: 100%|███████████████████████████████████████████████████| 276/276 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 153/153 [1:43:07<00:00, 241.31s/it]
```

### 2. Birden Fazla Dil Çevirisi

Projenizi birden fazla dile (örneğin İspanyolca, Fransızca ve Almanca) çevirmek için bu komutu kullanın:

```bash
translate -l "es fr de"
```

Bu komut, projeyi İspanyolca, Fransızca ve Almanca'ya çevirecek, mevcut çevirileri silmeden yeni çeviriler ekleyecektir.

#### Phi-3 CookBook Üzerinde Örnek

**Phi-3 CookBook**'ta, en son commitleri yansıtmak için değişiklikleri çektikten sonra, yeni eklenen markdown dosyaları ve resimleri çevirmek için aşağıdaki yöntemi kullandım.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko ja zh tw es fr" -a
Translating images: 100%|███████████████████████████████████████████████████| 273/273 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 6/6 [24:07<00:00, 241.31s/it]
```

> [!NOTE]
> Genellikle bir dili tek seferde çevirmek önerilir, ancak belirli değişikliklerin eklenmesi gereken durumlarda birden fazla dili aynı anda çevirmek daha verimli olabilir.

### 3. Çevirileri Güncelleme (Mevcut Çevirileri Siler)

Mevcut çevirileri güncellemek (yani mevcut çevirileri silip yenileriyle değiştirmek) için `-u` seçeneğini kullanın. Bu, belirtilen dillerdeki tüm mevcut çevirileri silecek ve yeniden çevirecektir.

```bash
translate -l "ko" -u
```

Uyarı: Bu komut, mevcut çevirileri silmeden önce onay isteyecektir.

#### Phi-3 CookBook Üzerinde Örnek

**Phi-3 CookBook**'ta, İspanyolca olarak çevrilmiş tüm dosyaları güncellemek için aşağıdaki yöntemi kullandım. Orijinal içerikte birden fazla markdown dosyasında önemli değişiklikler olduğunda bu yöntemi kullanmanızı öneririm. Sadece birkaç çevrilmiş markdown dosyası güncellenecekse, bu dosyaları manuel silip ardından `-a` yöntemini kullanarak güncellenmiş çevirileri eklemek daha verimlidir.

### 5. Sadece Resimleri Çevirme

Projenizde sadece resim dosyalarını çevirmek için `-img` seçeneğini kullanın:

```bash
translate -l "ko" -img
```

Bu komut, sadece resimleri Korece'ye çevirecek, markdown dosyalarına dokunmayacaktır.

### 6. Sadece Markdown Dosyalarını Çevirme

Projenizde sadece markdown dosyalarını çevirmek için `-md` seçeneğini kullanın:

```bash
translate -l "ko" -md
```

### 7. Çevrilmiş Dosyalarda Hata Kontrolü

Çevrilmiş dosyalarda hata kontrolü yapmak ve gerekirse çeviriyi yeniden denemek için `-chk` seçeneğini kullanın:

```bash
translate -l "ko" -chk
```

Bu komut, çevrilmiş markdown dosyalarını tarayacak ve hatalı dosyalar için çeviriyi yeniden deneyecektir.

#### Phi-3 CookBook Üzerinde Örnek

**Phi-3 CookBook**'ta, Korece dosyalarda çeviri hatalarını kontrol etmek ve tespit edilen dosyalar için otomatik olarak çeviriyi yeniden denemek amacıyla aşağıdaki yöntemi kullandım.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko" -chk 
Checking translated files for errors in ko...
Checking files for ko: 100%|██████████████████████████████████████████████████| 95/95 [00:01<00:00, 65.47file/s]
Retrying vsc-extension-quickstart.md for ko:   0%|                                     | 0/17 [00:00<?, ?file/s] 
```

Bu seçenek, çeviri hatalarını kontrol eder. Şu anda, orijinal ve çevrilmiş dosyalar arasındaki satır sonu farkı altıdan fazla ise dosya çeviri hatası olarak işaretlenir. Gelecekte bu kriteri daha esnek hale getirmeyi planlıyorum.

Örneğin, bu yöntem eksik parçalar veya bozuk çevirileri tespit etmek için faydalıdır ve bu dosyalar için otomatik olarak çeviriyi yeniden dener.

Ancak, hangi dosyaların sorunlu olduğunu zaten biliyorsanız, bu dosyaları manuel silip `-a` option to re-translate them.

### 8. Debug Mode

To enable detailed logging for troubleshooting, use the `-d` seçeneğini kullanmak daha verimlidir:

```bash
translate -l "ko" -d
```

Bu komut, çeviriyi hata ayıklama modunda çalıştırır ve çeviri sürecindeki sorunları tespit etmenize yardımcı olacak ek günlük bilgileri sağlar.

#### Phi-3 CookBook Üzerinde Örnek

**Phi-3 CookBook**'ta, markdown dosyalarında çok sayıda bağlantı içeren çevirilerin biçimlendirme hatalarına (bozuk çeviriler ve satır sonlarının yok sayılması gibi) yol açtığı bir sorunla karşılaştım. Bu sorunu teşhis etmek için çeviri sürecinin nasıl işlediğini görmek amacıyla `-d` seçeneğini kullandım.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "ko" -d
DEBUG:openai._base_client:Request options: {'method': 'post', 'url': '/chat/completions', 'headers': {'api-key': 'af04e0bea45747d8a7b8c131c1971044'}, 'files': None, 'json_data': {'messages': [{'role': 'user', 'content': "Translate the following text to ko. NEVER ADD ANY EXTRA CONTENT OUTSIDE THE TRANSLATION. TRANSLATE ONLY WHAT IS GIVEN TO YOU.. MAINTAIN MARKDOWN FORMAT\n\n# Phi-3 Cookbook: Hands-On Examples with Microsoft's Phi-3 Models [![Open and use the samples in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phi-3cookbook) [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%
...
```

### 9. Tüm Dilleri Çevirme

Projeyi desteklenen tüm dillere çevirmek isterseniz, `all` anahtar kelimesini kullanın.

> [!WARNING]
> Tüm dillerin aynı anda çevrilmesi, projenin büyüklüğüne bağlı olarak önemli zaman alabilir. Örneğin, **Phi-3 CookBook**'un İspanyolcaya çevrilmesi yaklaşık 2 saat sürdü. Ölçek göz önüne alındığında, tek bir kişinin 20 dili yönetmesi pratik değildir. Çalışmayı birden fazla katılımcıya bölmek, her birinin bir veya iki dili yönetmesi ve çevirileri kademeli olarak güncellemesi önerilir.

```bash
translate -l "all"
```

Bu komut, projeyi mevcut tüm dillere çevirecektir. Devam ederseniz, çeviri projenin büyüklüğüne bağlı olarak önemli zaman alabilir.

> [!TIP]
>
> ### Çevrilmiş Dosyaların Manuel Silinmesi (İsteğe Bağlı)
> Kaynak dosya güncellendiğinde çevrilmiş dosyalar artık otomatik olarak tespit edilip temizleniyor.
>
> Ancak, bir çeviriyi manuel olarak güncellemek istiyorsanız — örneğin belirli bir dosyayı yeniden yapmak veya sistem davranışını geçersiz kılmak için — aşağıdaki komutla dosyanın tüm dil klasörlerindeki sürümlerini silebilirsiniz.
>
> ### Windows Üzerinde:
> 1. **Komut İstemi Kullanarak**:
>    - Komut İstemi'ni açın.
>    - `cd` komutuyla dosyaların bulunduğu klasöre gidin.
>    - Dosyaları silmek için aşağıdaki komutu kullanın:
>      ```
>      del /s *filename*
>      ```
>      `filename` with the specific part of the file name you're looking for. The `/s` seçeneği alt dizinlerde de arama yapar.
>
> 2. **PowerShell Kullanarak**:
>    - PowerShell'i açın.
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
>     `filename` with the specific name.
>
> Always double-check the files before deleting to avoid accidental loss. 
>
> Once you have deleted the files which need to be replace simply rerun your `translate -l` komutunu en son dosya değişikliklerini güncellemek için değiştirin.

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba gösterilse de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayınız. Orijinal belge, kendi ana dilindeki haliyle yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu oluşabilecek yanlış anlamalar veya yorum hatalarından sorumlu değiliz.