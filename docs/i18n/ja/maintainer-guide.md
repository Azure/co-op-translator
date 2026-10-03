# メンテナ向けガイド

このページは、API、CLI、およびドキュメントサイトがどのように連携しているかを要約しています。

## 公開APIの境界

安定した Python API は次の場所からエクスポートされています:

```python
co_op_translator.api
```

公開APIは、コンテンツ翻訳ヘルパー、パス書き換えヘルパー、プロジェクトオーケストレーション、およびレビューに分類されています:

```python
from co_op_translator.api import (
    ImageTranslationOptions,
    MarkdownTranslationOptions,
    NotebookTranslationOptions,
    TranslationBaseline,
    TranslationStateProvider,
    TranslationUpdate,
    run_review,
    run_translation,
    rewrite_markdown_paths,
    rewrite_notebook_paths,
    translate_image_content,
    translate_markdown_content,
    translate_notebook_content,
    translate_project,
)
```

`TranslationStateProvider` はホスト統合の永続化境界です。
生成された候補を受け入れられたベースラインから分離して保持する必要があり、
未マージの翻訳が事実上の単一の情報源にならないようにします。

新しい公開APIを追加する場合は、次を更新してください:

- `src/co_op_translator/api/__init__.py`
- `docs/api.md`
- `tests/co_op_translator/` 以下の関連する API テスト（例: `test_api.py` や `test_review_api.py`）

プロジェクトがそれらを直接サポートする意図がない限り、低レベルの `core` モジュールを安定した API として文書化することは避けてください。

## CLI エントリポイント

パッケージは次の Poetry スクリプトを定義しています:

```toml
[tool.poetry.scripts]
translate = "co_op_translator.__main__:main"
evaluate = "co_op_translator.__main__:main"
migrate-links = "co_op_translator.__main__:main"
co-op-review = "co_op_translator.__main__:main"
co-op-translator-mcp = "co_op_translator.mcp.server:main"
```

`src/co_op_translator/__main__.py` はスクリプト名でディスパッチします:

- `translate` は `co_op_translator.cli.translate.translate_command` を呼び出します
- `evaluate` は `co_op_translator.cli.evaluate.evaluate_command` を呼び出します
- `migrate-links` は `co_op_translator.cli.migrate_links.migrate_links_command` を呼び出します
- `co-op-review` は `co_op_translator.cli.review.review_command` を呼び出します

`co-op-translator-mcp` は `__main__.py` をバイパスし、`co_op_translator.mcp.server:main` を直接呼び出します。

CLI オプションを追加または変更する場合は、次を更新してください:

- 該当する `src/co_op_translator/cli/*.py` コマンド
- `docs/cli.md`
- 振る舞いが変更される場合の CLI 関連テスト

## MCP サーバー

MCP サーバーは次で実装されています:

```python
co_op_translator.mcp.server
```

サーバーは意図的に低レベルの `core` モジュールを呼び出すのではなく、公開 Python API をラップしています。この境界を維持して、MCP クライアント、Python 呼び出し元、および CLI が同じ動作を共有するようにしてください。

MCP ツールを追加または変更する場合は、次を更新してください:

- `src/co_op_translator/mcp/server.py`
- `tests/co_op_translator/test_mcp_server.py`
- `docs/mcp.md`
- `docs/api.md`（公開 API のインターフェースが変更される場合）

リポジトリの翻訳ツールは MCP 経由でモデルから呼び出し可能であり、多くのファイルを書き込むことがあります。デフォルトは `dry_run=True` にしておき、dry-run でないプロジェクト翻訳の前に `confirm_write=True` を要求してください。

## 翻訳フロー

高レベルのプロジェクト翻訳フローは次のとおりです:

