<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d95d7ec0097c5569ac16dd42840787a2",
  "translation_date": "2025-06-12T09:32:03+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "pa"
}
-->
# Co-op Translator ਵਿੱਚ ਯੋਗਦਾਨ ਪਾਉਣਾ

ਇਹ ਪ੍ਰੋਜੈਕਟ ਯੋਗਦਾਨ ਅਤੇ ਸੁਝਾਵਾਂ ਦਾ ਸਵਾਗਤ ਕਰਦਾ ਹੈ। ਜ਼ਿਆਦਾਤਰ ਯੋਗਦਾਨਾਂ ਲਈ ਤੁਹਾਨੂੰ ਇੱਕ Contributor License Agreement (CLA) ਨਾਲ ਸਹਿਮਤ ਹੋਣਾ ਪੈਂਦਾ ਹੈ, ਜਿਸ ਵਿੱਚ ਤੁਸੀਂ ਇਹ ਦੱਸਦੇ ਹੋ ਕਿ ਤੁਹਾਡੇ ਕੋਲ ਆਪਣੇ ਯੋਗਦਾਨ ਦੇ ਉਪਯੋਗ ਦੇ ਅਧਿਕਾਰ ਹਨ ਅਤੇ ਤੁਸੀਂ ਸਾਨੂੰ ਉਹ ਅਧਿਕਾਰ ਦੇ ਰਹੇ ਹੋ। ਵੇਰਵੇ ਲਈ, https://cla.opensource.microsoft.com 'ਤੇ ਜਾਓ।

ਜਦੋਂ ਤੁਸੀਂ ਇੱਕ pull request ਸਬਮਿਟ ਕਰਦੇ ਹੋ, ਤਾਂ CLA ਬੋਟ ਆਪਣੇ ਆਪ ਇਹ ਨਿਰਧਾਰਤ ਕਰੇਗਾ ਕਿ ਤੁਹਾਨੂੰ CLA ਪ੍ਰਦਾਨ ਕਰਨ ਦੀ ਲੋੜ ਹੈ ਜਾਂ ਨਹੀਂ ਅਤੇ PR ਨੂੰ ਉਚਿਤ ਤਰੀਕੇ ਨਾਲ ਸਜਾਵੇਗਾ (ਜਿਵੇਂ ਕਿ status check, comment)। ਬੋਟ ਵੱਲੋਂ ਦਿੱਤੇ ਨਿਰਦੇਸ਼ਾਂ ਦੀ ਪਾਲਣਾ ਕਰੋ। ਤੁਹਾਨੂੰ ਸਾਰੀਆਂ ਰੀਪੋਜ਼ ਵਿੱਚ ਸਿਰਫ ਇੱਕ ਵਾਰੀ ਇਹ ਕਰਨਾ ਪਵੇਗਾ।

## ਵਿਕਾਸ ਵਾਤਾਵਰਣ ਸੈੱਟਅਪ

ਇਸ ਪ੍ਰੋਜੈਕਟ ਲਈ ਵਿਕਾਸ ਵਾਤਾਵਰਣ ਸੈੱਟਅਪ ਕਰਨ ਲਈ, ਅਸੀਂ dependencies ਦੇ ਪ੍ਰਬੰਧਨ ਲਈ Poetry ਦੀ ਸਿਫਾਰਸ਼ ਕਰਦੇ ਹਾਂ। ਅਸੀਂ `pyproject.toml` ਦਾ ਇਸਤੇਮਾਲ ਕਰਦੇ ਹਾਂ ਪ੍ਰੋਜੈਕਟ dependencies ਨੂੰ ਸੰਭਾਲਣ ਲਈ, ਇਸ ਲਈ dependencies ਇੰਸਟਾਲ ਕਰਨ ਲਈ ਤੁਹਾਨੂੰ Poetry ਵਰਤਣਾ ਚਾਹੀਦਾ ਹੈ।

### ਵਰਚੁਅਲ ਵਾਤਾਵਰਣ ਬਣਾਉਣਾ

#### pip ਨਾਲ

```bash
python -m venv .venv
```

#### Poetry ਨਾਲ

```bash
poetry init
```

### ਵਰਚੁਅਲ ਵਾਤਾਵਰਣ ਐਕਟੀਵੇਟ ਕਰੋ

#### pip ਅਤੇ Poetry ਦੋਹਾਂ ਲਈ

- Windows:

    ```bash
    .venv\Scripts\activate.bat
    ```

