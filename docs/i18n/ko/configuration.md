# 구성

Co-op Translator는 하나의 언어 모델 제공자를 필요로 합니다. 이미지 번역은 추가로 Azure AI Vision이 필요합니다.

구성은 환경 변수에서 읽어옵니다. 로컬 프로젝트의 경우 프로젝트 루트에 `.env` 파일에 배치하세요.

Azure 리소스 설정은 [Azure AI 설정](azure-ai-setup.md)을 참조하세요.

## 로컬 런타임 설정

로컬에서 CLI를 실행하기 전에 가상 환경을 사용하세요. Co-op Translator는 Python 3.11부터 3.14까지를 지원합니다.

일반적인 CLI 사용의 경우 가상 환경 안에 게시된 패키지를 설치하세요:

### Windows (PowerShell)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install co-op-translator
translate --help
```

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install co-op-translator
translate --help
```

### 리포지토리 개발

리포지토리 개발의 경우 대신 프로젝트 루트에서 의존성을 설치하세요:

```bash
poetry install
poetry run translate --help
```

CLI를 사용할 수 있게 된 후 `.env`에서 하나의 언어 모델 제공자를 구성하세요.

## 제공자 선택

도구는 다음 순서로 제공자를 자동으로 감지합니다:

1. Azure OpenAI
2. OpenAI
3. Anthropic

번역에는 제공자 자격 증명이 필요합니다. 단, `translate -l "ko" -md --dry-run`와 같은 미리보기는 예외입니다. `migrate-links`, `co-op-review`, 및 `run_review`는 결정론적 유지보수 작업으로 제공자 자격 증명이 필요하지 않습니다.

## 모델 클라이언트 백엔드

Co-op Translator 0.22.0부터 Azure OpenAI, OpenAI 및 Anthropic은 기본적으로 Microsoft Agent Framework를 사용합니다. 일반 사용에는 백엔드 설정이 필요하지 않습니다.

호환성을 위해 Semantic Kernel은 일시적으로 계속 사용 가능합니다. 명시적으로 선택하려면 다음을 설정하세요:

```bash
CO_OP_TRANSLATOR_MODEL_CLIENT="semantic-kernel"
```

