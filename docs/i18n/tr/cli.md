# CLI Referansı

Co-op Translator şu komut satırı giriş noktalarını kurar:

- `translate`
- `evaluate`
- `migrate-links`
- `co-op-review`
- `co-op-translator-mcp`

`translate`, `evaluate`, `migrate-links` ve `co-op-review` komutları, çağrılan betik adına göre komut uygulamasını seçen `co_op_translator.__main__` aracılığıyla gönderilir. MCP sunucusu doğrudan `co_op_translator.mcp.server` kullanır.

CLI, Python API ve MCP arasında karar veriyorsanız, [İş Akışınızı Seçin](workflows.md) ile başlayın.

## Konsol Çıkışı

Etkileşimli terminaller, komut başlığı, ilerleme ve özetler için Rich biçemlendirmesini kullanır. CI ve etkileşimsiz çıktılar otomatik olarak düz metne döner.

Düz çıktı zorlamak için `CO_OP_TRANSLATOR_OUTPUT_STYLE=plain` ayarlayın veya Rich çıktıyı zorlamak için `CO_OP_TRANSLATOR_OUTPUT_STYLE=rich` ayarlayın. Canlı ilerleme çubuklarını bastırırken özetleri tutmak için `CO_OP_TRANSLATOR_NO_PROGRESS=1` ayarlayın.

Başka bir sistem makine tarafından okunabilir ilerlemeye ihtiyaç duyduğunda `translate --json-events progress.ndjson` kullanın
makine tarafından okunabilir ilerleme. CLI insanlara yönelik çıktıyı görüntülemeye devam ederken,
NDJSON dosyası, `co-op.translation.event.v1` sürümlü olayları alır ve
sabit alanlar, ör. `type`, `stage_key`, `completed`, `total`, ve
`current_path`.

## İlk Kez CLI Akışı

Bir terminalden Co-op Translator kullanıyorsanız buradan başlayın:

1. [Configuration](configuration.md) bölümünde açıklandığı gibi bir LLM sağlayıcısı yapılandırın.
2. Çevirmek istediğiniz içerik türünü seçin.
3. Öncelikle odaklanmış bir komut çalıştırın; örneğin yalnızca Markdown çevirisi.
4. Büyük depo değişikliklerinden önce `--dry-run` kullanın.
5. Yapıyı ve güncelliği kontrol etmek için çeviriden sonra `co-op-review` kullanın.

| Hedef | Başlamak için komut |
| --- | --- |
| Markdown belgelerini çevirin | `translate -l "ko" -md` |
| Not defterlerini çevirin | `translate -l "ko" -nb` |
| Görüntü metnini çevirin | `translate -l "ko" -img` |
| Dosya yazmadan çalışmayı önizleyin | `translate -l "ko" -md --dry-run` |
| Mevcut çevirileri gözden geçirin | `co-op-review -l "ko"` |
| Not defteri ve Markdown bağlantılarını güncelleyin | `migrate-links -l "ko" --dry-run` |
| Araçları bir MCP istemcisine açın | CLI komutlarını doğrudan çalıştırmak yerine [MCP Sunucusu](mcp.md) yapılandırın. |

## translate

Markdown dosyalarını, not defterlerini ve görüntü metnini bir veya daha fazla hedef dile çevirin.

```bash
translate -l "ko ja fr"
```

### Yaygın örnekler

Sadece Markdown'u çevirin:

```bash
translate -l "de" -md
```

Sadece not defterlerini çevirin:

```bash
translate -l "zh-CN" -nb
```

Markdown ve görselleri çevirin:

```bash
translate -l "pt-BR" -md -img
```

Mevcut çevirileri silip yeniden oluşturarak güncelleyin:

```bash
translate -l "ko" -u
```

Etkileşimli istemler olmadan çalıştırın:

```bash
translate -l "ko ja" -md -y
```

Günlükleri kaydedin:

