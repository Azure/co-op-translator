# ワークフローを選択

Co-op Translator は3つの方法で使用できます: CLI、Python API、MCP サーバー。それらは同じ翻訳機能を共有しますが、それぞれ異なるワークフローに適しています。

どこから始めるかを決める際にこのページを参照してください。

**翻訳を手作業で編集する場合：** デフォルトのCLIおよびActionsワークフローは変更されたソースファイルを完全に再翻訳するため、該当ファイルの表現が上書きされる可能性があります。更新を受け入れる前に差分を確認してください。受け入れた編集をMarkdownのブロックレベルで保持するには、オプションの[Python API 翻訳状態プロバイダー](api.md#preserve-accepted-human-edits-with-a-translation-state-provider)を使用してください。

## クイック判断

| したいこと | 使用するもの | 始める場所 |
| --- | --- | --- |
| ターミナルからリポジトリを翻訳またはレビューする | CLI | [CLI リファレンス](cli.md) |
| Pythonスクリプト、サービス、ノートブック、またはCIジョブに翻訳を追加する | Python API | [Python API](api.md) |
| エージェント、エディター、または MCP 互換クライアントに翻訳を任せる | MCP サーバー | [MCP サーバー](mcp.md) |
| アプリが既に読み込んでいるMarkdownドキュメント、ノートブック、または画像を1つ翻訳する | Python API または MCP サーバー | [Python API](api.md) または [MCP サーバー](mcp.md) |
| 標準の出力フォルダーとメタデータを使ってリポジトリ全体を翻訳する | CLI or `run_translation` | [CLI リファレンス](cli.md) または [Python API](api.md) |

## CLI を使用する場合

人や CI ジョブがシェルからリポジトリの翻訳を実行する場合は、CLI を選択してください。

Co-op Translator にプロジェクトファイルを検出させ、翻訳出力を作成し、プロジェクトレイアウトを維持し、メタデータを更新し、レビューコマンドを実行させたい場合、CLI が最も直接的な方法です。

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -md -nb
co-op-review -l "ko"
migrate-links -l "ko" --dry-run
```

この例は Markdown とノートブックを翻訳します。`-img` は [Azure AI Vision](configuration.md#azure-ai-vision) を設定した後にのみ追加してください。Markdown のみの最初の実行については、[最初の翻訳](first-translation.md) を参照してください。

適しているケース：

- ターミナルからリポジトリを翻訳する場合。
- CI やリリースワークフロー向けに再現可能なコマンドが欲しい場合。
- 組み込みのプロジェクト検出、出力パス、メタデータ、クリーンアップ、レビュー機能が欲しい場合。
- Python コードを書くよりもコマンドインターフェイスを好む場合。

## Python API を使用する場合

ワークフローを自分のコードで制御したい場合は、Python API を選択してください。

この API はアプリケーション、オートメーションスクリプト、ノートブック、サービス、カスタムパイプラインに有用です。個々のファイル向けの低レベルなコンテンツ翻訳 API を呼び出したり、CLI が使うのと同じリポジトリレベルのオーケストレーションを実行したりできます。

Markdown ドキュメントを1件翻訳して、保存先を決める:

```python
import asyncio
from pathlib import Path

from co_op_translator.api import rewrite_markdown_paths, translate_markdown_content


async def main() -> None:
    source_path = Path("docs/guide.md")
    target_path = Path("translations/ko/docs/guide.md")

    translated = await translate_markdown_content(
        source_path.read_text(encoding="utf-8"),
        "ko",
        {"source_path": source_path},
    )

    rewritten = rewrite_markdown_paths(
        translated,
        source_path=source_path,
        target_path=target_path,
    )

    target_path.parent.mkdir(parents=True, exist_ok=True)
    target_path.write_text(rewritten, encoding="utf-8")


asyncio.run(main())
```

Python からリポジトリの翻訳を実行する:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    notebook=True,
    images=False,
    dry_run=True,
)
```

適しているケース：

- アプリケーションが既にファイル、バッファ、ノートブック、または画像のバイト列を読み取っている場合。
- カスタムの検証、ストレージ、ログ記録、リトライ、または承認フローが必要な場合。
- リポジトリ全体を処理せずに、1つのドキュメント、ノートブック、または画像を翻訳したい場合。
- リポジトリの翻訳を行いたいが、シェルコマンドではなく Python の自動化から行いたい場合。

## MCP サーバーを使用する場合

エージェント、エディター、または MCP 互換クライアントが Co-op Translator のツールを呼び出すべき場合は、MCP サーバーを選択してください。

通常のローカルセットアップでは、ユーザーが手動でサーバーを常駐させることはありません。MCP クライアントはツールが必要なときに `stdio` 経由で `co-op-translator-mcp` を起動します。

エージェントが処理できるユーザーリクエストの例：

- "この Markdown ファイルを韓国語に翻訳し、リンクを正しく保ってください。"
- "エージェント支援型の MCP ワークフローでこの Markdown ファイルを韓国語に翻訳し、翻訳されたチャンクには自分のモデルを使用してください。"
- "このノートブックを韓国語に翻訳し、コードセルを保持し、Co-op Translator MCP を使ってノートブックを再構築してください。"
- "この画像内のテキストを日本語に翻訳して結果を保存してください。"
- "リポジトリ翻訳をスペイン語でドライランして、何が変更されるか教えてください。"
- "韓国語翻訳の出力が最新かどうかを確認してください。"

Markdown とノートブックについて、MCP は2つのモードで動作できます：

| モード | 使う場面 | 主なツール |
| --- | --- | --- |
| エージェント支援型 | MCP ホストエージェントが Co-op Translator の LLM プロバイダー資格情報を使わずに、自身のモデルでチャンクを翻訳する場合。 | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| プロバイダー支援型 | Co-op Translator が直接 Azure OpenAI、OpenAI、または Anthropic を呼び出す場合。 | `translate_markdown_content`, `translate_notebook_content` |

MCP のプロバイダー支援型 Markdown ツール呼び出しの形式：

```json
{
  "tool": "translate_markdown_content",
  "arguments": {
    "document": "# Setup\n\nInstall Co-op Translator first.",
    "language_code": "ko",
    "options": {
      "source_path": "docs/setup.md"
    }
  }
}
```

MCP 画像ツール呼び出しの形式：

```json
{
  "tool": "translate_image_content",
  "arguments": {
    "image_path": "assets/architecture.png",
    "language_code": "ko",
    "output_path": "translated_images/ko/assets/architecture.png"
  }
}
```

リポジトリの翻訳はデフォルトで MCP を通じてドライランされます：

```json
{
  "tool": "run_translation",
  "arguments": {
    "language_codes": ["ko"],
    "translate_markdown": true,
    "translate_notebooks": true,
    "translate_images": false,
    "dry_run": true
  }
}
```

適しているケース：

- エージェントやエディター内で自然言語ベースの翻訳ワークフローを望む場合。
- ホストエージェントのモデルが準備されたチャンクを翻訳するような Markdown またはノートブックの翻訳が必要な場合。
- リポジトリ全体ではなく、エージェントに選択したコンテンツを翻訳してほしい場合。
- リポジトリ全体への書き込みの前に承認ステップを設けたい場合。
- Markdown、ノートブック、画像、レビュー、パス書き換えツールを公開する単一のインターフェイスが欲しい場合。

## それらの連携

リポジトリを翻訳する人には CLI がデフォルトで最適です。コードがワークフローを担う場合は Python API が最適です。エージェントやエディターがワークフローを担う場合は MCP サーバーが最適です。

3つの経路はすべて同じ公開 Co-op Translator API を使用するため、CLI で始めてあとで Python で自動化し、エージェント主導のワークフローが必要になったら同じ機能を MCP クライアントに公開することができます。