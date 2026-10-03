# MCP サーバー

Co-op Translator には、エージェント、エディタ、および MCP 互換クライアント向けの Model Context Protocol サーバーが含まれています。

デフォルトのローカル設定では、ユーザーが別途サーバーを手動で起動し続ける必要はありません。MCP クライアントを設定すると、必要に応じてクライアントが `co-op-translator-mcp` を `stdio` 経由で自動的に起動します。

もし CLI、Python API、MCP のどれを使うか迷っている場合は、まず [ワークフローを選択](workflows.md) をご覧ください。

エージェントやエディタが Co-op Translator を直接呼び出す必要がある場合は MCP を使用します:

| User goal | MCP tools |
| --- | --- |
| 単一の Markdown ドキュメント、ノートブック、または画像を翻訳する | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content` |
| ホストエージェントモデルで Markdown またはノートブックの内容を翻訳する | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| 出力パスを選択した後に翻訳済みの Markdown またはノートブックのリンクを書き換える | `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| CLI のようにリポジトリ全体を翻訳する | `run_translation`, `translate_project` |
| LLM の資格情報なしで翻訳結果をレビューする | `run_review` |
| 機能と環境の状態を確認する | `get_api_overview`, `list_supported_languages`, `get_configuration_status` |

MCP サーバーは [Python API](api.md) に記載されている同じ公開 Python API をラップします。プロバイダ対応のツールは CLI および Python API と同じ構成済みプロバイダを使用します。エージェント支援ツールは MCP ホストエージェントが翻訳するためのチャンクを準備し、その後 Co-op Translator を使って最終的な Markdown またはノートブックを再構築します。

## ステップ 1: Co-op Translator のインストールと構成

MCP クライアントが使用する Python 環境に Co-op Translator をインストールします:

```bash
pip install co-op-translator
```

このリポジトリからローカル開発を行う場合は、パッケージを編集可能モードでインストールしてください:

```bash
pip install -e .
```

MCP クライアントが使用する翻訳モードを選択します:

