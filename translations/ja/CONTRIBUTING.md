<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d95d7ec0097c5569ac16dd42840787a2",
  "translation_date": "2025-06-12T09:28:48+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "ja"
}
-->
# Co-op Translatorへの貢献

このプロジェクトでは、貢献や提案を歓迎しています。ほとんどの貢献には、Contributor License Agreement（CLA）に同意していただく必要があります。CLAは、あなたが貢献物の権利を持ち、実際に私たちにその使用権を許諾していることを宣言するものです。詳細は https://cla.opensource.microsoft.com をご覧ください。

プルリクエストを提出すると、CLAボットが自動的にCLAの提出が必要かどうかを判定し、プルリクエストに適切な装飾（ステータスチェックやコメントなど）を付けます。ボットの指示に従うだけで構いません。CLAはすべてのリポジトリで一度だけ行えば大丈夫です。

## 開発環境のセットアップ

このプロジェクトの開発環境をセットアップするには、依存関係管理にPoetryの使用を推奨します。プロジェクトの依存関係管理には`pyproject.toml`を使用しているため、依存関係のインストールにはPoetryを使ってください。

### 仮想環境の作成

#### pipを使う場合

```bash
python -m venv .venv
```

#### Poetryを使う場合

```bash
poetry init
```

### 仮想環境の有効化

#### pipとPoetryの両方の場合

- Windows:

    ```bash
    .venv\Scripts\activate.bat
    ```

- Mac/Linux:

    ```bash
    source .venv/bin/activate
    ```

#### Poetryを使う場合

```bash
poetry shell
```

### パッケージと必要なパッケージのインストール

#### Poetryを使う場合（pyproject.tomlから）

```bash
poetry install
```

### 手動テスト

プルリクエストを提出する前に、実際のドキュメントで翻訳機能をテストすることが重要です：

1. ルートディレクトリにテスト用ディレクトリを作成します：
    ```bash
    mkdir test_docs
    ```

2. 翻訳したいマークダウンのドキュメントや画像をテストディレクトリにコピーします。例：
    ```bash
    cp /path/to/your/docs/*.md test_docs/
    cp /path/to/your/images/*.png test_docs/
    ```

3. パッケージをローカルにインストールします：
    ```bash
    pip install -e .
    ```

4. テストドキュメントに対してCo-op Translatorを実行します：
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

1. Create an `.env` file in the root directory by copying the provided `.env.template` ファイル内の翻訳済みファイルを確認します。
1. 環境変数を指示に従って入力してください。

> [!TIP]
>
> ### 追加の開発環境オプション
>
> ローカルでプロジェクトを実行する以外に、GitHub CodespacesやVS Code Dev Containersを使った開発環境構築も可能です。
>
> #### GitHub Codespaces
>
> GitHub Codespacesを使えば、追加の設定なしにブラウザ上でVS Codeを実行できます。
>
> ボタンをクリックするとブラウザでVS Codeが開きます：
>
> 1. テンプレートを開きます（数分かかる場合があります）：
>
>     [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/azure/co-op-translator)
>
> #### VS Code Dev Containersを使ったローカル実行
>
> ⚠️ このオプションはDocker Desktopに最低16GBのRAMが割り当てられている場合にのみ動作します。16GB未満の場合は[GitHub Codespacesオプション](../..)か[ローカルセットアップ](../..)をお試しください。
>
> 関連オプションとしてVS Code Dev Containersがあります。これはローカルのVS Codeで[Dev Containers拡張機能](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)を使ってプロジェクトを開きます：
>
> 1. Docker Desktopを起動します（未インストールの場合はインストールしてください）
> 2. プロジェクトを開きます：
>
>    [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator)


### コードスタイル

プロジェクト全体で一貫したコードスタイルを維持するために、Pythonコードフォーマッターとして[Black](https://github.com/psf/black)を使用しています。Blackは妥協しないコードフォーマッターで、自動的にPythonコードをBlackのコードスタイルに整形します。

#### 設定

Blackの設定は`pyproject.toml`に記載されています：

```toml
[tool.black]
line-length = 88
target-version = ['py310']
include = '\.pyi?$'
```

#### Blackのインストール

BlackはPoetry（推奨）またはpipでインストールできます：

##### Poetryを使う場合

開発環境のセットアップ時にBlackは自動的にインストールされます：
```bash
poetry install
```

##### pipを使う場合

pipを使う場合はBlackを直接インストールしてください：
```bash
pip install black
```

#### Blackの使い方

##### Poetryの場合

1. プロジェクト内のすべてのPythonファイルを整形：
    ```bash
    poetry run black .
    ```

2. 特定のファイルやディレクトリを整形：
    ```bash
    poetry run black path/to/file_or_directory
    ```

##### pipの場合

1. プロジェクト内のすべてのPythonファイルを整形：
    ```bash
    black .
    ```

2. 特定のファイルやディレクトリを整形：
    ```bash
    black path/to/file_or_directory
    ```

> [!TIP]
> 保存時にBlackで自動整形するようエディタを設定することをおすすめします。多くのモダンなエディタは拡張機能やプラグインで対応しています。

## Co-op Translatorの実行

Poetryを使ってCo-op Translatorを実行するには、以下の手順に従ってください：

1. 翻訳テストを行いたいディレクトリに移動するか、テスト用の一時フォルダを作成します。

2. 次のコマンドを実行します。`-l ko` with the language code you wish to translate into. The `-d` はデバッグモードを示します。

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> [!NOTE]
> コマンド実行前にPoetry環境が有効（poetry shell）になっていることを確認してください。

## メンテナ

### コミットメッセージとマージ戦略

プロジェクトのコミット履歴の一貫性と明瞭さを保つため、**Squash and Merge**戦略を使う際の**最終コミットメッセージ**には特定のフォーマットを使用しています。

プルリクエスト（PR）がマージされると、個々のコミットは一つにまとめられます。最終コミットメッセージは以下のフォーマットに従い、履歴をきれいに保ちます。

#### コミットメッセージのフォーマット（Squash and Merge用）

コミットメッセージは以下の形式を使います：

```bash
<type>: <description> (#<PR number>)
```

- **type**: コミットのカテゴリを指定します。以下のタイプを使います：
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

**免責事項**：  
本書類はAI翻訳サービス「[Co-op Translator](https://github.com/Azure/co-op-translator)」を使用して翻訳されました。正確性の向上に努めておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご了承ください。原文の言語による文書が正式な情報源とみなされます。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や誤訳についても、当方は一切の責任を負いかねます。