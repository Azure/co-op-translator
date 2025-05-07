<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9b1b247a8d0f1736459e0e9ede0d9c92",
  "translation_date": "2025-05-06T17:43:18+00:00",
  "source_file": "getting_started/markdown-only-mode.md",
  "language_code": "ja"
}
-->
# Markdownのみモードの使用

## はじめに
Markdownのみモードは、プロジェクトのMarkdownコンテンツのみを翻訳するために設計されています。このモードは画像翻訳のプロセスをスキップし、テキストコンテンツにのみ注力するため、画像翻訳が不要な場合やComputer Visionに必要な環境変数が設定されていない場合に最適です。

## 使用するタイミング
- Computer Vision関連の環境変数が設定されていない場合。
- 画像リンクを更新せず、テキストコンテンツだけを翻訳したい場合。
- ユーザーが`-md`コマンドラインオプションで明示的に指定した場合。

## 有効化方法
Markdownのみモードを有効にするには、コマンドで`-md`オプションを使用します。例えば：
```
translate -l "ko" -md
```

または、Computer Vision関連の環境変数が設定されていない場合、`translate -l "ko"`を実行すると自動的にMarkdownのみモードに切り替わります。

```
translate -l "ko"
```

このコマンドはMarkdownの内容を韓国語に翻訳し、画像リンクは翻訳された画像パスに変更せず元のパスのままにします。

## 動作
Markdownのみモードでは：
- 翻訳プロセスで画像翻訳のステップをスキップします。
- Markdown内の画像リンクは変更されず、元のパスを指したままです。

## 例
### 変更前
```markdown
![Image](../../../getting_started/translated/path/to/image.png)
```
### Markdownのみモード使用後
```markdown
![Image](../../../getting_started/original/path/to/image.png)
```

## トラブルシューティング
- `-md`オプションがコマンドで正しく指定されているか確認してください。
- Computer Visionの環境変数がプロセスに干渉していないか確認してください。

## まとめ
Markdownのみモードは、画像リンクを変更せずにテキストコンテンツのみを翻訳する簡潔な方法を提供します。画像翻訳が不要な場合やComputer Visionのセットアップがない環境で特に役立ちます。

**免責事項**：  
本書類はAI翻訳サービス「[Co-op Translator](https://github.com/Azure/co-op-translator)」を使用して翻訳されました。正確性を期しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。正式な情報源としては、原文の原言語版を参照してください。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や解釈の相違についても、一切の責任を負いかねます。