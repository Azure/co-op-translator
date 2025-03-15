# Translate your project using Co-op Translator

The **Co-op Translator** is a command-line interface (CLI) tool that helps you translate markdown and image files in your project into multiple languages. This section explains how to use the tool, covers the various CLI options, and provides examples for different use cases.

> [!NOTE]
> For a complete list of commands and their detailed descriptions, please refer to the [Command reference](./command-reference.md).

---

## Example Scenarios and Commands

Here are a few common use cases for the **Co-op Translator**, along with the appropriate commands to run.

### 1. Basic Translation (Single Language)

To translate your entire project (markdown files and images) into a single language, like Korean, use the following command:

```bash
translate -l "ko"
```

This command will translate all markdown and image files into Korean, adding new translations without deleting any existing ones.

> [!TIP]
>
> Want to see which language codes are available in **Co-op Translator**? Visit the [Supported Languages](https://github.com/Azure/co-op-translator#supported-languages) section in the repository for more details.

#### Example on Phi-3 CookBook

In the **Phi-3 CookBook**, I used the following method to add the Korean translation for the existing markdown files and images.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko"
Translating images: 100%|███████████████████████████████████████████████████| 276/276 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 153/153 [1:43:07<00:00, 241.31s/it]
```

### 2. Translating Multiple Languages

To translate your project into multiple languages (e.g., Spanish, French, and German), use this command:

```bash
translate -l "es fr de"
```

This command will translate the project into Spanish, French, and German, adding new translations without overwriting existing ones.

#### Example on Phi-3 CookBook

In the **Phi-3 CookBook**, after pulling the latest changes to reflect the most recent commits, I used the following method to translate newly added markdown files and images.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko ja zh tw es fr" -a
Translating images: 100%|███████████████████████████████████████████████████| 273/273 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 6/6 [24:07<00:00, 241.31s/it]
```

> [!NOTE]
> While it's generally recommended to translate one language at a time, in situations like this where specific changes need to be added, translating multiple languages at once can be efficient.

### 3. Specifying the Root Directory

By default, the translator uses the current working directory. If your project is located elsewhere, specify the root directory with the -r option:

```bash
translate -l "es fr de" -r "./my_project"
```

This command translates the files in `./my_project` into Spanish, French, and German.

### 4. Updating Translations (Deletes Existing Translations)

To update existing translations (i.e., delete the current translations and replace them with new ones), use the `-u` option. This will delete all existing translations for the specified languages and re-translate them.

```bash
translate -l "ko" -u
```

Warning: This command will prompt you for confirmation before proceeding with deleting the existing translations.

#### Example on Phi-3 CookBook

In the **Phi-3 CookBook**, I used the following method to update all translated files in Spanish. I recommend using this method when there are significant changes to the original content across multiple markdown documents. If there are only a few translated markdown files to update, it’s more efficient to manually delete those specific files and then use the `-a` method to add the updated translations.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "es" -u
Warning: The update command will delete all existing translations for 'es' and re-translate everything.
Do you want to continue? Type 'yes' to proceed: yes
Proceeding with update...
Translating images: 100%|████████████████████████████████████████████| 150/150 [43:46<00:00, 15.55s/it]
Translating markdown files: 100%|███████████████████████████████████| 95/95 [1:40:27<00:00, 125.62s/it]
```

### 6. Translating Only Images

To translate only the image files in your project, use the `-img` option:

```bash
translate -l "ko" -img
```

This command will translate only the images into Korean, without affecting any markdown files.

### 7. Translating Only Markdown Files

To translate only the markdown files in your project, use the `-md` option:

```bash
translate -l "ko" -md
```

### 8. Checking for Errors in Translated Files

If you want to check translated files for errors and retry the translation if necessary, use the `-chk` option:

```bash
translate -l "ko" -chk
```

This command will scan the translated markdown files and retry translation for any files with errors.

#### Example on Phi-3 CookBook

In the **Phi-3 CookBook**, I used the following method to check for translation errors in the Korean files and automatically retry translation for any files with detected issues.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko" -chk 
Checking translated files for errors in ko...
Checking files for ko: 100%|██████████████████████████████████████████████████| 95/95 [00:01<00:00, 65.47file/s]
Retrying vsc-extension-quickstart.md for ko:   0%|                                     | 0/17 [00:00<?, ?file/s] 
```

This option checks for translation errors. Currently, if the difference in line breaks between the original and translated files is more than six, the file is flagged as having a translation error. I plan to improve this criterion for greater flexibility in the future.

For example, this method is useful for detecting missing chunks or corrupted translations, and it will automatically retry the translation for those files.

However, if you already know which files are problematic, it’s more efficient to manually delete those files and use the `-a` option to re-translate them.

### 9. Debug Mode

To enable detailed logging for troubleshooting, use the `-d` option:

```bash
translate -l "ko" -d
```

This command will run the translation in debug mode, providing additional logging information that can help you identify issues during the translation process.

#### Example on Phi-3 CookBook

In the **Phi-3 CookBook**, I encountered an issue where translations with many links in markdown files caused formatting errors, such as broken translations and ignored line breaks. To diagnose this problem, I used the `-d` option to see how the translation process was works.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "ko" -d
DEBUG:openai._base_client:Request options: {'method': 'post', 'url': '/chat/completions', 'headers': {'api-key': 'af04e0bea45747d8a7b8c131c1971044'}, 'files': None, 'json_data': {'messages': [{'role': 'user', 'content': "Translate the following text to ko. NEVER ADD ANY EXTRA CONTENT OUTSIDE THE TRANSLATION. TRANSLATE ONLY WHAT IS GIVEN TO YOU.. MAINTAIN MARKDOWN FORMAT\n\n# Phi-3 Cookbook: Hands-On Examples with Microsoft's Phi-3 Models [![Open and use the samples in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phi-3cookbook) [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%
...
```

### 10. Translating All Languages

If you want to translate the project into all supported languages, use the all keyword.

> [!WARNING]
> Translating all languages at once can take a significant amount of time depending on the project size. For example, translating the **Phi-3 CookBook** into Spanish took about 2 hour. Given the scale, it's not practical for one person to handle 20 languages. It's recommended to split the work among multiple contributors, each managing one or two languages, and update translations gradually.

```bash
translate -l "all"
```

This command will translate the project into all available languages. If you proceed, the translation may take a significant amount of time depending on the size of the project.

> [!TIP]
>
> ### Deleting files which need to be updated 
> To update files recently changed in Pull Request the first step is to delete all the existing versions of the specific file located in the different language translation folders. You can do this in bulk by using the following command to delete all the files with a specific name within the translation folders.
>
> ### On Windows:
> 1. **Using Command Prompt**:
>    - Open Command Prompt.
>    - Navigate to the folder where the files are located using the `cd` command.
>    - Use the following command to delete files:
>      ```
>      del /s *filename*
>      ```
>      Replace `filename` with the specific part of the file name you're looking for. The `/s` option searches subdirectories as well.
>
> 2. **Using PowerShell**:
>    - Open PowerShell.
>    - Run this command:
>      ```powershell
>      Get-ChildItem -Path "C:\YourPath" -Filter "*filename*" -Recurse | Remove-Item -Force
>      ```
>      Replace `"C:\YourPath"` with the folder path and `filename` with the specific name.
>
> ### On macOS/Linux:
> 1. **Using Terminal**:
>   - Open Terminal.
>   - Navigate to the directory with `cd`.
>   - Use the `find` command:
>     ```bash
>     find . -type f -name "*filename*" -delete
>     ```
>     Replace `filename` with the specific name.
>
> Always double-check the files before deleting to avoid accidental loss. 
>
> Once you have deleted the files which need to be replace simply rerun your `translate -l` command to update the most recent file changes.