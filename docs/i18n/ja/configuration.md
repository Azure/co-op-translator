# 設定

Co-op Translator は1つの言語モデルプロバイダーを必要とします。画像翻訳には追加で Azure AI Vision が必要です。

設定は環境変数から読み取られます。ローカルプロジェクトでは、プロジェクトルートに `.env` ファイルを置いてください。

Azure リソースのセットアップについては [Azure AI セットアップ](azure-ai-setup.md) を参照してください。

## Local runtime setup

ローカルで CLI を実行する前に仮想環境を使用してください。Co-op Translator は Python 3.10 から 3.12 をサポートしています。

通常の CLI 利用では、公開されているパッケージを仮想環境の中にインストールしてください:

=== "Windows"

    ```powershell
    python -m venv .venv
    .venv\Scripts\activate
    pip install co-op-translator
    translate --help
    ```

=== "macOS / Linux"

    ```bash
    python -m venv .venv
    source .venv/bin/activate
    pip install co-op-translator
    translate --help
    ```

リポジトリの開発を行う場合は、代わりにプロジェクトルートから依存関係をインストールしてください:

```bash
poetry install
poetry run translate --help
```

CLI が利用可能になったら、`.env` に1つの言語モデルプロバイダーを設定してください。

## Provider selection

ツールは以下の順序でプロバイダーを自動検出します:

1. Azure OpenAI
2. OpenAI

どちらのプロバイダーも設定されていない場合、`translate`、`evaluate`、`migrate-links`、および `run_translation` は設定検証の段階で失敗します。`co-op-review` と `run_review` は決定的なメンテナンスチェックであり、プロバイダーの認証情報は必要ありません。

## Azure OpenAI

モデルが Azure AI Foundry または Azure OpenAI Service にデプロイされている場合は Azure OpenAI を使用してください。

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

接続確認は、翻訳を開始する前にエンドポイント、API キー、API バージョン、およびデプロイメント名を使用して行われます。

## OpenAI

OpenAI API を直接呼び出す場合は OpenAI を使用してください。

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
OPENAI_ORG_ID="..."          # 任意
OPENAI_BASE_URL="..."        # 任意
```

`OPENAI_CHAT_MODEL_ID` は、トランスレーターが API 呼び出しのために明示的なチャットモデルを必要とするため、必須です。

## Azure AI Vision

画像翻訳は、ツールが画像からテキストを抽出してから翻訳を行うために Azure AI Vision を必要とします。

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

`-img`、`images=True`、またはコンテンツタイプフィルターがない状態で画像翻訳が選択された場合、翻訳を開始する前に Vision の構成を検証します。

## Multiple credential sets

設定レイヤーは、変数に同じインデックスを付与して複数の資格情報セットをサポートします:

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

各セットは完全でなければなりません。ヘルスチェックは翻訳を進める前に動作するセットを選択します。

## Command requirements

| Command or API | LLM required | Vision required | Notes |
| --- | --- | --- | --- |
| `translate -md` | Yes | No | Markdown のみを翻訳します。 |
| `translate -nb` | Yes | No | ノートブックのみを翻訳します。 |
| `translate -img` | Yes | Yes | 画像のみを翻訳します。 |
| `translate` with no type flags | Yes | Yes | デフォルトモードでは Markdown、ノートブック、および画像が含まれます。 |
| `evaluate` | Yes | No | `--fast` が選択されていない限り LLM による評価を使用します。 |
| `migrate-links` | Yes | No | リンクの移行を実行しますが、共有の構成チェックは引き続き実行します。 |
| `co-op-review` | No | No | 决定的な翻訳構造、鮮度、Markdown、ノートブック、およびローカルリンクのチェックを実行します。 |
| `run_translation(markdown=True)` | Yes | No | プログラムによる Markdown 翻訳。 |
| `run_translation(images=True)` | Yes | Yes | プログラムによる画像翻訳。 |
| `run_review(...)` | No | No | プログラムによる決定的なレビュー。 |

## Output directories

Default text translation output:

```text
translations/<language-code>/<source-relative-path>
```

Default translated image output:

```text
translated_images/<language-code>/<source-relative-path>
```

Python API は `translations_dir` と `image_dir` でこれらのディレクトリを上書きできます。