<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9b1b247a8d0f1736459e0e9ede0d9c92",
  "translation_date": "2025-06-12T11:37:38+00:00",
  "source_file": "getting_started/markdown-only-mode.md",
  "language_code": "hk"
}
-->
# 使用 Markdown-Only 模式

## 介紹
Markdown-only 模式專門用來翻譯你項目中的 Markdown 內容。這個模式會跳過圖片翻譯的步驟，只專注於文字內容，非常適合不需要圖片翻譯，或是沒有設定 Computer Vision 相關環境變數的情況。

## 何時使用
- 當沒有設定 Computer Vision 相關的環境變數時。
- 當你只想翻譯文字內容，而不更新圖片連結時。
- 當使用者透過 `-md` 命令行選項明確指定時。

## 如何啟用
要啟用 Markdown-only 模式，請在命令中使用 `-md` 選項。例如：
```
translate -l "ko" -md
```

或者當沒有設定 Computer Vision 相關環境變數時，執行 `translate -l "ko"` 會自動切換到 Markdown-only 模式。

```
translate -l "ko"
```

此命令會將 Markdown 內容翻譯成韓文，並將圖片連結保持為原始路徑，而不會改成翻譯後的圖片路徑。

## 行為
在 Markdown-only 模式下：
- 翻譯過程會跳過圖片翻譯的步驟。
- Markdown 中的圖片連結保持不變，指向原始路徑。

## 範例
### 使用前
```markdown
![Image](../../../translated_images/image.aa98bae4d78871bb3b23ac9f938ff86539da4cd6fb4c52dafedc4665135c3d61.hk.png)
```
### 使用 Markdown-only 模式後
```markdown
![Image](../../../translated_images/image.fc8708ffe1e1ca12c38822b1a382726da4b232025d1daa8a50ab75c8635d0c4a.hk.png)
```

## 疑難排解
- 確認命令中正確指定了 `-md` 選項。
- 確認沒有任何 Computer Vision 環境變數影響流程。

## 結論
Markdown-only 模式提供一種簡化的方式來翻譯文字內容，而不會改動圖片連結。當不需要圖片翻譯或在缺乏 Computer Vision 環境的情況下，這個模式特別有用。

**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我哋盡力確保準確性，但請注意自動翻譯可能會有錯誤或不準確之處。原始文件嘅母語版本應被視為權威來源。對於重要資料，建議採用專業人手翻譯。因使用本翻譯而引致嘅任何誤會或誤解，我哋概不負責。