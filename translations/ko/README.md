<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "18318279bb851dc2c709bfc6a26f6e1d",
  "translation_date": "2025-05-07T13:56:59+00:00",
  "source_file": "README.md",
  "language_code": "ko"
}
-->
![Logo](../../imgs/logo.png)

# Co-op Translator: 교육 문서 번역을 손쉽게 자동화하세요

_문서를 여러 언어로 자동 번역하여 전 세계 사용자에게 쉽게 다가가세요._

[![Python package](https://img.shields.io/pypi/v/co-op-translator?color=4BA3FF)](https://pypi.org/project/co-op-translator/)
[![License: MIT](https://img.shields.io/github/license/azure/co-op-translator?color=4BA3FF)](https://github.com/azure/co-op-translator/blob/main/LICENSE)
[![Downloads](https://static.pepy.tech/badge/co-op-translator)](https://pepy.tech/project/co-op-translator)
[![Downloads](https://static.pepy.tech/badge/co-op-translator/month)](https://pepy.tech/project/co-op-translator)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[![GitHub contributors](https://img.shields.io/github/contributors/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/graphs/contributors/)
[![GitHub issues](https://img.shields.io/github/issues/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/issues/)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/pulls/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

### Co-op Translator가 지원하는 언어

[Korean](./README.md) | [Japanese](../ja/README.md) | [Chinese (Simplified)](../zh/README.md) | [Chinese (Traditional, Taiwan)](../tw/README.md) | [Spanish](../es/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Portuguese (Brazil)](../br/README.md) | [Hindi](../hi/README.md) | [Russian](../ru/README.md) | [Turkish](../tr/README.md) | [Arabic](../ar/README.md) | [Indonesian](../id/README.md) | [Vietnamese](../vi/README.md)

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator.svg?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Azure AI Community Discord](https://dcbadge.vercel.app/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)
[![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=VS%20Code%20Dev%20Containers&message=Open&color=007ACC&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator)

> [!TIP]
>
> **강력한 자동화**: 이제 GitHub Actions를 지원합니다! 저장소에 변경 사항이 생기면 문서가 자동으로 번역되어 항상 최신 상태를 손쉽게 유지할 수 있습니다. [자세히 알아보기](../..).

## 지원되는 모델 및 서비스

| 유형                   | 이름                             |
|------------------------|---------------------------------|
| Language Model         | ![Azure OpenAI](https://img.shields.io/badge/Azure_OpenAI-blue?style=flat-square) ![OpenAI](https://img.shields.io/badge/OpenAI-green?style=flat-square&logo=openai) |
| Computer Vision        | ![Azure Computer Vision](https://img.shields.io/badge/Azure_Computer_Vision-blue?style=flat-square) |

> [!NOTE]
> 컴퓨터 비전 서비스가 제공되지 않는 경우, co-op translator는 [Markdown-only mode](./getting_started/markdown-only-mode.md)로 전환됩니다.

## 개요: 교육 콘텐츠 번역 간소화

언어 장벽은 전 세계 학습자와 개발자가 귀중한 교육 자료와 기술 지식에 접근하는 데 큰 장애물이 됩니다. 이는 참여를 제한하고 글로벌 혁신과 학습의 속도를 늦춥니다.

**Co-op Translator**는 Microsoft의 대규모 교육 시리즈(예: "For Beginners" 가이드)의 비효율적인 수동 번역 과정을 해결하기 위해 탄생했습니다. 누구나 쉽게 사용할 수 있는 강력한 도구로 발전하여 이러한 장벽을 허물고자 합니다. CLI와 GitHub Actions를 통해 고품질 자동 번역을 제공함으로써, 전 세계 교육자, 학생, 연구원, 개발자가 언어의 제약 없이 지식을 공유하고 접근할 수 있도록 지원합니다.

Co-op Translator가 번역된 교육 콘텐츠를 어떻게 정리하는지 확인해보세요:

![Example](../../imgs/translation-ex.png)

Markdown 파일과 이미지 내 텍스트가 자동으로 번역되어 언어별 폴더에 깔끔하게 정리됩니다.

**지금 바로 Co-op Translator로 교육 콘텐츠의 글로벌 접근성을 열어보세요!**

## Microsoft 학습 자료의 글로벌 접근성 지원

Co-op Translator는 글로벌 개발자 커뮤니티를 위한 주요 Microsoft 교육 프로젝트의 언어 장벽을 해소하고, 저장소의 번역 프로세스를 자동화하는 데 도움을 줍니다. 현재 Co-op Translator를 사용하는 예시는 다음과 같습니다:

[![ML-For-Beginners](https://github-readme-stats.vercel.app/api/pin/?username=microsoft&repo=ML-For-Beginners&bg_color=ffffff&title_color=0078D4&text_color=333333&border_color=c0d8f0&border_radius=10)](https://github.com/microsoft/ML-For-Beginners)
[![Generative-AI-for-beginners-dotnet](https://github-readme-stats.vercel.app/api/pin/?username=microsoft&repo=Generative-AI-for-beginners-dotnet&bg_color=ffffff&title_color=0078D4&text_color=333333&border_color=c0d8f0&border_radius=10)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet)
[![AI-For-Beginners](https://github-readme-stats.vercel.app/api/pin/?username=microsoft&repo=AI-For-Beginners&bg_color=ffffff&title_color=0078D4&text_color=333333&border_color=c0d8f0&border_radius=10)](https://github.com/microsoft/AI-For-Beginners)
[![ai-agents-for-beginners](https://github-readme-stats.vercel.app/api/pin/?username=microsoft&repo=ai-agents-for-beginners&bg_color=ffffff&title_color=0078D4&text_color=333333&border_color=c0d8f0&border_radius=10)](https://github.com/microsoft/ai-agents-for-beginners)
[![PhiCookBook](https://github-readme-stats.vercel.app/api/pin/?username=microsoft&repo=PhiCookBook&bg_color=ffffff&title_color=0078D4&text_color=333333&border_color=c0d8f0&border_radius=10)](https://github.com/microsoft/PhiCookBook)

## 주요 기능

- **자동 번역**: 여러 언어로 텍스트를 손쉽게 번역합니다.
- **GitHub Actions 통합**: CI/CD 파이프라인의 일부로 번역을 자동화합니다.
- **Markdown 유지**: 번역 과정에서 올바른 Markdown 구문을 유지합니다.
- **이미지 텍스트 번역**: 이미지 내 텍스트를 추출하고 번역합니다.
- **최신 LLM 기술**: 최첨단 언어 모델을 활용해 고품질 번역을 제공합니다.
- **쉬운 통합**: 기존 프로젝트 환경에 원활하게 통합됩니다.
- **로컬라이제이션 간소화**: 국제 시장을 위한 프로젝트 현지화 과정을 단순화합니다.

## 작동 방식

![Architecture](../../imgs/architecture_241019.png)

Co-op Translator는 프로젝트 폴더 내 Markdown 파일과 이미지를 다음과 같이 처리합니다:

1. **텍스트 추출**: Markdown 파일에서 텍스트를 추출하고, 구성된 경우(예: Azure Computer Vision 사용 시) 이미지 내 텍스트도 추출합니다.
1. **AI 번역**: 추출된 텍스트를 설정된 LLM(Azure OpenAI, OpenAI 등)으로 보내 번역합니다.
1. **결과 저장**: 번역된 Markdown 파일과 이미지(번역된 텍스트 포함)를 언어별 폴더에 저장하며 원본 형식을 유지합니다.

## 시작하기

> [!NOTE]
> 이 튜토리얼은 Azure 리소스에 초점을 맞추고 있지만, [지원되는 모델 및 서비스](../..) 목록에 있는 어떤 언어 모델도 사용할 수 있습니다.

CLI로 빠르게 시작하거나 GitHub Actions를 통해 완전 자동화를 설정할 수 있습니다.

### 초기 설정

- [Azure AI 설정](./getting_started/set-up-azure-ai.md)

### 빠른 시작: 명령줄

명령줄을 이용한 빠른 시작 방법:

1. 패키지 설치:
    ```bash
    pip install co-op-translator
    ```
2. 자격 증명 구성:
  - `.env` file in your project's root directory.
  - Copy the contents from the [.env.template](../../.env.template) file into your new `.env` file.
  - Fill in the required API keys and endpoint information in your `.env` file.
3. Run Translation:
  - Navigate to your project's root directory in your terminal.
  - Execute the translate command, specifying target languages with the `-l` 플래그 생성:
    ```bash
    translate -l "ko ja fr"
    ```
    *(저장소 내 `"ko ja fr"` with your desired space-separated language codes)*

### Detailed Usage Guides

Choose the approach that best fits your workflow:

#### 1. Using the Command Line (CLI)

- Best for: One-time translations, manual control, or integration into custom scripts.
- Requires: Local installation of Python and the `co-op-translator` package.
- Guide: [Command Line Guide](./getting_started/command-line-guide/command-line-guide.md)

#### 2. Using GitHub Actions (Automation)

- Best for: Automatically translating content whenever changes are pushed to your repository. Keeps translations consistently up-to-date.
- Requires: Setting up a workflow file (`.github/workflows`) 교체 필요. 로컬 설치 불필요.
- 가이드:
  - [GitHub Actions 가이드 (공개 저장소 및 표준 시크릿)](./getting_started/github-actions-guide/github-actions-guide-public.md) - 대부분의 공개 또는 개인 저장소에서 표준 저장소 시크릿을 사용하는 경우.
  - [GitHub Actions 가이드 (Microsoft 조직 저장소 및 조직 단위 설정)](./getting_started/github-actions-guide/github-actions-guide-org.md) - Microsoft GitHub 조직 내에서 작업하거나 조직 단위 시크릿 및 러너를 사용해야 할 때.

### 문제 해결 및 팁

- [문제 해결 가이드](./getting_started/troubleshooting.md)

### 추가 자료

- [명령어 참조](./getting_started/command-reference.md): 모든 명령과 옵션에 대한 자세한 안내.
- [다국어 지원 설정](./getting_started/multi-language-support.md): README에 번역본 링크 표 추가 방법.
- [지원 언어](./getting_started/supported-languages.md): 지원 언어 목록 및 신규 언어 추가 방법.
- [Markdown 전용 모드](./getting_started/markdown-only-mode.md): 이미지 번역 없이 텍스트만 번역하는 방법.

## 동영상 발표

Co-op Translator에 대해 더 알아보세요 _(아래 이미지를 클릭하면 YouTube에서 시청할 수 있습니다.)_:

- **Open at Microsoft**: Co-op Translator 사용법을 간단히 소개하는 18분 분량의 영상.

  [![Open at Microsoft](../../imgs/open-ms-thumbnail.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

- **Microsoft Reactor**: Co-op Translator의 개념 이해부터 도구 설정, 효과적인 사용법, 라이브 데모까지 1시간 동안 자세히 설명하는 단계별 가이드.

  [![Microsoft Reactor](../../imgs/reactor-thumbnail.jpg)](https://www.youtube.com/watch?v=boTtKVPBLAc)

## 후원 및 글로벌 학습 지원

교육 콘텐츠가 전 세계에 공유되는 방식을 혁신하는 데 함께하세요! [Co-op Translator](https://github.com/azure/co-op-translator)에 GitHub 스타를 눌러주시면, 학습과 기술 분야의 언어 장벽을 허무는 우리의 사명을 응원하는 큰 힘이 됩니다. 여러분의 관심과 기여가 큰 변화를 만듭니다! 코드 기여와 기능 제안도 언제나 환영합니다.

## 기여하기

이 프로젝트는 기여와 제안을 환영합니다. Azure Co-op Translator에 기여하고 싶으신가요? [CONTRIBUTING.md](./CONTRIBUTING.md)에서 기여 가이드를 확인하세요.

## 기여자

[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## 행동 강령

이 프로젝트는 [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/)를 채택하고 있습니다.
자세한 내용은 [행동 강령 FAQ](https://opensource.microsoft.com/codeofconduct/faq/)를 참조하거나
추가 질문 및 의견은 [opencode@microsoft.com](mailto:opencode@microsoft.com)으로 문의해 주세요.

## 책임 있는 AI

Microsoft는 고객이 AI 제품을 책임감 있게 사용할 수 있도록 지원하며, 투명성 노트와 영향 평가 같은 도구를 통해 학습 내용을 공유하고 신뢰 기반의 파트너십을 구축하는 데 전념하고 있습니다. 이러한 자료들은 [https://aka.ms/RAI](https://aka.ms/RAI)에서 확인할 수 있습니다.
Microsoft의 책임 있는 AI 접근법은 공정성, 신뢰성 및 안전성, 개인정보 보호 및 보안, 포용성, 투명성, 책임성을 핵심 원칙으로 삼고 있습니다.
대규모 자연어, 이미지 및 음성 모델 - 이 샘플에서 사용된 것과 같은 모델들은 잠재적으로 불공정하거나 신뢰할 수 없거나 불쾌감을 줄 수 있는 방식으로 작동하여 피해를 초래할 수 있습니다. 위험과 한계에 대해 알고 싶다면 [Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text)를 참조하세요.

이러한 위험을 완화하기 위한 권장 방법은 아키텍처에 해로운 행동을 감지하고 방지할 수 있는 안전 시스템을 포함하는 것입니다. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview)는 독립적인 보호 계층을 제공하며, 애플리케이션과 서비스에서 사용자 생성 및 AI 생성의 해로운 콘텐츠를 감지할 수 있습니다. Azure AI Content Safety에는 해로운 자료를 탐지할 수 있는 텍스트 및 이미지 API가 포함되어 있습니다. 또한 다양한 모달리티에서 해로운 콘텐츠를 감지하는 샘플 코드를 보고 탐색하며 체험할 수 있는 인터랙티브한 Content Safety Studio도 제공합니다. 다음 [빠른 시작 문서](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest)는 서비스에 요청하는 방법을 안내합니다.

또 다른 고려 사항은 전체 애플리케이션 성능입니다. 멀티모달 및 멀티모델 애플리케이션의 경우, 성능은 시스템이 사용자와 개발자가 기대하는 대로 작동하는 것을 의미하며, 여기에는 해로운 출력이 생성되지 않는 것도 포함됩니다. [생성 품질 및 위험 및 안전 지표](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in)를 사용하여 전체 애플리케이션의 성능을 평가하는 것이 중요합니다.

[Prompt flow SDK](https://microsoft.github.io/promptflow/index.html)를 사용하면 개발 환경에서 AI 애플리케이션을 평가할 수 있습니다. 테스트 데이터셋이나 목표를 기준으로, 생성 AI 애플리케이션의 생성 결과를 내장 평가자나 원하는 맞춤 평가자를 통해 정량적으로 측정할 수 있습니다. 시스템 평가를 위해 prompt flow sdk를 시작하려면 [빠른 시작 가이드](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk)를 따라 하세요. 평가 실행 후에는 [Azure AI Studio에서 결과를 시각화](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results)할 수 있습니다.

## 상표

이 프로젝트에는 프로젝트, 제품 또는 서비스의 상표나 로고가 포함될 수 있습니다. Microsoft 상표나 로고의 승인된 사용은 [Microsoft의 상표 및 브랜드 가이드라인](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general)을 준수해야 합니다. 이 프로젝트의 수정된 버전에서 Microsoft 상표나 로고를 사용하는 경우 혼동을 일으키거나 Microsoft의 후원을 암시해서는 안 됩니다. 제3자 상표나 로고 사용은 해당 제3자의 정책을 따라야 합니다.

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 노력하고 있으나, 자동 번역에는 오류나 부정확성이 포함될 수 있음을 유의해 주시기 바랍니다. 원문 문서가 권위 있는 출처로 간주되어야 합니다. 중요한 정보의 경우 전문적인 인간 번역을 권장합니다. 본 번역의 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.