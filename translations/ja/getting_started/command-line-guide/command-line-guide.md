<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d8eec418d6325416b9fab19a2dfcbf41",
  "translation_date": "2025-05-06T17:51:48+00:00",
  "source_file": "getting_started/command-line-guide/command-line-guide.md",
  "language_code": "ja"
}
-->
# Co-op Translator コマンドラインインターフェース（CLI）の使い方

## 前提条件

- **Python 3.10以上**：Co-op Translator を実行するために必要です。
- **言語モデルリソース**：  
  - **Azure OpenAI** またはその他のLLM。詳細は [supported models and services](../../../../README.md) を参照してください。
- **コンピュータビジョンリソース**（任意）：  
  - 画像翻訳用。利用できない場合、翻訳は [Markdown-only mode](../markdown-only-mode.md) に切り替わります。  
  - **Azure Computer Vision**

### 初期設定

始める前に、以下のリソースを準備してください。

- [Azure OpenAI のセットアップ](../set-up-resources/set-up-azure-openai.md)  
- [Azure Computer Vision のセットアップ](../set-up-resources/set-up-azure-computer-vision.md)（任意）

## 目次

1. [ルートディレクトリに '.env' ファイルを作成する](./create-env-file.md)  
   - 選択した言語モデルサービスの必要なキーを含めてください。  
   - Azure Computer Vision のキーが省略されているか `-md` が指定されている場合、翻訳は Markdown-only モードで動作します。  
3. [Co-op translator パッケージをインストールする](./install-package.md)  
4. [Co-op Translator を使ってプロジェクトを翻訳する](./translator-your-project.md)

**免責事項**：  
本書類はAI翻訳サービス[Co-op Translator](https://github.com/Azure/co-op-translator)を使用して翻訳されました。正確性を期していますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。原文の言語によるオリジナル文書が権威ある情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の使用により生じた誤解や誤訳について、当方は一切の責任を負いません。