Semantic Kernel을 사용하면 사용 중단 경고가 발생합니다. 이 패키지는 호환성 결과와 사용자 피드백에 따라 0.23.0에서 Semantic Kernel을 선택적 의존성으로 이동하고 0.24.0에서 통합을 제거할 예정입니다. Anthropic은 `agent-framework`를 요구합니다; Anthropic과 함께 `semantic-kernel`을 명시적으로 선택하면 구성 오류가 발생합니다. 잘못된 값은 조용히 대체되는 대신 제공자 기반 번역기 초기화 중에 실패합니다. 롤아웃 진행 상황을 팔로우하고 차단 이슈를 [GitHub 이슈 #543](https://github.com/Azure/co-op-translator/issues/543)에 보고하세요.

## Azure OpenAI

모델이 Azure AI Foundry 또는 Azure OpenAI Service에 배포된 경우 Azure OpenAI를 사용하세요.

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

연결성 검사는 번역이 시작되기 전에 엔드포인트, API 키, API 버전 및 배포 이름을 사용합니다.

## OpenAI

OpenAI API를 직접 호출할 때 OpenAI를 사용하세요.

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

`OPENAI_CHAT_MODEL_ID`는 번역기가 API 호출을 위해 명시적인 챗 모델이 필요하므로 필수입니다.

기본 설정의 경우 `OPENAI_ORG_ID`와 `OPENAI_BASE_URL`을 설정하지 않은 상태로 두세요. 조직 ID는 계정에서 필요할 때만 추가하고, base URL은 커스텀 엔드포인트를 사용할 때만 추가하세요. 선택적 설정에 대해 자리표시자 값을 복사하지 마세요.

## Anthropic Claude

Claude API를 직접 호출할 때 Anthropic을 사용하세요. [Anthropic API 키](https://platform.claude.com/docs/en/get-started)를 생성하고 지원되는 [Claude 모델 ID](https://platform.claude.com/docs/en/about-claude/models/model-ids-and-versions)를 선택하세요.

```bash
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

`ANTHROPIC_API_KEY`와 `ANTHROPIC_MODEL`은 필수입니다. `CO_OP_TRANSLATOR_MODEL_CLIENT`를 설정할 필요는 없습니다; 기본 백엔드는 Agent Framework입니다.

Anthropic API의 경우 `ANTHROPIC_BASE_URL`을 설정하지 않은 상태로 두세요. 커스텀 엔드포인트를 사용할 때만 설정하세요.

`ANTHROPIC_MAX_TOKENS`의 기본값은 `8192`로, Meitei Mayek와 같이 토큰이 많은 스크립트에 여유를 둡니다. 모델이나 Anthropic 호환 엔드포인트가 그보다 낮게 출력을 제한하면 값을 줄이세요.

## Azure AI Vision

이미지 번역은 도구가 구성된 언어 모델이 번역하기 전에 이미지에서 텍스트를 추출할 수 있도록 Azure AI Vision을 요구합니다. Anthropic은 Azure OpenAI나 OpenAI와 마찬가지로 추출된 텍스트를 번역할 수 있습니다.

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

`-img`, `images=True`를 선택하거나 콘텐츠 유형 필터가 없을 경우, 도구는 번역 시작 전에 Vision 구성을 검증합니다.

## 다중 자격 증명 세트

구성 계층은 변수에 같은 인덱스를 접미사로 붙여 다중 자격 증명 세트를 지원합니다:

```bash
AZURE_OPENAI_API_KEY_1="..."
AZURE_OPENAI_ENDPOINT_1="https://<resource-1>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME_1="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME_1="<deployment-1>"
AZURE_OPENAI_API_VERSION_1="2024-12-01-preview"

AZURE_OPENAI_API_KEY_2="..."
AZURE_OPENAI_ENDPOINT_2="https://<resource-2>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME_2="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME_2="<deployment-2>"
AZURE_OPENAI_API_VERSION_2="2024-12-01-preview"
```

각 세트는 완전해야 합니다. 상태 검사(health check)가 번역이 진행되기 전에 작동 가능한 세트를 선택합니다.

OpenAI와 Anthropic은 동일한 접미사 규칙을 지원합니다. `OPENAI_BASE_URL_1` 또는 `ANTHROPIC_BASE_URL_1`과 같은 선택적 값을 포함하여 자격 증명 세트의 모든 변수를 동일한 접미사에 두세요.

## 명령 요구사항

| 명령 또는 API | LLM 필요 | Vision 필요 | 비고 |
| --- | --- | --- | --- |
| `translate -md` | 예 | 아니오 | Markdown만 번역합니다. |
| `translate -nb` | 예 | 아니오 | 노트북만 번역합니다. |
| `translate -img` | 예 | 예 | 이미지만 번역합니다. |
| `translate` 타입 플래그 없이 | 예 | 예 | 기본 모드는 Markdown, 노트북 및 이미지를 포함합니다. |
| `evaluate` | 예 | 아니오 | `--fast`가 선택되지 않으면 LLM 평가를 사용합니다. |
| `migrate-links` | 아니오 | 아니오 | 제공자 호출 없이 로컬 링크 마이그레이션을 수행합니다. |
| `co-op-review` | 아니오 | 아니오 | 결정론적 번역 구조, 최신성, Markdown, 노트북, 및 로컬 링크 검사를 실행합니다. |
| `run_translation(markdown=True)` | 예 | 아니오 | 프로그래밍 방식의 Markdown 번역. |
| `run_translation(images=True)` | 예 | 예 | 프로그래밍 방식의 이미지 번역. |
| `run_review(...)` | 아니오 | 아니오 | 프로그래밍 방식의 결정론적 검토. |

## 출력 디렉토리

기본 텍스트 번역 출력:

```text
translations/<language-code>/<source-relative-path>
```

기본 번역된 이미지 출력:

```text
translated_images/<language-code>/<source-relative-path>
```

Python API는 `translations_dir` 및 `image_dir`로 이러한 디렉토리를 재정의할 수 있습니다.