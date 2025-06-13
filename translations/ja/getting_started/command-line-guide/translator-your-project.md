<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d238206c3503631e32774716d11d1868",
  "translation_date": "2025-06-12T18:43:26+00:00",
  "source_file": "getting_started/command-line-guide/translator-your-project.md",
  "language_code": "ja"
}
-->
# Co-op Translator を使ってプロジェクトを翻訳する

**Co-op Translator** は、プロジェクト内のマークダウンファイルや画像ファイルを複数の言語に翻訳するためのコマンドラインインターフェース（CLI）ツールです。このセクションでは、ツールの使い方、さまざまなCLIオプションの説明、そして用途別の例を紹介します。

> [!NOTE]
> コマンド一覧と詳細な説明については、[Command reference](./command-reference.md) をご覧ください。

---

## 例とコマンド

ここでは、**Co-op Translator** のよくある使い方と、それに対応するコマンドを紹介します。

### 1. 基本的な翻訳（単一言語）

プロジェクト全体（マークダウンファイルと画像）を単一言語、例えば韓国語に翻訳するには、以下のコマンドを使います。

```bash
translate -l "ko"
```

このコマンドは、既存の翻訳を削除せずに、すべてのマークダウンと画像ファイルを韓国語に翻訳して追加します。

> [!TIP]
>
> **Co-op Translator** で利用可能な言語コードを確認したい場合は、リポジトリの [Supported Languages](https://github.com/Azure/co-op-translator#supported-languages) セクションをご覧ください。

#### Phi-3 CookBook の例

**Phi-3 CookBook** では、既存のマークダウンファイルと画像に韓国語の翻訳を追加するために、以下の方法を使いました。

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko"
Translating images: 100%|███████████████████████████████████████████████████| 276/276 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 153/153 [1:43:07<00:00, 241.31s/it]
```

### 2. 複数言語の翻訳

プロジェクトを複数の言語（例：スペイン語、フランス語、ドイツ語）に翻訳するには、次のコマンドを使います。

```bash
translate -l "es fr de"
```

このコマンドは、既存の翻訳を上書きせずに、新しい翻訳をスペイン語、フランス語、ドイツ語で追加します。

#### Phi-3 CookBook の例

**Phi-3 CookBook** では、最新のコミットを反映するために最新の変更をプルした後、追加されたマークダウンファイルと画像を翻訳するために以下の方法を使いました。

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko ja zh tw es fr" -a
Translating images: 100%|███████████████████████████████████████████████████| 273/273 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 6/6 [24:07<00:00, 241.31s/it]
```

> [!NOTE]
> 基本的には一度に一言語ずつ翻訳することが推奨されていますが、特定の変更を一括で追加するような場合は、複数言語を同時に翻訳するのも効率的です。

### 3. 翻訳の更新（既存翻訳を削除）

既存の翻訳を更新するには（つまり現在の翻訳を削除して新しい翻訳に置き換えるには）、`-u` オプションを使います。このオプションは、指定した言語の既存の翻訳をすべて削除してから再翻訳します。

```bash
translate -l "ko" -u
```

警告：このコマンドは、既存の翻訳を削除する前に確認を求められます。

#### Phi-3 CookBook の例

**Phi-3 CookBook** では、スペイン語の翻訳ファイルをすべて更新するために以下の方法を使いました。複数のマークダウン文書にわたって元のコンテンツに大きな変更があった場合は、この方法が推奨されます。更新する翻訳ファイルが少数の場合は、該当ファイルを手動で削除してから `-a` オプションで再追加するほうが効率的です。

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "es" -u
Warning: The update command will delete all existing translations for 'es' and re-translate everything.
Do you want to continue? Type 'yes' to proceed: yes
Proceeding with update...
Translating images: 100%|████████████████████████████████████████████| 150/150 [43:46<00:00, 15.55s/it]
Translating markdown files: 100%|███████████████████████████████████| 95/95 [1:40:27<00:00, 125.62s/it]
```

### 5. 画像のみを翻訳する

プロジェクト内の画像ファイルのみを翻訳したい場合は、`-img` オプションを使います。

```bash
translate -l "ko" -img
```

このコマンドは、マークダウンファイルには影響を与えず、画像だけを韓国語に翻訳します。

### 6. マークダウンファイルのみを翻訳する

マークダウンファイルだけを翻訳したい場合は、`-md` オプションを使います。

```bash
translate -l "ko" -md
```

### 7. 翻訳ファイルのエラー確認

翻訳済みファイルのエラーをチェックし、必要に応じて翻訳を再試行したい場合は、`-chk` オプションを使います。

```bash
translate -l "ko" -chk
```

このコマンドは、翻訳済みのマークダウンファイルをスキャンし、エラーのあるファイルに対して翻訳を再試行します。

#### Phi-3 CookBook の例

**Phi-3 CookBook** では、韓国語ファイルの翻訳エラーをチェックし、問題があったファイルの翻訳を自動で再試行するために以下の方法を使いました。

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko" -chk 
Checking translated files for errors in ko...
Checking files for ko: 100%|██████████████████████████████████████████████████| 95/95 [00:01<00:00, 65.47file/s]
Retrying vsc-extension-quickstart.md for ko:   0%|                                     | 0/17 [00:00<?, ?file/s] 
```

このオプションは翻訳エラーを検出します。現在は、元ファイルと翻訳ファイルの改行差が6行以上ある場合に翻訳エラーと見なしています。将来的には、より柔軟な基準に改善する予定です。

例えば、この方法は欠落したチャンクや壊れた翻訳を検出するのに役立ち、それらのファイルの翻訳を自動的に再試行します。

ただし、問題のあるファイルが既にわかっている場合は、それらのファイルを手動で削除してから `-a` option to re-translate them.

### 8. Debug Mode

To enable detailed logging for troubleshooting, use the `-d` オプションを使うほうが効率的です。

```bash
translate -l "ko" -d
```

このコマンドはデバッグモードで翻訳を実行し、翻訳プロセス中の問題特定に役立つ追加のログ情報を提供します。

#### Phi-3 CookBook の例

**Phi-3 CookBook** では、多くのリンクを含むマークダウンファイルの翻訳で、翻訳の崩れや改行が無視されるなどのフォーマットエラーが発生しました。この問題を診断するために、`-d` オプションを使って翻訳プロセスの動作を確認しました。

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "ko" -d
DEBUG:openai._base_client:Request options: {'method': 'post', 'url': '/chat/completions', 'headers': {'api-key': 'af04e0bea45747d8a7b8c131c1971044'}, 'files': None, 'json_data': {'messages': [{'role': 'user', 'content': "Translate the following text to ko. NEVER ADD ANY EXTRA CONTENT OUTSIDE THE TRANSLATION. TRANSLATE ONLY WHAT IS GIVEN TO YOU.. MAINTAIN MARKDOWN FORMAT\n\n# Phi-3 Cookbook: Hands-On Examples with Microsoft's Phi-3 Models [![Open and use the samples in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phi-3cookbook) [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%
...
```

### 9. すべての言語を翻訳する

プロジェクトをサポートされているすべての言語に翻訳したい場合は、`all` キーワードを使います。

> [!WARNING]
> 一度にすべての言語を翻訳すると、プロジェクトの規模によっては非常に長い時間がかかることがあります。例えば、**Phi-3 CookBook** をスペイン語に翻訳するだけで約2時間かかりました。この規模で20言語を一人で処理するのは現実的ではありません。複数の貢献者で作業を分担し、1～2言語ずつ担当して徐々に翻訳を更新することを推奨します。

```bash
translate -l "all"
```

このコマンドは、利用可能なすべての言語に翻訳を行います。実行すると、プロジェクトの規模によってはかなり時間がかかる可能性があります。

> [!TIP]
>
> ### 翻訳済みファイルの手動削除（任意）
> ソースファイルが更新されると、翻訳済みファイルは自動的に検出されてクリーンアップされます。
>
> しかし、特定のファイルをやり直したい、またはシステムの動作を上書きしたい場合は、以下のコマンドで言語フォルダ内のすべてのバージョンのファイルを削除できます。
>
> ### Windowsの場合：
> 1. **コマンドプロンプトを使う場合**：
>    - コマンドプロンプトを開きます。
>    - `cd` コマンドでファイルがあるフォルダに移動します。
>    - 以下のコマンドでファイルを削除します：
>      ```
>      del /s *filename*
>      ```
>      `filename` with the specific part of the file name you're looking for. The `/s` オプションはサブディレクトリも検索します。
>
> 2. **PowerShellを使う場合**：
>    - PowerShellを開きます。
>    - 次のコマンドを実行します：
>      ```powershell
>      Get-ChildItem -Path "C:\YourPath" -Filter "*filename*" -Recurse | Remove-Item -Force
>      ```
>      `"C:\YourPath"` with the folder path and `filename` with the specific name.
>
> ### On macOS/Linux:
> 1. **Using Terminal**:
>   - Open Terminal.
>   - Navigate to the directory with `cd`.
>   - Use the `find` コマンド：
>     ```bash
>     find . -type f -name "*filename*" -delete
>     ```
>     `filename` with the specific name.
>
> Always double-check the files before deleting to avoid accidental loss. 
>
> Once you have deleted the files which need to be replace simply rerun your `translate -l` コマンドで最新のファイル変更を更新します。

**免責事項**:  
本書類はAI翻訳サービス「[Co-op Translator](https://github.com/Azure/co-op-translator)」を使用して翻訳されました。正確性には努めておりますが、自動翻訳には誤りや不正確な箇所が含まれる可能性があることをご承知おきください。原文の言語によるオリジナル文書が正式な情報源とみなされます。重要な情報については、専門の人間による翻訳を推奨いたします。本翻訳の使用に起因するいかなる誤解や誤訳についても、当方は責任を負いかねます。