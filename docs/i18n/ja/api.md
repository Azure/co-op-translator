# Python API

安定した公開 Python API は `co_op_translator.api` からエクスポートされます。ほとんどの統合は次のワークフローのいずれかを使用します:

| Scenario | Use this when | Main APIs |
| --- | --- | --- |
| 個々のファイルまたはドキュメントを翻訳する | アプリケーションがソースコンテンツを読み取り、Co-op Translator を呼び出して翻訳し、結果をどこに保存するかを決定します。 | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| ホストエージェントによる翻訳のためにコンテンツを準備する | MCP ホストまたはアプリケーションモデルがチャンクを翻訳し、Co-op Translator はチャンク分割と再構築を処理します。 | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| リポジトリ全体を翻訳する | Python API に CLI のように動作させ、探索、出力パス、メタデータ、クリーンアップ、および書き込みを処理させたい場合。 | `run_translation` |

`core`、`config`、`review`、および `utils` の下位モジュールの多くは、これらの API エントリポイントで使用される実装の詳細です。

MCP クライアントは [MCP サーバー](mcp.md) 経由で同じ公開 API を使用します。Python を直接呼び出す場合はこのページを使用し、エージェントやエディタに Co-op Translator を公開する場合は MCP ガイドを使用してください。CLI、Python API、MCP のどれを選ぶか迷っている場合は、まず [ワークフローの選択](workflows.md) を見てください。

## 初回の API フロー

Python コードから Co-op Translator を呼び出す場合はここから始めてください:

1. ホストエージェント翻訳用に Markdown やノートブックのチャンクを準備するだけでない限り、[設定](configuration.md) に記載のとおり LLM プロバイダーを設定します。
2. アプリケーションがファイル I/O を担当するかどうかを決めます。
3. アプリケーションが個々のファイルを読み書きする場合は、コンテンツ用 API を使用します。
4. Co-op Translator にリポジトリを CLI のように処理させる場合は `run_translation` を使用します。
5. 自動化で決定論的なチェックが必要な場合は、翻訳後に `run_review` を使用します。

| Goal | API to start with |
| --- | --- |
| 1つの Markdown 文字列またはファイルを翻訳する | `translate_markdown_content` |
| Translate one notebook payload | `translate_notebook_content` |
| Translate one image | `translate_image_content` |
| ホスト エージェントに Markdown またはノートブックのチャンクを翻訳させる | `start_markdown_agent_translation` or `start_notebook_agent_translation` |
| 出力パスを選択した後に翻訳済みリンクを書き換える | `rewrite_markdown_paths` or `rewrite_notebook_paths` |
| Translate a full repository | `run_translation` |
| Review translated output | `run_review` |

## シナリオ 1: 個別のファイルまたはドキュメントを翻訳する

ファイル、エディタのバッファ、ノートブックのペイロード、MCP リクエスト、またはカスタムパイプライン入力を既に持っている場合は、このワークフローを使用します。ファイル I/O はあなたのコードが担当します:

1. ソースコンテンツを読み取ります。
2. コンテンツ翻訳 API を呼び出します。
3. 翻訳されたコンテンツをプロジェクトの翻訳フォルダーに書き込む場合は、オプションでパス書き換え API を呼び出します。
4. アプリケーションから結果を保存または返します。

コンテンツ翻訳 API はプロジェクト検出を行わず、メタデータを書き込まず、免責事項を追加せず、リンクを書き換えません。

### マークダウンファイル

```python
import asyncio
from pathlib import Path

from co_op_translator.api import (
    rewrite_markdown_paths,
    translate_markdown_content,
)


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
        policy={
            "language_code": "ko",
            "root_dir": ".",
            "translations_dir": "translations",
            "translated_images_dir": "translated_images",
            "translation_types": ["markdown", "images"],
        },
    )

    target_path.parent.mkdir(parents=True, exist_ok=True)
    target_path.write_text(rewritten, encoding="utf-8")


asyncio.run(main())
```

