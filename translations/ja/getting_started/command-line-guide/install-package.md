<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b6d85d887d2664539a438dae5d0dfa50",
  "translation_date": "2025-06-12T18:32:26+00:00",
  "source_file": "getting_started/command-line-guide/install-package.md",
  "language_code": "ja"
}
-->
# Co-op Translatorパッケージのインストール

**Co-op Translator**は、プロジェクト内のすべてのMarkdownファイルや画像を複数の言語に翻訳するためのコマンドラインインターフェース（CLI）ツールです。このチュートリアルでは、翻訳ツールの設定方法やさまざまな使用例での実行方法を案内します。

### 仮想環境の作成

仮想環境は`pip`または`Poetry`のいずれかを使って作成できます。ターミナルで以下のいずれかのコマンドを入力してください。

#### pipを使う場合

```bash
python -m venv .venv
```

#### Poetryを使う場合

```bash
poetry init
```

### 仮想環境の有効化

仮想環境を作成したら、有効化する必要があります。使用しているOSによって手順が異なります。ターミナルで以下のコマンドを入力してください。

#### pipとPoetryの両方共通

- Windowsの場合：

    ```bash
    .venv\Scripts\activate
    ```

- Mac/Linuxの場合：

    ```bash
    source .venv/bin/activate
    ```

#### Poetryを使う場合

1. Poetryで環境を作成した場合は、以下のコマンドをターミナルで入力して有効化してください。

    ```bash
    poetry shell
    ```

### パッケージおよび必要な依存パッケージのインストール

仮想環境のセットアップと有効化が完了したら、次は必要な依存パッケージをインストールします。

### クイックインストール

Co-Op Translatorをpipでインストール

```
pip install co-op-translator
```  
または

poetryでインストール

```
poetry add co-op-translator
```

#### このリポジトリをクローンした場合のpip利用（requirements.txtから）

![NOTE] クイックインストールでco-op translatorをインストールした場合は、この方法は行わないでください。

1. pipを使う場合は、ターミナルで以下のコマンドを入力してください。`requirements.txt`に指定された必要なパッケージが自動的にインストールされます。

    ```bash
    pip install -r requirements.txt
    ```

#### Poetryを使う場合（pyproject.tomlから）

1. Poetryを使う場合は、ターミナルで以下のコマンドを入力してください。`pyproject.toml`に指定された必要なパッケージが自動的にインストールされます。

    ```bash
    poetry install
    ```

**免責事項**：  
本書類はAI翻訳サービス「[Co-op Translator](https://github.com/Azure/co-op-translator)」を使用して翻訳されました。正確性には努めておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。原文（原言語）の文書が正式な情報源とみなされます。重要な情報については、専門の人間による翻訳を推奨いたします。本翻訳の利用により生じた誤解や誤訳について、当方は一切の責任を負いかねます。