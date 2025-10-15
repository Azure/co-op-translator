<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "20943a46b11c6d74814f41a817a6db4c",
  "translation_date": "2025-10-15T03:11:22+00:00",
  "source_file": "getting_started/command-line-guide/translator-your-project.md",
  "language_code": "tr"
}
-->
# Projenizi Co-op Translator ile Çevirin

**Co-op Translator**, projenizdeki markdown ve görsel dosyalarını birden fazla dile çevirmeye yardımcı olan bir komut satırı aracı (CLI)dır. Bu bölümde aracın nasıl kullanılacağı, çeşitli CLI seçenekleri ve farklı kullanım senaryoları için örnekler anlatılmaktadır.

> [!NOTE]
> Tüm komutların ve detaylı açıklamalarının tam listesi için lütfen [Komut referansı](./command-reference.md) sayfasına bakın.

---

## Örnek Senaryolar ve Komutlar

**Co-op Translator** için sık karşılaşılan bazı kullanım senaryoları ve uygun komutlar aşağıda yer almaktadır.

### 1. Temel Çeviri (Tek Dil)

Tüm projenizi (markdown dosyaları ve görseller) tek bir dile, örneğin Korece'ye çevirmek için aşağıdaki komutu kullanın:

```bash
translate -l "ko"
```

Bu komut, tüm markdown ve görsel dosyalarını Korece'ye çevirecek ve mevcut çevirileri silmeden yeni çeviriler ekleyecektir.

> [!TIP]
>
> **Co-op Translator**'da hangi dil kodlarının mevcut olduğunu görmek ister misiniz? Daha fazla bilgi için depo içindeki [Desteklenen Diller](https://github.com/Azure/co-op-translator#supported-languages) bölümünü ziyaret edin.

#### Phi-3 CookBook Üzerinde Örnek

**Phi-3 CookBook**'ta, mevcut markdown dosyaları ve görseller için Korece çevirisini eklemek amacıyla aşağıdaki yöntemi kullandım.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko"
Translating images: 100%|███████████████████████████████████████████████████| 276/276 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 153/153 [1:43:07<00:00, 241.31s/it]
```

### 2. Birden Fazla Dile Çeviri

Projenizi birden fazla dile (örneğin İspanyolca, Fransızca ve Almanca) çevirmek için bu komutu kullanın:

```bash
translate -l "es fr de"
```

Bu komut, projeyi İspanyolca, Fransızca ve Almanca'ya çevirecek ve mevcut çevirileri silmeden yeni çeviriler ekleyecektir.

#### Phi-3 CookBook Üzerinde Örnek

**Phi-3 CookBook**'ta, en son commitleri yansıtmak için güncellemeleri çektikten sonra, yeni eklenen markdown dosyaları ve görselleri çevirmek için aşağıdaki yöntemi kullandım.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko ja zh tw es fr" -a
Translating images: 100%|███████████████████████████████████████████████████| 273/273 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 6/6 [24:07<00:00, 241.31s/it]
```

> [!NOTE]
> Genellikle bir seferde tek bir dili çevirmek önerilir, ancak bu gibi özel değişikliklerin eklenmesi gereken durumlarda birden fazla dili aynı anda çevirmek verimli olabilir.

### 3. Çevirileri Güncelleme (Mevcut Çevirileri Siler)

Mevcut çevirileri güncellemek (yani mevcut çevirileri silip yenileriyle değiştirmek) için `-u` seçeneğini kullanın. Bu, belirtilen dillerdeki tüm mevcut çevirileri silecek ve yeniden çevirecektir.

```bash
translate -l "ko" -u
```

Uyarı: Bu komut, mevcut çevirileri silmeden önce sizden onay isteyecektir.

#### Phi-3 CookBook Üzerinde Örnek

**Phi-3 CookBook**'ta, İspanyolca'daki tüm çevrilmiş dosyaları güncellemek için aşağıdaki yöntemi kullandım. Orijinal içerikte birden fazla markdown belgesinde önemli değişiklikler varsa bu yöntemi kullanmanızı öneririm. Sadece birkaç çevrilmiş markdown dosyasını güncellemek gerekiyorsa, o dosyaları manuel olarak silip ardından `-a` yöntemiyle güncellenmiş çevirileri eklemek daha verimli olur.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "es" -u
Warning: The update command will delete all existing translations for 'es' and re-translate everything.
Do you want to continue? Type 'yes' to proceed: yes
Proceeding with update...
Translating images: 100%|████████████████████████████████████████████| 150/150 [43:46<00:00, 15.55s/it]
Translating markdown files: 100%|███████████████████████████████████| 95/95 [1:40:27<00:00, 125.62s/it]
```

### 5. Sadece Görselleri Çevirme

Projenizde sadece görsel dosyalarını çevirmek için `-img` seçeneğini kullanın:

```bash
translate -l "ko" -img
```

Bu komut, sadece görselleri Korece'ye çevirecek ve markdown dosyalarına dokunmayacaktır.

### 6. Sadece Markdown Dosyalarını Çevirme

Projenizde sadece markdown dosyalarını çevirmek için `-md` seçeneğini kullanın:

```bash
translate -l "ko" -md
```

#### Phi-3 CookBook Üzerinde Örnek

**Phi-3 CookBook**'ta, Korece dosyalardaki çeviri hatalarını kontrol etmek ve tespit edilen sorunlu dosyalar için otomatik olarak yeniden çeviri yapmak amacıyla aşağıdaki yöntemi kullandım.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko" -chk 
Checking translated files for errors in ko...
Checking files for ko: 100%|██████████████████████████████████████████████████| 95/95 [00:01<00:00, 65.47file/s]
Retrying vsc-extension-quickstart.md for ko:   0%|                                     | 0/17 [00:00<?, ?file/s] 
```

