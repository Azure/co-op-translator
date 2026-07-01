# Languages Wey We Dey Support

Co-op Translator dey support di following language codes for text, notebook, and image translation outputs.

If you wan add new language, update the language and font mappings under `src/co_op_translator/fonts/` and test the language before you open a pull request.

| Language Code | Language Name | Font | RTL Support | Known Issues |
| --- | --- | --- | --- | --- |
| en | English | NotoSans-Medium.ttf | No | No |
| fr | French | NotoSans-Medium.ttf | No | No |
| es | Spanish | NotoSans-Medium.ttf | No | No |
| de | German | NotoSans-Medium.ttf | No | No |
| ru | Russian | NotoSans-Medium.ttf | No | No |
| ar | Arabic | NotoSansArabic-Medium.ttf | Yes | No |
| fa | Persian (Farsi) | NotoSansArabic-Medium.ttf | Yes | No |
| ur | Urdu | NotoSansArabic-Medium.ttf | Yes | No |
| zh-CN | Chinese (Simplified) | NotoSansCJK-Medium.ttc | No | No |
| zh-MO | Chinese (Traditional, Macau) | NotoSansCJK-Medium.ttc | No | No |
| zh-HK | Chinese (Traditional, Hong Kong) | NotoSansCJK-Medium.ttc | No | No |
| zh-TW | Chinese (Traditional, Taiwan) | NotoSansCJK-Medium.ttc | No | No |
| ja | Japanese | NotoSansCJK-Medium.ttc | No | No |
| ko | Korean | NotoSansCJK-Medium.ttc | No | No |
| hi | Hindi | NotoSansDevanagari-Medium.ttf | No | No |
| bn | Bengali | NotoSansBengali-Medium.ttf | No | No |
| mr | Marathi | NotoSansDevanagari-Medium.ttf | No | No |
| ne | Nepali | NotoSansDevanagari-Medium.ttf | No | No |
| pa | Punjabi (Gurmukhi) | NotoSansGurmukhi-Medium.ttf | No | No |
| pt-PT | Portuguese (Portugal) | NotoSans-Medium.ttf | No | No |
| pt-BR | Portuguese (Brazil) | NotoSans-Medium.ttf | No | No |
| it | Italian | NotoSans-Medium.ttf | No | No |
| lt | Lithuanian | NotoSans-Medium.ttf | No | No |
| pl | Polish | NotoSans-Medium.ttf | No | No |
| tr | Turkish | NotoSans-Medium.ttf | No | No |
| el | Greek | NotoSans-Medium.ttf | No | No |
| th | Thai | NotoSansThai-Medium.ttf | No | No |
| sv | Swedish | NotoSans-Medium.ttf | No | No |
| da | Danish | NotoSans-Medium.ttf | No | No |
| no | Norwegian | NotoSans-Medium.ttf | No | No |
| fi | Finnish | NotoSans-Medium.ttf | No | No |
| nl | Dutch | NotoSans-Medium.ttf | No | No |
| he | Hebrew | NotoSansHebrew-Medium.ttf | Yes | No |
| vi | Vietnamese | NotoSans-Medium.ttf | No | No |
| id | Indonesian | NotoSans-Medium.ttf | No | No |
| ms | Malay | NotoSans-Medium.ttf | No | No |
| tl | Tagalog (Filipino) | NotoSans-Medium.ttf | No | No |
| sw | Swahili | NotoSans-Medium.ttf | No | No |
| hu | Hungarian | NotoSans-Medium.ttf | No | No |
| cs | Czech | NotoSans-Medium.ttf | No | No |
| sk | Slovak | NotoSans-Medium.ttf | No | No |
| ro | Romanian | NotoSans-Medium.ttf | No | No |
| bg | Bulgarian | NotoSans-Medium.ttf | No | No |
| sr | Serbian (Cyrillic) | NotoSans-Medium.ttf | No | No |
| hr | Croatian | NotoSans-Medium.ttf | No | No |
| sl | Slovenian | NotoSans-Medium.ttf | No | No |
| uk | Ukrainian | NotoSans-Medium.ttf | No | No |
| my | Burmese (Myanmar) | NotoSansMyanmar-Medium.ttf | No | No |
| ta | Tamil | NotoSansTamil-Medium.ttf | No | No |
| et | Estonian | NotoSans-Medium.ttf | No | No |
| pcm | Nigerian Pidgin | NotoSans-Medium.ttf | No | No |
| te | Telugu | NotoSans-Medium.ttf | No | No |
| ml | Malayalam | NotoSans-Medium.ttf | No | No |
| kn | Kannada | NotoSans-Medium.ttf | No | No |
| km | Khmer | NotoSansKhmer-Medium.ttf | No | No |

## How You Go Add Language

To add support for a new language:

1. Add di language code and di display name to di language utilities.
2. Add or map a font in `src/co_op_translator/fonts/font_language_mappings.yml`.
3. Test di Markdown and image translation output.
4. Open a pull request wey get di mapping and validation notes.