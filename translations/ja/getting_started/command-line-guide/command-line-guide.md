<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a5eb9b53c81804f04bc9456160e79940",
  "translation_date": "2025-05-07T13:59:05+00:00",
  "source_file": "getting_started/command-line-guide/command-line-guide.md",
  "language_code": "ja"
}
-->
# Co-op Translator コマンドラインインターフェース（CLI）の使い方

## 前提条件

- **Python 3.10以上**: Co-op Translatorを実行するために必要です。
- **言語モデルリソース**:  
  - **Azure OpenAI** またはその他のLLM。詳細は [supported models and services](../../../../README.md) を参照してください。
- **コンピュータビジョンリソース**（任意）:  
  - 画像翻訳用。利用できない場合、翻訳は [Markdown-only mode](../markdown-only-mode.md) に切り替わります。  
  - **Azure Computer Vision**

## 目次

1. [ルートディレクトリに '.env' ファイルを作成する](./create-env-file.md)  
   - 選択した言語モデルサービスに必要なキーを含めてください。  
   - Azure Computer Visionのキーが省略されているか`-md`が指定されている場合、翻訳はMarkdown-onlyモードで動作します。  
1. [Co-op translatorパッケージをインストールする](./install-package.md)  
1. [Co-op Translatorを使ってプロジェクトを翻訳する](./translator-your-project.md)

**免責事項**：  
本書類はAI翻訳サービス「[Co-op Translator](https://github.com/Azure/co-op-translator)」を使用して翻訳されています。正確性の向上に努めておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知おきください。原文の言語で記載されたオリジナル文書が権威ある情報源とみなされます。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や誤訳についても、当方は一切責任を負いかねます。