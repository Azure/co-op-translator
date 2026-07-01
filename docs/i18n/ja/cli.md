# CLI リファレンス

Co-op Translator は以下のコマンドラインエントリポイントをインストールします:

- `translate`
- `evaluate`
- `migrate-links`
- `co-op-review`
- `co-op-translator-mcp`

`translate`、`evaluate`、`migrate-links`、および `co-op-review` コマンドは `co_op_translator.__main__` を経由してディスパッチされ、呼び出されたスクリプト名に基づいてコマンド実装を選択します。MCP サーバーは `co_op_translator.mcp.server` を直接使用します。

CLI、Python API、MCP の間で迷っている場合は、まず [ワークフローを選択](workflows.md) を参照してください。

## First-Time CLI Flow

ターミナルから Co-op Translator を使用する場合はここから始めてください:

1. [設定](configuration.md) に記載されているように、LLM プロバイダーを構成します。
2. 翻訳したいコンテンツの種類を選択します。
3. まずは Markdown のみの翻訳など、限定されたコマンドを実行します。
4. 大規模なリポジトリ変更の前に `--dry-run` を使用します。
5. 翻訳後に `co-op-review` を使って構造と最新性を確認します。

| 目的 | 開始に使うコマンド |
| --- | --- |
| Markdown ドキュメントを翻訳する | `translate -l "ko" -md` |
| ノートブックを翻訳する | `translate -l "ko" -nb` |
| 画像のテキストを翻訳する | `translate -l "ko" -img` |
| ファイルを書き込まずに作業をプレビューする | `translate -l "ko" -md --dry-run` |
| 既存の翻訳をレビューする | `co-op-review -l "ko"` |
| ノートブックと Markdown のリンクを更新する | `migrate-links -l "ko" --dry-run` |
| MCP クライアントにツールを公開する | CLI コマンドを直接実行する代わりに [MCP サーバー](mcp.md) を構成します。 |

## translate

Translate Markdown files, notebooks, and image text into one or more target languages.

```bash
translate -l "ko ja fr"
```

### よくある例

Markdown のみを翻訳:

```bash
translate -l "de" -md
```

ノートブックのみを翻訳:

```bash
translate -l "zh-CN" -nb
```

Markdown と画像を翻訳:

```bash
translate -l "pt-BR" -md -img
```

既存の翻訳を削除して再作成して更新:

```bash
translate -l "ko" -u
```

対話型プロンプトなしで実行:

```bash
translate -l "ko ja" -md -y
```

ログを保存:

```bash
translate -l "ko" -s
```

### オプション

| オプション | 必須 | 説明 |
| --- | --- | --- |
| `-l`, `--language-codes` | Yes | スペース区切りの言語コード（例: "es fr de"）、または `"all"`。 |
| `-r`, `--root-dir` | No | プロジェクトのルート。デフォルトはカレントディレクトリです。 |
| `-u`, `--update` | No | 選択した言語の既存の翻訳を削除して再作成します。 |
| `-img`, `--images` | No | 画像ファイルのみを翻訳します。 |
| `-md`, `--markdown` | No | Markdown ファイルのみを翻訳します。 |
| `-nb`, `--notebook` | No | Jupyter ノートブックファイルのみを翻訳します。 |
| `-d`, `--debug` | No | コンソールでデバッグログを有効にします。 |
| `-s`, `--save-logs` | No | DEBUG レベルのログを `<root-dir>/logs/` に保存します。 |
| `-x`, `--fix` | No | 以前の評価結果に基づいて低信頼度の Markdown ファイルを再翻訳します。 |
| `-c`, `--min-confidence` | No | `--fix` のための信頼度閾値。デフォルトは `0.7`。 |
| `--add-disclaimer`, `--no-disclaimer` | No | 機械翻訳の免責事項を追加または抑制します。CLI ではデフォルトで有効です。 |
| `-f`, `--fast` | No | 非推奨の高速画像モードです。 |
| `-y`, `--yes` | No | プロンプトを自動確認します。CIで有用です。 |
| `--repo-url` | No | README の言語テーブルの sparse-checkout アドバイスで使用されるリポジトリ URL。 |
| `--migrate-language-folders` | No | `cn` や `tw` のような旧式のエイリアスフォルダーを正規の BCP 47 フォルダー名にリネームします。 |
| `--dry-run` | No | ファイルを書き込まずに言語フォルダの移行と翻訳見積をプレビューします。 |

タイプフラグが指定されない場合、`translate` は Markdown、ノートブック、画像を処理します。画像翻訳には Azure AI Vision の設定が必要です。

## evaluate

Evaluate translated Markdown quality for one language.

!!! warning "実験的"
    `evaluate` は実験的です。ルールベースおよび LLM ベースの品質チェックを使用することができ、評価結果を翻訳メタデータに書き込みます。スコアリングモデルとメタデータの挙動は変更される可能性があります。

```bash
evaluate -l "ko"
```

### よくある例

厳しめの低信頼度閾値を使用:

```bash
evaluate -l "es" -c 0.8
```

ルールベースのチェックのみ実行:

```bash
evaluate -l "fr" -f
```

LLM ベースのチェックのみ実行:

```bash
evaluate -l "ja" -D
```

### オプション

| オプション | 必須 | 説明 |
| --- | --- | --- |
| `-l`, `--language-code` | Yes | 評価する単一の言語コード。エイリアスコードは正規化されます。 |
| `-r`, `--root-dir` | No | プロジェクトのルート。デフォルトはカレントディレクトリです。 |
| `-c`, `--min-confidence` | No | 低信頼度翻訳を列挙する際に使う閾値。デフォルトは `0.7`。 |
| `-d`, `--debug` | No | デバッグログを有効にします。 |
| `-s`, `--save-logs` | No | DEBUG レベルのログを `<root-dir>/logs/` に保存します。 |
| `-f`, `--fast` | No | ルールベースの評価のみ。 |
| `-D`, `--deep` | No | LLM ベースの評価のみ。 |

