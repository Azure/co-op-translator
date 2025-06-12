<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b4ed48f23ec418b31e90a02fe629fcde",
  "translation_date": "2025-06-12T12:15:52+00:00",
  "source_file": "getting_started/supported-languages.md",
  "language_code": "tl"
}
-->
# Sinusuportahang mga Wika

Ang talahanayan sa ibaba ay naglilista ng mga wikang kasalukuyang sinusuportahan ng **Co-op Translator**. Kasama rito ang mga language code, pangalan ng wika, at anumang kilalang isyu na nauugnay sa bawat wika. Kung nais mong magdagdag ng suporta para sa bagong wika, pakidagdag ang kaukulang language code, pangalan, at angkop na font sa `font_language_mappings.yml` file na matatagpuan sa `src/co_op_translator/fonts/` at magsumite ng pull request pagkatapos ng pagsubok.

| Language Code | Language Name        | Font                              | RTL Support | Known Issues |
|---------------|----------------------|-----------------------------------|-------------|--------------|
| en            | Ingles               | NotoSans-Medium.ttf               | Hindi       | Wala         |
| fr            | Pranses              | NotoSans-Medium.ttf               | Hindi       | Wala         |
| es            | Kastila              | NotoSans-Medium.ttf               | Hindi       | Wala         |
| de            | Aleman               | NotoSans-Medium.ttf               | Hindi       | Wala         |
| ru            | Ruso                 | NotoSans-Medium.ttf               | Hindi       | Wala         |
| ar            | Arabe                | NotoSansArabic-Medium.ttf         | Oo          | Wala         |
| fa            | Persian (Farsi)      | NotoSansArabic-Medium.ttf         | Hindi       | Wala         |
| ur            | Urdu                 | NotoSansArabic-Medium.ttf         | Hindi       | Wala         |
| zh            | Tsino (Pinasimple)   | NotoSansCJK-Medium.ttc            | Hindi       | Wala         |
| mo            | Tsino (Tradisyonal, Macau) | NotoSansCJK-Medium.ttc    | Hindi       | Wala         |
| hk            | Tsino (Tradisyonal, Hong Kong) | NotoSansCJK-Medium.ttc| Hindi       | Wala         |
| tw            | Tsino (Tradisyonal, Taiwan) | NotoSansCJK-Medium.ttc   | Hindi       | Wala         |
| ja            | Hapones              | NotoSansCJK-Medium.ttc            | Hindi       | Wala         |
| ko            | Koreano              | NotoSansCJK-Medium.ttc            | Hindi       | Wala         |
| hi            | Hindi                | NotoSansDevanagari-Medium.ttf     | Hindi       | Wala         |
| bn            | Bengali              | NotoSansBengali-Medium.ttf        | Hindi       | Wala         |
| mr            | Marathi              | NotoSansDevanagari-Medium.ttf     | Hindi       | Wala         |
| ne            | Nepali               | NotoSansDevanagari-Medium.ttf     | Hindi       | Wala         |
| pa            | Punjabi (Gurmukhi)   | NotoSansGurmukhi-Medium.ttf       | Hindi       | Wala         |
| pt            | Portuges (Portugal)  | NotoSans-Medium.ttf               | Hindi       | Wala         |
| br            | Portuges (Brazil)    | NotoSans-Medium.ttf               | Hindi       | Wala         |
| it            | Italyano             | NotoSans-Medium.ttf               | Hindi       | Wala         |
| pl            | Polish               | NotoSans-Medium.ttf               | Hindi       | Wala         |
| tr            | Turkish              | NotoSans-Medium.ttf               | Hindi       | Wala         |
| el            | Griyego              | NotoSans-Medium.ttf               | Hindi       | Wala         |
| th            | Thai                 | NotoSansThai-Medium.ttf           | Hindi       | Wala         |
| sv            | Swedish              | NotoSans-Medium.ttf               | Hindi       | Wala         |
| da            | Danish               | NotoSans-Medium.ttf               | Hindi       | Wala         |
| no            | Norwegian            | NotoSans-Medium.ttf               | Hindi       | Wala         |
| fi            | Finnish              | NotoSans-Medium.ttf               | Hindi       | Wala         |
| nl            | Dutch                | NotoSans-Medium.ttf               | Hindi       | Wala         |
| he            | Hebrew               | NotoSansHebrew-Medium.ttf         | Hindi       | Wala         |
| vi            | Vietnamese           | NotoSans-Medium.ttf               | Hindi       | Wala         |
| id            | Indonesian           | NotoSans-Medium.ttf               | Hindi       | Wala         |
| ms            | Malay                | NotoSans-Medium.ttf               | Hindi       | Wala         |
| tl            | Tagalog (Filipino)   | NotoSans-Medium.ttf               | Hindi       | Wala         |
| sw            | Swahili              | NotoSans-Medium.ttf               | Hindi       | Wala         |
| hu            | Hungarian            | NotoSans-Medium.ttf               | Hindi       | Wala         |
| cs            | Czech                | NotoSans-Medium.ttf               | Hindi       | Wala         |
| sk            | Slovak               | NotoSans-Medium.ttf               | Hindi       | Wala         |
| ro            | Romanian             | NotoSans-Medium.ttf               | Hindi       | Wala         |
| bg            | Bulgarian            | NotoSans-Medium.ttf               | Hindi       | Wala         |
| sr            | Serbian (Cyrillic)   | NotoSans-Medium.ttf               | Hindi       | Wala         |
| hr            | Croatian             | NotoSans-Medium.ttf               | Hindi       | Wala         |
| sl            | Slovenian            | NotoSans-Medium.ttf               | Hindi       | Wala         |
| uk            | Ukrainian            | NotoSans-Medium.ttf               | Hindi       | Wala         |
| my            | Burmese (Myanmar)    | NotoSans-Medium.ttf               | Hindi       | Wala         |

## Pagdaragdag ng bagong wika

Para magdagdag ng suporta para sa bagong wika:

1. Pumunta sa [src/co_op_translator/fonts/font_language_mappings.yml](https://github.com/Azure/co-op-translator/blob/main/src/co_op_translator/fonts/font_language_mappings.yml).
2. Idagdag ang language code, pangalan, at angkop na pangalan ng font file. Siguraduhing isama ang `rtl` attribute kung ang wika ay right-to-left.
3. Kung kailangan mong gumamit ng bagong font, tiyaking libre itong gamitin sa mga open-source na proyekto sa pamamagitan ng pagsuri sa lisensya at karapatan sa paggamit. Pagkatapos matiyak, idagdag ang font file sa `src/co_op_translator/fonts/` directory.
4. Subukan ang mga pagbabago nang lokal upang matiyak na maayos na sinusuportahan ang bagong wika.
5. Mag-submit ng Pull Request na may mga pagbabago at ipahiwatig ang pagdagdag ng bagong wika sa deskripsyon ng PR.

Halimbawa:

```yaml
new_lang:
  name: "New Language"
  font: "NotoSans-Medium.ttf"
  rtl: false
```

**Pagtatangi**:  
Ang dokumentong ito ay isinalin gamit ang serbisyong AI na pagsasalin na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat nagsusumikap kami para sa katumpakan, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o di-tumpak na impormasyon. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.