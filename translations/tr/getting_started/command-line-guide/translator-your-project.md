<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "33db54f4f3ca9f0321be05374b591f2b",
  "translation_date": "2025-05-06T18:00:51+00:00",
  "source_file": "getting_started/command-line-guide/translator-your-project.md",
  "language_code": "tr"
}
-->
# Projenizi Co-op Translator ile Çevirin

**Co-op Translator**, projenizdeki markdown ve resim dosyalarını birden fazla dile çevirmenize yardımcı olan bir komut satırı aracı (CLI)dır. Bu bölüm, aracın nasıl kullanılacağını, çeşitli CLI seçeneklerini ve farklı kullanım senaryoları için örnekleri açıklar.

> [!NOTE]
> Komutların tam listesi ve ayrıntılı açıklamaları için lütfen [Command reference](./command-reference.md) bölümüne bakınız.

---

## Örnek Senaryolar ve Komutlar

İşte **Co-op Translator** için birkaç yaygın kullanım durumu ve çalıştırılacak uygun komutlar.

### 1. Temel Çeviri (Tek Dil)

Tüm projenizi (markdown dosyaları ve resimler) tek bir dile, örneğin Korece’ye çevirmek için aşağıdaki komutu kullanın:

```bash
translate -l "ko"
```

Bu komut, tüm markdown ve resim dosyalarını Korece’ye çevirir ve mevcut çevirileri silmeden yenilerini ekler.

