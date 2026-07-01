# ワークフローを選択

Co-op Translator は CLI、Python API、MCP サーバーの三通りで使用できます。翻訳機能は共通ですが、それぞれ異なるワークフローに適しています。

どこから始めるかを決めるときにこのページを使用してください。

## 迅速な判断

| If you want to... | Use | Start here |
| --- | --- | --- |
| ターミナルからリポジトリを翻訳またはレビューする | CLI | [CLI リファレンス](cli.md) |
| Python スクリプト、サービス、ノートブック、または CI ジョブに翻訳を追加する | Python API | [Python API](api.md) |
| エージェント、エディタ、または MCP 互換クライアントにコンテンツを翻訳させる | MCP Server | [MCP サーバー](mcp.md) |
| アプリが既に読み込んでいる Markdown ドキュメント、ノートブック、または画像を1つ翻訳する | [Python API](api.md) または [MCP サーバー](mcp.md) | [Python API](api.md) または [MCP サーバー](mcp.md) |
| 標準的な出力フォルダとメタデータを持つリポジトリ全体を翻訳する | CLI または `run_translation` | [CLI リファレンス](cli.md) または [Python API](api.md) |

## CLI を使用する場合

人や CI ジョブがシェルからリポジトリの翻訳を実行する場合は CLI を選んでください。

Co-op Translator にプロジェクトファイルを検出させ、翻訳された出力を作成し、プロジェクトのレイアウトを保持し、メタデータを更新し、レビューコマンドを実行させたいときに、CLI が最も直接的な方法です。

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -md -nb -img
co-op-review -l "ko" -md -nb
migrate-links -l "ko" --dry-run
```

適しているケース:

- ターミナルからリポジトリを翻訳している。
- CI やリリースワークフローのために再現可能なコマンドが欲しい。
- 組み込みのプロジェクト検出、出力パス、メタデータ、クリーンアップ、およびレビューを望む。
- Python コードを書くよりコマンドインターフェイスを好む。

## Python API を使用する場合

ワークフローを自身のコードで制御する場合は Python API を選んでください。

API はアプリケーション、自動化スクリプト、ノートブック、サービス、およびカスタムパイプラインで役立ちます。個々のファイルに対する低レベルのコンテンツ翻訳 API を呼び出したり、CLI と同じリポジトリレベルのオーケストレーションを実行したりできます。

Markdown ドキュメントを1つ翻訳し、保存先を決める:

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
import asyncio

from co_op_translator.api import run_translation


async def main() -> None:
    await run_translation(
        language_codes=["ko"],
        translate_markdown=True,
        translate_notebooks=True,
        translate_images=False,
        dry_run=True,
    )


asyncio.run(main())
```

適しているケース:

- アプリケーションが既にファイル、バッファ、ノートブック、または画像のバイト列を読み取っている。
- カスタム検証、ストレージ、ロギング、再試行、または承認フローが必要である。
- リポジトリ全体を処理せずに1つのドキュメント、ノートブック、または画像を翻訳したい。
- シェルコマンドではなく Python 自動化からリポジトリ翻訳を行いたい。

## MCP サーバーを使用する場合

エージェント、エディタ、または MCP 互換クライアントが Co-op Translator のツールを呼び出すべき場合は MCP サーバーを選んでください。

通常のローカルセットアップでは、ユーザーが手動でサーバーを常駐させることはありません。MCP クライアントはツールが必要になったときに `co-op-translator-mcp` を `stdio` 経由で起動します。

エージェントが対応できるユーザーのリクエスト例:

- "この Markdown ファイルを韓国語に翻訳し、リンクを正しく維持してください。"
- "エージェント支援の MCP ワークフローで、この Markdown ファイルを韓国語に翻訳し、翻訳したチャンクに自身のモデルを使用してください。"
- "このノートブックを韓国語に翻訳し、コードセルを保持し、Co-op Translator MCP を使ってノートブックを再構築してください。"
- "この画像内のテキストを日本語に翻訳して結果を保存してください。"
- "リポジトリの翻訳をスペイン語でドライランし、何が変更されるか教えてください。"
- "韓国語翻訳の出力が最新かどうかをレビューしてください。"

Markdown とノートブックについて、MCP は2つのモードで動作できます:

| Mode | Use when | Main tools |
| --- | --- | --- |
| エージェント支援 | MCP ホストのエージェントが、Co-op Translator の LLM プロバイダーの資格情報を使わずに自身のモデルでチャンクを翻訳する場合に使用します。 | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| プロバイダー対応 | Co-op Translator が Azure OpenAI や OpenAI を直接呼び出す場合に使用します。 | `translate_markdown_content`, `translate_notebook_content` |

MCP プロバイダー対応の Markdown ツール呼び出し形式:

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

MCP 画像ツール呼び出し形式:

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

リポジトリの翻訳はデフォルトで MCP 経由でドライランされます:

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

適しているケース:

- エージェントやエディタ内で自然言語の翻訳ワークフローを望む場合。
- ホストエージェントのモデルが準備されたチャンクを翻訳する Markdown またはノートブックの翻訳を望む場合。
- リポジトリ全体ではなく、エージェントに選択したコンテンツを翻訳させたい場合。
- リポジトリ全体への書き込みの前に承認ステップを入れたい場合。
- Markdown、ノートブック、画像、レビュー、パス書き換えツールを公開する一つのインターフェースを望む場合。

## それらの連携方法

CLI は人がリポジトリを翻訳する際のデフォルトとして最適です。Python API はコードがワークフローを所有する場合に最適です。MCP サーバーはエージェントやエディタがワークフローを所有する場合に最適です。

3つのパスはすべて同じ公開 Co-op Translator API を使用するため、CLI で始めて後で Python で自動化し、エージェント駆動のワークフローが必要になったときには同じ機能を MCP クライアントに公開することができます。