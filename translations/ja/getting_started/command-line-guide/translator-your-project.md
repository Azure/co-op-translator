<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d238206c3503631e32774716d11d1868",
  "translation_date": "2025-05-07T13:59:21+00:00",
  "source_file": "getting_started/command-line-guide/translator-your-project.md",
  "language_code": "ja"
}
-->
# Co-op Translatorでプロジェクトを翻訳する

**Co-op Translator**は、プロジェクト内のマークダウンファイルや画像ファイルを複数の言語に翻訳するためのコマンドラインインターフェイス（CLI）ツールです。このセクションでは、ツールの使い方、各種CLIオプション、そしてさまざまなユースケースの例を説明します。

> [!NOTE]
> コマンドの完全な一覧と詳細な説明については、[Command reference](./command-reference.md)を参照してください。

---

## 利用シナリオとコマンド例

以下に、**Co-op Translator**のよくある使い方と、それに対応するコマンド例を示します。

### 1. 基本の翻訳（単一言語）

プロジェクト全体（マークダウンファイルと画像）を単一言語、例えば韓国語に翻訳するには、次のコマンドを使います：

```bash
translate -l "ko"
```

このコマンドは、すべてのマークダウンおよび画像ファイルを韓国語に翻訳し、既存の翻訳を削除せずに新しい翻訳を追加します。

