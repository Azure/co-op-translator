# MCP 서버

Co-op Translator에는 에이전트, 편집기 및 MCP 호환 클라이언트를 위한 Model Context Protocol 서버가 포함되어 있습니다.

기본 로컬 설정에서는 사용자가 별도의 서버를 수동으로 실행할 필요가 없습니다. MCP 클라이언트를 구성하면, 클라이언트가 Co-op Translator 도구가 필요할 때 `co-op-translator-mcp`를 자동으로 `stdio`를 통해 시작합니다.

결정해야 하는 상황이 CLI, Python API, MCP 중이라면 [작업 흐름 선택](workflows.md)에서 시작하세요.

에이전트나 편집기가 Co-op Translator를 직접 호출해야 할 때 MCP를 사용하세요:

| 사용자 목표 | MCP 도구 |
| --- | --- |
| Markdown 문서, 노트북 또는 이미지 하나 번역 | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content` |
| 호스트 에이전트 모델로 Markdown 또는 노트북 콘텐츠 번역 | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| 출력 경로를 선택한 후 번역된 Markdown 또는 노트북 링크 재작성 | `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| CLI처럼 전체 저장소 번역 | `run_translation`, `translate_project` |
| LLM 자격증명 없이 번역된 출력 검토 | `run_review` |
| 기능 및 환경 상태 확인 | `get_api_overview`, `list_supported_languages`, `get_configuration_status` |

MCP 서버는 [Python API](api.md)에 문서화된 동일한 공개 Python API를 래핑합니다. 프로바이더 기반 도구는 CLI 및 Python API와 동일하게 구성된 제공자를 사용합니다. 에이전트 지원 도구는 MCP 호스트 에이전트가 번역할 청크를 준비한 다음 Co-op Translator를 사용하여 최종 Markdown 또는 노트북을 재구성합니다.

## 1단계: Co-op Translator 설치 및 구성

MCP 클라이언트가 사용할 Python 환경에 Co-op Translator를 설치하세요:

```bash
pip install co-op-translator
```

이 저장소에서 로컬 개발을 하는 경우 패키지를 편집 가능 모드로 설치하세요:

```bash
pip install -e .
```

MCP 클라이언트가 사용할 번역 모드를 선택하세요:

| 모드 | 사용 대상 | 자격 증명 |
| --- | --- | --- |
| 프로바이더 기반 | Co-op Translator가 `translate_markdown_content`, `translate_notebook_content`, `translate_image_content` 또는 `run_translation`을 호출합니다. | 번역에는 Azure OpenAI, OpenAI 또는 Anthropic이 필요합니다. 이미지 번역은 또한 Azure AI Vision이 필요합니다. |
| 에이전트 지원 | MCP 호스트 에이전트가 `start_markdown_agent_translation` 또는 `start_notebook_agent_translation`이 반환한 청크를 번역합니다. | Markdown 또는 노트북 청크에는 Co-op Translator LLM 제공자 자격증명이 필요하지 않습니다. 이미지 번역은 아직 에이전트 지원 모드에서 다루지 않습니다. |

Codex나 Claude Code 같은 에이전트 내에서 Markdown 또는 노트북 번역을 시작하는 경우 에이전트 지원 모드부터 시작하세요. Co-op Translator 자체가 구성된 제공자를 호출하도록 하려면(또는 이미지를 번역하거나 CLI와 같은 저장소 수준 번역을 실행하려면) 프로바이더 기반 모드를 사용하세요.

프로바이더 기반 워크플로우의 경우 하나의 제공자를 구성하세요:

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

프로바이더 기반 이미지 번역에는 추가로 다음이 필요합니다:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

!!! note
    에이전트 지원 모드는 현재 Markdown 및 노트북의 Markdown 셀을 다룹니다. 이미지 번역은 여전히 프로바이더 기반 이미지 파이프라인을 사용하며 OCR 및 레이아웃 인식 렌더링을 위해 Azure AI Vision이 필요합니다.

## 2단계: MCP 클라이언트 구성

