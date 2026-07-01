# メンテナ向けガイド

このページは、API、CLI、およびドキュメントサイトがどのように連携しているかをまとめたものです。

## 公開 API の境界

安定した Python API は次からエクスポートされます:

```python
co_op_translator.api
```

公開 API は、コンテンツ翻訳ヘルパー、パス書き換えヘルパー、プロジェクトオーケストレーション、およびレビューに整理されています:

```python
from co_op_translator.api import (
    ImageTranslationOptions,
    MarkdownTranslationOptions,
    NotebookTranslationOptions,
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

新しいパブリック API を追加する場合は、次を更新してください:

- `src/co_op_translator/api/__init__.py`
- `docs/api.md`
- 関連する API テスト（`tests/co_op_translator/` 以下）、例: `test_api.py` または `test_review_api.py`

プロジェクトが直接サポートするつもりがない限り、低レベルの `core` モジュールを安定した API として文書化することは避けてください。

## CLI エントリポイント

パッケージはこれらの Poetry スクリプトを定義しています:

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
- 動作が変わる場合は CLI 関連のテスト

## MCP server

MCP サーバーは次で実装されています:

```python
co_op_translator.mcp.server
```

サーバーは意図的に低レベルの `core` モジュールを呼び出すのではなく、公開された Python API をラップしています。この境界を保持して、MCP クライアント、Python 呼び出し元、および CLI が同じ動作を共有するようにしてください。

MCP ツールを追加または変更する場合は、次を更新してください:

- `src/co_op_translator/mcp/server.py`
- `tests/co_op_translator/test_mcp_server.py`
- `docs/mcp.md`
- 公開 API の表面が変わる場合は `docs/api.md`

リポジトリ翻訳ツールは MCP を通じてモデル呼び出し可能で、多数のファイルを書き込むことができます。既定では `dry_run=True` を維持し、非ドライランのプロジェクト翻訳を行う前に `confirm_write=True` を必須にしてください。

## 翻訳フロー

高レベルなプロジェクト翻訳フローは以下です:

1. CLI 引数または API パラメーターを解析する。
2. `LLMConfig` で LLM 構成を検証する。
3. 画像翻訳が選択された場合は Azure AI Vision を検証する。
4. 言語コードを正規化する。
5. レガシー言語フォルダの別名を検出する。
6. 翻訳量を見積もる。
7. 該当する場合は README の language/course セクションを更新する。
8. プロジェクト翻訳を `ProjectTranslator` に委譲する。
9. `ProjectTranslator` はファイル処理を `TranslationManager` に委譲する。

`TranslationManager` はフォーカスされたファイルタイプミキシンで構成されています:

- `ProjectMarkdownTranslationMixin` は Markdown ファイルの読み取り、コンテンツ翻訳、パス書き換え、メタデータ、免責事項、および書き込みを処理します。
- `ProjectNotebookTranslationMixin` はノートブックファイルの読み取り、Markdown セルの翻訳、パス書き換え、メタデータ、免責事項、および書き込みを処理します。
- `ProjectImageTranslationMixin` は画像の検出、テキスト抽出/翻訳、レンダリングされた画像の書き込み、およびメタデータを処理します。

低レベルのコンテンツ API はプロジェクトワークフローをスキップします:

1. `translate_markdown_content` と `translate_notebook_content` はメモリ内のコンテンツのみを翻訳します。
2. `translate_image_content` は単一の画像内のテキストを翻訳し、レンダリングされた画像オブジェクトを返します。
3. `rewrite_markdown_paths` と `rewrite_notebook_paths` は明示的な事後処理ヘルパーです。これらは翻訳もプロジェクト書き込みも行いません。

## レビューフロー

決定論的なレビューフローは以下です:

1. CLI 引数または API パラメーターを解析する。
2. 要求された言語コードを正規化する。
3. `root_dir`、`root_dirs`、または `groups` から1つ以上のレビューターゲットを構築する。
4. 必要に応じて `--changed-from` でソースファイルを制限する。
5. 構造、翻訳の鮮度、Markdown の整合性、ローカルなリンク/画像パスの決定論的チェックを実行する。
6. テキスト出力または GitHub-flavored Markdown のいずれかを出力する。
7. レビューエラーが見つかった場合は失敗で終了する。

レビューフローは API キーを必要とせず、プルリクエスト CI に適したままであるべきです。プルリクエストワークフローは毎回チェックサマリーを書き込み、`co-op-review` が失敗した場合にのみ PR コメントを投稿します。

## ドキュメントサイト

ドキュメントサイトは次で構成されています:

```text
mkdocs.yml
requirements-docs.txt
docs/
```

`docs/` ディレクトリは公式のドキュメントソースです。このディレクトリの外に新しいエンドユーザー向けガイドを追加しないでください。プロジェクトが別の公開ドキュメント面を意図的に導入する場合を除きます。

ローカルでビルドするには:

```bash
python -m pip install -r requirements-docs.txt
python -m mkdocs build --strict
```

ローカルでプレビューするには:

```bash
python -m mkdocs serve
```

生成されたサイトは `site/` に書き出され、これは git に無視されています。

## GitHub Pages ワークフロー

`.github/workflows/docs.yml` はプルリクエストでサイトをビルドし、`main` へのプッシュでデプロイします。

ワークフローは次をインストールします:

```bash
pip install -r requirements-docs.txt
```

ドキュメントワークフローはドキュメンテーション用のツールチェーンのみをインストールします。`mkdocs.yml` は `mkdocstrings` を `src/` に向けているため、公開 API ページはフルのランタイム依存関係をインストールせずにソースツリーからレンダリングできます。将来の API ドキュメントがビルド中にオプションのランタイムプロバイダーのインポートを必要とする場合は、`.github/workflows/docs.yml` とこのガイドの両方を更新してください。

## ドキュメント品質基準

ドキュメントの変更をマージする前に、次を実行してください:

```bash
python -m mkdocs build --strict
git diff --check
```

壊れたリンク、無効なナビゲーションエントリ、および API レンダリングの問題が早期に失敗するように、厳密なビルドを使用してください。