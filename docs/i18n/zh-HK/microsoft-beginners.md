# Microsoft 初學者儲存庫

此頁面適用於 Microsoft 「For Beginners」儲存庫的維護者，這些儲存庫使用共享的「其他課程」README 區段。

大多數 Co-op Translator 使用者不需要這個頁面。

## 自動同步「其他課程」區段

在你的 README 中，於「其他課程」區段周圍加入這些標記：

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

每次 Co-op Translator 透過 CLI 或 GitHub Actions 執行時，會用打包好的範本替換標記之間的內容。

## 更新共享範本

範本來源位於：

```text
src/co_op_translator/templates/other_courses.md
```

要更新共享內容：

1. 編輯範本。
2. 向 Co-op Translator 開啟一個 pull request。
3. 變更發佈後，在目標儲存庫中執行 Co-op Translator。

## 稀疏檢出建議

當大型課程儲存庫包含大量翻譯輸出時，複製(clone) 可能會變得昂貴。你可以在產生的語言區段中加入這則建議：

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