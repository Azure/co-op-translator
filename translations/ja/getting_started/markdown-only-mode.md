<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9b1b247a8d0f1736459e0e9ede0d9c92",
  "translation_date": "2025-06-12T11:38:01+00:00",
  "source_file": "getting_started/markdown-only-mode.md",
  "language_code": "ja"
}
-->
# Markdownのみモードの使い方

## はじめに
Markdownのみモードは、プロジェクトのMarkdownコンテンツのみを翻訳するために設計されています。このモードでは画像の翻訳処理をスキップし、テキストコンテンツのみに注力するため、画像翻訳が不要な場合やComputer Vision関連の環境変数が設定されていない場合に最適です。

## 使用するタイミング
- Computer Vision関連の環境変数が設定されていない場合。
- 画像リンクを更新せずにテキストだけを翻訳したい場合。
- ユーザーが`-md`コマンドラインオプションを明示的に指定した場合。

## 有効化方法
Markdownのみモードを有効にするには、コマンドで`-md`オプションを使用します。例えば：
```
translate -l "ko" -md
```

または、Computer Vision関連の環境変数が設定されていない場合、`translate -l "ko"`を実行すると自動的にMarkdownのみモードに切り替わります。

```
translate -l "ko"
```

このコマンドはMarkdownコンテンツを韓国語に翻訳し、画像リンクは翻訳されたパスではなく元のパスのままにします。

## 動作
Markdownのみモードでは：
- 翻訳処理で画像翻訳のステップをスキップします。
- Markdown内の画像リンクは変更されず、元のパスのままです。

## 例
### 実行前
```markdown
![Image](../../../translated_images/image.aa98bae4d78871bb3b23ac9f938ff86539da4cd6fb4c52dafedc4665135c3d61.ja.png)
```
### Markdownのみモード使用後
```markdown
![Image](../../../translated_images/image.fc8708ffe1e1ca12c38822b1a382726da4b232025d1daa8a50ab75c8635d0c4a.ja.png)
```

## トラブルシューティング
- コマンドで`-md`オプションが正しく指定されているか確認してください。
- Computer Visionの環境変数が処理に影響を与えていないか確認してください。

## まとめ
Markdownのみモードは、画像リンクを変更せずにテキストコンテンツだけを翻訳する簡潔な方法を提供します。画像翻訳が不要な場合や、Computer Vision環境が整っていない環境での作業に特に便利です。

**免責事項**：  
本書類はAI翻訳サービス[Co-op Translator](https://github.com/Azure/co-op-translator)を使用して翻訳されています。正確性には努めておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知ください。原文の母国語版が正式な情報源とみなされます。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や誤訳についても、当方は責任を負いかねます。