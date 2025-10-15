<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "20943a46b11c6d74814f41a817a6db4c",
  "translation_date": "2025-10-15T02:39:06+00:00",
  "source_file": "getting_started/command-line-guide/translator-your-project.md",
  "language_code": "ja"
}
-->
# Co-op Translatorでプロジェクトを翻訳する

**Co-op Translator**は、プロジェクト内のMarkdownファイルや画像ファイルを複数の言語に翻訳できるコマンドラインツール（CLI）です。このセクションでは、ツールの使い方やCLIオプションの説明、さまざまな利用例を紹介します。

> [!NOTE]
> コマンド一覧や詳細な説明については、[コマンドリファレンス](./command-reference.md)をご覧ください。

---

## 利用例とコマンド

**Co-op Translator**のよくある使い方と、それぞれに適したコマンドを紹介します。

### 1. 基本的な翻訳（単一言語）

プロジェクト全体（Markdownファイルと画像）を韓国語など1つの言語に翻訳するには、次のコマンドを使います。

```bash
translate -l "ko"
```

このコマンドは、すべてのMarkdownファイルと画像ファイルを韓国語に翻訳し、既存の翻訳を削除せずに新しい翻訳を追加します。

> [!TIP]
>
> **Co-op Translator**で利用できる言語コードを確認したい場合は、リポジトリの[対応言語一覧](https://github.com/Azure/co-op-translator#supported-languages)セクションをご覧ください。

#### Phi-3 CookBookでの例

**Phi-3 CookBook**では、既存のMarkdownファイルと画像に韓国語翻訳を追加するため、次の方法を使いました。

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko"
Translating images: 100%|███████████████████████████████████████████████████| 276/276 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 153/153 [1:43:07<00:00, 241.31s/it]
```

### 2. 複数言語への翻訳

プロジェクトを複数の言語（例：スペイン語、フランス語、ドイツ語）に翻訳するには、次のコマンドを使います。

```bash
translate -l "es fr de"
```

このコマンドは、スペイン語、フランス語、ドイツ語に翻訳し、既存の翻訳を上書きせずに新しい翻訳を追加します。

#### Phi-3 CookBookでの例

**Phi-3 CookBook**では、最新のコミットを反映させた後、新しく追加されたMarkdownファイルや画像を翻訳するために次の方法を使いました。

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko ja zh tw es fr" -a
Translating images: 100%|███████████████████████████████████████████████████| 273/273 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 6/6 [24:07<00:00, 241.31s/it]
```

> [!NOTE]
> 通常は1言語ずつ翻訳するのがおすすめですが、このように特定の変更をまとめて追加したい場合は、複数言語を同時に翻訳すると効率的です。

### 3. 翻訳の更新（既存翻訳の削除）

既存の翻訳を更新したい場合（現在の翻訳を削除して新しく翻訳し直す場合）は、`-u`オプションを使います。このオプションは指定した言語の既存翻訳をすべて削除し、再翻訳します。

```bash
translate -l "ko" -u
```

注意：このコマンドは、既存の翻訳を削除する前に確認のプロンプトが表示されます。

#### Phi-3 CookBookでの例

**Phi-3 CookBook**では、スペイン語のすべての翻訳ファイルを更新するためにこの方法を使いました。元の内容が大きく変更された場合は、この方法がおすすめです。もし更新したい翻訳ファイルが少数なら、該当ファイルだけ手動で削除し、`-a`オプションで翻訳を追加する方が効率的です。

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "es" -u
Warning: The update command will delete all existing translations for 'es' and re-translate everything.
Do you want to continue? Type 'yes' to proceed: yes
Proceeding with update...
Translating images: 100%|████████████████████████████████████████████| 150/150 [43:46<00:00, 15.55s/it]
Translating markdown files: 100%|███████████████████████████████████| 95/95 [1:40:27<00:00, 125.62s/it]
```

### 5. 画像のみ翻訳する

画像ファイルだけを翻訳したい場合は、`-img`オプションを使います。

```bash
translate -l "ko" -img
```

このコマンドは画像のみを韓国語に翻訳し、Markdownファイルには影響しません。

### 6. Markdownファイルのみ翻訳する

Markdownファイルだけを翻訳したい場合は、`-md`オプションを使います。

```bash
translate -l "ko" -md
```

#### Phi-3 CookBookでの例

**Phi-3 CookBook**では、韓国語ファイルの翻訳エラーをチェックし、問題が検出されたファイルを自動的に再翻訳するためにこの方法を使いました。

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko" -chk 
Checking translated files for errors in ko...
Checking files for ko: 100%|██████████████████████████████████████████████████| 95/95 [00:01<00:00, 65.47file/s]
Retrying vsc-extension-quickstart.md for ko:   0%|                                     | 0/17 [00:00<?, ?file/s] 
```

このオプションは翻訳エラーをチェックします。現在は、元ファイルと翻訳ファイルの改行数の差が6以上ある場合、翻訳エラーと判定しています。今後はより柔軟な基準に改善する予定です。

例えば、翻訳の抜けや破損を検出し、自動で再翻訳できるので便利です。

ただし、問題のあるファイルがすでに分かっている場合は、該当ファイルを手動で削除し、`-a`オプションで再翻訳する方が効率的です。

### 8. デバッグモード

詳細なログを出力してトラブルシューティングしたい場合は、`-d`オプションを使います。

```bash
translate -l "ko" -d
```

このコマンドはデバッグモードで翻訳を実行し、翻訳処理中の問題を特定するのに役立つ追加のログ情報を表示します。

#### Phi-3 CookBookでの例

**Phi-3 CookBook**では、Markdownファイル内のリンクが多い場合に翻訳のフォーマットが崩れたり、改行が無視されたりする問題が発生しました。原因を調査するため、`-d`オプションを使って翻訳処理の詳細を確認しました。

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "ko" -d
DEBUG:openai._base_client:Request options: {'method': 'post', 'url': '/chat/completions', 'headers': {'api-key': 'af04e0bea45747d8a7b8c131c1971044'}, 'files': None, 'json_data': {'messages': [{'role': 'user', 'content': "Translate the following text to ko. NEVER ADD ANY EXTRA CONTENT OUTSIDE THE TRANSLATION. TRANSLATE ONLY WHAT IS GIVEN TO YOU.. MAINTAIN MARKDOWN FORMAT\n\n# Phi-3 Cookbook: Hands-On Examples with Microsoft's Phi-3 Models [![Open and use the samples in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phi-3cookbook) [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%
...
```

### 9. すべての言語に翻訳する

プロジェクトを対応しているすべての言語に翻訳したい場合は、allキーワードを使います。

> [!WARNING]
> すべての言語に一度に翻訳すると、プロジェクトの規模によってはかなり時間がかかります。例えば、**Phi-3 CookBook**をスペイン語に翻訳するだけでも約2時間かかりました。20言語を1人で管理するのは現実的ではないので、複数の貢献者で分担し、1人が1～2言語ずつ担当して徐々に翻訳を更新するのがおすすめです。

```bash
translate -l "all"
```

このコマンドはプロジェクトをすべての対応言語に翻訳します。実行すると、プロジェクトの規模によってはかなり時間がかかる場合があります。

> [!TIP]
>
> ### 翻訳ファイルの手動削除（任意）
> ソースファイルが更新された場合、翻訳ファイルは自動的に検出されてクリーンアップされます。
>
> ただし、特定のファイルだけ翻訳をやり直したい場合や、システムの動作を上書きしたい場合は、次のコマンドで言語フォルダー内の該当ファイルをすべて削除できます。
>
> ### Windowsの場合:
> 1. **コマンドプロンプトを使う**:
>    - コマンドプロンプトを開く
>    - `cd`コマンドでファイルがあるフォルダーに移動
>    - 次のコマンドでファイルを削除
>      ```
>      del /s *filename*
>      ```
>      `filename`は探したいファイル名の一部に置き換えてください。`/s`オプションでサブディレクトリも検索します。
>
> 2. **PowerShellを使う**:
>    - PowerShellを開く
>    - 次のコマンドを実行
>      ```powershell
>      Get-ChildItem -Path "C:\YourPath" -Filter "*filename*" -Recurse | Remove-Item -Force
>      ```
>      `"C:\YourPath"`はフォルダーのパス、`filename`は特定のファイル名に置き換えてください。
>
> ### macOS/Linuxの場合:
> 1. **ターミナルを使う**:
>   - ターミナルを開く
>   - `cd`でディレクトリに移動
>   - `find`コマンドを使う
>     ```bash
>     find . -type f -name "*filename*" -delete
>     ```
>     `filename`は特定のファイル名に置き換えてください。
>
> 削除する前に必ずファイルを確認し、誤って消さないよう注意してください。
>
> 必要なファイルを削除したら、`translate -l`コマンドを再実行して最新のファイル変更を反映させましょう。

---

**免責事項**：
本書類は、AI翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性には努めておりますが、自動翻訳には誤りや不正確な表現が含まれる場合がありますのでご注意ください。原文（元の言語の文書）が正式な情報源となります。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用によって生じたいかなる誤解や誤認についても、当方は責任を負いかねます。