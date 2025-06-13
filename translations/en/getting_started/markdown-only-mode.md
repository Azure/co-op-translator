<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9b1b247a8d0f1736459e0e9ede0d9c92",
  "translation_date": "2025-06-12T11:35:28+00:00",
  "source_file": "getting_started/markdown-only-mode.md",
  "language_code": "en"
}
-->
# Using Markdown-Only Mode

## Introduction
Markdown-only mode is designed to translate only the Markdown content of your project. This mode skips the image translation process and focuses solely on the text, making it ideal for situations where image translation isn’t needed or when the required environment variables for Computer Vision aren’t set.

## When to Use
- When Computer Vision-related environment variables aren’t configured.
- When you want to translate just the text content without changing image links.
- When the user explicitly specifies it using the `-md` command-line option.

## How to Enable
To activate Markdown-only mode, use the `-md` option in your command. For example:
```
translate -l "ko" -md
```

Or if the Computer Vision related environment variables aren’t set, running `translate -l "ko"` will automatically switch to Markdown-only mode.

```
translate -l "ko"
```

This command translates the Markdown content into Korean and keeps image links pointing to their original paths, instead of changing them to translated image paths.

## Behavior
In Markdown-only mode:
- The translation process skips the image translation step.
- Image links in the Markdown remain unchanged, still pointing to their original paths.

## Examples
### Before
```markdown
![Image](../../../translated_images/image.aa98bae4d78871bb3b23ac9f938ff86539da4cd6fb4c52dafedc4665135c3d61.en.png)
```
### After using Markdown-only mode
```markdown
![Image](../../../translated_images/image.fc8708ffe1e1ca12c38822b1a382726da4b232025d1daa8a50ab75c8635d0c4a.en.png)
```

## Troubleshooting
- Make sure the `-md` option is correctly included in the command.
- Check that no Computer Vision environment variables are interfering with the process.

## Conclusion
Markdown-only mode provides a streamlined way to translate text content without altering image links. It’s especially useful when image translation isn’t necessary or when working in environments without a Computer Vision setup.

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we strive for accuracy, please be aware that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not liable for any misunderstandings or misinterpretations arising from the use of this translation.