```bash
translate -l "ko" -s
```

Yapılandırılmış ilerleme olayları yazın:

```bash
translate -l "ko ja" -md --json-events progress.ndjson
```

### Seçenekler

| Seçenek | Gerekli | Açıklama |
| --- | --- | --- |
| `-l`, `--language-codes` | Evet | Boşlukla ayrılmış dil kodları, örneğin `"es fr de"` veya `"all"`. |
| `-r`, `--root-dir` | Hayır | Proje kökü. Varsayılan olarak geçerli dizindir. |
| `-u`, `--update` | Hayır | Seçilen diller için mevcut çevirileri siler ve yeniden oluşturur. |
| `-img`, `--images` | Hayır | Sadece görsel dosyalarını çevir. |
| `-md`, `--markdown` | Hayır | Sadece Markdown dosyalarını çevir. |
| `-nb`, `--notebook` | Hayır | Sadece Jupyter notebook dosyalarını çevir. |
| `-d`, `--debug` | Hayır | Konsolda hata ayıklama günlüklerini etkinleştir. |
| `-s`, `--save-logs` | Hayır | DEBUG seviyesindeki günlükleri `<root-dir>/logs/` altında kaydet. |
| `--json-events` | Hayır | Makine tarafından okunabilir çeviri ilerleme olaylarını NDJSON olarak yazar. |
| `-x`, `--fix` | Hayır | Önceki değerlendirme sonuçlarına göre düşük güvene sahip Markdown dosyalarını yeniden çevirir. |
| `-c`, `--min-confidence` | Hayır | `--fix` için güven eşiği. Varsayılan `0.7`. |
| `--add-disclaimer`, `--no-disclaimer` | Hayır | Makine çevirisi feragatnamelerini ekler veya bastırır. CLI'da varsayılan olarak etkinleştirilmiştir. |
| `-f`, `--fast` | Hayır | Kullanımdan kaldırılmış hızlı görsel modu. |
| `-y`, `--yes` | Hayır | İstekleri otomatik onaylar, CI için kullanışlıdır. |
| `--repo-url` | Hayır | README diller tablosundaki sparse-checkout önerisi için kullanılan depo URL'si. |
| `--migrate-language-folders` | Hayır | Örneğin `cn` veya `tw` gibi eski takma ad klasörlerini kanonik BCP 47 klasörlerine yeniden adlandırır. |
| `--dry-run` | Hayır | Dosya yazmadan dil klasörü göçünü ve çeviri tahminlerini önizler. |

Eğer bir tür bayrağı belirtilmezse, `translate` Markdown, notebook'ları ve görselleri işler. Görsel çevirisi Azure AI Vision yapılandırması gerektirir.

## evaluate

Bir dil için çevrilmiş Markdown kalitesini değerlendirin.

!!! warning "Deneysel"
    `evaluate` deneysel bir özelliktir. Kural tabanlı ve LLM tabanlı kalite kontrolleri kullanabilir, değerlendirme sonuçlarını çeviri meta verilerine yazar ve puanlama modeli ile meta veri davranışı değişebilir.

```bash
evaluate -l "ko"
```

### Yaygın örnekler

Daha katı bir düşük güven eşiği kullanın:

```bash
evaluate -l "es" -c 0.8
```

Sadece kural tabanlı kontrolleri çalıştırın:

```bash
evaluate -l "fr" -f
```

Sadece LLM tabanlı kontrolleri çalıştırın:

```bash
evaluate -l "ja" -D
```

### Seçenekler

