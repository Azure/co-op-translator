# CLI 참조

Co-op Translator는 다음 명령줄 진입점을 설치합니다:

- `translate`
- `evaluate`
- `migrate-links`
- `co-op-review`
- `co-op-translator-mcp`

`translate`, `evaluate`, `migrate-links`, 및 `co-op-review` 명령은 `co_op_translator.__main__`을 통해 디스패치되며, 호출된 스크립트 이름에 따라 명령 구현을 선택합니다. MCP 서버는 `co_op_translator.mcp.server`를 직접 사용합니다.

CLI, Python API 및 MCP 중에서 결정하려면 [작업 흐름 선택](workflows.md)에서 시작하세요.

## 콘솔 출력

대화형 터미널은 명령 헤더, 진행 상황 및 요약에 Rich 형식을 사용합니다. CI 및 비대화형 출력은 자동으로 일반 텍스트로 대체됩니다.

`CO_OP_TRANSLATOR_OUTPUT_STYLE=plain`로 설정하면 일반 출력을 강제하고, `CO_OP_TRANSLATOR_OUTPUT_STYLE=rich`로 설정하면 Rich 출력을 강제합니다. `CO_OP_TRANSLATOR_NO_PROGRESS=1`을 설정하면 실시간 진행 표시줄은 숨기고 요약은 유지합니다.

다른 시스템이 기계 판독 가능한 진행 정보를 필요로 할 때 `translate --json-events progress.ndjson`를 사용하세요.
CLI는 계속해서 사람이 보는 출력을 렌더링하는 동안,
NDJSON 파일은 버전이 지정된 `co-op.translation.event.v1` 이벤트를 수신하며
`type`, `stage_key`, `completed`, `total` 같은 안정적인 필드를 포함합니다,
`current_path`.

## 처음 사용하는 CLI 흐름

터미널에서 Co-op Translator를 사용하는 경우 여기서 시작하세요:

1. [구성](configuration.md)에 설명된 대로 LLM 공급자를 구성하세요.
2. 번역하려는 콘텐츠 유형을 선택하세요.
3. 먼저 Markdown 전용 번역과 같은 특정 작업에 집중한 명령을 실행하세요.
4. 대규모 저장소 변경 전에 `--dry-run`을 사용하세요.
5. 구조와 최신성을 확인하기 위해 번역 후 `co-op-review`를 사용하세요.

| 목표 | 시작할 명령 |
| --- | --- |
| Markdown 문서 번역 | `translate -l "ko" -md` |
| 노트북 번역 | `translate -l "ko" -nb` |
| 이미지 내 텍스트 번역 | `translate -l "ko" -img` |
| 파일을 쓰지 않고 작업 미리보기 | `translate -l "ko" -md --dry-run` |
| 기존 번역 검토 | `co-op-review -l "ko"` |
| 노트북 및 Markdown 링크 업데이트 | `migrate-links -l "ko" --dry-run` |
| 도구를 MCP 클라이언트에 노출 | CLI 명령을 직접 실행하는 대신 [MCP 서버](mcp.md)를 구성하세요. |

## translate

Markdown 파일, 노트북 및 이미지 텍스트를 하나 이상의 대상 언어로 번역합니다.

```bash
translate -l "ko ja fr"
```

### 일반 예제

Markdown만 번역:

```bash
translate -l "de" -md
```

노트북만 번역:

```bash
translate -l "zh-CN" -nb
```

Markdown 및 이미지 번역:

```bash
translate -l "pt-BR" -md -img
```

기존 번역을 삭제하고 다시 생성하여 업데이트:

```bash
translate -l "ko" -u
```

대화형 프롬프트 없이 실행:

```bash
translate -l "ko ja" -md -y
```

로그 저장:

```bash
translate -l "ko" -s
```

구조화된 진행 이벤트 기록:

```bash
translate -l "ko ja" -md --json-events progress.ndjson
```

### 옵션

