<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b6d85d887d2664539a438dae5d0dfa50",
  "translation_date": "2025-05-06T17:56:11+00:00",
  "source_file": "getting_started/command-line-guide/install-package.md",
  "language_code": "zh"
}
-->
# 安装 Co-op translator 包

**Co-op Translator** 是一个命令行界面（CLI）工具，旨在帮助你将项目中的所有 Markdown 文件和图片翻译成多种语言。本教程将引导你配置翻译器并针对各种使用场景运行它。

### 创建虚拟环境

你可以使用 `pip` 或 `Poetry` 来创建虚拟环境。在终端中输入以下任意命令。

#### 使用 pip

```bash
python -m venv .venv
```

#### 使用 Poetry

```bash
poetry init
```

### 激活虚拟环境

创建虚拟环境后，需要激活它。激活步骤因操作系统而异。在终端中输入以下命令。

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

1. 如果你是用 Poetry 创建的环境，在终端中输入以下命令激活它。

    ```bash
    poetry shell
    ```

### 安装包和所需依赖

虚拟环境创建并激活后，下一步是安装所需依赖。

### 快速安装

通过 pip 安装 Co-Op Translator

```
pip install co-op-translator
```  
或者  

通过 Poetry 安装  
```
poetry add co-op-translator
```

#### 使用 pip（从 requirements.txt）如果你克隆了此仓库

![NOTE] 如果你通过快速安装方式安装 co-op translator，请不要使用此方法。

1. 如果你使用 pip，在终端中输入以下命令。它会自动安装 `requirements.txt` 文件中指定的依赖包：

    ```bash
    pip install -r requirements.txt
    ```

#### 使用 Poetry（从 pyproject.toml）

1. 如果你使用 Poetry，在终端中输入以下命令。它会自动安装 `pyproject.toml` 文件中指定的依赖包：

    ```bash
    poetry install
    ```

**免责声明**：  
本文件由 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻译而成。虽然我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始语言版本的文件应被视为权威来源。对于重要信息，建议使用专业人工翻译。我们不对因使用本翻译而产生的任何误解或误释承担责任。