| Mode | Use this for | Credentials |
| --- | --- | --- |
| プロバイダ対応 | Co-op Translator が `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, または `run_translation` を呼び出します。 | 翻訳には Azure OpenAI、OpenAI、または Anthropic が必要です。画像翻訳は追加で Azure AI Vision が必要です。 |
| エージェント支援 | MCP ホストエージェントが `start_markdown_agent_translation` や `start_notebook_agent_translation` によって返されるチャンクを翻訳します。 | Markdown やノートブックのチャンクには Co-op Translator の LLM プロバイダ資格情報は不要です。画像翻訳はまだエージェント支援モードの対象外です。 |

Codex や Claude Code のようなエージェント内で Markdown やノートブックの翻訳を開始する場合は、エージェント支援モードから始めてください。Co-op Translator 自体に構成済みプロバイダを呼び出させたい場合、画像を翻訳する場合、または CLI のようなリポジトリレベルの翻訳を実行する場合は、プロバイダ対応モードを使用してください。

プロバイダ対応のワークフローにはプロバイダを一つ設定します:

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

プロバイダ対応の画像翻訳には、さらに次が必要です:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

!!! note
    エージェント支援モードは現在 Markdown およびノートブックの Markdown セルを対象としています。画像翻訳は引き続きプロバイダ対応の画像パイプラインを使用し、OCR とレイアウト対応のレンダリングには Azure AI Vision が必要です。

## ステップ 2: MCP クライアントの構成

通常のローカル `stdio` 設定では、Co-op Translator を MCP クライアントの構成に追加します。クライアントがプロセスを自動的に起動および停止します。

インストール済みパッケージの構成:

```json
{
  "mcpServers": {
    "co-op-translator": {
      "command": "co-op-translator-mcp",
      "args": []
    }
  }
}
```

ソースチェックアウトの構成（Windows）:

```json
{
  "mcpServers": {
    "co-op-translator": {
      "command": "C:\\Users\\you\\dev\\co-op-translator\\.venv\\Scripts\\python.exe",
      "args": ["-m", "co_op_translator.mcp.server"],
      "cwd": "C:\\Users\\you\\dev\\co-op-translator"
    }
  }
}
```

ソースチェックアウトの構成（macOS または Linux）:

```json
{
  "mcpServers": {
    "co-op-translator": {
      "command": "/Users/you/dev/co-op-translator/.venv/bin/python",
      "args": ["-m", "co_op_translator.mcp.server"],
      "cwd": "/Users/you/dev/co-op-translator"
    }
  }
}
```

MCP クライアントの構成を変更したら、クライアントを再起動またはリロードして新しいサーバーを検出できるようにしてください。

## ステップ 3: クライアントでサーバーを確認する

MCP クライアントに利用可能なツールの一覧を要求するか、まず読み取り専用のヘルパーのいずれかを呼び出してください:

```json
{
  "tool": "get_api_overview",
  "arguments": {}
}
```

初期に行うと有用なチェック:

| Tool | What to check |
| --- | --- |
| `get_api_overview` | サーバーに到達できることを確認し、利用可能なワークフローを表示します。 |
| `list_supported_languages` | パッケージ化された言語データが読み込めることを確認します。 |
| `get_configuration_status` | シークレット値を公開することなく、LLM と Vision プロバイダの利用可能性を確認します。 |

## ステップ 4: ワークフローを選ぶ

### 個別ファイルまたはドキュメントの翻訳

MCP クライアントに既にドキュメントの内容や画像パスがあり、Co-op Translator が構成済みの翻訳プロバイダを呼び出すべき場合は、プロバイダ対応のコンテンツツールを使用します。

Markdown の場合:

1. `document`、`language_code`、必要に応じて `source_path` を指定して `translate_markdown_content` を呼び出します。
2. 翻訳結果が Co-op Translator の出力レイアウトに書き込まれる場合は、`rewrite_markdown_paths` を呼び出します。
3. クライアントに最終的な `content` を書き込むか返却させます。

ノートブックの場合:

1. ノートブックの JSON と `language_code` を指定して `translate_notebook_content` を呼び出します。
2. 翻訳済みノートブックのリンクをターゲットパスに合わせて調整する必要がある場合は、`rewrite_notebook_paths` を呼び出します。
3. 最終的なノートブックの JSON を書き込むか返却します。

画像の場合:

1. `image_path`、`language_code`、および任意の `root_dir` または `fast_mode` を指定して `translate_image_content` を呼び出します。
2. 返された `data_base64` と `mime_type` を読み取ります。
3. `output_path` が指定されている場合、翻訳された画像もそのパスに保存されます。

コンテンツツールはプロジェクト検出、メタデータ更新、免責事項の追加、または自動的なパス書き換えを行いません。Co-op Translator の LLM プロバイダ資格情報なしでホストエージェントに Markdown やノートブックのチャンクを翻訳させたい場合は、以下のエージェント支援ワークフローを使用してください。

### ホストエージェントモデルで翻訳する

Co-op Translator のために LLM プロバイダを構成する代わりに、コーディングアシスタントのような MCP ホストエージェントに翻訳テキストを生成させたい場合は、エージェント支援ツールを使用します。

チャットベースの MCP クライアントでは、通常ツールの JSON を自分で書く必要はありません。エージェントにエージェント支援ワークフローを使うよう依頼してください:

```text
Translate this Markdown file to Korean with Co-op Translator MCP.
Use agent-assisted mode: call start_markdown_agent_translation, translate the returned chunks with your own model, then call finish_markdown_agent_translation.
Keep Markdown formatting, code blocks, and links intact.
```

ノートブックでも同じパターンを使用します:

```text
Translate this notebook to Korean with Co-op Translator MCP.
Use start_notebook_agent_translation, translate the returned Markdown-cell chunks with your own model, then call finish_notebook_agent_translation.
Preserve code cells, outputs, and notebook metadata.
```

MCP クライアントがサーバープロンプトをサポートしている場合は、`agent_assisted_markdown_translation_prompt` を使用してクライアントに同じワークフロー指示を読み込ませます。

Markdown の場合:

1. `document`、`language_code`、および必要に応じて `source_path` を指定して `start_markdown_agent_translation` を呼び出します。
2. 返された各チャンクをホストエージェント内でチャンクの `prompt` に従って翻訳します。
3. 元の `job` と翻訳済みチャンク（`chunk_id` と `translated_text` を使用）を指定して `finish_markdown_agent_translation` を呼び出します。
4. コンテンツが翻訳先のターゲットパスに書き込まれる場合は、`rewrite_markdown_paths` を呼び出します。

ノートブックの場合:

1. ノートブックの JSON と `language_code` を指定して `start_notebook_agent_translation` を呼び出します。
2. 返された各チャンクをホストエージェント内で翻訳します。
3. 元の `job` と翻訳済みチャンクを使って `finish_notebook_agent_translation` を呼び出します。
4. 翻訳されたノートブックのリンクでターゲットパスの調整が必要な場合は `rewrite_notebook_paths` を呼び出します。

エージェント支援ツールは Co-op Translator から設定された LLM プロバイダーを呼び出しません。ホストエージェントが返されたチャンクの翻訳を担当します。Co-op Translator は Markdown のチャンク化、プレースホルダの保持、フロントマターの再構築、ノートブックセルの置換、および翻訳後の正規化を処理します。

### リポジトリ全体を翻訳する

ユーザーが Co-op Translator に `translate` CLI のように動作させたい場合は `run_translation` を使用します。

リポジトリの翻訳はデフォルトで `dry_run=true` になっており、エージェントがファイル変更前に範囲を確認できます:

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "dry_run": true
}
```

