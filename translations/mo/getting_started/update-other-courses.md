<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "93a7150216aa3c2d191135358fa6dd21",
  "translation_date": "2025-11-30T13:37:56+00:00",
  "source_file": "getting_started/update-other-courses.md",
  "language_code": "mo"
}
-->
# 更新「其他課程」部分（Microsoft 初學者倉庫）

本指南說明如何使用 Co-op Translator 自動同步「其他課程」部分，以及如何更新所有倉庫的全局範本。

- 適用範圍：僅限 Microsoft 初學者倉庫
- 配合工具：Co-op Translator CLI 和 GitHub Actions
- 範本來源：[src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## 快速開始：在你的倉庫啟用自動同步

在 README 的「其他課程」部分周圍加入以下標記。Co-op Translator 每次執行時都會替換這些標記之間的所有內容。

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

每次 Co-op Translator 執行時—無論是透過 CLI（例如 `translate -l "<language codes>"`）或 GitHub Actions—都會自動更新這些標記包圍的「其他課程」部分。

> [!NOTE]
> 如果你已有現成的清單，只要用相同標記包起來即可。下一次執行時會用最新的標準化內容取代。

---

## 如何更改全局內容

如果你想更新所有初學者倉庫中顯示的標準化內容：

1. 編輯範本：[src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)
2. 向 Co-op Translator 倉庫提交拉取請求（PR）來包含你的更改
3. PR 合併後，Co-op Translator 版本會更新
4. 下一次 Co-op Translator 在目標倉庫執行（CLI 或 GitHub Action）時，會自動同步更新後的部分

這樣就能確保所有初學者倉庫的「其他課程」內容有唯一且一致的來源。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件係使用人工智能翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我哋致力於確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件以其母語版本為權威來源。對於重要資訊，建議採用專業人工翻譯。我哋對因使用本翻譯而引起嘅任何誤解或誤釋概不負責。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->