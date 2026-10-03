# README ဘာသာစကား စံနမူနာ

Co-op Translator သည် ဘာသာပြန်ထားသော အကြောင်းအရာများကို ထုတ်ဝေသော repository များအတွက် README ဘာသာစကား ဇယားကို ထိန်းသိမ်းနိုင်သည်။

Co-op Translator ကို တစ်ကြိမ်ပြန်ပြန် ဘာသာပြန်ရာတွင် အပိုင်းတစ်ခုလုံးကို အစားထိုးစေလိုပါက အောက်ပါ အမှတ်အသားများကို အသုံးပြုပါ။ ကိုယ်တိုင် စိတ်ကြိုက် အပိုင်းအစုကို ထိန်းသိမ်းလိုပါက အမှတ်အသားများကို ဖယ်ရှားပါ။

အထက်ဖော်ပြထားသော attribution နှင့် getting-started link များသည် ရွေးချယ်နိုင်သော အရာများဖြစ်သည်။ ၎င်းတို့က ဖတ်ရှုသူများအား ဘာသာပြန်ခြင်းများကို မည်သို့ ထိန်းသိမ်းကြသည်နှင့် မိမိတို့ repository များကို မည်သို့ ဘာသာပြန်ရမည်ကို ရှာဖွေတွေ့ရှိနိုင်စေသည်။ ဘာသာစကားဇယား အပ်ဒိတ်များတွင် ၎င်းတို့ကို ထိန်းသိမ်းထားရန် အမှတ်အသားများပြင်ပတွင် ထားပါ။ အခြား repository ကို အပ်ဒိတ်လုပ်စဉ်၌ ၎င်း၏ အလှူအပို့လမ်းညွှန်ချက်များကို လိုက်နာပြီး ထိန်းသိမ်းသူများအား ဤစာသားကို ထည့်သွင်းမည် မဟုတ်မဟုတ် ဆုံးဖြတ်ခွင့်ပေးပါ။

````markdown
### Multi-Language Support

#### Supported by [Co-op Translator](https://github.com/Azure/co-op-translator)

Maintain your own documentation? [Start with one README and one language](https://github.com/Azure/co-op-translator/blob/main/docs/github-actions.md#your-first-readme-translation-pr).

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](./translations/ar/README.md) | [Bengali](./translations/bn/README.md) | [Bulgarian](./translations/bg/README.md) | [Burmese (Myanmar)](./translations/my/README.md) | [Chinese (Simplified)](./translations/zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](./translations/zh-HK/README.md) | [Chinese (Traditional, Macau)](./translations/zh-MO/README.md) | [Chinese (Traditional, Taiwan)](./translations/zh-TW/README.md) | [Croatian](./translations/hr/README.md) | [Czech](./translations/cs/README.md) | [Danish](./translations/da/README.md) | [Dutch](./translations/nl/README.md) | [Estonian](./translations/et/README.md) | [Finnish](./translations/fi/README.md) | [French](./translations/fr/README.md) | [German](./translations/de/README.md) | [Greek](./translations/el/README.md) | [Hebrew](./translations/he/README.md) | [Hindi](./translations/hi/README.md) | [Hungarian](./translations/hu/README.md) | [Indonesian](./translations/id/README.md) | [Italian](./translations/it/README.md) | [Japanese](./translations/ja/README.md) | [Kannada](./translations/kn/README.md) | [Khmer](./translations/km/README.md) | [Korean](./translations/ko/README.md) | [Lithuanian](./translations/lt/README.md) | [Malay](./translations/ms/README.md) | [Malayalam](./translations/ml/README.md) | [Manipuri (Meitei Mayek)](./translations/mni/README.md) | [Marathi](./translations/mr/README.md) | [Nepali](./translations/ne/README.md) | [Nigerian Pidgin](./translations/pcm/README.md) | [Norwegian](./translations/no/README.md) | [Persian (Farsi)](./translations/fa/README.md) | [Polish](./translations/pl/README.md) | [Portuguese (Brazil)](./translations/pt-BR/README.md) | [Portuguese (Portugal)](./translations/pt-PT/README.md) | [Punjabi (Gurmukhi)](./translations/pa/README.md) | [Romanian](./translations/ro/README.md) | [Russian](./translations/ru/README.md) | [Serbian (Cyrillic)](./translations/sr/README.md) | [Slovak](./translations/sk/README.md) | [Slovenian](./translations/sl/README.md) | [Spanish](./translations/es/README.md) | [Swahili](./translations/sw/README.md) | [Swedish](./translations/sv/README.md) | [Tagalog (Filipino)](./translations/tl/README.md) | [Tamil](./translations/ta/README.md) | [Telugu](./translations/te/README.md) | [Thai](./translations/th/README.md) | [Turkish](./translations/tr/README.md) | [Ukrainian](./translations/uk/README.md) | [Urdu](./translations/ur/README.md) | [Vietnamese](./translations/vi/README.md)

> **Prefer to Clone Locally?**
>
> This repository includes many language translations, which can significantly increase download size. To clone without translations, use sparse checkout:
>
> ```bash
> git clone --filter=blob:none --sparse https://github.com/org/repo.git
> cd repo
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```

<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->
````

ဘာသာပြန်စဉ် sparse-checkout repository URL ကို ကိုယ်ပိုင်ပြုလုပ်ပါ:

```bash
translate -l "ko" --repo-url "https://github.com/org/repo.git"
```

အမှတ်အသားများ ရှိပါက၊ ဘာသာစကားများ ထည့်သွင်းသို့မဟုတ် ပြောင်းလဲသောအခါ Co-op Translator သည် ထုတ်လုပ်ထားသော ဇယားကို အပ်ဒိတ်လုပ်နိုင်သည်။

အခုရှိပြီးသား README အတွက် သင်သည် ၎င်း၏ ဘာသာစကားဇယား အမှတ်အသားများအထက်တွင် ရွေးချယ်နိုင်သော attribution နှင့် getting-started link ကို ၎င်း၏ ဘာသာစကားလင့်ခ်များ သို့မဟုတ် အခြား အကြောင်းအရာများကို အစားထိုးခြင်းမပြုဘဲ ထည့်နိုင်ပါသည်။ ပံ့ပိုးထားသော ဘာသာစကားလင့်ခ်များကို [လက်ရှိ ဘာသာစကား လမ်းညွှန်](https://github.com/Azure/co-op-translator/blob/main/docs/supported-languages.md) ဆီသို့ ညွှန်းပါ။