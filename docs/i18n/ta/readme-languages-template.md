# README மொழிகள் வார்ப்புரு

Co-op Translator மொழிபெயர்க்கப்பட்ட உள்ளடக்கத்தை வெளியிடும் களஞ்சியங்களுக்கு README மொழி அட்டவணையை பராமரிக்க முடியும்.

ஒவ்வொரு மொழிபெயர்ப்பு ஓட்டத்திலும் முழு பகுதியையும் மாற்ற Co-op Translator-ஐ நீங்கள் விரும்பினால் கீழுள்ள குறிச்சொற்களைப் பயன்படுத்துங்கள். தனிப்பயன் துண்டை கைமுறைமாக பராமரிக்க விரும்பினால் குறிச்சொற்களை நீக்குங்கள்.

குறிச்சொற்களின் மேற்பகுதியில் உள்ள பெயர்குறிப்பும் தொடக்க வழிமுறை இணைப்பும் விருப்பத்தின்னுடையவை. அவைகள் மொழிபெயர்ப்புகள் எவ்வாறு பராமரிக்கப்படுகின்றன மற்றும் அவர்களின் சொந்த களஞ்சியங்களை எவ்வாறு மொழிபெயர்ப்பது என்பதை வாசகர்கள் கண்டறிய உதவுகின்றன. மொழி அட்டவணை புதுப்பிப்புகள் அவற்றை பாதிக்காமல் இருக்க அவற்றை குறிச்சொற்களுக்குப் வெளியில் வைத்திருங்கள். மற்றொரு களஞ்சியத்தை புதுப்பிக்கும் போது, அதன் பங்களிப்பு வழிகாட்டுதல்களை பின்பற்றவும் மற்றும் இந்த உரையை சேர்க்கவேண்டுமா என்பதை பராமரிப்பவர்கள் தீர்மானிக்கவிடுங்கள்.

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

மொழிபெயர்ப்பின் போது sparse-checkout repository URL ஐ தனிப்பயனாக்கவும்:

```bash
translate -l "ko" --repo-url "https://github.com/org/repo.git"
```

குறிச்சொற்கள் இருந்தால், மொழிகள் சேர்க்கப்பட்டாலோ அல்லது மாற்றப்பட்டாலோ Co-op Translator உருவாக்கப்பட்ட அட்டவணையை புதுப்பிக்க முடியும்.

ஏற்கனவே உள்ள README ஒன்றிற்கு, அதன் மொழி அட்டவணை குறிச்சொற்களை மாற்றாமல் மேலுள்ள விருப்பமான பெயர்குறிப்பையும் தொடக்க வழிமுறை இணைப்பையும் நீங்கள் சேர்க்கலாம். ஆதரிக்கப்படும் மொழி இணைப்புகளை [தற்போதைய மொழி வழிகாட்டி](https://github.com/Azure/co-op-translator/blob/main/docs/supported-languages.md)-க்கு குறிக்கவும்.