翻訳された Markdown が Co-op Translator のプロジェクトレイアウトに置かれない場合は、`rewrite_markdown_paths` はスキップして、翻訳済みの文字列を直接保存します。

### ノートブックファイル

```python
import asyncio
from pathlib import Path

from co_op_translator.api import (
    rewrite_notebook_paths,
    translate_notebook_content,
)


async def main() -> None:
    source_path = Path("docs/tutorial.ipynb")
    target_path = Path("translations/ja/docs/tutorial.ipynb")

    translated_json = await translate_notebook_content(
        source_path.read_text(encoding="utf-8"),
        "ja",
        {"source_path": source_path},
    )

    rewritten_json = rewrite_notebook_paths(
        translated_json,
        source_path=source_path,
        target_path=target_path,
        policy={
            "language_code": "ja",
            "root_dir": ".",
            "translations_dir": "translations",
            "translated_images_dir": "translated_images",
            "translation_types": ["notebook", "images"],
        },
    )

    target_path.parent.mkdir(parents=True, exist_ok=True)
    target_path.write_text(rewritten_json, encoding="utf-8")


asyncio.run(main())
```

`translate_notebook_content` は Markdown セルを翻訳し、非 Markdown セルは保持します。パスの書き換えは Markdown セルにのみ適用されます。

### 画像ファイル

```python
from pathlib import Path

from co_op_translator.api import translate_image_content

source_path = Path("docs/images/hero.png")
target_path = Path("translated_images/fr/hero.png")

translated_image = translate_image_content(
    source_path,
    "fr",
    {
        "root_dir": ".",
        "fast_mode": False,
    },
)

target_path.parent.mkdir(parents=True, exist_ok=True)
translated_image.save(target_path)
```

`translate_image_content` はソース画像を読み込み、レンダリングされた `PIL.Image.Image` を返します。翻訳された画像のメタデータは書き込みません。

## シナリオ 2: リポジトリ全体を翻訳する

このワークフローは、Python API を `translate` CLI のように動作させたい場合に使用します。`run_translation` はサポートされているファイルを検出し、選択されたコンテンツタイプを翻訳し、パスを書き換え、出力ファイルを書き込み、メタデータを更新し、クリーンアップなどの翻訳保守タスクを実行します。

`run_translation` は推奨されるプロジェクトオーケストレーションのエントリポイントです。`translate_project` は同じ動作の互換エイリアスとしてエクスポートされています。

現在のリポジトリ内の Markdown ファイルを韓国語と日本語に翻訳する:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    markdown=True,
)
```

特定のプロジェクトルートからノートブックのみを翻訳する:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="fr",
    root_dir="./my-course",
    notebook=True,
)
```

ファイルを書き込まずに翻訳ボリュームをプレビューする:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="es de",
    root_dir="./my-course",
    markdown=True,
    dry_run=True,
)
```

統合のために構造化された進捗イベントを記録する:

```python
from co_op_translator.api import TranslationEvent, run_translation


def on_event(event: TranslationEvent) -> None:
    payload = event.to_dict()
    # ペイロードをジョブイベントテーブルに保存するか、UIにストリーミングしてください。


run_translation(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
    progress_callback=on_event,
)
```

Events use the versioned schema `co-op.translation.event.v1`. Integrations should
depend on stable fields such as `type` and `stage_key`, not on human-facing
console text or `stage_label`.

複数のコンテンツルートを一度の呼び出しで翻訳する:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    root_dirs=["./docs", "./labs"],
)
```

翻訳を明示的な出力グループに書き込む:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ja",
    markdown=True,
    groups=[
        ("./course-a", "./localized/course-a"),
        ("./course-b", "./localized/course-b"),
    ],
)
```

各言語ごとにネストされたサブディレクトリが必要な場合は、言語ごとのプレースホルダーを使用します:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    groups=[
        ("./course", "./translations/<lang>/course"),
    ],
)
```

