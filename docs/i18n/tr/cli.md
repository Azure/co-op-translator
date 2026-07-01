# CLI Referansı

Co-op Translator şu komut satırı giriş noktalarını kurar:

- `translate`
- `evaluate`
- `migrate-links`
- `co-op-review`
- `co-op-translator-mcp`

`translate`, `evaluate`, `migrate-links` ve `co-op-review` komutları, çağrılan betik adına göre komut uygulamasını seçen `co_op_translator.__main__` aracılığıyla yönlendirilir. MCP sunucusu doğrudan `co_op_translator.mcp.server` kullanır.

CLI, Python API ve MCP arasında karar veriyorsanız, [Çalışma Akışınızı Seçin](workflows.md) ile başlayın.

## İlk Kez CLI Akışı

Terminalden Co-op Translator kullanıyorsanız buradan başlayın:

1. [Configuration](configuration.md) altında açıklandığı gibi bir LLM sağlayıcısı yapılandırın.
2. Çevirmek istediğiniz içerik türünü seçin.
3. Önce Markdown yalnız çeviri gibi odaklanmış bir komut çalıştırın.
4. Büyük depo değişikliklerinden önce `--dry-run` kullanın.
5. Çeviriden sonra yapı ve tazelik kontrolü için `co-op-review` kullanın.

| Amaç | Başlangıç komutu |
| --- | --- |
| Translate Markdown documents | `translate -l "ko" -md` |
| Translate notebooks | `translate -l "ko" -nb` |
| Translate image text | `translate -l "ko" -img` |
| Preview work without writing files | `translate -l "ko" -md --dry-run` |
| Review existing translations | `co-op-review -l "ko"` |
| Update notebook and Markdown links | `migrate-links -l "ko" --dry-run` |
| Expose tools to an MCP client | Configure the [MCP Server](mcp.md) instead of running CLI commands directly. |

## translate

Translate Markdown files, notebooks, and image text into one or more target languages.

```bash
translate -l "ko ja fr"
```

### Yaygın Örnekler

Sadece Markdown çevir:

```bash
translate -l "de" -md
```

Sadece notebook'ları çevir:

```bash
translate -l "zh-CN" -nb
```

Markdown ve resimleri çevir:

```bash
translate -l "pt-BR" -md -img
```

Mevcut çevirileri silip yeniden oluşturarak güncelle:

```bash
translate -l "ko" -u
```

Etkileşimli istemler olmadan çalıştır:

```bash
translate -l "ko ja" -md -y
```

Günlükleri kaydet:

```bash
translate -l "ko" -s
```

### Seçenekler

| Seçenek | Gerekli | Açıklama |
| --- | --- | --- |
| `-l`, `--language-codes` | Yes | Boşlukla ayrılmış dil kodları, örneğin `"es fr de"`, veya `"all"`. |
| `-r`, `--root-dir` | No | Proje kökü. Varsayılan olarak geçerli dizindir. |
| `-u`, `--update` | No | Seçilen diller için mevcut çevirileri siler ve yeniden oluşturur. |
| `-img`, `--images` | No | Yalnızca görüntü dosyalarını çevirir. |
| `-md`, `--markdown` | No | Yalnızca Markdown dosyalarını çevirir. |
| `-nb`, `--notebook` | No | Yalnızca Jupyter notebook dosyalarını çevirir. |
| `-d`, `--debug` | No | Konsolda hata ayıklama günlüklemesini etkinleştirir. |
| `-s`, `--save-logs` | No | DEBUG düzeyindeki günlükleri `<root-dir>/logs/` altında kaydeder. |
| `-x`, `--fix` | No | Önceki değerlendirme sonuçlarına dayanarak düşük güvenilirlikli Markdown dosyalarını yeniden çevirir. |
| `-c`, `--min-confidence` | No | `--fix` için güven eşiği. Varsayılan `0.7`. |
| `--add-disclaimer`, `--no-disclaimer` | No | Makine çevirisi uyarılarını ekler veya bastırır. CLI'de varsayılan olarak etkin. |
| `-f`, `--fast` | No | Kullanımdan kaldırılmış hızlı görüntü modu. |
| `-y`, `--yes` | No | İstemleri otomatik onaylar, CI'da kullanışlıdır. |
| `--repo-url` | No | README diller tablosundaki sparse-checkout önerisi için kullanılan depo URL'si. |
| `--migrate-language-folders` | No | Örneğin `cn` veya `tw` gibi eski takma ad klasörlerini kanonik BCP 47 klasör adlarına yeniden adlandırır. |
| `--dry-run` | No | Dosya yazmadan dil klasörü göçünü ve çeviri tahminlerini önizler. |

