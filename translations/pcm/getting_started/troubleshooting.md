<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6e626bef5ed78a1cc55b0dbf44f01d47",
  "translation_date": "2025-11-06T17:31:10+00:00",
  "source_file": "getting_started/troubleshooting.md",
  "language_code": "pcm"
}
-->
# Microsoft Co-op Translator Troubleshooting Guide


## Overview
Microsoft Co-Op Translator na strong tool wey dey help translate Markdown documents well. Dis guide go help you solve common wahala wey fit happen wen you dey use di tool.

## Common Wahala and Solution

### 1. Markdown Tag Wahala
**Wahala:** Di translated Markdown document get `markdown` tag for di top, wey dey cause problem for di rendering.

**Solution:** To solve am, just delete di `markdown` tag wey dey di top of di file. Dis go make di Markdown file render well.

**Steps:**
1. Open di translated Markdown (`.md`) file.
2. Find di `markdown` tag wey dey di top of di document.
3. Delete di `markdown` tag.
4. Save di changes for di file.
5. Open di file again to make sure say e dey render well.

### 2. Embedded Images URL Wahala
**Wahala:** Di URLs of embedded images no match di language locale, e dey cause wrong or missing images.

**Solution:** Check di URL of di embedded images and make sure say e match di language locale. All images dey inside di `translated_images` folder and each image get language locale tag for di image file name.

**Steps:**
1. Open di translated Markdown document.
2. Look di embedded images and dia URLs.
3. Check say di language locale for di image file name match di document language.
4. Update di URLs if e dey necessary.
5. Save di changes and open di document again to confirm say di images dey render well.

### 3. Translation Accuracy
**Wahala:** Di translated content no dey accurate or e need more editing.

**Solution:** Check di translated document well and make di changes wey go make am better.

**Steps:**
1. Open di translated document.
2. Look di content well.
3. Make di changes wey go make di translation accurate.
4. Save di changes.

## 4. Permission Error Redacted or 404

If images or text no translate to di correct language and wen you dey run am for -d debug mode you see 401 error. Dis na authentication problem—e fit be say di key no correct, e don expire, or e no dey linked to di endpoint region.

