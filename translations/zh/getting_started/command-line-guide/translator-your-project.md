<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d238206c3503631e32774716d11d1868",
  "translation_date": "2025-06-12T18:41:49+00:00",
  "source_file": "getting_started/command-line-guide/translator-your-project.md",
  "language_code": "zh"
}
-->
# 使用 Co-op Translator 翻译你的项目

**Co-op Translator** 是一个命令行界面（CLI）工具，帮助你将项目中的 markdown 和图片文件翻译成多种语言。本节介绍如何使用该工具，涵盖各种 CLI 选项，并提供不同用例的示例。

> [!NOTE]
> 有关完整命令列表及详细说明，请参阅 [Command reference](./command-reference.md)。

---

## 示例场景和命令

以下是一些常见的 **Co-op Translator** 用例及相应的命令。

### 1. 基础翻译（单语言）

要将整个项目（markdown 文件和图片）翻译成单一语言，如韩语，使用以下命令：

```bash
translate -l "ko"
```

此命令会将所有 markdown 和图片文件翻译成韩语，新增翻译内容，不会删除已有翻译。

> [!TIP]
>
> 想查看 **Co-op Translator** 支持哪些语言代码？请访问仓库中的 [Supported Languages](https://github.com/Azure/co-op-translator#supported-languages) 部分了解详情。

#### Phi-3 CookBook 示例

在 **Phi-3 CookBook** 中，我用以下方法为现有的 markdown 文件和图片添加了韩语翻译。

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko"
Translating images: 100%|███████████████████████████████████████████████████| 276/276 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 153/153 [1:43:07<00:00, 241.31s/it]
```

### 2. 多语言翻译

若要将项目翻译成多种语言（例如西班牙语、法语和德语），使用此命令：

```bash
translate -l "es fr de"
```

该命令会将项目翻译成西班牙语、法语和德语，新增翻译内容，不覆盖已有翻译。

#### Phi-3 CookBook 示例

在 **Phi-3 CookBook** 中，拉取最新更改以同步最新提交后，我用以下方法翻译新增的 markdown 文件和图片。

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko ja zh tw es fr" -a
Translating images: 100%|███████████████████████████████████████████████████| 273/273 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 6/6 [24:07<00:00, 241.31s/it]
```

> [!NOTE]
> 虽然一般建议一次翻译一种语言，但在需要添加特定更改的情况下，一次翻译多种语言会更高效。

### 3. 更新翻译（删除已有翻译）

要更新已有翻译（即删除当前翻译并替换为新翻译），使用 `-u` 选项。该操作会删除指定语言的所有现有翻译并重新翻译。

```bash
translate -l "ko" -u
```

警告：执行此命令前会提示确认，防止误删已有翻译。

#### Phi-3 CookBook 示例

在 **Phi-3 CookBook** 中，我用以下方法更新了所有西班牙语翻译文件。建议当多个 markdown 文档的原文内容发生重大变化时使用此方法。如果只是少数几个翻译文件需要更新，手动删除这些文件后再用 `-a` 方法添加更新的翻译会更高效。

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "es" -u
Warning: The update command will delete all existing translations for 'es' and re-translate everything.
Do you want to continue? Type 'yes' to proceed: yes
Proceeding with update...
Translating images: 100%|████████████████████████████████████████████| 150/150 [43:46<00:00, 15.55s/it]
Translating markdown files: 100%|███████████████████████████████████| 95/95 [1:40:27<00:00, 125.62s/it]
```

### 5. 仅翻译图片

若只想翻译项目中的图片文件，使用 `-img` 选项：

```bash
translate -l "ko" -img
```

此命令只会将图片翻译成韩语，不影响任何 markdown 文件。

### 6. 仅翻译 Markdown 文件

若只想翻译项目中的 markdown 文件，使用 `-md` 选项：

```bash
translate -l "ko" -md
```

### 7. 检查翻译文件中的错误

如果想检查翻译文件中的错误，并在必要时重试翻译，使用 `-chk` 选项：

```bash
translate -l "ko" -chk
```

该命令会扫描翻译的 markdown 文件，对有错误的文件重试翻译。

#### Phi-3 CookBook 示例

在 **Phi-3 CookBook** 中，我用以下方法检查韩语文件中的翻译错误，并自动重试有问题的文件翻译。

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko" -chk 
Checking translated files for errors in ko...
Checking files for ko: 100%|██████████████████████████████████████████████████| 95/95 [00:01<00:00, 65.47file/s]
Retrying vsc-extension-quickstart.md for ko:   0%|                                     | 0/17 [00:00<?, ?file/s] 
```

该选项用于检测翻译错误。目前，如果原文与译文的换行符差异超过六行，该文件会被标记为翻译错误。未来计划改进此标准，使其更灵活。

例如，这种方法适合检测缺失的内容块或损坏的翻译，并会自动重新翻译这些文件。

不过，如果你已经知道哪些文件有问题，手动删除这些文件后使用 `-a` option to re-translate them.

### 8. Debug Mode

To enable detailed logging for troubleshooting, use the `-d` 选项更高效：

```bash
translate -l "ko" -d
```

该命令会以调试模式运行翻译，提供更多日志信息，帮助你定位翻译过程中的问题。

#### Phi-3 CookBook 示例

在 **Phi-3 CookBook** 中，我遇到过因 markdown 文件中包含大量链接导致格式错误的问题，比如翻译断裂和换行被忽略。为诊断这个问题，我使用了 `-d` 选项查看翻译流程。

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "ko" -d
DEBUG:openai._base_client:Request options: {'method': 'post', 'url': '/chat/completions', 'headers': {'api-key': 'af04e0bea45747d8a7b8c131c1971044'}, 'files': None, 'json_data': {'messages': [{'role': 'user', 'content': "Translate the following text to ko. NEVER ADD ANY EXTRA CONTENT OUTSIDE THE TRANSLATION. TRANSLATE ONLY WHAT IS GIVEN TO YOU.. MAINTAIN MARKDOWN FORMAT\n\n# Phi-3 Cookbook: Hands-On Examples with Microsoft's Phi-3 Models [![Open and use the samples in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phi-3cookbook) [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%
...
```

### 9. 翻译所有语言

如果想将项目翻译成所有支持的语言，可以使用 all 关键字。

> [!WARNING]
> 一次翻译所有语言可能耗时较长，具体取决于项目规模。例如，将 **Phi-3 CookBook** 翻译成西班牙语就花了大约 2 小时。鉴于规模，单人处理 20 种语言并不现实。建议分配给多位贡献者，每人负责一两种语言，逐步更新翻译。

```bash
translate -l "all"
```

此命令会将项目翻译成所有可用语言。请注意，翻译过程可能耗时较长，具体取决于项目大小。

> [!TIP]
>
> ### 手动删除翻译文件（可选）
> 当源文件更新时，翻译文件会自动检测并清理。
>
> 但如果你想手动更新某个翻译——比如重做某个文件或覆盖系统行为——可以用以下命令删除所有语言文件夹中的该文件版本。
>
> ### Windows 系统：
> 1. **使用命令提示符**：
>    - 打开命令提示符。
>    - 用 `cd` 命令切换到文件所在文件夹。
>    - 使用以下命令删除文件：
>      ```
>      del /s *filename*
>      ```
>      其中 `/s` 选项表示同时搜索子目录。
>
> 2. **使用 PowerShell**：
>    - 打开 PowerShell。
>    - 运行此命令：
>      ```powershell
>      Get-ChildItem -Path "C:\YourPath" -Filter "*filename*" -Recurse | Remove-Item -Force
>      ```
>      替换 `"C:\YourPath"`、`filename`、`cd`、`find` 命令：
>     ```bash
>     find . -type f -name "*filename*" -delete
>     ```
>     替换 `filename`，使用 `translate -l` 命令更新最新文件更改。

**免责声明**：  
本文件使用 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。尽管我们努力确保准确性，但请注意自动翻译可能存在错误或不准确之处。原始文件的母语版本应被视为权威来源。对于重要信息，建议使用专业人工翻译。对于因使用本翻译而产生的任何误解或误释，我们不承担任何责任。