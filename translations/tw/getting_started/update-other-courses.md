<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "93a7150216aa3c2d191135358fa6dd21",
  "translation_date": "2025-11-30T13:38:40+00:00",
  "source_file": "getting_started/update-other-courses.md",
  "language_code": "tw"
}
-->
# 更新「其他課程」區塊（Microsoft 初學者資源庫）

本指南說明如何使用 Co-op Translator 自動同步「其他課程」區塊，以及如何更新所有資源庫的全域範本。

- 適用範圍：僅限 Microsoft 初學者資源庫
- 適用工具：Co-op Translator CLI 與 GitHub Actions
- 範本來源：[src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## 快速開始：在你的資源庫啟用自動同步

在 README 中的「其他課程」區塊周圍加入以下標記。Co-op Translator 每次執行時都會替換這些標記之間的內容。

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

每次 Co-op Translator 執行時（無論是透過 CLI，例如 `translate -l "<language codes>"`，或是 GitHub Actions），都會自動更新這些標記包圍的「其他課程」區塊。

> [!NOTE]
> 如果你已有現成的清單，只要用相同的標記包起來即可。下一次執行時會自動替換成最新的標準化內容。

---

## 如何修改全域內容

如果你想更新所有初學者資源庫中統一顯示的標準內容：

1. 編輯範本檔案：[src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)
2. 將修改內容提交至 Co-op Translator 資源庫，並開啟 Pull Request
3. PR 合併後，Co-op Translator 的版本會更新
4. 下一次 Co-op Translator 在目標資源庫執行（CLI 或 GitHub Action）時，會自動同步更新後的區塊

這樣就能確保所有初學者資源庫的「其他課程」內容有唯一且一致的來源。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於確保翻譯的準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤譯負責。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->