| 옵션 | 필수 | 설명 |
| --- | --- | --- |
| `-l`, `--language-codes` | 예 | 공백으로 구분된 언어 코드, 예: `"es fr de"`, 또는 `"all"`. |
| `-r`, `--root-dir` | 아니오 | 프로젝트 루트. 기본값은 현재 디렉터리입니다. |
| `-u`, `--update` | 아니오 | 선택한 언어에 대한 기존 번역을 삭제하고 다시 생성합니다. |
| `-img`, `--images` | 아니오 | 이미지 파일만 번역합니다. |
| `-md`, `--markdown` | 아니오 | Markdown 파일만 번역합니다. |
| `-nb`, `--notebook` | 아니오 | Jupyter 노트북 파일만 번역합니다. |
| `-d`, `--debug` | 아니오 | 콘솔에서 디버그 로깅을 활성화합니다. |
| `-s`, `--save-logs` | 아니오 | DEBUG 레벨 로그를 `<root-dir>/logs/`에 저장합니다. |
| `--json-events` | 아니오 | 기계 판독 가능한 번역 진행 이벤트를 NDJSON으로 기록합니다. |
| `-x`, `--fix` | 아니오 | 이전 평가 결과를 기반으로 신뢰도가 낮은 Markdown 파일을 재번역합니다. |
| `-c`, `--min-confidence` | 아니오 | `--fix`에 대한 신뢰도 임계값. 기본값은 `0.7`입니다. |
| `--add-disclaimer`, `--no-disclaimer` | 아니오 | 기계 번역 면책 조항을 추가하거나 숨깁니다. CLI에서는 기본적으로 활성화되어 있습니다. |
| `-f`, `--fast` | 아니오 | 더 이상 권장되지 않는 빠른 이미지 모드입니다. |
| `-y`, `--yes` | 아니오 | 프롬프트를 자동으로 확인합니다( CI에서 유용 ). |
| `--repo-url` | 아니오 | README 언어 표의 sparse-checkout 권고에 사용되는 저장소 URL입니다. |
| `--migrate-language-folders` | 아니오 | `cn` 또는 `tw` 같은 이전 별칭 폴더를 표준 BCP 47 폴더 이름으로 변경합니다. |
| `--dry-run` | 아니오 | 파일을 쓰지 않고 언어 폴더 이전 및 번역 추정치를 미리 봅니다. |

타입 플래그가 제공되지 않으면 `translate`는 Markdown, 노트북 및 이미지를 처리합니다. 이미지 번역은 Azure AI Vision 구성이 필요합니다.

## evaluate

하나의 언어에 대해 번역된 Markdown의 품질을 평가합니다.

!!! warning "실험적"
    `evaluate`는 실험적입니다. 규칙 기반 및 LLM 기반 품질 검사 모두를 사용할 수 있으며, 평가 결과를 번역 메타데이터에 기록하고 점수 모델 및 메타데이터 동작은 변경될 수 있습니다.

```bash
evaluate -l "ko"
```

### 일반 예제

더 엄격한 저신뢰도 임계값 사용:

```bash
evaluate -l "es" -c 0.8
```

규칙 기반 검사만 실행:

```bash
evaluate -l "fr" -f
```

LLM 기반 검사만 실행:

```bash
evaluate -l "ja" -D
```

### 옵션

| 옵션 | 필수 | 설명 |
| --- | --- | --- |
| `-l`, `--language-code` | 예 | 평가할 단일 언어 코드. 별칭 코드는 정규화됩니다. |
| `-r`, `--root-dir` | 아니오 | 프로젝트 루트. 기본값은 현재 디렉터리입니다. |
| `-c`, `--min-confidence` | 아니오 | 저신뢰 번역을 나열할 때 사용되는 임계값. 기본값은 `0.7`입니다. |
| `-d`, `--debug` | 아니오 | 디버그 로깅을 활성화합니다. |
| `-s`, `--save-logs` | 아니오 | DEBUG 레벨 로그를 `<root-dir>/logs/`에 저장합니다. |
| `-f`, `--fast` | 아니오 | 규칙 기반 평가만 실행합니다. |
| `-D`, `--deep` | 아니오 | LLM 기반 평가만 실행합니다. |

기본적으로 `evaluate`는 규칙 기반 및 LLM 기반 평가를 모두 사용합니다. 결과는 번역 메타데이터에 기록되며 콘솔에 요약됩니다.

## co-op-review

API 자격 증명 없이 결정론적 번역 유지보수 검사를 실행합니다.

!!! note "베타"
    `co-op-review`는 베타 상태의 결정론적 검토 명령입니다. 이 명령은 모델 제공자를 호출하거나 파일을 작성하지 않지만, 검사 및 이슈 출력 스키마는 변경될 수 있습니다.

```bash
co-op-review -l "ko"
```

### 일반 예제

현재 디렉터리에서 한국어 및 일본어 번역 검토:

```bash
co-op-review -l "ko ja"
```

특정 프로젝트 루트 검토:

```bash
co-op-review -l "fr" -r ./my-course
```

README 전용 번역 후 README만 검토:

```bash
translate -l "ko" --readme-only -y
co-op-review -l "ko" --readme-only --format github
```

`--readme-only`는 다른 문서와 중첩된 README를 무시합니다. 루트 `README.md`가 없으면 실패합니다.
`--changed-from`와 함께 사용하면, 해당 소스 파일이 변경된 경우에만 README만 검토합니다.
README 전용 번역은 소스 README를 변경하지 않습니다,
공유 섹션 마커를 포함하여 그대로 둡니다.

기준 참조와 비교하여 변경된 소스 파일만 검토:

```bash
co-op-review -l "ko" --changed-from origin/main
```

CI 요약을 위해 GitHub 스타일의 Markdown 출력:

```bash
co-op-review -l "ko ja" --changed-from origin/main --format github
```

### 옵션

