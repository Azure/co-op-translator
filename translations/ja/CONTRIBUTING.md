<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d95d7ec0097c5569ac16dd42840787a2",
  "translation_date": "2025-07-04T08:09:02+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "ja"
}
-->
# Co-op Translatorへの貢献

このプロジェクトは貢献と提案を歓迎します。ほとんどの貢献には、貢献者ライセンス契約（CLA）に同意する必要があります。CLAは、あなたが貢献する権利を持ち、実際に貢献を使用する権利を私たちに与えることを宣言するものです。詳細は、https://cla.opensource.microsoft.com をご覧ください。

プルリクエストを提出すると、CLAボットが自動的にCLAを提供する必要があるかどうかを判断し、PRに適切に装飾を施します（例：ステータスチェック、コメント）。ボットの指示に従うだけで済みます。CLAを使用するすべてのリポジトリでこれを一度だけ行う必要があります。

## 開発環境のセットアップ

このプロジェクトの開発環境をセットアップするには、依存関係管理にPoetryを使用することをお勧めします。プロジェクトの依存関係を管理するために`pyproject.toml`を使用しているため、依存関係をインストールするにはPoetryを使用してください。

### 仮想環境の作成

#### pipを使用する場合

```bash
python -m venv .venv
```

#### Poetryを使用する場合

```bash
poetry init
```

### 仮想環境のアクティブ化

#### pipとPoetryの両方の場合

- Windows:

    ```bash
    .venv\Scripts\activate.bat
    ```

- Mac/Linux:

    ```bash
    source .venv/bin/activate
    ```

#### Poetryを使用する場合

```bash
poetry shell
```

### パッケージと必要なパッケージのインストール

#### Poetryを使用する場合（pyproject.tomlから）

```bash
poetry install
```

### 手動テスト

PRを提出する前に、実際のドキュメントで翻訳機能をテストすることが重要です：

1. ルートディレクトリにテストディレクトリを作成します：
    ```bash
    mkdir test_docs
    ```

2. 翻訳したいMarkdownドキュメントと画像をテストディレクトリにコピーします。例えば：
    ```bash
    cp /path/to/your/docs/*.md test_docs/
    cp /path/to/your/images/*.png test_docs/
    ```

3. パッケージをローカルにインストールします：
    ```bash
    pip install -e .
    ```

4. テストドキュメントでCo-op Translatorを実行します：
    ```bash
    python -m co_op_translator --language-codes ko --root-dir test_docs
    ```

5. `test_docs/translations`と`test_docs/translated_images`で翻訳されたファイルを確認して、以下を検証します：
   - 翻訳の品質
   - メタデータコメントが正しいか
   - 元のMarkdown構造が保持されているか
   - リンクと画像が正しく動作しているか

この手動テストは、実際のシナリオで変更がうまく機能することを確認するのに役立ちます。

### 環境変数

1. 提供された`.env.template`ファイルをコピーして、ルートディレクトリに`.env`ファイルを作成します。
1. 指示に従って環境変数を入力します。

> [!TIP]
>
> ### 追加の開発環境オプション
>
> プロジェクトをローカルで実行することに加えて、GitHub CodespacesやVS Code Dev Containersを使用して代替の開発環境をセットアップすることもできます。
>
> #### GitHub Codespaces
>
> GitHub Codespacesを使用してサンプルを仮想的に実行することができ、追加の設定やセットアップは不要です。
>
> ボタンをクリックすると、ブラウザでWebベースのVS Codeインスタンスが開きます：
>
> 1. テンプレートを開く（数分かかる場合があります）：
>
>     [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/azure/co-op-translator)
>
> #### VS Code Dev Containersを使用してローカルで実行する
>
> ⚠️ このオプションは、Docker Desktopに少なくとも16 GBのRAMが割り当てられている場合にのみ機能します。16 GB未満のRAMを持っている場合は、[GitHub Codespacesオプション](../..)を試すか、[ローカルでセットアップ](../..)してください。
>
> 関連するオプションはVS Code Dev Containersで、[Dev Containers拡張機能](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)を使用してローカルのVS Codeでプロジェクトを開きます：
>
> 1. Docker Desktopを起動する（インストールされていない場合はインストールする）
> 2. プロジェクトを開く：
>
>    [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator)

### コードスタイル