일반적인 로컬 `stdio` 설정에서는 Co-op Translator를 MCP 클라이언트 구성에 추가하세요. 클라이언트가 프로세스를 자동으로 시작하고 중지합니다.

설치된 패키지 구성:

```json
{
  "mcpServers": {
    "co-op-translator": {
      "command": "co-op-translator-mcp",
      "args": []
    }
  }
}
```

Windows의 소스 체크아웃 구성:

```json
{
  "mcpServers": {
    "co-op-translator": {
      "command": "C:\\Users\\you\\dev\\co-op-translator\\.venv\\Scripts\\python.exe",
      "args": ["-m", "co_op_translator.mcp.server"],
      "cwd": "C:\\Users\\you\\dev\\co-op-translator"
    }
  }
}
```

macOS 또는 Linux의 소스 체크아웃 구성:

```json
{
  "mcpServers": {
    "co-op-translator": {
      "command": "/Users/you/dev/co-op-translator/.venv/bin/python",
      "args": ["-m", "co_op_translator.mcp.server"],
      "cwd": "/Users/you/dev/co-op-translator"
    }
  }
}
```

MCP 클라이언트 구성을 변경한 후에는 클라이언트를 재시작하거나 다시 로드하여 새 서버를 검색할 수 있도록 하세요.

## 3단계: 클라이언트에서 서버 확인

MCP 클라이언트에게 사용 가능한 도구 목록을 요청하거나 먼저 읽기 전용 헬퍼 중 하나를 호출하세요:

```json
{
  "tool": "get_api_overview",
  "arguments": {}
}
```

유용한 첫 검사:

| 도구 | 확인할 사항 |
| --- | --- |
| `get_api_overview` | 서버에 도달 가능한지 확인하고 사용 가능한 워크플로우를 표시합니다. |
| `list_supported_languages` | 패키지된 언어 데이터를 로드할 수 있는지 확인합니다. |
| `get_configuration_status` | 비밀 값을 노출하지 않고 LLM 및 Vision 제공자의 사용 가능 여부를 확인합니다. |

## 4단계: 워크플로우 선택

### 개별 파일 또는 문서 번역

MCP 클라이언트가 이미 문서 콘텐츠나 이미지 경로를 가지고 있고 Co-op Translator가 구성된 번역 제공자를 호출해야 하는 경우 프로바이더 기반 콘텐츠 도구를 사용하세요.

Markdown의 경우:

1. `document`, `language_code`, 선택적으로 `source_path`와 함께 `translate_markdown_content`를 호출합니다.
2. 번역된 결과를 Co-op Translator 출력 레이아웃에 쓸 경우 `rewrite_markdown_paths`를 호출합니다.
3. 클라이언트가 최종 `content`를 쓰거나 반환하게 합니다.

노트북의 경우:

1. 노트북 JSON과 `language_code`로 `translate_notebook_content`를 호출합니다.
2. 번역된 노트북 링크를 대상 경로에 맞게 조정해야 하면 `rewrite_notebook_paths`를 호출합니다.
3. 최종 노트북 JSON을 쓰거나 반환합니다.

이미지의 경우:

1. `image_path`, `language_code`, 선택적으로 `root_dir` 또는 `fast_mode`와 함께 `translate_image_content`를 호출합니다.
2. 반환된 `data_base64` 및 `mime_type`를 읽습니다.
3. `output_path`가 제공되면 번역된 이미지는 해당 경로에 저장됩니다.

콘텐츠 도구는 프로젝트 탐지, 메타데이터 업데이트, 면책조항 또는 자동 경로 재작성 등을 수행하지 않습니다. 호스트 에이전트가 Co-op Translator LLM 제공자 자격증명 없이 Markdown 또는 노트북 청크를 번역하도록 하려면 아래의 에이전트 지원 워크플로우를 사용하세요.

### 호스트 에이전트 모델로 번역

Co-op Translator용 LLM 제공자를 구성하는 대신 코딩 어시스턴트와 같은 MCP 호스트 에이전트가 번역된 텍스트를 생성하게 하려면 에이전트 지원 도구를 사용하세요.

