<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9b1b247a8d0f1736459e0e9ede0d9c92",
  "translation_date": "2025-05-06T17:43:05+00:00",
  "source_file": "getting_started/markdown-only-mode.md",
  "language_code": "en"
}
-->
# Using Markdown-Only Mode

## Introduction
Markdown-only mode is designed to translate just the Markdown content of your project. This mode skips the image translation process and focuses exclusively on the text, making it ideal for situations where image translation isn’t needed or when the required environment variables for Computer Vision aren’t set.

## When to Use
- When Computer Vision-related environment variables are not configured.
- When you want to translate only the text without changing image links.
- When explicitly specified by the user using the `-md` command-line option.

## How to Enable
To activate Markdown-only mode, use the `-md` option in your command. For example:
```
translate -l "ko" -md
```

Or if the Computer Vision related environment variables are not configured. Running `translate -l "ko"` will automatically switch to Markdown-only mode.

```
translate -l "ko"
```

This command translates the Markdown content into Korean and keeps image links pointing to their original paths instead of changing them to translated image paths.

## Behavior
In Markdown-only mode:
- The translation process skips the image translation step.
- Image links in the Markdown remain unchanged, pointing to their original locations.

## Examples
### Before
```markdown
![Image](../../../getting_started/translated/path/to/image.png)
```
### After using Markdown-only mode
```markdown
![Image](../../../getting_started/original/path/to/image.png)
```

## Troubleshooting
- Make sure the `-md` option is correctly included in the command.
- Check that no Computer Vision environment variables are interfering with the process.

## Conclusion
Markdown-only mode provides a simple way to translate text content without altering image links. It’s especially useful when image translation isn’t needed or when working in environments without a Computer Vision setup.

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we strive for accuracy, please be aware that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not liable for any misunderstandings or misinterpretations arising from the use of this translation.