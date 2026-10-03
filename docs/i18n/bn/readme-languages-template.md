# README ভাষা টেমপ্লেট

Co-op Translator এমন রেপোজিটরির README ভাষা টেবিল বজায় রাখতে পারে যেগুলো অনূদিত সামগ্রী প্রকাশ করে।

নিচের মার্কারগুলো ব্যবহার করুন যখন আপনি চান Co-op Translator প্রতিটি অনুবাদ চলাকালে পুরো অংশটি প্রতিস্থাপন করুক। যদি আপনি নিজে ম্যানুয়ালি একটি কাস্টম সাবসেট বজায় রাখতে পছন্দ করেন, তবে মার্কারগুলো সরিয়ে দিন।

মার্কারগুলোর উপরে থাকা অ্যাট্রিবিউশন এবং শুরু করার লিঙ্ক ঐচ্ছিক। এগুলো পাঠকদের সাহায্য করে জানতে যে অনুবাদগুলি কীভাবে বজায় রাখা হয় এবং কীভাবে তারা নিজেদের রেপোজিটরি অনুবাদ করবে। এগুলোকে মার্কারগুলোর বাইরে রাখুন যাতে ভাষা-টেবিল আপডেট করলে সেগুলো অক্ষুণ্ন থাকে। যখন অন্য কোনো রেপোজিটরি আপডেট করবেন, তার অবদান নির্দেশিকা অনুসরণ করুন এবং তার রক্ষণাবেক্ষকরা সিদ্ধান্ত নেবেন যে এই টেক্সটটি অন্তর্ভুক্ত করা হবে কিনা।

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

অনুবাদের সময় sparse-checkout রেপোজিটরি URL ব্যক্তিগতকরণ করুন:

```bash
translate -l "ko" --repo-url "https://github.com/org/repo.git"
```

যদি মার্কারগুলো উপস্থিত থাকে, Co-op Translator ভাষা যোগ বা পরিবর্তন হলে তৈরি হওয়া টেবিলটি আপডেট করতে পারে।

বিদ্যমান README-এর জন্য, আপনি ভাষা-টেবিল মার্কারগুলোর উপরে ঐচ্ছিক অ্যাট্রিবিউশন এবং শুরু করার লিংক যোগ করতে পারেন, তার ভাষার লিঙ্ক বা অন্যান্য কনটেন্ট প্রতিস্থাপন না করে। সমর্থিত ভাষার লিঙ্কগুলো [বর্তমান ভাষা গাইড](https://github.com/Azure/co-op-translator/blob/main/docs/supported-languages.md) এ নির্দেশ করুন।