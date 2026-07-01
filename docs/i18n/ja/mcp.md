# MCP サーバー

Co-op Translator には、エージェント、エディター、および MCP 互換クライアント向けの Model Context Protocol サーバーが含まれています。

デフォルトのローカル構成では、ユーザーが手動で別のサーバーを常時起動しておく必要はありません。MCP クライアントを構成すると、クライアントは Co-op Translator ツールが必要になったときに自動的に `co-op-translator-mcp` を `stdio` 経由で起動します。

CLI、Python API、MCP のいずれを選ぶか迷っている場合は、まず [ワークフローを選ぶ](workflows.md) を参照してください。

エージェントやエディターが Co-op Translator を直接呼び出すべき場合は MCP を使用します:

| User goal | MCP tools |
| --- | --- |
| Translate one Markdown document, notebook, or image | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content` |
| Translate Markdown or notebook content with the host agent model | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Rewrite translated Markdown or notebook links after choosing the output path | `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Translate a full repository like the CLI | `run_translation`, `translate_project` |
| Review translated output without LLM credentials | `run_review` |
| Inspect capabilities and environment status | `get_api_overview`, `list_supported_languages`, `get_configuration_status` |

MCP サーバーは [Python API](api.md) に記載されているのと同じ公開 Python API をラップします。プロバイダー対応ツールは CLI や Python API と同じ構成済みプロバイダーを使用します。エージェント支援ツールは MCP ホストエージェントが翻訳するためのチャンクを準備し、その後 Co-op Translator を使って最終的な Markdown やノートブックを再構築します。

## Step 1: Install and Configure Co-op Translator

MCP クライアントが使用する Python 環境に Co-op Translator をインストールします:

```bash
pip install co-op-translator
```

このリポジトリからローカル開発を行う場合は、パッケージを編集可能モードでインストールします:

```bash
pip install -e .
```

MCP クライアントが使用する翻訳モードを選択します:

