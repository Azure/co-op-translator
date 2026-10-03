# CLI リファレンス

Co-op Translator は次のコマンドラインエントリポイントをインストールします:

- `translate`
- `evaluate`
- `migrate-links`
- `co-op-review`
- `co-op-translator-mcp`

`translate`、`evaluate`、`migrate-links`、および `co-op-review` コマンドは `co_op_translator.__main__` を経由してディスパッチされ、起動されたスクリプト名に基づいてコマンド実装を選択します。MCP サーバーは `co_op_translator.mcp.server` を直接使用します。

CLI、Python API、MCP のどれを選ぶか迷っている場合は、[ワークフローの選択](workflows.md) から始めてください。

## コンソール出力

対話型ターミナルはコマンドヘッダー、進行状況、サマリに Rich フォーマットを使用します。CI や非対話的な出力は自動的にプレーンテキストにフォールバックします。

プレーン出力を強制するには `CO_OP_TRANSLATOR_OUTPUT_STYLE=plain` を設定し、Rich 出力を強制するには `CO_OP_TRANSLATOR_OUTPUT_STYLE=rich` を設定します。ライブのプログレスバーを抑制しつつサマリを保持するには `CO_OP_TRANSLATOR_NO_PROGRESS=1` を設定してください。

別のシステムが機械可読の進行状況を必要とする場合は、`translate --json-events progress.ndjson` を使用してください。
CLI は引き続き人間向けの出力をレンダリングし、
NDJSON ファイルにはバージョン付きの `co-op.translation.event.v1` イベントが記録され、
`type`、`stage_key`、`completed`、`total` といった安定したフィールドや
`current_path` が含まれます。

## 初めての CLI フロー

ターミナルから Co-op Translator を使用する場合はここから始めてください:

1. [構成](configuration.md) に記載のとおり、LLM プロバイダーを設定します。
2. 翻訳するコンテンツの種類を選択します。
3. まずは Markdown のみの翻訳など、対象を絞ったコマンドを実行します。
4. 大規模なリポジトリ変更の前には `--dry-run` を使用してください。
5. 翻訳後は `co-op-review` を使って構造や鮮度をチェックしてください。

| 目的 | 開始に使うコマンド |
| --- | --- |
| Markdown 文書を翻訳する | `translate -l "ko" -md` |
| ノートブックを翻訳する | `translate -l "ko" -nb` |
| 画像内テキストを翻訳する | `translate -l "ko" -img` |
| ファイルを書き込まずに作業をプレビューする | `translate -l "ko" -md --dry-run` |
| 既存の翻訳をレビューする | `co-op-review -l "ko"` |
| ノートブックとMarkdownのリンクを更新する | `migrate-links -l "ko" --dry-run` |
| ツールをMCPクライアントに公開する | CLI コマンドを直接実行する代わりに [MCP サーバー](mcp.md) を設定します。 |

## translate

Markdown ファイル、ノートブック、画像内テキストを1つ以上のターゲット言語に翻訳します。

```bash
translate -l "ko ja fr"
```

### よくある例

Markdown のみを翻訳する:

```bash
translate -l "de" -md
```

ノートブックのみを翻訳する:

```bash
translate -l "zh-CN" -nb
```

Markdown と画像を翻訳する:

```bash
translate -l "pt-BR" -md -img
```

既存の翻訳を削除して再作成して更新する:

```bash
translate -l "ko" -u
```

対話プロンプトなしで実行する:

```bash
translate -l "ko ja" -md -y
```

ログを保存する:

```bash
translate -l "ko" -s
```

構造化された進行イベントを書き出す:

```bash
translate -l "ko ja" -md --json-events progress.ndjson
```

### オプション

