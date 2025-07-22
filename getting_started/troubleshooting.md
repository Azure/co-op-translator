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