채팅 기반 MCP 클라이언트에서는 보통 도구 JSON을 직접 작성할 필요가 없습니다. 에이전트에게 에이전트 지원 워크플로우를 사용하라고 요청하세요:

```text
Translate this Markdown file to Korean with Co-op Translator MCP.
Use agent-assisted mode: call start_markdown_agent_translation, translate the returned chunks with your own model, then call finish_markdown_agent_translation.
Keep Markdown formatting, code blocks, and links intact.
```

노트북의 경우 동일한 패턴을 사용하세요:

```text
Translate this notebook to Korean with Co-op Translator MCP.
Use start_notebook_agent_translation, translate the returned Markdown-cell chunks with your own model, then call finish_notebook_agent_translation.
Preserve code cells, outputs, and notebook metadata.
```

MCP 클라이언트가 서버 프롬프트를 지원하면 `agent_assisted_markdown_translation_prompt`를 사용하여 클라이언트가 동일한 워크플로우 지침을 로드하게 하세요.

Markdown의 경우:

1. `document`, `language_code`, 선택적으로 `source_path`와 함께 `start_markdown_agent_translation`를 호출합니다.
2. 반환된 각 청크의 `prompt`를 따라 호스트 에이전트에서 번역합니다.
3. 원본 `job`과 `chunk_id` 및 `translated_text`를 사용한 번역된 청크들과 함께 `finish_markdown_agent_translation`를 호출합니다.
4. 콘텐츠가 번역된 대상 경로에 쓰일 경우 `rewrite_markdown_paths`를 호출합니다.

노트북의 경우:

1. 노트북 JSON과 `language_code`로 `start_notebook_agent_translation`를 호출합니다.
2. 반환된 각 청크를 호스트 에이전트에서 번역합니다.
3. 원본 `job`과 번역된 청크들과 함께 `finish_notebook_agent_translation`를 호출합니다.
4. 번역된 노트북 링크에 대상 경로 조정이 필요하면 `rewrite_notebook_paths`를 호출합니다.

에이전트 지원 도구는 Co-op Translator에서 구성된 LLM 제공자를 호출하지 않습니다. 반환된 청크의 번역은 호스트 에이전트의 책임입니다. Co-op Translator는 Markdown 청크화, 플레이스홀더 보존, frontmatter 재구성, 노트북 셀 교체 및 번역 후 정규화를 처리합니다.

### 전체 저장소 번역

사용자가 Co-op Translator가 `translate` CLI처럼 동작하기를 원할 때 `run_translation`을 사용하세요.

저장소 번역은 기본적으로 `dry_run=true`로 설정되어 있어 에이전트가 파일 변경 전 범위를 검사할 수 있습니다:

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "dry_run": true
}
```

The `run_translation` 결과에는 버전이 지정된 `events` 배열이 포함되어
`co-op.translation.event.v1` 진행 이벤트가 포함됩니다. MCP 클라이언트는
`type`, `stage_key`, `completed`, `total`, 및 `current_path`와 같은 필드를 사용해야 하며,
캡처된 콘솔 텍스트를 파싱하는 대신 사용하세요. 이러한 이벤트를 NDJSON 파일에 기록하려면 `json_events_path`를 전달하세요
NDJSON 파일로.

쓰기를 허용하려면 호출자는 `dry_run=false`와 `confirm_write=true`를 모두 설정해야 합니다:

```json
{
  "language_codes": "ko",
  "root_dir": ".",
  "markdown": true,
  "dry_run": false,
  "confirm_write": true
}
```

`translate_project`는 `run_translation`의 호환성 별칭으로 제공됩니다.

### 번역된 출력 검토

LLM 또는 Vision 자격증명을 필요로 하지 않는 결정론적 검사를 위해 `run_review`를 사용하세요:

!!! note "Beta"
    MCP는 베타 `run_review` API를 노출합니다. 이는 읽기 전용 검토 워크플로우에 안전하지만 검토 검사 및 이슈 스키마는 변경될 수 있습니다.

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "notebook": true
}
```

