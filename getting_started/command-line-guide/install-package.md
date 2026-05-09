# Install Co-op Translator

Co-op Translator supports Python 3.10 through 3.12. Use a virtual environment before installing the package.

## Install from PyPI

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

## Install from a repository clone

Use Poetry when developing this repository:

```bash
poetry install
poetry run translate --help
```

If you are using pip from a clone instead, install the pinned runtime dependencies:

```bash
pip install -r requirements.txt
pip install -e .
```

After installation, configure one LLM provider before running translation. See the [configuration guide](../../docs/configuration.md) for the current environment variables and command requirements.
