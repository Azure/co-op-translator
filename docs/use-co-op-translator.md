# Use Co Op translator in your project

The Co-Op Translator is a command-line interface (CLI) tool that helps you translate markdown and image files in your project into multiple languages. This tutorial explains how to use the CLI and describes which commands to use in specific scenarios.

## CLI Options Overview

The Co-Op Translator CLI provides several options to customize the translation process:

- **`-l` (or `--language-codes`)**: Space-separated list of language codes for translation. For example, `"es fr de"` translates to Spanish, French, and German. Use `"all"` to translate into all supported languages.

- **`-r` (or `--root-dir`)**: The root directory of the project (default is the current directory).

- **`-a` (or `--add`)**: Adds new translations without deleting existing ones (default behavior).

- **`-u` (or `--update`)**: Updates translations by deleting all existing translations and recreating them. **Warning**: This will delete existing translations.

- **`-img` (or `--images`)**: Translates only image files.

- **`-md` (or `--markdown`)**: Translates only markdown files.

- **`-chk` (or `--check`)**: Checks translated files for errors and retries the translation if needed.

- **`-d` (or `--debug`)**: Enables debug mode for detailed logging.

## Example Scenarios and Commands

### 1. Basic Translation (Single Language)

If you want to translate your project into a single language, like Korean, use the following command:

```bash
translate -l "ko"
```

This command translates all markdown and image files into Korean and adds the translations without deleting any existing ones.

### 2. Translating Multiple Languages

To translate your project into multiple languages (e.g., Spanish, French, and German), use this command:

```bash
translate -l "es fr de"
```

This command will translate the project into Spanish, French, and German, adding new translations without overwriting existing ones.

### 3. Specifying the Root Directory

By default, the translator uses the current working directory. If your project is located elsewhere, specify the root directory with the -r option:

```bash
translate -l "es fr de" -r "./my_project"
```

This command translates the files in `./my_project` into Spanish, French, and German.

### 4. Add New Translations Without Deleting Existing Ones

The default behavior is to add new translations without deleting existing ones. You can explicitly specify this by using the `-a` option:

```bash
translate -l "ko" -a
```

This command will add new translations in Korean without affecting the existing translations.

### 5. Updating Translations (Deletes Existing Translations)

To update existing translations (i.e., delete the current translations and replace them with new ones), use the `-u` option. This will delete all existing translations for the specified languages and re-translate them.

```bash
translate -l "ko" -u
```

Warning: This command will prompt you for confirmation before proceeding with deleting the existing translations.

### 6. Translating Only Images

To translate only the image files in your project, use the `-img` option:

```bash
translate -l "ko" -img
```

This command will translate only the images into Korean, without affecting any markdown files.

### Translating Only Markdown Files

To translate only the markdown files in your project, use the `-md` option:

```bash
translate -l "ko" -md
```

### 8. Checking for Errors in Translated Files

If you want to check translated files for errors and retry the translation if necessary, use the `-chk` option:

```bash
translate -l "ko" -chk
```

This command will scan the translated files and retry translation for any files with errors. You can also use this option with `-img` or `-md` to check errors only in images or markdown files.

### 9. Debug Mode

To enable detailed logging for troubleshooting, use the `-d` option:

```bash
translate -l "ko" -d
```

This command will run the translation in debug mode, providing additional logging information that can help you identify issues during the translation process.

### 10. Translating All Languages

If you want to translate the project into all supported languages, use the all keyword.

> [!WARNING]
> Translating all languages at once can take a significant amount of time depending on the project size. For example, translating the Phi-3 CookBook into Spanish took about 1 hour and 25-30 minutes. Given the scale, it's not practical for one person to handle 20 languages. It's recommended to split the work among multiple contributors, each managing one or two languages, and update translations gradually.


```bash
translate -l "all"
```

This command will translate the project into all available languages. If you proceed, the translation may take a significant amount of time depending on the size of the project.
