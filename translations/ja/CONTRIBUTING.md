<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "bd4704f50c55da7d572b691484aa0b30",
  "translation_date": "2025-10-15T02:37:01+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "ja"
}
-->
# Co-op Translatorへの貢献

このプロジェクトでは、貢献や提案を歓迎しています。ほとんどの貢献には、Contributor License Agreement（CLA）への同意が必要です。これは、あなたが貢献する権利を持ち、実際にその権利を私たちに付与することを宣言するものです。詳細は https://cla.opensource.microsoft.com をご覧ください。

プルリクエストを提出すると、CLAボットが自動的にCLAの提出が必要かどうかを判断し、PRにステータスチェックやコメントなどを付与します。ボットの指示に従ってください。CLAへの同意は、CLAを利用しているすべてのリポジトリで一度だけ行えば大丈夫です。

## 開発環境のセットアップ

このプロジェクトの開発環境をセットアップするには、依存関係管理にPoetryの利用を推奨しています。プロジェクトの依存関係は `pyproject.toml` で管理しているため、依存関係のインストールにはPoetryを使ってください。

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

#### pip・Poetry共通

- Windowsの場合:

    ```bash
    .venv\Scripts\activate.bat
    ```

- Mac/Linuxの場合:

    ```bash
    source .venv/bin/activate
    ```

#### Poetryを使う場合

```bash
poetry shell
```

### パッケージと必要なパッケージのインストール

#### Poetry（pyproject.tomlから）

```bash
poetry install
```

### 手動テスト

PRを提出する前に、実際のドキュメントで翻訳機能をテストすることが重要です。

1. ルートディレクトリにテスト用ディレクトリを作成します:
    ```bash
    mkdir test_docs
    ```

2. 翻訳したいMarkdownドキュメントや画像をテストディレクトリにコピーします。例:
    ```bash
    cp /path/to/your/docs/*.md test_docs/
    cp /path/to/your/images/*.png test_docs/
    ```

3. パッケージをローカルにインストールします:
    ```bash
    pip install -e .
    ```

4. テストドキュメントでCo-op Translatorを実行します:
    ```bash
    python -m co_op_translator --language-codes ko --root-dir test_docs
    ```

5. `test_docs/translations` と `test_docs/translated_images` の翻訳済みファイルを確認し、以下を検証します:
   - 翻訳品質
   - メタデータコメントが正しいか
   - 元のMarkdown構造が保持されているか
   - リンクや画像が正しく動作しているか

この手動テストにより、あなたの変更が実際の利用シーンで問題なく動作することを確認できます。

### 環境変数

1. ルートディレクトリに `.env.template` ファイルをコピーして `.env` ファイルを作成します。
1. 指示に従って環境変数を記入してください。

> [!TIP]
>
> ### 開発環境の追加オプション
>
> プロジェクトをローカルで実行する以外にも、GitHub CodespacesやVS Code Dev Containersを使って開発環境をセットアップできます。
>
> #### GitHub Codespaces
>
> GitHub Codespacesを使えば、追加の設定やセットアップなしでサンプルを仮想的に実行できます。
>
> ボタンをクリックすると、ブラウザ上でWeb版VS Codeが開きます:
>
> 1. テンプレートを開く（数分かかる場合があります）:
>
>     <a href="https://codespaces.new/azure/co-op-translator"><img src="https://github.com/codespaces/badge.svg" alt="Open in GitHub Codespaces"></a>
>
> #### VS Code Dev Containersを使ってローカルで実行
>
> ⚠️ このオプションは、Docker Desktopに最低16GBのRAMが割り当てられている場合のみ動作します。16GB未満の場合は、[GitHub Codespacesオプション](../..)や[ローカルセットアップ](../..)をお試しください。
>
> 関連オプションとしてVS Code Dev Containersがあります。これは[Dev Containers拡張機能](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)を使い、ローカルのVS Codeでプロジェクトを開きます:
>
> 1. Docker Desktopを起動（未インストールの場合はインストール）
> 2. プロジェクトを開く:
>
>    <a href="https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator"><img src="https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode" alt="Open in Dev Containers"></a>


### コードスタイル

