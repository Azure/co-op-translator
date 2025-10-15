<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3fd2055f97f093b6fe102ea24df4458b",
  "translation_date": "2025-10-15T04:23:17+00:00",
  "source_file": "AGENTS.md",
  "language_code": "ko"
}
-->
## 프로젝트 개요

Co‑op Translator는 마크다운 파일, 주피터 노트북, 이미지 내 텍스트를 여러 언어로 번역하는 Python 명령줄 도구이자 GitHub Actions 워크플로우입니다. 번역 결과는 언어별 폴더에 정리되며, 원본과 동기화 상태를 유지합니다. 이 프로젝트는 Poetry로 관리되는 라이브러리 구조와 CLI 진입점을 갖추고 있습니다.

### 아키텍처 개요

- CLI 진입점(`translate`, `migrate-links`, `evaluate`)은 통합 CLI를 호출하여 번역, 링크 마이그레이션, 평가 플로우로 분기합니다.
- 설정 로더가 `.env`를 읽고 LLM 제공자(Azure OpenAI 또는 OpenAI)를 자동 감지하며, 요청 시 이미지 텍스트 추출을 위한 비전 제공자(Azure AI Service)도 감지합니다.
- 번역 코어는 마크다운과 노트북을 처리하며, `-img` 옵션 사용 시 비전 파이프라인이 이미지에서 텍스트를 추출합니다.
- 결과물은 텍스트는 `translations/<lang>/`, 이미지는 `translated_images/`에 원본 구조를 보존하며 정리됩니다.

### 주요 기술 및 프레임워크

- Python 3.10–3.12, 패키징은 Poetry 사용
- CLI: `click`
- LLM/AI SDK: Azure OpenAI, OpenAI
- 비전: Azure AI Service (Computer Vision)
- HTTP 및 데이터: `httpx`, `pydantic`
- 이미지 처리: `pillow`, `opencv-python`, `matplotlib`
- 도구: `pytest`, `black`, `ruff`

## 설치 명령어

### 사전 준비

- Python 3.10–3.12
- Azure 구독(선택, Azure AI 서비스 사용 시)
- LLM/비전 API 사용을 위한 인터넷 연결 (예: Azure OpenAI/OpenAI, Azure AI Vision)

### 옵션 A: Poetry (권장)

```bash
# From repository root
pip install poetry
poetry install

# Run any command via Poetry
poetry run translate --help
```

### 옵션 B: pip/venv

```bash
# Create & activate virtual environment
python -m venv .venv
# Windows
.venv\\Scripts\\activate
# Linux/macOS
# source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# (Optional) Editable install for local development
pip install -e .
```

## 최종 사용자 사용법

### Docker (배포 이미지)

```bash
# Pull public image from GHCR
docker pull ghcr.io/azure/co-op-translator:latest

# Run with current folder mounted and .env provided (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "fr es" -md

# PowerShell
docker run --rm -it --env-file .env -v ${PWD}:/work ghcr.io/azure/co-op-translator:latest -l "fr es" -md
```

참고:
- 기본 엔트리포인트는 `translate`입니다. 링크 마이그레이션은 `--entrypoint migrate-links`로 변경하세요.
- 익명 다운로드를 위해 GHCR 패키지 공개 설정이 필요합니다.

### CLI (pip)

```bash
pip install co-op-translator
translate -l "fr es" -md
```

### 환경 설정

저장소 루트에 `.env` 파일을 만들고, 선택한 언어 모델 및(선택) 비전 서비스의 자격 증명/엔드포인트를 입력하세요. 제공자별 설정은 `getting_started/set-up-azure-ai.md`를 참고하세요.

### 필수 환경 변수

최소 한 개의 LLM 제공자 설정이 필요합니다. 이미지 번역 시 Azure AI Service도 설정해야 합니다.

- Azure OpenAI (텍스트 번역):
  - `AZURE_OPENAI_API_KEY`
  - `AZURE_OPENAI_ENDPOINT`
  - `AZURE_OPENAI_MODEL_NAME`
  - `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME`
  - `AZURE_OPENAI_API_VERSION`

