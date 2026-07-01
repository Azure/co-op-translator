# CLI 참조

Co-op Translator는 다음 명령줄 진입점을 설치합니다:

- `translate`
- `evaluate`
- `migrate-links`
- `co-op-review`
- `co-op-translator-mcp`

`translate`, `evaluate`, `migrate-links` 및 `co-op-review` 명령은 호출된 스크립트 이름에 따라 명령 구현을 선택하는 `co_op_translator.__main__`를 통해 디스패치됩니다. MCP 서버는 `co_op_translator.mcp.server`를 직접 사용합니다.

CLI, Python API 및 MCP 중에서 선택하려는 경우 [Choose Your Workflow](workflows.md)에서 시작하세요.

## 처음 사용하는 CLI 흐름

터미널에서 Co-op Translator를 사용하는 경우 여기에 따라 시작하세요:

1. [Configuration](configuration.md)에 설명된 대로 LLM 공급자를 구성합니다.
2. 번역하려는 콘텐츠 유형을 선택합니다.
3. 먼저 Markdown 전용 번역과 같은 집중된 명령을 실행합니다.
4. 대규모 리포지토리 변경 전에 `--dry-run`을 사용하세요.
5. 번역 후 구조와 최신성을 확인하려면 `co-op-review`를 사용하세요.

| 목표 | 시작할 명령 |
| --- | --- |
| Markdown 문서 번역 | `translate -l "ko" -md` |
| 노트북 번역 | `translate -l "ko" -nb` |
| 이미지 텍스트 번역 | `translate -l "ko" -img` |
| 파일을 작성하지 않고 작업 미리보기 | `translate -l "ko" -md --dry-run` |
| 기존 번역 검토 | `co-op-review -l "ko"` |
| 노트북 및 Markdown 링크 업데이트 | `migrate-links -l "ko" --dry-run` |
| 도구를 MCP 클라이언트에 노출 | CLI 명령을 직접 실행하는 대신 [MCP Server](mcp.md)를 구성하세요. |

## translate

Markdown 파일, 노트북 및 이미지 텍스트를 하나 이상의 대상 언어로 번역합니다.

```bash
translate -l "ko ja fr"
```

### 일반적인 예

Markdown만 번역:

```bash
translate -l "de" -md
```

노트북만 번역:

```bash
translate -l "zh-CN" -nb
```

Markdown과 이미지 번역:

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

### 옵션

| 옵션 | 필수 | 설명 |
| --- | --- | --- |
| `-l`, `--language-codes` | 예 | 공백으로 구분된 언어 코드(예: `"es fr de"`) 또는 `"all"`. |
| `-r`, `--root-dir` | 아니요 | 프로젝트 루트. 기본값은 현재 디렉터리입니다. |
| `-u`, `--update` | 아니요 | 선택한 언어에 대한 기존 번역을 삭제하고 다시 생성합니다. |
| `-img`, `--images` | 아니요 | 이미지 파일만 번역합니다. |
| `-md`, `--markdown` | 아니요 | Markdown 파일만 번역합니다. |
| `-nb`, `--notebook` | 아니요 | Jupyter 노트북 파일만 번역합니다. |
| `-d`, `--debug` | 아니요 | 콘솔에서 디버그 로깅을 활성화합니다. |
| `-s`, `--save-logs` | 아니요 | `<root-dir>/logs/` 아래에 DEBUG 수준 로그를 저장합니다. |
| `-x`, `--fix` | 아니요 | 이전 평가 결과를 기반으로 신뢰도 낮은 Markdown 파일을 다시 번역합니다. |
| `-c`, `--min-confidence` | 아니요 | `--fix`에 사용되는 신뢰도 임계값. 기본값은 `0.7`입니다. |
| `--add-disclaimer`, `--no-disclaimer` | 아니요 | 기계 번역 경고문을 추가하거나 억제합니다. CLI에서는 기본적으로 활성화되어 있습니다. |
| `-f`, `--fast` | 아니요 | 더 이상 사용되지 않는 빠른 이미지 모드입니다. |
| `-y`, `--yes` | 아니요 | 프롬프트를 자동 확인합니다(CI에서 유용). |
| `--repo-url` | 아니요 | README 언어 표의 sparse-checkout 권고에 사용되는 리포지토리 URL입니다. |
| `--migrate-language-folders` | 아니요 | `cn` 또는 `tw`와 같은 레거시 별칭 폴더를 정식 BCP 47 폴더로 이름 변경합니다. |
| `--dry-run` | 아니요 | 파일을 작성하지 않고 언어 폴더 마이그레이션 및 번역 추정치를 미리 봅니다. |

