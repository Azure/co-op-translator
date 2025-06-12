<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0788d7ebe4876c9be89132f48e09b26d",
  "translation_date": "2025-06-12T12:31:56+00:00",
  "source_file": "getting_started/troubleshooting.md",
  "language_code": "my"
}
-->
# Microsoft Co-op Translator Troubleshooting Guide


## Overview
The Microsoft Co-Op Translator is a powerful tool for translating Markdown documents seamlessly. This guide will help you troubleshoot common issues encountered when using the tool.

## Common Issues and Solutions

### 1. Markdown Tag Issue
**Problem:** The translated Markdown document includes a `markdown` tag at the top, causing rendering issues.

**Solution:** To fix this, just remove the `markdown` tag at the beginning of the file. This will ensure the Markdown file displays correctly.

**Steps:**
1. Open the translated Markdown (`.md`) file.
2. Find the `markdown` tag at the top of the document.
3. Delete the `markdown` tag.
4. Save the file.
5. Re-open it to confirm it renders properly.

### 2. Embedded Images URL Issue
**Problem:** The URLs of embedded images don’t match the language locale, resulting in incorrect or missing images.

**Solution:** Verify the URLs of embedded images and make sure they correspond to the language locale. All images are stored in the `translated_images` folder, and each image file name contains a language locale tag.

**Steps:**
1. Open the translated Markdown document.
2. Locate the embedded images and their URLs.
3. Check that the language locale in each image file name matches the document’s language.
4. Update URLs if needed.
5. Save and re-open the document to ensure images display correctly.

### 3. Translation Accuracy
**Problem:** The translated content is inaccurate or needs further editing.

**Solution:** Review the translated document and make necessary adjustments to enhance accuracy and readability.

**Steps:**
1. Open the translated document.
2. Carefully review the content.
3. Edit as needed to improve translation quality.
4. Save your changes.

### 4. File Formatting Issues
**Problem:** The formatting of the translated document is incorrect. This can happen in tables; the additional ``` are added.

**Solution:** Adjust the formatting of the document to match the original structure. Simply deleting the ``` will help fix table issues.

**Steps:**
1. Open the translated document.
2. Compare it to the original to spot formatting problems.
3. Adjust formatting to match the original.
4. Save your changes.

Could you please specify which language "my" refers to? For example, is it Burmese (Myanmar), Malay, or another language? This will help me provide an accurate translation.