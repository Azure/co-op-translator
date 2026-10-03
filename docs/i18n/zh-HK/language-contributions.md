# 為語言改進作出貢獻

你的語言知識可以幫助改善 Co-op Translator。從一個例子、一項建議修正和一段解釋開始，使用 [翻譯回饋表單](https://github.com/Azure/co-op-translator/issues/new?template=translation_feedback.yml)。你不需要編寫程式碼或為模型執行付費。

## 從回報到共同改進

1. 投稿者提供一段原文摘錄、其翻譯和上下文。
2. 語言審核者檢查意思、自然度，以及該建議是否依賴特定地區語言變體或課程。
3. 維護者判定修正應該放在來源課程、共用語言指示、術語設定，或翻譯程式碼中。
4. 若為共用規則，維護者會比較在回報範例和無關範例上變更前後的輸出。投稿者可在不自行執行工具的情況下檢視這些輸出。
5. 所得的 PR 會連結該回報並標註提供範例與審核的貢獻者。部署或在使用此資源的倉庫重新生成則為另一個步驟。

回報不會自動更改 prompt 或重新生成課程翻譯。課程特定的修正應保留在該課程的儲存庫中。不要假設手動編輯在後續重新翻譯時會被保留；請確認該工作流程的實際行為。

## 現有範例：日文 Markdown 連結

該 [日文指示檔案](https://github.com/Azure/co-op-translator/blob/main/src/co_op_translator/templates/language/ja.md) 告訴模型在保留 Markdown 語法和連結目的地的同時翻譯連結文字。例如，一個寫成 `[text](URL)` 的連結不應變成 `「text」（URL）`。

這是一個針對語言規則的重點範例，並輔以正確與不正確輸出的說明。它並非證明僅靠 prompt 指示就能保證 Markdown 會正確。

該 [Markdown prompt builder](https://github.com/Azure/co-op-translator/blob/main/src/co_op_translator/utils/markdown/prompts.py) 載入 `templates/language/<language_code>.md`，使用小寫且去頭尾空白的語言代碼。如無此檔案，則使用通用指示。這描述的是 Markdown prompt 的路徑；不要假設每個圖片或其他翻譯路徑都使用相同的指示。

該 [prompt tests](https://github.com/Azure/co-op-translator/blob/main/tests/co_op_translator/utils/markdown/test_prompts.py) 檢查是否包含日文指示。那是驗證 prompt 組裝，而非翻譯品質。

## 什麼應該放在語言規則中？

提出一個具體且可重複的修正，包含原文範例、預期行為，以及該規則不應套用的反例。保留意思、佔位符、程式碼、URL 與文件結構。避免將某個人的風格偏好或某門課程的術語變成普遍規則。

目前的 [詞彙表實作](https://github.com/Azure/co-op-translator/blob/main/src/co_op_translator/glossary.py) 可保護詞彙不被翻譯。它並不是一個源對目標的術語字典。在向貢獻者承諾之前，先討論新的術語行為。

## 社群範例：一則日文產品名稱回報

在 [report #527](https://github.com/Azure/co-op-translator/issues/527) 中，@hyoshioka0128 識別出一個日文翻譯將產品名稱 `Co-op Translator` 改成 `Co-op 翻訳`。該回報附上了受影響文件的連結和截圖，使問題容易定位。

投稿者亦連結了一個 [相關課程 PR](https://github.com/microsoft/AZD-for-beginners/pull/109)。在議題討論中，維護者已接納該回報並建議調查名稱變更的原因，包括術語保護、詞彙表行為，以及翻譯流程。

這展示了一則小回報如何支持對超出單一措辭修正的調查。這並非經驗證的前後比較結果，也不是證明上述日文 Markdown 連結指示修正了該產品名稱問題的證據。

你也可以用相同方式貢獻：分享原始文字、目前翻譯、建議修正，及其重要原因。必要時附上文件連結或截圖。你不需要在回報前診斷原因或撰寫 prompt。

## 採納規則前的驗證

在基線與候選測試中使用相同的來源範例、翻譯器修訂、供應者/模型與產生設定，唯一變更的應該是提議的指示。記錄實際的 prompt 變更與輸出；必要時重複範例以區分一致效果與輸出變異性。包含該回報失敗的範例、對比的上下文，及已正確翻譯的範例。

| 範例 | 原文/上下文 | 基線輸出 | 候選輸出 | 審核者評估 |
| --- | --- | --- | --- | --- |
| 回報的失敗案例 | 待收集 | 未執行 | 未執行 | 待定 |
| 反例 | 待收集 | 未執行 | 未執行 | 待定 |
| 未受影響的範例 | 待收集 | 未執行 | 未執行 | 待定 |

將結構不變量（structural invariants）與語言判斷分開檢查。成功載入 prompt 的測試並不是品質評估，而一個精確的預期句子也不是唯一有效的翻譯。如果缺少上下文、模型運行或語言審核，應將提案保留待定，而不是宣稱問題已修復。