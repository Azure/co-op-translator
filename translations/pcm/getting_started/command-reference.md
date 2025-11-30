<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "822238e4451d04bb152cebb1be6f13c2",
  "translation_date": "2025-11-30T13:07:46+00:00",
  "source_file": "getting_started/command-reference.md",
  "language_code": "pcm"
}
-->
# Command reference

Di **Co-op Translator** CLI get plenti options wey fit help you customize how you go take translate:

Command                                       | Wetin e mean
----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"                 | E go translate your project go inside di languages wey you specify. Example: translate -l "es fr de" go translate am go Spanish, French, and German. Use translate -l "all" to translate am go all di languages wey e support.
translate -l "language_codes" -u              | E go update di translations by deleting di ones wey dey before and create new ones. Warning: E go delete all di translations wey dey for di languages wey you specify.
translate -l "language_codes" -img            | E go translate only di image files dem.
translate -l "language_codes" -md             | E go translate only di Markdown files dem.
translate -l "language_codes" -nb             | E go translate only Jupyter notebook files (.ipynb).
translate -l "language_codes" --fix           | E go retranslate files wey get low confidence scores based on di previous evaluation results.
translate -l "language_codes" -d              | E go enable debug mode for detailed logging.
translate -l "language_codes" --save-logs, -s | E go save DEBUG-level logs for files under <root_dir>/logs/ (console still dey controlled by -d)
translate -l "language_codes" -r "root_dir"   | E go specify di root directory of di project
translate -l "language_codes" -f              | E go use fast mode for image translation (fit do am up to 3x faster but small small quality and alignment go reduce).
translate -l "language_codes" -y              | E go automatically confirm all prompts (good for CI/CD pipelines)
translate -l "language_codes" --add-disclaimer/--no-disclaimer | E go enable or disable adding machine translation disclaimer section to translated markdown and notebooks (default: enabled).
translate -l "language_codes" --help          | Help details inside di CLI wey show di commands wey dey available
evaluate -l "language_code"                  | E go evaluate translation quality for one language and give confidence scores
evaluate -l "language_code" -c 0.8           | E go evaluate translations with custom confidence threshold
evaluate -l "language_code" -f               | Fast evaluation mode (rule-based only, no LLM)
evaluate -l "language_code" -D               | Deep evaluation mode (LLM-based only, more thorough but slower)
evaluate -l "language_code" --save-logs, -s  | E go save DEBUG-level logs for files under <root_dir>/logs/
migrate-links -l "language_codes"             | E go reprocess translated Markdown files to update links to notebooks (.ipynb). E prefer translated notebooks if dem dey; if no, e fit use original notebooks.
migrate-links -l "language_codes" -r          | E go specify di project root directory (default na current directory).
migrate-links -l "language_codes" --dry-run   | E go show which files go change but e no go write any change.
migrate-links -l "language_codes" --no-fallback-to-original | E no go rewrite links to original notebooks if translated ones no dey (e go update only if translated ones dey).
migrate-links -l "language_codes" -d          | E go enable debug mode for detailed logging.
migrate-links -l "language_codes" --save-logs, -s | E go save DEBUG-level logs for files under <root_dir>/logs/
migrate-links -l "all" -y                      | E go process all languages and auto-confirm di warning prompt.

## Usage examples

  1. Default way (add new translations without deleting di ones wey dey before):   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. Add only new Korean image translations (no existing translations go delete):    translate -l "ko" -img

  3. Update all Korean translations (Warning: E go delete all di Korean translations wey dey before before e re-translate):    translate -l "ko" -u

  4. Update only Korean images (Warning: E go delete all di Korean images wey dey before before e re-translate):    translate -l "ko" -img -u

  5. Add new markdown translations for Korean without touching other translations:    translate -l "ko" -md

  6. Fix low confidence translations based on previous evaluation results: translate -l "ko" --fix

  7. Fix low confidence translations for specific files only (markdown): translate -l "ko" --fix -md

  8. Fix low confidence translations for specific files only (images): translate -l "ko" --fix -img

  9. Use fast mode for image translation:    translate -l "ko" -img -f

  10. Fix low confidence translations with custom threshold: translate -l "ko" --fix -c 0.8

  11. Debug mode example: - translate -l "ko" -d: E go enable debug logging.
  12. Save logs to files: translate -l "ko" -s
  13. Console DEBUG and file DEBUG: translate -l "ko" -d -s
  14. Translate without adding machine translation disclaimers to outputs: translate -l "ko" --no-disclaimer

  15. Migrate notebook links for Korean translations (update links to translated notebooks if dem dey):    migrate-links -l "ko"

  15. Migrate links with dry-run (no file writes):    migrate-links -l "ko" --dry-run

  16. Only update links if translated notebooks dey (no fallback to originals):    migrate-links -l "ko" --no-fallback-to-original

  17. Process all languages with confirmation prompt:    migrate-links -l "all"

  18. Process all languages and auto-confirm:    migrate-links -l "all" -y
  19. Save logs to files for migrate-links:    migrate-links -l "ko ja" -s

### Evaluation Examples

> [!WARNING]  
> **Beta Feature**: Di evaluation function dey beta now. Dem release am to evaluate translated documents, but di evaluation methods and how e work well well still dey develop and fit change.

  1. Evaluate Korean translations: evaluate -l "ko"

  2. Evaluate with custom confidence threshold: evaluate -l "ko" -c 0.8

  3. Fast evaluation (rule-based only): evaluate -l "ko" -f

  4. Deep evaluation (LLM-based only): evaluate -l "ko" -D

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document na wetin AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator) translate. Even though we try make e correct, abeg sabi say automated translation fit get some mistakes or no too correct. Di original document wey e dey for im own language na di correct one. If na serious matter, e better make person wey sabi translate am well do am. We no go responsible if person no understand well or if dem use dis translation do wrong tin.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->