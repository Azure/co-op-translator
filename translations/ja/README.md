<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "329abbc9354793ea422f7e7ebf66be2c",
  "translation_date": "2025-05-07T01:51:09+00:00",
  "source_file": "README.md",
  "language_code": "ja"
}
-->
![Logo](../../imgs/logo.png)

# Co-op Translator: 教育ドキュメントの翻訳を簡単に自動化

_ドキュメントを複数言語に簡単に自動翻訳し、世界中のユーザーに届けましょう。_

[![Python package](https://img.shields.io/pypi/v/co-op-translator?color=4BA3FF)](https://pypi.org/project/co-op-translator/)
[![License: MIT](https://img.shields.io/github/license/azure/co-op-translator?color=4BA3FF)](https://github.com/azure/co-op-translator/blob/main/LICENSE)
[![Downloads](https://static.pepy.tech/badge/co-op-translator)](https://pepy.tech/project/co-op-translator)
[![Downloads](https://static.pepy.tech/badge/co-op-translator/month)](https://pepy.tech/project/co-op-translator)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[![GitHub contributors](https://img.shields.io/github/contributors/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/graphs/contributors/)
[![GitHub issues](https://img.shields.io/github/issues/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/issues/)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/pulls/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

### Co-op Translator が支える言語サポート

[Korean](../ko/README.md) | [Japanese](./README.md) | [Chinese (Simplified)](../zh/README.md) | [Chinese (Traditional, Taiwan)](../tw/README.md) | [Spanish](../es/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Portuguese (Brazil)](../br/README.md) | [Hindi](../hi/README.md) | [Russian](../ru/README.md) | [Turkish](../tr/README.md) | [Arabic](../ar/README.md) | [Indonesian](../id/README.md) | [Vietnamese](../vi/README.md)

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator.svg?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Azure AI Community Discord](https://dcbadge.vercel.app/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)
[![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=VS%20Code%20Dev%20Containers&message=Open&color=007ACC&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator)

> [!TIP]
> **強力な自動化**: GitHub Actionsに対応しました！リポジトリの変更に応じてドキュメントを自動で翻訳し、手間なく常に最新の状態を保てます。[詳細はこちら](../..)。

## 対応モデルとサービス

| 種類                  | 名前                           |
|-----------------------|--------------------------------|
| 言語モデル            | ![Azure OpenAI](https://img.shields.io/badge/Azure_OpenAI-blue?style=flat-square) ![OpenAI](https://img.shields.io/badge/OpenAI-green?style=flat-square&logo=openai) |
| コンピュータビジョン  | ![Azure Computer Vision](https://img.shields.io/badge/Azure_Computer_Vision-blue?style=flat-square) |

> [!NOTE]
> コンピュータビジョンサービスが利用できない場合、co-op translatorは[Markdownのみモード](./getting_started/markdown-only-mode.md)に切り替わります。

## 概要: 教育コンテンツの翻訳を効率化

言語の壁は、世界中の学習者や開発者が貴重な教育リソースや技術知識にアクセスする上で大きな障害となっています。これにより参加が制限され、グローバルなイノベーションや学習の速度が遅れてしまいます。

**Co-op Translator** は、Microsoft自身の大規模な教育シリーズ（「For Beginners」ガイドなど）の非効率な手動翻訳プロセスを解決する必要から生まれました。使いやすく強力なツールへと進化し、誰もが言語の壁を越えられるように設計されています。CLIやGitHub Actionsを通じて高品質な自動翻訳を提供することで、教育者、学生、研究者、開発者が言語の制約なく知識を共有・利用できるよう支援します。

Co-op Translatorが翻訳された教育コンテンツをどのように整理するかをご覧ください：

![例](../../imgs/translation-ex.png)

Markdownファイルや画像内のテキストは自動的に翻訳され、言語ごとのフォルダーにきれいに整理されます。

**Co-op Translatorで教育コンテンツを世界中に届けましょう！**

## Microsoftの学習リソースのグローバルアクセス支援

Co-op Translatorは、グローバルな開発者コミュニティに向けた主要なMicrosoft教育イニシアチブの言語の壁を越える手助けをし、リポジトリの翻訳プロセスを自動化しています。現在Co-op Translatorを利用している例：

[![ML-For-Beginners](https://github-readme-stats.vercel.app/api/pin/?username=microsoft&repo=ML-For-Beginners&bg_color=ffffff&title_color=0078D4&text_color=333333&border_color=c0d8f0&border_radius=10)](https://github.com/microsoft/ML-For-Beginners)
[![Generative-AI-for-beginners-dotnet](https://github-readme-stats.vercel.app/api/pin/?username=microsoft&repo=Generative-AI-for-beginners-dotnet&bg_color=ffffff&title_color=0078D4&text_color=333333&border_color=c0d8f0&border_radius=10)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet)
[![AI-For-Beginners](https://github-readme-stats.vercel.app/api/pin/?username=microsoft&repo=AI-For-Beginners&bg_color=ffffff&title_color=0078D4&text_color=333333&border_color=c0d8f0&border_radius=10)](https://github.com/microsoft/AI-For-Beginners)
[![ai-agents-for-beginners](https://github-readme-stats.vercel.app/api/pin/?username=microsoft&repo=ai-agents-for-beginners&bg_color=ffffff&title_color=0078D4&text_color=333333&border_color=c0d8f0&border_radius=10)](https://github.com/microsoft/ai-agents-for-beginners)
[![PhiCookBook](https://github-readme-stats.vercel.app/api/pin/?username=microsoft&repo=PhiCookBook&bg_color=ffffff&title_color=0078D4&text_color=333333&border_color=c0d8f0&border_radius=10)](https://github.com/microsoft/PhiCookBook)

## 主な特徴

- **自動翻訳**: 複数言語へのテキスト翻訳を手軽に実行。
- **GitHub Actions連携**: CI/CDパイプラインの一部として翻訳を自動化。
- **Markdownの保持**: 翻訳時に正しいMarkdown構文を維持。
- **画像内テキスト翻訳**: 画像に含まれるテキストを抽出して翻訳。
- **高度なLLM技術**: 最新の言語モデルを活用し高品質な翻訳を実現。
- **簡単な統合**: 既存のプロジェクトにスムーズに組み込み可能。
- **ローカライズの簡素化**: 国際市場向けのローカライズ作業を効率化。

## 動作の仕組み

![アーキテクチャ](../../imgs/architecture_241019.png)

Co-op Translatorは、プロジェクトフォルダー内のMarkdownファイルと画像を以下のように処理します：

1. **テキスト抽出**: Markdownファイルからテキストを抽出し、設定によっては（例：Azure Computer Vision）画像内のテキストも抽出します。
1. **AI翻訳**: 抽出したテキストを設定されたLLM（Azure OpenAI、OpenAIなど）に送り翻訳を行います。
1. **結果保存**: 翻訳済みのMarkdownファイルと画像（翻訳済みテキスト付き）を言語別フォルダーに保存し、元のフォーマットを保持します。

## はじめに

CLIで素早く始めるか、GitHub Actionsで完全自動化を設定しましょう。

### クイックスタート：コマンドライン

コマンドラインで手早く始めるには：

1. パッケージをインストール：
    ```bash
    pip install co-op-translator
    ```
2. 認証情報を設定：
  - `.env` file in your project's root directory.
  - Copy the contents from the [.env.template](../../.env.template) file into your new `.env` file.
  - Fill in the required API keys and endpoint information in your `.env` file.
3. Run Translation:
  - Navigate to your project's root directory in your terminal.
  - Execute the translate command, specifying target languages with the `-l`フラグを使って設定：
    ```bash
    translate -l "ko ja fr"
    ```
    *(リポジトリ内の`"ko ja fr"` with your desired space-separated language codes)*

### Detailed Usage Guides

Choose the approach that best fits your workflow:

#### 1. Using the Command Line (CLI)

- Best for: One-time translations, manual control, or integration into custom scripts.
- Requires: Local installation of Python and the `co-op-translator` package.
- Guide: [Command Line Guide](./getting_started/command-line-guide/command-line-guide.md)

#### 2. Using GitHub Actions (Automation)

- Best for: Automatically translating content whenever changes are pushed to your repository. Keeps translations consistently up-to-date.
- Requires: Setting up a workflow file (`.github/workflows`を置き換えてください。ローカルインストールは不要です。*
- ガイド：
  - [GitHub Actionsガイド（パブリックリポジトリ＆標準シークレット対応）](./getting_started/github-actions-guide/github-actions-guide-public.md) - 標準のリポジトリシークレットを使うほとんどのパブリックや個人リポジトリに最適です。
  - [GitHub Actionsガイド（Microsoft組織リポジトリ＆組織レベル設定対応）](./getting_started/github-actions-guide/github-actions-guide-org.md) - Microsoft GitHub組織内で作業する場合や組織レベルのシークレットやランナーを利用する場合はこちらを参照してください。

> [!NOTE]
> このチュートリアルはAzureリソースに焦点を当てていますが、[対応モデルとサービス](../..)リストにある任意の言語モデルを使用できます。

### トラブルシューティングとヒント

- [トラブルシューティングガイド](./getting_started/troubleshooting.md)

### 追加リソース

- [コマンドリファレンス](./getting_started/command-reference.md): 利用可能なコマンドとオプションの詳細ガイド。
- [多言語対応セットアップ](./getting_started/multi-language-support.md): READMEに翻訳版へのリンクテーブルを追加する方法。
- [対応言語一覧](./getting_started/supported-languages.md): 対応言語の一覧と新規追加手順。
- [Markdownのみモード](./getting_started/markdown-only-mode.md): 画像翻訳なしでテキストのみを翻訳する方法。

## ビデオプレゼンテーション

Co-op Translatorについて詳しくはプレゼンテーションをご覧ください（下の画像をクリックするとYouTubeで視聴できます）：

- **Open at Microsoft**: 18分の簡単な紹介と使い方ガイド。

  [![Open at Microsoft](../../imgs/open-ms-thumbnail.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

- **Microsoft Reactor**: 1時間にわたる詳細なステップバイステップガイド。Co-op Translatorの概要、セットアップ、効果的な使い方、実演デモまでカバー。

  [![Microsoft Reactor](../../imgs/reactor-thumbnail.jpg)](https://www.youtube.com/watch?v=boTtKVPBLAc)

## ご支援とグローバル学習の促進

教育コンテンツの世界的な共有方法を一緒に変革しましょう！[Co-op Translator](https://github.com/azure/co-op-translator)にGitHubで⭐をつけて、学習と技術における言語の壁を打破する私たちのミッションを応援してください。皆さまの関心と貢献が大きな力になります！コード貢献や機能提案も常に歓迎しています。

## コントリビューション

このプロジェクトでは貢献や提案を歓迎しています。Azure Co-op Translatorへの参加に興味がある方は、[CONTRIBUTING.md](./CONTRIBUTING.md)をご覧いただき、Co-op Translatorをより使いやすくするための支援方法をご確認ください。

## コントリビューター

[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## 行動規範

このプロジェクトは[Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/)を採用しています。詳細は[行動規範FAQ](https://opensource.microsoft.com/codeofconduct/faq/)をご覧いただくか、ご質問やコメントは[opencode@microsoft.com](mailto:opencode@microsoft.com)までお問い合わせください。

## 責任あるAI

Microsoftは、お客様がAI製品を責任を持って利用できるよう支援し、学びを共有し、Transparency NotesやImpact Assessmentsなどのツールを通じて信頼に基づくパートナーシップを築くことにコミットしています。これらのリソースは多くが[https://aka.ms/RAI](https://aka.ms/RAI)で入手可能です。Microsoftの責任あるAIへの取り組みは、公平性、信頼性と安全性、プライバシーとセキュリティ、包括性、透明性、説明責任というAI原則に基づいています。

このサンプルで使用されているような大規模な自然言語、画像、音声モデルは、不公平、不信頼、攻撃的な挙動を示す可能性があり、それが害を引き起こすことがあります。リスクと制限については、[Azure OpenAIサービス Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text)をご参照ください。
これらのリスクを軽減する推奨される方法は、アーキテクチャに安全システムを組み込み、有害な行動を検出・防止できるようにすることです。[Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview)は独立した保護レイヤーを提供し、アプリケーションやサービス内の有害なユーザー生成コンテンツやAI生成コンテンツを検出できます。Azure AI Content Safetyには、有害な素材を検出できるテキストおよび画像APIが含まれています。また、インタラクティブなContent Safety Studioがあり、異なるモダリティで有害なコンテンツを検出するサンプルコードを閲覧、探索、試すことができます。以下の[クイックスタートドキュメント](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest)では、サービスへのリクエスト方法を案内しています。

もう一つ考慮すべき点は、全体的なアプリケーションのパフォーマンスです。マルチモーダルかつマルチモデルのアプリケーションにおいて、パフォーマンスとはシステムがあなたやユーザーの期待通りに動作し、有害な出力を生成しないことを意味します。全体のアプリケーションパフォーマンスを[生成品質およびリスク・安全性指標](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in)を使って評価することが重要です。

開発環境でAIアプリケーションを評価するには、[prompt flow SDK](https://microsoft.github.io/promptflow/index.html)を使用できます。テストデータセットやターゲットを与えると、生成AIアプリケーションの生成物は組み込みの評価器やお好みのカスタム評価器で定量的に測定されます。prompt flow sdkを使ってシステムを評価するには、[クイックスタートガイド](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk)に従ってください。評価実行後は、[Azure AI Studioで結果を可視化](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results)できます。

## トレードマーク

このプロジェクトには、プロジェクト、製品、サービスのトレードマークやロゴが含まれている場合があります。Microsoftのトレードマークやロゴの使用は、[Microsoftのトレードマーク＆ブランドガイドライン](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general)に従い、許可された範囲内で行う必要があります。このプロジェクトの改変版でMicrosoftのトレードマークやロゴを使用する場合、混乱を招いたりMicrosoftの後援を示唆したりしてはいけません。第三者のトレードマークやロゴの使用は、それら第三者のポリシーに従います。

**免責事項**：  
本書類はAI翻訳サービス[Co-op Translator](https://github.com/Azure/co-op-translator)を使用して翻訳されています。正確性を期しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご了承ください。原文はその言語における正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じた誤解や誤訳について、一切の責任を負いかねます。