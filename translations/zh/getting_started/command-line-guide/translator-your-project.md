<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "33db54f4f3ca9f0321be05374b591f2b",
  "translation_date": "2025-05-06T17:58:44+00:00",
  "source_file": "getting_started/command-line-guide/translator-your-project.md",
  "language_code": "zh"
}
-->
# 使用 Co-op Translator 翻译你的项目

**Co-op Translator** 是一个命令行界面（CLI）工具，帮助你将项目中的 markdown 和图片文件翻译成多种语言。本节介绍如何使用该工具，涵盖各种 CLI 选项，并提供不同使用场景的示例。

> [!NOTE]
> 有关命令的完整列表及详细说明，请参阅 [Command reference](./command-reference.md)。

---

## 示例场景与命令

以下是一些常见的 **Co-op Translator** 使用场景及相应的命令。

### 1. 基础翻译（单语言）

要将整个项目（markdown 文件和图片）翻译成单一语言，比如韩语，请使用以下命令：

```bash
translate -l "ko"
```

该命令会将所有 markdown 和图片文件翻译成韩语，新增翻译内容而不会删除现有翻译。

> [!TIP]
>
> 想了解 **Co-op Translator** 支持哪些语言代码？请访问仓库中的 [Supported Languages](https://github.com/Azure/co-op-translator#supported-languages) 部分获取更多信息。

#### Phi-3 CookBook 示例

在 **Phi-3 CookBook** 中，我用以下方法为已有的 markdown 文件和图片添加了韩语翻译。

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko"
Translating images: 100%|███████████████████████████████████████████████████| 276/276 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 153/153 [1:43:07<00:00, 241.31s/it]
```

### 2. 多语言翻译

要将项目翻译成多种语言（例如西班牙语、法语和德语），使用此命令：

```bash
translate -l "es fr de"
```

该命令会将项目翻译成西班牙语、法语和德语，新增翻译内容而不会覆盖现有翻译。

#### Phi-3 CookBook 示例

在 **Phi-3 CookBook** 中，拉取最新更改以同步最近提交后，我使用以下方法翻译新添加的 markdown 文件和图片。

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko ja zh tw es fr" -a
Translating images: 100%|███████████████████████████████████████████████████| 273/273 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 6/6 [24:07<00:00, 241.31s/it]
```

> [!NOTE]
> 通常建议一次只翻译一种语言，但在需要添加特定更改的情况下，同时翻译多种语言可以提高效率。

### 3. 指定根目录

默认情况下，翻译器使用当前工作目录。如果你的项目位于其他位置，可以用 -r 选项指定根目录：

```bash
translate -l "es fr de" -r "./my_project"
```

该命令会翻译 `./my_project` 文件夹中的文件。

使用 `-u` 选项时，会删除指定语言的所有现有翻译并重新翻译。

```bash
translate -l "ko" -u
```

警告：该命令在删除现有翻译前会提示确认。

#### Phi-3 CookBook 示例

在 **Phi-3 CookBook** 中，我用以下方法更新了所有西班牙语翻译文件。当多个 markdown 文档的原始内容发生较大变动时，推荐使用此方法。如果只需更新少量翻译文件，手动删除这些文件后再用 `-a` 方式添加更新的翻译会更高效。

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "es" -u
Warning: The update command will delete all existing translations for 'es' and re-translate everything.
Do you want to continue? Type 'yes' to proceed: yes
Proceeding with update...
Translating images: 100%|████████████████████████████████████████████| 150/150 [43:46<00:00, 15.55s/it]
Translating markdown files: 100%|███████████████████████████████████| 95/95 [1:40:27<00:00, 125.62s/it]
```

### 6. 仅翻译图片

如果只想翻译项目中的图片文件，使用 `-img` 选项：

```bash
translate -l "ko" -img
```

该命令只会将图片翻译成韩语，不会影响任何 markdown 文件。

### 7. 仅翻译 Markdown 文件

如果只想翻译项目中的 markdown 文件，使用 `-md` 选项：

```bash
translate -l "ko" -md
```

### 8. 检查翻译文件中的错误

如果想检查翻译文件是否有错误，并在必要时重试翻译，使用 `-chk` 选项：

```bash
translate -l "ko" -chk
```

该命令会扫描翻译后的 markdown 文件，对有错误的文件重新尝试翻译。

#### Phi-3 CookBook 示例

在 **Phi-3 CookBook** 中，我用以下方法检查韩语翻译文件中的错误，并对检测到问题的文件自动重试翻译。

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko" -chk 
Checking translated files for errors in ko...
Checking files for ko: 100%|██████████████████████████████████████████████████| 95/95 [00:01<00:00, 65.47file/s]
Retrying vsc-extension-quickstart.md for ko:   0%|                                     | 0/17 [00:00<?, ?file/s] 
```

此选项用于检查翻译错误。目前，如果原文和译文在换行符数量上的差异超过六行，该文件即被标记为翻译错误。未来计划改进这一标准，使其更灵活。

例如，这种方法适合检测缺失内容块或翻译损坏的情况，并会自动重试这些文件的翻译。

不过，如果你已经知道哪些文件有问题，手动删除这些文件并使用 `-a` option to re-translate them.

### 9. Debug Mode

To enable detailed logging for troubleshooting, use the `-d` 选项会更高效：

```bash
translate -l "ko" -d
```

该命令以调试模式运行翻译，提供额外的日志信息，帮助你定位翻译过程中的问题。

#### Phi-3 CookBook 示例

在 **Phi-3 CookBook** 中，我遇到过由于 markdown 文件中包含大量链接导致格式错误（如翻译断裂和忽略换行）的情况。为诊断此问题，我使用了 `-d` 选项查看翻译过程的详细信息。

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "ko" -d
DEBUG:openai._base_client:Request options: {'method': 'post', 'url': '/chat/completions', 'headers': {'api-key': 'af04e0bea45747d8a7b8c131c1971044'}, 'files': None, 'json_data': {'messages': [{'role': 'user', 'content': "Translate the following text to ko. NEVER ADD ANY EXTRA CONTENT OUTSIDE THE TRANSLATION. TRANSLATE ONLY WHAT IS GIVEN TO YOU.. MAINTAIN MARKDOWN FORMAT\n\n# Phi-3 Cookbook: Hands-On Examples with Microsoft's Phi-3 Models [![Open and use the samples in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phi-3cookbook) [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%
...
```

### 10. 翻译所有语言

如果想将项目翻译成所有支持的语言，使用 all 关键字。

> [!WARNING]
> 一次性翻译所有语言可能耗时较长，具体取决于项目大小。例如，将 **Phi-3 CookBook** 翻译成西班牙语大约花费了 2 小时。考虑到规模，一个人同时处理 20 种语言并不现实。建议由多位贡献者分工合作，每人负责一两种语言，逐步更新翻译。

```bash
translate -l "all"
```

该命令会将项目翻译成所有可用语言。执行时，翻译时间可能较长，具体取决于项目规模。

> [!TIP]
>
> ### 删除需要更新的文件
> 若要更新 Pull Request 中最近修改的文件，第一步是删除不同语言翻译文件夹中该文件的所有现有版本。你可以使用以下命令批量删除所有指定名称的文件。
>
> ### 在 Windows 上：
> 1. **使用命令提示符**：
>    - 打开命令提示符。
>    - 使用 `cd` 命令进入文件所在文件夹。
>    - 使用以下命令删除文件：
>      ```
>      del /s *filename*
>      ```
>      `filename` with the specific part of the file name you're looking for. The `/s` 选项会搜索子目录。
>
> 2. **使用 PowerShell**：
>    - 打开 PowerShell。
>    - 运行此命令：
>      ```powershell
>      Get-ChildItem -Path "C:\YourPath" -Filter "*filename*" -Recurse | Remove-Item -Force
>      ```
>      替换 `"C:\YourPath"` with the folder path and `filename` with the specific name.
>
> ### On macOS/Linux:
> 1. **Using Terminal**:
>   - Open Terminal.
>   - Navigate to the directory with `cd`.
>   - Use the `find` 命令：
>     ```bash
>     find . -type f -name "*filename*" -delete
>     ```
>     替换 `filename` with the specific name.
>
> Always double-check the files before deleting to avoid accidental loss. 
>
> Once you have deleted the files which need to be replace simply rerun your `translate -l` 命令以更新最近的文件更改。

**免责声明**：  
本文件由 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻译而成。尽管我们力求准确，但请注意，自动翻译可能存在错误或不准确之处。原始文件的母语版本应被视为权威来源。对于重要信息，建议采用专业人工翻译。对于因使用本翻译而引起的任何误解或误释，我们概不负责。