| オプション | 必須 | 説明 |
| --- | --- | --- |
| `-l`, `--language-codes` | はい | スペース区切りの言語コード（例: "es fr de"）、または "all"。 |
| `-r`, `--root-dir` | いいえ | プロジェクトのルート。デフォルトは現在のディレクトリです。 |
| `-u`, `--update` | いいえ | 選択した言語の既存の翻訳を削除して再作成します。 |
| `-img`, `--images` | いいえ | 画像ファイルのみを翻訳します。 |
| `-md`, `--markdown` | いいえ | Markdown ファイルのみを翻訳します。 |
| `-nb`, `--notebook` | いいえ | Jupyter ノートブックファイルのみを翻訳します。 |
| `-d`, `--debug` | いいえ | コンソールでデバッグログを有効にします。 |
| `-s`, `--save-logs` | いいえ | DEBUG レベルのログを `<root-dir>/logs/` に保存します。 |
| `--json-events` | いいえ | 翻訳進行イベントを NDJSON として機械可読で書き出します。 |
| `-x`, `--fix` | いいえ | 以前の評価結果に基づいて低信頼度の Markdown ファイルを再翻訳します。 |
| `-c`, `--min-confidence` | いいえ | `--fix` に使用する信頼度しきい値。デフォルトは `0.7` です。 |
| `--add-disclaimer`, `--no-disclaimer` | いいえ | 機械翻訳の免責事項を追加または抑制します。CLI ではデフォルトで有効です。 |
| `-f`, `--fast` | いいえ | 廃止予定の高速画像モード。 |
| `-y`, `--yes` | いいえ | プロンプトを自動確認します。CI で便利です。 |
| `--repo-url` | いいえ | README の言語テーブルの sparse-checkout アドバイスで使用するリポジトリ URL。 |
| `--migrate-language-folders` | いいえ | `cn` や `tw` のような旧エイリアスフォルダを正規の BCP 47 フォルダ名にリネームします。 |
| `--dry-run` | いいえ | ファイルを書き込まずに言語フォルダの移行と翻訳見積もりをプレビューします。 |

タイプフラグが指定されない場合、`translate` は Markdown、ノートブック、画像を処理します。画像翻訳には Azure AI Vision の設定が必要です。

## evaluate

1 言語の翻訳された Markdown の品質を評価します。

!!! warning "実験的"
    `evaluate` は実験的です。ルールベースおよび LLM ベースの品質チェックを使用することがあり、評価結果を翻訳メタデータに書き込みます。スコアリングモデルやメタデータの挙動は変更される可能性があります。

```bash
evaluate -l "ko"
```

### よくある例

より厳しい低信頼度のしきい値を使用する:

```bash
evaluate -l "es" -c 0.8
```

ルールベースのチェックのみを実行する:

```bash
evaluate -l "fr" -f
```

LLM ベースのチェックのみを実行する:

```bash
evaluate -l "ja" -D
```

### オプション

| オプション | 必須 | 説明 |
| --- | --- | --- |
| `-l`, `--language-code` | はい | 評価する単一の言語コード。エイリアスコードは正規化されます。 |
| `-r`, `--root-dir` | いいえ | プロジェクトのルート。デフォルトは現在のディレクトリです。 |
| `-c`, `--min-confidence` | いいえ | 低信頼度の翻訳を一覧表示する際に使用するしきい値。デフォルトは `0.7` です。 |
| `-d`, `--debug` | いいえ | デバッグログを有効にします。 |
| `-s`, `--save-logs` | いいえ | DEBUG レベルのログを `<root-dir>/logs/` に保存します。 |
| `-f`, `--fast` | いいえ | ルールベース評価のみ。 |
| `-D`, `--deep` | いいえ | LLM ベースの評価のみ。 |

デフォルトでは、`evaluate` はルールベースと LLM ベースの両方の評価を使用します。結果は翻訳メタデータに書き込まれ、コンソールに要約が表示されます。

## co-op-review

API 資格情報なしで決定論的な翻訳メンテナンスチェックを実行します。

!!! note "ベータ"
    `co-op-review` はベータの決定論的レビューコマンドです。モデルプロバイダーを呼び出したりファイルを書き込んだりすることはありませんが、チェックや問題出力のスキーマは変更される可能性があります。

```bash
co-op-review -l "ko"
```

### よくある例

現在のディレクトリから韓国語と日本語の翻訳をレビューする:

```bash
co-op-review -l "ko ja"
```

特定のプロジェクトルートをレビューする:

```bash
co-op-review -l "fr" -r ./my-course
```

README のみの翻訳後に README のみをレビューする:

```bash
translate -l "ko" --readme-only -y
co-op-review -l "ko" --readme-only --format github
```

`--readme-only` は他のドキュメントやネストされた README を無視します。
ルートの `README.md` が存在しない場合は失敗します。
`--changed-from` と組み合わせると、そのソースファイルが変更された場合に README のみをレビューします。
README のみの翻訳では、共有セクションマーカーを含め、ソース README は変更されません。

ベースリファレンスに対して変更されたソースファイルのみをレビューする:

```bash
co-op-review -l "ko" --changed-from origin/main
```

CI 用サマリのために GitHub 互換の Markdown 出力を生成する:

```bash
co-op-review -l "ko ja" --changed-from origin/main --format github
```

### オプション

| オプション | 必須 | 説明 |
| --- | --- | --- |
| `-l`, `--language-code` | いいえ | レビューする言語コード。複数回指定するか、スペース区切りで渡せます。デフォルトは発見された全ての翻訳言語です。 |
| `-r`, `--root-dir` | いいえ | プロジェクトのルート。デフォルトは現在のディレクトリです。 |
| `--changed-from` | いいえ | レビューを変更されたソースファイルに限定するために使用する Git リファレンス。 |
| `--readme-only` | いいえ | ルートの `README.md` 翻訳のみをレビューします。 |
| `--format` | いいえ | 出力形式: `text` または `github`。デフォルトは `text` です。 |

`co-op-review` は現在、翻訳済みファイルの欠如、翻訳メタデータの欠落や陳腐化、Markdown のフロントマターやコードフェンスの整合性、無効な翻訳済みノートブックの JSON、ローカルの Markdown や画像リンクターゲットの欠如をチェックします。リンクの欠落はデフォルトで警告ですが、構造上の問題や鮮度に関する問題はコマンドを失敗させます。

## co-op-translator-mcp

エージェント、エディタ、および MCP 互換クライアント向けに Co-op Translator MCP サーバーを実行します。

```bash
co-op-translator-mcp
```

デフォルトのトランスポートは `stdio` です。クライアント構成、ツール、リソース、および安全に関する注意点については [MCP サーバー](mcp.md) ガイドを参照してください。

### オプション

| オプション | 必須 | 説明 |
| --- | --- | --- |
| `--transport` | いいえ | MCP トランスポート: `stdio`, `streamable-http`, または `sse`。デフォルトは `stdio`。 |

## migrate-links

翻訳済みの Markdown ファイルを再処理し、翻訳済みノートブックが利用可能な場合にノートブックリンクを翻訳版に更新します。

```bash
migrate-links -l "ko ja"
```

### よくある例

リンク更新をプレビューする:

```bash
migrate-links -l "ko" --dry-run
```

確認なしでサポートされている全言語を処理する:

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
| `-l`, `--language-codes` | はい | スペース区切りの言語コード、または "all"。 |
| `-r`, `--root-dir` | いいえ | プロジェクトのルート。デフォルトは現在のディレクトリです。 |
| `--image-dir` | いいえ | ルートからの相対の翻訳済み画像ディレクトリ。デフォルトは `translated_images`。 |
| `--dry-run` | いいえ | 変更されるファイルを表示し、更新を書き込まないようにします。 |
| `--fallback-to-original`, `--no-fallback-to-original` | いいえ | 翻訳済みノートブックがない場合に元のノートブックリンクを使用します。デフォルトで有効です。 |
| `-d`, `--debug` | いいえ | デバッグログを有効にします。 |
| `-s`, `--save-logs` | いいえ | DEBUG レベルのログを `<root-dir>/logs/` に保存します。 |
| `-y`, `--yes` | いいえ | 全言語を処理する際のプロンプトを自動確認します。 |

## 環境

コマンドがプロバイダの資格情報を必要とする場合は、次のいずれかのプロバイダセットを構成してください。`translate --dry-run` と `co-op-review` はプロバイダ資格情報を必要としません:

```bash
# Azure OpenAI
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"

# または OpenAI
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"

# または Anthropic
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

画像翻訳にはさらに Azure AI Vision が必要です:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

## 出力レイアウト

テキスト翻訳は次の場所に書き込まれます:

```text
translations/<language-code>/<original-path>
```

翻訳された画像の出力は次の場所に書き込まれます:

```text
translated_images/<language-code>/<original-path>
```

例えば、`README.md` と `docs/setup.md` を韓国語に翻訳すると次のようになります:

```text
translations/ko/README.md
translations/ko/docs/setup.md
```

## コピペ用 CLI 例

Markdown を 3 つの言語に翻訳する:

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

CI に適した Markdown 翻訳を実行する:

```bash
translate -l "ko ja" -md -y -s
```

翻訳された出力をレビューする:

```bash
co-op-review -l "ko ja"
```

リンク移行をプレビューする:

```bash
migrate-links -l "ko" --dry-run
```