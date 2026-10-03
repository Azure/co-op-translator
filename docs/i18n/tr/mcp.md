# MCP Sunucusu

Co-op Translator, ajanlar, düzenleyiciler ve MCP-uyumlu istemciler için bir Model Context Protocol sunucusu içerir.

Varsayılan yerel kurulum için, kullanıcılar ayrı bir sunucuyu elle çalıştırmazlar. MCP istemcilerini yapılandırır ve istemci, Co-op Translator araçlarına ihtiyaç duyduğunda `co-op-translator-mcp`'yi otomatik olarak `stdio` üzerinden başlatır.

Eğer CLI, Python API ve MCP arasında karar veriyorsanız, [İş Akışınızı Seçin](workflows.md) ile başlayın.

Bir ajan veya düzenleyici Co-op Translator'ı doğrudan çağırmalıysa MCP'yi kullanın:

| Kullanıcı hedefi | MCP araçları |
| --- | --- |
| Tek bir Markdown belgesini, notebook'u veya resmi çevir | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content` |
| Markdown veya notebook içeriğini host ajan modeli ile çevir | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Çıkış yolu seçildikten sonra çevrilmiş Markdown veya notebook bağlantılarını yeniden yaz | `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| CLI gibi tam bir depoyu çevir | `run_translation`, `translate_project` |
| LLM kimlik bilgileri olmadan çevrilmiş çıktıyı gözden geçir | `run_review` |
| Yetkinlikleri ve ortam durumunu incele | `get_api_overview`, `list_supported_languages`, `get_configuration_status` |

MCP sunucusu, [Python API](api.md)'de belgelenen aynı genel Python API'sini sarar. Sağlayıcı destekli araçlar, CLI ve Python API ile aynı yapılandırılmış sağlayıcıları kullanır. Ajan destekli araçlar, MCP host ajanı için çevrilecek parçaları hazırlar, ardından Co-op Translator son Markdown veya notebook'u yeniden oluşturmak için kullanılır.

## Adım 1: Co-op Translator'ı Yükleyin ve Yapılandırın

MCP istemcinizin kullanacağı Python ortamına Co-op Translator'ı yükleyin:

```bash
pip install co-op-translator
```

Bu depo üzerinden yerel geliştirme için, paketi düzenlenebilir modda yükleyin:

```bash
pip install -e .
```

MCP istemcinizin kullanacağı çeviri modunu seçin:

| Mod | Bunun için kullanın | Kimlik bilgileri |
| --- | --- | --- |
| Provider-backed | Co-op Translator `translate_markdown_content`, `translate_notebook_content`, `translate_image_content` veya `run_translation`'ı çağırır. | Çeviri için Azure OpenAI, OpenAI veya Anthropic gerekir. Görsel çevirisi ayrıca Azure AI Vision gerektirir. |
| Agent-assisted | MCP host ajanı, `start_markdown_agent_translation` veya `start_notebook_agent_translation` tarafından döndürülen parçaları çevirir. | Markdown veya notebook parçaları için Co-op Translator LLM sağlayıcı kimlik bilgisi gerekmez. Görsel çevirisi henüz ajan destekli mod tarafından kapsanmıyor. |

Eğer Codex veya Claude Code gibi bir ajan içinde Markdown veya notebook çevirisi ile başlıyorsanız, ajan destekli modla başlayın. Co-op Translator'ın kendisinin yapılandırılmış sağlayıcılarınızı çağırmasını istediğinizde, görselleri çevirirken veya CLI gibi depo düzeyinde çeviri çalıştırırken sağlayıcı destekli modu kullanın.

Sağlayıcı destekli iş akışları için bir sağlayıcı yapılandırın:

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

Sağlayıcı destekli görsel çevirisi ayrıca şunları gerektirir:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

!!! note
    Ajan destekli mod şu anda Markdown ve notebook Markdown hücrelerini kapsar. Görsel çevirisi hâlâ sağlayıcı destekli görsel hattını kullanır ve OCR ile düzen farkındalıklı render için Azure AI Vision gerektirir.

## Adım 2: MCP İstemcinizi Yapılandırın

Normal yerel `stdio` kurulumu için Co-op Translator'ı MCP istemci yapılandırmanıza ekleyin. İstemci, süreci otomatik olarak başlatıp durduracaktır.

Yüklü paket yapılandırması:

```json
{
  "mcpServers": {
    "co-op-translator": {
      "command": "co-op-translator-mcp",
      "args": []
    }
  }
}
```

Windows'ta kaynak çekme yapılandırması:

```json
{
  "mcpServers": {
    "co-op-translator": {
      "command": "C:\\Users\\you\\dev\\co-op-translator\\.venv\\Scripts\\python.exe",
      "args": ["-m", "co_op_translator.mcp.server"],
      "cwd": "C:\\Users\\you\\dev\\co-op-translator"
    }
  }
}
```

macOS veya Linux'ta kaynak çekme yapılandırması:

```json
{
  "mcpServers": {
    "co-op-translator": {
      "command": "/Users/you/dev/co-op-translator/.venv/bin/python",
      "args": ["-m", "co_op_translator.mcp.server"],
      "cwd": "/Users/you/dev/co-op-translator"
    }
  }
}
```

MCP istemci yapılandırmasını değiştirdikten sonra, yeni sunucuyu keşfedebilmesi için istemciyi yeniden başlatın veya yeniden yükleyin.

## Adım 3: İstemcide Sunucuyu Doğrulayın

MCP istemcisinden kullanılabilir araçları listelemesini isteyin veya önce salt-okunur yardımcı araçlardan birini çağırın:

```json
{
  "tool": "get_api_overview",
  "arguments": {}
}
```

İlk yapılması yararlı kontroller:

| Araç | Ne kontrol edilmeli |
| --- | --- |
| `get_api_overview` | Sunucunun ulaşılabilir olduğunu onaylar ve kullanılabilir iş akışlarını gösterir. |
| `list_supported_languages` | Paketlenmiş dil verilerinin yüklenebildiğini doğrular. |
| `get_configuration_status` | Gizli değerleri açığa çıkarmadan LLM ve Vision sağlayıcı kullanılabilirliğini doğrular. |

## Adım 4: Bir İş Akışı Seçin

### Bireysel Dosyaları veya Belgeleri Çevirin

MCP istemcisi zaten belge içeriğine veya bir görsel yoluna sahipse ve Co-op Translator yapılandırılmış çeviri sağlayıcılarını çağırmalıysa sağlayıcı destekli içerik araçlarını kullanın.

Markdown için:

1. `document`, `language_code` ve isteğe bağlı olarak `source_path` ile `translate_markdown_content`'i çağırın.
2. Çevrilmiş sonuç Co-op Translator çıktı düzenine yazılacaksa `rewrite_markdown_paths`'i çağırın.
3. İstemcinin nihai `content`'i yazmasına veya döndürmesine izin verin.

Notebook'lar için:

1. Notebook JSON'u ve `language_code` ile `translate_notebook_content`'i çağırın.
2. Çevrilmiş notebook bağlantılarının hedef yol için ayarlanması gerekiyorsa `rewrite_notebook_paths`'i çağırın.
3. Nihai notebook JSON'unu yazın veya döndürün.

Görseller için:

1. `image_path`, `language_code` ve isteğe bağlı `root_dir` veya `fast_mode` ile `translate_image_content`'i çağırın.
2. Döndürülen `data_base64` ve `mime_type`'ı okuyun.
3. `output_path` sağlandıysa, çevrilmiş görsel ayrıca o yola kaydedilir.

İçerik araçları proje keşfi, meta veri güncellemeleri, feragatnameler veya otomatik yol yeniden yazımı yapmaz. Eğer host ajanın Co-op Translator LLM sağlayıcı kimlik bilgileri olmadan Markdown veya notebook parçalarını çevirmesini istiyorsanız, aşağıdaki ajan destekli iş akışını kullanın.

### Host Ajan Modeli ile Çeviri

MCP host ajanının, örneğin bir kod yardımcısının, Co-op Translator için bir LLM sağlayıcısı yapılandırmak yerine çevrilmiş metni üretmesini istediğinizde ajan destekli araçları kullanın.

Sohbet tabanlı bir MCP istemcisinde genellikle araç JSON'unu kendiniz yazmanız gerekmez. Ajandan ajan destekli iş akışını kullanmasını isteyin:

```text
Translate this Markdown file to Korean with Co-op Translator MCP.
Use agent-assisted mode: call start_markdown_agent_translation, translate the returned chunks with your own model, then call finish_markdown_agent_translation.
Keep Markdown formatting, code blocks, and links intact.
```

Notebook'lar için aynı deseni kullanın:

```text
Translate this notebook to Korean with Co-op Translator MCP.
Use start_notebook_agent_translation, translate the returned Markdown-cell chunks with your own model, then call finish_notebook_agent_translation.
Preserve code cells, outputs, and notebook metadata.
```

MCP istemciniz sunucu istemlerini destekliyorsa, istemcinin aynı iş akışı talimatlarını yüklemesi için `agent_assisted_markdown_translation_prompt`'u kullanın.

Markdown için:

1. `document`, `language_code` ve isteğe bağlı `source_path` ile `start_markdown_agent_translation`'ı çağırın.
2. Döndürülen her parçayı, parçanın `prompt`unu izleyerek host ajan içinde çevirin.
3. Orijinal `job` ve `chunk_id` ile `translated_text` kullanarak çevrilmiş parçaları içeren `finish_markdown_agent_translation`'ı çağırın.
4. İçerik çevrilmiş hedef bir yola yazılacaksa, `rewrite_markdown_paths`'i çağırın.

Notebook'lar için:

1. Notebook JSON'u ve `language_code` ile `start_notebook_agent_translation`'ı çağırın.
2. Döndürülen her parçayı host ajan içinde çevirin.
3. Orijinal `job` ve çevrilmiş parçalar ile `finish_notebook_agent_translation`'ı çağırın.
4. Çevrilmiş notebook bağlantılarının hedef yol için ayarlanması gerekiyorsa `rewrite_notebook_paths`'i çağırın.

Ajan destekli araçlar Co-op Translator'dan yapılandırılmış LLM sağlayıcısını çağırmaz. Döndürülen parçaları çevirmekten host ajan sorumludur. Co-op Translator, Markdown parçalama, yer tutucu koruma, frontmatter yeniden oluşturma, notebook hücresi değişimi ve çeviri sonrası normalizasyonu ele alır.

### Tüm Bir Depoyu Çevirin

Kullanıcı Co-op Translator'ın `translate` CLI'sı gibi davranmasını istediğinde `run_translation`'ı kullanın.

Depo çevirisi varsayılan olarak `dry_run=true` olur, böylece bir ajan dosya değişiklikleri öncesi kapsamı inceleyebilir:

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "dry_run": true
}
```

