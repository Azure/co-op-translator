# Install Co-op Translator

Co-op Translator supports Python 3.10 through 3.12. Use a virtual environment so the CLI dependencies stay separate from your system Python packages.

## Install from PyPI

Use this path when you want to run the published CLI in your own documentation project.

### Windows

```powershell
python -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip
pip install co-op-translator
translate --help
```

### macOS / Linux

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install co-op-translator
translate --help
```

After installation, create a `.env` file and configure one language model provider before running translation. See [Create a `.env` file](./create-env-file.md) and the full [configuration reference](../../docs/configuration.md).

## Install from a repository clone

Use this path when you want to contribute to Co-op Translator itself.

1. Fork the repository on GitHub.
2. Clone your fork:

   ```bash
   git clone https://github.com/<your-account>/co-op-translator.git
   cd co-op-translator
   ```

3. Install dependencies with Poetry:

   ```bash
   poetry install
   poetry run translate --help
   ```

If you prefer pip for local development, install the development requirements and then install the package in editable mode:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements-dev.txt
pip install -e .
translate --help
```

On Windows, replace `source .venv/bin/activate` with:

```powershell
.venv\Scripts\activate
```

## First translation check

Run a narrow Markdown-only command first. This confirms that the CLI, credentials, and output folder are working before you add notebooks or images.

```bash
translate -l "ko" -md
```

Image translation requires Azure AI Vision credentials in addition to an LLM provider:

```bash
translate -l "ko" -img
```
