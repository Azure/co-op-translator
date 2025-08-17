# Command reference

The **Co-op Translator** CLI offers several options to customize the translation process:

Command                                       | Description
----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"                 | Translates your project into specified languages. Example: translate -l "es fr de" translates into Spanish, French, and German. Use translate -l "all" to translate into all supported languages.
translate -l "language_codes" -u              | Updates translations by deleting existing ones and re-creating them. Warning: This will delete all current translations for specified languages.
translate -l "language_codes" -img            | Translates only image files.
translate -l "language_codes" -md             | Translates only Markdown files.
translate -l "language_codes" -nb             | Translates only Jupyter notebook files (.ipynb).
translate -l "language_codes" --fix           | Retranslates files with low confidence scores based on previous evaluation results.
translate -l "language_codes" -d              | Enables debug mode for detailed logging.
translate -l "language_codes" -r "root_dir"   | Specifies the root directory of the project
translate -l "language_codes" -f              | Uses fast mode for image translation (up to 3x faster plotting at a slight cost to quality and alignment).
translate -l "language_codes" -y              | Automatically confirm all prompts (useful for CI/CD pipelines)
translate -l "language_codes" --help          | help details within the CLI showing available commands
evaluate -l "language_code"                  | Evaluates translation quality for a specific language and provides confidence scores
evaluate -l "language_code" -c 0.8           | Evaluates translations with custom confidence threshold
evaluate -l "language_code" -f               | Fast evaluation mode (rule-based only, no LLM)
evaluate -l "language_code" -D               | Deep evaluation mode (LLM-based only, more thorough but slower)

## Usage examples

  1. Default behavior (add new translations without deleting existing ones):   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. Add only new Korean image translations (no existing translations are deleted):    translate -l "ko" -img

  3. Update all Korean translations (Warning: This deletes all existing Korean translations before re-translating):    translate -l "ko" -u

  4. Update only Korean images (Warning: This deletes all existing Korean images before re-translating):    translate -l "ko" -img -u

  5. Add new markdown translations for Korean without affecting other translations:    translate -l "ko" -md

  6. Fix low confidence translations based on previous evaluation results: translate -l "ko" --fix

  7. Fix low confidence translations for specific files only (markdown): translate -l "ko" --fix -md

  8. Fix low confidence translations for specific files only (images): translate -l "ko" --fix -img

  9. Use fast mode for image translation:    translate -l "ko" -img -f

  10. Fix low confidence translations with custom threshold: translate -l "ko" --fix -c 0.8

  11. Debug mode example: - translate -l "ko" -d: Enable debug logging.

### Evaluation Examples

> [!WARNING]  
> **Beta Feature**: The evaluation functionality is currently in beta. This feature was released to evaluate translated documents, and the evaluation methods and detailed implementation are still under development and subject to change.

  1. Evaluate Korean translations: evaluate -l "ko"

  2. Evaluate with custom confidence threshold: evaluate -l "ko" -c 0.8

  3. Fast evaluation (rule-based only): evaluate -l "ko" -f

  4. Deep evaluation (LLM-based only): evaluate -l "ko" -D
