# Co-op Translator

_프로젝트가 발전함에 따라 교육용 GitHub 콘텐츠의 번역을 여러 언어로 손쉽게 자동화하고 유지하세요._

![Python 3.10–3.12](https://img.shields.io/badge/python-3.10--3.12-blue)
[![Python 패키지](https://img.shields.io/pypi/v/co-op-translator?color=4BA3FF)](https://pypi.org/project/co-op-translator/)
[![라이선스: MIT](https://img.shields.io/github/license/azure/co-op-translator?color=4BA3FF)](https://github.com/azure/co-op-translator/blob/main/LICENSE)
[![다운로드](https://static.pepy.tech/badge/co-op-translator)](https://pepy.tech/project/co-op-translator)
[![다운로드](https://static.pepy.tech/badge/co-op-translator/month)](https://pepy.tech/project/co-op-translator)
[![컨테이너: GHCR](https://img.shields.io/badge/Container-GHCR-2496ED?logo=docker&logoColor=fff)](https://github.com/azure/co-op-translator/pkgs/container/co-op-translator)
[![코드 스타일: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[![GitHub 기여자](https://img.shields.io/github/contributors/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/graphs/contributors/)
[![GitHub 이슈](https://img.shields.io/github/issues/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/issues/)
[![GitHub 풀 리퀘스트](https://img.shields.io/github/issues-pr/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/pulls/)
[![PR 환영](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

**시작하기:** [워크플로 선택](https://azure.github.io/co-op-translator/workflows/) | [구성](https://azure.github.io/co-op-translator/configuration/) | [CLI](https://azure.github.io/co-op-translator/cli/) | [Python API](https://azure.github.io/co-op-translator/api/) | [MCP 서버](https://azure.github.io/co-op-translator/mcp/)

### 🌐 다국어 지원

#### 지원: [Co-op Translator](https://github.com/Azure/co-op-translator)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[아랍어](../ar/README.md) | [벵골어](../bn/README.md) | [불가리아어](../bg/README.md) | [버마어 (미얀마)](../my/README.md) | [중국어 (간체)](../zh-CN/README.md) | [중국어 (번체, 홍콩)](../zh-HK/README.md) | [중국어 (번체, 마카오)](../zh-MO/README.md) | [중국어 (번체, 대만)](../zh-TW/README.md) | [크로아티아어](../hr/README.md) | [체코어](../cs/README.md) | [덴마크어](../da/README.md) | [네덜란드어](../nl/README.md) | [에스토니아어](../et/README.md) | [핀란드어](../fi/README.md) | [프랑스어](../fr/README.md) | [독일어](../de/README.md) | [그리스어](../el/README.md) | [히브리어](../he/README.md) | [힌디어](../hi/README.md) | [헝가리어](../hu/README.md) | [인도네시아어](../id/README.md) | [이탈리아어](../it/README.md) | [일본어](../ja/README.md) | [칸나다어](../kn/README.md) | [크메르어](../km/README.md) | [한국어](./README.md) | [리투아니아어](../lt/README.md) | [말레이어](../ms/README.md) | [말라얄람어](../ml/README.md) | [마라티어](../mr/README.md) | [네팔어](../ne/README.md) | [나이지리아 피진어](../pcm/README.md) | [노르웨이어](../no/README.md) | [페르시아어 (파르시)](../fa/README.md) | [폴란드어](../pl/README.md) | [포르투갈어 (브라질)](../pt-BR/README.md) | [포르투갈어 (포르투갈)](../pt-PT/README.md) | [펀자브어 (구르무키)](../pa/README.md) | [루마니아어](../ro/README.md) | [러시아어](../ru/README.md) | [세르비아어 (키릴)](../sr/README.md) | [슬로바키아어](../sk/README.md) | [슬로베니아어](../sl/README.md) | [스페인어](../es/README.md) | [스와힐리어](../sw/README.md) | [스웨덴어](../sv/README.md) | [타갈로그어 (필리핀)](../tl/README.md) | [타밀어](../ta/README.md) | [텔루구어](../te/README.md) | [태국어](../th/README.md) | [터키어](../tr/README.md) | [우크라이나어](../uk/README.md) | [우르두어](../ur/README.md) | [베트남어](../vi/README.md)

> **로컬로 복제하시겠습니까?**
>
> 이 저장소에는 50개 이상의 언어 번역이 포함되어 있어 다운로드 크기가 크게 증가합니다. 번역 없이 복제하려면 sparse checkout을 사용하세요:
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
> 이 방법을 사용하면 과정 완료에 필요한 모든 것을 훨씬 빠른 다운로드로 얻을 수 있습니다.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![GitHub Codespaces에서 열기](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## 개요

<strong>Co-op Translator</strong>는 교육용 GitHub 콘텐츠를 여러 언어로 손쉽게 현지화하도록 도와줍니다.
Markdown 파일, 이미지 또는 노트북을 업데이트하면 번역도 자동으로 동기화되어 전 세계 학습자에게 콘텐츠의 정확성과 최신성이 유지됩니다.

CLI에서 저장소 번역을 실행하거나 자동화를 위해 Python API를 사용하거나 에이전트 및 편집자 워크플로를 위해 MCP 서버를 통해 사용할 수 있습니다.

번역된 콘텐츠가 구성되는 예:

![예시](../../imgs/translation-ex.png)

## Co-op Translator를 사용하는 이유

하나의 파일을 번역하는 것은 쉽습니다. 전체 문서 저장소를
번역하고, 링크를 맞추고, 최신 상태로 유지하는 것이 더 어렵습니다.

| 문제 | Co-op Translator의 도움 |
| --- | --- |
| 긴 문서는 하나의 프롬프트로 처리할 수 없음 | 큰 Markdown 파일은 청크로 분할되므로 긴 README가 하나의 취약한 모델 응답에 의존하지 않습니다. 청크가 실패하면 Co-op Translator는 실패한 부분만 재시도하고 재청크할 수 있습니다. |
| 불완전한 번역을 현재 상태로 표시해서는 안 됨 | 잘린 번역이 최신으로 봉인되어서는 안 됩니다. Co-op Translator는 저장하기 전에 번역 무결성을 검사하고 구조적으로 불완전한 기존 번역을 감지할 수 있습니다. |
| 링크는 번역된 저장소 구조와 일치해야 함 | 수동 번역은 종종 상대 링크가 원본 트리를 가리키도록 남깁니다. Co-op Translator는 Markdown, 노트북, 이미지 및 README 링크를 `translations/<lang>/...` 구조에 맞게 재작성합니다. |
| 전체 저장소에 대한 번역이 작동해야 함 | Co-op Translator는 파일을 하나씩 번역하는 대신 README 파일, 문서, 노트북 및 이미지 텍스트를 하나의 저장소 워크플로의 일부로 처리합니다. |
| 번역을 단 한번 생성하는 것보다 유지하는 것이 더 중요함 | 소스 해시와 번역 메타데이터를 통해 Co-op Translator는 오래된 파일을 찾고, 변경되지 않은 파일을 건너뛰며, 원본 저장소가 진화함에 따라 번역된 콘텐츠를 동기화 상태로 유지할 수 있습니다. |

## 번역 상태 관리 방법

Co-op Translator는 번역된 콘텐츠를 <strong>버전 관리되는 소프트웨어 아티팩트</strong>로 관리합니다.  
정적 파일로 취급하지 않습니다.

이 도구는 <strong>언어 범위 메타데이터</strong>를 사용하여 번역된 Markdown, 이미지 및 노트북의 상태를 추적합니다.

이 설계는 Co-op Translator가 다음을 가능하게 합니다:

- 오래된 번역을 신뢰성 있게 감지
- Markdown, 이미지 및 노트북을 일관되게 처리
- 크고 빠르게 변화하는 다국어 저장소 전반에서 안전하게 확장

번역을 관리형 아티팩트로 모델링함으로써,
번역 워크플로는 최신 소프트웨어 종속성 및 아티팩트 관리 관행과 자연스럽게 정렬됩니다.

→ [번역 상태 관리 방법](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/rethinking-documentation-translation-treating-translations-as-versioned-software/4491755)

### 관련 심층 글

- [AI 번역에서 깨진 Markdown 수정: 프로덕션 파이프라인 강건화](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/fixing-broken-markdown-in-ai-translation-hardening-a-production-pipeline/4511378)

## 시작하기

Co-op Translator는 CLI, Python API 또는 MCP 서버에서 사용할 수 있습니다. 로컬 번역, 자동화, CI 및 에이전트/편집기 통합 중에서 선택할 때 워크플로 가이드부터 시작하세요.

- [워크플로 선택](../../docs/workflows.md)
- [자격 증명 구성](../../docs/configuration.md)
- [CLI로 번역하기](../../docs/cli.md)
- [Python API로 자동화하기](../../docs/api.md)
- [MCP 서버와 연결하기](../../docs/mcp.md)
- [GitHub Actions에서 실행하기](../../docs/github-actions.md)

구성 후 최소 CLI 예시:

```bash
python -m venv .venv
# 윈도우
.venv\Scripts\activate
# macOS/리눅스
source .venv/bin/activate

pip install co-op-translator
translate -l "ko" -md
co-op-review -l "ko"
```

대규모 저장소에서 처음 실행할 때는 번역된 파일을 쓰기 전에 `--dry-run`을 사용하세요. 콘텐츠 유형 플래그, 로그, 검토 및 링크 마이그레이션은 [CLI 참조](../../docs/cli.md)를 참조하세요.

Bash/Zsh에서 컨테이너 빠른 실행:

```bash
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko" -md
```

PowerShell에서 컨테이너 빠른 실행:

```powershell
docker run --rm -it --env-file .env -v ${PWD}:/work ghcr.io/azure/co-op-translator:latest -l "ko" -md
```

## 기능

- Markdown, 노트북 및 이미지에 대한 자동 번역
- 소스 변경과 번역을 동기 상태로 유지
- 로컬(CLI) 또는 CI(GitHub Actions)에서 작동
- MCP를 통해 Markdown, 노트북, 이미지, 검토 및 프로젝트 번역 도구 노출
- 제공자 기반 번역을 위해 Azure OpenAI 또는 OpenAI 사용
- MCP가 에이전트를 호스팅하여 Co-op Translator LLM 자격 증명 없이 Markdown 및 노트북 청크를 번역하도록 허용
- 이미지 텍스트 추출 및 번역을 위해 Azure AI Vision 사용
- 결정론적 검사를 통해 번역 구조와 최신성 검토
- Markdown 서식과 구조 보존

## 문서

- [문서 사이트](https://azure.github.io/co-op-translator/)
- [워크플로 선택](../../docs/workflows.md)
- [구성](../../docs/configuration.md)
- [Azure AI 설정](../../docs/azure-ai-setup.md)
- [CLI 참조](../../docs/cli.md)
- [Python API](../../docs/api.md)
- [MCP 서버](../../docs/mcp.md)
- [GitHub Actions](../../docs/github-actions.md)
- [README 언어 템플릿](../../docs/readme-languages-template.md)
- [지원되는 언어](../../docs/supported-languages.md)
- [기여하기](../../CONTRIBUTING.md)
- [문제 해결](../../docs/troubleshooting.md)

### Microsoft 전용 가이드
> [!NOTE]
> Microsoft “For Beginners” 저장소의 유지 관리자를 위한 안내입니다.

- [“other courses” 목록 업데이트 (Microsoft For Beginners 저장소 전용)](../../docs/microsoft-beginners.md)

## 저희를 지원하고 전 세계 학습을 촉진하세요

교육용 콘텐츠가 전 세계에 공유되는 방식을 혁신하는 여정에 함께하세요! [Co-op Translator](https://github.com/azure/co-op-translator)에 GitHub에서 ⭐를 눌러 주시고 학습과 기술에서 언어 장벽을 허무는 우리의 미션을 지원해주세요. 여러분의 관심과 기여는 큰 영향을 줍니다! 코드 기여와 기능 제안은 언제나 환영합니다.

### 사용자의 언어로 Microsoft 교육 자료 탐색
- [LangChain4j-for-Beginners](https://github.com/microsoft/LangChain4j-for-Beginners)
- [AZD for Beginners](https://github.com/microsoft/AZD-for-beginners)
- [Edge AI for Beginners](https://github.com/microsoft/edgeai-for-beginners)
- [Model Context Protocol (MCP) For Beginners](https://github.com/microsoft/mcp-for-beginners)
- [AI Agents for Beginners](https://github.com/microsoft/ai-agents-for-beginners)
- [Generative AI for Beginners using .NET](https://github.com/microsoft/Generative-AI-for-beginners-dotnet)
- [Generative AI for Beginners](https://github.com/microsoft/generative-ai-for-beginners)
- [Generative AI for Beginners using Java](https://github.com/microsoft/generative-ai-for-beginners-java)
- [ML for Beginners](https://aka.ms/ml-beginners)
- [Data Science for Beginners](https://aka.ms/datascience-beginners)
- [AI for Beginners](https://aka.ms/ai-beginners)
- [Cybersecurity for Beginners](https://github.com/microsoft/Security-101)
- [Web Dev for Beginners](https://aka.ms/webdev-beginners)
- [IoT for Beginners](https://aka.ms/iot-beginners)
- [PhiCookBook](https://github.com/microsoft/PhiCookBook)

## 비디오 발표

👉 아래 이미지를 클릭하면 YouTube에서 시청할 수 있습니다.

- **Microsoft에서 공개**: Co-op Translator 사용 방법에 대한 간단한 18분 소개 및 빠른 안내.

  [![Microsoft에서 공개](../../imgs/open-ms-thumbnail.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## 기여

이 프로젝트는 기여와 제안을 환영합니다. Azure Co-op Translator에 기여하는 데 관심이 있으신가요? Co-op Translator를 보다 접근 가능하게 만드는 데 도움이 될 수 있는 지침은 [CONTRIBUTING.md](../../CONTRIBUTING.md) 를 참조하세요.

## 기여자

[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## 행동 강령

이 프로젝트는 [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/) 를 채택했습니다.
자세한 내용은 [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) 를 참조하거나 추가 질문이나 의견이 있으면 [opencode@microsoft.com](mailto:opencode@microsoft.com) 으로 문의하세요.

## 책임 있는 AI

Microsoft는 고객이 당사의 AI 제품을 책임감 있게 사용할 수 있도록 지원하고, 학습 내용을 공유하며, Transparency Notes 및 Impact Assessments 같은 도구를 통해 신뢰 기반의 파트너십을 구축하는 데 전념하고 있습니다. 이러한 리소스의 많은 부분은 [https://aka.ms/RAI](https://aka.ms/RAI) 에서 확인할 수 있습니다.
Microsoft의 책임 있는 AI 접근 방식은 공정성, 신뢰성과 안전성, 개인 정보 보호 및 보안, 포용성, 투명성 및 책임성이라는 AI 원칙에 기반합니다.

이 샘플에서 사용된 것과 같은 대규모 자연어, 이미지 및 음성 모델은 잠재적으로 불공정하거나 신뢰할 수 없거나 공격적인 방식으로 동작하여 피해를 초래할 수 있습니다. 위험과 한계에 대해 알기 위해 [Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) 를 참조하세요.

이러한 위험을 완화하기 위한 권장 접근 방식은 유해한 동작을 감지하고 방지할 수 있는 안전 시스템을 아키텍처에 포함시키는 것입니다. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) 는 애플리케이션과 서비스에서 유해한 사용자 생성 및 AI 생성 콘텐츠를 감지할 수 있는 독립적인 보호 계층을 제공합니다. Azure AI Content Safety는 유해한 자료를 감지할 수 있는 텍스트 및 이미지 API를 포함합니다. 또한 다양한 모달리티에 걸쳐 유해한 콘텐츠를 감지하기 위한 샘플 코드를 보고, 탐색하고, 직접 시도해볼 수 있는 대화형 Content Safety Studio도 제공합니다. 다음의 [빠른 시작 문서](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) 는 서비스에 요청을 보내는 과정을 안내합니다.

고려해야 할 또 다른 측면은 전체 애플리케이션 성능입니다. 멀티모달 및 멀티모델 애플리케이션의 경우, 성능은 시스템이 사용자와 귀하가 기대하는 대로 동작하는지(유해한 출력물을 생성하지 않는 것을 포함)를 의미합니다. 전체 애플리케이션의 성능을 평가하는 것은 [generation quality and risk and safety metrics](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in) 를 사용하여 수행하는 것이 중요합니다.

개발 환경에서 [prompt flow SDK](https://microsoft.github.io/promptflow/index.html) 를 사용하여 AI 애플리케이션을 평가할 수 있습니다. 테스트 데이터셋이나 목표를 기반으로 귀하의 생성형 AI 애플리케이션 생성물은 내장 평가기 또는 선택한 맞춤 평가기를 통해 정량적으로 측정됩니다. 시스템을 평가하기 위해 prompt flow SDK를 시작하려면 [빠른 시작 가이드](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk) 를 따라 하세요. 평가 실행을 완료하면 [Azure AI Studio에서 결과를 시각화](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results) 할 수 있습니다.

## 상표

이 프로젝트에는 프로젝트, 제품 또는 서비스의 상표 또는 로고가 포함될 수 있습니다. Microsoft 상표 또는 로고의 승인된 사용은 [Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general) 를 준수해야 합니다.
이 프로젝트의 수정된 버전에서 Microsoft 상표 또는 로고를 사용하는 경우 혼동을 초래하거나 Microsoft의 후원을 암시해서는 안 됩니다.
타사 상표 또는 로고의 사용은 해당 타사 정책의 적용을 받습니다.

## 도움 받기

AI 앱을 빌드하는 중에 막히거나 질문이 있는 경우 다음에 참여하세요:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

제품 피드백이 있거나 빌드 중 오류가 발생한 경우 방문하세요:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)