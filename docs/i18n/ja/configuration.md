# 構成

Co-op Translator は 1 つの言語モデル プロバイダーを必要とします。画像の翻訳にはさらに Azure AI Vision が必要です。

設定は環境変数から読み取られます。ローカルプロジェクトでは、プロジェクトのルートに `.env` ファイルを置いてください。

Azure リソースのセットアップについては [Azure AI のセットアップ](azure-ai-setup.md) を参照してください。

## ローカル実行環境のセットアップ

CLI をローカルで実行する前に仮想環境を使用してください。Co-op Translator は Python 3.11 から 3.14 をサポートしています。

通常の CLI 利用では、仮想環境内に公開パッケージをインストールしてください:

### Windows (PowerShell)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install co-op-translator
translate --help
```

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install co-op-translator
translate --help
```

### リポジトリの開発

リポジトリ開発では、代わりにプロジェクトルートから依存関係をインストールしてください:

```bash
poetry install
poetry run translate --help
```

CLI が利用可能になったら、`.env` に 1 つの言語モデルプロバイダーを設定してください。

## プロバイダーの選択

ツールは次の順でプロバイダーを自動検出します:

1. Azure OpenAI
2. OpenAI
3. Anthropic

翻訳にはプロバイダーの資格情報が必要です。`translate -l "ko" -md --dry-run` のようなプレビューを除きます。`migrate-links`、`co-op-review`、および `run_review` は決定論的なメンテナンス操作であり、プロバイダーの資格情報は不要です。

## モデルクライアントのバックエンド

Co-op Translator 0.22.0 以降、Azure OpenAI、OpenAI、Anthropic はデフォルトで Microsoft Agent Framework を使用します。通常の使用ではバックエンドの設定は不要です。

Semantic Kernel は互換性のために一時的に利用可能です。明示的に選択するには、次を設定してください:

```bash
CO_OP_TRANSLATOR_MODEL_CLIENT="semantic-kernel"
```

Semantic Kernel を使用すると非推奨の警告が出ます。パッケージは Semantic Kernel をオプションの依存関係に移行する予定で、0.23.0 で移行し、0.24.0 で統合を削除する予定です（互換性の結果およびユーザーのフィードバックに依存します）。Anthropic は `agent-framework` を必要とします; Anthropic で `semantic-kernel` を明示的に選択すると設定エラーになります。無効な値は、静かにフォールバックするのではなく、プロバイダ対応の翻訳器初期化時に失敗します。ロールアウトを追跡し、障害を [GitHub issue #543](https://github.com/Azure/co-op-translator/issues/543) で報告してください。

## Azure OpenAI

モデルが Azure AI Foundry または Azure OpenAI Service にデプロイされている場合は Azure OpenAI を使用してください。

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

接続確認は翻訳が開始される前にエンドポイント、API キー、API バージョン、デプロイメント名を使用します。

## OpenAI

OpenAI API を直接呼び出す場合は OpenAI を使用してください。

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

`OPENAI_CHAT_MODEL_ID` は必須です。翻訳器は API 呼び出しのために明示的なチャットモデルを必要とします。

デフォルトのセットアップでは `OPENAI_ORG_ID` と `OPENAI_BASE_URL` を未設定のままにしてください。アカウントに組織 ID が必要な場合のみ追加し、カスタムエンドポイントを使用する場合のみ base URL を追加してください。オプション設定のプレースホルダー値をコピーしないでください。

## Anthropic Claude

Claude API を直接呼び出す場合は Anthropic を使用してください。[Anthropic API キー](https://platform.claude.com/docs/en/get-started) を作成し、サポートされている [Claude モデル ID](https://platform.claude.com/docs/en/about-claude/models/model-ids-and-versions) を選択してください。

```bash
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

`ANTHROPIC_API_KEY` と `ANTHROPIC_MODEL` は必須です。`CO_OP_TRANSLATOR_MODEL_CLIENT` を設定する必要はありません; Agent Framework がデフォルトのバックエンドです。

Anthropic API では `ANTHROPIC_BASE_URL` を未設定にしてください。カスタムエンドポイントを使用する場合のみ設定してください。

`ANTHROPIC_MAX_TOKENS` のデフォルトは `8192` です。これは Meitei Mayek のようなトークン密度の高いスクリプトに余裕を残します。モデルや Anthropic 互換エンドポイントがそれを下回る出力を制限する場合は、値を小さくしてください。

## Azure AI Vision

画像翻訳では、ツールが画像からテキストを抽出してから設定された言語モデルが翻訳するために Azure AI Vision が必要です。Anthropic は抽出されたテキストを Azure OpenAI や OpenAI と同様に翻訳できます。

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

`-img`、`images=True`、またはコンテンツタイプフィルターがない場合に画像翻訳が選択されると、ツールは翻訳開始前に Vision の構成を検証します。

## 複数の認証情報セット

設定層は変数に同じインデックスを付与して複数の認証情報セットをサポートします:

```bash
AZURE_OPENAI_API_KEY_1="..."
AZURE_OPENAI_ENDPOINT_1="https://<resource-1>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME_1="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME_1="<deployment-1>"
AZURE_OPENAI_API_VERSION_1="2024-12-01-preview"

AZURE_OPENAI_API_KEY_2="..."
AZURE_OPENAI_ENDPOINT_2="https://<resource-2>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME_2="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME_2="<deployment-2>"
AZURE_OPENAI_API_VERSION_2="2024-12-01-preview"
```

各セットは完全でなければなりません。ヘルスチェックは翻訳が進行する前に動作するセットを選択します。

OpenAI と Anthropic は同じサフィックス慣例をサポートします。`OPENAI_BASE_URL_1` や `ANTHROPIC_BASE_URL_1` のようなオプション値を含め、認証情報セット内のすべての変数を同じサフィックスにしてください。

## コマンドの要件

| Command or API | LLM required | Vision required | Notes |
| --- | --- | --- | --- |
| `translate -md` | はい | いいえ | Markdown のみを翻訳します。 |
| `translate -nb` | はい | いいえ | ノートブックのみを翻訳します。 |
| `translate -img` | はい | はい | 画像のみを翻訳します。 |
| `translate` with no type flags | はい | はい | デフォルトモードは Markdown、ノートブック、画像を含みます。 |
| `evaluate` | はい | いいえ | `--fast` が選択されていない限り LLM 評価を使用します。 |
| `migrate-links` | いいえ | いいえ | プロバイダー呼び出しなしでローカルリンクの移行を行います。 |
| `co-op-review` | いいえ | いいえ | 決定論的な翻訳構造、新鮮さ、Markdown、ノートブック、およびローカルリンクのチェックを実行します。 |
| `run_translation(markdown=True)` | はい | いいえ | プログラムによる Markdown 翻訳。 |
| `run_translation(images=True)` | はい | はい | プログラムによる画像翻訳。 |
| `run_review(...)` | いいえ | いいえ | プログラムによる決定論的レビュー。 |

## 出力ディレクトリ

デフォルトのテキスト翻訳出力:

```text
translations/<language-code>/<source-relative-path>
```

デフォルトの翻訳済み画像出力:

```text
translated_images/<language-code>/<source-relative-path>
```

Python API は `translations_dir` と `image_dir` でこれらのディレクトリを上書きできます。