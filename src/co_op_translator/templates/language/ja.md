Japanese mode: preserve Markdown tokens strictly.

Rules (must follow):
1) Keep Markdown links exactly: [text](URL) -> [translated text](same URL).
2) NEVER rewrite links as plain text (e.g., 「text」（URL）, text (URL)).
3) Translate only link text; keep Markdown structure and URL unchanged.
4) Do not add 「」 around a Markdown link unless outside-link grammar requires it.

STRUCTURE IS MORE IMPORTANT THAN STYLE.
Do not optimize Japanese naturalness if Markdown tokens would change.

Example
Source: This document uses [Co-op Translator](https://github.com/Azure/co-op-translator).
Correct: 本書類は [Co-op Translator](https://github.com/Azure/co-op-translator) を使用しています。
Incorrect: 本書類は「Co-op Translator」（https://github.com/Azure/co-op-translator）を使用しています。
