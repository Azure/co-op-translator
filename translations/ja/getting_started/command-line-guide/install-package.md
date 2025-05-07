<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b6d85d887d2664539a438dae5d0dfa50",
  "translation_date": "2025-05-06T17:56:03+00:00",
  "source_file": "getting_started/command-line-guide/install-package.md",
  "language_code": "ja"
}
-->
# Co-op translator パッケージのインストール

**Co-op Translator** は、プロジェクト内のすべてのマークダウンファイルや画像を複数の言語に翻訳するためのコマンドラインインターフェース（CLI）ツールです。このチュートリアルでは、翻訳ツールの設定方法とさまざまな使い方について説明します。

### 仮想環境の作成

仮想環境は `pip` または `Poetry` を使って作成できます。ターミナルで以下のいずれかのコマンドを入力してください。

#### pip を使う場合

```bash
python -m venv .venv
```

#### Poetry を使う場合

```bash
poetry init
```

### 仮想環境の有効化

仮想環境を作成したら、それを有効化する必要があります。使用しているOSによって手順が異なります。ターミナルで以下のコマンドを入力してください。

#### pip と Poetry 共通

- Windows:

    ```bash
    .venv\Scripts\activate
    ```

- Mac/Linux:

    ```bash
    source .venv/bin/activate
    ```

#### Poetry を使う場合

1. Poetryで環境を作成した場合は、以下のコマンドをターミナルで入力して有効化します。

    ```bash
    poetry shell
    ```

### パッケージおよび必要な依存関係のインストール

仮想環境のセットアップと有効化が完了したら、次に必要な依存パッケージをインストールします。

### クイックインストール

pip を使って Co-Op Translator をインストール

```
pip install co-op-translator
```
または

poetry を使ってインストール

```
poetry add co-op-translator
```

#### pip を使う場合（リポジトリをクローンした場合）

![NOTE] クイックインストールで co-op translator をインストールする場合は、この方法を使わないでください。

1. pip を使う場合は、以下のコマンドをターミナルで入力してください。`requirements.txt` に記載された必要なパッケージが自動的にインストールされます。

    ```bash
    pip install -r requirements.txt
    ```

#### Poetry を使う場合（pyproject.toml から）

1. Poetry を使う場合は、以下のコマンドをターミナルで入力してください。`pyproject.toml` に記載された必要なパッケージが自動的にインストールされます。

    ```bash
    poetry install
    ```

**免責事項**：  
本書類はAI翻訳サービス「Co-op Translator」（https://github.com/Azure/co-op-translator）を使用して翻訳されています。正確性には努めておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。原文の言語によるオリジナルの文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じた誤解や誤訳について、当方は一切の責任を負いかねます。