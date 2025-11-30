<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "822238e4451d04bb152cebb1be6f13c2",
  "translation_date": "2025-11-30T10:25:42+00:00",
  "source_file": "getting_started/command-reference.md",
  "language_code": "ja"
}
-->
# コマンドリファレンス

**Co-op Translator** CLI は、翻訳プロセスをカスタマイズするためのいくつかのオプションを提供します。

コマンド                                       | 説明
----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"                 | プロジェクトを指定した言語に翻訳します。例：translate -l "es fr de" はスペイン語、フランス語、ドイツ語に翻訳します。translate -l "all" を使うとサポートされているすべての言語に翻訳します。
translate -l "language_codes" -u              | 既存の翻訳を削除して再作成することで翻訳を更新します。警告：指定した言語の現在の翻訳はすべて削除されます。
translate -l "language_codes" -img            | 画像ファイルのみを翻訳します。
translate -l "language_codes" -md             | Markdownファイルのみを翻訳します。
translate -l "language_codes" -nb             | Jupyterノートブックファイル（.ipynb）のみを翻訳します。
translate -l "language_codes" --fix           | 以前の評価結果に基づき、信頼度の低い翻訳を再翻訳します。
translate -l "language_codes" -d              | 詳細なログを出力するデバッグモードを有効にします。
translate -l "language_codes" --save-logs, -s | DEBUGレベルのログを <root_dir>/logs/ 以下のファイルに保存します（コンソールのログは -d で制御）。
translate -l "language_codes" -r "root_dir"   | プロジェクトのルートディレクトリを指定します。
translate -l "language_codes" -f              | 画像翻訳に高速モードを使用します（品質や配置の精度を少し犠牲にして最大3倍速く描画）。
translate -l "language_codes" -y              | すべてのプロンプトを自動的に承認します（CI/CDパイプラインで便利）。
translate -l "language_codes" --add-disclaimer/--no-disclaimer | 翻訳されたMarkdownやノートブックに機械翻訳の免責事項セクションを追加するかどうかを切り替えます（デフォルトは有効）。
translate -l "language_codes" --help          | CLI内のヘルプ詳細を表示します。
evaluate -l "language_code"                  | 特定の言語の翻訳品質を評価し、信頼度スコアを提供します。
evaluate -l "language_code" -c 0.8           | カスタム信頼度閾値で翻訳を評価します。
evaluate -l "language_code" -f               | 高速評価モード（ルールベースのみ、LLMは使用しません）。
evaluate -l "language_code" -D               | 詳細評価モード（LLMベースのみ、より徹底的ですが遅い）。
evaluate -l "language_code" --save-logs, -s  | DEBUGレベルのログを <root_dir>/logs/ に保存します。
migrate-links -l "language_codes"             | 翻訳済みMarkdownファイルを再処理し、ノートブック（.ipynb）へのリンクを更新します。翻訳済みノートブックがあればそちらを優先し、なければ元のノートブックにフォールバックします。
migrate-links -l "language_codes" -r          | プロジェクトのルートディレクトリを指定します（デフォルトはカレントディレクトリ）。
migrate-links -l "language_codes" --dry-run   | 変更されるファイルを表示しますが、実際には書き込みません。
migrate-links -l "language_codes" --no-fallback-to-original | 翻訳済みノートブックがない場合に元のノートブックへのリンクを書き換えません（翻訳済みがある場合のみ更新）。
migrate-links -l "language_codes" -d          | 詳細なログを出力するデバッグモードを有効にします。
migrate-links -l "language_codes" --save-logs, -s | DEBUGレベルのログを <root_dir>/logs/ に保存します。
migrate-links -l "all" -y                      | すべての言語を処理し、警告プロンプトを自動承認します。

## 使用例

  1. デフォルト動作（既存の翻訳を削除せずに新しい翻訳を追加）：   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. 新しい韓国語の画像翻訳のみ追加（既存の翻訳は削除されません）：    translate -l "ko" -img

  3. すべての韓国語翻訳を更新（警告：既存の韓国語翻訳はすべて削除されてから再翻訳されます）：    translate -l "ko" -u

  4. 韓国語の画像のみ更新（警告：既存の韓国語画像はすべて削除されてから再翻訳されます）：    translate -l "ko" -img -u

  5. 他の翻訳に影響を与えずに韓国語のMarkdown翻訳のみ追加：    translate -l "ko" -md

  6. 以前の評価結果に基づき信頼度の低い翻訳を修正： translate -l "ko" --fix

  7. 特定ファイルのみ信頼度の低いMarkdown翻訳を修正： translate -l "ko" --fix -md

  8. 特定ファイルのみ信頼度の低い画像翻訳を修正： translate -l "ko" --fix -img

  9. 画像翻訳に高速モードを使用：    translate -l "ko" -img -f

  10. カスタム閾値で信頼度の低い翻訳を修正： translate -l "ko" --fix -c 0.8

  11. デバッグモードの例： - translate -l "ko" -d：デバッグログを有効化。
  12. ログをファイルに保存： translate -l "ko" -s
  13. コンソールとファイル両方にDEBUGログ： translate -l "ko" -d -s
  14. 出力に機械翻訳の免責事項を追加しないで翻訳： translate -l "ko" --no-disclaimer

  15. 韓国語翻訳のノートブックリンクを移行（翻訳済みノートブックへのリンクを更新）：    migrate-links -l "ko"

  15. dry-runでリンク移行（ファイルは書き換えません）：    migrate-links -l "ko" --dry-run

  16. 翻訳済みノートブックがある場合のみリンクを更新（元のノートブックには戻さない）：    migrate-links -l "ko" --no-fallback-to-original

  17. すべての言語を処理し、確認プロンプトを表示：    migrate-links -l "all"

  18. すべての言語を処理し、自動承認：    migrate-links -l "all" -y
  19. migrate-linksのログをファイルに保存：    migrate-links -l "ko ja" -s

### 評価の例

> [!WARNING]  
> **ベータ機能**：評価機能は現在ベータ版です。この機能は翻訳されたドキュメントを評価するためにリリースされており、評価方法や詳細な実装はまだ開発中で変更される可能性があります。

  1. 韓国語翻訳を評価： evaluate -l "ko"

  2. カスタム信頼度閾値で評価： evaluate -l "ko" -c 0.8

  3. 高速評価（ルールベースのみ）： evaluate -l "ko" -f

  4. 詳細評価（LLMベースのみ）： evaluate -l "ko" -D

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：  
本書類はAI翻訳サービス「Co-op Translator」（https://github.com/Azure/co-op-translator）を使用して翻訳されました。正確性の向上に努めておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。原文の言語によるオリジナル文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や誤訳についても、当方は責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->