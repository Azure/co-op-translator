# Command reference

Command                                       | Description
----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"                 | Translates your project into specified languages. Example: translate -l "es fr de" translates into Spanish, French, and German. Use translate -l "all" to translate into all supported languages.
translate -l "language_codes" -a              | Adds new translations without deleting existing ones (default behavior).
translate -l "language_codes" -u              | Updates translations by deleting existing ones and re-creating them. Warning: This will delete all current translations for specified languages.
translate -l "language_codes" -img            | Translates only image files.
translate -l "language_codes" -md             | Translates only Markdown files.
translate -l "language_codes" -chk            | Checks translated files for errors and retries translation if needed.
translate -l "language_codes" -d              | Enables debug mode for detailed logging.
translate -l "language_codes" -r "root_dir"   | Specifies the root directory of the project
translate -l "language_codes" -f              | Uses fast mode for image translation (up to 3x faster plotting at a slight cost to quality and alignment).

## CLI options explanation

The **Co-op Translator** CLI offers several options to customize the translation process:

- **`-l` (or `--language-codes`)**: Space-separated list of language codes for translation (e.g., `"es fr de"` for Spanish, French, and German). Use `"all"` to translate into all supported languages.
- **`-r` (or `--root-dir`)**: Specifies the root directory of the project (default is the current directory).
- **`-a` (or `--add`)**: Adds new translations without deleting existing ones (default behavior).
- **`-u` (or `--update`)**: Updates translations by deleting existing ones and re-creating them. **Warning**: This will delete all current translations.
- **`-img` (or `--images`)**: Translates only image files.
- **`-md` (or `--markdown`)**: Translates only markdown files.
- **`-chk` (or `--check`)**: Checks translated files for errors and retries translation if needed.
- **`-d` (or `--debug`)**: Enables debug mode for detailed logging.
- **`-f` (or `--fast`)**: Enables fast mode for image translation. Translations are up to 3x faster plotting, at a slight cost to quality and alignment precision.