| Mode | Use this for | Credentials |
| --- | --- | --- |
| Provider-backed | Co-op Translator calls `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, or `run_translation`. | Markdown and notebook translation require Azure OpenAI or OpenAI. Image translation also requires Azure AI Vision. |
| Agent-assisted | The MCP host agent translates chunks returned by `start_markdown_agent_translation` or `start_notebook_agent_translation`. | No Co-op Translator LLM provider credentials are required for Markdown or notebook chunks. Image translation is not covered by agent-assisted mode yet. |

Codex や Claude Code のようなエージェント内で Markdown やノートブックの翻訳を開始する場合は、エージェント支援モードから始めてください。Co-op Translator 自身に構成済みプロバイダーを呼び出してほしい場合、画像を翻訳する場合、または CLI のようなリポジトリ単位の翻訳を実行する場合は、プロバイダー対応モードを使用してください。

プロバイダー対応ワークフローにはプロバイダーの認証情報を構成してください:

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

プロバイダー対応の画像翻訳には追加で以下が必要です:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

!!! note
    エージェント支援モードは現在 Markdown とノートブックの Markdown セルをカバーしています。画像翻訳はまだエージェント支援モードには含まれず、OCR とレイアウト対応レンダリングには Azure AI Vision が必要です。

## Step 2: Configure Your MCP Client

通常のローカル `stdio` 構成では、Co-op Translator を MCP クライアントの構成に追加します。クライアントはプロセスを自動的に開始および停止します。

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

Windows のソースチェックアウト構成:

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

macOS または Linux のソースチェックアウト構成:

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

MCP クライアント構成を変更した後、クライアントを再起動またはリロードして新しいサーバーを検出させてください。

## Step 3: Verify the Server in the Client

MCP クライアントに利用可能なツールの一覧を表示させるか、まずは読み取り専用のヘルパーを呼び出してください:

```json
{
  "tool": "get_api_overview",
  "arguments": {}
}
```

便利な最初のチェック:

| Tool | What to check |
| --- | --- |
| `get_api_overview` | サーバーに到達でき、利用可能なワークフローが表示されることを確認します。 |
| `list_supported_languages` | 同梱された言語データが読み込めることを確認します。 |
| `get_configuration_status` | シークレット値を晒さずに LLM と Vision プロバイダーの利用可能性を確認します。 |

## Step 4: Choose a Workflow

### Translate Individual Files or Documents

MCP クライアントが既にドキュメントの内容や画像パスを持っており、Co-op Translator が構成済みの翻訳プロバイダーを呼び出すべき場合は、プロバイダー対応のコンテンツツールを使用してください。

Markdown の場合:

1. `document`、`language_code`、およびオプションで `source_path` を指定して `translate_markdown_content` を呼び出します。
2. 翻訳結果を Co-op Translator の出力レイアウトに書き込む場合は、`rewrite_markdown_paths` を呼び出します。
3. クライアントに最終的な `content` を書き込ませるか返却します。

ノートブックの場合:

1. ノートブック JSON と `language_code` を指定して `translate_notebook_content` を呼び出します。
2. 翻訳済みノートブックのリンクをターゲットパスに合わせて調整する必要がある場合は `rewrite_notebook_paths` を呼び出します。
3. 最終的なノートブック JSON を書き込むか返却します。

画像の場合:

1. `image_path`、`language_code`、およびオプションの `root_dir` や `fast_mode` を指定して `translate_image_content` を呼び出します。
2. 返された `data_base64` と `mime_type` を読み取ります。
3. `output_path` が指定されている場合、翻訳済み画像はそのパスにも保存されます。

これらのコンテンツツールは、プロジェクトの検出、メタデータ更新、免責事項、または自動的なパス書き換えを実行しません。ホストエージェントに Co-op Translator の LLM プロバイダー認証情報なしで Markdown またはノートブックのチャンクを翻訳させたい場合は、以下のエージェント支援ワークフローを使用してください。

### Translate with the Host Agent Model

エージェント支援ツールは、Azure OpenAI や OpenAI を Co-op Translator に構成せずに、MCP ホストエージェント（コーディングアシスタントなど）に翻訳テキストを生成させたい場合に使用します。

チャットベースの MCP クライアントでは、通常ツールの JSON を自分で書く必要はありません。エージェントにエージェント支援ワークフローを使用するよう依頼してください:

```text
Translate this Markdown file to Korean with Co-op Translator MCP.
Use agent-assisted mode: call start_markdown_agent_translation, translate the returned chunks with your own model, then call finish_markdown_agent_translation.
Keep Markdown formatting, code blocks, and links intact.
```

ノートブックの場合も同じパターンを使用します:

```text
Translate this notebook to Korean with Co-op Translator MCP.
Use start_notebook_agent_translation, translate the returned Markdown-cell chunks with your own model, then call finish_notebook_agent_translation.
Preserve code cells, outputs, and notebook metadata.
```

MCP クライアントがサーバープロンプトをサポートしている場合は、クライアントに同じワークフロー指示を読み込ませるために `agent_assisted_markdown_translation_prompt` を使用してください。

Markdown の場合:

1. `document`、`language_code`、およびオプションで `source_path` を指定して `start_markdown_agent_translation` を呼び出します。
2. ホストエージェント内で返された各チャンクを、チャンクの `prompt` に従って翻訳します。
3. 元の `job` と `chunk_id` と `translated_text` を使用して翻訳済みチャンクで `finish_markdown_agent_translation` を呼び出します。
4. コンテンツが翻訳されたターゲットパスに書き込まれる場合は、`rewrite_markdown_paths` を呼び出します。

ノートブックの場合:

1. ノートブック JSON と `language_code` を指定して `start_notebook_agent_translation` を呼び出します。
2. ホストエージェント内で返された各チャンクを翻訳します。
3. 元の `job` と翻訳済みチャンクで `finish_notebook_agent_translation` を呼び出します。
4. 翻訳済みノートブックのリンクをターゲットパスに合わせて調整する必要がある場合は `rewrite_notebook_paths` を呼び出します。

エージェント支援ツールは Co-op Translator から Azure OpenAI や OpenAI を呼び出しません。ホストエージェントが返されたチャンクの翻訳を担当します。Co-op Translator は Markdown のチャンク化、プレースホルダーの保持、フロントマターの再構築、ノートブックセルの置換、翻訳後の正規化を処理します。

### Translate an Entire Repository

ユーザーが Co-op Translator に CLI のように動作させたい場合は `run_translation` を使用します。

リポジトリ翻訳はデフォルトで `dry_run=true` になっており、エージェントがファイル変更の範囲を検査できます:

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "dry_run": true
}
```

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

### Review Translated Output

LLM や Vision の認証情報を必要としない決定論的チェックには `run_review` を使用します。