Hiçbir tür bayrağı verilmemişse, `translate` Markdown, notebook'lar ve resimleri işler. Görüntü çevirisi Azure AI Vision yapılandırması gerektirir.

## evaluate

Evaluate translated Markdown quality for one language.

!!! warning "Deneysel"
    `evaluate` deneysel bir özelliktir. Kural tabanlı ve LLM tabanlı kalite kontrollerini kullanabilir, değerlendirme sonuçlarını çeviri meta verisine yazar ve puanlama modeli ile meta veri davranışı değişebilir.

```bash
evaluate -l "ko"
```

### Yaygın Örnekler

Daha sıkı bir düşük güven eşiği kullan:

```bash
evaluate -l "es" -c 0.8
```

Sadece kural tabanlı kontrolleri çalıştır:

```bash
evaluate -l "fr" -f
```

Sadece LLM tabanlı kontrolleri çalıştır:

```bash
evaluate -l "ja" -D
```

### Seçenekler

| Seçenek | Gerekli | Açıklama |
| --- | --- | --- |
| `-l`, `--language-code` | Yes | Değerlendirilecek tek bir dil kodu. Takma ad kodlar normalleştirilir. |
| `-r`, `--root-dir` | No | Proje kökü. Varsayılan olarak geçerli dizindir. |
| `-c`, `--min-confidence` | No | Düşük güven çevirilerini listelerken kullanılan eşik. Varsayılan `0.7`. |
| `-d`, `--debug` | No | Hata ayıklama günlüklemesini etkinleştirir. |
| `-s`, `--save-logs` | No | DEBUG düzeyindeki günlükleri `<root-dir>/logs/` altında kaydeder. |
| `-f`, `--fast` | No | Sadece kural tabanlı değerlendirme. |
| `-D`, `--deep` | No | Sadece LLM tabanlı değerlendirme. |

Varsayılan olarak `evaluate` hem kural tabanlı hem de LLM tabanlı değerlendirme kullanır. Sonuçlar çeviri meta verisine yazılır ve konsolda özetlenir.

## co-op-review

API kimlik bilgisi olmadan deterministik çeviri bakım kontrollerini çalıştırın.

!!! note "Beta"
    `co-op-review` beta bir deterministik denetleme komutudur. Model sağlayıcılarını çağırmaz veya dosya yazmaz, ancak kontrolleri ve sorun çıktı şeması zamanla değişebilir.

```bash
co-op-review -l "ko"
```

### Yaygın Örnekler

Geçerli dizinden Korece ve Japonca çevirilerini denetle:

```bash
co-op-review -l "ko ja"
```

Belirli bir proje kökünü denetle:

```bash
co-op-review -l "fr" -r ./my-course
```

Sadece bir temel ref'e karşı değişmiş kaynak dosyaları denetle:

```bash
co-op-review -l "ko" --changed-from origin/main
```

CI özetleri için GitHub biçimli Markdown çıktısı yazdır:

```bash
co-op-review -l "ko ja" --changed-from origin/main --format github
```

### Seçenekler

| Seçenek | Gerekli | Açıklama |
| --- | --- | --- |
| `-l`, `--language-code` | No | Denetlenecek dil kodu. Birden fazla kez veya boşlukla ayrılmış değer olarak verilebilir. Varsayılan tüm bulunan çeviri dilleridir. |
| `-r`, `--root-dir` | No | Proje kökü. Varsayılan olarak geçerli dizindir. |
| `--changed-from` | No | Denetimi değişen kaynak dosyalarla sınırlamak için kullanılan Git ref. |
| `--format` | No | Çıktı formatı: `text` veya `github`. Varsayılan `text`. |