Run co-op translator with di [-d debug switch](https://github.com/Azure/co-op-translator/blob/main/getting_started/command-reference.md) to understand di root cause.

- **Error Message**: `Access denied due to invalid subscription key or wrong API endpoint.`
- **Possible Causes**:
  - Subscription key no correct or e dey redacted for di request.
  - AI Services Key or Subscription Key fit belong to different Azure resource (like Translator or OpenAI) instead of **Azure AI Vision** resource.

 **Resource Type**
  - Go di [Azure Portal](https://portal.azure.com) or [Azure AI Foundry](https://ai.azure.com) and make sure say di resource na `Azure AI services` → `Vision`.
  - Check di keys and make sure say di correct key dey used.

## 5. Configuration Errors (New Error Handling)

Starting with di new selective translation system, Co-op Translator dey show clear error messages wen di required services no dey configured.

### 5.1. Azure AI Service No Configure for Image Translation

**Wahala:** You request image translation (`-img` flag) but Azure AI Service no configure well.

**Error Message:**
```
Error: Image translation requested but Azure AI Service is not configured.
Please add AZURE_AI_SERVICE_API_KEY and AZURE_AI_SERVICE_ENDPOINT to your .env file.
Check Azure AI Service availability and configuration.
```

**Solution:**
1. **Option 1**: Configure Azure AI Service
   - Add `AZURE_AI_SERVICE_API_KEY` for your `.env` file
   - Add `AZURE_AI_SERVICE_ENDPOINT` for your `.env` file
   - Make sure say di service dey accessible

2. **Option 2**: Remove image translation request
   ```bash
   # Instead of: translate -l "ko" -img
   # Use: translate -l "ko" -md
   ```

### 5.2. Missing Required Configuration

**Wahala:** Important LLM configuration no dey.

**Error Message:**
```
Error: No language model configuration found.
Please configure either Azure OpenAI or OpenAI in your .env file.
```

**Solution:**
1. Check say your `.env` file get at least one of di following LLM configurations:
   - **Azure OpenAI**: `AZURE_OPENAI_API_KEY` and `AZURE_OPENAI_ENDPOINT`
   - **OpenAI**: `OPENAI_API_KEY`
   
   You need either Azure OpenAI OR OpenAI configured, no be both.

### 5.3. Selective Translation Confusion

**Wahala:** No files translate even though di command work.

**Possible Causes:**
- Wrong file type flags (`-md`, `-img`, `-nb`)
- No matching files dey di project
- Directory structure no correct

**Solution:**
1. **Use debug mode** to see wetin dey happen:
   ```bash
   translate -l "ko" -md -d
   ```

2. **Check file types** wey dey your project:
   ```bash
   # For markdown files
   find . -name "*.md" -not -path "./translations/*"
   
   # For notebooks
   find . -name "*.ipynb" -not -path "./translations/*"
   
   # For images
   find . -name "*.png" -o -name "*.jpg" -o -name "*.jpeg" -not -path "./translations/*"
   ```

3. **Verify flag combinations**:
   ```bash
   # Translate everything (default)
   translate -l "ko"
   
   # Translate specific types
   translate -l "ko" -md -img
   ```

## 6. Migration from Old System

### 6.1. Markdown-Only Mode Don Stop

**Wahala:** Commands wey dey depend on automatic markdown-only fallback no dey work as e suppose be.

**Old Behavior:**
```bash
# This used to automatically switch to markdown-only mode
translate -l "ko"  # (when Azure AI Vision was not configured)
```

**New Behavior:**
```bash
# This now produces an error if image translation is requested but not configured
translate -l "ko" -img
```

**Solution:**
- **Talk am clear** wetin you wan translate:
  ```bash
  translate -l "ko" -md        # Only markdown
  translate -l "ko" -md -img   # Markdown and images
  translate -l "ko"            # Everything (if all services configured)
  ```

### 6.2. Unexpected Link Behavior

**Wahala:** Links for translated files dey point to wrong places.

**Cause:** Dynamic link processing dey change based on di file types wey you select.

**Solution:**
1. **Understand di new link behavior**:
   - `-nb` dey included: Notebook links dey point to translated versions
   - `-nb` dey excluded: Notebook links dey point to original files
   - `-img` dey included: Image links dey point to translated versions
   - `-img` dey excluded: Image links dey point to original files

2. **Choose di correct combination** wey fit your use case:
   ```bash
   # All internal links point to translated versions
   translate -l "ko" -md -img -nb
   
   # Only markdown translated, other links point to originals
   translate -l "ko" -md
   ```

## 7. GitHub Action run but no Pull Request (PR) create

**Symptom:** Di workflow logs for `peter-evans/create-pull-request` show:

> Branch 'update-translations' no dey ahead of base 'main' and e no go create

**Likely causes:**
- **No changes detect:** Di translation step no produce any diffs (repo don already dey up to date).
- **Ignored outputs:** `.gitignore` dey exclude files wey you dey expect to commit (e.g., `*.ipynb`, `translations/`, `translated_images/`).
- **add-paths mismatch:** Di paths wey dey provided to di action no match di actual output locations.
- **Workflow logic/conditions:** Di translation step stop early or e write to wrong directories.

**How to fix / verify:**
1. **Confirm outputs dey:** After translation, check say workspace get new/changed files for `translations/` and/or `translated_images/`.
   - If you dey translate notebooks, make sure say `.ipynb` files dey actually write under `translations/<lang>/...`.
2. **Check `.gitignore`:** No ignore di generated outputs. Make sure say you no dey ignore:
   - `translations/`
   - `translated_images/`
   - `*.ipynb` (if you dey translate notebooks)
3. **Make sure add-paths match outputs:** Use multiline value and include both folders if e dey necessary:
   ```yaml
   with:
     add-paths: |
       translations/
       translated_images/
   ```
4. **Force PR for debugging:** Allow empty commits for small time to confirm say wiring dey correct:
   ```yaml
   with:
     commit-empty: true
   ```
5. **Run with debug:** Add `-d` to di translate command to show wetin files dem discover and write.
6. **Permissions (GITHUB_TOKEN):** Make sure say di workflow get write permissions to create commits and PRs:
   ```yaml
   permissions:
     contents: write
     pull-requests: write
   ```

## Quick Debugging Checklist

Wen you dey troubleshoot translation wahala:

1. **Use debug mode**: Add `-d` flag to see detailed logs
2. **Check your flags**: Make sure say `-md`, `-img`, `-nb` match wetin you wan do
3. **Verify configuration**: Check say your `.env` file get di required keys
4. **Test small small**: Start with `-md` only, then add other types
5. **Check file structure**: Make sure say source files dey and dem dey accessible

For more detailed information about di available commands and flags, see di [Command Reference](./command-reference.md).

---

**Disclaimer**:  
Dis dokyument don use AI transle-shon service [Co-op Translator](https://github.com/Azure/co-op-translator) do di transle-shon. Even as we dey try make am accurate, abeg make you sabi say transle-shon wey machine do fit get mistake or no dey correct well. Di original dokyument for im native language na di one wey you go take as di correct source. For important mata, e good make you use professional human transle-shon. We no go fit take blame for any misunderstanding or wrong interpretation wey fit happen because you use dis transle-shon.