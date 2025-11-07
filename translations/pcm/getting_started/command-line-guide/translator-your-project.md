<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "20943a46b11c6d74814f41a817a6db4c",
  "translation_date": "2025-11-06T17:31:56+00:00",
  "source_file": "getting_started/command-line-guide/translator-your-project.md",
  "language_code": "pcm"
}
-->
# Translate your project using Co-op Translator

**Co-op Translator** na command-line interface (CLI) tool wey go help you translate markdown and image files for your project go plenty languages. Dis section go explain how you fit use di tool, di different CLI options wey e get, and e go show you examples for different use cases.

> [!NOTE]
> For full list of commands and wetin dem mean, abeg check di [Command reference](./command-reference.md).

---

## Example Scenarios and Commands

Here be some common ways wey you fit use **Co-op Translator**, plus di correct commands to run.

### 1. Basic Translation (Single Language)

If you wan translate your whole project (markdown files and images) go one language, like Korean, use dis command:

```bash
translate -l "ko"
```

Dis command go translate all markdown and image files go Korean, e go add new translations but e no go delete di ones wey dey already.

> [!TIP]
>
> You wan know di language codes wey dey available for **Co-op Translator**? Check di [Supported Languages](https://github.com/Azure/co-op-translator#supported-languages) section for di repository for more gist.

#### Example for Phi-3 CookBook

For **Phi-3 CookBook**, I use dis method to add di Korean translation for di markdown files and images wey dey already.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko"
Translating images: 100%|███████████████████████████████████████████████████| 276/276 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 153/153 [1:43:07<00:00, 241.31s/it]
```

### 2. Translating Multiple Languages

If you wan translate your project go plenty languages (e.g., Spanish, French, and German), use dis command:

```bash
translate -l "es fr de"
```

Dis command go translate di project go Spanish, French, and German, e go add new translations but e no go touch di ones wey dey already.

#### Example for Phi-3 CookBook

For **Phi-3 CookBook**, after I pull di latest changes to reflect di most recent commits, I use dis method to translate di new markdown files and images wey I add.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko ja zh tw es fr" -a
Translating images: 100%|███████████████████████████████████████████████████| 273/273 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 6/6 [24:07<00:00, 241.31s/it]
```

> [!NOTE]
> Normally, e good make you dey translate one language at a time, but for cases like dis wey you wan add specific changes, translating plenty languages at once fit make sense.

### 3. Updating Translations (Deletes Existing Translations)

If you wan update di translations wey dey already (e.g., delete di ones wey dey and replace dem with new ones), use di `-u` option. Dis one go delete all di translations wey dey for di languages wey you choose and re-translate dem.

```bash
translate -l "ko" -u
```

Warning: Dis command go ask you to confirm before e go delete di translations wey dey already.

#### Example for Phi-3 CookBook

For **Phi-3 CookBook**, I use dis method to update all di Spanish translated files. I go advise make you use dis method if di original content don change well well for plenty markdown documents. But if na only small files you wan update, e better make you delete dem manually and use di `-a` method to add di updated translations.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "es" -u
Warning: The update command will delete all existing translations for 'es' and re-translate everything.
Do you want to continue? Type 'yes' to proceed: yes
Proceeding with update...
Translating images: 100%|████████████████████████████████████████████| 150/150 [43:46<00:00, 15.55s/it]
Translating markdown files: 100%|███████████████████████████████████| 95/95 [1:40:27<00:00, 125.62s/it]
```

### 5. Translating Only Images

If na only di image files for your project you wan translate, use di `-img` option:

```bash
translate -l "ko" -img
```

Dis command go translate only di images go Korean, e no go touch any markdown files.

### 6. Translating Only Markdown Files

If na only di markdown files for your project you wan translate, use di `-md` option:

```bash
translate -l "ko" -md
```

#### Example for Phi-3 CookBook

For **Phi-3 CookBook**, I use dis method to check for translation errors for di Korean files and e go automatically retry di translation for any file wey get problem.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko" -chk 
Checking translated files for errors in ko...
Checking files for ko: 100%|██████████████████████████████████████████████████| 95/95 [00:01<00:00, 65.47file/s]
Retrying vsc-extension-quickstart.md for ko:   0%|                                     | 0/17 [00:00<?, ?file/s] 
```

Dis option dey check for translation errors. Right now, if di difference for line breaks between di original and di translated files pass six, di file go dey flagged as get translation error. I dey plan to improve dis check to make am more flexible for future.

For example, dis method dey useful to find missing parts or translations wey don spoil, and e go automatically retry di translation for di files.

But if you don already sabi di files wey get problem, e better make you delete dem manually and use di `-a` option to re-translate dem.

### 8. Debug Mode

If you wan see detailed logging to troubleshoot, use di `-d` option:

```bash
translate -l "ko" -d
```

Dis command go run di translation for debug mode, e go show you extra logging info wey fit help you find di problem wey dey during di translation process.

#### Example for Phi-3 CookBook

For **Phi-3 CookBook**, I see one issue wey translations wey get plenty links for markdown files dey cause formatting errors, like broken translations and ignored line breaks. To find di problem, I use di `-d` option to see how di translation process dey work.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "ko" -d
DEBUG:openai._base_client:Request options: {'method': 'post', 'url': '/chat/completions', 'headers': {'api-key': 'af04e0bea45747d8a7b8c131c1971044'}, 'files': None, 'json_data': {'messages': [{'role': 'user', 'content': "Translate the following text to ko. NEVER ADD ANY EXTRA CONTENT OUTSIDE THE TRANSLATION. TRANSLATE ONLY WHAT IS GIVEN TO YOU.. MAINTAIN MARKDOWN FORMAT\n\n# Phi-3 Cookbook: Hands-On Examples with Microsoft's Phi-3 Models [![Open and use the samples in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phi-3cookbook) [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%
...
```

### 9. Translating All Languages

If you wan translate di project go all di languages wey di tool support, use di all keyword.

> [!WARNING]
> Translating all di languages at once fit take plenty time depending on how big di project be. For example, to translate **Phi-3 CookBook** go Spanish e take like 2 hours. Because of di size, e no go make sense for one person to handle 20 languages. E better make una share di work among plenty people, each person go handle one or two languages, and una go dey update di translations small small.

```bash
translate -l "all"
```

Dis command go translate di project go all di languages wey dey available. If you wan continue, di translation fit take plenty time depending on di size of di project.

> [!TIP]
>
> ### Manually Deleting Translated Files (Optional)
> Translated files now dey automatically detect and clean up when source file don update.
>
> But if you wan manually update translation - like if you wan redo one file or override di system behavior - you fit use dis command to delete all di versions of di file for di language folders.
>
> ### For Windows:
> 1. **Using Command Prompt**:
>    - Open Command Prompt.
>    - Go to di folder wey di files dey with di `cd` command.
>    - Use dis command to delete files:
>      ```
>      del /s *filename*
>      ```
>      Replace `filename` with di specific part of di file name wey you dey find. Di `/s` option go search subdirectories too.
>
> 2. **Using PowerShell**:
>    - Open PowerShell.
>    - Run dis command:
>      ```powershell
>      Get-ChildItem -Path "C:\YourPath" -Filter "*filename*" -Recurse | Remove-Item -Force
>      ```
>      Replace `"C:\YourPath"` with di folder path and `filename` with di specific name.
>
> ### For macOS/Linux:
> 1. **Using Terminal**:
>   - Open Terminal.
>   - Go to di directory with `cd`.
>   - Use di `find` command:
>     ```bash
>     find . -type f -name "*filename*" -delete
>     ```
>     Replace `filename` with di specific name.
>
> Always check di files well before you delete am to avoid mistake. 
>
> Once you don delete di files wey you wan replace, just run your `translate -l` command again to update di latest file changes.

---

**Disclaimer**:  
Dis dokyument don use AI transleto service [Co-op Translator](https://github.com/Azure/co-op-translator) do di translation. Even as we dey try make am correct, abeg sabi say machine translation fit get mistake or no dey accurate well. Di original dokyument wey dey for im native language na di main source wey you go trust. For important mata, e good make professional human transleto check am. We no go fit take blame for any misunderstanding or wrong interpretation wey fit happen because you use dis translation.