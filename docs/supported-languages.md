# Supported Languages

Co-op Translator supports the following language codes for text, notebook, and image translation outputs.

If you want to add a new language, update the language and font mappings under `src/co_op_translator/fonts/` and test the language before opening a pull request.

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

## Temporarily Unsupported Languages

| Language Code | Language Name | Status | Reason |
| --- | --- | --- | --- |
| mni | Manipuri (Meitei Mayek) | Temporarily unsupported | Current model deployments do not reliably produce valid Meitei Mayek output. It is excluded from `all` translations and explicit requests fail before any model call. Support will be re-evaluated after future model updates and restored once translation quality checks pass. |

## Script Quality Validation

Some languages are written in scripts that models do not generate reliably. A weak model may leave the English source in place, romanize the target language in Latin letters, or fall back to a different script. To keep such output from being written as a successful translation, a language can declare a `script_quality` policy in `src/co_op_translator/fonts/font_language_mappings.yml`:

```yaml
mni:
  name: "Manipuri (Meitei Mayek)"
  font: "NotoSansMeeteiMayek-Medium.ttf"
  script_quality:
    required_blocks: ["ABC0-ABFF", "AAE0-AAFF"]   # Meetei Mayek + Extensions
    forbidden_blocks: ["0980-09FF"]               # Bengali script
    min_required_share: 0.6
    max_forbidden_share: 0.02
```

After each chunk is translated, code spans, placeholders, URLs, link destinations and HTML tags are removed and the remaining letters are classified by Unicode block. The chunk is rejected when fewer than `min_required_share` of the letters fall inside `required_blocks`, or more than `max_forbidden_share` fall inside `forbidden_blocks`. Latin letters are allowed up to the remaining share so that product names, identifiers and acronyms can stay in Latin script. Chunks with fewer than `min_letters` letters (default 20) are not judged.

A rejected chunk is retried once with the same prompt. If the retry also fails, the file fails with a `script_quality` error instead of being written, and the `block_retry` translation event carries the measured shares. Agent Framework jobs apply the same check in `finish_markdown_agent_translation` and raise a `ValueError` naming the failing chunks.

Languages without a `script_quality` block are not affected.

## Add a Language

To add support for a new language:

1. Add the language code and display name to the language utilities.
2. Add or map a font in `src/co_op_translator/fonts/font_language_mappings.yml`.
3. Test Markdown and image translation output.
4. Open a pull request with the mapping and validation notes.
