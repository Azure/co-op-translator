# How to use Co-op Translator command line interface (CLI)

## Prerequisites

- **Python 3.10 or higher**: Required for running the Co-op Translator.
- **Language Model Resource**: 
  - **Azure OpenAI** or other LLMs. Details can be found in the [supported models and services](../../README.md#supported-models-and-services).
- **Computer Vision Resource** (optional):
  - For image translation. If unavailable, the translator defaults to [Markdown-only mode](../markdown-only-mode.md).
  - **Azure Computer Vision**

## Table of Contents

1. [Create an '.env' file in the root directory](./create-env-file.md)
   - Include necessary keys for the chosen language model service.
   - If Azure Computer Vision keys are omitted or `-md` is specified, the translator will operate in Markdown-only mode.
1. [Install the Co-op translator package](./install-package.md)
1. [Translate your project using Co-op Translator](./translator-your-project.md)
