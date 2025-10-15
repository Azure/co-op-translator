<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "510827ad22a2031a50838919c3594828",
  "translation_date": "2025-10-15T02:35:55+00:00",
  "source_file": "getting_started/command-line-guide/install-package.md",
  "language_code": "tw"
}
-->
# 安裝 Co-op Translator 套件

**Co-op Translator** 是一款命令列介面（CLI）工具，能協助你將專案中的所有 markdown 檔案和圖片翻譯成多種語言。本教學將引導你設定翻譯器並針對不同情境執行它。

### 建立虛擬環境

你可以使用 `pip` 或 `Poetry` 來建立虛擬環境。請在終端機輸入以下其中一個指令。

#### 使用 pip

```bash
python -m venv .venv
```

#### 使用 Poetry

```bash
poetry init
```

### 啟動虛擬環境

建立好虛擬環境後，你需要將它啟動。根據你的作業系統，步驟會有所不同。請在終端機輸入以下指令。

#### pip 和 Poetry 都適用

- Windows：

    ```bash
    .venv\Scripts\activate
    ```

- Mac/Linux：

    ```bash
    source .venv/bin/activate
    ```

#### 使用 Poetry

1. 如果你是用 Poetry 建立環境，請在終端機輸入以下指令來啟動它。

    ```bash
    poetry shell
    ```

### 安裝套件及必要套件

當你的虛擬環境建立並啟動後，下一步就是安裝所需的相依套件。

### 快速安裝

透過 pip 安裝 Co-Op Translator

```
pip install co-op-translator
```
或

透過 poetry 安裝
```
poetry add co-op-translator
```

#### 如果你是複製這個 repo，使用 pip（從 requirements.txt）

> [!NOTE]
> 如果你是用快速安裝方式安裝 co-op translator，請不要執行這個步驟。

1. 如果你使用 pip，請在終端機輸入以下指令。它會自動安裝 `requirements.txt` 檔案中指定的必要套件：

    ```bash
    pip install -r requirements.txt
    ```

#### 使用 Poetry（從 pyproject.toml）

1. 如果你使用 Poetry，請在終端機輸入以下指令。它會自動安裝 `pyproject.toml` 檔案中指定的必要套件：

    ```bash
    poetry install
    ```

---

**免責聲明**：
本文件是使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不精確之處。原始語言的文件應被視為具權威性的來源。對於重要資訊，建議採用專業人工翻譯。因使用本翻譯而產生的任何誤解或誤釋，我們概不負責。