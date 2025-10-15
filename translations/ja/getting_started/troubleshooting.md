<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6e626bef5ed78a1cc55b0dbf44f01d47",
  "translation_date": "2025-10-15T02:38:35+00:00",
  "source_file": "getting_started/troubleshooting.md",
  "language_code": "ja"
}
-->
# Microsoft Co-op Translator トラブルシューティングガイド

## 概要
Microsoft Co-Op Translator は、Markdown ドキュメントをシームレスに翻訳できる強力なツールです。このガイドでは、ツール使用時によくある問題の対処方法を説明します。

## よくある問題と解決策

### 1. Markdown タグの問題
**問題:** 翻訳後の Markdown ドキュメントの先頭に `markdown` タグが含まれており、正しく表示されない。

**解決策:** ファイルの先頭にある `markdown` タグを削除してください。これで Markdown ファイルが正しく表示されるようになります。

**手順:**
1. 翻訳後の Markdown（.md）ファイルを開く
2. ドキュメントの先頭にある `markdown` タグを探す
3. `markdown` タグを削除する
4. ファイルを保存する
5. ファイルを再度開き、正しく表示されるか確認する

### 2. 埋め込み画像のURLの問題
**問題:** 埋め込み画像のURLが言語ロケールと一致せず、画像が正しく表示されない、または表示されない。

**解決策:** 埋め込み画像のURLを確認し、言語ロケールが一致しているか確認してください。すべての画像は `translated_images` フォルダーにあり、画像ファイル名に言語ロケールタグが含まれています。

**手順:**
1. 翻訳後の Markdown ドキュメントを開く
2. 埋め込み画像とそのURLを確認する
3. 画像ファイル名の言語ロケールがドキュメントの言語と一致しているか確認する
4. 必要に応じてURLを修正する
5. ファイルを保存し、画像が正しく表示されるか確認する

### 3. 翻訳精度の問題
**問題:** 翻訳内容が正確でない、またはさらに編集が必要。

**解決策:** 翻訳後のドキュメントを見直し、必要に応じて修正してください。

**手順:**
1. 翻訳後のドキュメントを開く
2. 内容を丁寧に確認する
3. 必要な修正を加えて翻訳精度を高める
4. ファイルを保存する

## 4. パーミッションエラー（Redacted または 404）

画像やテキストが正しい言語に翻訳されず、-d デバッグモードで 401 エラーが発生する場合、これは典型的な認証失敗です。キーが無効、期限切れ、またはエンドポイントのリージョンと紐付いていない可能性があります。