| Seçenek | Gerekli | Açıklama |
| --- | --- | --- |
| `-l`, `--language-code` | Evet | Değerlendirilecek tek dil kodu. Takma ad kodları normalleştirilir. |
| `-r`, `--root-dir` | Hayır | Proje kökü. Varsayılan olarak geçerli dizindir. |
| `-c`, `--min-confidence` | Hayır | Düşük güvene sahip çevirileri listelerken kullanılan eşik değeri. Varsayılan `0.7`. |
| `-d`, `--debug` | Hayır | Hata ayıklama günlük kaydını etkinleştir. |
| `-s`, `--save-logs` | Hayır | DEBUG seviyesindeki günlükleri `<root-dir>/logs/` altında kaydet. |
| `-f`, `--fast` | Hayır | Sadece kural tabanlı değerlendirme. |
| `-D`, `--deep` | Hayır | Yalnızca LLM tabanlı değerlendirme. |

Varsayılan olarak `evaluate` hem kural tabanlı hem de LLM tabanlı değerlendirmeyi kullanır. Sonuçlar çeviri meta verilerine yazılır ve konsolda özetlenir.

## co-op-review

API kimlik bilgileri olmadan deterministik çeviri bakım kontrolleri çalıştırın.

!!! note "Beta"
    `co-op-review` beta bir deterministik inceleme komutudur. Model sağlayıcılarını çağırmaz veya dosya yazmaz, ancak yaptığı kontroller ve sorun çıktı şeması gelişebilir.

```bash
co-op-review -l "ko"
```

### Yaygın örnekler

Geçerli dizinden Korece ve Japonca çevirilerini inceleyin:

```bash
co-op-review -l "ko ja"
```

Belirli bir proje kökünü inceleyin:

```bash
co-op-review -l "fr" -r ./my-course
```

README'e özel bir çeviri sonrası sadece README'i inceleyin:

```bash
translate -l "ko" --readme-only -y
co-op-review -l "ko" --readme-only --format github
```

`--readme-only` diğer belgeleri ve iç içe README'leri yoksayar. Kök
`README.md` eksiktir. `--changed-from` ile birleştirildiğinde, sadece README'i inceler
kaynak dosya değiştiğinde. README'e özel çeviri, kaynak README'i
değiştirmeden bırakır; paylaşılan bölüm işaretleri dahil.

Yalnızca bir temel referansa karşı değişen kaynak dosyaları inceleyin:

```bash
co-op-review -l "ko" --changed-from origin/main
```

CI özetleri için GitHub usulü Markdown çıktısı yazdırın:

```bash
co-op-review -l "ko ja" --changed-from origin/main --format github
```

### Seçenekler

| Seçenek | Gerekli | Açıklama |
| --- | --- | --- |
| `-l`, `--language-code` | Hayır | İncelenecek dil kodu. Birden çok kere veya boşlukla ayrılmış değer olarak verilebilir. Varsayılan olarak bulunan tüm çeviri dillerini alır. |
| `-r`, `--root-dir` | Hayır | Proje kökü. Varsayılan olarak geçerli dizindir. |
| `--changed-from` | Hayır | İncelemeyi değişen kaynak dosyalarla sınırlamak için kullanılan Git ref'i. |
| `--readme-only` | Hayır | Yalnızca kök `README.md` çevirisini inceleyin. |
| `--format` | Hayır | Çıktı formatı: `text` veya `github`. Varsayılan `text`. |

`co-op-review` şu anda eksik çevrilmiş dosyaları, eksik veya güncelliğini yitirmiş çeviri meta verilerini, Markdown frontmatter ve kod bloğu bütünlüğünü, geçersiz çevrilmiş not defteri JSON'unu ve eksik yerel Markdown veya resim bağlantısı hedeflerini kontrol eder. Eksik bağlantılar varsayılan olarak uyarıdır; yapısal ve tazelik sorunları komutu başarısız kılar.

## co-op-translator-mcp

Ajanlar, editörler ve MCP-uyumlu istemciler için Co-op Translator MCP sunucusunu çalıştırın.

```bash
co-op-translator-mcp
```

Varsayılan taşıma `stdio`'dur. İstemci yapılandırması, araçlar, kaynaklar ve güvenlik notları için [MCP Server](mcp.md) kılavuzuna bakın.