결과에는 캡처된 텍스트 출력과 사용 가능한 경우 구조화된 검토 요약이 포함됩니다.

## 수동 서버 실행

수동 실행은 주로 디버깅이나 장기간 실행되는 서버처럼 동작하는 전송 수단을 위한 것입니다.

기본 stdio 서버 디버깅:

```bash
co-op-translator-mcp
```

소스 체크아웃에서 실행:

```bash
python -m co_op_translator.mcp.server
```

장기간 실행되는 HTTP 또는 SSE 서버 실행:

```bash
co-op-translator-mcp --transport streamable-http
co-op-translator-mcp --transport sse
```

로컬 편집기 및 에이전트 통합의 경우 2단계의 클라이언트 관리 `stdio` 구성을 사용하는 것을 권장합니다.

## 도구

| 도구 | 목적 | 파일 작성 여부 |
| --- | --- | --- |
| `translate_markdown_content` | Markdown 문자열을 번역합니다. | 아니요 |
| `translate_notebook_content` | 노트북 JSON의 Markdown 셀을 번역합니다. | 아니요 |
| `translate_image_content` | 이미지 하나의 텍스트를 번역하고 base64 이미지 데이터를 반환합니다. | 선택적, `output_path`가 제공된 경우에만 |
| `start_markdown_agent_translation` | Co-op Translator LLM 자격증명 없이 호스트 에이전트가 번역할 수 있도록 Markdown 청크를 준비합니다. | 아니요 |
| `finish_markdown_agent_translation` | 호스트 에이전트가 번역한 청크로부터 Markdown을 재구성합니다. | 아니요 |
| `start_notebook_agent_translation` | 호스트 에이전트가 번역할 노트북 Markdown 셀 청크를 준비합니다. | 아니요 |
| `finish_notebook_agent_translation` | 호스트 에이전트가 번역한 청크로부터 노트북 JSON을 재구성합니다. | 아니요 |
| `rewrite_markdown_paths` | 번역된 대상에 대해 Markdown 본문 및 frontmatter 경로를 재작성합니다. | 아니요 |
| `rewrite_notebook_paths` | 노트북 Markdown 셀 내의 경로를 재작성합니다. | 아니요 |
| `run_translation` | CLI처럼 프로젝트 수준 번역을 실행합니다. | 예 — `dry_run=false` 및 `confirm_write=true`일 때 |
| `translate_project` | `run_translation`의 호환성 별칭입니다. | 예 — `dry_run=false` 및 `confirm_write=true`일 때 |
| `run_review` | 결정론적 검토 검사를 실행합니다. | 아니요 |
| `get_configuration_status` | 비밀을 노출하지 않고 구성된 LLM 및 Vision 제공자 상태를 보고합니다. | 아니요 |
| `list_supported_languages` | 지원되는 대상 언어 코드를 나열합니다. | 아니요 |
| `get_api_overview` | 사용 가능한 MCP 워크플로우와 도구를 설명합니다. | 아니요 |

## 리소스

| 리소스 URI | 목적 |
| --- | --- |
| `co-op://api` | 워크플로우 및 도구에 대한 JSON 개요. |
| `co-op://supported-languages` | 지원되는 언어 코드의 JSON 목록. |
| `co-op://configuration` | 비밀 없이 제공자 사용 가능성 요약의 JSON. |

## 프롬프트

| 프롬프트 | 목적 |
| --- | --- |
| `translate_markdown_document_prompt` | MCP 클라이언트가 콘텐츠 번역 및 선택적 경로 재작성을 수행하도록 안내합니다. |
| `agent_assisted_markdown_translation_prompt` | Co-op Translator LLM 제공자 자격증명 없이 호스트 에이전트 Markdown 번역을 수행하도록 MCP 클라이언트를 안내합니다. |
| `translate_repository_prompt` | 먼저 dry-run을 수행하는 저장소 번역을 MCP 클라이언트가 수행하도록 안내합니다. |

