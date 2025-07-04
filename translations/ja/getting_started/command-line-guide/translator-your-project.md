<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d238206c3503631e32774716d11d1868",
  "translation_date": "2025-07-04T08:13:18+00:00",
  "source_file": "getting_started/command-line-guide/translator-your-project.md",
  "language_code": "ja"
}
-->
# Co-op Translatorでプロジェクトを翻訳する

**Co-op Translator**は、プロジェクト内のMarkdownファイルや画像ファイルを複数の言語に翻訳するためのコマンドラインインターフェース（CLI）ツールです。このセクションでは、ツールの使用方法、さまざまなCLIオプション、および異なるユースケースの例を説明します。

> [!NOTE]
> コマンドの完全なリストとその詳細な説明については、[コマンドリファレンス](./command-reference.md)を参照してください。

---

## 例シナリオとコマンド

ここでは、**Co-op Translator**の一般的なユースケースと、それに対応するコマンドを紹介します。

### 1. 基本的な翻訳（単一言語）

プロジェクト全体（Markdownファイルと画像）を単一の言語、例えば韓国語に翻訳するには、次のコマンドを使用します。

```bash
translate -l "ko"
```

このコマンドは、すべてのMarkdownファイルと画像ファイルを韓国語に翻訳し、既存の翻訳を削除せずに新しい翻訳を追加します。