`markdown`、`notebook`、または `images` のいずれも設定されていない場合、API はサポートされているすべてのタイプ（Markdown、ノートブック、画像）を翻訳します。

### 翻訳ステートプロバイダーで受け入れられた人間の編集を保持する

デフォルトでは、Co-op Translator は従来のファイル単位の動作を維持します:
Markdown ソースが古くなっている場合、翻訳済みファイル全体が再生成されます。ホストされた
統合はオプションで `TranslationStateProvider` を渡して、
変更されていないソースブロック内の人間による編集を保持できます。

プロバイダーは最後に受け入れられたソース/ターゲットのペアを提供し、各新しい
候補を記録します。受け入れは統合側の責任のままです—例えば、
翻訳のプルリクエストがマージされた後など:

```python
from pathlib import Path

from co_op_translator.api import (
    TranslationBaseline,
    TranslationUpdate,
    run_translation,
)


class DatabaseTranslationState:
    def load_baseline(
        self,
        *,
        source_path: Path,
        translation_path: Path,
        language_code: str,
    ) -> TranslationBaseline | None:
        row = load_accepted_translation(
            source_path=source_path,
            translation_path=translation_path,
            language_code=language_code,
        )
        if row is None:
            return None
        return TranslationBaseline(
            source_text=row.source_text,
            target_text=row.target_text,
            revision=row.accepted_revision,
        )

    def record_candidate(
        self,
        *,
        source_path: Path,
        translation_path: Path,
        language_code: str,
        source_text: str,
        target_text: str,
        update: TranslationUpdate,
    ) -> None:
        save_translation_candidate(
            source_path=source_path,
            translation_path=translation_path,
            language_code=language_code,
            source_text=source_text,
            target_text=target_text,
            mode=update.mode,
            fallback_reason=update.fallback_reason,
        )


run_translation(
    language_codes="ko",
    root_dir="./course",
    markdown=True,
    translation_state_provider=DatabaseTranslationState(),
)
```

有効な受け入れベースラインを持つ Markdown ファイルについて、Co-op Translator は
トップレベルの Markdown ブロックを整列します。変更されていないソースブロックは現在の翻訳済み
ブロック（人による編集を含む）を再利用します。変更または追加されたソースブロックは翻訳に送られ、
削除されたソースブロックは削除されます。整列があいまいな場合、
ターゲット構造が変更された場合、ブロック翻訳が無効な場合、またはベースラインが
利用できない場合、Co-op Translator は安全に既存のファイル全体の
翻訳パスにフォールバックします。

この API はドキュメントの翻訳状態を保存します。文書間のフレーズや
セグメント翻訳メモリではありません。現在は Markdown プロジェクトの
翻訳に適用されます。ノートブックと画像の挙動は変更されません。`update=True` を渡すと
それでも完全な再生成を要求します。

1つ以上のファイルを翻訳できない場合、`run_translation` は
プロジェクトワークフローの終了後に `RuntimeError` を発生させ、
出力が欠けた成功実行を報告する代わりにエラーとします。統合はこれを失敗した
ジョブと見なし、以前の受け入れ済み翻訳状態を保持するべきです。

## 翻訳された出力を確認する

`run_review` は LLM や Vision の認証情報なしで決定論的な翻訳チェックを実行します。

!!! note "ベータ"
    `run_review` はベータの決定的なレビュー API です。モデルプロバイダーを呼び出したりファイルを書き込んだりはしませんが、チェックや issue スキーマは進化する可能性があります。

```python
from co_op_translator.api import run_review

run_review(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
)
```

README のみの翻訳の後は、レビューに同じスコープを使用します:

```python
run_review(language_codes="ko", root_dir="./my-course", readme_only=True)
```

`readme_only=True` は、各設定されたソースルートの下にある `README.md` のみをレビューします、
カスタムの `groups` や出力ディレクトリを含みます。他のドキュメントや入れ子になった
README は除外されます。ソース README がない場合は `ValueError` を発生させます; 失敗した
翻訳チェックの失敗は `RuntimeError` を発生させます。