### Seçenekler

| Seçenek | Gerekli | Açıklama |
| --- | --- | --- |
| `--transport` | Hayır | MCP taşıması: `stdio`, `streamable-http` veya `sse`. Varsayılan `stdio`. |

## migrate-links

Çevrilmiş Markdown dosyalarını yeniden işleyin ve not defteri bağlantılarını, mevcut olduğunda çevrilmiş not defterlerine işaret edecek şekilde güncelleyin.

```bash
migrate-links -l "ko ja"
```

### Yaygın örnekler

Bağlantı güncellemelerini önizleyin:

```bash
migrate-links -l "ko" --dry-run
```

Tüm desteklenen dilleri onaylamadan işleyin:

```bash
migrate-links -l "all" -y
```

Yalnızca çevrilmiş not defterleri mevcut olduğunda bağlantıları yeniden yazın:

```bash
migrate-links -l "ko" --no-fallback-to-original
```

### Seçenekler

| Seçenek | Gerekli | Açıklama |
| --- | --- | --- |
| `-l`, `--language-codes` | Evet | Boşlukla ayrılmış dil kodları veya "all". |
| `-r`, `--root-dir` | Hayır | Proje kökü. Varsayılan geçerli dizindir. |
| `--image-dir` | Hayır | Kök dizine göre çevrilmiş resim dizini. Varsayılan `translated_images`. |
| `--dry-run` | Hayır | Güncelleme yazmadan değişecek dosyaları göster. |
| `--fallback-to-original`, `--no-fallback-to-original` | Hayır | Çevrilmiş not defterleri yoksa orijinal not defteri bağlantılarını kullan. Varsayılan olarak etkin. |
| `-d`, `--debug` | Hayır | Hata ayıklama kaydını etkinleştir. |
| `-s`, `--save-logs` | Hayır | DEBUG düzeyindeki günlükleri `<root-dir>/logs/` altında kaydet. |
| `-y`, `--yes` | Hayır | Tüm diller işlenirken istemleri otomatik onayla. |

## Ortam

Bir komut sağlayıcı kimlik bilgileri gerektirdiğinde, bu sağlayıcı setlerinden birini yapılandırın. `translate --dry-run` ve `co-op-review` sağlayıcı kimlik bilgileri gerektirmez:

```bash
# Azure OpenAI
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"

# Veya OpenAI
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"

# Veya Anthropic
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

Resim çevirisi ayrıca Azure AI Vision gerektirir:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

## Çıktı düzeni

Metin çevirileri şu konuma yazılır:

```text
translations/<language-code>/<original-path>
```

Çevrilmiş resim çıktısı şu konuma yazılır:

```text
translated_images/<language-code>/<original-path>
```

Örneğin, `README.md` ve `docs/setup.md` dosyalarını Korece'ye çevirmek şu sonucu üretir:

```text
translations/ko/README.md
translations/ko/docs/setup.md
```

## Kopyala-Yapıştır CLI Örnekleri

Markdown'u üç dile çevirin:

```bash
translate -l "ko ja fr" -md
```

Sadece not defterlerini çevirin:

```bash
translate -l "zh-CN" -nb
```

Sadece resimleri çevirin:

```bash
translate -l "pt-BR" -img
```

Dosyaları yazmadan Markdown çevirisini önizleyin:

```bash
translate -l "de es" -md --dry-run
```

Düşük güven skorlu Markdown çevirilerini onarın:

```bash
evaluate -l "ko" -c 0.8
translate -l "ko" --fix -c 0.8 -md
```

CI dostu Markdown çevirisi çalıştırın:

```bash
translate -l "ko ja" -md -y -s
```

Çevrilmiş çıktıyı inceleyin:

```bash
co-op-review -l "ko ja"
```

Bağlantı geçişini önizleyin:

```bash
migrate-links -l "ko" --dry-run
```