- Mac/Linux:

    ```bash
    source .venv/bin/activate
    ```

#### Poetry ਨਾਲ

```bash
poetry shell
```

### ਪੈਕੇਜ ਅਤੇ ਲੋੜੀਂਦੇ ਪੈਕੇਜ ਇੰਸਟਾਲ ਕਰਨਾ

#### Poetry ਨਾਲ (pyproject.toml ਤੋਂ)

```bash
poetry install
```

### ਮੈਨੂਅਲ ਟੈਸਟਿੰਗ

PR ਸਬਮਿਟ ਕਰਨ ਤੋਂ ਪਹਿਲਾਂ, ਅਸਲੀ ਡੌਕਯੂਮੈਂਟੇਸ਼ਨ ਨਾਲ ਅਨੁਵਾਦ ਫੰਕਸ਼ਨਾਲਿਟੀ ਦੀ ਜਾਂਚ ਕਰਨਾ ਜਰੂਰੀ ਹੈ:

1. ਰੂਟ ਡਾਇਰੈਕਟਰੀ ਵਿੱਚ ਇੱਕ test ਡਾਇਰੈਕਟਰੀ ਬਣਾਓ:
    ```bash
    mkdir test_docs
    ```

2. ਕੁਝ markdown ਡੌਕਯੂਮੈਂਟੇਸ਼ਨ ਅਤੇ ਚਿੱਤਰਾਂ ਜੋ ਤੁਸੀਂ ਅਨੁਵਾਦ ਕਰਨਾ ਚਾਹੁੰਦੇ ਹੋ, ਉਹ test ਡਾਇਰੈਕਟਰੀ ਵਿੱਚ ਕਾਪੀ ਕਰੋ। ਉਦਾਹਰਨ ਵਜੋਂ:
    ```bash
    cp /path/to/your/docs/*.md test_docs/
    cp /path/to/your/images/*.png test_docs/
    ```

3. ਪੈਕੇਜ ਨੂੰ ਲੋਕਲ ਤੌਰ 'ਤੇ ਇੰਸਟਾਲ ਕਰੋ:
    ```bash
    pip install -e .
    ```

4. ਆਪਣੇ ਟੈਸਟ ਡੌਕਯੂਮੈਂਟਾਂ 'ਤੇ Co-op Translator ਚਲਾਓ:
    ```bash
    python -m co_op_translator --language-codes ko --root-dir test_docs
    ```

5. `test_docs/translations` and `test_docs/translated_images` to verify:
   - The translation quality
   - The metadata comments are correct
   - The original markdown structure is preserved
   - Links and images are working properly

This manual testing helps ensure that your changes work well in real-world scenarios.

### Environment variables

1. Create an `.env` file in the root directory by copying the provided `.env.template` ਫਾਈਲ ਵਿੱਚ ਅਨੁਵਾਦਿਤ ਫਾਈਲਾਂ ਚੈੱਕ ਕਰੋ।
1. ਵਾਤਾਵਰਣ ਵੇਰੀਏਬਲਜ਼ ਨੂੰ ਦਿੱਖਾਈ ਗਈ ਹਦਾਇਤਾਂ ਅਨੁਸਾਰ ਭਰੋ।

