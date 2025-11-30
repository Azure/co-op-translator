<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "758ca1c5ae0d32c52d2dd59132dcfbf0",
  "translation_date": "2025-11-30T10:23:30+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "ja"
}
-->
# Co-op Translatorへの貢献について

このプロジェクトでは、貢献や提案を歓迎しています。ほとんどの貢献には、あなたが貢献物の使用権を当社に付与する権利を持ち、実際に付与していることを宣言するContributor License Agreement（CLA）への同意が必要です。詳細は https://cla.opensource.microsoft.com をご覧ください。

プルリクエストを提出すると、CLAボットが自動的にCLAの提出が必要かどうかを判定し、PRに適切な装飾（ステータスチェックやコメントなど）を行います。ボットの指示に従うだけで、当社のCLAを使用しているすべてのリポジトリで一度だけ対応すれば済みます。

## 開発環境のセットアップ

このプロジェクトの開発環境をセットアップするには、依存関係管理にPoetryの使用を推奨します。`pyproject.toml`でプロジェクトの依存関係を管理しているため、依存関係のインストールにはPoetryを使ってください。

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

PRを提出する前に、実際のドキュメントで翻訳機能をテストすることが重要です：

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

5. `test_docs/translations` と `test_docs/translated_images` にある翻訳ファイルを確認し、以下を検証します：
   - 翻訳の品質
   - メタデータコメントが正しいこと
   - 元のマークダウン構造が保持されていること
   - リンクや画像が正しく動作していること

この手動テストにより、変更が実際の使用環境で問題なく動作することを確認できます。

### 環境変数

1. ルートディレクトリに `.env.template` をコピーして `.env` ファイルを作成します。
2. 指示に従って環境変数を入力してください。

> [!TIP]
>
> ### 追加の開発環境オプション
>
> ローカルでプロジェクトを実行する以外に、GitHub CodespacesやVS Code Dev Containersを使った代替の開発環境セットアップも可能です。
>
> #### GitHub Codespaces
>
> GitHub Codespacesを使えば、追加の設定なしでこのサンプルを仮想的に実行できます。
>
> 以下のボタンをクリックすると、ブラウザ上でVS Codeのインスタンスが開きます：
>
> 1. テンプレートを開く（数分かかる場合があります）：
>
>     [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/azure/co-op-translator)
>
> #### VS Code Dev Containersを使ってローカルで実行する場合
>
> ⚠️ この方法はDocker Desktopに最低16GBのRAMが割り当てられている場合にのみ動作します。16GB未満の場合は、[GitHub Codespacesオプション](../..)を試すか、[ローカルセットアップ](../..)を行ってください。
>
> 関連オプションとして、VS Code Dev Containersがあります。これは[Dev Containers拡張機能](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)を使い、ローカルのVS Codeでプロジェクトを開きます：
>
> 1. Docker Desktopを起動（未インストールの場合はインストール）
> 2. プロジェクトを開く：
>
>    [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator)


### コードスタイル