> [!TIP]
>
> **Co-op Translator**で利用可能な言語コードを確認したい場合は、リポジトリ内の[Supported Languages](https://github.com/Azure/co-op-translator#supported-languages)セクションをご覧ください。

#### Phi-3 CookBookでの例

**Phi-3 CookBook**では、既存のマークダウンファイルと画像に韓国語翻訳を追加するために、以下の方法を使いました。

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko"
Translating images: 100%|███████████████████████████████████████████████████| 276/276 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 153/153 [1:43:07<00:00, 241.31s/it]
```

### 2. 複数言語の翻訳

プロジェクトを複数言語（例：スペイン語、フランス語、ドイツ語）に翻訳するには、次のコマンドを使用します：

```bash
translate -l "es fr de"
```

このコマンドは、スペイン語、フランス語、ドイツ語に翻訳し、既存の翻訳を上書きせずに新しい翻訳を追加します。

#### Phi-3 CookBookでの例

**Phi-3 CookBook**では、最新のコミットを反映させるために最新の変更をプルした後、新たに追加されたマークダウンファイルと画像を翻訳するために、以下の方法を使いました。

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko ja zh tw es fr" -a
Translating images: 100%|███████████████████████████████████████████████████| 273/273 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 6/6 [24:07<00:00, 241.31s/it]
```

> [!NOTE]
> 通常は一度に一言語ずつ翻訳することが推奨されますが、特定の変更を一括で追加したい場合などは、複数言語を同時に翻訳することも効率的です。

### 3. 翻訳の更新（既存翻訳の削除）

既存の翻訳を削除して新しい翻訳に置き換えるには、`-u`オプションを使います。これにより指定した言語の既存翻訳がすべて削除され、再翻訳されます。

```bash
translate -l "ko" -u
```

注意：このコマンドは、既存翻訳を削除する前に確認のプロンプトが表示されます。

#### Phi-3 CookBookでの例

**Phi-3 CookBook**では、スペイン語のすべての翻訳ファイルを更新するために以下の方法を使いました。複数のマークダウンドキュメントにわたり元のコンテンツに大きな変更があった場合に、この方法を推奨します。翻訳ファイルが少数だけ更新が必要な場合は、該当ファイルを手動で削除してから`-a`オプションで更新翻訳を追加する方が効率的です。

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "es" -u
Warning: The update command will delete all existing translations for 'es' and re-translate everything.
Do you want to continue? Type 'yes' to proceed: yes
Proceeding with update...
Translating images: 100%|████████████████████████████████████████████| 150/150 [43:46<00:00, 15.55s/it]
Translating markdown files: 100%|███████████████████████████████████| 95/95 [1:40:27<00:00, 125.62s/it]
```

### 5. 画像ファイルのみを翻訳

プロジェクト内の画像ファイルだけを翻訳したい場合は、`-img`オプションを使います：

```bash
translate -l "ko" -img
```

このコマンドは画像のみを韓国語に翻訳し、マークダウンファイルには影響を与えません。

### 6. マークダウンファイルのみを翻訳

マークダウンファイルだけを翻訳したい場合は、`-md`オプションを使います：

```bash
translate -l "ko" -md
```

### 7. 翻訳ファイルのエラー確認

翻訳ファイルにエラーがないかチェックし、必要に応じて再翻訳したい場合は、`-chk`オプションを使います：

```bash
translate -l "ko" -chk
```

このコマンドは翻訳済みのマークダウンファイルをスキャンし、エラーのあるファイルの翻訳を再試行します。

#### Phi-3 CookBookでの例

**Phi-3 CookBook**では、韓国語ファイルの翻訳エラーをチェックし、問題が検出されたファイルの翻訳を自動で再試行するために以下の方法を使いました。

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko" -chk 
Checking translated files for errors in ko...
Checking files for ko: 100%|██████████████████████████████████████████████████| 95/95 [00:01<00:00, 65.47file/s]
Retrying vsc-extension-quickstart.md for ko:   0%|                                     | 0/17 [00:00<?, ?file/s] 
```

このオプションは翻訳エラーを検出します。現在は、元ファイルと翻訳ファイルの改行差が6行以上ある場合、そのファイルを翻訳エラーとみなしています。将来的にこの判定基準を柔軟に改善する予定です。

例えば、この方法は翻訳の欠落や破損を検出するのに有用で、該当ファイルの翻訳を自動的に再試行します。

ただし、問題のあるファイルが既に特定できている場合は、手動で該当ファイルを削除し、`-a` option to re-translate them.

### 8. Debug Mode

To enable detailed logging for troubleshooting, use the `-d`オプションを使う方が効率的です：

```bash
translate -l "ko" -d
```

このコマンドはデバッグモードで翻訳を実行し、翻訳処理中の問題特定に役立つ追加ログ情報を提供します。

#### Phi-3 CookBookでの例

**Phi-3 CookBook**では、マークダウンファイル内に多数のリンクが含まれる翻訳が原因で、翻訳の崩れや改行無視といったフォーマットの問題が発生しました。この問題の診断には、`-d`オプションを使い翻訳処理の動作を確認しました。

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "ko" -d
DEBUG:openai._base_client:Request options: {'method': 'post', 'url': '/chat/completions', 'headers': {'api-key': 'af04e0bea45747d8a7b8c131c1971044'}, 'files': None, 'json_data': {'messages': [{'role': 'user', 'content': "Translate the following text to ko. NEVER ADD ANY EXTRA CONTENT OUTSIDE THE TRANSLATION. TRANSLATE ONLY WHAT IS GIVEN TO YOU.. MAINTAIN MARKDOWN FORMAT\n\n# Phi-3 Cookbook: Hands-On Examples with Microsoft's Phi-3 Models [![Open and use the samples in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phi-3cookbook) [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%
...
```

### 9. 全言語への翻訳

プロジェクトをサポートされているすべての言語に翻訳したい場合は、`all`キーワードを使います。

> [!WARNING]
> 一度にすべての言語を翻訳すると、プロジェクトの規模によってはかなり時間がかかることがあります。例えば、**Phi-3 CookBook**をスペイン語に翻訳するのに約2時間かかりました。20言語を1人で対応するのは現実的ではありません。複数の参加者で分担し、1～2言語ずつ担当して段階的に翻訳を進めることを推奨します。

```bash
translate -l "all"
```

このコマンドは利用可能なすべての言語に翻訳します。実行すると、プロジェクトの規模に応じてかなりの時間がかかる可能性があります。

> [!TIP]
>
> ### 翻訳ファイルの手動削除（任意）
> 翻訳ファイルは、ソースファイルが更新されると自動的に検出されクリーンアップされるようになりました。
>
> しかし、特定のファイルをやり直したりシステムの動作を上書きしたい場合は、以下のコマンドで言語フォルダ全体から該当ファイルを削除できます。
>
> ### Windowsの場合：
> 1. **コマンドプロンプトを使う場合**：
>    - コマンドプロンプトを開く
>    - `cd`コマンドでファイルがあるフォルダに移動
>    - 次のコマンドでファイルを削除：
>      ```
>      del /s *filename*
>      ```
>      `filename` with the specific part of the file name you're looking for. The `/s`オプションはサブディレクトリも検索します。
>
> 2. **PowerShellを使う場合**：
>    - PowerShellを開く
>    - 次のコマンドを実行：
>      ```powershell
>      Get-ChildItem -Path "C:\YourPath" -Filter "*filename*" -Recurse | Remove-Item -Force
>      ```
>      `"C:\YourPath"` with the folder path and `filename` with the specific name.
>
> ### On macOS/Linux:
> 1. **Using Terminal**:
>   - Open Terminal.
>   - Navigate to the directory with `cd`.
>   - Use the `find`コマンド：
>     ```bash
>     find . -type f -name "*filename*" -delete
>     ```
>     `filename` with the specific name.
>
> Always double-check the files before deleting to avoid accidental loss. 
>
> Once you have deleted the files which need to be replace simply rerun your `translate -l`コマンドは最新のファイル変更を反映して更新します。

**免責事項**:  
本書類はAI翻訳サービス「[Co-op Translator](https://github.com/Azure/co-op-translator)」を使用して翻訳されています。正確性には努めておりますが、自動翻訳には誤りや不正確な箇所が含まれる可能性があることをご理解ください。原文の母国語版が正式な情報源とみなされます。重要な情報については、専門の人間による翻訳を推奨いたします。本翻訳の使用により生じたいかなる誤解や誤訳についても、当方は責任を負いかねます。