- OpenAI (텍스트 번역 대안):
  - `OPENAI_API_KEY`
  - `OPENAI_ORG_ID` (선택)
  - `OPENAI_CHAT_MODEL_ID` (OpenAI 제공자 사용 시 필수)
  - `OPENAI_BASE_URL` (선택, 기본값: `https://api.openai.com/v1`)

- 이미지 텍스트 추출용 Azure AI Service (`-img` 사용 시 필수):
  - `AZURE_AI_SERVICE_API_KEY` (권장) 또는 기존 `AZURE_SUBSCRIPTION_KEY`
  - `AZURE_AI_SERVICE_ENDPOINT`

`.env` 예시:

```bash
# Azure AI Service (for image translation)
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<your-ai-service>.cognitiveservices.azure.com/"

# Azure OpenAI (primary option)
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<your-azure-openai>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<your-deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"

# OpenAI (alternative option)
OPENAI_API_KEY="..."
OPENAI_ORG_ID="..."            # optional
OPENAI_CHAT_MODEL_ID="gpt-4o"   # required when using OpenAI
OPENAI_BASE_URL="https://api.openai.com/v1" # optional
```

참고:

- 도구가 사용 가능한 LLM 제공자를 자동 감지합니다. Azure OpenAI 또는 OpenAI 중 하나만 설정하면 됩니다.
- 이미지 번역에는 `AZURE_AI_SERVICE_API_KEY`와 `AZURE_AI_SERVICE_ENDPOINT`가 모두 필요합니다.
- 필수 변수가 누락되면 CLI에서 명확한 오류를 안내합니다.

## 개발 워크플로우

- 소스 코드는 `src/co_op_translator`에, 테스트는 `tests/`에 위치합니다.
- 주요 CLI(엔트리포인트로 설치):

```bash
# Translate content to one or more languages (space‑separated codes)
translate -l "fr es de"

# Restrict by content type
translate -l "ja" -md            # only Markdown
translate -l "ko" -nb            # only notebooks
translate -l "zh" -md -img       # Markdown + images

# Update links in previously translated notebooks/Markdown
migrate-links -l "all" -y
```

추가 사용법 문서는 `getting_started/`에서 확인하세요.

## 테스트 방법

저장소 루트에서 테스트를 실행하세요. 일부 테스트는 API 자격 증명이 필요할 수 있으니, 필요 시 해당 테스트는 건너뛰세요.

```bash
# Run full test suite
pytest

# Skip tests that require live API keys
pytest -m "not api_key_required"

# Run a subset
pytest tests/co_op_translator -k "name_substring"
```

커버리지(선택, `coverage` 필요):

```bash
coverage run -m pytest -m "not api_key_required"
coverage html  # outputs to ./htmlcov
```

## 코드 스타일 가이드

- 포매터: Black (`pyproject.toml`에 설정, 줄 길이 88)
- 린터: Ruff (`pyproject.toml`에 설정, 줄 길이 120)
- 타입 체크: mypy (설정 포함, 설치 시 활성화 가능)

명령어:

```bash
# Via Poetry
poetry run black .
poetry run ruff check .
poetry run ruff check . --fix   # safe auto‑fixes

# Or with global tools
black .
ruff check .
```

Python 소스는 `src/`, 테스트는 `tests/`에 정리하고, 패키지 네임스페이스(`co_op_translator.*`) 내에서 명시적 임포트를 권장합니다.

## 빌드 및 배포

빌드 결과물은 `dist/`에 생성됩니다.

```bash
# Build (Poetry)
poetry build

# Local install of the built wheel
pip install dist/*.whl
```

GitHub Actions를 통한 자동화 지원; 자세한 내용은 다음을 참고하세요:

- `getting_started/github-actions-guide/github-actions-guide-public.md`
- `getting_started/github-actions-guide/github-actions-guide-org.md`

### 컨테이너 이미지 (GHCR)

- 공식 이미지: `ghcr.io/azure/co-op-translator:<tag>`
- 태그: `latest`(main 기준), `vX.Y.Z`와 같은 시맨틱 태그, `sha` 태그
- 멀티 아키텍처: Buildx로 `linux/amd64, linux/arm64` 지원
- Dockerfile 패턴: 빌더에서 의존성 wheel 빌드(`build-essential`, `python3-dev` 포함), 런타임에서 로컬 wheelhouse로 설치(`pip install --no-index --find-links=/wheels`)
- 워크플로우: `.github/workflows/docker-publish.yml`에서 빌드 및 GHCR로 푸시