プロジェクト全体で一貫したコードスタイルを保つために、Pythonコードフォーマッターとして[Black](https://github.com/psf/black)を使用しています。Blackは妥協のないコードフォーマッターで、Pythonコードを自動的にBlackのスタイルに整形します。

#### 設定

Blackの設定は `pyproject.toml` に記載されています：

```toml
[tool.black]
line-length = 88
target-version = ['py310']
include = '\.pyi?$'
```

#### Blackのインストール

BlackはPoetry（推奨）またはpipでインストールできます：

##### Poetryを使う場合

開発環境セットアップ時にBlackは自動的にインストールされます：
```bash
poetry install
```

##### pipを使う場合

pipを使う場合はBlackを直接インストールできます：
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
> エディターで保存時にBlackで自動整形する設定を推奨します。多くのモダンなエディターは拡張機能やプラグインで対応しています。

## Co-op Translatorの実行

Poetryを使ってCo-op Translatorを実行するには、以下の手順に従ってください：

1. 翻訳テストを行いたいディレクトリに移動するか、一時的なフォルダーを作成します。

2. 以下のコマンドを実行します。`-l ko` の部分は翻訳先の言語コードに置き換えてください。`-d` はデバッグモードを示します。

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> [!NOTE]
> コマンド実行前にPoetry環境が有効（poetry shell）になっていることを確認してください。

## 新しい言語の追加

新しい言語のサポート追加も歓迎します。PRを開く前に、スムーズなレビューのために以下の手順を完了してください。

1. フォントマッピングに言語を追加
   - `src/co_op_translator/fonts/font_language_mappings.yml` を編集
   - 以下の項目を追加：
     - `code`: ISO風の言語コード（例：`vi`）
     - `name`: 人間にわかりやすい表示名
     - `font`: `src/co_op_translator/fonts/` に含まれる、そのスクリプトをサポートするフォント
     - `rtl`: 右から左の言語なら `true`、それ以外は `false`

2. 必要なフォントファイルを含める（必要な場合）
   - 新しいフォントが必要な場合は、オープンソース配布のライセンス互換性を確認
   - フォントファイルを `src/co_op_translator/fonts/` に追加

3. ローカルでの検証
   - 小さなサンプル（Markdown、画像、ノートブックなど）で翻訳を実行
   - フォントやRTLレイアウトを含め、出力が正しくレンダリングされることを確認

4. ドキュメントの更新
   - `getting_started/supported-languages.md` に言語が表示されていることを確認
   - `getting_started/README_languages_template.md` はサポートリストから生成されるため変更不要

5. PRを開く
   - 追加した言語やフォント・ライセンスの注意点を説明
   - 可能ならレンダリング結果のスクリーンショットを添付

YAMLの例：

```yaml
new_lang(code):
  name: "New Language"
  font: "NotoSans-Medium.ttf"
  rtl: false
```

### 新しい言語のテスト

以下のコマンドで新しい言語をテストできます：

```bash
# 仮想環境を作成して有効化する
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
# 開発パッケージをインストールする
pip install -e .
# 翻訳を実行する
translate -l "new_lang"
```

## メンテナ

### コミットメッセージとマージ戦略

プロジェクトのコミット履歴の一貫性と明確さを保つため、**Squash and Merge**戦略を使う際の**最終コミットメッセージ**には特定のフォーマットを使用します。

プルリクエスト（PR）がマージされると、個々のコミットは1つにまとめられます。最終コミットメッセージは以下のフォーマットに従い、履歴をきれいに保ちます。

#### コミットメッセージのフォーマット（Squash and Merge用）

コミットメッセージは以下の形式を使います：

```bash
<type>: <description> (#<PR番号>)
```

- **type**: コミットのカテゴリを示します。以下のタイプを使用します：
  - `Docs`: ドキュメントの更新
  - `Build`: ビルドシステムや依存関係の変更（設定ファイル、CIワークフロー、Dockerfileの更新など）
  - `Core`: プロジェクトのコア機能や特徴の変更、特に `src/co_op_translator/core` ディレクトリ内のファイルに関するもの

- **description**: 変更内容の簡潔な要約
- **PR番号**: 関連するプルリクエストの番号

**例**：

- `Docs: インストール手順の明確化 (#50)`
- `Core: 画像翻訳処理の改善 (#60)`

> [!NOTE]
> 現在、**`Docs`**、**`Core`**、**`Build`** のプレフィックスは、変更されたソースコードに付けられたラベルに基づいてPRタイトルに自動的に追加されます。正しいラベルが付いていれば、通常はPRタイトルを手動で変更する必要はありません。内容が正しいか、プレフィックスが適切に生成されているかを確認してください。

#### マージ戦略

プルリクエストのマージには**Squash and Merge**をデフォルトで使用しています。この方法により、個々のコミットがフォーマットに従っていなくても、最終的なコミットメッセージは一貫した形式になります。

**理由**：

- クリーンで直線的なプロジェクト履歴
- コミットメッセージの一貫性
- 小さなコミット（例：「typo修正」）によるノイズの削減

マージ時には、最終コミットメッセージが上記のフォーマットに従っていることを確認してください。

**Squash and Mergeの例**  
PRに以下のコミットがある場合：

- `fix typo`
- `update README`
- `adjust formatting`

これらは以下のようにまとめられます：  
`Docs: ドキュメントの明確化とフォーマット調整 (#65)`

### リリース手順

ここでは、メンテナがCo-op Translatorの新しいリリースを公開する最も簡単な方法を説明します。

#### 1. `pyproject.toml` のバージョンを更新

1. 次のバージョン番号を決定します（セマンティックバージョニング：`MAJOR.MINOR.PATCH`に従う）。
2. `pyproject.toml` の `[tool.poetry]` セクションの `version` フィールドを更新します。
3. バージョンのみ（および自動更新されたロックファイルやメタデータファイルがあればそれも）を変更する専用のプルリクエストを作成します。
4. レビュー後、**Squash and Merge**を使い、最終コミットメッセージが上記フォーマットに従っていることを確認します。

#### 2. GitHubリリースを作成

1. GitHubリポジトリのページで **Releases** → **Draft a new release** を開きます。
2. `main` ブランチから新しいタグ（例：`v0.13.0`）を作成します。
3. リリースタイトルを同じバージョン（例：`v0.13.0`）に設定します。
4. **Generate release notes** をクリックして変更履歴を自動生成します。
5. 必要に応じてテキストを編集（新しくサポートされた言語や重要な変更点の強調など）。
6. リリースを公開します。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：  
本書類はAI翻訳サービス「Co-op Translator」（https://github.com/Azure/co-op-translator）を使用して翻訳されました。正確性の向上に努めておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。原文の言語による文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じた誤解や誤訳について、当方は一切の責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->