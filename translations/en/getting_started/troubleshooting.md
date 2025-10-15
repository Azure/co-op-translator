<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6e626bef5ed78a1cc55b0dbf44f01d47",
  "translation_date": "2025-10-15T02:06:10+00:00",
  "source_file": "getting_started/troubleshooting.md",
  "language_code": "en"
}
-->
# Microsoft Co-op Translator Troubleshooting Guide

## Overview
The Microsoft Co-Op Translator is a robust tool for translating Markdown documents smoothly. This guide will help you resolve common problems you might encounter while using it.

## Common Issues and Solutions

### 1. Markdown Tag Issue
**Problem:** The translated Markdown file has a `markdown` tag at the top, which causes display problems.

**Solution:** Just remove the `markdown` tag from the top of the file. This will fix the rendering issue.

**Steps:**
1. Open the translated Markdown (`.md`) file.
2. Find the `markdown` tag at the very top.
3. Delete the `markdown` tag.
4. Save the file.
5. Re-open it to check that it displays properly.

### 2. Embedded Images URL Issue
**Problem:** The URLs for embedded images don’t match the language locale, so images are missing or incorrect.

**Solution:** Make sure the image URLs match the language locale. All images are stored in the `translated_images` folder, and each image filename includes a language locale tag.

**Steps:**
1. Open the translated Markdown file.
2. Find the embedded images and their URLs.
3. Check that the language locale in the image filename matches the document’s language.
4. Update the URLs if needed.
5. Save and re-open the file to confirm the images display correctly.

### 3. Translation Accuracy
**Problem:** The translation isn’t accurate or needs more editing.

**Solution:** Review the translated file and make any necessary changes to improve clarity and accuracy.

**Steps:**
1. Open the translated file.
2. Read through the content carefully.
3. Edit as needed to improve the translation.
4. Save your changes.

## 4. Permission Error Redacted or 404

If images or text aren’t translated to the correct language and you see a 401 error in debug mode, it’s usually an authentication problem—your key might be invalid, expired, or not linked to the right endpoint region.

