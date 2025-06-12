<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b4ed48f23ec418b31e90a02fe629fcde",
  "translation_date": "2025-06-12T12:20:37+00:00",
  "source_file": "getting_started/supported-languages.md",
  "language_code": "my"
}
-->
# ထောက်ခံထားသော ဘာသာစကားများ

အောက်ပါဇယားတွင် **Co-op Translator** မှ လက်ရှိထောက်ခံထားသော ဘာသာစကားများကို ဖော်ပြထားသည်။ ၎င်းတွင် ဘာသာစကားကုဒ်များ၊ ဘာသာစကားအမည်များနှင့် အဆိုပါဘာသာစကားနှင့်ဆက်စပ်သော ပြဿနာများ ပါဝင်သည်။ ဘာသာစကားအသစ်တစ်ခုထည့်သွင်းလိုပါက၊ `font_language_mappings.yml` ဖိုင်တွင် သင့်ဘာသာစကားကုဒ်၊ အမည်နှင့် သင့်တော်သော ဖောင့်ကို `src/co_op_translator/fonts/` တွင် ထည့်သွင်းပြီး စမ်းသပ်ပြီးနောက် Pull Request တင်ပေးပါ။

| Language Code | Language Name        | Font                              | RTL Support | Known Issues |
|---------------|----------------------|-----------------------------------|-------------|--------------|
| en            | English              | NotoSans-Medium.ttf               | No          | No           |
| fr            | French               | NotoSans-Medium.ttf               | No          | No           |
| es            | Spanish              | NotoSans-Medium.ttf               | No          | No           |
| de            | German               | NotoSans-Medium.ttf               | No          | No           |
| ru            | Russian              | NotoSans-Medium.ttf               | No          | No           |
| ar            | Arabic               | NotoSansArabic-Medium.ttf         | Yes         | No           |
| fa            | Persian (Farsi)      | NotoSansArabic-Medium.ttf         | No          | No           |
| ur            | Urdu                 | NotoSansArabic-Medium.ttf         | No          | No           |
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
| he            | Hebrew               | NotoSansHebrew-Medium.ttf         | No          | No           |
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
| uk            | Ukrainian            | NotoSans-Medium.ttf               | No          | No           |
| my            | Burmese (Myanmar)    | NotoSans-Medium.ttf               | No          | No           |

## ဘာသာစကားအသစ်ထည့်သွင်းခြင်း

ဘာသာစကားအသစ်တစ်ခု ထည့်သွင်းရန်အတွက် -

1. [src/co_op_translator/fonts/font_language_mappings.yml](https://github.com/Azure/co-op-translator/blob/main/src/co_op_translator/fonts/font_language_mappings.yml) သို့ သွားပါ။
2. ဘာသာစကားကုဒ်၊ အမည်နှင့် သင့်တော်သော ဖောင့်ဖိုင်အမည်ကို ထည့်ပါ။ ဘာသာစကားသည် ညာမှ ဘယ်သို့ဖတ်ရသော (right-to-left) ဖြစ်ပါက `rtl` attribute ကိုပါ ထည့်သွင်းရန် သတိပြုပါ။
3. ဖောင့်အသစ်အသုံးပြုလိုပါက၊ ဖောင့်သည် open-source ပရောဂျက်များတွင် အခမဲ့အသုံးပြုနိုင်ကြောင်း လိုင်စင်နှင့် မူပိုင်ခွင့် စည်းမျဉ်းများကို စစ်ဆေးပါ။ စစ်ဆေးပြီးနောက် ဖောင့်ဖိုင်ကို `src/co_op_translator/fonts/` ဖိုလ်ဒါထဲ ထည့်သွင်းပါ။
4. သင့်ပြင်ဆင်မှုများကို ဒေသတွင်း စမ်းသပ်၍ ဘာသာစကားအသစ်ကို မှန်ကန်စွာ ထောက်ခံထားကြောင်း သေချာစေပါ။
5. ပြင်ဆင်မှုများနှင့်အတူ Pull Request တင်ပြီး PR ဖော်ပြချက်တွင် ဘာသာစကားအသစ် ထည့်သွင်းမှုကို ဖော်ပြပါ။

ဥပမာ -

```yaml
new_lang:
  name: "New Language"
  font: "NotoSans-Medium.ttf"
  rtl: false
```

Sure! Please specify which language "my" refers to, so I can provide the correct translation.