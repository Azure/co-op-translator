# README ഭാഷകൾക്കുള്ള ടെംപ്ലേറ്റ്

Co-op Translator വിവർത്തനം ചെയ്ത ഉള്ളടക്കം പ്രസിദ്ധീകരിക്കുന്ന റിപ്പോസിറ്ററികളായുള്ള README ഭാഷാ പട്ടിക പരിപാലിക്കാൻ കഴിയും.

ഓരോ വിവർത്തന ഓട്ടത്തിലും Co-op Translator മുഴുവൻ സെക്ഷൻ പകരംവെക്കണമെന്ന് നിങ്ങൾ ആഗ്രഹിക്കുന്നുവെങ്കിൽ താഴെ കാണുന്ന മാർക്കറുകൾ ഉപയോഗിക്കുക. നിങ്ങൾക്ക് ഒരു കസ്റ്റം ഉപസെറ്റ് കൈയോടെ കൈമാറി പരിപാലിക്കേണ്ടതുണ്ടെങ്കിൽ മാർക്കറുകൾ നീക്കം ചെയ്യുക.

മാർക്കറുകളുടെ മുകളിൽ ഉള്ള അറ്റ്ട്രിബ്യൂഷവും 'ആരംഭിക്കാൻ' ലിങ്കും اخت്യൻ എന്നായിരിക്കും. അവ വായকদের വിവർത്തനങ്ങൾ എങ്ങനെ പരിപാലിക്കുന്നു എന്നും അവരുടെ സ്വന്തം റിപ്പോസിറ്ററികൾ എങ്ങനെ വിവർത്തനം ചെയ്യാമെന്നും കണ്ടെത്താൻ സഹായിക്കുന്നു. ഭാഷാ പട്ടിക അപ്‌ഡേറ്റുകൾ അവ സംരക്ഷിക്കേണ്ടതിനാൽ ഇവയെ മാർക്കറുകൾക്കപ്പുറം വയ്ക്കുക. മറ്റൊരു റിപ്പോസിറ്ററി അപ്‌ഡേറ്റ് ചെയ്യുമ്പോൾ അതിന്റെ സംഭാവനാ മാർഗനിർദ്ദേശങ്ങൾ പിന്തുടരുക, പരിപാലകർക്ക് ഈ വാചകം ഉൾപ്പെടുത്തിയാലോ ഇല്ലയാലോ തീരുമാനിക്കാൻ അവകാശം നൽകുക.

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

വിവർത്തനത്തിനിടെ sparse-checkout റിപ്പോസിറ്ററി URL വ്യക്തിഗതമാക്കുക:

```bash
translate -l "ko" --repo-url "https://github.com/org/repo.git"
```

മാർക്കറുകൾ നിലവിലുള്ള പക്ഷം, ഭാഷകൾ ചേർക്കുകയോ മാറ്റം വരുത്തുകയോ ചെയ്യുമ്പോൾ Co-op Translator സൃഷ്ടിച്ച പട്ടിക അപ്‌ഡേറ്റ് ചെയ്യാൻ കഴിയും.

നിലവിലുള്ള README-ലേക്ക്, അതിന്റെ ഭാഷാ-പട്ടിക മാർക്കറുകളുടെ മുകളിൽ ഓപ്ഷണൽ അറ്റ Trib്‌ ഡ്യൂഷനും 'ആരംഭിക്കാനുള്ള' ലിങ്കും അതിന്റെ ഭാഷാ ലിങ്കുകളും മറ്റ് ഉള്ളടക്കവും മാറ്റാതെ ചേർക്കാവുന്നതാണ്. പിന്തുണയുള്ള ഭാഷാ ലിങ്കുകൾ [നിലവിലെ ഭാഷാ ഗൈഡ്](https://github.com/Azure/co-op-translator/blob/main/docs/supported-languages.md) എന്നതിലേക്കു സൂചിപ്പിക്കൂ.