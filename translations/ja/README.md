# Co-op Translator

_Easily automate and maintain translations for your educational GitHub content across multiple languages as your project evolves._

![Python 3.10–3.12](https://img.shields.io/badge/python-3.10--3.12-blue)
[![Python package](https://img.shields.io/pypi/v/co-op-translator?color=4BA3FF)](https://pypi.org/project/co-op-translator/)
[![License: MIT](https://img.shields.io/github/license/azure/co-op-translator?color=4BA3FF)](https://github.com/azure/co-op-translator/blob/main/LICENSE)
[![Downloads](https://static.pepy.tech/badge/co-op-translator)](https://pepy.tech/project/co-op-translator)
[![Downloads](https://static.pepy.tech/badge/co-op-translator/month)](https://pepy.tech/project/co-op-translator)
[![Container: GHCR](https://img.shields.io/badge/Container-GHCR-2496ED?logo=docker&logoColor=fff)](https://github.com/azure/co-op-translator/pkgs/container/co-op-translator)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[![GitHub contributors](https://img.shields.io/github/contributors/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/graphs/contributors/)
[![GitHub issues](https://img.shields.io/github/issues/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/issues/)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/pulls/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

**Start here:** [ワークフローを選択](https://azure.github.io/co-op-translator/workflows/) | [設定](https://azure.github.io/co-op-translator/configuration/) | [CLI](https://azure.github.io/co-op-translator/cli/) | [Python API](https://azure.github.io/co-op-translator/api/) | [MCP Server](https://azure.github.io/co-op-translator/mcp/)

### 🌐 多言語サポート

#### Co-op Translator がサポートする言語

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[アラビア語](../ar/README.md) | [ベンガル語](../bn/README.md) | [ブルガリア語](../bg/README.md) | [ビルマ語（ミャンマー）](../my/README.md) | [中国語（簡体字）](../zh-CN/README.md) | [中国語（繁体字、香港）](../zh-HK/README.md) | [中国語（繁体字、マカオ）](../zh-MO/README.md) | [中国語（繁体字、台湾）](../zh-TW/README.md) | [クロアチア語](../hr/README.md) | [チェコ語](../cs/README.md) | [デンマーク語](../da/README.md) | [オランダ語](../nl/README.md) | [エストニア語](../et/README.md) | [フィンランド語](../fi/README.md) | [フランス語](../fr/README.md) | [ドイツ語](../de/README.md) | [ギリシャ語](../el/README.md) | [ヘブライ語](../he/README.md) | [ヒンディー語](../hi/README.md) | [ハンガリー語](../hu/README.md) | [インドネシア語](../id/README.md) | [イタリア語](../it/README.md) | [日本語](./README.md) | [カンナダ語](../kn/README.md) | [クメール語](../km/README.md) | [韓国語](../ko/README.md) | [リトアニア語](../lt/README.md) | [マレー語](../ms/README.md) | [マラヤーラム語](../ml/README.md) | [マラーティー語](../mr/README.md) | [ネパール語](../ne/README.md) | [ナイジェリア・ピジン語](../pcm/README.md) | [ノルウェー語](../no/README.md) | [ペルシア語（ファールシー）](../fa/README.md) | [ポーランド語](../pl/README.md) | [ポルトガル語（ブラジル）](../pt-BR/README.md) | [ポルトガル語（ポルトガル）](../pt-PT/README.md) | [パンジャブ語（グルムキー）](../pa/README.md) | [ルーマニア語](../ro/README.md) | [ロシア語](../ru/README.md) | [セルビア語（キリル）](../sr/README.md) | [スロバキア語](../sk/README.md) | [スロベニア語](../sl/README.md) | [スペイン語](../es/README.md) | [スワヒリ語](../sw/README.md) | [スウェーデン語](../sv/README.md) | [タガログ語（フィリピノ）](../tl/README.md) | [タミル語](../ta/README.md) | [テルグ語](../te/README.md) | [タイ語](../th/README.md) | [トルコ語](../tr/README.md) | [ウクライナ語](../uk/README.md) | [ウルドゥー語](../ur/README.md) | [ベトナム語](../vi/README.md)

> **ローカルにクローンする方がよいですか？**
>
> このリポジトリには50以上の言語翻訳が含まれており、ダウンロードサイズが大幅に増加します。翻訳を含めずにクローンするには、スパースチェックアウトを使用してください：
>
> **Bash / macOS / Linux:**
> ```bash
> git clone --filter=blob:none --sparse https://github.com/Azure/co-op-translator.git
> cd co-op-translator
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
>
> **CMD (Windows):**
> ```cmd
> git clone --filter=blob:none --sparse https://github.com/Azure/co-op-translator.git
> cd co-op-translator
> git sparse-checkout set --no-cone "/*" "!translations" "!translated_images"
> ```
>
> これにより、コースを完了するために必要なものがすべて得られ、ダウンロードがずっと高速になります。
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## 概要

**Co-op Translator** は、教育向けの GitHub コンテンツを複数の言語に簡単にローカライズするのを支援します。
Markdown ファイル、画像、ノートブックを更新すると、翻訳は自動的に同期され、世界中の学習者に対してコンテンツの正確性と最新性が保たれます。

CLI からリポジトリの翻訳を行ったり、Python API で自動化したり、エージェントや編集者向けのワークフローのために MCP サーバー経由で利用できます。

翻訳されたコンテンツの構成例：

![例](../../imgs/translation-ex.png)

## なぜ Co-op Translator を使うのか？

ファイル1つの翻訳は簡単です。ドキュメント全体のリポジトリを
翻訳・リンク・最新状態に保つことが難しい点です。

| 問題 | Co-op Translator が助ける方法 |
| --- | --- |
| 長いドキュメントは1つのプロンプトではない | 大きな Markdown ファイルはチャンクに分割されるため、長い README が1つの脆弱なモデル応答に依存することはありません。チャンクが失敗した場合、Co-op Translator は失敗した部分のみを再チャンクして再試行できます。 |
| 不完全な翻訳を最新として扱うべきではない | 切り詰められた翻訳が最新として確定されるべきではありません。Co-op Translator は保存前に翻訳の整合性をチェックし、構造的に不完全な既存の翻訳を検出できます。 |
| リンクは翻訳されたリポジトリ構造に一致するべき | 手動翻訳では相対リンクが元のツリーを指し続けることがよくあります。Co-op Translator は Markdown、ノートブック、画像、README のリンクを書き換え、`translations/<lang>/...` 構造に一致させます。 |
| 翻訳はリポジトリ全体で機能するべき | Co-op Translator は README ファイル、ドキュメント、ノートブック、画像のテキストを1つのリポジトリワークフローの一部として扱い、ファイルを一つずつ翻訳するのではなく一括で処理します。 |
| 翻訳の維持は一度作るより重要 | ソースハッシュと翻訳メタデータにより、Co-op Translator は古くなったファイルを見つけ、変更がないファイルをスキップし、ソースリポジトリが進化しても翻訳コンテンツを同期させ続けます。 |

## 翻訳状態はどのように管理されるか

Co-op Translator は翻訳されたコンテンツを<strong>静的ファイルではなく、バージョン管理されたソフトウェアアーティファクト</strong>として管理します。

このツールは <strong>言語スコープのメタデータ</strong> を使用して、翻訳された Markdown、画像、ノートブックの状態を追跡します。

この設計により、Co-op Translator は次を実現します：

- 古い翻訳を確実に検出する
- Markdown、画像、ノートブックを一貫して扱う
- 大規模で動きの速い多言語リポジトリでも安全にスケールする

翻訳を管理されたアーティファクトとしてモデル化することで、
翻訳ワークフローは現代の
ソフトウェア依存関係とアーティファクト管理プラクティスと自然に整合します。

→ [翻訳状態の管理について](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/rethinking-documentation-translation-treating-translations-as-versioned-software/4491755)

### 関連の詳細記事

- [Fixing Broken Markdown in AI Translation: Hardening a Production Pipeline](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/fixing-broken-markdown-in-ai-translation-hardening-a-production-pipeline/4511378)

## 始める

Co-op Translator は CLI、Python API、または MCP サーバーから利用できます。ローカル翻訳、自動化、CI、エージェント/エディタ統合のどれを選ぶか迷っている場合は、ワークフローガイドから始めてください。

- [ワークフローを選択](../../docs/workflows.md)
- [資格情報の設定](../../docs/configuration.md)
- [CLI から翻訳](../../docs/cli.md)
- [Python API で自動化](../../docs/api.md)
- [MCP サーバーと接続](../../docs/mcp.md)
- [GitHub Actions で実行](../../docs/github-actions.md)

設定後の最小の CLI 例：

```bash
python -m venv .venv
# ウィンドウズ
.venv\Scripts\activate
# macOS/リナックス
source .venv/bin/activate

pip install co-op-translator
translate -l "ko" -md
co-op-review -l "ko"
```

大規模なリポジトリで初回実行する場合は、翻訳ファイルを書き込む前に `--dry-run` を使用してください。コンテンツタイプフラグ、ログ、レビュー、リンク移行については [CLIリファレンス](../../docs/cli.md) を参照してください。

コンテナの簡単な実行（Bash/Zsh）:

```bash
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko" -md
```

コンテナの簡単な実行（PowerShell）:

```powershell
docker run --rm -it --env-file .env -v ${PWD}:/work ghcr.io/azure/co-op-translator:latest -l "ko" -md
```

## 機能

- Markdown、ノートブック、画像の自動翻訳
- ソースの変更と翻訳を同期して維持
- ローカル（CLI）や CI（GitHub Actions）で動作
- MCP を通じて Markdown、ノートブック、画像、レビュー、プロジェクト翻訳ツールを公開
- プロバイダー対応の翻訳に Azure OpenAI や OpenAI を使用
- MCP がエージェントをホストして、Co-op Translator の LLM 資格情報なしで Markdown やノートブックのチャンクを翻訳できるようにする
- 画像テキスト抽出と翻訳に Azure AI Vision を使用
- 決定論的チェックで翻訳の構造と鮮度をレビュー
- Markdown のフォーマットと構造を保持

## ドキュメント

- [ドキュメントサイト](https://azure.github.io/co-op-translator/)
- [ワークフローを選択](../../docs/workflows.md)
- [設定](../../docs/configuration.md)
- [Azure AI のセットアップ](../../docs/azure-ai-setup.md)
- [CLI リファレンス](../../docs/cli.md)
- [Python API](../../docs/api.md)
- [MCP サーバー](../../docs/mcp.md)
- [GitHub Actions](../../docs/github-actions.md)
- [README 言語テンプレート](../../docs/readme-languages-template.md)
- [サポートされている言語](../../docs/supported-languages.md)
- [コントリビューティング](../../CONTRIBUTING.md)
- [トラブルシューティング](../../docs/troubleshooting.md)

### Microsoft 固有のガイド
> [!NOTE]
> Microsoft の “For Beginners” リポジトリのメンテナー向けのみ。

- [“other courses” リストの更新（MS Beginners リポジトリ向け）](../../docs/microsoft-beginners.md)

## 私たちをサポートして、グローバルな学習を促進してください

教育コンテンツの世界的な共有方法を革命的に改善する取り組みに参加してください！GitHub で [Co-op Translator](https://github.com/azure/co-op-translator) に ⭐ を付けて、学習と技術における言語の壁を取り除く私たちのミッションを支援してください。あなたの関心と貢献は大きな影響を与えます！コードの貢献や機能提案は常に歓迎します。

### あなたの言語で Microsoft の教育コンテンツを探検しましょう
- [LangChain4j 入門](https://github.com/microsoft/LangChain4j-for-Beginners)
- [AZD 入門](https://github.com/microsoft/AZD-for-beginners)
- [Edge AI 入門](https://github.com/microsoft/edgeai-for-beginners)
- [Model Context Protocol (MCP) 入門](https://github.com/microsoft/mcp-for-beginners)
- [AIエージェント入門](https://github.com/microsoft/ai-agents-for-beginners)
- [.NETを使った生成AI入門](https://github.com/microsoft/Generative-AI-for-beginners-dotnet)
- [生成AI入門](https://github.com/microsoft/generative-ai-for-beginners)
- [Javaを使った生成AI入門](https://github.com/microsoft/generative-ai-for-beginners-java)
- [機械学習入門](https://aka.ms/ml-beginners)
- [データサイエンス入門](https://aka.ms/datascience-beginners)
- [AI入門](https://aka.ms/ai-beginners)
- [サイバーセキュリティ入門](https://github.com/microsoft/Security-101)
- [Web開発入門](https://aka.ms/webdev-beginners)
- [IoT入門](https://aka.ms/iot-beginners)
- [PhiCookBook](https://github.com/microsoft/PhiCookBook)

## ビデオプレゼンテーション

👉 下の画像をクリックして YouTube で視聴してください。

- **Open at Microsoft**: Co-op Translator の簡潔な18分の紹介と使い方のクイックガイド。

  [![Open at Microsoft](../../imgs/open-ms-thumbnail.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## 貢献

このプロジェクトでは、貢献や提案を歓迎します。Azure Co-op Translator に貢献したいですか？Co-op Translator をより利用しやすくするための支援方法については、[CONTRIBUTING.md](../../CONTRIBUTING.md) をご覧ください。

## 貢献者

[![co-op-translator 貢献者](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## 行動規範

このプロジェクトは [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/) を採用しています。
詳細については [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) を参照するか、追加の質問やコメントがある場合は [opencode@microsoft.com](mailto:opencode@microsoft.com) にご連絡ください。

## 責任ある AI

Microsoft は、お客様が当社の AI 製品を責任を持って使用できるよう支援し、知見を共有し、Transparency Notes や Impact Assessments のようなツールを通じて信頼に基づくパートナーシップを構築することに尽力しています。これらの多くのリソースは [https://aka.ms/RAI](https://aka.ms/RAI) で確認できます。
Microsoft の責任ある AI に対するアプローチは、公平性、信頼性と安全性、プライバシーとセキュリティ、包括性、透明性、説明責任といった AI 原則に基づいています。

このサンプルで使用されているような大規模な自然言語、画像、音声モデルは、不公平、信頼性の欠如、攻撃的な振る舞いを示し、結果として害を引き起こす可能性があります。リスクと制限については、[Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) を参照してください。

これらのリスクを軽減するための推奨アプローチは、有害な振る舞いを検出し防止できる安全システムをアーキテクチャに組み込むことです。[Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) は、アプリケーションやサービス内のユーザー生成コンテンツや AI 生成コンテンツの有害性を検出できる独立した防護レイヤーを提供します。Azure AI Content Safety には、有害な素材を検出するためのテキストおよび画像の API が含まれています。さらに、異なるモダリティにわたる有害コンテンツを検出するサンプルコードを表示、探索、試すことができるインタラクティブな Content Safety Studio も提供しています。次の [クイックスタート ドキュメント](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) は、サービスへのリクエストの作成手順を案内します。

もう一つ考慮すべき側面は、全体のアプリケーションパフォーマンスです。マルチモーダルかつマルチモデルのアプリケーションでは、パフォーマンスとは、ユーザーやあなたが期待する通りにシステムが動作すること、そして有害な出力を生成しないことを意味します。全体のアプリケーションのパフォーマンスを評価するために、[生成品質およびリスクと安全性の指標](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in) を使用して評価することが重要です。

開発環境で AI アプリケーションを評価するには、[prompt flow SDK](https://microsoft.github.io/promptflow/index.html) を使用できます。テストデータセットまたはターゲットを与えると、生成系 AI アプリケーションの生成物は、組み込みの評価器やカスタム評価器で定量的に測定されます。システムを評価するために prompt flow sdk を使用して開始するには、[クイックスタート ガイド](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk) に従ってください。評価実行を行うと、結果を [Azure AI Studio で可視化](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results) できます。

## 商標

このプロジェクトには、プロジェクト、製品、サービスの商標やロゴが含まれている場合があります。Microsoft の商標やロゴの正当な使用は [Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general) に従う必要があります。
このプロジェクトの改変版における Microsoft の商標やロゴの使用は、混乱を招いたり Microsoft の後援を示唆したりしてはなりません。
サードパーティの商標やロゴの使用は、それらのサードパーティのポリシーに従います。

## ヘルプ

AI アプリの構築で行き詰まったり質問がある場合は、以下に参加してください：

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

製品に関するフィードバックや構築中のエラーがある場合は、次を参照してください：

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)