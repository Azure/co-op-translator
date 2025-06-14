<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b6d85d887d2664539a438dae5d0dfa50",
  "translation_date": "2025-06-14T12:50:27+00:00",
  "source_file": "getting_started/command-line-guide/install-package.md",
  "language_code": "mo"
}
-->
# 安裝 Co-op 翻譯器套件

**Co-op Translator** 是一個命令行介面（CLI）工具，旨在幫助您將項目中的所有 Markdown 文件和圖片翻譯成多種語言。本教程將指導您配置翻譯器並在各種使用情況下運行它。

### 創建虛擬環境

您可以使用 `pip` 或 `Poetry` 創建虛擬環境。在終端中輸入以下命令之一。

#### 使用 pip

```bash
python -m venv .venv
```

#### 使用 Poetry

```bash
poetry init
```

### 啟動虛擬環境

創建虛擬環境後，您需要啟動它。步驟因操作系統而異。在終端中輸入以下命令。

#### 適用於 pip 和 Poetry

- Windows:

    ```bash
    .venv\Scripts\activate
    ```

- Mac/Linux:

    ```bash
    source .venv/bin/activate
    ```

#### 使用 Poetry

1. 如果您使用 Poetry 創建環境，請在終端中輸入以下命令以啟動它。

    ```bash
    poetry shell
    ```

### 安裝套件和所需的套件

一旦您的虛擬環境設置並啟動，下一步就是安裝必要的依賴項。

### 快速安裝

通過 pip 安裝 Co-Op Translator

```
pip install co-op-translator
```
或者

通過 poetry 安裝
```
poetry add co-op-translator
```

#### 使用 pip（從 requirements.txt）如果您克隆此 repo

![NOTE] 如果您通過快速安裝安裝 co-op translator，請不要這樣做。

1. 如果您使用 pip，請在終端中輸入以下命令。它將自動安裝 `requirements.txt` 文件中指定的所需套件：

    ```bash
    pip install -r requirements.txt
    ```

#### 使用 Poetry（從 pyproject.toml）

1. 如果您使用 Poetry，請在終端中輸入以下命令。它將自動安裝 `pyproject.toml` 文件中指定的所需套件：

    ```bash
    poetry install
    ```

**免責聲明**：  
本文件使用AI翻譯服務[Co-op Translator](https://github.com/Azure/co-op-translator)進行翻譯。我們努力追求準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。應將原始文件的母語版本視為權威來源。對於關鍵資訊，建議進行專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤譯承擔責任。