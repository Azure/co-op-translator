# README भाषाहरू ढाँचा

Co-op Translator ले अनुवादित सामग्री प्रकाशित गर्ने रिपोजिटरीहरूको लागि README भाषा तालिका व्यवस्थापन गर्न सक्छ।

प्रत्येक अनुवाद कार्यमा Co-op Translator लाई सम्पूर्ण खण्ड प्रतिस्थापन गर्न चाहँदा तलका मार्करहरू प्रयोग गर्नुहोस्। यदि तपाईं अनुकूलित उपसमूह म्यानुअली व्यवस्थापन गर्न चाहनुहुन्छ भने मार्करहरू हटाउनुहोस्।

मार्करहरू माथिको श्रेय र सुरु गर्ने लिङ्क वैकल्पिक छन्। ती पाठकहरूलाई अनुवादहरू कसरी व्यवस्थापन गरिन्छ र कसरी आफ्नै रिपोजिटरीहरू अनुवाद गर्ने भन्ने कुरा पत्ता लगाउन मद्दत गर्छन्। भाषा-तालिका अपडेटहरूले तिनीहरूलाई सुरक्षित राख्न मार्करहरूको बाहिरै राख्नुहोस्। अर्को रिपोजिटरी अपडेट गर्दा यसको योगदान दिशानिर्देशहरू पालना गर्नुहोस् र यस पाठलाई समावेश गर्ने कि नघुमाउने निर्णय यसको मर्मतकर्ताहरूलाई छोड्नुहोस्।

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

अनुवादको समयमा sparse-checkout रिपोजिटरी URL व्यक्तिगत बनाउनुहोस्:

```bash
translate -l "ko" --repo-url "https://github.com/org/repo.git"
```

यदि मार्करहरू उपस्थित छन् भने, भाषाहरू थपिंदा वा परिवर्तन हुँदा Co-op Translator ले उत्पन्न तालिका अपडेट गर्न सक्छ।

अवस्थित README का लागि, तपाईंले यसको भाषा-तालिका मार्करहरूको माथि वैकल्पिक श्रेय र सुरु गर्ने लिङ्क थप्न सक्नुहुन्छ बिना यसको भाषा लिङ्कहरू वा अन्य सामग्री प्रतिस्थापन नगरी। समर्थित-भाषा लिङ्कहरूलाई [वर्तमान भाषा मार्गदर्शक](https://github.com/Azure/co-op-translator/blob/main/docs/supported-languages.md) तर्फ निर्देश गर्नुहोस्।
