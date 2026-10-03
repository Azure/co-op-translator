# README भाषाओं का टेम्पलेट

Co-op Translator उन रिपॉज़िटरीज़ के लिए README भाषा तालिका बनाए रख सकता है जो अनुवादित सामग्री प्रकाशित करती हैं।

नीचे दिए गए मार्करों का उपयोग करें जब आप चाहें कि Co-op Translator प्रत्येक अनुवाद रन पर पूरे सेक्शन को बदल दे। यदि आप मैन्युअल रूप से एक कस्टम उपसमूह बनाए रखना पसंद करते हैं तो मार्करों को हटा दें।

मार्करों के ऊपर दिया गया श्रेय और शुरुआती-लिंक वैकल्पिक है। ये पाठकों को यह जानने में मदद करते हैं कि अनुवादों का रखरखाव कैसे किया जाता है और वे अपनी स्वयं की रिपॉज़िटरीज़ का अनुवाद कैसे कर सकते हैं। उन्हें मार्करों के बाहर रखें ताकि भाषा-तालिका के अपडेट उन्हें बरकरार रखें। जब आप किसी अन्य रिपॉज़िटरी को अपडेट कर रहे हों, तो इसके योगदान दिशानिर्देशों का पालन करें और इसके मेंटेनर्स को यह चुनने दें कि क्या वे इस टेक्स्ट को शामिल करना चाहते हैं।

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

अनुवाद के दौरान sparse-checkout रिपोजिटरी URL को वैयक्तिकृत करें:

```bash
translate -l "ko" --repo-url "https://github.com/org/repo.git"
```

यदि मार्कर मौजूद हैं, तो Co-op Translator जब भाषाएँ जोड़ी या बदली जाती हैं तो जनरेट की गई तालिका को अपडेट कर सकता है।

मौजूदा README के लिए, आप इसके भाषा-तालिका मार्करों के ऊपर वैकल्पिक श्रेय और शुरूआती लिंक जोड़ सकते हैं बिना इसके भाषा लिंक या अन्य सामग्री को बदलने के। समर्थित-भाषा लिंक को [वर्तमान भाषा मार्गदर्शिका](https://github.com/Azure/co-op-translator/blob/main/docs/supported-languages.md) की ओर निर्देशित करें।