> [!TIP]
>
> **Co-op Translator**’da hangi dil kodlarının mevcut olduğunu görmek ister misiniz? Daha fazla bilgi için repodaki [Supported Languages](https://github.com/Azure/co-op-translator#supported-languages) bölümünü ziyaret edin.

#### Phi-3 CookBook Üzerinde Örnek

**Phi-3 CookBook**’ta, mevcut markdown dosyaları ve resimler için Korece çeviriyi eklemek amacıyla aşağıdaki yöntemi kullandım.

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

Bu komut, projeyi İspanyolca, Fransızca ve Almanca’ya çevirir, mevcut çevirileri silmeden yenilerini ekler.

#### Phi-3 CookBook Üzerinde Örnek

**Phi-3 CookBook**’ta, en son commitleri yansıtmak için güncellemeleri çektikten sonra, yeni eklenen markdown dosyaları ve resimleri çevirmek için aşağıdaki yöntemi kullandım.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko ja zh tw es fr" -a
Translating images: 100%|███████████████████████████████████████████████████| 273/273 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 6/6 [24:07<00:00, 241.31s/it]
```

> [!NOTE]
> Genellikle bir dili tek seferde çevirmek önerilir, ancak belirli değişikliklerin eklenmesi gereken durumlarda, birden fazla dili aynı anda çevirmek daha verimli olabilir.

### 3. Kök Dizini Belirtmek

Varsayılan olarak, çevirmen geçerli çalışma dizinini kullanır. Projeniz başka bir yerdeyse, kök dizini -r seçeneği ile belirtin:

```bash
translate -l "es fr de" -r "./my_project"
```

Bu komut `./my_project` içindeki dosyaları çevirir. `-u` seçeneği, belirtilen dillerdeki mevcut tüm çevirileri siler ve yeniden çevirir.

```bash
translate -l "ko" -u
```

Uyarı: Bu komut, mevcut çevirileri silmeden önce onay isteyecektir.

#### Phi-3 CookBook Üzerinde Örnek

**Phi-3 CookBook**’ta, İspanyolca çevirisi yapılmış tüm dosyaları güncellemek için aşağıdaki yöntemi kullandım. Orijinal içerikte birden fazla markdown dokümanında önemli değişiklikler olduğunda bu yöntemi kullanmanızı öneririm. Sadece birkaç çeviri dosyasını güncellemeniz gerekiyorsa, o dosyaları manuel silip sonra `-a` yöntemini kullanmak daha verimlidir.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "es" -u
Warning: The update command will delete all existing translations for 'es' and re-translate everything.
Do you want to continue? Type 'yes' to proceed: yes
Proceeding with update...
Translating images: 100%|████████████████████████████████████████████| 150/150 [43:46<00:00, 15.55s/it]
Translating markdown files: 100%|███████████████████████████████████| 95/95 [1:40:27<00:00, 125.62s/it]
```

### 6. Sadece Resimleri Çevirme

Projede sadece resim dosyalarını çevirmek için `-img` seçeneğini kullanın:

```bash
translate -l "ko" -img
```

Bu komut, sadece resimleri Korece’ye çevirir, markdown dosyalarına dokunmaz.

### 7. Sadece Markdown Dosyalarını Çevirme

Projede sadece markdown dosyalarını çevirmek için `-md` seçeneğini kullanın:

```bash
translate -l "ko" -md
```

### 8. Çevrilen Dosyalarda Hata Kontrolü

Çevrilen dosyalarda hata kontrolü yapmak ve gerekirse çeviriyi tekrar denemek için `-chk` seçeneğini kullanın:

```bash
translate -l "ko" -chk
```

Bu komut, çevrilmiş markdown dosyalarını tarar ve hata olan dosyalar için çeviriyi tekrar dener.

#### Phi-3 CookBook Üzerinde Örnek

**Phi-3 CookBook**’ta, Korece dosyalardaki çeviri hatalarını kontrol etmek ve sorunlu dosyalar için otomatik olarak çeviriyi tekrar denemek için aşağıdaki yöntemi kullandım.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko" -chk 
Checking translated files for errors in ko...
Checking files for ko: 100%|██████████████████████████████████████████████████| 95/95 [00:01<00:00, 65.47file/s]
Retrying vsc-extension-quickstart.md for ko:   0%|                                     | 0/17 [00:00<?, ?file/s] 
```

Bu seçenek çeviri hatalarını kontrol eder. Şu anda, orijinal ve çevrilmiş dosyalar arasındaki satır sonu farkı altıdan fazla ise dosya çeviri hatası olarak işaretlenir. Gelecekte bu kriteri daha esnek hale getirmeyi planlıyorum.

Örneğin, bu yöntem eksik parçaları veya bozuk çevirileri tespit etmek için faydalıdır ve bu dosyalar için çeviriyi otomatik olarak tekrar dener.

Ancak, hangi dosyaların sorunlu olduğunu zaten biliyorsanız, o dosyaları manuel silmek ve `-a` option to re-translate them.

### 9. Debug Mode

To enable detailed logging for troubleshooting, use the `-d` seçeneğini kullanmak daha verimlidir:

```bash
translate -l "ko" -d
```

Bu komut, çeviriyi hata ayıklama modunda çalıştırır ve çeviri sürecinde sorunları tespit etmenize yardımcı olacak ek günlük bilgisi sağlar.

#### Phi-3 CookBook Üzerinde Örnek

**Phi-3 CookBook**’ta, markdown dosyalarındaki çok sayıda link içeren çeviriler formatlama hatalarına, kırık çevirilere ve göz ardı edilen satır sonlarına neden olduğunda bir sorunla karşılaştım. Sorunu teşhis etmek için çeviri sürecinin nasıl işlediğini görmek amacıyla `-d` seçeneğini kullandım.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "ko" -d
DEBUG:openai._base_client:Request options: {'method': 'post', 'url': '/chat/completions', 'headers': {'api-key': 'af04e0bea45747d8a7b8c131c1971044'}, 'files': None, 'json_data': {'messages': [{'role': 'user', 'content': "Translate the following text to ko. NEVER ADD ANY EXTRA CONTENT OUTSIDE THE TRANSLATION. TRANSLATE ONLY WHAT IS GIVEN TO YOU.. MAINTAIN MARKDOWN FORMAT\n\n# Phi-3 Cookbook: Hands-On Examples with Microsoft's Phi-3 Models [![Open and use the samples in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phi-3cookbook) [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%
...
```

### 10. Tüm Dillerde Çeviri

Projeyi desteklenen tüm dillere çevirmek isterseniz, all anahtar kelimesini kullanın.

> [!WARNING]
> Tüm dilleri aynı anda çevirmek, projenin büyüklüğüne bağlı olarak önemli zaman alabilir. Örneğin, **Phi-3 CookBook**’un İspanyolca çevirisi yaklaşık 2 saat sürdü. Ölçek göz önüne alındığında, 20 dili tek bir kişinin yönetmesi pratik değildir. Çalışmanın birden fazla katkıcı arasında bölünmesi, her birinin bir veya iki dili yönetmesi ve çevirilerin kademeli olarak güncellenmesi önerilir.

```bash
translate -l "all"
```

Bu komut projeyi mevcut tüm dillere çevirir. Devam ederseniz, projenin büyüklüğüne bağlı olarak çeviri önemli zaman alabilir.

> [!TIP]
>
> ### Güncellenmesi Gereken Dosyaların Silinmesi
> Pull Request’te son değişiklikleri güncellemek için ilk adım, farklı dil çeviri klasörlerinde bulunan ilgili dosyanın tüm mevcut versiyonlarını silmektir. Aşağıdaki komutla, belirli isimdeki tüm dosyaları çeviri klasörleri içinde topluca silebilirsiniz.
>
> ### Windows Üzerinde:
> 1. **Komut İstemi Kullanarak**:
>    - Komut İstemini açın.
>    - `cd` komutuyla dosyaların bulunduğu klasöre gidin.
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
>   - Use the `find` komutu:
>     ```bash
>     find . -type f -name "*filename*" -delete
>     ```
>     `filename` with the specific name.
>
> Always double-check the files before deleting to avoid accidental loss. 
>
> Once you have deleted the files which need to be replace simply rerun your `translate -l` komutunu en son dosya değişikliklerini güncellemek için kullanın.

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalar veya yanlış yorumlamalardan sorumlu değiliz.