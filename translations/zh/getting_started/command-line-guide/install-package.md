<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "510827ad22a2031a50838919c3594828",
  "translation_date": "2025-10-15T02:27:33+00:00",
  "source_file": "getting_started/command-line-guide/install-package.md",
  "language_code": "zh"
}
-->
# 安装 Co-op Translator 包

**Co-op Translator** 是一个命令行界面（CLI）工具，旨在帮助你将项目中的所有 markdown 文件和图片翻译成多种语言。本教程将指导你如何配置翻译器并根据不同场景运行它。

### 创建虚拟环境

你可以使用 `pip` 或 `Poetry` 创建虚拟环境。在终端中输入以下任一命令。

#### 使用 pip

```bash
python -m venv .venv
```

#### 使用 Poetry

```bash
poetry init
```

### 激活虚拟环境

创建好虚拟环境后，你需要激活它。不同操作系统的激活方式不同。在终端中输入以下命令。

#### 适用于 pip 和 Poetry

- Windows：

    ```bash
    .venv\Scripts\activate
    ```

- Mac/Linux：

    ```bash
    source .venv/bin/activate
    ```

#### 使用 Poetry

1. 如果你是用 Poetry 创建的环境，在终端中输入以下命令来激活它。

    ```bash
    poetry shell
    ```

### 安装包及所需依赖

当你的虚拟环境搭建并激活后，下一步就是安装所需的依赖包。

### 快速安装

通过 pip 安装 Co-Op Translator

```
pip install co-op-translator
```
或者

通过 poetry 安装
```
poetry add co-op-translator
```

#### 如果你克隆了本仓库，使用 pip（通过 requirements.txt）

> [!NOTE]
> 如果你已经通过快速安装方式安装了 co-op translator，请不要执行此步骤。

1. 如果你使用 pip，在终端中输入以下命令。它会自动安装 `requirements.txt` 文件中指定的所有依赖包：

    ```bash
    pip install -r requirements.txt
    ```

#### 使用 Poetry（通过 pyproject.toml）

1. 如果你使用 Poetry，在终端中输入以下命令。它会自动安装 `pyproject.toml` 文件中指定的所有依赖包：

    ```bash
    poetry install
    ```

---

**免责声明**：
本文件由 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻译。尽管我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始语言的文件应被视为权威来源。对于关键信息，建议使用专业人工翻译。因使用本翻译而产生的任何误解或误读，我们概不负责。