# Command-line guide

This walkthrough keeps the setup path short. The detailed and current references live in the MkDocs documentation:

- [Configuration](../../docs/configuration.md)
- [CLI reference](../../docs/cli.md)
- [Examples](../../docs/examples.md)

## Prerequisites

- Python 3.10 through 3.12
- One configured LLM provider: Azure OpenAI or OpenAI
- Azure AI Vision only when translating images or running the default all-content mode

## Setup path

1. [Install Co-op Translator](./install-package.md).
2. [Create a `.env` file](./create-env-file.md) with one LLM provider.
3. Run a narrow first translation, such as Markdown only:

   ```bash
   translate -l "ko" -md
   ```

4. Add notebooks or images when you have the matching configuration:

   ```bash
   translate -l "ko" -nb
   translate -l "ko" -img
   ```

5. Run deterministic review checks before opening a pull request:

   ```bash
   co-op-review -l "ko"
   ```

For all flags and command behavior, use the [CLI reference](../../docs/cli.md). This prevents the tutorial from drifting away from the documentation site as new options are added.