プロジェクト全体のコードスタイルを統一するため、Pythonコードフォーマッター [Black](https://github.com/psf/black) を使用しています。Blackは妥協のないコードフォーマッターで、Pythonコードを自動的にBlackのスタイルに整形します。

#### 設定

Blackの設定は `pyproject.toml` に記載されています:

```toml
[tool.black]
line-length = 88
target-version = ['py310']
include = '\.pyi?$'
```

#### Blackのインストール

BlackはPoetry（推奨）またはpipでインストールできます。

##### Poetryを使う場合

開発環境をセットアップすると自動的にBlackがインストールされます:
```bash
poetry install
```

##### pipを使う場合

pipを使う場合は、Blackを直接インストールできます:
```bash
pip install black
```

#### Blackの使い方

##### Poetryの場合

1. プロジェクト内のすべてのPythonファイルを整形:
    ```bash
    poetry run black .
    ```

2. 特定のファイルやディレクトリを整形:
    ```bash
    poetry run black path/to/file_or_directory
    ```

##### pipの場合

1. プロジェクト内のすべてのPythonファイルを整形:
    ```bash
    black .
    ```

2. 特定のファイルやディレクトリを整形:
    ```bash
    black path/to/file_or_directory
    ```

> [!TIP]
> エディターの保存時にBlackで自動整形する設定をおすすめします。多くのエディターで拡張機能やプラグインを通じて対応しています。

## Co-op Translatorの実行

Poetryを使ってCo-op Translatorを実行するには、以下の手順に従ってください。

1. 翻訳テストを行いたいディレクトリに移動するか、テスト用の一時フォルダーを作成します。

2. 以下のコマンドを実行します。`-l ko` は翻訳先の言語コードに置き換えてください。`-d` フラグはデバッグモードを示します。

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> [!NOTE]
> コマンド実行前にPoetry環境（poetry shell）が有効になっていることを確認してください。

## 新しい言語の追加

新しい言語のサポート追加も歓迎しています。PRを作成する前に、以下の手順を完了してください。

1. フォントマッピングへの言語追加
   - `src/co_op_translator/fonts/font_language_mappings.yml` を編集
   - 以下の項目でエントリを追加:
     - `code`: ISO風の言語コード（例: `vi`）
     - `name`: 人が分かりやすい表示名
     - `font`: 対応するスクリプトのフォント（`src/co_op_translator/fonts/` に含まれるもの）
     - `rtl`: 右から左書きの場合は `true`、それ以外は `false`

2. 必要なフォントファイルの追加（必要な場合）
   - 新しいフォントが必要な場合は、オープンソース配布のライセンス互換性を確認
   - フォントファイルを `src/co_op_translator/fonts/` に追加

3. ローカル検証
   - 少量のサンプル（Markdown、画像、ノートブックなど）で翻訳を実行
   - フォントやRTLレイアウトも含め、出力が正しく表示されるか確認

4. ドキュメントの更新
   - 言語が `getting_started/supported-languages.md` に記載されていることを確認
   - `README_languages_template.md` の変更は不要です。これはサポートリストから自動生成されます

5. PRの作成
   - 追加した言語やフォント・ライセンスの考慮事項を説明
   - 可能であれば、レンダリングされた出力のスクリーンショットを添付

YAMLエントリ例:

```yaml
new_lang(code):
  name: "New Language"
  font: "NotoSans-Medium.ttf"
  rtl: false
```


## メンテナー向け

### コミットメッセージとマージ戦略

プロジェクトのコミット履歴の一貫性と明確さを保つため、**Squash and Merge**戦略を使う際の**最終コミットメッセージ**には特定のフォーマットを採用しています。

プルリクエスト（PR）がマージされると、個々のコミットは1つのコミットにまとめられます。最終コミットメッセージは、以下のフォーマットに従ってください。

#### コミットメッセージフォーマット（Squash and Merge用）

コミットメッセージは以下のフォーマットを使います:

```bash
<type>: <description> (#<PR number>)
```

- **type**: コミットのカテゴリを指定します。以下のタイプを使います:
  - `Docs`: ドキュメントの更新
  - `Build`: ビルドシステムや依存関係の変更（設定ファイル、CIワークフロー、Dockerfileなどの更新を含む）
  - `Core`: プロジェクトのコア機能や特徴の修正（特に `src/co_op_translator/core` ディレクトリのファイル）

- **description**: 変更内容の簡潔な要約
- **PR number**: コミットに関連するプルリクエスト番号

**例**:

- `Docs: インストール手順を分かりやすく更新 (#50)`
- `Core: 画像翻訳の処理を改善 (#60)`

> [!NOTE]
> 現在、**`Docs`**、**`Core`**、**`Build`** のプレフィックスは、変更されたソースコードに適用されたラベルに基づきPRタイトルに自動的に追加されます。正しいラベルが適用されていれば、通常はPRタイトルを手動で更新する必要はありません。すべてが正しいか、プレフィックスが適切に生成されているかを確認してください。

#### マージ戦略

プルリクエストには**Squash and Merge**をデフォルト戦略として使用しています。この戦略により、個々のコミットがどのような内容でも、コミットメッセージがフォーマットに従うことが保証されます。

**理由**:

- プロジェクト履歴がクリーンで直線的になる
- コミットメッセージの一貫性
- 細かなコミット（例: "fix typo"）によるノイズの削減

マージ時は、最終コミットメッセージが上記のフォーマットに従っていることを確認してください。

**Squash and Mergeの例**
PRに以下のコミットが含まれている場合:

- `fix typo`
- `update README`
- `adjust formatting`

これらはまとめて次のようにします:
`Docs: ドキュメントの明確化とフォーマット調整 (#65)`

---

**免責事項**：
本書類は、AI翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性には努めておりますが、自動翻訳には誤りや不正確な表現が含まれる場合がありますのでご注意ください。原文（元の言語の文書）が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や誤認についても、当方は責任を負いかねます。