> [!TIP]
>
> **Co-op Translator**で利用可能な言語コードを確認したいですか？詳細はリポジトリの[サポートされている言語](https://github.com/Azure/co-op-translator#supported-languages)セクションを訪問してください。

#### Phi-3 CookBookの例

**Phi-3 CookBook**では、既存のMarkdownファイルと画像に韓国語の翻訳を追加するために、次の方法を使用しました。

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko"
Translating images: 100%|███████████████████████████████████████████████████| 276/276 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 153/153 [1:43:07<00:00, 241.31s/it]
```

### 2. 複数言語の翻訳

プロジェクトを複数の言語（例：スペイン語、フランス語、ドイツ語）に翻訳するには、次のコマンドを使用します。

```bash
translate -l "es fr de"
```

このコマンドは、プロジェクトをスペイン語、フランス語、ドイツ語に翻訳し、既存の翻訳を上書きせずに新しい翻訳を追加します。

#### Phi-3 CookBookの例

**Phi-3 CookBook**では、最新のコミットを反映するために最新の変更をプルした後、新しく追加されたMarkdownファイルと画像を翻訳するために次の方法を使用しました。

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko ja zh tw es fr" -a
Translating images: 100%|███████████████████████████████████████████████████| 273/273 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 6/6 [24:07<00:00, 241.31s/it]
```

> [!NOTE]
> 一度に1つの言語を翻訳することが一般的に推奨されますが、このように特定の変更を追加する必要がある場合には、複数の言語を一度に翻訳することが効率的です。

### 3. 翻訳の更新（既存の翻訳を削除）

既存の翻訳を更新する（つまり、現在の翻訳を削除して新しいものに置き換える）には、`-u`オプションを使用します。これにより、指定された言語のすべての既存の翻訳が削除され、再翻訳されます。

```bash
translate -l "ko" -u
```

警告: このコマンドは、既存の翻訳を削除する前に確認を求めます。

#### Phi-3 CookBookの例

**Phi-3 CookBook**では、スペイン語のすべての翻訳ファイルを更新するために次の方法を使用しました。複数のMarkdownドキュメントにわたって元のコンテンツに大きな変更がある場合、この方法を使用することをお勧めします。更新する翻訳されたMarkdownファイルが少数の場合は、それらの特定のファイルを手動で削除し、`-a`メソッドを使用して更新された翻訳を追加する方が効率的です。

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "es" -u
Warning: The update command will delete all existing translations for 'es' and re-translate everything.
Do you want to continue? Type 'yes' to proceed: yes
Proceeding with update...
Translating images: 100%|████████████████████████████████████████████| 150/150 [43:46<00:00, 15.55s/it]
Translating markdown files: 100%|███████████████████████████████████| 95/95 [1:40:27<00:00, 125.62s/it]
```

### 5. 画像のみの翻訳

プロジェクト内の画像ファイルのみを翻訳するには、`-img`オプションを使用します。

```bash
translate -l "ko" -img
```

このコマンドは、Markdownファイルに影響を与えずに画像のみを韓国語に翻訳します。

### 6. Markdownファイルのみの翻訳

プロジェクト内のMarkdownファイルのみを翻訳するには、`-md`オプションを使用します。

```bash
translate -l "ko" -md
```

### 7. 翻訳ファイルのエラーをチェック

翻訳されたファイルのエラーをチェックし、必要に応じて翻訳を再試行したい場合は、`-chk`オプションを使用します。

```bash
translate -l "ko" -chk
```

このコマンドは、翻訳されたMarkdownファイルをスキャンし、エラーのあるファイルの翻訳を再試行します。

#### Phi-3 CookBookの例

**Phi-3 CookBook**では、韓国語ファイルの翻訳エラーをチェックし、問題のあるファイルの翻訳を自動的に再試行するために次の方法を使用しました。

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko" -chk 
Checking translated files for errors in ko...
Checking files for ko: 100%|██████████████████████████████████████████████████| 95/95 [00:01<00:00, 65.47file/s]
Retrying vsc-extension-quickstart.md for ko:   0%|                                     | 0/17 [00:00<?, ?file/s] 
```

このオプションは翻訳エラーをチェックします。現在、元のファイルと翻訳されたファイルの改行の差が6以上の場合、そのファイルは翻訳エラーとしてフラグが立てられます。将来的には、この基準をより柔軟にする予定です。

例えば、この方法は欠落した部分や破損した翻訳を検出するのに役立ち、それらのファイルの翻訳を自動的に再試行します。

ただし、問題のあるファイルがすでにわかっている場合は、それらのファイルを手動で削除し、`-a`オプションを使用して再翻訳する方が効率的です。

### 8. デバッグモード

トラブルシューティングのために詳細なログを有効にするには、`-d`オプションを使用します。

```bash
translate -l "ko" -d
```

このコマンドは、翻訳をデバッグモードで実行し、翻訳プロセス中の問題を特定するのに役立つ追加のログ情報を提供します。

#### Phi-3 CookBookの例

**Phi-3 CookBook**では、Markdownファイルに多くのリンクがある翻訳がフォーマットエラーを引き起こし、翻訳が壊れたり改行が無視されたりする問題が発生しました。この問題を診断するために、`-d`オプションを使用して翻訳プロセスがどのように機能しているかを確認しました。

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "ko" -d
DEBUG:openai._base_client:Request options: {'method': 'post', 'url': '/chat/completions', 'headers': {'api-key': 'af04e0bea45747d8a7b8c131c1971044'}, 'files': None, 'json_data': {'messages': [{'role': 'user', 'content': "Translate the following text to ko. NEVER ADD ANY EXTRA CONTENT OUTSIDE THE TRANSLATION. TRANSLATE ONLY WHAT IS GIVEN TO YOU.. MAINTAIN MARKDOWN FORMAT\n\n# Phi-3 Cookbook: Hands-On Examples with Microsoft's Phi-3 Models [![Open and use the samples in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phi-3cookbook) [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%
...
```

### 9. すべての言語を翻訳

プロジェクトをすべてのサポートされている言語に翻訳したい場合は、allキーワードを使用します。

> [!WARNING]
> すべての言語を一度に翻訳するには、プロジェクトのサイズに応じてかなりの時間がかかる場合があります。例えば、**Phi-3 CookBook**をスペイン語に翻訳するのに約2時間かかりました。この規模では、1人で20言語を扱うのは現実的ではありません。複数の貢献者に作業を分担し、それぞれが1つまたは2つの言語を管理し、翻訳を段階的に更新することをお勧めします。

```bash
translate -l "all"
```

このコマンドは、プロジェクトをすべての利用可能な言語に翻訳します。進める場合、プロジェクトのサイズに応じて翻訳にかなりの時間がかかる可能性があります。

> [!TIP]
>
> ### 翻訳ファイルの手動削除（オプション）
> 翻訳されたファイルは、ソースファイルが更新されたときに自動的に検出され、クリーンアップされます。
>
> ただし、特定のファイルをやり直したり、システムの動作を上書きしたりするために手動で翻訳を更新したい場合は、次のコマンドを使用して言語フォルダ全体のファイルのバージョンを削除できます。
>
> ### Windowsの場合:
> 1. **コマンドプロンプトを使用**:
>    - コマンドプロンプトを開きます。
>    - `cd`コマンドを使用してファイルがあるフォルダに移動します。
>    - 次のコマンドを使用してファイルを削除します:
>      ```
>      del /s *filename*
>      ```
>      `filename`を探しているファイル名の特定の部分に置き換えます。`/s`オプションはサブディレクトリも検索します。
>
> 2. **PowerShellを使用**:
>    - PowerShellを開きます。
>    - 次のコマンドを実行します:
>      ```powershell
>      Get-ChildItem -Path "C:\YourPath" -Filter "*filename*" -Recurse | Remove-Item -Force
>      ```
>      `"C:\YourPath"`をフォルダパスに、`filename`を特定の名前に置き換えます。
>
> ### macOS/Linuxの場合:
> 1. **ターミナルを使用**:
>   - ターミナルを開きます。
>   - `cd`でディレクトリに移動します。
>   - `find`コマンドを使用します:
>     ```bash
>     find . -type f -name "*filename*" -delete
>     ```
>     `filename`を特定の名前に置き換えます。
>
> 削除する前にファイルを必ずダブルチェックして、誤って削除しないようにしてください。
>
> 置き換える必要のあるファイルを削除したら、単に`translate -l`コマンドを再実行して最新のファイル変更を更新します。

**免責事項**:
この文書はAI翻訳サービス[Co-op Translator](https://github.com/Azure/co-op-translator)を使用して翻訳されています。正確性を追求していますが、自動翻訳には誤りや不正確さが含まれる可能性があることをご了承ください。元の文書をその言語で読むことが信頼できる情報源とされるべきです。重要な情報については、専門の人間による翻訳をお勧めします。この翻訳の使用に起因する誤解や誤った解釈について、当社は責任を負いません。