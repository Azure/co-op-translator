<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "18318279bb851dc2c709bfc6a26f6e1d",
  "translation_date": "2025-05-07T13:58:28+00:00",
  "source_file": "README.md",
  "language_code": "ja"
}
-->
![Logo](../../imgs/logo.png)

# Co-op Translator: 教育ドキュメントの翻訳を簡単に自動化

_ドキュメントの翻訳を複数言語に簡単に自動化し、世界中のユーザーに届けましょう。_

[![Python package](https://img.shields.io/pypi/v/co-op-translator?color=4BA3FF)](https://pypi.org/project/co-op-translator/)
[![License: MIT](https://img.shields.io/github/license/azure/co-op-translator?color=4BA3FF)](https://github.com/azure/co-op-translator/blob/main/LICENSE)
[![Downloads](https://static.pepy.tech/badge/co-op-translator)](https://pepy.tech/project/co-op-translator)
[![Downloads](https://static.pepy.tech/badge/co-op-translator/month)](https://pepy.tech/project/co-op-translator)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[![GitHub contributors](https://img.shields.io/github/contributors/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/graphs/contributors/)
[![GitHub issues](https://img.shields.io/github/issues/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/issues/)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/pulls/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

### Co-op Translatorによる言語サポート

[Korean](../ko/README.md) | [Japanese](./README.md) | [Chinese (Simplified)](../zh/README.md) | [Chinese (Traditional, Taiwan)](../tw/README.md) | [Spanish](../es/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Portuguese (Brazil)](../br/README.md) | [Hindi](../hi/README.md) | [Russian](../ru/README.md) | [Turkish](../tr/README.md) | [Arabic](../ar/README.md) | [Indonesian](../id/README.md) | [Vietnamese](../vi/README.md)

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator.svg?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Azure AI Community Discord](https://dcbadge.vercel.app/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)
[![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=VS%20Code%20Dev%20Containers&message=Open&color=007ACC&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator)

> [!TIP]
> **強力な自動化**: GitHub Actions に対応しました！リポジトリに変更が加えられると、自動的にドキュメントを翻訳し、常に最新の状態を簡単に保てます。[詳しくはこちら](../..)。

## 対応モデルとサービス

| 種類                  | 名前                           |
|-----------------------|--------------------------------|
| Language Model        | ![Azure OpenAI](https://img.shields.io/badge/Azure_OpenAI-blue?style=flat-square) ![OpenAI](https://img.shields.io/badge/OpenAI-green?style=flat-square&logo=openai) |
| Computer Vision       | ![Azure Computer Vision](https://img.shields.io/badge/Azure_Computer_Vision-blue?style=flat-square) |

> [!NOTE]
> コンピュータビジョンサービスが利用できない場合、co-op translator は[Markdownのみモード](./getting_started/markdown-only-mode.md)に切り替わります。

## 概要: 教育コンテンツの翻訳を効率化

言語の壁は、世界中の学習者や開発者が貴重な教育リソースや技術知識にアクセスするのを大きく妨げています。これにより参加が制限され、世界的なイノベーションや学習のスピードが遅くなっています。

**Co-op Translator** は、Microsoft 自身の大規模教育シリーズ（例えば「For Beginners」ガイド）の非効率な手動翻訳プロセスを解決する必要から生まれました。使いやすく強力なツールへと進化し、誰もが言語の壁を越えられるよう設計されています。CLI と GitHub Actions を通じて高品質な自動翻訳を提供することで、教育者、学生、研究者、開発者が言語の制約なしに知識を共有・アクセスできるよう支援します。

Co-op Translator が翻訳された教育コンテンツをどのように整理するかをご覧ください：

![Example](../../imgs/translation-ex.png)

Markdown ファイルと画像内のテキストは自動的に翻訳され、言語ごとのフォルダーにきれいに整理されます。

**今すぐ Co-op Translator で教育コンテンツのグローバルアクセスを実現しましょう！**

## Microsoft の学習リソースのグローバルアクセス支援

Co-op Translator は、グローバルな開発者コミュニティ向けのリポジトリの翻訳プロセスを自動化し、Microsoft の主要な教育イニシアティブの言語の壁を橋渡しします。現在 Co-op Translator を利用している例：

[![ML-For-Beginners](https://github-readme-stats.vercel.app/api/pin/?username=microsoft&repo=ML-For-Beginners&bg_color=ffffff&title_color=0078D4&text_color=333333&border_color=c0d8f0&border_radius=10)](https://github.com/microsoft/ML-For-Beginners)
[![Generative-AI-for-beginners-dotnet](https://github-readme-stats.vercel.app/api/pin/?username=microsoft&repo=Generative-AI-for-beginners-dotnet&bg_color=ffffff&title_color=0078D4&text_color=333333&border_color=c0d8f0&border_radius=10)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet)
[![AI-For-Beginners](https://github-readme-stats.vercel.app/api/pin/?username=microsoft&repo=AI-For-Beginners&bg_color=ffffff&title_color=0078D4&text_color=333333&border_color=c0d8f0&border_radius=10)](https://github.com/microsoft/AI-For-Beginners)
[![ai-agents-for-beginners](https://github-readme-stats.vercel.app/api/pin/?username=microsoft&repo=ai-agents-for-beginners&bg_color=ffffff&title_color=0078D4&text_color=333333&border_color=c0d8f0&border_radius=10)](https://github.com/microsoft/ai-agents-for-beginners)
[![PhiCookBook](https://github-readme-stats.vercel.app/api/pin/?username=microsoft&repo=PhiCookBook&bg_color=ffffff&title_color=0078D4&text_color=333333&border_color=c0d8f0&border_radius=10)](https://github.com/microsoft/PhiCookBook)

## 主な特徴

- **自動翻訳**: テキストを複数の言語に手間なく翻訳。
- **GitHub Actions 連携**: CI/CD パイプラインの一部として翻訳を自動化。
- **Markdown の保持**: 翻訳時も正しい Markdown 構文を維持。
- **画像内テキスト翻訳**: 画像内のテキストを抽出して翻訳。
- **高度な LLM 技術**: 最新の言語モデルを使った高品質な翻訳。
- **簡単な統合**: 既存のプロジェクトにスムーズに組み込み可能。
- **ローカリゼーションの簡素化**: 国際市場向けのローカライズ作業を効率化。

## 動作の仕組み

![Architecture](../../imgs/architecture_241019.png)

Co-op Translator はプロジェクトフォルダーの Markdown ファイルと画像を以下のように処理します：

1. **テキスト抽出**: Markdown ファイルからテキストを抽出し、設定によっては（例：Azure Computer Vision）画像内のテキストも抽出します。
1. **AI 翻訳**: 抽出したテキストを設定された LLM（Azure OpenAI、OpenAI など）に送信して翻訳。
1. **結果保存**: 翻訳済みの Markdown ファイルと画像（翻訳済みテキスト入り）を言語別フォルダーに保存し、元のフォーマットを保持。

## はじめに

> [!NOTE]
> このチュートリアルは Azure リソースを中心に説明していますが、[対応モデルとサービス](../..) の一覧にある任意の言語モデルを利用可能です。

CLI で手早く始めるか、GitHub Actions で完全自動化を設定しましょう。

### 初期設定

- [Azure AI のセットアップ](./getting_started/set-up-azure-ai.md)

### クイックスタート: コマンドライン

コマンドラインで素早く始めるには：

1. パッケージをインストール：
    ```bash
    pip install co-op-translator
    ```
2. 資格情報を設定：
  - プロジェクトのルート ディレクトリにある `.env` ファイル。
  - Copy the contents from the [.env.template](../../.env.template) file into your new `.env` file.
  - Fill in the required API keys and endpoint information in your `.env` file.
3. Run Translation:
  - Navigate to your project's root directory in your terminal.
  - Execute the translate command, specifying target languages with the `-l` フラグを作成：
    ```bash
    translate -l "ko ja fr"
    ```
    *(リポジトリ内の `"ko ja fr"` with your desired space-separated language codes)*

### Detailed Usage Guides

Choose the approach that best fits your workflow:

#### 1. Using the Command Line (CLI)

- Best for: One-time translations, manual control, or integration into custom scripts.
- Requires: Local installation of Python and the `co-op-translator` package.
- Guide: [Command Line Guide](./getting_started/command-line-guide/command-line-guide.md)

#### 2. Using GitHub Actions (Automation)

- Best for: Automatically translating content whenever changes are pushed to your repository. Keeps translations consistently up-to-date.
- Requires: Setting up a workflow file (`.github/workflows` を置き換えてください。ローカルインストールは不要です。)
- ガイド：
  - [GitHub Actions ガイド（パブリックリポジトリ＆標準シークレット用）](./getting_started/github-actions-guide/github-actions-guide-public.md) - 標準のリポジトリシークレットを使うパブリックまたは個人リポジトリ向け。
  - [GitHub Actions ガイド（Microsoft組織リポジトリ＆組織レベル設定用）](./getting_started/github-actions-guide/github-actions-guide-org.md) - Microsoft GitHub 組織内で作業する場合や組織レベルのシークレットやランナーを利用する場合はこちら。

### トラブルシューティングとヒント

- [トラブルシューティングガイド](./getting_started/troubleshooting.md)

### 追加リソース

- [コマンドリファレンス](./getting_started/command-reference.md): 利用可能なすべてのコマンドとオプションの詳細ガイド。
- [多言語対応設定](./getting_started/multi-language-support.md): README に翻訳版へのリンクテーブルを追加する方法。
- [対応言語](./getting_started/supported-languages.md): 対応言語の一覧と新しい言語の追加手順。
- [Markdownのみモード](./getting_started/markdown-only-mode.md): 画像翻訳なしでテキストのみを翻訳する方法。

## ビデオプレゼンテーション

Co-op Translator についてのプレゼンテーションを動画で学べます（下の画像をクリックすると YouTube で視聴できます）：

- **Open at Microsoft**: 18分の簡単な紹介と使い方ガイド。

  [![Open at Microsoft](../../imgs/open-ms-thumbnail.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

- **Microsoft Reactor**: Co-op Translator の概要から設定、実践的な使い方、ライブデモまで1時間で詳しく解説。

  [![Microsoft Reactor](../../imgs/reactor-thumbnail.jpg)](https://www.youtube.com/watch?v=boTtKVPBLAc)

## 私たちをサポートし、グローバルな学びを促進しましょう

教育コンテンツのグローバル共有のあり方を変革する取り組みに参加しませんか？[Co-op Translator](https://github.com/azure/co-op-translator) に GitHub で⭐を付けて、学習と技術の言語の壁を打ち破るミッションを応援してください。皆さまの関心と貢献が大きな力になります！コードの貢献や機能提案も歓迎します。

## コントリビューション

このプロジェクトは貢献や提案を歓迎しています。Azure Co-op Translator への貢献に興味がある方は、[CONTRIBUTING.md](./CONTRIBUTING.md) をご覧ください。Co-op Translator をより多くの人に届けるための手助け方法を記載しています。

## コントリビューター

[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## 行動規範

このプロジェクトは [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/) を採用しています。
詳細は [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) をご覧いただくか、
ご質問やご意見は [opencode@microsoft.com](mailto:opencode@microsoft.com) までご連絡ください。

## Responsible AI

Microsoft は、お客様が AI 製品を責任を持って利用できるよう支援し、学びを共有し、Transparency Notes や Impact Assessments などのツールを通じて信頼に基づくパートナーシップを築くことにコミットしています。これらのリソースの多くは [https://aka.ms/RAI](https://aka.ms/RAI) でご覧いただけます。
Microsoft の責任ある AI への取り組みは、公平性、信頼性と安全性、プライバシーとセキュリティ、包括性、透明性、説明責任という AI 原則に基づいています。
大規模な自然言語、画像、音声モデル—このサンプルで使用されているもののような—は、不公平であったり信頼性に欠けたり、不快感を与える振る舞いをする可能性があり、その結果として被害をもたらすことがあります。リスクや制限について理解するために、[Azure OpenAI サービスの透明性ノート](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text)をご参照ください。

これらのリスクを軽減する推奨される方法は、有害な振る舞いを検知・防止できる安全システムをアーキテクチャに組み込むことです。[Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview)は独立した保護レイヤーを提供し、アプリケーションやサービス内のユーザー生成およびAI生成の有害コンテンツを検出できます。Azure AI Content Safetyには、有害な素材を検出するためのテキストおよび画像APIが含まれています。また、異なるモダリティにわたる有害コンテンツ検出のサンプルコードを閲覧、探索、試用できるインタラクティブなContent Safety Studioも用意されています。以下の[クイックスタートドキュメント](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest)では、サービスへのリクエスト方法を案内しています。

もう一つ考慮すべき点は、全体のアプリケーションパフォーマンスです。マルチモーダルかつマルチモデルのアプリケーションにおいては、パフォーマンスとはシステムがユーザーや開発者の期待通りに動作し、有害な出力を生成しないことを意味します。全体のアプリケーションのパフォーマンスを評価するために、[生成品質およびリスクと安全性の指標](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in)を活用することが重要です。

開発環境でAIアプリケーションを評価するには、[prompt flow SDK](https://microsoft.github.io/promptflow/index.html)を使用できます。テストデータセットまたはターゲットを用意すると、生成AIアプリケーションの生成結果を組み込み評価器やカスタム評価器で定量的に測定できます。prompt flow SDKを使ってシステムを評価するには、[クイックスタートガイド](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk)に従ってください。評価実行後は、[Azure AI Studioで結果を可視化](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results)できます。

## 商標

このプロジェクトには、プロジェクト、製品、サービスの商標やロゴが含まれている場合があります。Microsoftの商標やロゴの使用は、[Microsoftの商標およびブランドガイドライン](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general)に従い、許可された範囲内で行われなければなりません。
本プロジェクトの修正バージョンでMicrosoftの商標やロゴを使用する場合、混乱を招いたりMicrosoftの支援を示唆したりしてはなりません。
第三者の商標やロゴの使用は、それら第三者のポリシーに従う必要があります。

**免責事項**：  
本書類はAI翻訳サービス[Co-op Translator](https://github.com/Azure/co-op-translator)を使用して翻訳されています。正確性を期していますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご理解ください。原文の言語によるオリジナル文書が正式な情報源とみなされます。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の使用により生じた誤解や誤訳について、当方は一切責任を負いかねます。
