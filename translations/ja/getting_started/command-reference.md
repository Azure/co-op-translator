<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a6cddf5e9648ef0bba0de7eb07e74cf1",
  "translation_date": "2025-10-15T02:38:05+00:00",
  "source_file": "getting_started/command-reference.md",
  "language_code": "ja"
}
-->
# コマンドリファレンス

**Co-op Translator** CLIは、翻訳プロセスをカスタマイズするためのさまざまなオプションを提供しています。

コマンド                                       | 説明
----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"                 | プロジェクトを指定した言語に翻訳します。例: translate -l "es fr de" はスペイン語、フランス語、ドイツ語に翻訳します。translate -l "all" でサポートされているすべての言語に翻訳できます。
translate -l "language_codes" -u              | 既存の翻訳を削除して再作成し、翻訳を更新します。警告: 指定した言語の現在の翻訳がすべて削除されます。
translate -l "language_codes" -img            | 画像ファイルのみを翻訳します。
translate -l "language_codes" -md             | Markdownファイルのみを翻訳します。
translate -l "language_codes" -nb             | Jupyterノートブックファイル（.ipynb）のみを翻訳します。
translate -l "language_codes" --fix           | 過去の評価結果に基づき、信頼度が低いファイルを再翻訳します。
translate -l "language_codes" -d              | 詳細なログを表示するデバッグモードを有効にします。
translate -l "language_codes" --save-logs, -s | DEBUGレベルのログを <root_dir>/logs/ にファイル保存します（コンソールの表示は -d で制御）
translate -l "language_codes" -r "root_dir"   | プロジェクトのルートディレクトリを指定します
translate -l "language_codes" -f              | 画像翻訳の高速モードを使用します（最大3倍速で描画、品質と配置がやや低下する場合があります）。
translate -l "language_codes" -y              | すべてのプロンプトを自動的に承認します（CI/CDパイプラインに便利）
translate -l "language_codes" --help          | CLI内で利用可能なコマンドのヘルプ詳細を表示します
evaluate -l "language_code"                  | 特定の言語の翻訳品質を評価し、信頼度スコアを表示します
evaluate -l "language_code" -c 0.8           | カスタム信頼度しきい値で翻訳を評価します
evaluate -l "language_code" -f               | 高速評価モード（ルールベースのみ、LLMなし）
evaluate -l "language_code" -D               | 詳細評価モード（LLMベースのみ、より徹底的だが遅い）
evaluate -l "language_code" --save-logs, -s  | DEBUGレベルのログを <root_dir>/logs/ にファイル保存します
migrate-links -l "language_codes"             | 翻訳済みMarkdownファイルを再処理し、ノートブック（.ipynb）へのリンクを更新します。翻訳済みノートブックがあれば優先し、なければ元のノートブックにフォールバックできます。
migrate-links -l "language_codes" -r          | プロジェクトのルートディレクトリを指定します（デフォルト: 現在のディレクトリ）。
migrate-links -l "language_codes" --dry-run   | どのファイルが変更されるかを表示し、実際には書き込みません。
migrate-links -l "language_codes" --no-fallback-to-original | 翻訳済みノートブックがない場合、元のノートブックへのリンクを書き換えません（翻訳済みがある場合のみ更新）。
migrate-links -l "language_codes" -d          | 詳細なログを表示するデバッグモードを有効にします。
migrate-links -l "language_codes" --save-logs, -s | DEBUGレベルのログを <root_dir>/logs/ にファイル保存します
migrate-links -l "all" -y                      | すべての言語を処理し、警告プロンプトを自動的に承認します。

## 使用例

  1. デフォルト動作（既存の翻訳を削除せず新しい翻訳を追加）:   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. 新しい韓国語画像翻訳のみ追加（既存の翻訳は削除されません）:    translate -l "ko" -img

  3. 韓国語の翻訳をすべて更新（警告: 既存の韓国語翻訳がすべて削除されてから再翻訳されます）:    translate -l "ko" -u

  4. 韓国語画像のみ更新（警告: 既存の韓国語画像がすべて削除されてから再翻訳されます）:    translate -l "ko" -img -u

  5. 韓国語のMarkdown翻訳のみ新規追加（他の翻訳には影響しません）:    translate -l "ko" -md

  6. 過去の評価結果に基づき、信頼度が低い翻訳を修正: translate -l "ko" --fix

  7. 特定ファイルのみ（Markdown）の信頼度が低い翻訳を修正: translate -l "ko" --fix -md

  8. 特定ファイルのみ（画像）の信頼度が低い翻訳を修正: translate -l "ko" --fix -img

  9. 画像翻訳の高速モードを使用:    translate -l "ko" -img -f

  10. カスタムしきい値で信頼度が低い翻訳を修正: translate -l "ko" --fix -c 0.8

  11. デバッグモード例: - translate -l "ko" -d: デバッグログを有効化
  12. ログをファイル保存: translate -l "ko" -s
  13. コンソールDEBUGとファイルDEBUG: translate -l "ko" -d -s

  14. 韓国語翻訳のノートブックリンクを移行（翻訳済みノートブックがあればリンクを更新）:    migrate-links -l "ko"

  15. ドライランでリンクを移行（ファイル書き込みなし）:    migrate-links -l "ko" --dry-run

  16. 翻訳済みノートブックが存在する場合のみリンクを更新（元のノートブックにはフォールバックしない）:    migrate-links -l "ko" --no-fallback-to-original

  17. 確認プロンプト付きですべての言語を処理:    migrate-links -l "all"

  18. すべての言語を自動承認で処理:    migrate-links -l "all" -y
  19. migrate-linksのログをファイル保存:    migrate-links -l "ko ja" -s

### 評価の例

> [!WARNING]  
> **ベータ機能**: 評価機能は現在ベータ版です。この機能は翻訳済みドキュメントの評価のためにリリースされており、評価方法や詳細な実装は今後変更される可能性があります。

  1. 韓国語翻訳を評価: evaluate -l "ko"

  2. カスタム信頼度しきい値で評価: evaluate -l "ko" -c 0.8

  3. 高速評価（ルールベースのみ）: evaluate -l "ko" -f

  4. 詳細評価（LLMベースのみ）: evaluate -l "ko" -D

---

**免責事項**：
本書類は、AI翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性には努めておりますが、自動翻訳には誤りや不正確な表現が含まれる場合がありますのでご注意ください。原文（元の言語の文書）が正式な情報源となります。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用によって生じたいかなる誤解や誤認についても、当方は責任を負いかねます。