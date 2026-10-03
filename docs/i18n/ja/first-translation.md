# 小さなプロジェクトを翻訳、編集、レビューする

2つの短いMarkdownファイルと1つのターゲット言語から始めます。翻訳がどこに書き込まれるか、ソースが変更されたときに何が起きるか、および結果をどのように確認するかがわかります。

## 記録結果

この例は2026年9月19日にCo-op Translator 0.21.0とAzure OpenAI（`gpt-5-mini`）で実行されました。未変更のCLIコマンドは、ビルドされたホイールと既存のPython依存関係を使用してClickの`CliRunner`を通じて呼び出されました。

| ステップ | 結果 |
| --- | --- |
| プレビュー | 終了コード 0; モデル翻訳は要求されませんでした |
| 初回翻訳 | 終了コード 0; 27.36 秒 |
| 初回レビュー | 終了コード 0 |
| README を編集してレビュー | 終了コード 1; 古くなった翻訳が検出されました |
| 翻訳を更新 | 終了コード 0; 22.17 秒 |
| 更新後のレビュー | 終了コード 0; エラーや警告なし |
| 変更のないガイド | README 更新前後でバイトが同一 |
| 再実行 | 終了コード 0; すべての翻訳ファイルでハッシュが同一 |

これらは個別の実行測定値であり、性能保証ではありません。セットアップ時間は除外されています；プロバイダーの課金は測定されていません。変更がない実行でもプロバイダーのヘルスチェックを行うことがあります。

以下を確認してください: [初回翻訳](../../assets/demo/before.txt)、[更新された翻訳](../../assets/demo/after.txt)、[完全な翻訳差分](../../assets/demo/update.diff)、[古くなったレビュー](../../assets/demo/review-stale.txt)、[最終レビュー](../../assets/demo/review-after.txt)、および[実行の詳細](../../assets/demo/results.json)。ファイル全体の翻訳では、キャプチャされた差分が示すように他の表現が変更されることがあります。両方のテキスト成果物は生成された免責事項を保持しています。

人的なレビューは依然重要です：キャプチャされた更新は `\[사용 가이드](guide.md)을` を使用しています；韓国語の助詞は `\[사용 가이드](guide.md)를` であるべきです。テキスト成果物は、この出力を編集された翻訳として提示するのではなくそのまま保持します。構造的なレビューはこの文言の問題にもかかわらず合格します。

## 1. 小さなフォルダを準備

Python 3.11–3.14 と [仮想環境のセットアップ](configuration.md#local-runtime-setup) を使用してください。例で使用したバージョンをインストールします:

```bash
python -m pip install co-op-translator==0.21.0
mkdir translation-demo
cd translation-demo
git init
```

このフォルダに [README.txt](../../assets/demo/README.txt) と [guide.txt](../../assets/demo/guide.txt) をダウンロードし、`README.md` と `guide.md` として保存してください。これらは小さな架空のプロジェクト文書で、アプリケーションのインストールは不要です。

README にはコードブロックと `guide.md` へのリンクが含まれています。その最後の文は次のとおりです:

```text
Notes are saved locally.
```

このフォルダにはこれら二つのソース文書のみを置いてください。以下のすべてのコマンドは `translation-demo` 内で実行され、Bash と PowerShell で動作します。

## 2. 認証情報なしでプレビュー

```bash
translate -l "ko" -md --dry-run
```

プレビューはモデルを呼び出したり翻訳を書き込んだりせずに翻訳作業を推定します。トークンの推定は請求見積もりではありません。最初の実行では両方のMarkdownファイルが新しい作業として識別されるはずです。

## 3. プロバイダーを選択して翻訳

[設定ガイド](configuration.md) を使用してプロバイダーを1つ設定します：Azure OpenAI、OpenAI、または Anthropic。OpenAI と Anthropic のテキスト翻訳は Azure アカウントを必要としません。この例では画像サービスは必要ありません。

ローカルの `.env` ファイルを使用する場合は、このフォルダの `.gitignore` に `.env` を追加してください。翻訳呼び出しはプロバイダーのアカウントを使用し、料金が発生する場合があります。

```bash
translate -l "ko" -md
co-op-review -l "ko"
```

`translations/ko/README.md` と `translations/ko/guide.md` を開いてください。韓国語の表現、コードブロック、翻訳された README から翻訳されたガイドへのリンクを確認します。出力の言い回しはモデルによって異なります。

`co-op-review` は新鮮さ、構造、およびローカルリンクをチェックします。合格した結果は言語的な正確性を保証するものではありません。続行する前に報告されたエラーを解決してください。

必要であれば先に Git のユーザー設定を行い、成功したベースラインを Git に記録します：

```bash
git add README.md guide.md translations
git commit -m "Record initial Korean translation"
```

## 4. ソースを変更

`README.md` 内で、`Notes are saved locally.` を次のように置き換えます:

```text
Notes are saved locally as Markdown files.
```

`guide.md` は変更しないでください。それから次を実行します：

```bash
co-op-review -l "ko"
translate -l "ko" -md --dry-run
```

レビューは README の翻訳が古くなっていると報告し、失敗終了するはずです。これは予想される中間状態です。プレビューは変更された README の作業を識別するはずです。

## 5. 更新して差分を確認

```bash
translate -l "ko" -md
git diff -- README.md translations/ko/README.md
git diff -- translations/ko/guide.md
co-op-review -l "ko"
```

実際の差分を検査してください：デフォルトのCLIは変更されたファイルを再翻訳するため、モデルはそのファイル内の他の表現も改訂することがあります。変更のないガイドには差分がないはずです。レビューはもはや README を古いものとして報告しないはずです；無視するのではなくその他の指摘を調査してください。

ブロックレベルでの人によるMarkdown編集の保持は、[Python API](api.md) にあるオプションの翻訳状態プロバイダーを必要とします。これはこれらのCLIコマンドでは有効になっていません。

## 6. 変更なしで再実行

更新されたソースと翻訳をコミットします：

```bash
git add README.md translations
git commit -m "Update Korean translation after source edit"
translate -l "ko" -md
git diff --exit-code -- translations
```

現在の翻訳と設定が変更されていない場合、翻訳ツールはファイルをスキップします。最後の Git コマンドは差分を出力せず正常に終了するはずです。

## 次のステップ

- [README のみを翻訳してプルリクエストを作成する](github-actions.md#your-first-readme-translation-pr).
- [CLI、Python API、または MCP を選択する](workflows.md).
- [コーディングせずに翻訳の問題を報告する](https://github.com/Azure/co-op-translator/issues/new?template=translation_feedback.yml).