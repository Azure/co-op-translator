<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "93a7150216aa3c2d191135358fa6dd21",
  "translation_date": "2025-11-30T13:39:03+00:00",
  "source_file": "getting_started/update-other-courses.md",
  "language_code": "ja"
}
-->
# 「Other Courses」セクションの更新（Microsoft Beginners リポジトリ）

このガイドでは、Co-op Translator を使って「Other Courses」セクションを自動同期する方法と、すべてのリポジトリに適用されるグローバルテンプレートの更新方法を説明します。

- 対象：Microsoft Beginners リポジトリのみ
- 対応ツール：Co-op Translator CLI と GitHub Actions
- テンプレートのソース：[src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## クイックスタート：リポジトリで自動同期を有効にする

README の「Other Courses」セクションの周りに以下のマーカーを追加してください。Co-op Translator はこれらのマーカー間の内容を毎回の実行時に置き換えます。

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

Co-op Translator が CLI（例：`translate -l "<language codes>"`）や GitHub Actions 経由で実行されるたびに、このマーカーで囲まれた「Other Courses」セクションが自動的に更新されます。

> [!NOTE]
> 既にリストがある場合は、同じマーカーで囲むだけで構いません。次回の実行時に最新の標準化された内容に置き換えられます。

---

## グローバルコンテンツの変更方法

すべての Beginners リポジトリに表示される標準化された内容を更新したい場合は、以下の手順を行ってください：

1. テンプレートを編集する：[src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)
2. 変更内容を含むプルリクエストを Co-op Translator リポジトリに送る
3. PR がマージされると、Co-op Translator のバージョンが更新される
4. 対象リポジトリで次回 Co-op Translator（CLI または GitHub Actions）が実行されると、自動的に更新されたセクションが同期される

これにより、すべての Beginners リポジトリで「Other Courses」コンテンツの単一の信頼できる情報源が確立されます。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：  
本書類はAI翻訳サービス「Co-op Translator」（https://github.com/Azure/co-op-translator）を使用して翻訳されました。正確性の向上に努めておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。原文の言語による文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や誤訳についても、当方は責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->