`run_translation` sonucu, sürümlenmiş bir `events` dizisi içerir.
`co-op.translation.event.v1` ilerleme olayları. MCP istemcileri, yakalanmış konsol metnini ayrıştırmak yerine
`type`, `stage_key`, `completed`, `total` ve `current_path` gibi alanları kullanmalıdır.
`json_events_path`'i geçirerek bu olayları
bir NDJSON dosyasına da yazabilirsiniz.

Yazma izinleri için, çağıran taraf hem `dry_run=false` hem de `confirm_write=true` olarak ayarlamalıdır:

```json
{
  "language_codes": "ko",
  "root_dir": ".",
  "markdown": true,
  "dry_run": false,
  "confirm_write": true
}
```

`translate_project`, `run_translation` için uyumluluk takma adıdır.

### Çevrilmiş Çıktıyı İnceleyin

`run_review`'u LLM veya Vision kimlik bilgileri gerektirmeyen deterministik kontroller için kullanın:

!!! note "Beta"
    MCP beta `run_review` API'sini açığa çıkarır. Salt-okunur inceleme iş akışları için güvenlidir, ancak inceleme kontrolleri ve sorun şemaları değişebilir.

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "notebook": true
}
```

Sonuç, yakalanmış metin çıktısını ve mevcut olduğunda yapılandırılmış bir inceleme özetini içerir.

## Manuel Sunucu Çalıştırmaları

Manuel çalıştırmalar esas olarak hata ayıklama için veya uzun süre çalışan sunucular gibi davranan taşıma mekanizmaları içindir.

Varsayılan stdio sunucusunu hata ayıklayın:

```bash
co-op-translator-mcp
```

Kaynak çekiminden çalıştırın:

```bash
python -m co_op_translator.mcp.server
```

Uzun ömürlü bir HTTP veya SSE sunucusu çalıştırın:

```bash
co-op-translator-mcp --transport streamable-http
co-op-translator-mcp --transport sse
```

Yerel düzenleyici ve ajan entegrasyonları için, Adım 2'deki istemci tarafından yönetilen `stdio` yapılandırmasını tercih edin.

## Araçlar

| Araç | Amaç | Dosya yazar mı |
| --- | --- | --- |
| `translate_markdown_content` | Bir Markdown dizesini çevirir. | Hayır |
| `translate_notebook_content` | Notebook JSON'undaki Markdown hücrelerini çevirir. | Hayır |
| `translate_image_content` | Bir görseldeki metni çevirir ve base64 görsel verisi döndürür. | Opsiyonel, yalnızca `output_path` sağlandığında |
| `start_markdown_agent_translation` | Co-op Translator LLM kimlik bilgisi olmadan host ajanın çevirmesi için Markdown parçalarını hazırlar. | Hayır |
| `finish_markdown_agent_translation` | Host-ajan tarafından çevrilen parçalarından Markdown'u yeniden oluşturur. | Hayır |
| `start_notebook_agent_translation` | Host ajanın çevirmesi için notebook Markdown-hücre parçalarını hazırlar. | Hayır |
| `finish_notebook_agent_translation` | Host-ajan tarafından çevrilen parçalarından notebook JSON'unu yeniden oluşturur. | Hayır |
| `rewrite_markdown_paths` | Çevrilmiş hedef için Markdown gövdesi ve frontmatter yollarını yeniden yazar. | Hayır |
| `rewrite_notebook_paths` | Notebook Markdown hücreleri içindeki yolları yeniden yazar. | Hayır |
| `run_translation` | CLI gibi proje düzeyinde çeviri çalıştırır. | Evet, `dry_run=false` ve `confirm_write=true` olduğunda |
| `translate_project` | `run_translation` için uyumluluk takma adı. | Evet, `dry_run=false` ve `confirm_write=true` olduğunda |
| `run_review` | Deterministik inceleme kontrollerini çalıştırır. | Hayır |
| `get_configuration_status` | Gizli bilgileri açığa çıkarmadan yapılandırılmış LLM ve Vision sağlayıcılarını raporlar. | Hayır |
| `list_supported_languages` | Desteklenen hedef dil kodlarını listeler. | Hayır |
| `get_api_overview` | Mevcut MCP iş akışları ve araçlarını açıklar. | Hayır |

## Kaynaklar

| Kaynak URI'si | Amaç |
| --- | --- |
| `co-op://api` | İş akışlarının ve araçların JSON genel görünümü. |
| `co-op://supported-languages` | Desteklenen dil kodlarının JSON listesi. |
| `co-op://configuration` | Gizli bilgileri açığa çıkarmadan sağlayıcı kullanılabilirliği özetinin JSON'u. |

