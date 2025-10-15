<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "bd4704f50c55da7d572b691484aa0b30",
  "translation_date": "2025-10-15T02:55:00+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "pa"
}
-->
# ਕੋ-ਓਪ ਟ੍ਰਾਂਸਲੇਟਰ ਵਿੱਚ ਯੋਗਦਾਨ ਪਾਉਣਾ

ਇਹ ਪ੍ਰੋਜੈਕਟ ਯੋਗਦਾਨ ਅਤੇ ਸੁਝਾਵਾਂ ਦਾ ਸਵਾਗਤ ਕਰਦਾ ਹੈ। ਜ਼ਿਆਦਾਤਰ ਯੋਗਦਾਨ ਲਈ ਤੁਹਾਨੂੰ ਇੱਕ Contributor License Agreement (CLA) 'ਤੇ ਸਹਿਮਤ ਹੋਣਾ ਪੈਂਦਾ ਹੈ, ਜਿਸ ਵਿੱਚ ਤੁਸੀਂ ਐਲਾਨ ਕਰਦੇ ਹੋ ਕਿ ਤੁਹਾਡੇ ਕੋਲ ਯੋਗਦਾਨ ਦੇ ਹੱਕ ਹਨ ਅਤੇ ਤੁਸੀਂ ਸਾਨੂੰ ਇਸਨੂੰ ਵਰਤਣ ਦੀ ਇਜਾਜ਼ਤ ਦਿੰਦੇ ਹੋ। ਹੋਰ ਜਾਣਕਾਰੀ ਲਈ https://cla.opensource.microsoft.com 'ਤੇ ਜਾਓ।

ਜਦੋਂ ਤੁਸੀਂ pull request ਭੇਜਦੇ ਹੋ, ਇੱਕ CLA bot ਆਪਣੇ-ਆਪ ਚੈੱਕ ਕਰੇਗਾ ਕਿ ਤੁਹਾਨੂੰ CLA ਦੇਣੀ ਲੋੜੀਂਦੀ ਹੈ ਜਾਂ ਨਹੀਂ ਅਤੇ PR 'ਤੇ ਸਹੀ ਤਰੀਕੇ ਨਾਲ ਸਟੇਟਸ ਜਾਂ ਟਿੱਪਣੀ ਲਗਾਏਗਾ। ਬਸ bot ਵੱਲੋਂ ਦਿੱਤੀਆਂ ਹਦਾਇਤਾਂ ਦੀ ਪਾਲਣਾ ਕਰੋ। ਤੁਹਾਨੂੰ ਇਹ ਸਿਰਫ ਇੱਕ ਵਾਰ ਕਰਨਾ ਪਵੇਗਾ, ਜਿੱਥੇ ਵੀ ਸਾਡੀ CLA ਵਰਤੀ ਜਾਂਦੀ ਹੈ।

## ਡਿਵੈਲਪਮੈਂਟ ਇਨਵਾਇਰਨਮੈਂਟ ਸੈਟਅੱਪ

ਇਸ ਪ੍ਰੋਜੈਕਟ ਲਈ ਡਿਵੈਲਪਮੈਂਟ ਇਨਵਾਇਰਨਮੈਂਟ ਸੈਟਅੱਪ ਕਰਨ ਲਈ, dependencies ਮੈਨੇਜ ਕਰਨ ਲਈ Poetry ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ `pyproject.toml` ਰਾਹੀਂ dependencies ਮੈਨੇਜ ਕਰਦੇ ਹਾਂ, ਇਸ ਲਈ dependencies install ਕਰਨ ਲਈ Poetry ਵਰਤੋ।

### ਵਰਚੁਅਲ ਇਨਵਾਇਰਨਮੈਂਟ ਬਣਾਓ

#### pip ਨਾਲ

```bash
python -m venv .venv
```

#### Poetry ਨਾਲ

```bash
poetry init
```

### ਵਰਚੁਅਲ ਇਨਵਾਇਰਨਮੈਂਟ ਐਕਟੀਵੇਟ ਕਰੋ

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

PR ਭੇਜਣ ਤੋਂ ਪਹਿਲਾਂ, ਟ੍ਰਾਂਸਲੇਸ਼ਨ ਫੰਕਸ਼ਨਲਿਟੀ ਨੂੰ ਅਸਲ ਡੌਕੂਮੈਂਟੇਸ਼ਨ ਨਾਲ ਟੈਸਟ ਕਰਨਾ ਜ਼ਰੂਰੀ ਹੈ:

1. ਰੂਟ ਡਾਇਰੈਕਟਰੀ ਵਿੱਚ ਇੱਕ test ਡਾਇਰੈਕਟਰੀ ਬਣਾਓ:
    ```bash
    mkdir test_docs
    ```

2. ਕੁਝ markdown ਡੌਕੂਮੈਂਟੇਸ਼ਨ ਅਤੇ ਚਿੱਤਰ, ਜੋ ਤੁਸੀਂ ਟ੍ਰਾਂਸਲੇਟ ਕਰਨਾ ਚਾਹੁੰਦੇ ਹੋ, test ਡਾਇਰੈਕਟਰੀ ਵਿੱਚ ਕਾਪੀ ਕਰੋ। ਉਦਾਹਰਨ ਵਜੋਂ:
    ```bash
    cp /path/to/your/docs/*.md test_docs/
    cp /path/to/your/images/*.png test_docs/
    ```

3. ਪੈਕੇਜ ਨੂੰ ਲੋਕਲ ਇੰਸਟਾਲ ਕਰੋ:
    ```bash
    pip install -e .
    ```

4. ਆਪਣੇ test ਡੌਕੂਮੈਂਟਸ 'ਤੇ Co-op Translator ਚਲਾਓ:
    ```bash
    python -m co_op_translator --language-codes ko --root-dir test_docs
    ```

5. `test_docs/translations` ਅਤੇ `test_docs/translated_images` ਵਿੱਚ ਟ੍ਰਾਂਸਲੇਟ ਕੀਤੇ ਫਾਈਲਾਂ ਚੈੱਕ ਕਰੋ, ਇਹ ਵੇਖਣ ਲਈ:
   - ਟ੍ਰਾਂਸਲੇਸ਼ਨ ਦੀ ਗੁਣਵੱਤਾ
   - ਮੈਟਾਡਾਟਾ ਟਿੱਪਣੀਆਂ ਠੀਕ ਹਨ
   - ਅਸਲ markdown ਸਟ੍ਰੱਕਚਰ ਬਰਕਰਾਰ ਹੈ
   - ਲਿੰਕ ਅਤੇ ਚਿੱਤਰ ਠੀਕ ਕੰਮ ਕਰ ਰਹੇ ਹਨ

ਇਹ ਮੈਨੂਅਲ ਟੈਸਟਿੰਗ ਯਕੀਨੀ ਬਣਾਉਂਦੀ ਹੈ ਕਿ ਤੁਹਾਡੀਆਂ ਤਬਦੀਲੀਆਂ ਅਸਲ ਹਾਲਾਤਾਂ ਵਿੱਚ ਠੀਕ ਕੰਮ ਕਰਦੀਆਂ ਹਨ।

### ਇਨਵਾਇਰਨਮੈਂਟ ਵੈਰੀਏਬਲ

1. `.env.template` ਫਾਈਲ ਤੋਂ `.env` ਫਾਈਲ ਰੂਟ ਡਾਇਰੈਕਟਰੀ ਵਿੱਚ ਕਾਪੀ ਕਰਕੇ ਬਣਾਓ।
1. ਵੈਰੀਏਬਲ ਹਦਾਇਤਾਂ ਅਨੁਸਾਰ ਭਰੋ।

