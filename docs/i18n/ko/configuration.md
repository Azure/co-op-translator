# 설정

Co-op Translator는 하나의 언어 모델 제공자를 필요로 합니다. 이미지 번역은 추가로 Azure AI Vision을 필요로 합니다.

구성은 환경 변수에서 읽습니다. 로컬 프로젝트의 경우 프로젝트 루트에 `.env` 파일로 배치하세요.

Azure 리소스 설정에 대해서는 [Azure AI Setup](azure-ai-setup.md)를 참조하세요.

## 로컬 런타임 설정

로컬에서 CLI를 실행하기 전에 가상 환경을 사용하세요. Co-op Translator는 Python 3.10에서 3.12를 지원합니다.

일반적인 CLI 사용의 경우, 가상 환경 안에 게시된 패키지를 설치하세요:

=== "Windows"

    ```powershell
    python -m venv .venv
    .venv\Scripts\activate
    pip install co-op-translator
    translate --help
    ```

=== "macOS / Linux"

    ```bash
    python -m venv .venv
    source .venv/bin/activate
    pip install co-op-translator
    translate --help
    ```

레포지토리 개발의 경우, 대신 프로젝트 루트에서 의존성을 설치하세요:

```bash
poetry install
poetry run translate --help
```

CLI를 사용할 수 있게 되면, `.env`에 하나의 언어 모델 제공자를 구성하세요.

## 제공자 선택

도구는 다음 순서로 제공자를 자동 감지합니다:

1. Azure OpenAI
2. OpenAI

어떤 제공자도 구성되어 있지 않으면, `translate`, `evaluate`, `migrate-links`, 및 `run_translation`은 구성 검사 중에 실패합니다. `co-op-review`와 `run_review`는 결정적 유지보수 검사로 제공자 자격증명을 필요로 하지 않습니다.

## Azure OpenAI

모델이 Azure AI Foundry 또는 Azure OpenAI Service에 배포된 경우 Azure OpenAI를 사용하세요.

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

연결성 검사는 번역이 시작되기 전에 엔드포인트, API 키, API 버전, 배포 이름을 사용합니다.

## OpenAI

OpenAI API를 직접 호출할 때 OpenAI를 사용하세요.

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
OPENAI_ORG_ID="..."          # 선택 사항
OPENAI_BASE_URL="..."        # 선택 사항
```

`OPENAI_CHAT_MODEL_ID`는 번역기가 API 호출을 위해 명시적인 채팅 모델을 필요로 하기 때문에 필수입니다.

## Azure AI Vision

이미지 번역은 도구가 번역하기 전에 이미지에서 텍스트를 추출할 수 있도록 Azure AI Vision을 필요로 합니다.

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

이미지 번역이 `-img`, `images=True`로 선택되었거나 콘텐츠 유형 필터가 없을 경우, 도구는 번역 시작 전에 Vision 구성을 검증합니다.

## 여러 자격 증명 세트

구성 계층은 변수에 동일한 인덱스를 접미사로 추가하여 여러 자격 증명 세트를 지원합니다:

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

각 세트는 완전해야 합니다. 헬스 체크는 번역이 진행되기 전에 작동하는 세트를 선택합니다.

## 명령 요구 사항

| Command or API | LLM required | Vision required | Notes |
| --- | --- | --- | --- |
| `translate -md` | 예 | 아니요 | Markdown만 번역합니다. |
| `translate -nb` | 예 | 아니요 | 노트북만 번역합니다. |
| `translate -img` | 예 | 예 | 이미지만 번역합니다. |
| `translate` with no type flags | 예 | 예 | 기본 모드는 Markdown, 노트북 및 이미지를 포함합니다. |
| `evaluate` | 예 | 아니요 | `--fast`가 선택되지 않는 한 LLM 평가를 사용합니다. |
| `migrate-links` | 예 | 아니요 | 링크 마이그레이션을 수행하지만 여전히 공유 구성 검사를 실행합니다. |
| `co-op-review` | 아니요 | 아니요 | 결정론적 번역 구조, 최신성, Markdown, 노트북, 로컬 링크 검사를 실행합니다. |
| `run_translation(markdown=True)` | 예 | 아니요 | 프로그래밍 방식의 Markdown 번역입니다. |
| `run_translation(images=True)` | 예 | 예 | 프로그래밍 방식의 이미지 번역입니다. |
| `run_review(...)` | 아니요 | 아니요 | 프로그래밍 방식의 결정론적 리뷰입니다. |

## 출력 디렉터리

기본 텍스트 번역 출력:

```text
translations/<language-code>/<source-relative-path>
```

기본 번역된 이미지 출력:

```text
translated_images/<language-code>/<source-relative-path>
```

Python API는 `translations_dir` 및 `image_dir`로 이러한 디렉터리를 재정의할 수 있습니다.