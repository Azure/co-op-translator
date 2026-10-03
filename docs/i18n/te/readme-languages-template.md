# README భాషల టెంప్లేట్

Co-op Translator అనువాదిత కంటెంట్‌ను ప్రచురించే రిపోజిటరీల కోసం README భాషల పట్టికను నిర్వహించగలదు.

ప్రతి అనువాద రన్‌లో మొత్తం విభాగాన్ని Co-op Translator ద్వారా మార్చాలనుకుంటే దిగువ మార్కర్లను ఉపయోగించండి. మీరు ప్రత్యేక ఉపసెట్‌ను మానవీయంగా నిర్వహించాలనుకుంటే మార్కర్లను తీసివేయండి.

మార్కర్ల పై ఉన్న attribution మరియు getting-started లింక్లు ఐచ్ఛికం. అవి పాఠకులకు అనువాదాలు ఎలా నిర్వహించబడతాయో మరియు తమ స్వంత రిపోజిటరీలను ఎలా అనువదించాలో కనుగొనటానికి సహాయపడతాయి. భాషా-పట్టిక నవీకరణలు వాటిని నిలిపివేయకుండా ఉంచడానికి వాటిని మార్కర్ల బాహ్యంగా ఉంచండి. మరొక రిపోజిటరీని నవీకరించే సమయంలో, దాని కాంట్రిబ్యూషన్ మార్గదర్శకాలను అనుసరించి, ఈ టెక్స్ట్‌ను చేర్చాలా లేదా కాకపోవాలా నిర్ణయించడానికి దాని నిర్వహకులకు అవకాశం ఇవ్వండి.

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

అనువాదం సమయంలో sparse-checkout రిపాజిటరీ URL ను వ్యక్తిగతీకరించండి:

```bash
translate -l "ko" --repo-url "https://github.com/org/repo.git"
```

మార్కర్లు ఉన్నట్లయితే, భాషలు జోడించబడినప్పుడు లేదా మార్చినప్పుడు Co-op Translator ఆ సృష్టించబడిన పట్టికను నవీకరించగలదు.

ఇప్పటికే ఉన్న README కోసం, దాని భాషా-పట్టిక మార్కర్ల పైన మీరు ఐచ్ఛిక క్రెడిట్ మరియు ప్రారంభించడానికి లింక్‌ను దాని భాషా లింకులు లేదా ఇతర కంటెంట్‌ను మార్చకుండా జోడించవచ్చు. మద్దతు పొందే భాషల లింకులను [ప్రస్తుత భాషా గైడ్](https://github.com/Azure/co-op-translator/blob/main/docs/supported-languages.md) కు సూచించండి.
