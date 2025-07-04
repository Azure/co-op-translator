<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b38d8f042530a4bc872def7cb2c141cd",
  "translation_date": "2025-07-04T08:11:40+00:00",
  "source_file": "getting_started/command-reference.md",
  "language_code": "ja"
}
-->
# コマンドリファレンス
**Co-op Translator** CLIは、翻訳プロセスをカスタマイズするためのいくつかのオプションを提供します。

コマンド                                       | 説明
----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"                 | プロジェクトを指定された言語に翻訳します。例: translate -l "es fr de" はスペイン語、フランス語、ドイツ語に翻訳します。translate -l "all" を使用すると、サポートされているすべての言語に翻訳します。
translate -l "language_codes" -u              | 既存の翻訳を削除して再作成することで翻訳を更新します。警告: これにより、指定された言語の現在の翻訳がすべて削除されます。
translate -l "language_codes" -img            | 画像ファイルのみを翻訳します。
translate -l "language_codes" -md             | Markdownファイルのみを翻訳します。
translate -l "language_codes" -chk            | 翻訳されたファイルをエラーがないかチェックし、必要に応じて翻訳を再試行します。
translate -l "language_codes" -d              | 詳細なログを記録するデバッグモードを有効にします。
translate -l "language_codes" -r "root_dir"   | プロジェクトのルートディレクトリを指定します。
translate -l "language_codes" -f              | 画像翻訳に高速モードを使用します（品質と整合性に若干の影響を与えつつ最大3倍速でプロット）。
translate -l "language_codes" -y              | すべてのプロンプトを自動的に確認します（CI/CDパイプラインに便利）。
translate -l "language_codes" --help          | CLI内で利用可能なコマンドを示すヘルプ詳細。

### 使用例:

  1. デフォルトの動作（既存の翻訳を削除せずに新しい翻訳を追加する）:   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. 新しい韓国語の画像翻訳のみを追加（既存の翻訳は削除されない）:    translate -l "ko" -img

  3. すべての韓国語翻訳を更新（警告: これにより、既存の韓国語翻訳がすべて削除されてから再翻訳されます）:    translate -l "ko" -u

  4. 韓国語の画像のみを更新（警告: これにより、既存の韓国語画像がすべて削除されてから再翻訳されます）:    translate -l "ko" -img -u

  5. 他の翻訳に影響を与えずに韓国語のMarkdown翻訳を追加:    translate -l "ko" -md

  6. 翻訳されたファイルをエラーがないかチェックし、必要に応じて翻訳を再試行: translate -l "ko" -chk

  7. 翻訳されたファイルをエラーがないかチェックし、必要に応じて翻訳を再試行（Markdownのみ）: translate -l "ko" -chk -md

  8. 翻訳されたファイルをエラーがないかチェックし、必要に応じて翻訳を再試行（画像のみ）: translate -l "ko" -chk -img

  9. 画像翻訳に高速モードを使用:    translate -l "ko" -img -f

  10. デバッグモードの例: - translate -l "ko" -d: デバッグログを有効にします。

**免責事項**:
この文書はAI翻訳サービス[Co-op Translator](https://github.com/Azure/co-op-translator)を使用して翻訳されています。正確性を追求していますが、自動翻訳には誤りや不正確さが含まれる可能性があることにご注意ください。元の言語での文書が信頼できる情報源とみなされるべきです。重要な情報については、専門の人間による翻訳をお勧めします。この翻訳の使用に起因する誤解や誤解について、当社は責任を負いません。