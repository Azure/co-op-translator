Manipuri (Meitei Mayek) mode: write Manipuri in Unicode Meitei Mayek script.

Rules (must follow):
1) The target language is Manipuri (Meiteilon). Translate the meaning into natural Manipuri.
2) Write ALL Manipuri text using Unicode Meitei Mayek (Meetei Mayek) characters from the U+ABC0-U+ABFF block.
3) NEVER write Manipuri in Bengali script (U+0980-U+09FF), Devanagari, or Latin transliteration. Bengali-script Manipuri is NOT acceptable output.
4) End Manipuri sentences with the Meitei Mayek full stop ꯫ (cheikhei); keep all other punctuation as in the source.
5) Keep numbers, version strings, and dates as ASCII digits; do not convert them to Meitei Mayek digits.
6) Do not translate or transliterate product names, programming languages, APIs, commands, identifiers, URLs, file paths, or code; keep them exactly in Latin script.
7) Keep Markdown links exactly: [text](URL) -> [translated text](same URL). Translate only the link text.

STRUCTURE IS MORE IMPORTANT THAN STYLE.
Do not optimize Manipuri naturalness if Markdown tokens would change.

Example
Source: This document uses [Co-op Translator](https://github.com/Azure/co-op-translator).
Correct: ꯗꯣꯀꯨꯃꯦꯟꯠ ꯑꯁꯤꯅꯥ [Co-op Translator](https://github.com/Azure/co-op-translator) ꯁꯤꯖꯤꯟꯅꯩ꯫
Incorrect (Bengali script): ডকুমেন্ট অসিনা [Co-op Translator](https://github.com/Azure/co-op-translator) শিজিন্নৈ।
