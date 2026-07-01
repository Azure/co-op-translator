# Microsoft 初學者儲存庫

本頁面供維護使用共用 "Other Courses" README 區段的 Microsoft "For Beginners" 儲存庫之維護者使用。

大多數 Co-op Translator 使用者不需要此頁面。

## 自動同步「Other Courses」區段

請在你的 README 的 "Other Courses" 區段周圍加入這些標記：

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

每次 Co-op Translator 透過 CLI 或 GitHub Actions 執行時，都會將標記之間的內容替換為已封裝的範本。

## 更新共用範本

範本來源位於：

```text
src/co_op_translator/templates/other_courses.md
```

要更新共用內容：

1. 編輯範本。
2. 向 Co-op Translator 提交一個 pull request。
3. 變更發布後，在目標儲存庫中執行 Co-op Translator。

## Sparse Checkout 建議

當大型課程儲存庫包含大量翻譯輸出時，複製（clone）可能會變得很昂貴。你可以在產生的語言區段中加入此建議：

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