## İstemler

| İstem | Amaç |
| --- | --- |
| `translate_markdown_document_prompt` | MCP istemcisini içerik çevirisi ve isteğe bağlı yol yeniden yazımı konusunda yönlendirir. |
| `agent_assisted_markdown_translation_prompt` | MCP istemcisini, Co-op Translator LLM sağlayıcı kimlik bilgileri olmadan host-ajan Markdown çevirisi konusunda yönlendirir. |
| `translate_repository_prompt` | MCP istemcisini öncelikle dry-run yaparak depo çevirisi konusunda yönlendirir. |

## Kopyala-Yapıştır Örnekleri

Markdown içeriğini çevir:

```json
{
  "tool": "translate_markdown_content",
  "arguments": {
    "document": "# Hello\n\nWelcome to the course.",
    "language_code": "ko",
    "source_path": "docs/guide.md"
  }
}
```

Çevrilmiş Markdown bağlantılarını yeniden yaz:

```json
{
  "tool": "rewrite_markdown_paths",
  "arguments": {
    "content": "[Setup](../setup.md)\n\n![Hero](images/hero.png)",
    "source_path": "docs/guide.md",
    "target_path": "translations/ko/docs/guide.md",
    "policy": {
      "language_code": "ko",
      "root_dir": ".",
      "translations_dir": "translations",
      "translated_images_dir": "translated_images",
      "translation_types": ["markdown", "images"]
    }
  }
}
```