ベースリファレンスとの差分のみをレビューし、GitHub 風の出力を表示する:

```python
from co_op_translator.api import run_review

run_review(
    language_codes="ko",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
    changed_from="origin/main",
    output_format="github",
)
```

## コピー＆ペースト API の例

ファイルを書き込まずに Markdown コンテンツを翻訳する:

```python
import asyncio

from co_op_translator.api import translate_markdown_content


async def main() -> None:
    translated = await translate_markdown_content(
        "# Hello\n\nWelcome to the course.",
        "ko",
    )
    print(translated)


asyncio.run(main())
```

Markdown リンクを翻訳して書き換える:

```python
import asyncio

from co_op_translator.api import rewrite_markdown_paths, translate_markdown_content


async def main() -> None:
    translated = await translate_markdown_content(
        "[Setup](../setup.md)\n\n![Hero](images/hero.png)",
        "ko",
        {"source_path": "docs/guide.md"},
    )
    rewritten = rewrite_markdown_paths(
        translated,
        source_path="docs/guide.md",
        target_path="translations/ko/docs/guide.md",
        policy={
            "language_code": "ko",
            "root_dir": ".",
            "translations_dir": "translations",
            "translated_images_dir": "translated_images",
            "translation_types": ["markdown", "images"],
        },
    )
    print(rewritten)


asyncio.run(main())
```

Python からリポジトリを翻訳する:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    root_dir="./course",
    markdown=True,
    yes=True,
)
```

複数のルートを翻訳する:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    root_dirs=[
        "./docs",
        "./labs",
    ],
)
```

用語集の用語を保持する:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="fr",
    markdown=True,
    glossaries=[
        "Co-op Translator",
        "Azure AI Foundry",
        "GitHub Actions",
    ],
)
```

## 公開エントリポイント

```python
from co_op_translator.api import (
    ImageTranslationOptions,
    MarkdownTranslationOptions,
    NotebookTranslationOptions,
    TranslationBaseline,
    TranslationStateProvider,
    TranslationUpdate,
    finish_markdown_agent_translation,
    finish_notebook_agent_translation,
    run_review,
    run_translation,
    rewrite_markdown_paths,
    rewrite_notebook_paths,
    start_markdown_agent_translation,
    start_notebook_agent_translation,
    translate_image_content,
    translate_markdown_content,
    translate_notebook_content,
    translate_project,
)
```

::: co_op_translator.api.translate_markdown_content

::: co_op_translator.api.translate_notebook_content

::: co_op_translator.api.translate_image_content

::: co_op_translator.api.start_markdown_agent_translation

::: co_op_translator.api.finish_markdown_agent_translation

::: co_op_translator.api.start_notebook_agent_translation

::: co_op_translator.api.finish_notebook_agent_translation

::: co_op_translator.api.rewrite_markdown_paths

::: co_op_translator.api.rewrite_notebook_paths

::: co_op_translator.api.MarkdownTranslationOptions

::: co_op_translator.api.NotebookTranslationOptions

::: co_op_translator.api.ImageTranslationOptions

::: co_op_translator.api.TranslationBaseline

::: co_op_translator.api.TranslationStateProvider

::: co_op_translator.api.TranslationUpdate

::: co_op_translator.api.run_translation

::: co_op_translator.api.translate_project

::: co_op_translator.api.run_review

## コンテンツ翻訳 API

コンテンツ翻訳 API は、エディタ拡張、MCP ツール、ノートブックプロセッサ、またはカスタムパイプラインなど、すでにメモリ内にコンテンツを持っている統合向けに設計されています。

| Function | Input | Output | File I/O | Notes |
| --- | --- | --- | --- | --- |
| `translate_markdown_content` | Markdown `str` | Markdown `str` | いいえ | 非同期。Markdown コンテンツのみを翻訳します。リンクの書き換え、メタデータの書き込み、免責事項の追加は行いません。 |
| `translate_notebook_content` | Notebook JSON `str` or `dict` | Notebook JSON `str` | いいえ | 非同期。Markdown セルを翻訳し、非-Markdown セルを保持します。リンクの書き換え、メタデータの書き込み、免責事項の追加は行いません。 |
| `translate_image_content` | 画像パス | `PIL.Image.Image` | ソース画像のみを読み取る | 同期。画像のテキストを抽出して翻訳し、レンダリング済みの画像を返します。翻訳された画像メタデータは保存しません。 |

`translate_markdown_content` と `translate_notebook_content` はオプションで `source_path` を受け取れます。パスは翻訳者へのコンテキストとして渡されます。呼び出し元は翻訳後のプロジェクト固有のパス書き換えの責任を負います。

```python
from co_op_translator.api import MarkdownTranslationOptions, translate_markdown_content