| 옵션 | 필수 | 설명 |
| --- | --- | --- |
| `-l`, `--language-code` | 아니오 | 검토할 언어 코드. 여러 번 전달하거나 공백으로 구분된 값으로 전달할 수 있습니다. 기본값은 발견된 모든 번역 언어입니다. |
| `-r`, `--root-dir` | 아니오 | 프로젝트 루트. 기본값은 현재 디렉터리입니다. |
| `--changed-from` | 아니오 | 변경된 소스 파일로 검토를 제한하는 데 사용되는 Git 참조입니다. |
| `--readme-only` | 아니오 | 루트 `README.md` 번역만 검토합니다. |
| `--format` | 아니오 | 출력 형식: `text` 또는 `github`. 기본값은 `text`입니다. |

`co-op-review`는 현재 누락된 번역 파일, 누락되었거나 오래된 번역 메타데이터, Markdown 프론트매터 및 코드 펜스 무결성, 잘못된 번역된 노트북 JSON, 그리고 누락된 로컬 Markdown 또는 이미지 링크 대상 등을 검사합니다. 누락된 링크는 기본적으로 경고이며, 구조적 문제나 최신성 문제는 명령을 실패하게 합니다.

## co-op-translator-mcp

에이전트, 에디터 및 MCP 호환 클라이언트를 위해 Co-op Translator MCP 서버를 실행합니다.

```bash
co-op-translator-mcp
```

기본 전송 방식은 `stdio`입니다. 클라이언트 구성, 도구, 리소스 및 안전 관련 메모는 [MCP 서버](mcp.md) 안내서를 참조하세요.

### 옵션

| 옵션 | 필수 | 설명 |
| --- | --- | --- |
| `--transport` | 아니오 | MCP 전송 방식: `stdio`, `streamable-http`, 또는 `sse`. 기본값은 `stdio`입니다. |

## migrate-links

번역된 Markdown 파일을 재처리하고 사용 가능한 경우 노트북 링크가 번역된 노트북을 가리키도록 업데이트합니다.

```bash
migrate-links -l "ko ja"
```

### 일반 예제

링크 업데이트 미리보기:

```bash
migrate-links -l "ko" --dry-run
```

확인 없이 모든 지원 언어 처리:

```bash
migrate-links -l "all" -y
```

번역된 노트북이 존재할 때만 링크 재작성:

```bash
migrate-links -l "ko" --no-fallback-to-original
```

### 옵션

| 옵션 | 필수 | 설명 |
| --- | --- | --- |
| `-l`, `--language-codes` | 예 | 공백으로 구분된 언어 코드 또는 `"all"`. |
| `-r`, `--root-dir` | 아니오 | 프로젝트 루트. 기본값은 현재 디렉터리입니다. |
| `--image-dir` | 아니오 | 루트 기준의 번역된 이미지 디렉터리. 기본값은 `translated_images`. |
| `--dry-run` | 아니오 | 업데이트를 작성하지 않고 변경될 파일을 표시합니다. |
| `--fallback-to-original`, `--no-fallback-to-original` | 아니오 | 번역된 노트북이 없을 경우 원본 노트북 링크를 사용합니다. 기본적으로 활성화되어 있습니다. |
| `-d`, `--debug` | 아니오 | 디버그 로깅을 활성화합니다. |
| `-s`, `--save-logs` | 아니오 | DEBUG 레벨 로그를 `<root-dir>/logs/`에 저장합니다. |
| `-y`, `--yes` | 아니오 | 모든 언어를 처리할 때 프롬프트를 자동 확인합니다. |

## 환경

명령이 제공자 자격 증명을 필요로 할 때는 다음 제공자 세트 중 하나를 구성하세요. `translate --dry-run`와 `co-op-review`는 제공자 자격 증명이 필요하지 않습니다:

```bash
# Azure OpenAI
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"

# 또는 OpenAI
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"

# 또는 Anthropic
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

이미지 번역에는 추가로 Azure AI Vision이 필요합니다:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

## 출력 레이아웃

텍스트 번역은 다음 경로에 기록됩니다:

```text
translations/<language-code>/<original-path>
```

번역된 이미지 출력은 다음 경로에 기록됩니다:

```text
translated_images/<language-code>/<original-path>
```

예를 들어 `README.md` 및 `docs/setup.md`를 한국어로 번역하면 다음과 같은 결과를 생성합니다:

```text
translations/ko/README.md
translations/ko/docs/setup.md
```

## 복사-붙여넣기 CLI 예제

Markdown을 세 언어로 번역:

```bash
translate -l "ko ja fr" -md
```

노트북만 번역:

```bash
translate -l "zh-CN" -nb
```

이미지만 번역:

```bash
translate -l "pt-BR" -img
```

파일을 쓰지 않고 Markdown 번역 미리보기:

```bash
translate -l "de es" -md --dry-run
```

신뢰도가 낮은 Markdown 번역 복구:

```bash
evaluate -l "ko" -c 0.8
translate -l "ko" --fix -c 0.8 -md
```

CI 친화적인 Markdown 번역 실행:

```bash
translate -l "ko ja" -md -y -s
```

번역된 출력 검토:

```bash
co-op-review -l "ko ja"
```

링크 이전 미리보기:

```bash
migrate-links -l "ko" --dry-run
```