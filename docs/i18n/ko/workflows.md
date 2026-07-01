# 워크플로 선택

Co-op Translator는 CLI, Python API, MCP 서버의 세 가지 방식으로 사용할 수 있습니다. 이들은 동일한 번역 기능을 공유하지만, 각 방식은 서로 다른 워크플로에 적합합니다.

어디서 시작할지 결정할 때 이 페이지를 사용하세요.

## 빠른 결정

| If you want to... | Use | Start here |
| --- | --- | --- |
| 터미널에서 리포지토리를 번역하거나 검토 | CLI | [CLI Reference](cli.md) |
| Python 스크립트, 서비스, 노트북 또는 CI 작업에 번역 기능 추가 | Python API | [Python API](api.md) |
| 에이전트, 편집기 또는 MCP 호환 클라이언트가 콘텐츠를 번역하게 함 | MCP Server | [MCP Server](mcp.md) |
| 앱이 이미 불러온 단일 Markdown 문서, 노트북 또는 이미지를 번역 | Python API or MCP Server | [Python API](api.md) or [MCP Server](mcp.md) |
| 표준 출력 폴더와 메타데이터를 포함해 전체 저장소를 번역 | CLI or `run_translation` | [CLI Reference](cli.md) or [Python API](api.md) |

## CLI를 사용할 때

사람이나 CI 작업이 셸에서 저장소 번역을 수행할 때 CLI를 선택하세요.

Co-op Translator가 프로젝트 파일을 검색하고, 번역된 출력을 생성하며, 프로젝트 레이아웃을 유지하고, 메타데이터를 업데이트하고, 검토 명령을 실행하기를 원할 때 CLI가 가장 직접적인 경로입니다.

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -md -nb -img
co-op-review -l "ko" -md -nb
migrate-links -l "ko" --dry-run
```

적합한 경우:

- 터미널에서 저장소를 번역하는 경우.
- CI 또는 릴리스 워크플로용으로 반복 가능한 명령을 원할 때.
- 내장된 프로젝트 검색, 출력 경로, 메타데이터, 정리 및 검토 기능을 원할 때.
- Python 코드를 작성하는 것보다 명령 인터페이스를 선호할 때.

## Python API를 사용할 때

자체 코드가 워크플로를 제어해야 할 때 Python API를 선택하세요.

이 API는 애플리케이션, 자동화 스크립트, 노트북, 서비스 및 맞춤 파이프라인에 유용합니다. 개별 파일에 대한 저수준 콘텐츠 번역 API를 호출하거나 CLI에서 사용하는 동일한 리포지토리 수준 오케스트레이션을 실행할 수 있습니다.

단일 Markdown 문서를 번역하고 저장 위치를 결정하려면:

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

Python에서 리포지토리 번역을 실행하려면:

```python
import asyncio

from co_op_translator.api import run_translation


async def main() -> None:
    await run_translation(
        language_codes=["ko"],
        translate_markdown=True,
        translate_notebooks=True,
        translate_images=False,
        dry_run=True,
    )


asyncio.run(main())
```

적합한 경우:

- 애플리케이션이 이미 파일, 버퍼, 노트북 또는 이미지 바이트를 읽는 경우.
- 맞춤 검증, 저장, 로깅, 재시도 또는 승인 흐름이 필요한 경우.
- 전체 저장소를 처리하지 않고 단일 문서, 노트북 또는 이미지를 번역하려는 경우.
- 저장소 번역을 원하지만 셸 명령 대신 Python 자동화에서 실행하려는 경우.

## MCP 서버를 사용할 때

에이전트, 편집기 또는 MCP 호환 클라이언트가 Co-op Translator 도구를 호출해야 할 때 MCP 서버를 선택하세요.

일반적인 로컬 설정에서는 사용자가 수동으로 서버를 계속 실행하지 않습니다. MCP 클라이언트는 도구가 필요할 때 `co-op-translator-mcp`를 `stdio`를 통해 시작합니다.

에이전트가 처리할 수 있는 사용자 요청 예:

- "이 Markdown 파일을 한국어로 번역하고 링크를 올바르게 유지해 주세요."
- "번역된 청크에 대해 자체 모델을 사용하여 에이전트 보조 MCP 워크플로로 이 Markdown 파일을 한국어로 번역해 주세요."
- "이 노트북을 한국어로 번역하고 코드 셀을 보존하며 Co-op Translator MCP를 사용하여 노트북을 재구성해 주세요."
- "이 이미지의 텍스트를 일본어로 번역하고 결과를 저장해 주세요."
- "저장소 번역을 스페인어로 드라이런(dry-run)하고 어떤 것이 변경될지 알려 주세요."
- "한국어 번역 출력이 최신인지 검토해 주세요."

Markdown과 노트북의 경우, MCP는 두 가지 모드로 동작할 수 있습니다:

| Mode | Use when | Main tools |
| --- | --- | --- |
| Agent-assisted | MCP 호스트 에이전트가 Co-op Translator LLM 제공자 자격 증명 없이 자체 모델로 청크를 번역해야 할 때. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Provider-backed | Co-op Translator가 Azure OpenAI 또는 OpenAI를 직접 호출해야 할 때. | `translate_markdown_content`, `translate_notebook_content` |

MCP provider-backed Markdown 도구 호출 형식:

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

저장소 번역은 MCP를 통해 기본적으로 드라이런(dry-run)됩니다:

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

- 에이전트나 편집기 내부에서 자연어 기반 번역 워크플로를 원할 때.
- 호스트 에이전트 모델이 준비된 청크를 번역하는 Markdown 또는 노트북 번역을 원할 때.
- 전체 저장소 대신 에이전트가 선택된 콘텐츠만 번역하길 원할 때.
- 저장소 전체에 쓰기 전에 승인 단계가 필요할 때.
- Markdown, 노트북, 이미지, 검토 및 경로 재작성 도구를 제공하는 하나의 인터페이스를 원할 때.

## 이들이 함께 작동하는 방식

CLI는 사람에게 저장소를 번역할 때 기본적으로 가장 적합합니다. Python API는 코드가 워크플로를 소유할 때 가장 적합합니다. MCP 서버는 에이전트나 편집기가 워크플로를 소유할 때 가장 적합합니다.

세 경로 모두 동일한 공개 Co-op Translator API를 사용하므로, CLI로 시작하고 나중에 Python으로 자동화하며, 에이전트 기반 워크플로가 필요할 때 동일한 기능을 MCP 클라이언트에 제공할 수 있습니다.