# Microsoft 初心者向けリポジトリ

このページは、共有の「Other Courses」READMEセクションを使用する Microsoft の「For Beginners」リポジトリのメンテナ向けです。

大半の Co-op Translator ユーザーはこのページを必要としません。

## 他のコースセクションを自動同期する

README の「Other Courses」セクションの周りにこれらのマーカーを追加してください:

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

Co-op Translator が CLI または GitHub Actions を通じて実行されるたびに、マーカーで囲まれた部分の内容をパッケージ化されたテンプレートに置き換えます。

## 共有テンプレートを更新する

テンプレートのソースは次の場所にあります:

```text
src/co_op_translator/templates/other_courses.md
```

共有コンテンツを更新するには:

1. テンプレートを編集します。
2. Co-op Translator に対してプルリクエストを開きます。
3. 変更がリリースされた後、ターゲットリポジトリで Co-op Translator を実行します。

## スパースチェックアウトに関する注意事項

多くの翻訳出力を含む大規模なコースリポジトリは、クローンする際にコストがかかることがあります。生成された言語セクションにこの注意事項を含めることができます:

```markdown
> **Prefer to Clone Locally?**
>
> This repository includes many language translations, which can significantly increase download size. To clone without translations, use sparse checkout:
>
> ```bash
> git clone --filter=blob:none --sparse https://github.com/org/repo.git
> cd repo
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
```