> [!TIP]
>
> ### ਹੋਰ ਵਿਕਾਸ ਵਾਤਾਵਰਣ ਵਿਕਲਪ
>
> ਪ੍ਰੋਜੈਕਟ ਨੂੰ ਲੋਕਲ ਤੌਰ 'ਤੇ ਚਲਾਉਣ ਦੇ ਇਲਾਵਾ, ਤੁਸੀਂ ਵਿਕਾਸ ਵਾਤਾਵਰਣ ਲਈ GitHub Codespaces ਜਾਂ VS Code Dev Containers ਵੀ ਵਰਤ ਸਕਦੇ ਹੋ।
>
> #### GitHub Codespaces
>
> ਤੁਸੀਂ GitHub Codespaces ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਇਹ ਨਮੂਨੇ ਵਰਚੁਅਲ ਤੌਰ 'ਤੇ ਚਲਾ ਸਕਦੇ ਹੋ ਅਤੇ ਕਿਸੇ ਵਾਧੂ ਸੈਟਅਪ ਦੀ ਲੋੜ ਨਹੀਂ।
>
> ਬਟਨ ਤੁਹਾਡੇ ਬ੍ਰਾਉਜ਼ਰ ਵਿੱਚ ਵੈੱਬ-ਅਧਾਰਿਤ VS Code ਇੰਸਟੈਂਸ ਖੋਲ੍ਹੇਗਾ:
>
> 1. ਟੈਮਪਲੇਟ ਖੋਲ੍ਹੋ (ਇਸ ਵਿੱਚ ਕੁਝ ਮਿੰਟ ਲੱਗ ਸਕਦੇ ਹਨ):
>
>     [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/azure/co-op-translator)
>
> #### VS Code Dev Containers ਨਾਲ ਲੋਕਲ ਚਲਾਉਣਾ
>
> ⚠️ ਇਹ ਵਿਕਲਪ ਸਿਰਫ਼ ਤਦ ਕੰਮ ਕਰੇਗਾ ਜਦੋਂ ਤੁਹਾਡੇ Docker Desktop ਨੂੰ ਘੱਟੋ-ਘੱਟ 16 GB RAM ਦਿੱਤੀ ਗਈ ਹੋਵੇ। ਜੇ ਤੁਹਾਡੇ ਕੋਲ 16 GB ਤੋਂ ਘੱਟ RAM ਹੈ, ਤਾਂ ਤੁਸੀਂ [GitHub Codespaces ਵਿਕਲਪ](../..) ਜਾਂ [ਇਸ ਨੂੰ ਲੋਕਲ ਤੌਰ 'ਤੇ ਸੈੱਟਅਪ](../..) ਕਰਨ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰ ਸਕਦੇ ਹੋ।
>
> ਇੱਕ ਸੰਬੰਧਤ ਵਿਕਲਪ VS Code Dev Containers ਹੈ, ਜੋ ਤੁਹਾਡੇ ਲੋਕਲ VS Code ਵਿੱਚ ਪ੍ਰੋਜੈਕਟ ਖੋਲ੍ਹੇਗਾ [Dev Containers ਐਕਸਟੇੰਸ਼ਨ](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) ਦੀ ਵਰਤੋਂ ਕਰਕੇ:
>
> 1. Docker Desktop ਸ਼ੁਰੂ ਕਰੋ (ਜੇ ਇੰਸਟਾਲ ਨਹੀਂ ਕੀਤਾ ਤਾਂ ਇੰਸਟਾਲ ਕਰੋ)
> 2. ਪ੍ਰੋਜੈਕਟ ਖੋਲ੍ਹੋ:
>
>    [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator)


### ਕੋਡ ਸਟਾਈਲ

ਅਸੀਂ ਪ੍ਰੋਜੈਕਟ ਵਿੱਚ ਸਥਿਰ ਕੋਡ ਸਟਾਈਲ ਨੂੰ ਬਰਕਰਾਰ ਰੱਖਣ ਲਈ Python ਕੋਡ ਫਾਰਮੈਟਰ ਵਜੋਂ [Black](https://github.com/psf/black) ਦੀ ਵਰਤੋਂ ਕਰਦੇ ਹਾਂ। Black ਇੱਕ ਕੜੀ ਕੋਡ ਫਾਰਮੈਟਰ ਹੈ ਜੋ Python ਕੋਡ ਨੂੰ ਆਪਣੇ ਸਟਾਈਲ ਅਨੁਸਾਰ ਆਟੋਮੈਟਿਕ ਤੌਰ 'ਤੇ ਫਾਰਮੈਟ ਕਰਦਾ ਹੈ।

#### ਕਨਫਿਗਰੇਸ਼ਨ

Black ਦੀ ਕਨਫਿਗਰੇਸ਼ਨ ਸਾਡੇ `pyproject.toml` ਵਿੱਚ ਦਿੱਤੀ ਗਈ ਹੈ:

```toml
[tool.black]
line-length = 88
target-version = ['py310']
include = '\.pyi?$'
```

#### Black ਇੰਸਟਾਲ ਕਰਨਾ

ਤੁਸੀਂ Black ਨੂੰ Poetry (ਸਿਫਾਰਸ਼ ਕੀਤੀ) ਜਾਂ pip ਦੀ ਵਰਤੋਂ ਨਾਲ ਇੰਸਟਾਲ ਕਰ ਸਕਦੇ ਹੋ:

##### Poetry ਨਾਲ

ਜਦੋਂ ਤੁਸੀਂ ਵਿਕਾਸ ਵਾਤਾਵਰਣ ਸੈੱਟਅਪ ਕਰਦੇ ਹੋ, Black ਆਪਣੇ ਆਪ ਇੰਸਟਾਲ ਹੋ ਜਾਂਦਾ ਹੈ:
```bash
poetry install
```

##### pip ਨਾਲ

ਜੇ ਤੁਸੀਂ pip ਵਰਤ ਰਹੇ ਹੋ, ਤਾਂ ਤੁਸੀਂ Black ਨੂੰ ਸਿੱਧਾ ਇੰਸਟਾਲ ਕਰ ਸਕਦੇ ਹੋ:
```bash
pip install black
```

#### Black ਵਰਤਣਾ

##### Poetry ਨਾਲ

1. ਪ੍ਰੋਜੈਕਟ ਵਿੱਚ ਸਾਰੇ Python ਫਾਈਲਾਂ ਨੂੰ ਫਾਰਮੈਟ ਕਰੋ:
    ```bash
    poetry run black .
    ```

2. ਕਿਸੇ ਖਾਸ ਫਾਈਲ ਜਾਂ ਡਾਇਰੈਕਟਰੀ ਨੂੰ ਫਾਰਮੈਟ ਕਰੋ:
    ```bash
    poetry run black path/to/file_or_directory
    ```

##### pip ਨਾਲ

1. ਪ੍ਰੋਜੈਕਟ ਵਿੱਚ ਸਾਰੇ Python ਫਾਈਲਾਂ ਨੂੰ ਫਾਰਮੈਟ ਕਰੋ:
    ```bash
    black .
    ```

2. ਕਿਸੇ ਖਾਸ ਫਾਈਲ ਜਾਂ ਡਾਇਰੈਕਟਰੀ ਨੂੰ ਫਾਰਮੈਟ ਕਰੋ:
    ```bash
    black path/to/file_or_directory
    ```

> [!TIP]
> ਅਸੀਂ ਸਿਫਾਰਸ਼ ਕਰਦੇ ਹਾਂ ਕਿ ਤੁਸੀਂ ਆਪਣੇ ਐਡੀਟਰ ਨੂੰ ਇਸ ਤਰ੍ਹਾਂ ਸੈੱਟ ਕਰੋ ਕਿ Black ਨਾਲ ਕੋਡ ਸੇਵ ਕਰਨ 'ਤੇ ਆਟੋਮੈਟਿਕ ਤੌਰ 'ਤੇ ਫਾਰਮੈਟ ਹੋ ਜਾਵੇ। ਜ਼ਿਆਦਾਤਰ ਆਧੁਨਿਕ ਐਡੀਟਰ ਇਸਨੂੰ ਐਕਸਟੈਂਸ਼ਨ ਜਾਂ ਪਲੱਗਇਨ ਰਾਹੀਂ ਸਹਿਯੋਗ ਦਿੰਦੇ ਹਨ।

## Co-op Translator ਚਲਾਉਣਾ

ਆਪਣੇ ਵਾਤਾਵਰਣ ਵਿੱਚ Poetry ਦੀ ਵਰਤੋਂ ਕਰਕੇ Co-op Translator ਚਲਾਉਣ ਲਈ, ਹੇਠਾਂ ਦਿੱਤੇ ਕਦਮਾਂ ਦੀ ਪਾਲਣਾ ਕਰੋ:

1. ਉਸ ਡਾਇਰੈਕਟਰੀ ਵਿੱਚ ਜਾਓ ਜਿੱਥੇ ਤੁਸੀਂ ਅਨੁਵਾਦ ਟੈਸਟ ਕਰਨਾ ਚਾਹੁੰਦੇ ਹੋ ਜਾਂ ਟੈਸਟਿੰਗ ਲਈ ਇੱਕ ਅਸਥਾਈ ਫੋਲਡਰ ਬਣਾਓ।

2. ਹੇਠਾਂ ਦਿੱਤਾ ਕਮਾਂਡ ਚਲਾਓ। `-l ko` with the language code you wish to translate into. The `-d` ਫਲੈਗ ਡੀਬੱਗ ਮੋਡ ਦਰਸਾਉਂਦਾ ਹੈ।

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> [!NOTE]
> ਕਮਾਂਡ ਚਲਾਉਣ ਤੋਂ ਪਹਿਲਾਂ ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਤੁਹਾਡਾ Poetry ਵਾਤਾਵਰਣ ਐਕਟੀਵੇਟ ਹੈ (poetry shell)।

## ਮੈਨਟੇਨਰ

### ਕਮਿਟ ਸੁਨੇਹਾ ਅਤੇ ਮਰਜ ਰਣਨੀਤੀ

ਸਾਡੇ ਪ੍ਰੋਜੈਕਟ ਦੀ ਕਮਿਟ ਇਤਿਹਾਸ ਵਿੱਚ ਇਕਸਾਰਤਾ ਅਤੇ ਸਪਸ਼ਟਤਾ ਬਣਾਈ ਰੱਖਣ ਲਈ, ਅਸੀਂ **Squash and Merge** ਰਣਨੀਤੀ ਵਰਤਦੇ ਸਮੇਂ **ਅੰਤਿਮ ਕਮਿਟ ਸੁਨੇਹੇ** ਲਈ ਇੱਕ ਖ਼ਾਸ ਫਾਰਮੈਟ ਦੀ ਪਾਲਣਾ ਕਰਦੇ ਹਾਂ।

ਜਦੋਂ ਕੋਈ pull request (PR) ਮਰਜ ਹੁੰਦਾ ਹੈ, ਤਾਂ ਵੱਖ-ਵੱਖ ਕਮਿਟ ਇੱਕ ਹੀ ਕਮਿਟ ਵਿੱਚ ਸਮਾਏ ਜਾਂਦੇ ਹਨ। ਅੰਤਿਮ ਕਮਿਟ ਸੁਨੇਹਾ ਹੇਠਾਂ ਦਿੱਤੇ ਫਾਰਮੈਟ ਦੇ ਅਨੁਸਾਰ ਹੋਣਾ ਚਾਹੀਦਾ ਹੈ ਤਾਂ ਜੋ ਇਤਿਹਾਸ ਸਾਫ਼ ਅਤੇ ਇਕਸਾਰ ਰਹੇ।

#### ਕਮਿਟ ਸੁਨੇਹਾ ਫਾਰਮੈਟ (squash and merge ਲਈ)

ਅਸੀਂ ਕਮਿਟ ਸੁਨੇਹਿਆਂ ਲਈ ਹੇਠਾਂ ਦਿੱਤਾ ਫਾਰਮੈਟ ਵਰਤਦੇ ਹਾਂ:

```bash
<type>: <description> (#<PR number>)
```

- **type**: ਕਮਿਟ ਦੀ ਸ਼੍ਰੇਣੀ ਦਰਸਾਉਂਦਾ ਹੈ। ਅਸੀਂ ਹੇਠਾਂ ਦਿੱਤੇ ਪ੍ਰਕਾਰ ਵਰਤਦੇ ਹਾਂ:
  - `Docs`: For documentation updates.
  - `Build`: For changes related to the build system or dependencies, including updates to configuration files, CI workflows, or the Dockerfile.
  - `Core`: For modifications to the project's core functionality or features, particularly those involving files in the `src/co_op_translator/core` directory.

- **description**: A concise summary of the change.
- **PR number**: The number of the pull request associated with the commit.

**Examples**:

- `Docs: Update installation instructions for clarity (#50)`
- `Core: Improve handling of image translation (#60)`

> [!NOTE]
> Currently, the **`Docs`**, **`Core`**, and **`Build`** prefixes are automatically added to PR titles based on the labels applied to the modified source code. As long as the correct label is applied, you typically don't need to manually update the PR title. You just need to verify that everything is correct and the prefix has been generated appropriately.

#### Merge strategy

We use **Squash and Merge** as our default strategy for pull requests. This strategy ensures that commit messages follow our format, even if individual commits don't.

**Reasons**:

- A clean, linear project history.
- Consistency in commit messages.
- Reduced noise from minor commits (e.g., "fix typo").

When merging, ensure the final commit message follows the commit message format described above.

**Example of Squash and Merge**
If a PR contains the following commits:

- `fix typo`
- `update README`
- `adjust formatting`

They should be squashed into:
`Docs: Improve documentation clarity and formatting (#65)`

**ਅਸਵੀਕਾਰੋਪਣ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ ਏਆਈ ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਨਾਲ ਅਨੁਵਾਦਿਤ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਤਾ ਲਈ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਵਿੱਚ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਪਸ਼ਟਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਪ੍ਰਮਾਣਿਕ ਸਰੋਤ ਵਜੋਂ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਉਤਪੰਨ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆ ਲਈ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।