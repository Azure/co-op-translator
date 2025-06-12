<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9b1b247a8d0f1736459e0e9ede0d9c92",
  "translation_date": "2025-06-12T11:37:51+00:00",
  "source_file": "getting_started/markdown-only-mode.md",
  "language_code": "tw"
}
-->
# 使用 Markdown-Only 模式

## 介紹
Markdown-only 模式專門用來翻譯專案中的 Markdown 內容。此模式會跳過圖片翻譯的步驟，只專注於文字內容，適合在不需要圖片翻譯或尚未設定 Computer Vision 環境變數的情況下使用。

## 何時使用
- 當未設定與 Computer Vision 相關的環境變數時。
- 當你只想翻譯文字內容，而不更新圖片連結時。
- 當使用者明確透過 `-md` 命令列選項指定時。

## 如何啟用
要啟用 Markdown-only 模式，請在命令中使用 `-md` 選項。例如：
```
translate -l "ko" -md
```

或者當未設定與 Computer Vision 相關的環境變數時，執行 `translate -l "ko"` 會自動切換到 Markdown-only 模式。

```
translate -l "ko"
```

此指令會將 Markdown 內容翻譯成韓文，並將圖片連結保留為原始路徑，而非改為翻譯後的圖片路徑。

## 行為
在 Markdown-only 模式下：
- 翻譯過程會跳過圖片翻譯步驟。
- Markdown 中的圖片連結保持不變，指向原始路徑。

## 範例
### 使用前
```markdown
![Image](../../../translated_images/image.aa98bae4d78871bb3b23ac9f938ff86539da4cd6fb4c52dafedc4665135c3d61.tw.png)
```
### 使用 Markdown-only 模式後
```markdown
![Image](../../../translated_images/image.fc8708ffe1e1ca12c38822b1a382726da4b232025d1daa8a50ab75c8635d0c4a.tw.png)
```

## 疑難排解
- 確認命令中有正確指定 `-md` 選項。
- 確認沒有與 Computer Vision 相關的環境變數干擾流程。

## 結論
Markdown-only 模式提供一種簡化的方式，讓你能翻譯文字內容而不更動圖片連結。當不需要圖片翻譯，或在缺乏 Computer Vision 設定的環境下，特別有用。

**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意自動翻譯可能包含錯誤或不精確之處。原始文件之母語版本應視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯所導致之任何誤解或誤釋負責。