!!! note "Beta"
    MCP はベータ版の `run_review` API を公開しています。読み取り専用のレビュー ワークフローには安全ですが、レビューのチェックや問題スキーマは進化する可能性があります。

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "notebook": true
}
```

結果には、キャプチャされたテキスト出力と、利用可能な場合は構造化されたレビューサマリーが含まれます。

## Manual Server Runs

手動実行は主にデバッグや長時間実行されるサーバーのように振る舞うトランスポート向けです。

デフォルトの stdio サーバーをデバッグする:

```bash
co-op-translator-mcp
```

ソースチェックアウトから実行する:

```bash
python -m co_op_translator.mcp.server
```

長時間稼働する HTTP または SSE サーバーを起動する:

```bash
co-op-translator-mcp --transport streamable-http
co-op-translator-mcp --transport sse
```

ローカルのエディターやエージェント統合では、ステップ 2 のクライアント管理の `stdio` 構成を優先してください。

## Tools

| Tool | Purpose | Writes files |
| --- | --- | --- |
| `translate_markdown_content` | Translate a Markdown string. | No |
| `translate_notebook_content` | Translate Markdown cells in notebook JSON. | No |
| `translate_image_content` | Translate text in one image and return base64 image data. | Optional, only when `output_path` is provided |
| `start_markdown_agent_translation` | Prepare Markdown chunks for the host agent to translate without Co-op Translator LLM credentials. | No |
| `finish_markdown_agent_translation` | Reconstruct Markdown from host-agent translated chunks. | No |
| `start_notebook_agent_translation` | Prepare notebook Markdown-cell chunks for the host agent to translate. | No |
| `finish_notebook_agent_translation` | Reconstruct notebook JSON from host-agent translated chunks. | No |
| `rewrite_markdown_paths` | Rewrite Markdown body and frontmatter paths for a translated target. | No |
| `rewrite_notebook_paths` | Rewrite paths inside notebook Markdown cells. | No |
| `run_translation` | Run project-level translation like the CLI. | Yes when `dry_run=false` and `confirm_write=true` |
| `translate_project` | Compatibility alias for `run_translation`. | Yes when `dry_run=false` and `confirm_write=true` |
| `run_review` | Run deterministic review checks. | No |
| `get_configuration_status` | Report configured LLM and Vision providers without exposing secrets. | No |
| `list_supported_languages` | List supported target language codes. | No |
| `get_api_overview` | Describe available MCP workflows and tools. | No |

## Resources

| Resource URI | Purpose |
| --- | --- |
| `co-op://api` | JSON overview of workflows and tools. |
| `co-op://supported-languages` | JSON list of supported language codes. |
| `co-op://configuration` | JSON provider availability summary without secrets. |

## Prompts

| Prompt | Purpose |
| --- | --- |
| `translate_markdown_document_prompt` | Guide an MCP client through content translation plus optional path rewriting. |
| `agent_assisted_markdown_translation_prompt` | Guide an MCP client through host-agent Markdown translation without Co-op Translator LLM provider credentials. |
| `translate_repository_prompt` | Guide an MCP client through dry-run-first repository translation. |

## Copy-Paste Examples

Translate Markdown content:

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

Rewrite translated Markdown links:

```json
{
  "tool": "rewrite_markdown_paths",
  "arguments": {
    "content": "[Setup](../setup.md)\n\n![Hero](../../images/hero.png)",
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

Translate Markdown with the host agent model:

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

After the host agent translates each returned chunk, finish the job with the complete `job` object returned by `start_markdown_agent_translation`:

```text
tool: finish_markdown_agent_translation
arguments:
  job: <the full job object returned by start_markdown_agent_translation>
  translated_chunks:
    - chunk_id: body:1
      translated_text: "# 안녕하세요\n\n시작하려면 `pip install`을 사용하세요."
```

Preview repository translation:

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

## Troubleshooting

| Problem | What to try |
| --- | --- |
| The MCP client cannot find `co-op-translator-mcp`. | Use the absolute Python executable path and `["-m", "co_op_translator.mcp.server"]` source checkout configuration. |
| The server is listed but translation fails. | Call `get_configuration_status` and confirm an LLM provider is available. |
| You want Markdown or notebook translation without Azure OpenAI/OpenAI keys. | Use `start_markdown_agent_translation` / `finish_markdown_agent_translation` or the notebook equivalents so the host agent translates the chunks. |
| Image translation fails. | Confirm Azure AI Vision variables are set and call `get_configuration_status`. |
| Repository translation does not write files. | Set `dry_run=false` and `confirm_write=true` only after explicit user approval. |
| Changes to client config do not appear. | Restart or reload the MCP client. |

## Safety Notes

- MCP tool calls are model-controlled by the host application, so repository translation is dry-run by default.
- Full repository translation can create, update, or remove many files. Require explicit user approval before setting `confirm_write=true`.
- The configuration status tool never returns API keys, endpoints, or other secret values.
- Image translation returns base64 image data. Large images can produce large tool responses.
- Agent-assisted tools return source chunks and prompts to the MCP host. Use them only with content the user is comfortable sending to that host agent model.