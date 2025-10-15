<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3fd2055f97f093b6fe102ea24df4458b",
  "translation_date": "2025-10-15T04:22:53+00:00",
  "source_file": "AGENTS.md",
  "language_code": "ja"
}
-->
## プロジェクト概要

Co‑op Translatorは、Markdownファイル、Jupyterノートブック、画像内テキストを複数言語に翻訳するPythonコマンドラインツールおよびGitHub Actionsワークフローです。翻訳結果は言語ごとのフォルダーに整理され、元のコンテンツと同期を保ちます。プロジェクトはPoetry管理のライブラリとして構成され、CLIエントリーポイントを持っています。

### アーキテクチャ概要

- CLIエントリーポイント（`translate`, `migrate-links`, `evaluate`）は統一CLIを呼び出し、翻訳・リンク移行・評価フローに振り分けます。
- 設定ローダーは`.env`を読み込み、LLMプロバイダー（Azure OpenAIまたはOpenAI）と、必要に応じて画像テキスト抽出用のビジョンプロバイダー（Azure AI Service）を自動検出します。
- 翻訳コアはMarkdownとノートブックを処理し、`-img`使用時は画像からテキストを抽出します。
- 出力はテキストは`translations/<lang>/`、画像は`translated_images/`に整理され、元の構造を保持します。

### 主な技術・フレームワーク

- Python 3.10–3.12、パッケージ管理はPoetry
- CLI: `click`
- LLM/AI SDK: Azure OpenAI, OpenAI
- Vision: Azure AI Service (Computer Vision)
- HTTP・データ: `httpx`, `pydantic`
- 画像処理: `pillow`, `opencv-python`, `matplotlib`
- ツール: `pytest`, `black`, `ruff`

## セットアップコマンド

### 前提条件

- Python 3.10–3.12
- Azureサブスクリプション（任意、Azure AIサービス利用時）
- LLM/Vision API（例: Azure OpenAI/OpenAI, Azure AI Vision）へのインターネット接続

### オプションA: Poetry（推奨）

```bash
# From repository root
pip install poetry
poetry install

# Run any command via Poetry
poetry run translate --help
```

### オプションB: pip/venv

```bash
# Create & activate virtual environment
python -m venv .venv
# Windows
.venv\\Scripts\\activate
# Linux/macOS
# source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# (Optional) Editable install for local development
pip install -e .
```

## エンドユーザー利用方法

### Docker（公開イメージ）

```bash
# Pull public image from GHCR
docker pull ghcr.io/azure/co-op-translator:latest

# Run with current folder mounted and .env provided (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "fr es" -md

# PowerShell
docker run --rm -it --env-file .env -v ${PWD}:/work ghcr.io/azure/co-op-translator:latest -l "fr es" -md
```

補足:
- デフォルトのエントリーポイントは`translate`です。リンク移行には`--entrypoint migrate-links`で上書きしてください。
- GHCRパッケージの可視性をPublicに設定し、匿名pullを許可してください。

### CLI（pip）

```bash
pip install co-op-translator
translate -l "fr es" -md
```

### 環境設定

リポジトリのルートに`.env`ファイルを作成し、選択した言語モデルや（必要に応じて）ビジョンサービスの認証情報・エンドポイントを記載してください。プロバイダーごとの詳細は`getting_started/set-up-azure-ai.md`を参照してください。

### 必須環境変数

少なくとも1つのLLMプロバイダーの設定が必要です。画像翻訳にはAzure AI Serviceの設定も必要です。

- Azure OpenAI（テキスト翻訳）:
  - `AZURE_OPENAI_API_KEY`
  - `AZURE_OPENAI_ENDPOINT`
  - `AZURE_OPENAI_MODEL_NAME`
  - `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME`
  - `AZURE_OPENAI_API_VERSION`

- OpenAI（テキスト翻訳の代替）:
  - `OPENAI_API_KEY`
  - `OPENAI_ORG_ID`（任意）
  - `OPENAI_CHAT_MODEL_ID`（OpenAIプロバイダー利用時必須）
  - `OPENAI_BASE_URL`（任意、デフォルトは`https://api.openai.com/v1`）

- Azure AI Service（画像テキスト抽出、`-img`利用時必須）:
  - `AZURE_AI_SERVICE_API_KEY`（推奨）または従来の`AZURE_SUBSCRIPTION_KEY`
  - `AZURE_AI_SERVICE_ENDPOINT`

`.env`例:

```bash
# Azure AI Service (for image translation)
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<your-ai-service>.cognitiveservices.azure.com/"

# Azure OpenAI (primary option)
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<your-azure-openai>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<your-deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"

# OpenAI (alternative option)
OPENAI_API_KEY="..."
OPENAI_ORG_ID="..."            # optional
OPENAI_CHAT_MODEL_ID="gpt-4o"   # required when using OpenAI
OPENAI_BASE_URL="https://api.openai.com/v1" # optional
```

補足:

- ツールは利用可能なLLMプロバイダーを自動検出します。Azure OpenAIまたはOpenAIのいずれかを設定してください。
- 画像翻訳には`AZURE_AI_SERVICE_API_KEY`と`AZURE_AI_SERVICE_ENDPOINT`の両方が必要です。
- 必須変数が不足している場合、CLIは明確なエラーを表示します。

## 開発ワークフロー

- ソースコードは`src/co_op_translator`、テストは`tests/`に配置します。
- 主なCLI（エントリーポイント経由でインストール）:

```bash
# Translate content to one or more languages (space‑separated codes)
translate -l "fr es de"

# Restrict by content type
translate -l "ja" -md            # only Markdown
translate -l "ko" -nb            # only notebooks
translate -l "zh" -md -img       # Markdown + images

# Update links in previously translated notebooks/Markdown
migrate-links -l "all" -y
```

