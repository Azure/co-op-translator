<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "510827ad22a2031a50838919c3594828",
  "translation_date": "2025-10-15T02:38:58+00:00",
  "source_file": "getting_started/command-line-guide/install-package.md",
  "language_code": "ja"
}
-->
# Co-op Translator パッケージのインストール

**Co-op Translator** は、プロジェクト内のすべてのMarkdownファイルや画像を複数の言語に翻訳するためのコマンドラインインターフェース（CLI）ツールです。このチュートリアルでは、トランスレーターの設定方法や、さまざまな用途での実行方法について説明します。

### 仮想環境の作成

仮想環境は `pip` または `Poetry` のどちらかを使って作成できます。ターミナルで以下のいずれかのコマンドを入力してください。

#### pipを使う場合

```bash
python -m venv .venv
```

#### Poetryを使う場合

```bash
poetry init
```

### 仮想環境の有効化

仮想環境を作成したら、有効化する必要があります。手順はOSによって異なります。ターミナルで以下のコマンドを入力してください。

#### pip・Poetry共通

- Windowsの場合:

    ```bash
    .venv\Scripts\activate
    ```

- Mac/Linuxの場合:

    ```bash
    source .venv/bin/activate
    ```

#### Poetryを使う場合

1. Poetryで環境を作成した場合は、ターミナルで以下のコマンドを入力して有効化してください。

    ```bash
    poetry shell
    ```

### パッケージと必要なパッケージのインストール

仮想環境のセットアップと有効化が完了したら、必要な依存パッケージをインストールします。

### クイックインストール

Co-Op Translatorをpipでインストール

```
pip install co-op-translator
```
または

Poetryでインストール
```
poetry add co-op-translator
```

#### このリポジトリをクローンした場合のpip（requirements.txtから）

> [!NOTE]
> クイックインストールでco-op translatorをインストールした場合は、こちらの手順は行わないでください。

1. pipを使う場合は、ターミナルで以下のコマンドを入力してください。`requirements.txt` ファイルに記載された必要なパッケージが自動的にインストールされます。

    ```bash
    pip install -r requirements.txt
    ```

#### Poetry（pyproject.tomlから）

1. Poetryを使う場合は、ターミナルで以下のコマンドを入力してください。`pyproject.toml` ファイルに記載された必要なパッケージが自動的にインストールされます。

    ```bash
    poetry install
    ```

---

**免責事項**：
本書類は、AI翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性には努めておりますが、自動翻訳には誤りや不正確な表現が含まれる場合がありますのでご注意ください。原文（元の言語の文書）が正式な情報源となります。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用によって生じたいかなる誤解や誤認についても、当方は責任を負いかねます。