プロジェクト全体で一貫したコードスタイルを維持するために、Pythonコードフォーマッタとして[Black](https://github.com/psf/black)を使用しています。Blackは妥協のないコードフォーマッタで、Pythonコードを自動的にBlackコードスタイルに準拠するように再フォーマットします。

#### 設定

Blackの設定は`pyproject.toml`に指定されています：

```toml
[tool.black]
line-length = 88
target-version = ['py310']
include = '\.pyi?$'
```

#### Blackのインストール

BlackはPoetry（推奨）またはpipを使用してインストールできます：

##### Poetryを使用する場合

開発環境をセットアップするとBlackが自動的にインストールされます：
```bash
poetry install
```

##### pipを使用する場合

pipを使用している場合は、Blackを直接インストールできます：
```bash
pip install black
```

#### Blackの使用

##### Poetryを使用する場合

1. プロジェクト内のすべてのPythonファイルをフォーマットします：
    ```bash
    poetry run black .
    ```

2. 特定のファイルまたはディレクトリをフォーマットします：
    ```bash
    poetry run black path/to/file_or_directory
    ```

##### pipを使用する場合

1. プロジェクト内のすべてのPythonファイルをフォーマットします：
    ```bash
    black .
    ```

2. 特定のファイルまたはディレクトリをフォーマットします：
    ```bash
    black path/to/file_or_directory
    ```

> [!TIP]
> エディタを設定して、保存時にBlackでコードを自動的にフォーマットすることをお勧めします。ほとんどの最新のエディタは、拡張機能やプラグインを通じてこれをサポートしています。

## Co-op Translatorの実行

Poetryを使用して環境でCo-op Translatorを実行するには、以下の手順に従ってください：

1. 翻訳テストを行いたいディレクトリに移動するか、テスト目的のために一時フォルダを作成します。

2. 次のコマンドを実行します。`-l ko`を翻訳したい言語コードに置き換えてください。`-d`フラグはデバッグモードを示します。

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> [!NOTE]
> コマンドを実行する前に、Poetry環境がアクティブ化されていることを確認してください（poetry shell）。

## メンテナー

### コミットメッセージとマージ戦略

プロジェクトのコミット履歴の一貫性と明確さを確保するために、**Squash and Merge**戦略を使用する際の**最終コミットメッセージ**の形式に従います。

プルリクエスト（PR）がマージされると、個々のコミットは1つのコミットにまとめられます。最終コミットメッセージは、以下の形式に従って、クリーンで一貫した履歴を維持する必要があります。

#### コミットメッセージ形式（Squash and Mergeの場合）

コミットメッセージには以下の形式を使用します：

```bash
<type>: <description> (#<PR number>)
```

- **type**: コミットのカテゴリを指定します。以下のタイプを使用します：
  - `Docs`: ドキュメントの更新。
  - `Build`: ビルドシステムや依存関係に関連する変更、設定ファイル、CIワークフロー、Dockerfileの更新を含む。
  - `Core`: プロジェクトのコア機能や特徴の変更、特に`src/co_op_translator/core`ディレクトリ内のファイルに関するもの。

- **description**: 変更の簡潔な概要。
- **PR number**: コミットに関連するプルリクエストの番号。

**例**：

- `Docs: インストール手順を明確に更新 (#50)`
- `Core: 画像翻訳の処理を改善 (#60)`

> [!NOTE]
> 現在、**`Docs`**、**`Core`**、**`Build`** のプレフィックスは、変更されたソースコードに適用されたラベルに基づいてPRタイトルに自動的に追加されます。正しいラベルが適用されている限り、通常はPRタイトルを手動で更新する必要はありません。すべてが正しいことを確認し、プレフィックスが適切に生成されていることを確認するだけです。

#### マージ戦略

プルリクエストには**Squash and Merge**をデフォルトの戦略として使用します。この戦略は、個々のコミットがそうでなくても、コミットメッセージが私たちの形式に従うことを保証します。

**理由**：

- クリーンで直線的なプロジェクト履歴。
- コミットメッセージの一貫性。
- マイナーなコミット（例："fix typo"）によるノイズの削減。

マージする際は、最終コミットメッセージが上記のコミットメッセージ形式に従っていることを確認してください。

**Squash and Mergeの例**
PRに以下のコミットが含まれている場合：

- `fix typo`
- `update README`
- `adjust formatting`

それらは次のようにまとめられるべきです：
`Docs: ドキュメントの明確さとフォーマットを改善 (#65)`

**免責事項**:
この文書はAI翻訳サービス[Co-op Translator](https://github.com/Azure/co-op-translator)を使用して翻訳されています。正確性を追求していますが、自動翻訳には誤りや不正確さが含まれる可能性があることをご了承ください。元の言語での文書が権威ある情報源とみなされるべきです。重要な情報については、専門の人間による翻訳をお勧めします。この翻訳の使用に起因する誤解や誤解について、当社は責任を負いません。
