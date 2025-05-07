<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b6d85d887d2664539a438dae5d0dfa50",
  "translation_date": "2025-05-06T17:56:18+00:00",
  "source_file": "getting_started/command-line-guide/install-package.md",
  "language_code": "tw"
}
-->
# 安裝 Co-op translator 套件

**Co-op Translator** 是一款命令列介面 (CLI) 工具，幫助你將專案中的所有 markdown 檔案和圖片翻譯成多種語言。本教學將引導你設定翻譯器並針對不同使用情境執行。

### 建立虛擬環境

你可以使用 `pip` 或 `Poetry` 來建立虛擬環境。在終端機中輸入以下其中一個指令。

#### 使用 pip

```bash
python -m venv .venv
```

#### 使用 Poetry

```bash
poetry init
```

### 啟動虛擬環境

建立虛擬環境後，需要將它啟動。步驟依作業系統不同而異。請在終端機輸入以下指令。

#### pip 與 Poetry 通用

- Windows：

    ```bash
    .venv\Scripts\activate
    ```

- Mac/Linux：

    ```bash
    source .venv/bin/activate
    ```

#### 使用 Poetry

1. 如果你是用 Poetry 建立虛擬環境，請在終端機輸入以下指令來啟動它。

    ```bash
    poetry shell
    ```

### 安裝套件與必要的相依套件

當虛擬環境設定並啟動完成後，下一步是安裝所需的依賴套件。

### 快速安裝

透過 pip 安裝 Co-Op Translator

```
pip install co-op-translator
```
或是

透過 poetry 安裝
```
poetry add co-op-translator
```

#### 使用 pip（從 requirements.txt）如果你是克隆此倉庫

![NOTE] 如果你是透過快速安裝安裝 co-op translator，請勿使用此方法。

1. 如果你使用 pip，請在終端機輸入以下指令。它會自動安裝 `requirements.txt` 檔案中指定的必要套件：

    ```bash
    pip install -r requirements.txt
    ```

#### 使用 Poetry（從 pyproject.toml）

1. 如果你使用 Poetry，請在終端機輸入以下指令。它會自動安裝 `pyproject.toml` 檔案中指定的必要套件：

    ```bash
    poetry install
    ```

**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於確保翻譯的準確性，但請注意自動翻譯可能會包含錯誤或不精確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議使用專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤譯負責。