타입 플래그가 제공되지 않으면 `translate`는 Markdown, 노트북 및 이미지를 처리합니다. 이미지 번역은 Azure AI Vision 구성이 필요합니다.

## evaluate

단일 언어에 대한 번역된 Markdown의 품질을 평가합니다.

!!! warning "실험적"
    `evaluate`는 실험적입니다. 규칙 기반 및 LLM 기반 품질 검사를 사용할 수 있고, 평가 결과를 번역 메타데이터에 기록하며, 점수 모델과 메타데이터 동작은 변경될 수 있습니다.

```bash
evaluate -l "ko"
```

### 일반적인 예

더 엄격한 낮은 신뢰도 임계값 사용:

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
| `-r`, `--root-dir` | 아니요 | 프로젝트 루트. 기본값은 현재 디렉터리입니다. |
| `-c`, `--min-confidence` | 아니요 | 낮은 신뢰도 번역을 나열할 때 사용되는 임계값. 기본값은 `0.7`입니다. |
| `-d`, `--debug` | 아니요 | 디버그 로깅을 활성화합니다. |
| `-s`, `--save-logs` | 아니요 | `<root-dir>/logs/` 아래에 DEBUG 수준 로그를 저장합니다. |
| `-f`, `--fast` | 아니요 | 규칙 기반 평가만 수행합니다. |
| `-D`, `--deep` | 아니요 | LLM 기반 평가만 수행합니다. |

기본적으로 `evaluate`는 규칙 기반과 LLM 기반 평가를 모두 사용합니다. 결과는 번역 메타데이터에 기록되며 콘솔에 요약되어 표시됩니다.

## co-op-review

API 자격 증명 없이 결정론적 번역 유지보수 검사를 실행합니다.

!!! note "베타"
    `co-op-review`는 베타 결정론적 검토 명령입니다. 모델 공급자 호출이나 파일 쓰기를 수행하지 않지만, 검사와 이슈 출력 스키마는 변경될 수 있습니다.

```bash
co-op-review -l "ko"
```

### 일반적인 예

현재 디렉터리에서 한국어 및 일본어 번역을 검토:

```bash
co-op-review -l "ko ja"
```

특정 프로젝트 루트 검토:

```bash
co-op-review -l "fr" -r ./my-course
```

기준 ref와 비교하여 변경된 소스 파일만 검토:

```bash
co-op-review -l "ko" --changed-from origin/main
```

CI 요약용 GitHub 형식의 Markdown 출력:

```bash
co-op-review -l "ko ja" --changed-from origin/main --format github
```

### 옵션

| 옵션 | 필수 | 설명 |
| --- | --- | --- |
| `-l`, `--language-code` | 아니요 | 검토할 언어 코드. 여러 번 전달하거나 공백으로 구분된 값으로 전달할 수 있습니다. 기본값은 발견된 모든 번역 언어입니다. |
| `-r`, `--root-dir` | 아니요 | 프로젝트 루트. 기본값은 현재 디렉터리입니다. |
| `--changed-from` | 아니요 | 변경된 소스 파일로 검토를 제한하는 데 사용되는 Git ref입니다. |
| `--format` | 아니요 | 출력 형식: `text` 또는 `github`. 기본값은 `text`입니다. |