デフォルトでは、`evaluate` はルールベースと LLM ベースの評価の両方を使用します。結果は翻訳メタデータに書き込まれ、コンソールに要約されます。

## co-op-review

Run deterministic translation maintenance checks without API credentials.

!!! note "ベータ"
    `co-op-review` はベータの決定論的レビューコマンドです。モデルプロバイダーを呼び出したりファイルを書き込んだりはしませんが、そのチェックや問題出力スキーマは変化する可能性があります。

```bash
co-op-review -l "ko"
```

### よくある例

カレントディレクトリから韓国語と日本語の翻訳をレビューする:

```bash
co-op-review -l "ko ja"
```

特定のプロジェクトルートをレビューする:

```bash
co-op-review -l "fr" -r ./my-course
```

ベースリファレンスと比較して変更されたソースファイルのみをレビューする:

```bash
co-op-review -l "ko" --changed-from origin/main
```

CI 用のサマリーとして GitHub-Flavored Markdown 出力を印刷する:

```bash
co-op-review -l "ko ja" --changed-from origin/main --format github
```

### オプション

| オプション | 必須 | 説明 |
| --- | --- | --- |
| `-l`, `--language-code` | No | レビューする言語コード。複数回渡すか、スペース区切りで指定できます。デフォルトは発見されたすべての翻訳言語です。 |
| `-r`, `--root-dir` | No | プロジェクトのルート。デフォルトはカレントディレクトリです。 |
| `--changed-from` | No | レビューを変更されたソースファイルに限定するのに使用する Git リファレンス。 |
| `--format` | No | 出力フォーマット：`text` または `github`。デフォルトは `text`。 |

`co-op-review` は現在、翻訳済みファイルの欠落、翻訳メタデータの欠落または陳腐化、Markdown の frontmatter とコードフェンスの整合性、無効な翻訳済みノートブックの JSON、ローカルの Markdown または画像リンクターゲットの欠落をチェックします。リンクの欠落はデフォルトで警告とみなされます。構造や最新性の問題はコマンドの失敗となります。

## co-op-translator-mcp

Run the Co-op Translator MCP server for agents, editors, and MCP-compatible clients.

```bash
co-op-translator-mcp
```

デフォルトのトランスポートは `stdio` です。クライアントの構成、ツール、リソース、安全上の注意については [MCP サーバー](mcp.md) ガイドを参照してください。

### オプション

| オプション | 必須 | 説明 |
| --- | --- | --- |
| `--transport` | No | MCP トランスポート：`stdio`、`streamable-http`、または `sse`。デフォルトは `stdio`。 |

## migrate-links

Reprocess translated Markdown files and update notebook links so they point to translated notebooks when available.

```bash
migrate-links -l "ko ja"
```

### よくある例

リンク更新をプレビュー:

```bash
migrate-links -l "ko" --dry-run
```

すべての対応言語を確認なしで処理する:

```bash
migrate-links -l "all" -y
```

翻訳済みノートブックが存在する場合にのみリンクを書き換える:

```bash
migrate-links -l "ko" --no-fallback-to-original
```

### オプション

| オプション | 必須 | 説明 |
| --- | --- | --- |
| `-l`, `--language-codes` | Yes | スペース区切りの言語コード、または `"all"`。 |
| `-r`, `--root-dir` | No | プロジェクトのルート。デフォルトはカレントディレクトリです。 |
| `--image-dir` | No | ルートからの相対パスでの翻訳済み画像ディレクトリ。デフォルトは `translated_images`。 |
| `--dry-run` | No | 変更されるファイルを表示し、更新を書き込まない。 |
| `--fallback-to-original`, `--no-fallback-to-original` | No | 翻訳済みノートブックがない場合に元のノートブックリンクを使用します。デフォルトで有効です。 |
| `-d`, `--debug` | No | デバッグログを有効にします。 |
| `-s`, `--save-logs` | No | DEBUG レベルのログを `<root-dir>/logs/` に保存します。 |
| `-y`, `--yes` | No | すべての言語を処理する際にプロンプトを自動確認します。 |

## Environment

All commands require one configured LLM provider:

```bash
# Azure の OpenAI
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"

# または OpenAI
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

Image translation additionally requires Azure AI Vision:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

## Output layout

Text translations are written under:

```text
translations/<language-code>/<original-path>
```

Translated image output is written under:

```text
translated_images/<language-code>/<original-path>
```

For example, translating `README.md` and `docs/setup.md` into Korean produces:

```text
translations/ko/README.md
translations/ko/docs/setup.md
```

## コピー＆ペースト用 CLI 例

Markdown を3つの言語に翻訳する:

```bash
translate -l "ko ja fr" -md
```

ノートブックのみを翻訳する:

```bash
translate -l "zh-CN" -nb
```

画像のみを翻訳する:

```bash
translate -l "pt-BR" -img
```

ファイルを書き込まずに Markdown 翻訳をプレビューする:

```bash
translate -l "de es" -md --dry-run
```

低信頼度の Markdown 翻訳を修復する:

```bash
evaluate -l "ko" -c 0.8
translate -l "ko" --fix -c 0.8 -md
```

CI 対応の Markdown 翻訳を実行する:

```bash
translate -l "ko ja" -md -y -s
```

翻訳結果をレビューする:

```bash
co-op-review -l "ko ja"
```

リンク移行をプレビューする:

```bash
migrate-links -l "ko" --dry-run
```