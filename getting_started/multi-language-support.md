# 🌐 Multi-language support setup

Before starting the translation process, you can add a table in the README that links to the translated versions of your document. Co-op Translator will automatically adjust these links during the translation process, allowing users to seamlessly switch between different language versions.

For example, if a user navigates to the Korean README, they can easily switch to other translations like Spanish or Japanese without leaving the translated page.

Here is an example of how the table should look before running the translation:

## Example

```md
## 🌐 Multi-Language Support

> **Note:**
> These translations were automatically generated using the open-source [co-op-translator](https://github.com/Azure/co-op-translator) and may contain errors or inaccuracies. For critical information, it is recommended to refer to the original or consult a professional human translation. If you'd like to add or update a translation, please refer to the [co-op-translator](https://github.com/Azure/co-op-translator) repository, where you can easily contribute using simple commands.

| Language             | Code | Link to Translated README                               | Last Updated |
|----------------------|------|---------------------------------------------------------|--------------|
| Chinese (Simplified) | zh   | [Chinese Translation](./translations/zh/README.md)      | 2024-10-04   |
| Chinese (Traditional)| tw   | [Chinese Translation](./translations/tw/README.md)      | 2024-10-04   |
| French               | fr   | [French Translation](./translations/fr/README.md)       | 2024-10-04   |
| Japanese             | ja   | [Japanese Translation](./translations/ja/README.md)     | 2024-10-04   |
| Korean               | ko   | [Korean Translation](./translations/ko/README.md)       | 2024-10-04   |
| Spanish              | es   | [Spanish Translation](./translations/es/README.md)      | 2024-10-04   |
```

### Simplified example

```md
## 🌐 Multi-Language Support

| [English](./translations/en/README.md) | [French](./translations/fr/README.md) | [Spanish](./translations/es/README.md) | [German](./translations/de/README.md) | [Russian](./translations/ru/README.md) | [Arabic](./translations/ar/README.md) | [Persian (Farsi)](./translations/fa/README.md) | [Urdu](./translations/ur/README.md) | [Chinese (Simplified)](./translations/zh/README.md) | [Chinese (Traditional, Macau)](./translations/mo/README.md) | [Chinese (Traditional, Hong Kong)](./translations/hk/README.md) | [Chinese (Traditional, Taiwan)](./translations/tw/README.md) | [Japanese](./translations/ja/README.md) | [Korean](./translations/ko/README.md) | [Hindi](./translations/hi/README.md) | [Bengali](./translations/bn/README.md) | [Marathi](./translations/mr/README.md) | [Nepali](./translations/ne/README.md) | [Punjabi (Gurmukhi)](./translations/pa/README.md) | [Portuguese](./translations/pt/README.md) | [Italian](./translations/it/README.md) | [Polish](./translations/pl/README.md) | [Turkish](./translations/tr/README.md) | [Greek](./translations/el/README.md) | [Thai](./translations/th/README.md) | [Swedish](./translations/sv/README.md) | [Danish](./translations/da/README.md) | [Norwegian](./translations/no/README.md) | [Finnish](./translations/fi/README.md) | [Dutch](./translations/nl/README.md) | [Hebrew](./translations/he/README.md) | [Vietnamese](./translations/vi/README.md) | [Indonesian](./translations/id/README.md) | [Malay](./translations/ms/README.md) | [Tagalog (Filipino)](./translations/tl/README.md) | [Swahili](./translations/sw/README.md) | [Hungarian](./translations/hu/README.md) | [Czech](./translations/cs/README.md) | [Slovak](./translations/sk/README.md) | [Romanian](./translations/ro/README.md) | [Bulgarian](./translations/bg/README.md) | [Serbian (Cyrillic)](./translations/sr/README.md) | [Croatian](./translations/hr/README.md) | [Slovenian](./translations/sl/README.md) |

> **Note:**
> These translations were automatically generated using the open-source [co-op-translator](https://github.com/Azure/co-op-translator) and may contain errors or inaccuracies. For critical information, it is recommended to refer to the original or consult a professional human translation. If you'd like to add or update a translation, please refer to the [co-op-translator](https://github.com/Azure/co-op-translator) repository, where you can easily contribute using simple commands.
```

## 🌟 Supported languages

The table below lists the languages currently supported by **Co-op Translator**. It includes language codes, language names, and any known issues associated with each language. If you would like to add support for a new language, please add the corresponding language code, name, and appropriate font in the `font_language_mappings.yml` file located at `src/co_op_translator/fonts/` and submit a pull request after testing.