translated = await translate_markdown_content(
    document,
    "ko",
    MarkdownTranslationOptions(source_path="docs/guide.md"),
)
```

同じオプションは辞書として渡すこともできます:

```python
translated = await translate_markdown_content(
    document,
    "ko",
    {"source_path": "docs/guide.md"},
)
```

## エージェント支援翻訳 API

エージェント支援 API は Co-op Translator から設定された LLM プロバイダーを呼び出しません。ホストエージェントが翻訳できるように Markdown またはノートブックのチャンクを準備し、翻訳済みチャンクから最終コンテンツを再構築します。

| Function | Purpose |
| --- | --- |
| `start_markdown_agent_translation` | チャンク、プロンプト、再構築状態を含む自己完結型の Markdown ジョブを返します。 |
| `finish_markdown_agent_translation` | ジョブとホストエージェントが翻訳したチャンクから Markdown を再構築します。 |
| `start_notebook_agent_translation` | ホストエージェントによる翻訳用の Markdown セルのチャンクを含むノートブックジョブを返します。 |
| `finish_notebook_agent_translation` | コードセル、出力、メタデータを保持しながらノートブック JSON を再構築します。 |

このワークフローは主に MCP ホストを対象としています。Co-op Translator がプロバイダー呼び出しを管理する本番環境のリポジトリ翻訳が必要な場合は、`translate_markdown_content`、`translate_notebook_content`、または `run_translation` を使用してください。

## パス書き換え API

パス書き換え API は翻訳を行いません。呼び出し元がソースパス、翻訳後のターゲットパス、およびプロジェクトレイアウトを把握した後にリンクとフロントマターのパスを更新します。

| Function | Scope | Notes |
| --- | --- | --- |
| `rewrite_markdown_paths` | Markdown 本文とフロントマター | 翻訳対象に合わせて Markdown のリンクとサポートされているフロントマターのパスフィールドを書き換えます。 |
| `rewrite_notebook_paths` | ノートブック JSON の Markdown セル | 各 Markdown セルに Markdown のパス書き換えを適用し、非-Markdown セルはそのままにします。 |

引数 `policy` は、次のフィールドを持つ辞書である場合があります:

| Field | Required | Purpose |
| --- | --- | --- |
| `language_code` | Yes | Target language code, such as `"ko"` or `"pt-BR"`. |
| `root_dir` | No | Source project root. Defaults to `"."`. |
| `translations_dir` | No | Text translation output directory. Defaults to `translations` under `root_dir`. |
| `translated_images_dir` | No | Translated image output directory. Defaults to `translated_images` under `root_dir`. |
| `translation_types` | いいえ | 有効な翻訳タイプ。デフォルトは Markdown、ノートブック、および画像です。 |
| `lang_subdir` | いいえ | 各言語フォルダー内の任意のサブディレクトリ。 |

## プロジェクト翻訳パラメーター

| Parameter | Type | Default | Purpose |
| --- | --- | --- | --- |
| `language_codes` | `str` | 必須 | スペース区切りのターゲット言語コード（例: `"ko ja fr"`、または `"all"`）。エイリアスコードは正規の BCP 47 値に正規化されます。 |
| `root_dir` | `str` | `"."` | 単一の翻訳ターゲット用のプロジェクトルート。`root_dirs` または `groups` が指定されている場合は無視されます。 |
| `update` | `bool` | `False` | 選択した言語の既存の翻訳を削除して再作成します。 |
| `images` | `bool` | `False` | Include image translation. Requires Azure AI Vision configuration. |
| `markdown` | `bool` | `False` | Include Markdown translation. |
| `notebook` | `bool` | `False` | Include Jupyter notebook translation. |
| `debug` | `bool` | `False` | Enable debug logging. |
| `save_logs` | `bool` | `False` | DEBUG レベルのログファイルをルート `logs/` ディレクトリの下に保存します。 |
| `yes` | `bool` | `True` | プログラムおよびCIでの使用時にプロンプトを自動で確認します。 |
| `add_disclaimer` | `bool` | `False` | 翻訳されたMarkdownとノートブックに機械翻訳の注意書きを追加します。 |
| `translations_dir` | `str \| None` | `None` | テキスト翻訳の出力ディレクトリをカスタム指定します。相対パスは各ルートを基準に解決されます。 |
| `image_dir` | `str \| None` | `None` | 翻訳された画像の出力ディレクトリをカスタム指定します。相対パスは各ルートを基準に解決されます。 |
| `root_dirs` | `Iterable[str] \| None` | `None` | 同じ出力設定を共有する複数のルート。 |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | 明示的な `(root_dir, translations_dir)` のペア。`root_dirs` より優先されます。 |
| `repo_url` | `str \| None` | `None` | READMEの言語テーブルの説明をレンダリングするときに使用されるリポジトリのURL。 |
| `glossaries` | `Iterable[str] \| None` | `None` | 翻訳中に保持する用語集の用語。重複や空白の用語は正規化されます。 |
| `dry_run` | `bool` | `False` | ファイルを書き込まずに翻訳量を見積もり、移行動作をプレビューします。 |
| `translation_state_provider` | `TranslationStateProvider \| None` | `None` | 増分のMarkdown更新のためのオプショナルな受け入れベースラインおよび候補の永続化アダプタ。指定しない場合は既存のフルファイルの動作が維持されます。 |

## レビュー パラメーター

`run_review` は可能な限り `run_translation` のシグネチャを意図的に反映しており、オートメーションが翻訳ワークフローとレビュー ワークフローの間を最小限の分岐で切り替えられるようにします。

| パラメーター | 型 | デフォルト | 目的 |
| --- | --- | --- | --- |
| `language_codes` | `str \| Iterable[str]` | `"all"` | レビュー対象の言語フォルダ。スペース区切りの文字列およびイテラブルが受け付けられます。`"all"` は発見されたすべての翻訳言語をレビューします。 |
| `root_dir` | `str` | `"."` | 単一のレビュー対象のプロジェクトルート。`root_dirs` または `groups` が指定されている場合は無視されます。 |
| `markdown` | `bool` | `False` | Markdown と MDX のソースファイルを含めます。 |
| `notebook` | `bool` | `False` | Jupyter ノートブックのソースファイルを含めます。 |
| `images` | `bool` | `False` | 翻訳オプションとの整合性のために予約されています。画像へのリンク参照はMarkdownからチェックされます。 |
| `translations_dir` | `str \| None` | `None` | テキスト翻訳の出力ディレクトリをカスタム指定します。相対パスは各ルートを基準に解決されます。 |
| `root_dirs` | `Iterable[str] \| None` | `None` | 同じ出力設定を共有する複数のルート。 |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | 明示的な `(root_dir, translations_dir)` のペア。`root_dirs` より優先されます。 |
| `changed_from` | `str \| None` | `None` | レビューを変更されたソースファイルに限定するために使用するGit参照。 |
| `readme_only` | `bool` | `False` | 各ソースルート下の `README.md` のみをレビューします。ソースREADMEが存在しない場合は `ValueError` を発生させます。 |
| `output_format` | `str` | `"text"` | レビュー出力の形式。サポートされている値は `"text"` と `"github"` です。 |
| `fail_on_warnings` | `bool` | `False` | 警告をエラーに加えて失敗として扱います。 |
| `debug` | `bool` | `False` | デバッグロギングを有効にします。 |
| `save_logs` | `bool` | `False` | ルートの `logs/` ディレクトリの下にDEBUGレベルのログファイルを保存します。 |

`markdown`、`notebook`、`images` のいずれも設定されていない場合、APIは該当する箇所でMarkdown、ノートブック、および画像のリンク参照をレビューします。レビューはLLMプロバイダーを呼び出さず、APIキーを必要としません。

## 設定要件

プロバイダに依存する翻訳APIは、翻訳を行う前にプロバイダの設定が必要です：

- Markdown とノートブックの翻訳にはLLMプロバイダーが必要です。Azure OpenAI、OpenAI、またはAnthropicを設定してください。
- 画像の翻訳にはLLMプロバイダーに加えてAzure AI Visionが必要です。
- `run_translation` はプロジェクトの翻訳開始前に軽量の接続確認を実行します。
- エージェント支援の `start_*_agent_translation` および `finish_*_agent_translation` API はCo-op TranslatorのLLMプロバイダーを呼び出しません。ホストアプリケーションまたはMCPエージェントが準備されたチャンクを翻訳します。
- `rewrite_markdown_paths`、`rewrite_notebook_paths`、および `run_review` は決定論的であり、プロバイダーの資格情報を必要としません。

必要な Azure OpenAI の環境変数：

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

必要な OpenAI の環境変数：

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

必要な Anthropic の環境変数：

```bash
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