co-op translator を [-d debug スイッチ](https://github.com/Azure/co-op-translator/blob/main/getting_started/command-reference.md) 付きで実行し、根本原因を特定してください。

- **エラーメッセージ**: `Access denied due to invalid subscription key or wrong API endpoint.`
- **考えられる原因**:
  - サブスクリプションキーがリクエストでマスクされている、または間違っている
  - AI Services Key または Subscription Key が **Azure AI Vision** ではなく、Translator や OpenAI など他の Azure リソースのものになっている

 **リソースタイプの確認**
  - [Azure Portal](https://portal.azure.com) または [Azure AI Foundry](https://ai.azure.com) でリソースが `Azure AI services` → `Vision` タイプであることを確認
  - キーが正しいか、正しいキーを使用しているか検証

## 5. 設定エラー（新しいエラーハンドリング）

新しい選択的翻訳システムでは、必要なサービスが未設定の場合に明確なエラーメッセージが表示されます。

### 5.1. 画像翻訳用 Azure AI Service 未設定

**問題:** 画像翻訳（`-img` フラグ）をリクエストしたが、Azure AI Service が正しく設定されていない。

**エラーメッセージ:**
```
Error: Image translation requested but Azure AI Service is not configured.
Please add AZURE_AI_SERVICE_API_KEY and AZURE_AI_SERVICE_ENDPOINT to your .env file.
Check Azure AI Service availability and configuration.
```

**解決策:**
1. **オプション1:** Azure AI Service を設定
   - `.env` ファイルに `AZURE_AI_SERVICE_API_KEY` を追加
   - `.env` ファイルに `AZURE_AI_SERVICE_ENDPOINT` を追加
   - サービスにアクセスできるか確認

2. **オプション2:** 画像翻訳リクエストを削除
   ```bash
   # Instead of: translate -l "ko" -img
   # Use: translate -l "ko" -md
   ```

### 5.2. 必須設定の不足

**問題:** 必要な LLM 設定が不足している。

**エラーメッセージ:**
```
Error: No language model configuration found.
Please configure either Azure OpenAI or OpenAI in your .env file.
```

**解決策:**
1. `.env` ファイルに以下のいずれかの LLM 設定があるか確認:
   - **Azure OpenAI**: `AZURE_OPENAI_API_KEY` と `AZURE_OPENAI_ENDPOINT`
   - **OpenAI**: `OPENAI_API_KEY`
   
   Azure OpenAI または OpenAI のどちらか一方のみ設定が必要です。

### 5.3. 選択的翻訳の混乱

**問題:** コマンドは成功したが、ファイルが翻訳されていない。

**考えられる原因:**
- ファイルタイプフラグ（`-md`, `-img`, `-nb`）の指定ミス
- プロジェクト内に該当ファイルが存在しない
- ディレクトリ構造が正しくない

**解決策:**
1. **デバッグモードを使用**して状況を確認:
   ```bash
   translate -l "ko" -md -d
   ```

2. **プロジェクト内のファイルタイプを確認**:
   ```bash
   # For markdown files
   find . -name "*.md" -not -path "./translations/*"
   
   # For notebooks
   find . -name "*.ipynb" -not -path "./translations/*"
   
   # For images
   find . -name "*.png" -o -name "*.jpg" -o -name "*.jpeg" -not -path "./translations/*"
   ```

3. **フラグの組み合わせを確認**:
   ```bash
   # Translate everything (default)
   translate -l "ko"
   
   # Translate specific types
   translate -l "ko" -md -img
   ```

## 6. 旧システムからの移行

### 6.1. Markdown のみモードの廃止

**問題:** 自動的な Markdown のみのフォールバックに依存したコマンドが期待通り動作しなくなった。

**旧動作:**
```bash
# This used to automatically switch to markdown-only mode
translate -l "ko"  # (when Azure AI Vision was not configured)
```

**新動作:**
```bash
# This now produces an error if image translation is requested but not configured
translate -l "ko" -img
```

**解決策:**
- **何を翻訳したいか明示的に指定**してください:
  ```bash
  translate -l "ko" -md        # Only markdown
  translate -l "ko" -md -img   # Markdown and images
  translate -l "ko"            # Everything (if all services configured)
  ```

### 6.2. 予期しないリンクの挙動

**問題:** 翻訳後のファイル内のリンクが予期しない場所を指している。

**原因:** 選択したファイルタイプによって動的にリンク処理が変わるため。

**解決策:**
1. **新しいリンクの挙動を理解する**:
   - `-nb` を含む: ノートブックのリンクは翻訳後バージョンを指す
   - `-nb` を含まない: ノートブックのリンクは元ファイルを指す
   - `-img` を含む: 画像リンクは翻訳後バージョンを指す
   - `-img` を含まない: 画像リンクは元ファイルを指す

2. **用途に合った組み合わせを選ぶ**:
   ```bash
   # All internal links point to translated versions
   translate -l "ko" -md -img -nb
   
   # Only markdown translated, other links point to originals
   translate -l "ko" -md
   ```

## 7. GitHub Action は実行されたが Pull Request（PR）が作成されない

**症状:** `peter-evans/create-pull-request` のワークフローのログに次のように表示される:

> Branch 'update-translations' is not ahead of base 'main' and will not be created

**主な原因:**
- **変更が検出されていない:** 翻訳ステップで差分が発生しなかった（リポジトリがすでに最新）
- **出力が無視されている:** `.gitignore` でコミットしたいファイル（例: `*.ipynb`, `translations/`, `translated_images/`）が除外されている
- **add-paths の不一致:** アクションに指定したパスが実際の出力先と一致していない
- **ワークフローのロジック/条件:** 翻訳ステップが早期終了した、または予期しないディレクトリに書き込んだ

**修正・確認方法:**
1. **出力が存在するか確認:** 翻訳後、`translations/` や `translated_images/` に新規/変更ファイルがあるかワークスペースを確認
   - ノートブックを翻訳する場合、`.ipynb` ファイルが `translations/<lang>/...` 配下に書き込まれているか確認
2. **.gitignore を見直す:** 生成された出力を無視しないようにする。以下は無視しないこと:
   - `translations/`
   - `translated_images/`
   - `*.ipynb`（ノートブック翻訳時）
3. **add-paths が出力と一致しているか確認:** 複数行で両方のフォルダーを含める:
   ```yaml
   with:
     add-paths: |
       translations/
       translated_images/
   ```
4. **デバッグ用に強制的にPRを作成:** 配線確認のため一時的に空コミットを許可:
   ```yaml
   with:
     commit-empty: true
   ```
5. **デバッグモードで実行:** translate コマンドに `-d` を追加し、検出・書き込みされたファイルを表示
6. **権限（GITHUB_TOKEN）:** コミットやPR作成のため、ワークフローに書き込み権限があるか確認:
   ```yaml
   permissions:
     contents: write
     pull-requests: write
   ```


## クイックデバッグチェックリスト

翻訳の問題をトラブルシュートする際は:

1. **デバッグモードを使う:** `-d` フラグで詳細ログを確認
2. **フラグを確認:** `-md`, `-img`, `-nb` が意図通りかチェック
3. **設定を確認:** `.env` ファイルに必要なキーがあるか確認
4. **段階的にテスト:** まず `-md` のみで試し、他のタイプを追加
5. **ファイル構造を確認:** ソースファイルが存在し、アクセス可能か確認

利用可能なコマンドやフラグの詳細は [コマンドリファレンス](./command-reference.md) を参照してください。

---

**免責事項**：
本書類は、AI翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性には努めておりますが、自動翻訳には誤りや不正確な表現が含まれる場合がありますのでご注意ください。原文（元の言語の文書）が正式な情報源となります。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用によって生じたいかなる誤解や誤認についても、当方は責任を負いかねます。