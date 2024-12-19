# Using Markdown-Only Mode

## Introduction
Markdown-only mode is designed to translate only the Markdown content of your project. This mode bypasses the image translation process and focuses solely on the textual content, making it ideal for scenarios where image translation is not required or the necessary environment variables for Computer Vision are not set.

## When to Use
- When Computer Vision-related environment variables are not configured.
- When you want to translate only the text content without updating image links.
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

This command translates the Markdown content into Korean and updates image links to their original paths, rather than modifying them to translated image paths.

## Behavior
In Markdown-only mode:
- The translation process skips the image translation step.
- Image links in the Markdown remain unchanged, pointing to their original paths.

## Examples
### Before
```markdown
![Image](translated/path/to/image.png)
```
### After using Markdown-only mode
```markdown
![Image](original/path/to/image.png)
```

## Troubleshooting
- Ensure the `-md` option is correctly specified in the command.
- Verify that no Computer Vision environment variables are interfering with the process.

## Conclusion
Markdown-only mode offers a streamlined way to translate text content without modifying image links. It is especially useful when image translation is unnecessary or when working in environments lacking Computer Vision setup.
