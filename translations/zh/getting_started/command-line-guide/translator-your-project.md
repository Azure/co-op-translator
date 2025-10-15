<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "20943a46b11c6d74814f41a817a6db4c",
  "translation_date": "2025-10-15T02:27:41+00:00",
  "source_file": "getting_started/command-line-guide/translator-your-project.md",
  "language_code": "zh"
}
-->
# 使用 Co-op Translator 翻译你的项目

**Co-op Translator** 是一个命令行界面（CLI）工具，可以帮助你将项目中的 markdown 文件和图片文件翻译成多种语言。本节将介绍如何使用该工具，涵盖各种 CLI 选项，并提供不同场景下的使用示例。

---

## 示例场景与命令

以下是使用 **Co-op Translator** 的几个常见场景，以及对应的命令。

### 1. 基础翻译（单一语言）

如果你想将整个项目（包括 markdown 文件和图片）翻译成一种语言，比如韩语，可以使用以下命令：

```bash
translate -l "ko"
```

此命令会将所有 markdown 和图片文件翻译成韩语，并新增翻译内容，不会删除已有的翻译。

#### 在 Phi-3 CookBook 上的示例

在 **Phi-3 CookBook** 项目中，我用以下方法为现有的 markdown 文件和图片添加了韩语翻译。

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko"
Translating images: 100%|███████████████████████████████████████████████████| 276/276 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 153/153 [1:43:07<00:00, 241.31s/it]
```

### 2. 多语言翻译

如果你想将项目翻译成多种语言（例如西班牙语、法语和德语），可以使用以下命令：

```bash
translate -l "es fr de"
```

此命令会将项目翻译成西班牙语、法语和德语，并新增翻译内容，不会覆盖已有的翻译。

#### 在 Phi-3 CookBook 上的示例

在 **Phi-3 CookBook** 项目中，拉取了最新的更改以反映最近的提交后，我用以下方法翻译了新添加的 markdown 文件和图片。

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko ja zh tw es fr" -a
Translating images: 100%|███████████████████████████████████████████████████| 273/273 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 6/6 [24:07<00:00, 241.31s/it]
```

### 3. 更新翻译（删除已有翻译）

如果你需要更新已有的翻译（即删除当前翻译并用新内容替换），可以使用 `-u` 选项。此操作会删除指定语言的所有现有翻译，并重新翻译。

```bash
translate -l "ko" -u
```

注意：此命令会在删除现有翻译前提示你确认。

#### 在 Phi-3 CookBook 上的示例

在 **Phi-3 CookBook** 项目中，我用以下方法更新了所有西班牙语的翻译文件。建议在原始内容有较大变动、涉及多个 markdown 文档时使用此方法。如果只需更新少量翻译文件，手动删除这些文件后再用 `-a` 方法添加更新的翻译会更高效。

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "es" -u
Warning: The update command will delete all existing translations for 'es' and re-translate everything.
Do you want to continue? Type 'yes' to proceed: yes
Proceeding with update...
Translating images: 100%|████████████████████████████████████████████| 150/150 [43:46<00:00, 15.55s/it]
Translating markdown files: 100%|███████████████████████████████████| 95/95 [1:40:27<00:00, 125.62s/it]
```

### 5. 只翻译图片

如果你只想翻译项目中的图片文件，可以使用 `-img` 选项：

```bash
translate -l "ko" -img
```

此命令只会将图片翻译成韩语，不会影响任何 markdown 文件。

### 6. 只翻译 Markdown 文件

如果你只想翻译项目中的 markdown 文件，可以使用 `-md` 选项：

```bash
translate -l "ko" -md
```

#### 在 Phi-3 CookBook 上的示例

在 **Phi-3 CookBook** 项目中，我用以下方法检查韩语文件的翻译错误，并自动重试有问题的文件。

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko" -chk 
Checking translated files for errors in ko...
Checking files for ko: 100%|██████████████████████████████████████████████████| 95/95 [00:01<00:00, 65.47file/s]
Retrying vsc-extension-quickstart.md for ko:   0%|                                     | 0/17 [00:00<?, ?file/s] 
```

此选项会检查翻译错误。目前，如果原文件和翻译文件的换行数差异超过六行，则会被标记为翻译错误。未来我计划优化这个标准，让检测更灵活。

比如，这个方法可以用来检测缺失内容或损坏的翻译，并自动重试这些文件的翻译。

不过，如果你已经知道哪些文件有问题，手动删除这些文件后用 `-a` 选项重新翻译会更高效。

### 8. 调试模式

如果你需要详细日志来排查问题，可以使用 `-d` 选项：

```bash
translate -l "ko" -d
```

此命令会以调试模式运行翻译，提供更多日志信息，帮助你定位翻译过程中的问题。

#### 在 Phi-3 CookBook 上的示例

在 **Phi-3 CookBook** 项目中，我遇到 markdown 文件中链接较多时，翻译会出现格式错误，比如翻译断裂或换行丢失。为了解决这个问题，我用 `-d` 选项查看了翻译过程的详细信息。

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "ko" -d
DEBUG:openai._base_client:Request options: {'method': 'post', 'url': '/chat/completions', 'headers': {'api-key': 'af04e0bea45747d8a7b8c131c1971044'}, 'files': None, 'json_data': {'messages': [{'role': 'user', 'content': "Translate the following text to ko. NEVER ADD ANY EXTRA CONTENT OUTSIDE THE TRANSLATION. TRANSLATE ONLY WHAT IS GIVEN TO YOU.. MAINTAIN MARKDOWN FORMAT\n\n# Phi-3 Cookbook: Hands-On Examples with Microsoft's Phi-3 Models [![Open and use the samples in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phi-3cookbook) [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%
...
```

### 9. 翻译所有语言

如果你想将项目翻译成所有支持的语言，可以使用 all 关键字。

```bash
translate -l "all"
```

此命令会将项目翻译成所有可用语言。根据项目大小，翻译可能需要较长时间。

> ### 手动删除翻译文件（可选）
> 当源文件更新时，翻译文件现在会自动检测并清理。
>
> 但如果你想手动更新某个翻译，比如重新翻译某个文件或覆盖系统行为，可以用以下命令删除该文件在所有语言文件夹中的版本。
>
> ### Windows 系统：
> 1. **使用命令提示符**：
>    - 打开命令提示符。
>    - 用 `cd` 命令进入文件所在文件夹。
>    - 用以下命令删除文件：
>      ```
>      del /s *filename*
>      ```
>      将 `filename` 替换为你要查找的文件名部分。`/s` 选项会搜索子目录。
>
> 2. **使用 PowerShell**：
>    - 打开 PowerShell。
>    - 运行以下命令：
>      ```powershell
>      Get-ChildItem -Path "C:\YourPath" -Filter "*filename*" -Recurse | Remove-Item -Force
>      ```
>      将 `"C:\YourPath"` 替换为文件夹路径，`filename` 替换为具体文件名。
>
> ### macOS/Linux 系统：
> 1. **使用终端**：
>   - 打开终端。
>   - 用 `cd` 进入目录。
>   - 用 `find` 命令：
>     ```bash
>     find . -type f -name "*filename*" -delete
>     ```
>     将 `filename` 替换为具体文件名。
>
> 删除前请务必仔细检查文件，避免误删。
>
> 删除需要替换的文件后，只需重新运行你的 `translate -l` 命令即可更新最新的文件内容。

---

**免责声明**：
本文件由 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻译。尽管我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始语言版本应被视为权威来源。对于关键信息，建议使用专业人工翻译。因使用本翻译而产生的任何误解或误读，我们概不负责。