<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "510827ad22a2031a50838919c3594828",
  "translation_date": "2025-10-15T02:33:01+00:00",
  "source_file": "getting_started/command-line-guide/install-package.md",
  "language_code": "hk"
}
-->
# 安裝 Co-op Translator 套件

**Co-op Translator** 是一個命令列介面（CLI）工具，專門幫你把專案裡所有 markdown 檔案和圖片翻譯成多種語言。這份教學會一步步教你如何設定翻譯器，以及針對不同情境執行它。

### 建立虛擬環境

你可以用 `pip` 或 `Poetry` 來建立虛擬環境。在終端機輸入以下其中一個指令。

#### 用 pip

```bash
python -m venv .venv
```

#### 用 Poetry

```bash
poetry init
```

### 啟動虛擬環境

建立好虛擬環境後，你需要啟動它。根據你的作業系統，步驟會有點不同。在終端機輸入以下指令。

#### pip 和 Poetry 都適用

- Windows：

    ```bash
    .venv\Scripts\activate
    ```

- Mac/Linux：

    ```bash
    source .venv/bin/activate
    ```

#### 用 Poetry

1. 如果你是用 Poetry 建立環境，在終端機輸入以下指令來啟動它。

    ```bash
    poetry shell
    ```

### 安裝套件和必要依賴

虛擬環境設定好並啟動後，下一步就是安裝所需的依賴套件。

### 快速安裝

用 pip 安裝 Co-Op Translator

```
pip install co-op-translator
```
或者

用 poetry 安裝
```
poetry add co-op-translator
```

#### 用 pip（從 requirements.txt）如果你有 clone 這個 repo

> [!NOTE]
> 如果你是用快速安裝安裝 co-op translator，請不要這樣做。

1. 如果你用 pip，在終端機輸入以下指令。它會自動安裝 `requirements.txt` 檔案裡指定的所有必要套件：

    ```bash
    pip install -r requirements.txt
    ```

#### 用 Poetry（從 pyproject.toml）

1. 如果你用 Poetry，在終端機輸入以下指令。它會自動安裝 `pyproject.toml` 檔案裡指定的所有必要套件：

    ```bash
    poetry install
    ```

---

**免責聲明**：
本文件是使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯而成。雖然我們致力於確保翻譯的準確性，但請注意自動翻譯可能會包含錯誤或不準確之處。原始語言的文件應被視為具權威性的來源。如涉及重要資訊，建議尋求專業人工翻譯。我們不會對因使用本翻譯而引起的任何誤解或錯誤負責。