Host ajan modeli ile Markdown çevirisi:

```json
{
  "tool": "start_markdown_agent_translation",
  "arguments": {
    "document": "# Hello\n\nUse `pip install` to get started.",
    "language_code": "ko",
    "source_path": "docs/guide.md"
  }
}
```

Host ajan her döndürülen parçayı çevirdikten sonra, `start_markdown_agent_translation` tarafından döndürülen eksiksiz `job` nesnesi ile işi bitirin:

```text
tool: finish_markdown_agent_translation
arguments:
  job: <the full job object returned by start_markdown_agent_translation>
  translated_chunks:
    - chunk_id: body:1
      translated_text: "# 안녕하세요\n\n시작하려면 `pip install`을 사용하세요."
```

Depo çevirisini önizleyin:

```json
{
  "tool": "run_translation",
  "arguments": {
    "language_codes": "ko",
    "root_dir": ".",
    "markdown": true,
    "dry_run": true
  }
}
```

## Sorun Giderme

| Sorun | Denenecekler |
| --- | --- |
| MCP istemcisi `co-op-translator-mcp`'yi bulamıyor. | Mutlak Python yürütülebilir yolunu ve `["-m", "co_op_translator.mcp.server"]` kaynak çekme yapılandırmasını kullanın. |
| Sunucu listeleniyor ancak çeviri başarısız oluyor. | `get_configuration_status`'i çağırın ve bir LLM sağlayıcısının kullanılabilir olduğunu onaylayın. |
| Sağlayıcı kimlik bilgileri olmadan Markdown veya notebook çevirisi istiyorsunuz. | `start_markdown_agent_translation` / `finish_markdown_agent_translation` veya notebook eşdeğerlerini kullanın, böylece host ajan parçaları çevirir. |
| Görsel çevirisi başarısız oluyor. | Azure AI Vision değişkenlerinin ayarlı olduğunu doğrulayın ve `get_configuration_status`'i çağırın. |
| Depo çevirisi dosyaları yazmıyor. | `dry_run=false` ve `confirm_write=true`'yi yalnızca açık kullanıcı onayı sonrası ayarlayın. |
| İstemci yapılandırmasındaki değişiklikler görünmüyor. | MCP istemcisini yeniden başlatın veya yeniden yükleyin. |

## Güvenlik Notları

- MCP araç çağrıları host uygulama tarafından model kontrollüdür, bu nedenle depo çevirisi varsayılan olarak dry-run'dur.
- Tam depo çevirisi birçok dosya oluşturabilir, güncelleyebilir veya kaldırabilir. `confirm_write=true`'yi ayarlamadan önce açık kullanıcı onayı gerektirin.
- Yapılandırma durumu aracı asla API anahtarlarını, uç noktaları veya diğer gizli değerleri döndürmez.
- Görsel çevirisi base64 görsel verisi döndürür. Büyük görseller büyük araç yanıtları üretebilir.
- Ajan destekli araçlar kaynak parçaları ve istemleri MCP host'una döndürür. Bunları yalnızca kullanıcının o host ajan modeline göndermekten rahat olduğu içerikle kullanın.