<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b6d85d887d2664539a438dae5d0dfa50",
  "translation_date": "2025-07-04T08:13:09+00:00",
  "source_file": "getting_started/command-line-guide/install-package.md",
  "language_code": "ja"
}
-->
# Co-op Translator パッケージのインストール

**Co-op Translator** は、プロジェクト内のすべてのMarkdownファイルと画像を複数の言語に翻訳するためのコマンドラインインターフェース (CLI) ツールです。このチュートリアルでは、翻訳ツールの設定方法とさまざまな使用例に対して実行する方法を説明します。

### 仮想環境の作成

`pip` または `Poetry` を使用して仮想環境を作成できます。ターミナル内で次のいずれかのコマンドを入力してください。

#### pipを使用する場合

```bash
python -m venv .venv
```

#### Poetryを使用する場合

```bash
poetry init
```

### 仮想環境のアクティベート

仮想環境を作成した後は、それをアクティベートする必要があります。手順はオペレーティングシステムによって異なります。ターミナル内で次のコマンドを入力してください。

#### pipとPoetryの両方の場合

- Windows:

    ```bash
    .venv\Scripts\activate
    ```

- Mac/Linux:

    ```bash
    source .venv/bin/activate
    ```

#### Poetryを使用する場合

1. Poetryで環境を作成した場合は、ターミナル内で次のコマンドを入力してアクティベートしてください。

    ```bash
    poetry shell
    ```

### パッケージと必要なパッケージのインストール

仮想環境が設定されてアクティベートされたら、次のステップは必要な依存関係をインストールすることです。

### クイックインストール

pipを使用してCo-Op Translatorをインストール

```
pip install co-op-translator
```
または

poetryを使用してインストール
```
poetry add co-op-translator
```

#### このリポジトリをクローンした場合、requirements.txtからpipを使用する

![NOTE] クイックインストールでco-op translatorをインストールした場合はこれを行わないでください。

1. pipを使用している場合は、ターミナル内で次のコマンドを入力してください。これにより、`requirements.txt`ファイルに指定された必要なパッケージが自動的にインストールされます。

    ```bash
    pip install -r requirements.txt
    ```

#### pyproject.tomlからPoetryを使用する場合

1. Poetryを使用している場合は、ターミナル内で次のコマンドを入力してください。これにより、`pyproject.toml`ファイルに指定された必要なパッケージが自動的にインストールされます。

    ```bash
    poetry install
    ```

**免責事項**:
この文書はAI翻訳サービス[Co-op Translator](https://github.com/Azure/co-op-translator)を使用して翻訳されています。正確性を追求していますが、自動翻訳には誤りや不正確さが含まれる可能性があることをご承知おきください。元の文書はその言語での権威ある情報源とみなされるべきです。重要な情報については、専門の人間による翻訳をお勧めします。この翻訳の使用に起因する誤解や誤った解釈について、当社は責任を負いません。