`run_translation` の結果にはバージョン管理された `events` 配列が含まれます
`co-op.translation.event.v1` の進捗イベントです。MCP クライアントは
`type`、`stage_key`、`completed`、`total`、および `current_path` のようなフィールドを使用し、
キャプチャされたコンソールテキストを解析するのではなくそれらを参照してください。`json_events_path` を渡すと、
それらのイベントを NDJSON ファイルにも書き込みます。

書き込みを許可するには、呼び出し側が `dry_run=false` と `confirm_write=true` の両方を設定する必要があります:

```json
{
  "language_codes": "ko",
  "root_dir": ".",
  "markdown": true,
  "dry_run": false,
  "confirm_write": true
}
```

`translate_project` は `run_translation` の互換エイリアスとして公開されています。

### 翻訳済み出力のレビュー

LLM または Vision の資格情報を必要としない決定論的チェックには `run_review` を使用します:

!!! note "ベータ"
    MCP はベータの `run_review` API を公開しています。読み取り専用のレビュー ワークフローには安全ですが、レビューのチェックや問題スキーマは変更される可能性があります。

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "notebook": true
}
```

結果にはキャプチャされたテキスト出力と、利用可能な場合は構造化されたレビュー概要が含まれます。

## 手動サーバーの実行

手動実行は主にデバッグや、長時間稼働するサーバーのように振る舞うトランスポート用です。

デフォルトの stdio サーバーをデバッグするには:

```bash
co-op-translator-mcp
```

ソースチェックアウトから実行するには:

```bash
python -m co_op_translator.mcp.server
```

長時間稼働する HTTP または SSE サーバーを起動するには:

```bash
co-op-translator-mcp --transport streamable-http
co-op-translator-mcp --transport sse
```

ローカルのエディタやエージェント統合では、ステップ2のクライアント管理の `stdio` 設定を優先してください。

## ツール

| ツール | 用途 | ファイルを書き込みますか |
| --- | --- | --- |
| `translate_markdown_content` | Markdown 文字列を翻訳します。 | いいえ |
| `translate_notebook_content` | ノートブック JSON の Markdown セルを翻訳します。 | いいえ |
| `translate_image_content` | 画像内のテキストを翻訳し、base64 画像データを返します。 | 任意（`output_path` が指定された場合のみ） |
| `start_markdown_agent_translation` | Co-op Translator の LLM 資格情報なしでホストエージェントが翻訳できるように Markdown チャンクを準備します。 | いいえ |
| `finish_markdown_agent_translation` | ホストエージェントが翻訳したチャンクから Markdown を再構築します。 | いいえ |
| `start_notebook_agent_translation` | ホストエージェントが翻訳するためのノートブックの Markdown セルチャンクを準備します。 | いいえ |
| `finish_notebook_agent_translation` | ホストエージェントが翻訳したチャンクからノートブックの JSON を再構築します。 | いいえ |
| `rewrite_markdown_paths` | 翻訳対象に合わせて Markdown 本文とフロントマターのパスを書き換えます。 | いいえ |
| `rewrite_notebook_paths` | ノートブックの Markdown セル内のパスを書き換えます。 | いいえ |
| `run_translation` | CLI のようにプロジェクトレベルの翻訳を実行します。 | はい（`dry_run=false` および `confirm_write=true` のとき） |
| `translate_project` | `run_translation` の互換エイリアス。 | はい（`dry_run=false` および `confirm_write=true` のとき） |
| `run_review` | 決定論的レビューのチェックを実行します。 | いいえ |
| `get_configuration_status` | シークレットを公開せずに設定された LLM および Vision プロバイダーを報告します。 | いいえ |
| `list_supported_languages` | サポートされているターゲット言語コードを一覧表示します。 | いいえ |
| `get_api_overview` | 利用可能な MCP ワークフローとツールを説明します。 | いいえ |

## リソース

| リソース URI | 用途 |
| --- | --- |
| `co-op://api` | ワークフローとツールの JSON 概要。 |
| `co-op://supported-languages` | サポートされている言語コードの JSON リスト。 |
| `co-op://configuration` | シークレットを含まないプロバイダーの可用性サマリーの JSON。 |