Run co-op translator with the [-d debug switch](https://github.com/Azure/co-op-translator/blob/main/getting_started/command-reference.md) to get more details about the root cause.

- **Error Message**: `Access denied due to invalid subscription key or wrong API endpoint.`
- **Possible Causes**:
  - The subscription key was redacted or incorrect in the request.
  - The AI Services Key or Subscription Key is for a different Azure resource (like Translator or OpenAI) instead of an **Azure AI Vision** resource.

 **Resource Type**
  - Go to the [Azure Portal](https://portal.azure.com) or [Azure AI Foundry](https://ai.azure.com) and make sure your resource is `Azure AI services` → `Vision`.
  - Check your keys and make sure you’re using the correct one.

## 5. Configuration Errors (New Error Handling)

With the new selective translation system, Co-op Translator now gives clear error messages when required services aren’t set up.

### 5.1. Azure AI Service Not Configured for Image Translation

**Problem:** You tried to translate images (`-img` flag) but Azure AI Service isn’t set up correctly.

**Error Message:**
```
Error: Image translation requested but Azure AI Service is not configured.
Please add AZURE_AI_SERVICE_API_KEY and AZURE_AI_SERVICE_ENDPOINT to your .env file.
Check Azure AI Service availability and configuration.
```

**Solution:**
1. **Option 1**: Set up Azure AI Service
   - Add `AZURE_AI_SERVICE_API_KEY` to your `.env` file
   - Add `AZURE_AI_SERVICE_ENDPOINT` to your `.env` file
   - Make sure the service is reachable

2. **Option 2**: Remove the image translation request
   ```bash
   # Instead of: translate -l "ko" -img
   # Use: translate -l "ko" -md
   ```

### 5.2. Missing Required Configuration

**Problem:** A required LLM configuration is missing.

**Error Message:**
```
Error: No language model configuration found.
Please configure either Azure OpenAI or OpenAI in your .env file.
```

**Solution:**
1. Make sure your `.env` file has at least one of these LLM configurations:
   - **Azure OpenAI**: `AZURE_OPENAI_API_KEY` and `AZURE_OPENAI_ENDPOINT`
   - **OpenAI**: `OPENAI_API_KEY`
   
   You only need one—either Azure OpenAI OR OpenAI, not both.

### 5.3. Selective Translation Confusion

**Problem:** No files were translated even though the command ran successfully.

**Possible Causes:**
- Wrong file type flags (`-md`, `-img`, `-nb`)
- No matching files in your project
- Incorrect folder structure

**Solution:**
1. **Use debug mode** to see what’s happening:
   ```bash
   translate -l "ko" -md -d
   ```

2. **Check file types** in your project:
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

### 6.1. Markdown-Only Mode Deprecated

**Problem:** Commands that used to automatically fall back to markdown-only mode don’t work the same way anymore.

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
- **Be specific** about what you want to translate:
  ```bash
  translate -l "ko" -md        # Only markdown
  translate -l "ko" -md -img   # Markdown and images
  translate -l "ko"            # Everything (if all services configured)
  ```

### 6.2. Unexpected Link Behavior

**Problem:** Links in translated files go to unexpected places.

**Cause:** Link processing now changes depending on which file types you select.

**Solution:**
1. **Understand the new link behavior**:
   - If you include `-nb`: Notebook links go to translated versions
   - If you exclude `-nb`: Notebook links go to original files
   - If you include `-img`: Image links go to translated versions
   - If you exclude `-img`: Image links go to original files

2. **Pick the right combination** for your needs:
   ```bash
   # All internal links point to translated versions
   translate -l "ko" -md -img -nb
   
   # Only markdown translated, other links point to originals
   translate -l "ko" -md
   ```

## 7. GitHub Action ran but no Pull Request (PR) was created

**Symptom:** The workflow logs for `peter-evans/create-pull-request` say:

> Branch 'update-translations' is not ahead of base 'main' and will not be created

**Likely causes:**
- **No changes found:** The translation step didn’t produce any differences (the repo is already up to date).
- **Ignored outputs:** `.gitignore` is excluding files you want to commit (like `*.ipynb`, `translations/`, `translated_images/`).
- **add-paths mismatch:** The paths given to the action don’t match where the outputs actually are.
- **Workflow logic/conditions:** The translation step finished early or wrote files to the wrong place.

**How to fix / check:**
1. **Check that outputs exist:** After translation, make sure there are new or changed files in `translations/` and/or `translated_images/`.
   - If you’re translating notebooks, make sure `.ipynb` files are written under `translations/<lang>/...`.
2. **Review `.gitignore`:** Don’t ignore generated outputs. Make sure you’re NOT ignoring:
   - `translations/`
   - `translated_images/`
   - `*.ipynb` (if you’re translating notebooks)
3. **Make sure add-paths matches outputs:** Use a multiline value and include both folders if needed:
   ```yaml
   with:
     add-paths: |
       translations/
       translated_images/
   ```
4. **Force a PR for debugging:** Temporarily allow empty commits to check that everything is wired up correctly:
   ```yaml
   with:
     commit-empty: true
   ```
5. **Run with debug:** Add `-d` to the translate command to see which files were found and written.
6. **Permissions (GITHUB_TOKEN):** Make sure the workflow has write permissions to create commits and PRs:
   ```yaml
   permissions:
     contents: write
     pull-requests: write
   ```


## Quick Debugging Checklist

When you’re troubleshooting translation problems:

1. **Use debug mode**: Add the `-d` flag to see detailed logs
2. **Check your flags**: Make sure `-md`, `-img`, `-nb` match what you want to do
3. **Verify configuration**: Check your `.env` file for the required keys
4. **Test step by step**: Start with just `-md`, then add other types
5. **Check your file structure**: Make sure your source files exist and are accessible

For more details about commands and flags, see the [Command Reference](./command-reference.md).

---

**Disclaimer**:
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we strive for accuracy, please be aware that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not liable for any misunderstandings or misinterpretations arising from the use of this translation.