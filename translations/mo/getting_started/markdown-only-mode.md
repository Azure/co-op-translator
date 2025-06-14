<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9b1b247a8d0f1736459e0e9ede0d9c92",
  "translation_date": "2025-06-14T12:49:17+00:00",
  "source_file": "getting_started/markdown-only-mode.md",
  "language_code": "mo"
}
-->
# 使用純 Markdown 模式

## 介紹
純 Markdown 模式專為翻譯項目的 Markdown 內容而設計。此模式跳過圖像翻譯過程，僅專注於文字內容，非常適合不需要圖像翻譯或未設置計算機視覺相關環境變數的情況。

## 何時使用
- 當計算機視覺相關環境變數未配置時。
- 當您只想翻譯文字內容而不更新圖像鏈接時。
- 當用戶通過 `-md` 命令行選項明確指定時。

## 如何啟用
要啟用純 Markdown 模式，請在命令中使用 `-md` 選項。例如：
```
translate -l "ko" -md
```

或者如果計算機視覺相關環境變數未配置。運行 `translate -l "ko"` 將自動切換到純 Markdown 模式。

```
translate -l "ko"
```

此命令將 Markdown 內容翻譯成韓文，並將圖像鏈接更新為其原始路徑，而不是修改為翻譯後的圖像路徑。

## 行為
在純 Markdown 模式中：
- 翻譯過程會跳過圖像翻譯步驟。
- Markdown 中的圖像鏈接保持不變，指向其原始路徑。

## 範例
### 之前
```markdown
![Image](../../../translated_images/image.aa98bae4d78871bb3b23ac9f938ff86539da4cd6fb4c52dafedc4665135c3d61.mo.png)
```
### 使用純 Markdown 模式後
```markdown
![Image](../../../translated_images/image.fc8708ffe1e1ca12c38822b1a382726da4b232025d1daa8a50ab75c8635d0c4a.mo.png)
```

## 疑難排解
- 確保在命令中正確指定了 `-md` 選項。
- 驗證是否有計算機視覺環境變數干擾了該過程。

## 結論
純 Markdown 模式提供了一種簡化的方法來翻譯文字內容而不修改圖像鏈接。當圖像翻譯不必要或在缺乏計算機視覺設置的環境中工作時，它特別有用。

**免責聲明**：
本文檔是使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯的。我們努力追求準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。應將原始語言的文件視為權威來源。對於關鍵信息，建議使用專業人工翻譯。對於因使用本翻譯而產生的任何誤解或誤釋，我們不承擔責任。