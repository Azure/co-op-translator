<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a6cddf5e9648ef0bba0de7eb07e74cf1",
  "translation_date": "2025-11-06T17:30:29+00:00",
  "source_file": "getting_started/command-reference.md",
  "language_code": "pcm"
}
-->
# Command Reference

Di **Co-op Translator** CLI get plenty options wey you fit use take customize di translation process:

Command                                       | Description
----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"                 | E go translate your project go di language wey you specify. Example: translate -l "es fr de" go translate go Spanish, French, and German. If you use translate -l "all", e go translate go all di languages wey dem support.
translate -l "language_codes" -u              | E go update translations by deleting di ones wey dey before and re-create dem again. Warning: E go delete all di current translations for di languages wey you specify.
translate -l "language_codes" -img            | E go translate only image files.
translate -l "language_codes" -md             | E go translate only Markdown files.
translate -l "language_codes" -nb             | E go translate only Jupyter notebook files (.ipynb).
translate -l "language_codes" --fix           | E go retranslate files wey get low confidence scores based on di previous evaluation results.
translate -l "language_codes" -d              | E go enable debug mode so you fit see detailed logging.
translate -l "language_codes" --save-logs, -s | E go save DEBUG-level logs for files under <root_dir>/logs/ (di console go still dey controlled by -d).
translate -l "language_codes" -r "root_dir"   | E go specify di root directory of di project.
translate -l "language_codes" -f              | E go use fast mode for image translation (e go quick wella, like 3x faster, but e fit reduce di quality and alignment small).
translate -l "language_codes" -y              | E go automatically confirm all prompts (e dey useful for CI/CD pipelines).
translate -l "language_codes" --help          | E go show help details for di CLI, including all di commands wey dey available.
evaluate -l "language_code"                  | E go check di translation quality for one specific language and give you confidence scores.
evaluate -l "language_code" -c 0.8           | E go check translations with custom confidence threshold.
evaluate -l "language_code" -f               | E go do fast evaluation (e go use only rule-based method, no LLM).
evaluate -l "language_code" -D               | E go do deep evaluation (e go use LLM-based method, e dey more thorough but e dey slow).
evaluate -l "language_code" --save-logs, -s  | E go save DEBUG-level logs for files under <root_dir>/logs/.
migrate-links -l "language_codes"             | E go reprocess translated Markdown files to update links to notebooks (.ipynb). If translated notebooks dey, e go prefer dem; if dem no dey, e go use di original notebooks.
migrate-links -l "language_codes" -r          | E go specify di project root directory (di default na di current directory).
migrate-links -l "language_codes" --dry-run   | E go show you which files go change but e no go write di changes.
migrate-links -l "language_codes" --no-fallback-to-original | E no go rewrite links to di original notebooks if di translated ones no dey (e go only update if di translated one dey).
migrate-links -l "language_codes" -d          | E go enable debug mode so you fit see detailed logging.
migrate-links -l "language_codes" --save-logs, -s | E go save DEBUG-level logs for files under <root_dir>/logs/.
migrate-links -l "all" -y                      | E go process all di languages and e go auto-confirm di warning prompt.

## Usage Examples

1. Default behavior (e go add new translations but e no go delete di ones wey dey before):   translate -l "ko"    translate -l "es fr de" -r "./my_project"

2. Add only new Korean image translations (e no go delete di ones wey dey before):    translate -l "ko" -img

3. Update all Korean translations (Warning: E go delete all di Korean translations wey dey before e retranslate dem):    translate -l "ko" -u

4. Update only Korean images (Warning: E go delete all di Korean images wey dey before e retranslate dem):    translate -l "ko" -img -u

5. Add new markdown translations for Korean but e no go touch di other translations:    translate -l "ko" -md

6. Fix low confidence translations based on di previous evaluation results: translate -l "ko" --fix

7. Fix low confidence translations for specific files only (markdown): translate -l "ko" --fix -md

8. Fix low confidence translations for specific files only (images): translate -l "ko" --fix -img

9. Use fast mode for image translation:    translate -l "ko" -img -f

10. Fix low confidence translations with custom threshold: translate -l "ko" --fix -c 0.8

11. Debug mode example: - translate -l "ko" -d: E go enable debug logging.
12. Save logs to files: translate -l "ko" -s
13. Console DEBUG and file DEBUG: translate -l "ko" -d -s

14. Migrate notebook links for Korean translations (e go update links to translated notebooks if dem dey):    migrate-links -l "ko"

15. Migrate links with dry-run (e no go write any file):    migrate-links -l "ko" --dry-run

16. Only update links when translated notebooks dey (e no go fallback to di original ones):    migrate-links -l "ko" --no-fallback-to-original

17. Process all languages with confirmation prompt:    migrate-links -l "all"

18. Process all languages and auto-confirm:    migrate-links -l "all" -y
19. Save logs to files for migrate-links:    migrate-links -l "ko ja" -s

### Evaluation Examples

> [!WARNING]  
> **Beta Feature**: Di evaluation functionality still dey beta. Dem release dis feature to take check translated documents, and di evaluation methods and di way e dey work fit still change.

1. Evaluate Korean translations: evaluate -l "ko"

2. Evaluate with custom confidence threshold: evaluate -l "ko" -c 0.8

3. Fast evaluation (e go use only rule-based method): evaluate -l "ko" -f

4. Deep evaluation (e go use LLM-based method, e dey more thorough but e dey slow): evaluate -l "ko" -D

---

**Disclaimer**:  
Dis dokyument don use AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator) do di translation. Even as we dey try make am accurate, abeg sabi say machine translation fit get mistake or no dey correct well. Di original dokyument wey dey for im native language na di one wey you go take as di correct source. For important information, e better make professional human translation dey use. We no go fit take blame for any misunderstanding or wrong interpretation wey fit happen because you use dis translation.