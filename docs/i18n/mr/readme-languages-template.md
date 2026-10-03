# README भाषा टेम्पलेट

Co-op Translator भाषांतरित सामग्री प्रकाशित करणाऱ्या रिपॉझिटरींसाठी README भाषा तक्ता व्यवस्थापित करू शकतो.

प्रत्येक भाषांतर चालनावर Co-op Translator संपूर्ण विभाग बदलणार असल्यास खालील मार्कर्स वापरा. तुम्ही सानुकूल उपसमूह हस्ते राखण्यासाठी प्राधान्य देता असल्यास मार्कर्स काढा.

मार्कर्सच्या वरचे श्रेय आणि सुरुवात करण्याचा दुवा ऐच्छिक आहेत. हे वाचकांना शोधण्यास मदत करतात की भाषांतर कसे व्यवस्थापित केले जातात आणि ते त्यांच्या स्वतःच्या रिपॉझिटरी कशी भाषांतरित करू शकतात. भाषा-तक्ता अद्यतनांदरम्यान हे टिकवून ठेवण्यासाठी त्यांना मार्कर्सच्या बाहेर ठेवा. दुसरी रिपॉझिटरी अद्यतनित करताना, तिच्या योगदान मार्गदर्शक तत्त्वांचे पालन करा आणि तिच्या मेंटेनर्सना ठरवू द्या की हा मजकूर समाविष्ट करायचा की नाही.

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

भाषांतरादरम्यान sparse-checkout रिपॉझिटरी URL वैयक्तिकृत करा:

```bash
translate -l "ko" --repo-url "https://github.com/org/repo.git"
```

जर मार्कर्स उपस्थित असतील, तर भाषा जोडल्यास किंवा बदलल्यास Co-op Translator तयार केलेला तक्ता अद्यतनित करू शकतो.

आधीच्या README साठी, तुम्ही त्याच्या भाषा-तक्ता मार्कर्सच्या वर ऐच्छिक श्रेय आणि सुरुवात करण्याचा दुवा जोडू शकता, त्याची भाषा दुवे किंवा इतर सामग्री बदलल्याशिवाय. समर्थित-भाषा दुव्यांचा निर्देश [सध्याचा भाषा मार्गदर्शक](https://github.com/Azure/co-op-translator/blob/main/docs/supported-languages.md) कडे करा.