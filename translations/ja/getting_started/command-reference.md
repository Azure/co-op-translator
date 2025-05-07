<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b38d8f042530a4bc872def7cb2c141cd",
  "translation_date": "2025-05-06T17:40:35+00:00",
  "source_file": "getting_started/command-reference.md",
  "language_code": "ja"
}
-->
# コマンドリファレンス
**Co-op Translator** CLI は翻訳プロセスをカスタマイズするためのいくつかのオプションを提供します：

コマンド                                       | 説明
----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"                 | プロジェクトを指定した言語に翻訳します。例：translate -l "es fr de" はスペイン語、フランス語、ドイツ語に翻訳します。translate -l "all" を使うとサポートされているすべての言語に翻訳します。
translate -l "language_codes" -u              | 既存の翻訳を削除して再作成することで翻訳を更新します。警告：指定した言語のすべての現在の翻訳が削除されます。
translate -l "language_codes" -img            | 画像ファイルのみを翻訳します。
translate -l "language_codes" -md             | Markdown ファイルのみを翻訳します。
translate -l "language_codes" -chk            | 翻訳済みファイルのエラーをチェックし、必要に応じて翻訳を再試行します。
translate -l "language_codes" -d              | 詳細なログを表示するデバッグモードを有効にします。
translate -l "language_codes" -r "root_dir"   | プロジェクトのルートディレクトリを指定します。
translate -l "language_codes" -f              | 画像翻訳に高速モードを使用します（品質と配置に若干の影響がありますが最大3倍速く処理します）。
translate -l "language_codes" -y              | すべてのプロンプトを自動的に承認します（CI/CDパイプラインで便利です）。
translate -l "language_codes" --help          | 利用可能なコマンドの詳細をCLI内で表示します。

### 使用例：

  1. デフォルト動作（既存の翻訳を削除せずに新しい翻訳を追加）：   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. 新しい韓国語の画像翻訳のみを追加（既存の翻訳は削除されません）：    translate -l "ko" -img

  3. すべての韓国語翻訳を更新（警告：既存の韓国語翻訳をすべて削除してから再翻訳します）：    translate -l "ko" -u

  4. 韓国語の画像のみを更新（警告：既存の韓国語画像をすべて削除してから再翻訳します）：    translate -l "ko" -img -u

  5. 他の翻訳に影響を与えずに韓国語のMarkdown翻訳のみ追加：    translate -l "ko" -md

  6. 翻訳済みファイルのエラーをチェックし、必要に応じて再翻訳： translate -l "ko" -chk

  7. 翻訳済みファイルのエラーをチェックし、必要に応じて再翻訳（Markdownのみ）： translate -l "ko" -chk -md

  8. 翻訳済みファイルのエラーをチェックし、必要に応じて再翻訳（画像のみ）： translate -l "ko" -chk -img

  9. 画像翻訳に高速モードを使用：    translate -l "ko" -img -f

  10. デバッグモードの例： - translate -l "ko" -d: デバッグログを有効にします。

**免責事項**:  
本書類はAI翻訳サービス[Co-op Translator](https://github.com/Azure/co-op-translator)を使用して翻訳されています。正確性には努めておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。原文の言語によるオリジナルの文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の使用により生じた誤解や誤訳について、一切の責任を負いかねます。