## プロンプト

| プロンプト | 用途 |
| --- | --- |
| `translate_markdown_document_prompt` | コンテンツの翻訳とオプションのパス書き換えを MCP クライアントに案内します。 |
| `agent_assisted_markdown_translation_prompt` | Co-op Translator の LLM プロバイダー資格情報なしでホストエージェントによる Markdown 翻訳を MCP クライアントに案内します。 |
| `translate_repository_prompt` | まずはドライランを行うリポジトリ翻訳を MCP クライアントに案内します。 |

## コピー＆ペースト例

Markdown コンテンツを翻訳する:

```json
{
  "tool": "translate_markdown_content",
  "arguments": {
    "document": "# Hello\n\nWelcome to the course.",
    "language_code": "ko",
    "source_path": "docs/guide.md"
  }
}
```

翻訳済み Markdown のリンクを書き換える:

```json
{
  "tool": "rewrite_markdown_paths",
  "arguments": {
    "content": "[Setup](../setup.md)\n\n![Hero](images/hero.png)",
    "source_path": "docs/guide.md",
    "target_path": "translations/ko/docs/guide.md",
    "policy": {
      "language_code": "ko",
      "root_dir": ".",
      "translations_dir": "translations",
      "translated_images_dir": "translated_images",
      "translation_types": ["markdown", "images"]
    }
  }
}
```

ホストエージェントモデルで Markdown を翻訳する:

```json
{
  "tool": "start_markdown_agent_translation",
  "arguments": {
    "document": "# Hello\n\nUse `pip install` to get started.",
    "language_code": "ko",
    "source_path": "docs/guide.md"
  }
}
```

ホストエージェントが返された各チャンクを翻訳した後、`start_markdown_agent_translation` によって返された完全な `job` オブジェクトでジョブを完了します:

```text
tool: finish_markdown_agent_translation
arguments:
  job: <the full job object returned by start_markdown_agent_translation>
  translated_chunks:
    - chunk_id: body:1
      translated_text: "# 안녕하세요\n\n시작하려면 `pip install`을 사용하세요."
```

リポジトリ翻訳のプレビュー:

```json
{
  "tool": "run_translation",
  "arguments": {
    "language_codes": "ko",
    "root_dir": ".",
    "markdown": true,
    "dry_run": true
  }
}
```

## トラブルシューティング

| 問題 | 試すこと |
| --- | --- |
| MCP クライアントが `co-op-translator-mcp` を見つけられません。 | 絶対パスの Python 実行ファイルと `["-m", "co_op_translator.mcp.server"]` のソースチェックアウト構成を使用してください。 |
| サーバーは一覧に表示されるが翻訳に失敗します。 | `get_configuration_status` を呼び出して LLM プロバイダーが利用可能であることを確認してください。 |
| プロバイダーの資格情報なしで Markdown やノートブックの翻訳を行いたい場合。 | `start_markdown_agent_translation` / `finish_markdown_agent_translation` またはノートブックの同等の手順を使用して、ホストエージェントがチャンクを翻訳するようにしてください。 |
| 画像の翻訳に失敗します。 | Azure AI Vision の変数が設定されていることを確認し、`get_configuration_status` を呼び出してください。 |
| リポジトリ翻訳がファイルを書き込みません。 | 明示的なユーザー承認の後にのみ `dry_run=false` と `confirm_write=true` を設定してください。 |
| クライアント構成の変更が反映されない。 | MCP クライアントを再起動するかリロードしてください。 |

## 安全上の注意

- MCP のツール呼び出しはホストアプリケーションによってモデル制御されるため、リポジトリ翻訳はデフォルトでドライランになっています。
- リポジトリ全体の翻訳は多くのファイルを作成、更新、または削除する可能性があります。`confirm_write=true` を設定する前に明示的なユーザー承認を要求してください。
- 設定ステータスツールは API キー、エンドポイント、その他のシークレット値を返すことは決してありません。
- 画像翻訳は base64 画像データを返します。大きな画像は大きなツール応答を生む可能性があります。
- エージェント支援ツールはソースチャンクとプロンプトを MCP ホストに返します。これらはユーザーがそのホストエージェントモデルに送信することに問題ないコンテンツに対してのみ使用してください。