# Microsoft 初學者 儲存庫

本頁面是給使用共用 "Other Courses" README 區段之 Microsoft "For Beginners" 儲存庫的維護者。

大多數 Co-op Translator 的使用者不需要此頁面。

## 自動同步 "Other Courses" 區段

請在 README 中的 "Other Courses" 區段周圍加入這些標記：

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

Each time Co-op Translator runs through the CLI or GitHub Actions, it replaces the content between the markers with the packaged template.

## 更新共用範本

範本來源位於：

```text
src/co_op_translator/templates/other_courses.md
```

To update the shared content:

1. 編輯範本。
2. 向 Co-op Translator 提交 pull request。
3. 變更發布後，在目標儲存庫中執行 Co-op Translator。

## 稀疏檢出 注意事項

當大型課程儲存庫包含許多翻譯輸出時，複製整個儲存庫的成本可能會很高。您可以在產生的語言區段中包含此建議：

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