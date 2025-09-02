# Microsoft Co-op Translator Troubleshooting Guide


## Overview
The Microsoft Co-Op Translator is a powerful tool for translating Markdown documents seamlessly. This guide will help you troubleshoot common issues encountered when using the tool.

## Common Issues and Solutions

### 1. Markdown Tag Issue
**Problem:** The translated Markdown document includes a `markdown` tag at the top, causing rendering issues.

**Solution:** To resolve this, simply delete the `markdown` tag at the top of the file. This will allow the Markdown file to render correctly.

**Steps:**
1. Open the translated Markdown (`.md`) file.
2. Locate the `markdown` tag at the top of the document.
3. Delete the `markdown` tag.
4. Save the changes to the file.
5. Re-open the file to ensure it renders correctly.

### 2. Embedded Images URL Issue
**Problem:** The URLs of embedded images do not match the language locale, leading to incorrect or missing images.

**Solution:** Check the URL of embedded images and ensure they match the language locale. All images are located in the `translated_images`folder each image has a language locale tag in the image file name.

**Steps:**
1. Open the translated Markdown document.
2. Identify the embedded images and their URLs.
3. Verify that the language locale in the image file name matches the document's language.
4. Update the URLs if necessary.
5. Save the changes and re-open the document to confirm the images render correctly.

### 3. Translation Accuracy
**Problem:** The translated content is not accurate or requires further editing.

**Solution:** Review the translated document and make necessary edits to improve accuracy and readability.

**Steps:**
1. Open the translated document.
2. Review the content carefully.
3. Make necessary edits to improve translation accuracy.
4. Save the changes.

## 4. Permission Error Redacted or 404

If images or text is not being translated to the correct language and when running in -d debug mode you experience 401 error. This is a classic authentication failure—either the key is invalid, expired, or not linked to the endpoint's region. 

Run co-op translator with the [-d debug switch](https://github.com/Azure/co-op-translator/blob/main/getting_started/command-reference.md) to gain further understanding of root cause.

- **Error Message**: `Access denied due to invalid subscription key or wrong API endpoint.`
- **Possible Causes**:
  - Subscription key was redacted or incorrect in the request.).
  - AI Services Key or Subscription Key might belong to a different Azure resource (like Translator or OpenAI) instead of an **Azure AI Vision** resource.

 **Resource Type**
  - Go to the [Azure Portal](https://portal.azure.com) or [Azure AI Foundry](https://ai.azure.com) and make sure the resource is of type `Azure AI services` → `Vision`.
  - Validate the keys and ensure the correct key is being used.

## 5. Configuration Errors (New Error Handling)

Starting with the new selective translation system, Co-op Translator now provides explicit error messages when required services are not configured.

### 5.1. Azure AI Service Not Configured for Image Translation

**Problem:** You requested image translation (`-img` flag) but Azure AI Service is not properly configured.

**Error Message:**
```
Error: Image translation requested but Azure AI Service is not configured.
Please add AZURE_AI_SERVICE_API_KEY and AZURE_AI_SERVICE_ENDPOINT to your .env file.
Check Azure AI Service availability and configuration.
```

**Solution:**
1. **Option 1**: Configure Azure AI Service
   - Add `AZURE_AI_SERVICE_API_KEY` to your `.env` file
   - Add `AZURE_AI_SERVICE_ENDPOINT` to your `.env` file
   - Verify the service is accessible

2. **Option 2**: Remove image translation request
   ```bash
   # Instead of: translate -l "ko" -img
   # Use: translate -l "ko" -md
   ```

### 5.2. Missing Required Configuration

**Problem:** Essential LLM configuration is missing.

**Error Message:**
```
Error: No language model configuration found.
Please configure either Azure OpenAI or OpenAI in your .env file.
```

**Solution:**
1. Verify that your `.env` file has at least one of the following LLM configurations:
   - **Azure OpenAI**: `AZURE_OPENAI_API_KEY` and `AZURE_OPENAI_ENDPOINT`
   - **OpenAI**: `OPENAI_API_KEY`
   
   You need either Azure OpenAI OR OpenAI configured, not both.

### 5.3. Selective Translation Confusion

**Problem:** No files were translated even though the command succeeded.

**Possible Causes:**
- Wrong file type flags (`-md`, `-img`, `-nb`)
- No matching files in the project
- Incorrect directory structure

**Solution:**
1. **Use debug mode** to see what's happening:
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

**Problem:** Commands that relied on automatic markdown-only fallback no longer work as expected.

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
- **Be explicit** about what you want to translate:
  ```bash
  translate -l "ko" -md        # Only markdown
  translate -l "ko" -md -img   # Markdown and images
  translate -l "ko"            # Everything (if all services configured)
  ```

### 6.2. Unexpected Link Behavior

**Problem:** Links in translated files point to unexpected locations.

**Cause:** Dynamic link processing changes based on selected file types.

**Solution:**
1. **Understand the new link behavior**:
   - `-nb` included: Notebook links point to translated versions
   - `-nb` excluded: Notebook links point to original files
   - `-img` included: Image links point to translated versions
   - `-img` excluded: Image links point to original files

2. **Choose the right combination** for your use case:
   ```bash
   # All internal links point to translated versions
   translate -l "ko" -md -img -nb
   
   # Only markdown translated, other links point to originals
   translate -l "ko" -md
   ```

## 7. GitHub Action ran but no Pull Request (PR) was created

**Symptom:** The workflow logs for `peter-evans/create-pull-request` show:

> Branch 'update-translations' is not ahead of base 'main' and will not be created

**Likely causes:**
- **No changes detected:** The translation step produced no diffs (repo already up to date).
- **Ignored outputs:** `.gitignore` excludes files you expect to commit (e.g., `*.ipynb`, `translations/`, `translated_images/`).
- **add-paths mismatch:** The paths provided to the action don’t match actual output locations.
- **Workflow logic/conditions:** The translation step exited early or wrote to unexpected directories.

**How to fix / verify:**
1. **Confirm outputs exist:** After translation, check the workspace has new/changed files in `translations/` and/or `translated_images/`.
   - If translating notebooks, ensure `.ipynb` files are actually written under `translations/<lang>/...`.
2. **Review `.gitignore`:** Do not ignore generated outputs. Ensure you are NOT ignoring:
   - `translations/`
   - `translated_images/`
   - `*.ipynb` (if translating notebooks)
3. **Ensure add-paths matches outputs:** Use a multiline value and include both folders if applicable:
   ```yaml
   with:
     add-paths: |
       translations/
       translated_images/
   ```
4. **Force a PR for debugging:** Temporarily allow empty commits to confirm wiring is correct:
   ```yaml
   with:
     commit-empty: true
   ```
5. **Run with debug:** Add `-d` to the translate command to print what files were discovered and written.
6. **Permissions (GITHUB_TOKEN):** Ensure the workflow has write permissions for creating commits and PRs:
   ```yaml
   permissions:
     contents: write
     pull-requests: write
   ```

## Quick Debugging Checklist

When troubleshooting translation issues:

1. **Use debug mode**: Add `-d` flag to see detailed logs
2. **Check your flags**: Ensure `-md`, `-img`, `-nb` match your intent
3. **Verify configuration**: Check your `.env` file has required keys
4. **Test incrementally**: Start with `-md` only, then add other types
5. **Check file structure**: Ensure source files exist and are accessible

For more detailed information about available commands and flags, see the [Command Reference](./command-reference.md).