`co-op-review`는 현재 누락된 번역 파일, 누락되었거나 오래된 번역 메타데이터, Markdown frontmatter 및 코드 펜스 무결성, 잘못된 번역된 노트북 JSON, 로컬 Markdown 또는 이미지 링크 대상 누락을 검사합니다. 누락된 링크는 기본적으로 경고이며, 구조적 문제 및 최신성 문제는 명령을 실패하게 합니다.

## co-op-translator-mcp

에이전트, 편집기 및 MCP 호환 클라이언트를 위해 Co-op Translator MCP 서버를 실행합니다.

```bash
co-op-translator-mcp
```

기본 전송 방식은 `stdio`입니다. 클라이언트 구성, 도구, 리소스 및 안전성 관련 주제는 [MCP Server](mcp.md) 가이드를 참조하세요.

### 옵션

| 옵션 | 필수 | 설명 |
| --- | --- | --- |
| `--transport` | 아니요 | MCP 전송 방식: `stdio`, `streamable-http` 또는 `sse`. 기본값은 `stdio`입니다. |

## migrate-links

번역된 Markdown 파일을 재처리하고 가능한 경우 번역된 노트북을 가리키도록 노트북 링크를 업데이트합니다.

```bash
migrate-links -l "ko ja"
```

### 일반적인 예

링크 업데이트 미리보기:

```bash
migrate-links -l "ko" --dry-run
```

확인 없이 모든 지원 언어 처리:

```bash
migrate-links -l "all" -y
```

번역된 노트북이 있는 경우에만 링크를 다시 작성:

```bash
migrate-links -l "ko" --no-fallback-to-original
```

### 옵션

| 옵션 | 필수 | 설명 |
| --- | --- | --- |
| `-l`, `--language-codes` | 예 | 공백으로 구분된 언어 코드 또는 `"all"`. |
| `-r`, `--root-dir` | 아니요 | 프로젝트 루트. 기본값은 현재 디렉터리입니다. |
| `--image-dir` | 아니요 | 루트 기준의 번역된 이미지 디렉터리. 기본값은 `translated_images`입니다. |
| `--dry-run` | 아니요 | 변경될 파일을 표시하되 업데이트를 쓰지 않습니다. |
| `--fallback-to-original`, `--no-fallback-to-original` | 아니요 | 번역된 노트북이 없을 때 원본 노트북 링크를 사용합니다. 기본적으로 활성화되어 있습니다. |
| `-d`, `--debug` | 아니요 | 디버그 로깅을 활성화합니다. |
| `-s`, `--save-logs` | 아니요 | `<root-dir>/logs/` 아래에 DEBUG 수준 로그를 저장합니다. |
| `-y`, `--yes` | 아니요 | 모든 언어를 처리할 때 프롬프트를 자동 확인합니다. |

## 환경

모든 명령은 하나의 구성된 LLM 공급자가 필요합니다:

```bash
# Azure의 OpenAI
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"

# 또는 OpenAI
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

이미지 번역은 추가로 Azure AI Vision이 필요합니다:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

## 출력 레이아웃

텍스트 번역은 다음 위치에 작성됩니다:

```text
translations/<language-code>/<original-path>
```

번역된 이미지 출력은 다음 위치에 작성됩니다:

```text
translated_images/<language-code>/<original-path>
```

예를 들어 `README.md` 및 `docs/setup.md`를 한국어로 번역하면 다음과 같이 생성됩니다:

```text
translations/ko/README.md
translations/ko/docs/setup.md
```

## 복사-붙여넣기용 CLI 예시

Markdown을 세 개 언어로 번역:

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

신뢰도 낮은 Markdown 번역 수정:

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

링크 마이그레이션 미리보기:

```bash
migrate-links -l "ko" --dry-run
```