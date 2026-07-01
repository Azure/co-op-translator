# README ഭാഷകൾ ടെംപ്ലേറ്റ്

Co-op Translator പരിഭാഷചെയ്ത ഉള്ളടക്കം പ്രസിദ്ധീകരിക്കുന്ന റിപോസിറ്ററികളെക്കായുള്ള README ഭാഷാപട്ടിക പരിപാലിക്കാവുന്നതാണ്.

ഓരോ പരിഭാഷ റൺ സമയത്തും മുഴുവൻ വിഭാഗം Co-op Translator മാറ്റാൻ നിങ്ങൾ ആഗ്രഹിക്കുന്നുവെങ്കിൽ താഴെയുള്ള മാർക്കറുകൾ ഉപയോഗിക്കുക. നിങ്ങൾ ഒരു ഇഷ്ടാനുസൃത സബ്സെറ്റ് മാനുവലായി പരിപാലിക്കാൻ ഇഷ്ടപ്പെടുന്നുവെങ്കിൽ മാർക്കറുകൾ നീക്കംചെയ്യുക.

````markdown
### Multi-Language Support

#### Supported by [Co-op Translator](https://github.com/Azure/co-op-translator)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](../zh-HK/README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Khmer](../km/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](./README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

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

പരിഭാഷ ചെയ്യുമ്പോൾ sparse-checkout റിപോസിറ്ററി URL വ്യക്തിഗതമാക്കുക:

```bash
translate -l "ko" --repo-url "https://github.com/org/repo.git"
```

മാർക്കറുകൾ ഉണ്ടായിരുന്നാൽ, ഭാഷകൾ ചേർക്കുകയോ മാറ്റുകയോ ചെയ്യുന്നപ്പോൾ Co-op Translator സൃഷ്ടിച്ച പട്ടിക പുതുക്കാൻ കഴിയും.