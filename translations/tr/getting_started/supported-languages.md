<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ba33aa8d5da0d3dd14322b77fcb63deb",
  "translation_date": "2025-05-06T17:48:37+00:00",
  "source_file": "getting_started/supported-languages.md",
  "language_code": "tr"
}
-->
# Desteklenen diller

Aşağıdaki tablo, **Co-op Translator** tarafından şu anda desteklenen dilleri listeler. Dil kodları, dil isimleri ve her dil ile ilgili bilinen sorunlar dahil edilmiştir. Yeni bir dil desteği eklemek isterseniz, lütfen ilgili dil kodunu, adını ve uygun fontu `font_language_mappings.yml` dosyasına `src/co_op_translator/fonts/` konumunda ekleyin ve test ettikten sonra bir pull request gönderin.

| Language Code | Language Name        | Font                              | RTL Support | Known Issues |
|---------------|----------------------|-----------------------------------|-------------|--------------|
| en            | English              | NotoSans-Medium.ttf               | No          | No           |
| fr            | French               | NotoSans-Medium.ttf               | No          | No           |
| es            | Spanish              | NotoSans-Medium.ttf               | No          | No           |
| de            | German               | NotoSans-Medium.ttf               | No          | No           |
| ru            | Russian              | NotoSans-Medium.ttf               | No          | No           |
| ar            | Arabic               | NotoSansArabic-Medium.ttf         | Yes         | No           |
| fa            | Persian (Farsi)      | NotoSansArabic-Medium.ttf         | Yes         | No           |
| ur            | Urdu                 | NotoSansArabic-Medium.ttf         | Yes         | No           |
| zh            | Chinese (Simplified) | NotoSansCJK-Medium.ttc            | No          | No           |
| mo            | Chinese (Traditional, Macau) | NotoSansCJK-Medium.ttc    | No          | No           |
| hk            | Chinese (Traditional, Hong Kong) | NotoSansCJK-Medium.ttc| No          | No           |
| tw            | Chinese (Traditional, Taiwan) | NotoSansCJK-Medium.ttc   | No          | No           |
| ja            | Japanese             | NotoSansCJK-Medium.ttc            | No          | No           |
| ko            | Korean               | NotoSansCJK-Medium.ttc            | No          | No           |
| hi            | Hindi                | NotoSansDevanagari-Medium.ttf     | No          | No           |
| bn            | Bengali              | NotoSansBengali-Medium.ttf        | No          | No           |
| mr            | Marathi              | NotoSansDevanagari-Medium.ttf     | No          | No           |
| ne            | Nepali               | NotoSansDevanagari-Medium.ttf     | No          | No           |
| pa            | Punjabi (Gurmukhi)   | NotoSansGurmukhi-Medium.ttf       | No          | No           |
| pt            | Portuguese (Portugal)| NotoSans-Medium.ttf               | No          | No           |
| br            | Portuguese (Brazil)  | NotoSans-Medium.ttf               | No          | No           |
| it            | Italian              | NotoSans-Medium.ttf               | No          | No           |
| pl            | Polish               | NotoSans-Medium.ttf               | No          | No           |
| tr            | Turkish              | NotoSans-Medium.ttf               | No          | No           |
| el            | Greek                | NotoSans-Medium.ttf               | No          | No           |
| th            | Thai                 | NotoSansThai-Medium.ttf           | No          | No           |
| sv            | Swedish              | NotoSans-Medium.ttf               | No          | No           |
| da            | Danish               | NotoSans-Medium.ttf               | No          | No           |
| no            | Norwegian            | NotoSans-Medium.ttf               | No          | No           |
| fi            | Finnish              | NotoSans-Medium.ttf               | No          | No           |
| nl            | Dutch                | NotoSans-Medium.ttf               | No          | No           |
| he            | Hebrew               | NotoSansHebrew-Medium.ttf         | Yes         | No           |
| vi            | Vietnamese           | NotoSans-Medium.ttf               | No          | No           |
| id            | Indonesian           | NotoSans-Medium.ttf               | No          | No           |
| ms            | Malay                | NotoSans-Medium.ttf               | No          | No           |
| tl            | Tagalog (Filipino)   | NotoSans-Medium.ttf               | No          | No           |
| sw            | Swahili              | NotoSans-Medium.ttf               | No          | No           |
| hu            | Hungarian            | NotoSans-Medium.ttf               | No          | No           |
| cs            | Czech                | NotoSans-Medium.ttf               | No          | No           |
| sk            | Slovak               | NotoSans-Medium.ttf               | No          | No           |
| ro            | Romanian             | NotoSans-Medium.ttf               | No          | No           |
| bg            | Bulgarian            | NotoSans-Medium.ttf               | No          | No           |
| sr            | Serbian (Cyrillic)   | NotoSans-Medium.ttf               | No          | No           |
| hr            | Croatian             | NotoSans-Medium.ttf               | No          | No           |
| sl            | Slovenian            | NotoSans-Medium.ttf               | No          | No           |

## Yeni bir dil eklemek

Yeni bir dil desteği eklemek için:

1. [src/co_op_translator/fonts/font_language_mappings.yml](https://github.com/Azure/co-op-translator/blob/main/src/co_op_translator/fonts/font_language_mappings.yml) dosyasına gidin.
2. Dil kodunu, adını ve uygun font dosyası adını ekleyin. Dil sağdan sola yazılıyorsa `rtl` özelliğini eklemeyi unutmayın.
3. Yeni bir font kullanmanız gerekiyorsa, fontun açık kaynak projelerde kullanımının ücretsiz olduğundan lisans ve telif hakları açısından emin olun. Doğruladıktan sonra font dosyasını `src/co_op_translator/fonts/` dizinine ekleyin.
4. Değişikliklerinizi yerel olarak test ederek yeni dilin düzgün desteklendiğinden emin olun.
5. Değişikliklerinizi içeren bir Pull Request gönderin ve PR açıklamasında yeni dil eklediğinizi belirtin.

Örnek:

```yaml
new_lang:
  name: "New Language"
  font: "NotoSans-Medium.ttf"
  rtl: false
```

**Feragatname**:  
Bu belge, AI çeviri servisi [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba gösterilse de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilindeki haliyle yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek herhangi bir yanlış anlama veya yanlış yorumdan sorumlu değiliz.