## 복사-붙여넣기 예제

Markdown 콘텐츠 번역:

```json
{
  "tool": "translate_markdown_content",
  "arguments": {
    "document": "# Hello\n\nWelcome to the course.",
    "language_code": "ko",
    "source_path": "docs/guide.md"
  }
}
```

번역된 Markdown 링크 재작성:

```json
{
  "tool": "rewrite_markdown_paths",
  "arguments": {
    "content": "[Setup](../setup.md)\n\n![Hero](images/hero.png)",
    "source_path": "docs/guide.md",
    "target_path": "translations/ko/docs/guide.md",
    "policy": {
      "language_code": "ko",
      "root_dir": ".",
      "translations_dir": "translations",
      "translated_images_dir": "translated_images",
      "translation_types": ["markdown", "images"]
    }
  }
}
```

호스트 에이전트 모델로 Markdown 번역:

```json
{
  "tool": "start_markdown_agent_translation",
  "arguments": {
    "document": "# Hello\n\nUse `pip install` to get started.",
    "language_code": "ko",
    "source_path": "docs/guide.md"
  }
}
```

호스트 에이전트가 반환된 각 청크를 번역한 후에는 `start_markdown_agent_translation`이 반환한 전체 `job` 객체로 작업을 완료하세요:

```text
tool: finish_markdown_agent_translation
arguments:
  job: <the full job object returned by start_markdown_agent_translation>
  translated_chunks:
    - chunk_id: body:1
      translated_text: "# 안녕하세요\n\n시작하려면 `pip install`을 사용하세요."
```

저장소 번역 미리보기:

```json
{
  "tool": "run_translation",
  "arguments": {
    "language_codes": "ko",
    "root_dir": ".",
    "markdown": true,
    "dry_run": true
  }
}
```

## 문제 해결

| 문제 | 시도할 사항 |
| --- | --- |
| MCP 클라이언트가 `co-op-translator-mcp`를 찾을 수 없습니다. | 절대 Python 실행 파일 경로와 `["-m", "co_op_translator.mcp.server"]` 소스 체크아웃 구성을 사용하세요. |
| 서버가 나열되지만 번역이 실패합니다. | `get_configuration_status`를 호출하고 LLM 제공자가 사용 가능한지 확인하세요. |
| 프로바이더 자격증명 없이 Markdown 또는 노트북 번역을 원합니다. | `start_markdown_agent_translation` / `finish_markdown_agent_translation` 또는 노트북 등가물을 사용하여 호스트 에이전트가 청크를 번역하게 하세요. |
| 이미지 번역이 실패합니다. | Azure AI Vision 변수가 설정되어 있는지 확인하고 `get_configuration_status`를 호출하세요. |
| 저장소 번역이 파일을 쓰지 않습니다. | 명시적인 사용자 승인을 받은 후에만 `dry_run=false`와 `confirm_write=true`를 설정하세요. |
| 클라이언트 구성 변경이 반영되지 않습니다. | MCP 클라이언트를 재시작하거나 다시 로드하세요. |

## 안전 참고사항

- MCP 도구 호출은 호스트 애플리케이션에 의해 모델 제어되므로 저장소 번역은 기본적으로 dry-run입니다.
- 전체 저장소 번역은 많은 파일을 생성, 업데이트 또는 제거할 수 있습니다. `confirm_write=true`를 설정하기 전에 명시적인 사용자 승인을 요구하세요.
- 구성 상태 도구는 API 키, 엔드포인트 또는 기타 비밀 값을 절대 반환하지 않습니다.
- 이미지 번역은 base64 이미지 데이터를 반환합니다. 큰 이미지는 큰 도구 응답을 생성할 수 있습니다.
- 에이전트 지원 도구는 원본 청크와 프롬프트를 MCP 호스트에 반환합니다. 사용자가 해당 호스트 에이전트 모델에 보내는 것에 동의하는 콘텐츠에만 사용하세요.