1. CLI 引数または API パラメーターを解析します。
2. `LLMConfig` で LLM 設定を検証します。
3. 画像翻訳が選択されている場合は Azure AI Vision を検証します。
4. 言語コードを正規化します。
5. レガシーな言語フォルダーのエイリアスを検出します。
6. 翻訳量を見積もります。
7. 該当する場合は README の言語／コースセクションを更新します。
8. プロジェクト翻訳を `ProjectTranslator` に委譲します。
9. `ProjectTranslator` はファイル処理を `TranslationManager` に委譲します。

`TranslationManager` はファイル種別に特化したミックスインから構成されています:

- `ProjectMarkdownTranslationMixin` は Markdown ファイルの読み取り、コンテンツ翻訳、パス書き換え、メタデータ、免責事項、および書き込みを処理します。
- `ProjectNotebookTranslationMixin` はノートブックファイルの読み取り、Markdown セルの翻訳、パス書き換え、メタデータ、免責事項、および書き込みを処理します。
- `ProjectImageTranslationMixin` は画像の検出、テキスト抽出/翻訳、レンダリング済み画像の書き込み、およびメタデータを処理します。

低レベルのコンテンツ API はプロジェクトワークフローをスキップします:

1. `translate_markdown_content` と `translate_notebook_content` はメモリ内コンテンツのみを翻訳します。
2. `translate_image_content` は単一画像のテキストを翻訳し、レンダリング済み画像オブジェクトを返します。
3. `rewrite_markdown_paths` と `rewrite_notebook_paths` は明示的な事後処理ヘルパーです。翻訳を行わず、プロジェクトへの書き込みもしません。

## レビューフロー

決定論的なレビューフローは次のとおりです:

1. CLI 引数または API パラメーターを解析します。
2. 要求された言語コードを正規化します。
3. `root_dir`、`root_dirs`、または `groups` から1つ以上のレビューターゲットを構築します。
4. 必要に応じて `--changed-from` でソースファイルを限定します。
5. 構造、翻訳の新鮮さ、Markdown の整合性、およびローカルなリンク/画像パスに対する決定論的チェックを実行します。
6. テキスト出力または GitHub 形式の Markdown のいずれかを出力します。
7. レビューエラーが見つかった場合は失敗で終了します。

レビューフローは API キーを必要とせず、ローカルチェックやオプトインの利用者 CI で利用可能です。本リポジトリはすべてのプルリクエストで `co-op-review` を自動実行しません。

## ドキュメントサイト

ドキュメントサイトは次で構成されています:

```text
mkdocs.yml
requirements-docs.txt
docs/
```

`docs/` ディレクトリが正式なドキュメントソースです。プロジェクトが別の公開ドキュメント面を意図的に導入しない限り、このディレクトリの外に新しいエンドユーザー向けガイドを追加しないでください。

ローカルでビルドするには:

```bash
python -m pip install -r requirements-docs.txt
python -m mkdocs build --strict
```

ローカルでプレビューするには:

```bash
python -m mkdocs serve
```

生成されたサイトは `site/` に書き込まれ、git に無視されています。

## GitHub Pages ワークフロー

`.github/workflows/docs.yml` はプルリクエストでサイトをビルドし、`main` へのプッシュでデプロイします。

ワークフローは次をインストールします:

```bash
pip install -r requirements-docs.txt
```

docs ワークフローはドキュメント用のツールチェーンのみをインストールします。`mkdocs.yml` は `mkdocstrings` を `src/` に向けているため、ランタイムの完全な依存関係セットをインストールせずにソースツリーから公開 API ページをレンダリングできます。将来 API ドキュメントがビルド中にオプションのランタイムプロバイダーのインポートを必要とする場合は、`.github/workflows/docs.yml` と本ガイドの両方を更新してください。

## ドキュメント品質基準

ドキュメント変更をマージする前に、次を実行してください:

```bash
python -m mkdocs build --strict
git diff --check
```

厳格なビルドを使用して、壊れたリンク、無効なナビゲーションエントリ、および API レンダリングの問題が早期に失敗するようにしてください。