> [!TIP]
>
> ### ਹੋਰ ਡਿਵੈਲਪਮੈਂਟ ਇਨਵਾਇਰਨਮੈਂਟ ਵਿਕਲਪ
>
> ਪ੍ਰੋਜੈਕਟ ਨੂੰ ਲੋਕਲ ਚਲਾਉਣ ਦੇ ਇਲਾਵਾ, ਤੁਸੀਂ GitHub Codespaces ਜਾਂ VS Code Dev Containers ਵੀ ਵਰਤ ਸਕਦੇ ਹੋ।
>
> #### GitHub Codespaces
>
> ਤੁਸੀਂ ਇਹ ਸੈਂਪਲ GitHub Codespaces ਰਾਹੀਂ ਵਰਚੁਅਲ ਚਲਾ ਸਕਦੇ ਹੋ, ਕਿਸੇ ਵਾਧੂ ਸੈਟਅੱਪ ਦੀ ਲੋੜ ਨਹੀਂ।
>
> ਇਹ ਬਟਨ ਤੁਹਾਡੇ ਬਰਾਊਜ਼ਰ ਵਿੱਚ VS Code ਦਾ web-ਅਧਾਰਿਤ ਇੰਸਟੈਂਸ ਖੋਲ੍ਹੇਗਾ:
>
> 1. ਟੈਮਪਲੇਟ ਖੋਲ੍ਹੋ (ਇਸ ਵਿੱਚ ਕੁਝ ਮਿੰਟ ਲੱਗ ਸਕਦੇ ਹਨ):
>
>     [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/azure/co-op-translator)
>
> #### ਲੋਕਲ VS Code Dev Containers ਰਾਹੀਂ ਚਲਾਉਣਾ
>
> ⚠️ ਇਹ ਵਿਕਲਪ ਤਦ ਹੀ ਕੰਮ ਕਰੇਗਾ ਜੇ ਤੁਹਾਡੇ Docker Desktop ਨੂੰ ਘੱਟੋ-ਘੱਟ 16 GB RAM ਮਿਲੀ ਹੋਈ ਹੈ। ਜੇ ਤੁਹਾਡੇ ਕੋਲ 16 GB ਤੋਂ ਘੱਟ RAM ਹੈ, ਤਾਂ ਤੁਸੀਂ [GitHub Codespaces](../..) ਜਾਂ [ਲੋਕਲ ਸੈਟਅੱਪ](../..) ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰ ਸਕਦੇ ਹੋ।
>
> ਇੱਕ ਹੋਰ ਵਿਕਲਪ VS Code Dev Containers ਹੈ, ਜੋ ਤੁਹਾਡੇ ਲੋਕਲ VS Code ਵਿੱਚ [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) ਰਾਹੀਂ ਪ੍ਰੋਜੈਕਟ ਖੋਲ੍ਹੇਗਾ:
>
> 1. Docker Desktop ਚਲਾਓ (ਜੇ ਇੰਸਟਾਲ ਨਹੀਂ, ਤਾਂ ਪਹਿਲਾਂ ਇੰਸਟਾਲ ਕਰੋ)
> 2. ਪ੍ਰੋਜੈਕਟ ਖੋਲ੍ਹੋ:
>
>    [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator)


### ਕੋਡ ਸਟਾਈਲ