| Language Code | Language Name        | Font                              | RTL Support | Known Issues |
|---------------|----------------------|-----------------------------------|-------------|--------------|
| en            | English              | NotoSans-Medium.ttf               | No          | No           |
| fr            | French               | NotoSans-Medium.ttf               | No          | No           |
| es            | Spanish              | NotoSans-Medium.ttf               | No          | No           |
| de            | German               | NotoSans-Medium.ttf               | No          | No           |
| ru            | Russian              | NotoSans-Medium.ttf               | No          | No           |
| ar            | Arabic               | NotoSansArabic-Medium.ttf         | Yes         | Yes          |
| fa            | Persian (Farsi)      | NotoSansArabic-Medium.ttf         | Yes         | Yes          |
| ur            | Urdu                 | NotoSansArabic-Medium.ttf         | Yes         | Yes          |
| zh            | Chinese (Simplified) | NotoSansCJK-Medium.ttc            | No          | No           |
| mo            | Chinese (Traditional, Macau) | NotoSansCJK-Medium.ttc           | No          | No           |
| hk            | Chinese (Traditional, Hong Kong) | NotoSansCJK-Medium.ttc           | No          | No           |
| tw            | Chinese (Traditional, Taiwan) | NotoSansCJK-Medium.ttc           | No          | No           |
| ja            | Japanese             | NotoSansCJK-Medium.ttc            | No          | No           |
| ko            | Korean               | NotoSansCJK-Medium.ttc            | No          | No           |
| hi            | Hindi                | NotoSansDevanagari-Medium.ttf     | No          | No           |
| bn            | Bengali              | NotoSansBengali-Medium.ttf        | No          | No           |
| mr            | Marathi              | NotoSansDevanagari-Medium.ttf     | No          | No           |
| ne            | Nepali               | NotoSansDevanagari-Medium.ttf     | No          | No           |
| pa            | Punjabi (Gurmukhi)   | NotoSansGurmukhi-Medium.ttf       | No          | No           |
| pt            | Portuguese           | NotoSans-Medium.ttf               | No          | No           |
| it            | Italian              | NotoSans-Medium.ttf               | No          | No           |
| pl            | Polish               | NotoSans-Medium.ttf               | No          | No           |
| tr            | Turkish              | NotoSans-Medium.ttf               | No          | No           |
| el            | Greek                | NotoSans-Medium.ttf               | No          | No           |
| th            | Thai                 | NotoSansThai-Medium.ttf           | No          | No           |
| sv            | Swedish              | NotoSans-Medium.ttf               | No          | No           |
| da            | Danish               | NotoSans-Medium.ttf               | No          | No           |
| no            | Norwegian            | NotoSans-Medium.ttf               | No          | No           |
| fi            | Finnish              | NotoSans-Medium.ttf               | No          | No           |
| nl            | Dutch                | NotoSans-Medium.ttf               | No          | No           |
| he            | Hebrew               | NotoSansHebrew-Medium.ttf         | Yes         | No           |
| vi            | Vietnamese           | NotoSans-Medium.ttf               | No          | No           |
| id            | Indonesian           | NotoSans-Medium.ttf               | No          | No           |
| ms            | Malay                | NotoSans-Medium.ttf               | No          | No           |
| tl            | Tagalog (Filipino)   | NotoSans-Medium.ttf               | No          | No           |
| sw            | Swahili              | NotoSans-Medium.ttf               | No          | No           |
| hu            | Hungarian            | NotoSans-Medium.ttf               | No          | No           |
| cs            | Czech                | NotoSans-Medium.ttf               | No          | No           |
| sk            | Slovak               | NotoSans-Medium.ttf               | No          | No           |
| ro            | Romanian             | NotoSans-Medium.ttf               | No          | No           |
| bg            | Bulgarian            | NotoSans-Medium.ttf               | No          | No           |
| sr            | Serbian (Cyrillic)   | NotoSans-Medium.ttf               | No          | No           |
| hr            | Croatian             | NotoSans-Medium.ttf               | No          | No           |
| sl            | Slovenian            | NotoSans-Medium.ttf               | No          | No           |

### Adding a new language

To add support for a new language:

1. Go to [src/co_op_translator/fonts/font_language_mappings.yml](https://github.com/Azure/co-op-translator/blob/main/src/co_op_translator/fonts/font_language_mappings.yml).
2. Add the language code, name, and appropriate font file name. Make sure to include the `rtl` attribute if the language is right-to-left.
3. If you need to use a new font, ensure that the font is free to use in open-source projects by checking its licensing and copyright terms. After verifying, add the font file to the `src/co_op_translator/fonts/` directory.
4. Test your changes locally to ensure that the new language is properly supported.
5. Submit a Pull Request with your changes and indicate the addition of the new language in the PR description.

Example:

```yaml
new_lang:
  name: "New Language"
  font: "NotoSans-Medium.ttf"
  rtl: false
```