`ANTHROPIC_BASE_URL` と `ANTHROPIC_MAX_TOKENS` はオプションです。Co-op Translator 0.22.0 以降、Microsoft Agent Framework がすべてのプロバイダーのデフォルトのモデルクライアントです。`CO_OP_TRANSLATOR_MODEL_CLIENT="semantic-kernel"` を使用して一時的に Semantic Kernel を選択することはまだ可能ですが、その場合は非推奨警告が出ます；段階的削除計画については [設定](configuration.md#model-client-backend) を参照してください。

画像翻訳のために必要な Azure AI Vision の環境変数：

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

`run_review` は決定論的であり、LLMやAzure AI Visionの設定を必要としません。

## 動作に関する注意事項

- コンテンツ翻訳APIは翻訳とプロジェクトパスの書き換えを分離します。翻訳されたコンテンツでプロジェクト相対リンクをターゲットの場所向けに調整する必要がある場合は、`rewrite_markdown_paths` または `rewrite_notebook_paths` を明示的に呼び出してください。
- プロジェクトオーケストレーションAPIは、ファイル検出、書き込み、パス書き換え、メタデータ、クリーンアップ、オプションの注意書きなど、コンテンツ翻訳の周りにプロジェクト固有の挙動を追加します。
- `run_translation` はCLIで使用されるのと同じRich対応のレポーターを通じて進行状況と見積もりの要約を出力します。非対話的な出力ではプレーンテキストにフォールバックします。
- `dry_run=True` は仮想のREADME更新を使って見積もりを計算しますが、READMEや翻訳ファイルは書き込みません。
- `groups` は順次処理されます。作業開始前に単一の集計見積もりが出力されます。
- 画像翻訳が選択されている場合、Visionの設定が欠如していると翻訳開始前にエラーが発生します。
- 既存のエイリアスベースの言語フォルダは検出され、実行の一部として正規の言語フォルダ名へ移行することができます。
- `run_review` は翻訳済みファイルの欠如、欠如または古い翻訳メタデータ、破損したMarkdownのフロントマター/コードフェンス、無効な翻訳済みノートブックJSONで失敗します。
- `run_review` はデフォルトでローカルのMarkdownおよび画像リンクのターゲットが見つからない場合を警告として報告します。

## 内部呼び出し経路

APIはCLIで使用されるのと同じコア実装に委譲します：

翻訳：

1. `co_op_translator.api.translation.translate_markdown_content`、`translate_notebook_content`、または `translate_image_content` — メモリ内翻訳用。
2. `co_op_translator.api.translation.rewrite_markdown_paths` または `rewrite_notebook_paths` — 明示的なパス後処理用。
3. `co_op_translator.api.translation.run_translation` — フルプロジェクトオーケストレーション用。
4. `co_op_translator.config.Config`, `LLMConfig`, and `VisionConfig`.
5. `co_op_translator.core.project.ProjectTranslator`.
6. `co_op_translator.core.project.TranslationManager`.
7. Markdown、ノートブック、画像向けの集中したプロジェクト翻訳ミックスイン。
8. `co_op_translator.core` 配下の Markdown、ノートブック、テキスト、および画像の翻訳器。

レビュー：

1. `co_op_translator.api.review.run_review`
2. `co_op_translator.review.targets.build_review_targets`
3. `co_op_translator.review.runner.ReviewRunner`
4. `co_op_translator.review.checks` 配下の決定論的チェック

以下のクラスは保守担当者に役立ちますが、パッケージレベルの安定APIとしてはエクスポートされていません。

| クラス | モジュール | 責務 |
| --- | --- | --- |
| `ProjectTranslator` | `co_op_translator.core.project.project_translator` | プロジェクトレベルの翻訳、ディレクトリ管理、各言語ごとのメタデータ正規化、およびMarkdown、ノートブック、画像の翻訳器への委譲を調整します。 |
| `TranslationManager` | `co_op_translator.core.project.translation` | Markdown、ノートブック、画像、古さ検出、および翻訳メタデータの更新に関する非同期ファイル処理を実行します。 |
| `ProjectMarkdownTranslationMixin` | `co_op_translator.core.project.translation.project_markdown_translation` | Markdownファイルの読み取り、コンテンツ翻訳、パス書き換え、メタデータ、注意書き、および書き込みをオーケストレーションします。 |
| `ProjectNotebookTranslationMixin` | `co_op_translator.core.project.translation.project_notebook_translation` | ノートブックファイルの読み取り、Markdownセルの翻訳、パス書き換え、メタデータ、注意書き、および書き込みをオーケストレーションします。 |
| `ProjectImageTranslationMixin` | `co_op_translator.core.project.translation.project_image_translation` | ソース画像の検出、画像翻訳、出力パス、メタデータ、および書き込みをオーケストレーションします。 |
| `ProjectEvaluator` | `co_op_translator.core.project.project_evaluator` | 翻訳されたMarkdownのペアを見つけ、翻訳品質を評価し、低信頼度の修復ワークフローのために信頼度メタデータを読み取ります。 |
| `ReviewRunner` | `co_op_translator.review.runner` | ソースファイル、ターゲット言語、および設定された翻訳ルートにわたる決定論的なレビュー検査を調整します。 |
| `ReviewTarget` | `co_op_translator.review.targets` | あるソースルートと、そのルートに対してレビューされる翻訳出力ディレクトリを記述します。 |
| `LanguageFolderMigrator` | `co_op_translator.core.project.language_migrator` | レガシーなエイリアス言語フォルダを検出し、正規のBCP 47フォルダへの移行計画を準備します。 |
| `Config` | `co_op_translator.config.base_config` | `.env` ファイルを読み込み、必要な LLM とオプションの Vision プロバイダーが設定されているかを確認します。 |
| `LLMConfig` | `co_op_translator.config.llm_config.config` | Azure OpenAI、OpenAI、またはAnthropicを自動検出し、必要な環境変数を検証し、プロバイダーの接続確認を実行します。 |
| `VisionConfig` | `co_op_translator.config.vision_config.config` | Azure AI Vision の設定を検出し、画像翻訳のための接続確認を実行します。 |