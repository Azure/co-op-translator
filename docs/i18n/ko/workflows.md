# 워크플로 선택

Co-op Translator는 CLI, Python API, MCP 서버의 세 가지 방식으로 사용할 수 있습니다. 이들은 동일한 번역 기능을 공유하지만 각각 다른 워크플로에 적합합니다.

어디서 시작할지 결정할 때 이 페이지를 사용하세요.

**번역을 수동으로 편집하는 경우:** 기본 CLI 및 Actions 워크플로는 변경된 소스 파일을 전체 재번역하므로 해당 파일의 문구가 덮어써질 수 있습니다. 업데이트를 수락하기 전에 diff를 검토하세요. 수락된 수정의 Markdown 블록 수준 보존을 위해서는 선택적 [Python API 번역 상태 제공자](api.md#preserve-accepted-human-edits-with-a-translation-state-provider)를 사용하세요.

## 빠른 결정

| 원하는 경우... | 사용 | 시작하기 |
| --- | --- | --- |
| 터미널에서 저장소를 번역하거나 검토하려는 경우 | CLI | [CLI 참조](cli.md) |
| Python 스크립트, 서비스, 노트북 또는 CI 작업에 번역을 추가하려는 경우 | Python API | [Python API](api.md) |
| 에이전트, 편집기 또는 MCP 호환 클라이언트가 콘텐츠를 대신 번역하도록 하려는 경우 | MCP Server | [MCP Server](mcp.md) |
| 앱이 이미 로드한 Markdown 문서, 노트북 또는 이미지를 번역하려는 경우 | Python API 또는 MCP Server | [Python API](api.md) 또는 [MCP Server](mcp.md) |
| 표준 출력 폴더 및 메타데이터와 함께 전체 저장소를 번역하려는 경우 | CLI 또는 `run_translation` | [CLI 참조](cli.md) 또는 [Python API](api.md) |

## CLI를 사용할 때

사람이나 CI 작업이 셸에서 저장소 번역을 수행할 때 CLI를 선택하세요.

Co-op Translator가 프로젝트 파일을 탐색하고, 번역된 출력을 생성하고, 프로젝트 레이아웃을 보존하고, 메타데이터를 업데이트하고, 검토 명령을 실행하길 원할 때 CLI가 가장 직접적인 경로입니다.

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -md -nb
co-op-review -l "ko"
migrate-links -l "ko" --dry-run
```

이 예제는 Markdown과 노트북을 번역합니다. `-img`는 [Azure AI Vision](configuration.md#azure-ai-vision)을 구성한 후에만 추가하세요. Markdown 전용 첫 실행은 [첫 번역](first-translation.md)을 따르세요.

적합한 경우:

- 터미널에서 저장소를 번역하고 있는 경우.
- CI 또는 릴리스 워크플로를 위한 반복 가능한 명령을 원할 경우.
- 빌트인 프로젝트 탐색, 출력 경로, 메타데이터, 정리 및 검토 기능을 원할 경우.
- Python 코드를 작성하는 것보다 명령 인터페이스를 선호하는 경우.

## Python API를 사용할 때

자신의 코드가 워크플로를 제어해야 할 때 Python API를 선택하세요.

API는 애플리케이션, 자동화 스크립트, 노트북, 서비스 및 맞춤 파이프라인에 유용합니다. 개별 파일에 대한 저수준 콘텐츠 번역 API를 호출하거나 CLI가 사용하는 동일한 리포지토리 수준 오케스트레이션을 실행할 수 있습니다.

Markdown 문서 하나를 번역하고 저장 위치를 결정하세요:

```python
import asyncio
from pathlib import Path

from co_op_translator.api import rewrite_markdown_paths, translate_markdown_content


async def main() -> None:
    source_path = Path("docs/guide.md")
    target_path = Path("translations/ko/docs/guide.md")

    translated = await translate_markdown_content(
        source_path.read_text(encoding="utf-8"),
        "ko",
        {"source_path": source_path},
    )

    rewritten = rewrite_markdown_paths(
        translated,
        source_path=source_path,
        target_path=target_path,
    )

    target_path.parent.mkdir(parents=True, exist_ok=True)
    target_path.write_text(rewritten, encoding="utf-8")


asyncio.run(main())
```

Python에서 리포지토리 번역을 실행하세요:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    notebook=True,
    images=False,
    dry_run=True,
)
```

적합한 경우:

- 애플리케이션이 이미 파일, 버퍼, 노트북 또는 이미지 바이트를 읽고 있는 경우.
- 사용자 정의 검증, 저장, 로깅, 재시도 또는 승인 흐름이 필요한 경우.
- 전체 저장소를 처리하지 않고 문서, 노트북 또는 이미지 하나만 번역하려는 경우.
- 저장소 번역을 원하지만 셸 명령 대신 Python 자동화에서 실행하려는 경우.

## MCP 서버를 사용할 때

에이전트, 편집기 또는 MCP 호환 클라이언트가 Co-op Translator 도구를 호출해야 할 때 MCP 서버를 선택하세요.

일반적인 로컬 설정에서는 사용자가 수동으로 서버를 계속 실행할 필요가 없습니다. MCP 클라이언트는 도구가 필요할 때 `co-op-translator-mcp`를 `stdio`를 통해 시작합니다.

에이전트가 처리할 수 있는 사용자 요청 예시:

- "이 Markdown 파일을 한국어로 번역하고 링크를 올바르게 유지해 주세요."
- "에이전트 지원 MCP 워크플로를 사용하여 이 Markdown 파일을 한국어로 번역하되, 번역된 청크에는 자신의 모델을 사용하세요."
- "이 노트북을 한국어로 번역하고 코드 셀을 보존하며 Co-op Translator MCP를 사용해 노트북을 재구성하세요."
- "이 이미지의 텍스트를 일본어로 번역하고 결과를 저장하세요."
- "저장소 번역을 스페인어로 dry-run하고 어떤 변경이 있을지 알려주세요."
- "한국어 번역 출력이 최신인지 검토하세요."

Markdown과 노트북의 경우 MCP는 두 가지 모드로 작동할 수 있습니다:

| 모드 | 사용 시 | 주요 도구 |
| --- | --- | --- |
| Agent-assisted | MCP 호스트 에이전트가 Co-op Translator LLM 제공자 자격증명 없이 자체 모델로 청크를 번역해야 할 때. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Provider-backed | Co-op Translator가 Azure OpenAI, OpenAI 또는 Anthropic을 직접 호출해야 할 때. | `translate_markdown_content`, `translate_notebook_content` |

MCP 제공자 기반 Markdown 도구 호출 형식:

```json
{
  "tool": "translate_markdown_content",
  "arguments": {
    "document": "# Setup\n\nInstall Co-op Translator first.",
    "language_code": "ko",
    "options": {
      "source_path": "docs/setup.md"
    }
  }
}
```

MCP 이미지 도구 호출 형식:

```json
{
  "tool": "translate_image_content",
  "arguments": {
    "image_path": "assets/architecture.png",
    "language_code": "ko",
    "output_path": "translated_images/ko/assets/architecture.png"
  }
}
```

저장소 번역은 기본적으로 MCP를 통해 dry-run(모의 실행)됩니다:

```json
{
  "tool": "run_translation",
  "arguments": {
    "language_codes": ["ko"],
    "translate_markdown": true,
    "translate_notebooks": true,
    "translate_images": false,
    "dry_run": true
  }
}
```

적합한 경우:

- 에이전트나 편집기 내부에서 자연어 번역 워크플로를 원할 경우.
- 호스트 에이전트 모델이 준비된 청크를 번역하는 Markdown 또는 노트북 번역을 원할 경우.
- 전체 저장소 대신 에이전트가 선택한 콘텐츠만 번역하길 원할 경우.
- 저장소 전체에 쓰기 전에 승인 단계를 원할 경우.
- Markdown, 노트북, 이미지, 검토 및 경로 재작성 도구를 노출하는 단일 인터페이스를 원할 경우.

## 어떻게 함께 작동하는지

CLI는 사람이 저장소를 번역할 때 기본적으로 가장 적합합니다. Python API는 코드가 워크플로를 담당할 때 가장 적합합니다. MCP 서버는 에이전트나 편집기가 워크플로를 담당할 때 가장 적합합니다.

세 경로 모두 동일한 공개 Co-op Translator API를 사용하므로 CLI로 시작하고 나중에 Python으로 자동화하며 에이전트 기반 워크플로가 필요할 때 MCP 클라이언트에 동일한 기능을 노출할 수 있습니다.