`co-op-review` şu anda eksik çevrilmiş dosyalar, eksik veya güncelliğini yitirmiş çeviri meta verileri, Markdown frontmatter ve kod bloğu bütünlüğü, geçersiz çevrilmiş notebook JSON'u ve eksik yerel Markdown veya görüntü bağlantı hedefleri için kontroller yapar. Eksik bağlantılar varsayılan olarak uyarıdır; yapısal ve tazelik sorunları komutu başarısız kılar.

## co-op-translator-mcp

Run the Co-op Translator MCP server for agents, editors, and MCP-compatible clients.

```bash
co-op-translator-mcp
```

The default transport is `stdio`. See the [MCP Server](mcp.md) guide for client configuration, tools, resources, and safety notes.

### Options

| Option | Required | Description |
| --- | --- | --- |
| `--transport` | No | MCP transport: `stdio`, `streamable-http`, or `sse`. Defaults to `stdio`. |

## migrate-links

Reprocess translated Markdown files and update notebook links so they point to translated notebooks when available.

```bash
migrate-links -l "ko ja"
```

### Yaygın Örnekler

Bağlantı güncellemelerini önizle:

```bash
migrate-links -l "ko" --dry-run
```

Onay olmadan tüm desteklenen dilleri işle:

```bash
migrate-links -l "all" -y
```

Sadece çevrilmiş notebook'lar mevcut olduğunda bağlantıları yeniden yaz:

```bash
migrate-links -l "ko" --no-fallback-to-original
```

### Seçenekler

| Seçenek | Gerekli | Açıklama |
| --- | --- | --- |
| `-l`, `--language-codes` | Yes | Boşlukla ayrılmış dil kodları veya `"all"`. |
| `-r`, `--root-dir` | No | Proje kökü. Varsayılan olarak geçerli dizindir. |
| `--image-dir` | No | Kök dizine göre çevrilmiş resim dizini. Varsayılan `translated_images`. |
| `--dry-run` | No | Güncellemeleri yazmadan önce değişecek dosyaları gösterir. |
| `--fallback-to-original`, `--no-fallback-to-original` | No | Çevrilmiş notebook'lar eksik olduğunda orijinal notebook bağlantılarını kullanır. Varsayılan olarak etkin. |
| `-d`, `--debug` | No | Hata ayıklama günlüklemesini etkinleştirir. |
| `-s`, `--save-logs` | No | DEBUG düzeyindeki günlükleri `<root-dir>/logs/` altında kaydeder. |
| `-y`, `--yes` | No | Tüm diller işlenirken istemleri otomatik onaylar. |

## Environment

All commands require one configured LLM provider:

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
```

Image translation additionally requires Azure AI Vision:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

## Output layout

Text translations are written under:

```text
translations/<language-code>/<original-path>
```

Translated image output is written under:

```text
translated_images/<language-code>/<original-path>
```

For example, translating `README.md` and `docs/setup.md` into Korean produces:

```text
translations/ko/README.md
translations/ko/docs/setup.md
```

## Copy-Paste CLI Examples

Translate Markdown into three languages:

```bash
translate -l "ko ja fr" -md
```

Translate notebooks only:

```bash
translate -l "zh-CN" -nb
```

Translate images only:

```bash
translate -l "pt-BR" -img
```

Preview Markdown translation without writing files:

```bash
translate -l "de es" -md --dry-run
```

Repair low-confidence Markdown translations:

```bash
evaluate -l "ko" -c 0.8
translate -l "ko" --fix -c 0.8 -md
```

Run CI-friendly Markdown translation:

```bash
translate -l "ko ja" -md -y -s
```

Review translated output:

```bash
co-op-review -l "ko ja"
```

Preview link migration:

```bash
migrate-links -l "ko" --dry-run
```