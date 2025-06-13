<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b6d85d887d2664539a438dae5d0dfa50",
  "translation_date": "2025-06-12T18:32:16+00:00",
  "source_file": "getting_started/command-line-guide/install-package.md",
  "language_code": "tw"
}
-->
# 安裝 Co-op translator 套件

**Co-op Translator** 是一個命令列介面（CLI）工具，能協助你將專案中的所有 Markdown 檔案與圖片翻譯成多種語言。本教學將引導你設定翻譯器並針對不同使用情境執行。

### 建立虛擬環境

你可以使用 `pip` 或 `Poetry` 來建立虛擬環境。在終端機輸入以下其中一個指令。

#### 使用 pip

```bash
python -m venv .venv
```

#### 使用 Poetry

```bash
poetry init
```

### 啟用虛擬環境

建立虛擬環境後，需要將其啟用。根據你的作業系統，操作步驟會有所不同。在終端機輸入以下指令。

#### pip 與 Poetry 共用

- Windows：

    ```bash
    .venv\Scripts\activate
    ```

- Mac/Linux：

    ```bash
    source .venv/bin/activate
    ```

#### 使用 Poetry

1. 如果你是用 Poetry 建立環境，請在終端機輸入以下指令來啟用虛擬環境。

    ```bash
    poetry shell
    ```

### 安裝套件與所需依賴

虛擬環境設定並啟用後，接下來安裝所需的依賴套件。

### 快速安裝

透過 pip 安裝 Co-Op Translator

```
pip install co-op-translator
```
或者

透過 Poetry 安裝
```
poetry add co-op-translator
```

#### 使用 pip（從 requirements.txt）如果你是從此 repo 克隆

![NOTE] 如果你是使用快速安裝方式安裝 co-op translator，請不要使用此方法。

1. 如果你使用 pip，請在終端機輸入以下指令。它會自動安裝 `requirements.txt` 中指定的套件：

    ```bash
    pip install -r requirements.txt
    ```

#### 使用 Poetry（從 pyproject.toml）

1. 如果你使用 Poetry，請在終端機輸入以下指令。它會自動安裝 `pyproject.toml` 中指定的套件：

    ```bash
    poetry install
    ```

**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們對因使用本翻譯所引起的任何誤解或誤譯概不負責。