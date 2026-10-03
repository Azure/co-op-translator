# README 언어 템플릿

Co-op Translator는 번역된 콘텐츠를 게시하는 리포지토리의 README 언어 표를 유지할 수 있습니다.

Co-op Translator가 각 번역 실행마다 전체 섹션을 교체하도록 하려면 아래 마커를 사용하세요. 사용자 지정 하위집합을 수동으로 유지하려면 마커를 제거하세요.

마커 위의 출처 표기와 시작하기 링크는 선택 사항입니다. 이 항목들은 독자들이 번역이 어떻게 관리되는지와 자신들의 리포지토리를 어떻게 번역할 수 있는지를 알 수 있도록 도와줍니다. 언어 표가 업데이트될 때 해당 항목이 보존되도록 마커 바깥에 두세요. 다른 리포지토리를 업데이트할 때에는 기여 지침을 따르고 유지 관리자가 이 텍스트를 포함할지 여부를 결정하도록 하세요.

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

번역하는 동안 sparse-checkout 저장소 URL을 개인화하세요:

```bash
translate -l "ko" --repo-url "https://github.com/org/repo.git"
```

마커가 있으면 Co-op Translator는 언어가 추가되거나 변경될 때 생성된 표를 업데이트할 수 있습니다.

기존 README의 경우, 언어 표 마커 위에 선택적 출처 표기 및 시작하기 링크를 언어 링크나 다른 내용을 교체하지 않고 추가할 수 있습니다. 지원되는 언어 링크를 [현재 언어 가이드](https://github.com/Azure/co-op-translator/blob/main/docs/supported-languages.md)로 연결하세요.