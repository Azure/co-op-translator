<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c64ba65e091e5d87385490fa63a8f574",
  "translation_date": "2025-06-12T12:33:46+00:00",
  "source_file": "getting_started/command-line-guide/command-line-guide.md",
  "language_code": "ja"
}
-->
# Co-op Translator コマンドラインインターフェース（CLI）の使い方

## 前提条件

- **Python 3.10 以上**: Co-op Translator を実行するために必要です。

## 目次

1. [ルートディレクトリに '.env' ファイルを作成する](./create-env-file.md)
   - 選択した言語モデルサービスに必要なキーを含めます。
   - Azure Computer Vision のキーを省略するか `-md` を指定すると、翻訳は Markdown のみのモードで動作します。
1. [Co-op translator パッケージをインストールする](./install-package.md)
1. [Co-op Translator を使ってプロジェクトを翻訳する](./translator-your-project.md)

**免責事項**：  
本書類はAI翻訳サービス[Co-op Translator](https://github.com/Azure/co-op-translator)を使用して翻訳されました。正確性を期しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。原文の母国語版が正式な情報源として優先されるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じた誤解や誤訳について、当方は一切の責任を負いかねます。