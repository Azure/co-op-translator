<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "33db54f4f3ca9f0321be05374b591f2b",
  "translation_date": "2025-05-06T17:58:21+00:00",
  "source_file": "getting_started/command-line-guide/translator-your-project.md",
  "language_code": "ja"
}
-->
# Co-op Translatorを使ってプロジェクトを翻訳する

**Co-op Translator**は、プロジェクト内のマークダウンファイルや画像ファイルを複数言語に翻訳するためのコマンドラインインターフェイス（CLI）ツールです。このセクションではツールの使い方、各種CLIオプション、そしてさまざまな利用例について説明します。

> [!NOTE]
> コマンドの一覧や詳細な説明については、[Command reference](./command-reference.md)を参照してください。

---

## 利用例とコマンド

ここでは**Co-op Translator**の代表的な使い方と、それに対応するコマンドを紹介します。

### 1. 基本の翻訳（一言語）

プロジェクト全体（マークダウンファイルと画像）を、例えば韓国語に翻訳したい場合は、以下のコマンドを使います。

```bash
translate -l "ko"
```

このコマンドは、既存の翻訳を削除せずに、すべてのマークダウンと画像ファイルを韓国語に翻訳して追加します。

> [!TIP]
>
> **Co-op Translator**で利用可能な言語コードを確認したい場合は、リポジトリの[Supported Languages](https://github.com/Azure/co-op-translator#supported-languages)セクションをご覧ください。

#### Phi-3 CookBookでの例

**Phi-3 CookBook**では、既存のマークダウンファイルと画像に韓国語の翻訳を追加するために、以下の方法を使いました。

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko"
Translating images: 100%|███████████████████████████████████████████████████| 276/276 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 153/153 [1:43:07<00:00, 241.31s/it]
```

### 2. 複数言語の翻訳

プロジェクトを複数の言語（例：スペイン語、フランス語、ドイツ語）に翻訳する場合は、次のコマンドを使います。

```bash
translate -l "es fr de"
```

このコマンドは、既存の翻訳を上書きせずに、スペイン語、フランス語、ドイツ語の翻訳を追加します。

#### Phi-3 CookBookでの例

**Phi-3 CookBook**では、最新のコミットを反映するために最新の変更を取得した後、新たに追加されたマークダウンファイルと画像を翻訳するために以下の方法を使いました。

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko ja zh tw es fr" -a
Translating images: 100%|███████████████████████████████████████████████████| 273/273 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 6/6 [24:07<00:00, 241.31s/it]
```

> [!NOTE]
> 通常は一度に一言語ずつ翻訳することが推奨されますが、特定の変更をまとめて追加したい場合などは、一度に複数言語を翻訳する方が効率的なこともあります。

### 3. ルートディレクトリの指定

デフォルトでは、翻訳ツールはカレントディレクトリを使用します。プロジェクトが別の場所にある場合は、`-r`オプションでルートディレクトリを指定してください。

```bash
translate -l "es fr de" -r "./my_project"
```

このコマンドは`./my_project`ディレクトリ内のファイルを翻訳します。`-u`オプションを付けると、指定した言語の既存の翻訳をすべて削除してから再翻訳します。

```bash
translate -l "ko" -u
```

警告: このコマンドは、既存の翻訳を削除する前に確認を求めます。

#### Phi-3 CookBookでの例

**Phi-3 CookBook**では、スペイン語の翻訳ファイルをすべて更新するために以下の方法を使いました。複数のマークダウンファイルで元のコンテンツに大幅な変更がある場合はこちらの方法を推奨します。もし更新すべき翻訳ファイルが少数であれば、対象ファイルを手動で削除し、その後`-a`オプションで更新した翻訳を追加する方が効率的です。

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "es" -u
Warning: The update command will delete all existing translations for 'es' and re-translate everything.
Do you want to continue? Type 'yes' to proceed: yes
Proceeding with update...
Translating images: 100%|████████████████████████████████████████████| 150/150 [43:46<00:00, 15.55s/it]
Translating markdown files: 100%|███████████████████████████████████| 95/95 [1:40:27<00:00, 125.62s/it]
```

### 6. 画像のみの翻訳

プロジェクト内の画像ファイルのみを翻訳したい場合は、`-img`オプションを使います。

```bash
translate -l "ko" -img
```

このコマンドはマークダウンファイルには影響を与えず、画像だけを韓国語に翻訳します。

### 7. マークダウンファイルのみの翻訳

マークダウンファイルだけを翻訳したい場合は、`-md`オプションを使います。

```bash
translate -l "ko" -md
```

### 8. 翻訳ファイルのエラー確認

翻訳済みファイルにエラーがないかチェックし、必要に応じて再翻訳したい場合は、`-chk`オプションを使います。

```bash
translate -l "ko" -chk
```

このコマンドは翻訳済みのマークダウンファイルをスキャンし、エラーがあったファイルに対して翻訳を再試行します。

#### Phi-3 CookBookでの例

**Phi-3 CookBook**では、韓国語ファイルの翻訳エラーをチェックし、問題が検出されたファイルを自動で再翻訳するために以下の方法を使いました。

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko" -chk 
Checking translated files for errors in ko...
Checking files for ko: 100%|██████████████████████████████████████████████████| 95/95 [00:01<00:00, 65.47file/s]
Retrying vsc-extension-quickstart.md for ko:   0%|                                     | 0/17 [00:00<?, ?file/s] 
```

このオプションは翻訳エラーを検出します。現状では、元ファイルと翻訳ファイルの改行差が6行以上ある場合、そのファイルを翻訳エラーとして扱います。今後はより柔軟な判定基準に改善する予定です。

例えば、欠落したチャンクや破損した翻訳を検出し、それらのファイルを自動的に再翻訳するのに役立ちます。

ただし、問題のあるファイルが分かっている場合は、該当ファイルを手動で削除し、`-a -d`オプションを使う方が効率的です。

```bash
translate -l "ko" -d
```

このコマンドはデバッグモードで翻訳を実行し、翻訳処理中の問題特定に役立つ詳細なログを出力します。

#### Phi-3 CookBookでの例

**Phi-3 CookBook**では、マークダウンファイル内のリンクが多い翻訳でフォーマット崩れ（翻訳が途切れる、改行が無視されるなど）が発生したため、`-d`オプションを使って翻訳処理の動作を確認しました。

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "ko" -d
DEBUG:openai._base_client:Request options: {'method': 'post', 'url': '/chat/completions', 'headers': {'api-key': 'af04e0bea45747d8a7b8c131c1971044'}, 'files': None, 'json_data': {'messages': [{'role': 'user', 'content': "Translate the following text to ko. NEVER ADD ANY EXTRA CONTENT OUTSIDE THE TRANSLATION. TRANSLATE ONLY WHAT IS GIVEN TO YOU.. MAINTAIN MARKDOWN FORMAT\n\n# Phi-3 Cookbook: Hands-On Examples with Microsoft's Phi-3 Models [![Open and use the samples in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phi-3cookbook) [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%
...
```

### 10. すべての言語に翻訳

プロジェクトを対応しているすべての言語に翻訳したい場合は、`all`キーワードを使います。

> [!WARNING]
> 一度にすべての言語を翻訳すると、プロジェクトの規模によってはかなりの時間がかかります。例えば**Phi-3 CookBook**をスペイン語に翻訳するのに約2時間かかりました。20言語を一人で対応するのは現実的ではないため、複数の参加者で分担し、1～2言語ずつ担当して段階的に翻訳を更新することをおすすめします。

```bash
translate -l "all"
```

このコマンドは利用可能なすべての言語に翻訳を行います。実行すると、プロジェクトの規模に応じてかなりの時間がかかる可能性があります。

> [!TIP]
>
> ### 更新が必要なファイルの削除
> プルリクエストで最近変更されたファイルを更新する際の最初のステップは、翻訳フォルダ内の各言語の該当ファイルをすべて削除することです。以下のコマンドを使うと、翻訳フォルダ内の特定の名前のファイルを一括削除できます。
>
> ### Windowsの場合：
> 1. **コマンドプロンプトを使う方法**：
>    - コマンドプロンプトを開く。
>    - `cd`コマンドで対象フォルダに移動する。
>    - 以下のコマンドでファイルを削除する：
>      ```
>      del /s *filename*
>      ```
>      `/s`オプションはサブディレクトリも検索します。
>
> 2. **PowerShellを使う方法**：
>    - PowerShellを開く。
>    - 次のコマンドを実行：
>      ```powershell
>      Get-ChildItem -Path "C:\YourPath" -Filter "*filename*" -Recurse | Remove-Item -Force
>      ```
>      `"C:\YourPath"`や`filename`は適宜置き換えてください。
>
>    - `cd`や`find`コマンドの代わりに以下も使えます：
>     ```bash
>     find . -type f -name "*filename*" -delete
>     ```
>
>    - `filename`を指定して、最新の変更を反映するために`translate -l`コマンドを使います。

**免責事項**:  
本書類はAI翻訳サービス「Co-op Translator」（https://github.com/Azure/co-op-translator）を使用して翻訳されています。正確性を期しておりますが、自動翻訳には誤りや不正確な箇所が含まれる可能性があることをご了承ください。原文はあくまで正式な情報源としてご参照ください。重要な情報については、専門の人間による翻訳を推奨いたします。本翻訳の利用により生じたいかなる誤解や解釈の相違についても、当方は責任を負いかねます。