詳細な利用方法は`getting_started/`を参照してください。

## テスト手順

リポジトリのルートからテストを実行します。一部のテストはAPI認証情報が必要な場合があります。必要に応じてスキップしてください。

```bash
# Run full test suite
pytest

# Skip tests that require live API keys
pytest -m "not api_key_required"

# Run a subset
pytest tests/co_op_translator -k "name_substring"
```

カバレッジ（`coverage`が必要）:

```bash
coverage run -m pytest -m "not api_key_required"
coverage html  # outputs to ./htmlcov
```

## コードスタイルガイドライン

- フォーマッター: Black（`pyproject.toml`で設定、行長88）
- リンター: Ruff（`pyproject.toml`で設定、行長120）
- 型チェック: mypy（設定済み、インストール時有効）

コマンド例:

```bash
# Via Poetry
poetry run black .
poetry run ruff check .
poetry run ruff check . --fix   # safe auto‑fixes

# Or with global tools
black .
ruff check .
```

Pythonソースは`src/`、テストは`tests/`に整理し、パッケージ名前空間（`co_op_translator.*`）で明示的なインポートを推奨します。

## ビルド・デプロイ

ビルド成果物は`dist/`に出力されます。

```bash
# Build (Poetry)
poetry build

# Local install of the built wheel
pip install dist/*.whl
```

GitHub Actionsによる自動化に対応しています。詳細は以下を参照してください:

- `getting_started/github-actions-guide/github-actions-guide-public.md`
- `getting_started/github-actions-guide/github-actions-guide-org.md`

### コンテナイメージ（GHCR）

- 公式イメージ: `ghcr.io/azure/co-op-translator:<tag>`
- タグ: `latest`（main）、`vX.Y.Z`などのセマンティックタグ、`sha`タグ
- マルチアーチ: Buildxで`linux/amd64, linux/arm64`対応
- Dockerfileパターン: ビルダーで依存ホイールを作成（`build-essential`と`python3-dev`）、ランタイムでローカルホイールハウスからインストール（`pip install --no-index --find-links=/wheels`）
- ワークフロー: `.github/workflows/docker-publish.yml`でGHCRへビルド・プッシュ

## セキュリティに関する注意

- APIキーやエンドポイントは`.env`やCIのシークレットストアに保管し、絶対にコミットしないでください。
- 画像翻訳にはAzure AI Visionのキー・エンドポイントが必要です。不要な場合は`-img`を省略してください。
- 大量翻訳時はプロバイダーのクォータやレート制限を事前に確認してください。

## プルリクエストガイドライン

### 提出前のチェック

1. **変更のテスト:**
   - 影響するノートブックを全て実行
   - 全セルがエラーなく実行できることを確認
   - 出力内容が適切か確認

2. **ドキュメント更新:**
   - 新しい概念追加時は`README.md`を更新
   - 複雑なコードにはノートブック内にコメントを追加
   - Markdownセルで目的を説明

3. **ファイル変更:**
   - `.env`ファイルはコミットせず（`.env.example`を利用）
   - `venv/`や`__pycache__/`ディレクトリはコミットしない
   - コンセプト説明のためのノートブック出力は残す
   - 一時ファイルやバックアップノートブック（`*-backup.ipynb`）は削除

4. **スタイル・フォーマット:**
   - スタイル・フォーマットガイドラインに従う
   - `poetry run black .`と`poetry run ruff check .`でスタイル・フォーマットを確認

5. **テスト・CLIヘルプの追加/更新:**
   - 挙動変更時はテストを追加・更新
   - CLIヘルプも変更内容に合わせて更新


### コミットメッセージ・マージ戦略

Squash and Mergeをデフォルトとしています。最終的なsquashコミットメッセージは以下の形式に従ってください:

```bash
<type>: <description> (#<PR number>)
```

許可されるタイプ:
- `Docs` — ドキュメント更新
- `Build` — ビルドシステム、依存関係、設定/CI
- `Core` — コア機能・機能追加（例: `src/co_op_translator/core`）

例:
- `Docs: インストール手順を明確化 (#50)`
- `Core: 画像翻訳の処理を改善 (#60)`

補足:
- PRタイトルはラベルに基づき自動でプレフィックスされることがあります。生成されたプレフィックスが正しいか確認してください。

### PRタイトル形式

明確で簡潔なタイトルを使用してください。最終squashコミットと同じ構成を推奨します:
- `Docs: インストール手順を明確化`
- `Core: 画像翻訳の処理を改善`

## デバッグ・トラブルシューティング

- よくある問題と対処法: `getting_started/troubleshooting.md`
- 対応言語と注意事項（フォント・既知の問題含む）: `getting_started/supported-languages.md`
- ノートブックのリンク問題は`migrate-links -l "all" -y`で再実行してください

## エージェント向け注意事項

- 再現性のある環境にはPoetryを推奨します。難しい場合は`requirements.txt`を利用してください。
- CIでCLIを呼び出す際は、必要なシークレットを環境変数または`.env`注入で渡してください。
- モノレポ利用者向けには、このリポジトリは単独パッケージとして動作します。サブパッケージ連携は不要です。

- マルチアーチ対応: ARMユーザー（Apple Silicon/ARMサーバー）が対象の場合は`linux/arm64`を維持してください。そうでなければ`linux/amd64`のみでも問題ありません。
- コンテナ利用希望者には`README.md`のDockerクイックスタートを案内してください。Bash・PowerShell両方の例を記載し、引用符の違いに注意してください。

---

**免責事項**：
本書類は、AI翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性には努めておりますが、自動翻訳には誤りや不正確な表現が含まれる場合がありますのでご注意ください。原文（元の言語の文書）が正式な情報源となります。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や誤認についても、当方は責任を負いかねます。