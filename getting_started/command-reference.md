# Command reference

Command                                       | Description
----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"                 | Translates your project into specified languages. Example: translate -l "es fr de" translates into Spanish, French, and German. Use translate -l "all" to translate into all supported languages.
translate -l "language_codes" -u              | Updates translations by deleting existing ones and re-creating them. Warning: This will delete all current translations for specified languages.
translate -l "language_codes" -img            | Translates only image files.
translate -l "language_codes" -md             | Translates only Markdown files.
translate -l "language_codes" -chk            | Checks translated files for errors and retries translation if needed.
translate -l "language_codes" -d              | Enables debug mode for detailed logging.
translate -l "language_codes" -r "root_dir"   | Specifies the root directory of the project
translate -l "language_codes" -f              | Uses fast mode for image translation (up to 3x faster plotting at a slight cost to quality and alignment).

## CLI options explanation

The **Co-op Translator** CLI offers several options to customize the translation process:

  -l, --language-codes TEXT  Space-separated language codes for translation
                             (e.g., "es fr de" or "all").  [required]
  -r, --root-dir TEXT        Root directory of the project (default is current
                             directory).
  -u, --update               Update translations by deleting and recreating
                             them (Warning: Existing translations will be
                             lost).
  -img, --images             Only translate image files.
  -md, --markdown            Only translate markdown files.
  -d, --debug                Enable debug mode.
  -chk, --check              Check translated files for errors and retry
                             translation if needed.
  -f, --fast                 Use fast mode for image translation (up to 3x
                             faster at a slight cost to quality and
                             alignment).
  -y, --yes                  Automatically confirm all prompts (useful for
                             CI/CD pipelines).
  --help                     Show this message and exit.


### Usage examples:

  1. Default behavior (add new translations without deleting existing ones):
  translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. Add only new Korean image translations (no existing translations are
  deleted):    translate -l "ko" -img

  3. Update all Korean translations (Warning: This deletes all existing Korean
  translations before re-translating):    translate -l "ko" -u

  4. Update only Korean images (Warning: This deletes all existing Korean
  images before re-translating):    translate -l "ko" -img -u

  5. Add new markdown translations for Korean without affecting other
  translations:    translate -l "ko" -md

  6. Check translated files for errors and retry translations if necessary:
  translate -l "ko" -chk

  7. Check translated files for errors and retry translations (only markdown):
  translate -l "ko" -chk -md

  8. Check translated files for errors and retry translations (only images):
  translate -l "ko" -chk -img

  9. Use fast mode for image translation:    translate -l "ko" -img -f

  Debug mode example: - translate -l "ko" -d: Enable debug logging.