ਅਸੀਂ [Black](https://github.com/psf/black) ਨੂੰ Python ਕੋਡ ਫਾਰਮੈਟਰ ਵਜੋਂ ਵਰਤਦੇ ਹਾਂ, ਤਾਂ ਜੋ ਪ੍ਰੋਜੈਕਟ ਵਿੱਚ ਕੋਡ ਸਟਾਈਲ ਇਕਸਾਰ ਰਹੇ। Black ਇੱਕ uncompromising ਕੋਡ ਫਾਰਮੈਟਰ ਹੈ, ਜੋ Python ਕੋਡ ਨੂੰ ਆਪਣੇ ਸਟਾਈਲ ਅਨੁਸਾਰ ਆਪਣੇ-ਆਪ ਰੀਫਾਰਮੈਟ ਕਰਦਾ ਹੈ।

#### ਕਨਫਿਗਰੇਸ਼ਨ

Black ਦੀ ਕਨਫਿਗਰੇਸ਼ਨ ਸਾਡੀ `pyproject.toml` ਵਿੱਚ ਦਿੱਤੀ ਹੋਈ ਹੈ:

```toml
[tool.black]
line-length = 88
target-version = ['py310']
include = '\.pyi?$'
```

#### Black ਇੰਸਟਾਲ ਕਰਨਾ

ਤੁਸੀਂ Black Poetry (ਸਿਫਾਰਸ਼ੀ) ਜਾਂ pip ਰਾਹੀਂ ਇੰਸਟਾਲ ਕਰ ਸਕਦੇ ਹੋ:

##### Poetry ਨਾਲ

Poetry ਰਾਹੀਂ ਡਿਵੈਲਪਮੈਂਟ ਇਨਵਾਇਰਨਮੈਂਟ ਸੈਟਅੱਪ ਕਰਦੇ ਸਮੇਂ Black ਆਪਣੇ-ਆਪ ਇੰਸਟਾਲ ਹੋ ਜਾਂਦਾ ਹੈ:
```bash
poetry install
```

##### pip ਨਾਲ

ਜੇ ਤੁਸੀਂ pip ਵਰਤ ਰਹੇ ਹੋ, ਤਾਂ Black ਨੂੰ ਸਿੱਧਾ ਇੰਸਟਾਲ ਕਰ ਸਕਦੇ ਹੋ:
```bash
pip install black
```

#### Black ਵਰਤਣਾ

##### Poetry ਨਾਲ

1. ਪ੍ਰੋਜੈਕਟ ਵਿੱਚ ਸਾਰੇ Python ਫਾਈਲਾਂ ਫਾਰਮੈਟ ਕਰੋ:
    ```bash
    poetry run black .
    ```

2. ਕਿਸੇ ਖਾਸ ਫਾਈਲ ਜਾਂ ਡਾਇਰੈਕਟਰੀ ਨੂੰ ਫਾਰਮੈਟ ਕਰੋ:
    ```bash
    poetry run black path/to/file_or_directory
    ```

##### pip ਨਾਲ

1. ਪ੍ਰੋਜੈਕਟ ਵਿੱਚ ਸਾਰੇ Python ਫਾਈਲਾਂ ਫਾਰਮੈਟ ਕਰੋ:
    ```bash
    black .
    ```

2. ਕਿਸੇ ਖਾਸ ਫਾਈਲ ਜਾਂ ਡਾਇਰੈਕਟਰੀ ਨੂੰ ਫਾਰਮੈਟ ਕਰੋ:
    ```bash
    black path/to/file_or_directory
    ```

> [!TIP]
> ਅਸੀਂ ਤੁਹਾਨੂੰ ਆਪਣੇ ਐਡੀਟਰ ਨੂੰ Black ਨਾਲ save 'ਤੇ code auto-format ਕਰਨ ਲਈ ਸੈਟਅੱਪ ਕਰਨ ਦੀ ਸਿਫਾਰਸ਼ ਕਰਦੇ ਹਾਂ। ਜ਼ਿਆਦਾਤਰ modern editors ਵਿੱਚ ਇਹ extension ਜਾਂ plugins ਰਾਹੀਂ ਹੋ ਜਾਂਦਾ ਹੈ।

## Co-op Translator ਚਲਾਉਣਾ

Poetry ਰਾਹੀਂ Co-op Translator ਚਲਾਉਣ ਲਈ, ਇਹ ਕਦਮ ਅਪਣਾਓ:

1. ਜਿਸ ਡਾਇਰੈਕਟਰੀ ਵਿੱਚ ਤੁਸੀਂ ਟੈਸਟ ਕਰਨਾ ਚਾਹੁੰਦੇ ਹੋ ਜਾਂ ਟੈਸਟ ਲਈ temporary folder ਬਣਾਉਣਾ ਚਾਹੁੰਦੇ ਹੋ, ਉੱਥੇ ਜਾਓ।

2. ਹੇਠਾਂ ਦਿੱਤਾ ਕਮਾਂਡ ਚਲਾਓ। `-l ko` ਨੂੰ ਆਪਣੀ ਚਾਹੀਦੀ ਭਾਸ਼ਾ ਕੋਡ ਨਾਲ ਬਦਲੋ। `-d` flag debug mode ਲਈ ਹੈ।

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> [!NOTE]
> ਕਮਾਂਡ ਚਲਾਉਣ ਤੋਂ ਪਹਿਲਾਂ ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਤੁਹਾਡਾ Poetry ਇਨਵਾਇਰਨਮੈਂਟ ਐਕਟੀਵੇਟ ਹੈ (poetry shell)।

## ਨਵੀਂ ਭਾਸ਼ਾ ਲਈ ਯੋਗਦਾਨ ਪਾਓ

ਅਸੀਂ ਨਵੀਆਂ ਭਾਸ਼ਾਵਾਂ ਲਈ ਯੋਗਦਾਨ ਦਾ ਸਵਾਗਤ ਕਰਦੇ ਹਾਂ। PR ਖੋਲ੍ਹਣ ਤੋਂ ਪਹਿਲਾਂ, ਹੇਠਾਂ ਦਿੱਤੇ ਕਦਮ ਪੂਰੇ ਕਰੋ, ਤਾਂ ਜੋ review ਆਸਾਨੀ ਨਾਲ ਹੋ ਸਕੇ।

1. ਭਾਸ਼ਾ font mapping ਵਿੱਚ ਸ਼ਾਮਲ ਕਰੋ
   - `src/co_op_translator/fonts/font_language_mappings.yml` ਐਡਿਟ ਕਰੋ
   - ਹੇਠਾਂ ਦਿੱਤੇ attributes ਨਾਲ entry ਸ਼ਾਮਲ ਕਰੋ:
     - `code`: ISO-ਵਾਂਗ ਭਾਸ਼ਾ ਕੋਡ (ਜਿਵੇਂ `vi`)
     - `name`: ਆਮ ਵਰਤੋਂ ਵਾਲਾ ਨਾਂ
     - `font`: `src/co_op_translator/fonts/` ਵਿੱਚ ਮੌਜੂਦ font, ਜੋ script ਨੂੰ support ਕਰਦਾ ਹੋਵੇ
     - `rtl`: ਜੇ right-to-left ਹੈ ਤਾਂ `true`, ਨਹੀਂ ਤਾਂ `false`

2. ਲੋੜੀਂਦੇ font files ਸ਼ਾਮਲ ਕਰੋ (ਜੇ ਲੋੜ ਹੋਵੇ)
   - ਜੇ ਨਵਾਂ font ਚਾਹੀਦਾ ਹੈ, open source distribution ਲਈ license compatibility ਚੈੱਕ ਕਰੋ
   - font file `src/co_op_translator/fonts/` ਵਿੱਚ ਪਾਓ

3. ਲੋਕਲ ਵੈਰੀਫਿਕੇਸ਼ਨ
   - ਛੋਟਾ sample (Markdown, images, notebooks) 'ਤੇ ਟ੍ਰਾਂਸਲੇਸ਼ਨ ਚਲਾਓ
   - output ਠੀਕ render ਹੋ ਰਿਹਾ ਹੈ, font ਅਤੇ RTL layout ਸਮੇਤ, ਚੈੱਕ ਕਰੋ

4. ਡੌਕੂਮੈਂਟੇਸ਼ਨ ਅੱਪਡੇਟ ਕਰੋ
   - ਭਾਸ਼ਾ `getting_started/supported-languages.md` ਵਿੱਚ ਆਉਣੀ ਚਾਹੀਦੀ ਹੈ
   - `README_languages_template.md` 'ਚ ਕੋਈ ਤਬਦੀਲੀ ਨਹੀਂ ਚਾਹੀਦੀ; ਇਹ supported list ਤੋਂ ਬਣਦੀ ਹੈ

5. PR ਖੋਲ੍ਹੋ
   - ਜੋ ਭਾਸ਼ਾ ਐਡ ਕੀਤੀ, font/licensing ਬਾਰੇ ਜਾਣਕਾਰੀ ਦਿਓ
   - ਹੋ ਸਕੇ ਤਾਂ rendered output ਦੇ screenshots ਲਗਾਓ

YAML entry ਦੀ ਉਦਾਹਰਨ:

```yaml
new_lang(code):
  name: "New Language"
  font: "NotoSans-Medium.ttf"
  rtl: false
```


## ਮੈਨਟੇਨਰ

### Commit message ਅਤੇ Merge strategy

ਸਾਡੇ ਪ੍ਰੋਜੈਕਟ ਦੀ commit history ਵਿਚ consistency ਅਤੇ clarity ਲਈ, ਅਸੀਂ **Squash and Merge** strategy ਵਰਤਦੇ ਹੋਏ commit message ਲਈ ਖਾਸ format follow ਕਰਦੇ ਹਾਂ।

ਜਦੋਂ pull request (PR) merge ਹੁੰਦੀ ਹੈ, ਤਾਂ ਵੱਖ-ਵੱਖ commits ਇੱਕ commit ਵਿੱਚ squash ਹੋ ਜਾਂਦੇ ਹਨ। Final commit message ਹੇਠਾਂ ਦਿੱਤੇ format 'ਚ ਹੋਣਾ ਚਾਹੀਦਾ ਹੈ, ਤਾਂ ਜੋ history ਸਾਫ਼ ਅਤੇ consistent ਰਹੇ।

#### Commit message format (squash and merge ਲਈ)

ਅਸੀਂ commit messages ਲਈ ਹੇਠਾਂ ਦਿੱਤਾ format ਵਰਤਦੇ ਹਾਂ:

```bash
<type>: <description> (#<PR number>)
```

- **type**: commit ਦੀ category ਦੱਸਦਾ ਹੈ। ਅਸੀਂ ਹੇਠਾਂ ਦਿੱਤੇ types ਵਰਤਦੇ ਹਾਂ:
  - `Docs`: ਡੌਕੂਮੈਂਟੇਸ਼ਨ ਅੱਪਡੇਟ ਲਈ।
  - `Build`: build system ਜਾਂ dependencies ਨਾਲ ਜੁੜੀਆਂ ਤਬਦੀਲੀਆਂ ਲਈ, configuration files, CI workflows, Dockerfile ਸਮੇਤ।
  - `Core`: ਪ੍ਰੋਜੈਕਟ ਦੀ core functionality ਜਾਂ features ਵਿੱਚ ਤਬਦੀਲੀਆਂ ਲਈ, ਖਾਸ ਕਰਕੇ `src/co_op_translator/core` ਡਾਇਰੈਕਟਰੀ ਵਾਲੀਆਂ।

- **description**: ਤਬਦੀਲੀ ਦਾ ਸੰਖੇਪ ਸਾਰ।
- **PR number**: commit ਨਾਲ ਜੁੜੀ pull request ਦਾ ਨੰਬਰ।

**ਉਦਾਹਰਨਾਂ**:

- `Docs: Update installation instructions for clarity (#50)`
- `Core: Improve handling of image translation (#60)`

> [!NOTE]
> ਇਸ ਵੇਲੇ **`Docs`**, **`Core`**, ਅਤੇ **`Build`** prefixes PR titles 'ਚ labels ਦੇ ਆਧਾਰ 'ਤੇ ਆਪਣੇ-ਆਪ ਲੱਗ ਜਾਂਦੇ ਹਨ। ਜੇ ਸਹੀ label ਲੱਗਾ ਹੋਇਆ ਹੈ, ਤਾਂ ਤੁਹਾਨੂੰ PR title ਹੱਥੋਂ update ਕਰਨ ਦੀ ਲੋੜ ਨਹੀਂ। ਸਿਰਫ਼ ਇਹ ਚੈੱਕ ਕਰੋ ਕਿ prefix ਠੀਕ ਹੈ।

#### Merge strategy

ਅਸੀਂ pull requests ਲਈ **Squash and Merge** default strategy ਵਜੋਂ ਵਰਤਦੇ ਹਾਂ। ਇਸ strategy ਨਾਲ commit messages ਸਾਡਾ format follow ਕਰਦੇ ਹਨ, ਭਾਵੇਂ individual commits ਨਾ ਕਰਦੇ ਹੋਣ।

**ਕਾਰਨ**:

- ਸਾਫ਼, linear project history।
- commit messages 'ਚ consistency।
- minor commits (ਜਿਵੇਂ "fix typo") ਤੋਂ noise ਘੱਟ।

Merge ਕਰਦੇ ਸਮੇਂ, final commit message ਉਪਰੋਕਤ format 'ਚ ਹੋਣਾ ਚਾਹੀਦਾ ਹੈ।

**Squash and Merge ਦੀ ਉਦਾਹਰਨ**
ਜੇ PR ਵਿੱਚ ਹੇਠਾਂ ਦਿੱਤੇ commits ਹਨ:

- `fix typo`
- `update README`
- `adjust formatting`

ਇਹ squash ਹੋ ਕੇ ਬਣ ਜਾਣਗੇ:
`Docs: Improve documentation clarity and formatting (#65)`

---

**ਅਸਵੀਕਰਨ**:
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਅਸੀਂ ਯਥਾਸੰਭਵ ਸਹੀ ਅਨੁਵਾਦ ਕਰਨ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਪਰ ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਵਿੱਚ ਰੱਖੋ ਕਿ ਆਟੋਮੈਟਿਕ ਅਨੁਵਾਦ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਣਪਛਾਤੀਆਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼, ਜਿਸ ਭਾਸ਼ਾ ਵਿੱਚ ਉਹ ਲਿਖਿਆ ਗਿਆ ਹੈ, ਨੂੰ ਹੀ ਅਧਿਕਾਰਤ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਜਰੂਰੀ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਹੋਣ ਵਾਲੀ ਕਿਸੇ ਵੀ ਗਲਤਫਹਮੀ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆ ਲਈ ਅਸੀਂ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।