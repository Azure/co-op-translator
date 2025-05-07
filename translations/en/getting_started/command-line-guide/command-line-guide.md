<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d8eec418d6325416b9fab19a2dfcbf41",
  "translation_date": "2025-05-06T17:51:33+00:00",
  "source_file": "getting_started/command-line-guide/command-line-guide.md",
  "language_code": "en"
}
-->
# How to use Co-op Translator command line interface (CLI)

## Prerequisites

- **Python 3.10 or higher**: Required to run the Co-op Translator.
- **Language Model Resource**:  
  - **Azure OpenAI** or other LLMs. Details are available in [supported models and services](../../../../README.md).
- **Computer Vision Resource** (optional):  
  - For image translation. If not available, the translator will switch to [Markdown-only mode](../markdown-only-mode.md).  
  - **Azure Computer Vision**

### Initial Setup

Before starting, make sure to configure the following resources:

- [Set up Azure OpenAI](../set-up-resources/set-up-azure-openai.md)  
- [Set up Azure Computer Vision](../set-up-resources/set-up-azure-computer-vision.md) (optional)

## Table of Contents

1. [Create an '.env' file in the root directory](./create-env-file.md)  
   - Include the required keys for the selected language model service.  
   - If Azure Computer Vision keys are missing or `-md` is set, the translator will run in Markdown-only mode.  
3. [Install the Co-op translator package](./install-package.md)  
4. [Translate your project using Co-op Translator](./translator-your-project.md)

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we strive for accuracy, please be aware that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not liable for any misunderstandings or misinterpretations arising from the use of this translation.