Bu seçenek çeviri hatalarını kontrol eder. Şu anda, orijinal ve çevrilmiş dosyalar arasındaki satır sonu farkı altıdan fazlaysa dosya çeviri hatası olarak işaretleniyor. Gelecekte bu kriteri daha esnek hale getirmeyi planlıyorum.

Örneğin, bu yöntem eksik bölümleri veya bozulmuş çevirileri tespit etmek için faydalıdır ve bu dosyalar için otomatik olarak yeniden çeviri yapılır.

Ancak, sorunlu dosyaların hangileri olduğunu zaten biliyorsanız, o dosyaları manuel olarak silip `-a` seçeneğiyle yeniden çevirmek daha verimli olur.

### 8. Hata Ayıklama Modu

Sorunları gidermek için ayrıntılı günlük kaydını etkinleştirmek için `-d` seçeneğini kullanın:

```bash
translate -l "ko" -d
```

Bu komut, çeviriyi hata ayıklama modunda çalıştırır ve çeviri sürecinde karşılaşılan sorunları tespit etmenize yardımcı olacak ek günlük bilgileri sağlar.

#### Phi-3 CookBook Üzerinde Örnek

**Phi-3 CookBook**'ta, markdown dosyalarında çok fazla bağlantı olduğunda çevirilerde biçimlendirme hataları (bozuk çeviriler, göz ardı edilen satır sonları gibi) yaşadım. Bu sorunu teşhis etmek için çeviri sürecinin nasıl işlediğini görmek amacıyla `-d` seçeneğini kullandım.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "ko" -d
DEBUG:openai._base_client:Request options: {'method': 'post', 'url': '/chat/completions', 'headers': {'api-key': 'af04e0bea45747d8a7b8c131c1971044'}, 'files': None, 'json_data': {'messages': [{'role': 'user', 'content': "Translate the following text to ko. NEVER ADD ANY EXTRA CONTENT OUTSIDE THE TRANSLATION. TRANSLATE ONLY WHAT IS GIVEN TO YOU.. MAINTAIN MARKDOWN FORMAT\n\n# Phi-3 Cookbook: Hands-On Examples with Microsoft's Phi-3 Models [![Open and use the samples in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phi-3cookbook) [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%
...
```

### 9. Tüm Dillere Çeviri

Projeyi tüm desteklenen dillere çevirmek istiyorsanız, all anahtar kelimesini kullanın.

> [!WARNING]
> Tüm dilleri aynı anda çevirmek, projenin boyutuna bağlı olarak oldukça uzun sürebilir. Örneğin, **Phi-3 CookBook**'u İspanyolca'ya çevirmek yaklaşık 2 saat sürdü. Bu ölçekle, 20 dili tek bir kişinin yönetmesi pratik değildir. Çeviri işini birden fazla katkıcıya bölmek, her birinin bir veya iki dili yönetmesi ve çevirileri kademeli olarak güncellemesi önerilir.

```bash
translate -l "all"
```

Bu komut, projeyi tüm mevcut dillere çevirecektir. Devam ederseniz, çeviri projenin boyutuna bağlı olarak oldukça uzun sürebilir.

> [!TIP]
>
> ### Çevrilmiş Dosyaları Manuel Olarak Silmek (İsteğe Bağlı)
> Artık çevrilmiş dosyalar, kaynak dosya güncellendiğinde otomatik olarak algılanıp temizleniyor.
>
> Ancak, bir çeviriyi manuel olarak güncellemek isterseniz - örneğin, belirli bir dosyayı yeniden çevirmek veya sistem davranışını geçersiz kılmak için - aşağıdaki komutu kullanarak dosyanın tüm dil klasörlerindeki sürümlerini silebilirsiniz.
>
> ### Windows'ta:
> 1. **Komut İstemcisi ile**:
>    - Komut İstemcisini açın.
>    - `cd` komutunu kullanarak dosyaların bulunduğu klasöre gidin.
>    - Dosyaları silmek için aşağıdaki komutu kullanın:
>      ```
>      del /s *filename*
>      ```
>      `filename` kısmını aradığınız dosya adıyla değiştirin. `/s` seçeneği alt klasörlerde de arama yapar.
>
> 2. **PowerShell ile**:
>    - PowerShell'i açın.
>    - Şu komutu çalıştırın:
>      ```powershell
>      Get-ChildItem -Path "C:\YourPath" -Filter "*filename*" -Recurse | Remove-Item -Force
>      ```
>      `"C:\YourPath"` kısmını klasör yolu ile, `filename` kısmını ise dosya adıyla değiştirin.
>
> ### macOS/Linux'ta:
> 1. **Terminal ile**:
>   - Terminali açın.
>   - `cd` ile dizine gidin.
>   - `find` komutunu kullanın:
>     ```bash
>     find . -type f -name "*filename*" -delete
>     ```
>     `filename` kısmını dosya adıyla değiştirin.
>
> Silmeden önce dosyaları iki kez kontrol edin, yanlışlıkla veri kaybı yaşamamak için. 
>
> Silinmesi gereken dosyaları sildikten sonra, en güncel dosya değişikliklerini güncellemek için `translate -l` komutunuzu tekrar çalıştırmanız yeterlidir.

---

**Feragatname**:
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerde hata veya yanlışlıklar olabileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından doğabilecek herhangi bir yanlış anlama veya yanlış yorumdan sorumlu değiliz.