## 보안 고려사항

- API 키와 엔드포인트는 `.env` 또는 CI 시크릿 스토어에 보관하고, 절대 커밋하지 마세요.
- 이미지 번역 시 Azure AI Vision 키/엔드포인트가 필요하며, 그렇지 않으면 `-img` 옵션을 생략하세요.
- 대량 번역 시 제공자 쿼터/요율 제한을 반드시 확인하세요.

## Pull Request 가이드라인

### 제출 전 체크리스트

1. **변경 사항 테스트:**
   - 수정한 노트북을 모두 실행
   - 모든 셀이 오류 없이 실행되는지 확인
   - 출력이 적절한지 점검

2. **문서 업데이트:**
   - 새로운 개념 추가 시 `README.md` 갱신
   - 복잡한 코드에는 노트북에 주석 추가
   - 마크다운 셀로 목적 설명

3. **파일 변경:**
   - `.env` 파일 커밋 금지(`.env.example` 사용)
   - `venv/`, `__pycache__/` 디렉터리 커밋 금지
   - 개념 설명에 필요한 노트북 출력은 유지
   - 임시 파일 및 백업 노트북(`*-backup.ipynb`) 삭제

4. **스타일 및 포매팅:**
   - 스타일/포매팅 가이드 준수
   - `poetry run black .` 및 `poetry run ruff check .`로 스타일/포매팅 점검

5. **테스트 및 CLI 도움말 추가/갱신:**
   - 동작 변경 시 테스트 추가/수정
   - CLI 도움말도 변경 사항에 맞게 유지


### 커밋 메시지 및 병합 전략

Squash and Merge를 기본으로 사용합니다. 최종 squash 커밋 메시지는 다음 형식을 따릅니다:

```bash
<type>: <description> (#<PR number>)
```

허용 타입:
- `Docs` — 문서 업데이트
- `Build` — 빌드 시스템, 의존성, 설정/CI
- `Core` — 핵심 기능 및 주요 코드(`src/co_op_translator/core` 등)

예시:
- `Docs: 설치 안내를 더 명확하게 수정 (#50)`
- `Core: 이미지 번역 처리 개선 (#60)`

참고:
- PR 제목은 라벨에 따라 자동 접두사가 붙을 수 있으니, 최종 접두사가 올바른지 확인하세요.

### PR 제목 형식

명확하고 간결하게 작성하세요. 최종 squash 커밋과 동일한 구조를 권장합니다:
- `Docs: 설치 안내를 더 명확하게 수정`
- `Core: 이미지 번역 처리 개선`

## 디버깅 및 문제 해결

- 자주 발생하는 문제 및 해결법: `getting_started/troubleshooting.md`
- 지원 언어 및 참고사항(폰트/알려진 이슈 포함): `getting_started/supported-languages.md`
- 노트북 내 링크 문제는 `migrate-links -l "all" -y`로 재실행

## 에이전트 참고사항

- 재현 가능한 환경을 위해 Poetry 사용을 권장하며, 그렇지 않으면 `requirements.txt`를 사용하세요.
- CI에서 CLI를 호출할 때는 환경 변수 또는 `.env` 주입으로 필요한 시크릿을 제공하세요.
- 모노레포 사용자는 이 저장소를 독립 패키지로 사용하면 되며, 하위 패키지 조정은 필요하지 않습니다.

- 멀티 아키텍처 안내: ARM 사용자(Apple Silicon/ARM 서버)가 대상이면 `linux/arm64`를 유지하세요. 그렇지 않으면 단순화를 위해 `linux/amd64`만 지원해도 무방합니다.
- 컨테이너 사용을 선호하는 사용자는 `README.md`의 Docker 빠른 시작을 안내하세요. Bash와 PowerShell 버전 모두 포함해 따옴표 차이로 인한 혼동을 방지하세요.

---

**면책 조항**:
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있지만, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서(원어)가 권위 있는 자료로 간주되어야 합니다. 중요한 정보의 경우 전문 번역가의 번역을 권장합니다. 본 번역을 사용함으로써 발생하는 오해나 오역에 대해 당사는 책임을 지지 않습니다.