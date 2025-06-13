<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0788d7ebe4876c9be89132f48e09b26d",
  "translation_date": "2025-06-12T12:21:32+00:00",
  "source_file": "getting_started/troubleshooting.md",
  "language_code": "en"
}
-->
# Microsoft Co-op Translator Troubleshooting Guide


## Overview
The Microsoft Co-Op Translator is a powerful tool for seamlessly translating Markdown documents. This guide will help you resolve common issues you might encounter while using the tool.

## Common Issues and Solutions

### 1. Markdown Tag Issue
**Problem:** The translated Markdown document contains a `markdown` tag at the top, causing rendering problems.

**Solution:** To fix this, simply remove the `markdown` tag at the beginning of the file. This will allow the Markdown file to display properly.

**Steps:**
1. Open the translated Markdown (`.md`) file.
2. Find the `markdown` tag at the top of the document.
3. Delete the `markdown` tag.
4. Save the file.
5. Reopen the file to confirm it renders correctly.

### 2. Embedded Images URL Issue
**Problem:** The URLs for embedded images don’t match the language locale, resulting in incorrect or missing images.

**Solution:** Verify the URLs of embedded images and ensure they correspond to the language locale. All images are stored in the `translated_images` folder, and each image file name includes a language locale tag.

**Steps:**
1. Open the translated Markdown document.
2. Locate the embedded images and their URLs.
3. Check that the language locale in the image file names matches the document’s language.
4. Update the URLs if needed.
5. Save the changes and reopen the document to make sure images display properly.

### 3. Translation Accuracy
**Problem:** The translated content is inaccurate or needs further refinement.

**Solution:** Review the translated document and make necessary corrections to improve accuracy and clarity.

**Steps:**
1. Open the translated document.
2. Carefully review the content.
3. Edit as needed to enhance translation quality.
4. Save your changes.

### 4. File Formatting Issues
**Problem:** The formatting in the translated document is incorrect. This can happen with tables; the additional ``` are added.

**Solution:** Adjust the formatting of the document to match the original structure. Simply deleting the ``` will help fix table issues.

**Steps:**
1. Open the translated document.
2. Compare it with the original to spot formatting errors.
3. Adjust the formatting to match the original.
4. Save your changes.

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we strive for accuracy, please be aware that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not liable for any misunderstandings or misinterpretations arising from the use of this translation.