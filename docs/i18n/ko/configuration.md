# 설정

Co-op Translator는 텍스트 번역에 언어 모델 제공자 하나를 사용합니다. 이미지 안의 텍스트를 번역하려면 Azure AI Vision이 추가로 필요합니다.

설정은 환경 변수에서 읽습니다. 로컬에서는 프로젝트 루트의 `.env` 파일에 저장하고, `.gitignore`에 `.env`를 추가하세요. Azure 리소스 생성 방법은 [Azure AI 설정](azure-ai-setup.md)을 참고하세요.

<a id="local-runtime-setup"></a>

## 로컬 실행 환경

Python 3.11–3.14를 사용하세요. 가상 환경을 만든 뒤 배포된 패키지를 설치합니다.

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

### 저장소 개발

개발 환경은 프로젝트 루트에서 설치하세요.

```bash
poetry install
poetry run translate --help
```

## 제공자 선택

제공자를 자동으로 감지하는 순서는 다음과 같습니다.

1. Azure OpenAI
2. OpenAI
3. Anthropic

텍스트 번역에는 이 중 하나만 설정하면 됩니다. OpenAI나 Anthropic을 사용한다면 Azure 계정이 필요하지 않습니다.

`translate -l "ko" -md --dry-run`은 자격 증명 없이 작업량을 미리 확인합니다. `migrate-links`, `co-op-review`, `run_review`도 제공자 호출 없이 실행됩니다. 실제 번역에는 제공자 자격 증명이 필요합니다.

## 모델 클라이언트 백엔드

0.22.0부터 Azure OpenAI, OpenAI, Anthropic은 Microsoft Agent Framework를 기본으로 사용합니다. 일반적인 사용에는 별도 백엔드 설정이 필요하지 않습니다.

기존 통합과의 호환성을 위해 Semantic Kernel을 선택할 수 있습니다.

```bash
CO_OP_TRANSLATOR_MODEL_CLIENT="semantic-kernel"
```

Semantic Kernel을 사용하면 지원 중단 예고 경고가 표시됩니다. 호환성 검증과 피드백에 따라 0.23.0에서 선택적 의존성으로 전환하고 0.24.0에서 통합을 제거할 계획입니다. Anthropic은 `agent-framework`가 필요하며 `semantic-kernel`과 함께 설정하면 오류가 발생합니다. 잘못된 백엔드 값도 번역기 초기화 중 오류로 처리됩니다. 진행 상황은 [이슈 #543](https://github.com/Azure/co-op-translator/issues/543)을 참고하세요.

## Azure OpenAI

Azure AI Foundry 또는 Azure OpenAI Service에 배포한 모델을 사용할 때 설정합니다.

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

번역 전에 엔드포인트, API 키, API 버전, 배포 이름으로 연결을 확인합니다.

## OpenAI

OpenAI API를 직접 사용할 때 설정합니다.

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

`OPENAI_CHAT_MODEL_ID`는 필수입니다. 기본 설정에서는 `OPENAI_ORG_ID`와 `OPENAI_BASE_URL`을 입력하지 마세요. 계정에 조직 ID가 필요하거나 별도의 엔드포인트를 사용할 때만 추가합니다. 선택 항목에 `"..."` 같은 자리표시자를 넣지 마세요.

## Anthropic Claude

Claude API를 직접 사용할 때 [API 키](https://platform.claude.com/docs/en/get-started)를 만들고 지원되는 [모델 ID](https://platform.claude.com/docs/en/about-claude/models/model-ids-and-versions)를 선택하세요.

```bash
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

두 항목 모두 필수입니다. 기본 백엔드가 Agent Framework이므로 `CO_OP_TRANSLATOR_MODEL_CLIENT`를 추가로 설정할 필요는 없습니다.

Anthropic API를 사용할 때는 `ANTHROPIC_BASE_URL`을 입력하지 마세요. 별도의 엔드포인트에 연결할 때만 설정합니다.

요청당 출력 토큰 한도인 `ANTHROPIC_MAX_TOKENS`의 기본값은 `8192`입니다. 사용하는 모델이나 엔드포인트의 출력 한도가 더 낮으면 값을 줄이세요.

## Azure AI Vision

이미지 번역은 Azure AI Vision으로 텍스트를 추출한 다음 선택한 언어 모델로 번역합니다. Anthropic도 추출된 텍스트를 번역할 수 있습니다.

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

`-img`, `images=True` 또는 콘텐츠 유형을 지정하지 않은 기본 모드는 Vision 설정을 검사합니다. Markdown만 번역하려면 `-md`를 지정하세요.

## 여러 자격 증명 세트

변수 이름 뒤에 같은 번호를 붙여 여러 세트를 구성할 수 있습니다.

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

각 세트의 필수 항목을 모두 입력하세요. 연결 검사에서 사용할 수 있는 세트를 선택합니다. OpenAI와 Anthropic도 같은 접미사 규칙을 지원합니다. `OPENAI_BASE_URL_1`, `ANTHROPIC_BASE_URL_1` 같은 선택 항목도 같은 번호를 사용해야 합니다.

## 명령별 요구 사항

| 명령 또는 API | LLM 필요 | Vision 필요 | 설명 |
| --- | --- | --- | --- |
| `translate -md` | 예 | 아니요 | Markdown만 번역합니다. |
| `translate -nb` | 예 | 아니요 | 노트북만 번역합니다. |
| `translate -img` | 예 | 예 | 이미지만 번역합니다. |
| 유형 플래그 없는 `translate` | 예 | 예 | Markdown, 노트북, 이미지를 모두 포함합니다. |
| `translate -l "ko" -md --dry-run` | 아니요 | 아니요 | 번역 호출이나 파일 쓰기 없이 작업량을 확인합니다. |
| `evaluate` | 예 | 아니요 | `--fast`를 제외하면 LLM 평가를 사용합니다. |
| `migrate-links` | 아니요 | 아니요 | 제공자 호출 없이 로컬 링크를 마이그레이션합니다. |
| `co-op-review` | 아니요 | 아니요 | 구조, 원문 변경 여부, Markdown, 노트북, 로컬 링크를 검사합니다. |
| `run_translation(markdown=True)` | 예 | 아니요 | Python에서 Markdown을 번역합니다. |
| `run_translation(images=True)` | 예 | 예 | Python에서 이미지를 번역합니다. |
| `run_review(...)` | 아니요 | 아니요 | Python에서 결정적 검사를 실행합니다. |

## 출력 디렉터리

텍스트 번역의 기본 경로:

```text
translations/<language-code>/<source-relative-path>
```

이미지 번역의 기본 경로:

```text
translated_images/<language-code>/<source-relative-path>
```

Python API의 `translations_dir`, `image_dir`로 경로를 바꿀 수 있습니다.
