# Python API

안정적인 공개 Python API는 `co_op_translator.api`에서 내보냅니다. 대부분의 통합은 다음 워크플로 중 하나를 사용합니다:

| Scenario | Use this when | Main APIs |
| --- | --- | --- |
| Translate individual files or documents | 애플리케이션이 소스 콘텐츠를 읽고 Co-op Translator에 번역을 요청한 후 결과를 저장할 위치를 결정하는 경우. | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Prepare content for host-agent translation | MCP 호스트 또는 애플리케이션 모델이 청크를 번역하고 Co-op Translator가 청크화 및 재구성을 처리하는 경우. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Translate an entire repository | Python API가 CLI처럼 작동하여 검색, 출력 경로, 메타데이터, 정리 및 쓰기를 처리하도록 하려는 경우. | `run_translation` |

`core`, `config`, `review`, 및 `utils` 아래의 대부분 하위 모듈은 이러한 API 진입점에서 사용하는 구현 세부사항입니다.

MCP 클라이언트는 [MCP Server](mcp.md)를 통해 동일한 공개 API를 사용합니다. Python을 직접 호출할 때는 이 페이지를 사용하고, 에이전트나 편집기에 Co-op Translator를 노출할 때는 MCP 가이드를 사용하세요. CLI, Python API 및 MCP 중에서 결정하는 경우 [Choose Your Workflow](workflows.md)에서 시작하세요.

## First-Time API Flow

Python 코드에서 Co-op Translator를 호출하는 경우 여기에서 시작하세요:

1. [Configuration](configuration.md)에 설명된 대로 LLM 공급자를 구성합니다(마크다운 또는 노트북 청크만 호스트-에이전트 번역용으로 준비하는 경우는 제외).
2. 애플리케이션이 파일 I/O를 소유하는지 결정합니다.
3. 애플리케이션이 개별 파일을 읽고 쓰는 경우 콘텐츠 API를 사용합니다.
4. Co-op Translator가 CLI처럼 리포지토리를 처리해야 하면 `run_translation`을 사용합니다.
5. 자동화에서 결정론적 검사가 필요하면 번역 후 `run_review`를 사용합니다.

| Goal | API to start with |
| --- | --- |
| Translate one Markdown string or file | `translate_markdown_content` |
| Translate one notebook payload | `translate_notebook_content` |
| Translate one image | `translate_image_content` |
| Let a host agent translate Markdown or notebook chunks | `start_markdown_agent_translation` or `start_notebook_agent_translation` |
| Rewrite translated links after choosing an output path | `rewrite_markdown_paths` or `rewrite_notebook_paths` |
| Translate a full repository | `run_translation` |
| Review translated output | `run_review` |

## Scenario 1: Translate Individual Files or Documents

파일, 편집기 버퍼, 노트북 페이로드, MCP 요청 또는 사용자 지정 파이프라인 입력이 이미 있는 경우 이 워크플로를 사용하세요. 귀하의 코드가 파일 I/O를 담당합니다:

1. 소스 콘텐츠를 읽습니다.
2. 콘텐츠 번역 API를 호출합니다.
3. 번역된 콘텐츠를 프로젝트 번역 폴더에 쓸 경우 선택적으로 경로 재작성 API를 호출합니다.
4. 애플리케이션에서 결과를 저장하거나 반환합니다.

콘텐츠 번역 API는 프로젝트 검색을 실행하지 않으며, 메타데이터를 쓰지 않으며, 면책 조항을 추가하지 않으며, 자동으로 링크를 재작성하지 않습니다.

### Markdown File

```python
import asyncio
from pathlib import Path

from co_op_translator.api import (
    rewrite_markdown_paths,
    translate_markdown_content,
)


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
        policy={
            "language_code": "ko",
            "root_dir": ".",
            "translations_dir": "translations",
            "translated_images_dir": "translated_images",
            "translation_types": ["markdown", "images"],
        },
    )

    target_path.parent.mkdir(parents=True, exist_ok=True)
    target_path.write_text(rewritten, encoding="utf-8")


asyncio.run(main())
```

번역된 마크다운이 Co-op Translator 프로젝트 레이아웃에 포함되지 않는 경우 `rewrite_markdown_paths`를 건너뛰고 번역된 문자열을 바로 저장하세요.

### Notebook File

```python
import asyncio
from pathlib import Path

from co_op_translator.api import (
    rewrite_notebook_paths,
    translate_notebook_content,
)


async def main() -> None:
    source_path = Path("docs/tutorial.ipynb")
    target_path = Path("translations/ja/docs/tutorial.ipynb")

    translated_json = await translate_notebook_content(
        source_path.read_text(encoding="utf-8"),
        "ja",
        {"source_path": source_path},
    )

    rewritten_json = rewrite_notebook_paths(
        translated_json,
        source_path=source_path,
        target_path=target_path,
        policy={
            "language_code": "ja",
            "root_dir": ".",
            "translations_dir": "translations",
            "translated_images_dir": "translated_images",
            "translation_types": ["notebook", "images"],
        },
    )

    target_path.parent.mkdir(parents=True, exist_ok=True)
    target_path.write_text(rewritten_json, encoding="utf-8")


asyncio.run(main())
```

`translate_notebook_content`는 마크다운 셀을 번역하고 비마크다운 셀은 보존합니다. 경로 재작성은 마크다운 셀에만 적용됩니다.

### Image File

```python
from pathlib import Path

from co_op_translator.api import translate_image_content

source_path = Path("docs/images/hero.png")
target_path = Path("translated_images/fr/hero.png")

translated_image = translate_image_content(
    source_path,
    "fr",
    {
        "root_dir": ".",
        "fast_mode": False,
    },
)

target_path.parent.mkdir(parents=True, exist_ok=True)
translated_image.save(target_path)
```

`translate_image_content`는 소스 이미지를 읽고 렌더링된 `PIL.Image.Image`를 반환합니다. 번역된 이미지 메타데이터를 쓰지 않습니다.

## Scenario 2: Translate an Entire Repository

Python API가 `translate` CLI처럼 동작하도록 하려면 이 워크플로를 사용하세요. `run_translation`은 지원되는 파일을 검색하고, 선택된 콘텐츠 유형을 번역하며, 경로를 재작성하고, 출력 파일을 쓰고, 메타데이터를 업데이트하며, 정리와 같은 번역 유지 관리 작업을 수행합니다.

`run_translation`은 프로젝트 오케스트레이션을 위한 권장 진입점입니다. `translate_project`는 동일한 동작을 가지는 호환성 별칭으로 내보내집니다.

현재 리포지토리의 Markdown 파일을 한국어와 일본어로 번역:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    markdown=True,
)
```

특정 프로젝트 루트에서 노트북만 번역:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="fr",
    root_dir="./my-course",
    notebook=True,
)
```

파일을 쓰지 않고 번역량 미리보기:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="es de",
    root_dir="./my-course",
    markdown=True,
    dry_run=True,
)
```

한 호출에서 여러 콘텐츠 루트를 번역:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    root_dirs=["./docs", "./labs"],
)
```

명시적 출력 그룹에 번역을 작성:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ja",
    markdown=True,
    groups=[
        ("./course-a", "./localized/course-a"),
        ("./course-b", "./localized/course-b"),
    ],
)
```

각 언어가 중첩된 하위 디렉터리를 가져야 할 때 언어별 자리표시자 사용:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    groups=[
        ("./course", "./translations/<lang>/course"),
    ],
)
```

`markdown`, `notebook`, 또는 `images` 중 어느 것도 설정되지 않은 경우 API는 지원되는 모든 유형(마크다운, 노트북 및 이미지)을 번역합니다.

## Review Translated Output

`run_review`는 LLM 또는 Vision 자격 증명 없이 결정론적 번역 검사를 실행합니다.

!!! note "베타"
    `run_review`는 베타 결정론적 검토 API입니다. 모델 공급자를 호출하거나 파일을 쓰지 않지만 검사 및 이슈 스키마는 변경될 수 있습니다.

```python
from co_op_translator.api import run_review

run_review(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
)
```

기준 참조와 비교해 변경된 파일만 검토하고 GitHub 형식의 출력을 인쇄:

```python
from co_op_translator.api import run_review

run_review(
    language_codes="ko",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
    changed_from="origin/main",
    output_format="github",
)
```

## Copy-Paste API Examples

파일 쓰기 없이 Markdown 콘텐츠 번역:

```python
import asyncio

from co_op_translator.api import translate_markdown_content


async def main() -> None:
    translated = await translate_markdown_content(
        "# Hello\n\nWelcome to the course.",
        "ko",
    )
    print(translated)


asyncio.run(main())
```

Markdown 링크 번역 및 재작성:

```python
import asyncio

from co_op_translator.api import rewrite_markdown_paths, translate_markdown_content


async def main() -> None:
    translated = await translate_markdown_content(
        "[Setup](../setup.md)\n\n![Hero](../../images/hero.png)",
        "ko",
        {"source_path": "docs/guide.md"},
    )
    rewritten = rewrite_markdown_paths(
        translated,
        source_path="docs/guide.md",
        target_path="translations/ko/docs/guide.md",
        policy={
            "language_code": "ko",
            "root_dir": ".",
            "translations_dir": "translations",
            "translated_images_dir": "translated_images",
            "translation_types": ["markdown", "images"],
        },
    )
    print(rewritten)


asyncio.run(main())
```

Python에서 리포지토리 번역:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    root_dir="./course",
    markdown=True,
    yes=True,
)
```

여러 루트 번역:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    root_dirs=[
        "./docs",
        "./labs",
    ],
)
```

용어집 항목 보존:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="fr",
    markdown=True,
    glossaries=[
        "Co-op Translator",
        "Azure AI Foundry",
        "GitHub Actions",
    ],
)
```

## Public Entry Points

```python
from co_op_translator.api import (
    ImageTranslationOptions,
    MarkdownTranslationOptions,
    NotebookTranslationOptions,
    finish_markdown_agent_translation,
    finish_notebook_agent_translation,
    run_review,
    run_translation,
    rewrite_markdown_paths,
    rewrite_notebook_paths,
    start_markdown_agent_translation,
    start_notebook_agent_translation,
    translate_image_content,
    translate_markdown_content,
    translate_notebook_content,
    translate_project,
)
```

::: co_op_translator.api.translate_markdown_content

::: co_op_translator.api.translate_notebook_content

::: co_op_translator.api.translate_image_content

::: co_op_translator.api.start_markdown_agent_translation

::: co_op_translator.api.finish_markdown_agent_translation

::: co_op_translator.api.start_notebook_agent_translation

::: co_op_translator.api.finish_notebook_agent_translation

::: co_op_translator.api.rewrite_markdown_paths

::: co_op_translator.api.rewrite_notebook_paths

::: co_op_translator.api.MarkdownTranslationOptions

::: co_op_translator.api.NotebookTranslationOptions

::: co_op_translator.api.ImageTranslationOptions

::: co_op_translator.api.run_translation

::: co_op_translator.api.translate_project

::: co_op_translator.api.run_review

## Content Translation APIs

콘텐츠 번역 API는 편집기 확장, MCP 도구, 노트북 프로세서 또는 사용자 지정 파이프라인처럼 이미 메모리에 콘텐츠가 있는 통합을 위해 설계되었습니다.

| Function | Input | Output | File I/O | Notes |
| --- | --- | --- | --- | --- |
| `translate_markdown_content` | Markdown `str` | Markdown `str` | No | 비동기입니다. 마크다운 콘텐츠만 번역합니다. 링크를 재작성하거나 메타데이터를 쓰거나 면책 조항을 추가하지 않습니다. |
| `translate_notebook_content` | Notebook JSON `str` or `dict` | Notebook JSON `str` | No | 비동기입니다. 마크다운 셀을 번역하고 비마크다운 셀은 보존합니다. 링크를 재작성하거나 메타데이터를 쓰거나 면책 조항을 추가하지 않습니다. |
| `translate_image_content` | Image path | `PIL.Image.Image` | Reads source image only | 동기식입니다. 이미지 텍스트를 추출하고 번역한 다음 렌더된 이미지를 반환합니다. 번역된 이미지 메타데이터를 저장하지 않습니다. |

`translate_markdown_content` 및 `translate_notebook_content`는 옵션을 통해 선택적 `source_path`를 허용합니다. 경로는 번역기에 컨텍스트로 전달되며, 호출자는 번역 후 프로젝트별 경로 재작성에 대한 책임을 집니다.

```python
from co_op_translator.api import MarkdownTranslationOptions, translate_markdown_content

translated = await translate_markdown_content(
    document,
    "ko",
    MarkdownTranslationOptions(source_path="docs/guide.md"),
)
```

동일한 옵션을 사전으로 전달할 수도 있습니다:

```python
translated = await translate_markdown_content(
    document,
    "ko",
    {"source_path": "docs/guide.md"},
)
```

## Agent-Assisted Translation APIs

에이전트 지원 API는 Co-op Translator에서 Azure OpenAI 또는 OpenAI를 호출하지 않습니다. 이들은 호스트 에이전트가 번역할 수 있도록 마크다운 또는 노트북 청크를 준비하고, 번역된 청크로부터 최종 콘텐츠를 재구성합니다.

| Function | Purpose |
| --- | --- |
| `start_markdown_agent_translation` | 청크, 프롬프트 및 재구성 상태가 포함된 독립 실행형 마크다운 작업을 반환합니다. |
| `finish_markdown_agent_translation` | 작업과 호스트-에이전트가 번역한 청크로부터 마크다운을 재구성합니다. |
| `start_notebook_agent_translation` | 호스트-에이전트 번역용 마크다운 셀 청크가 포함된 노트북 작업을 반환합니다. |
| `finish_notebook_agent_translation` | 코드 셀, 출력 및 메타데이터를 보존하면서 노트북 JSON을 재구성합니다. |

이 워크플로는 주로 MCP 호스트를 위한 것입니다. Co-op Translator가 공급자 호출을 관리하는 프로덕션 리포지토리 번역이 필요하면 `translate_markdown_content`, `translate_notebook_content` 또는 `run_translation`을 사용하세요.

## Path Rewriting APIs

경로 재작성 API는 번역을 수행하지 않습니다. 소스 경로, 번역된 대상 경로 및 프로젝트 레이아웃을 호출자가 알게 된 후 링크 및 프런트매터 경로를 업데이트합니다.

| Function | Scope | Notes |
| --- | --- | --- |
| `rewrite_markdown_paths` | Markdown body and frontmatter | 번역된 대상에 대해 마크다운 링크와 지원되는 프런트매터 경로 필드를 재작성합니다. |
| `rewrite_notebook_paths` | Markdown cells in notebook JSON | 노트북의 각 마크다운 셀에 마크다운 경로 재작성을 적용하고 비마크다운 셀은 변경하지 않습니다. |

`policy` 인수는 다음 필드를 갖는 사전일 수 있습니다:

| Field | Required | Purpose |
| --- | --- | --- |
| `language_code` | Yes | 대상 언어 코드(예: `"ko"` 또는 `"pt-BR"`). |
| `root_dir` | No | 소스 프로젝트 루트입니다. 기본값은 `"."`입니다. |
| `translations_dir` | No | 텍스트 번역 출력 디렉터리입니다. 기본값은 `root_dir` 아래의 `translations`입니다. |
| `translated_images_dir` | No | 번역된 이미지 출력 디렉터리입니다. 기본값은 `root_dir` 아래의 `translated_images`입니다. |
| `translation_types` | No | 활성화된 번역 유형입니다. 기본값은 마크다운, 노트북 및 이미지입니다. |
| `lang_subdir` | No | 각 언어 폴더 아래의 선택적 하위 디렉터리입니다. |

## Project Translation Parameters

| Parameter | Type | Default | Purpose |
| --- | --- | --- | --- |
| `language_codes` | `str` | Required | 공백으로 구분된 대상 언어 코드(예: `"ko ja fr"` 또는 `"all"`). 별칭 코드는 정규화되어 표준 BCP 47 값으로 변환됩니다. |
| `root_dir` | `str` | `"."` | 단일 번역 대상의 프로젝트 루트입니다. `root_dirs` 또는 `groups`가 제공되면 무시됩니다. |
| `update` | `bool` | `False` | 선택된 언어에 대해 기존 번역을 삭제하고 재생성합니다. |
| `images` | `bool` | `False` | 이미지 번역을 포함합니다. Azure AI Vision 구성이 필요합니다. |
| `markdown` | `bool` | `False` | 마크다운 번역을 포함합니다. |
| `notebook` | `bool` | `False` | Jupyter 노트북 번역을 포함합니다. |
| `debug` | `bool` | `False` | 디버그 로깅을 활성화합니다. |
| `save_logs` | `bool` | `False` | 루트 `logs/` 디렉터리 아래에 DEBUG 수준 로그 파일을 저장합니다. |
| `yes` | `bool` | `True` | 프로그래밍 및 CI 사용을 위한 자동 확인을 수행합니다. |
| `add_disclaimer` | `bool` | `False` | 번역된 마크다운과 노트북에 기계 번역 면책 조항을 추가합니다. |
| `translations_dir` | `str \| None` | `None` | 사용자 지정 텍스트 번역 출력 디렉터리입니다. 상대 경로는 각 루트에 대해 해결됩니다. |
| `image_dir` | `str \| None` | `None` | 사용자 지정 번역된 이미지 출력 디렉터리입니다. 상대 경로는 각 루트에 대해 해결됩니다. |
| `root_dirs` | `Iterable[str] \| None` | `None` | 동일한 출력 설정을 공유하는 여러 루트입니다. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | 명시적 `(root_dir, translations_dir)` 쌍입니다. `root_dirs`보다 우선합니다. |
| `repo_url` | `str \| None` | `None` | README 언어 표 안내를 렌더링할 때 사용되는 리포지토리 URL입니다. |
| `glossaries` | `Iterable[str] \| None` | `None` | 번역 중 보존할 용어집 항목들입니다. 중복 및 빈 항목은 정규화됩니다. |
| `dry_run` | `bool` | `False` | 파일을 쓰지 않고 번역량을 추정하고 마이그레이션 동작을 미리봅니다. |

## Review Parameters

`run_review`는 가능한 한 `run_translation` 서명을 의도적으로 반영하여 자동화가 번역 및 검토 워크플로 간에 최소한의 분기로 전환할 수 있게 합니다.

| Parameter | Type | Default | Purpose |
| --- | --- | --- | --- |
| `language_codes` | `str \| Iterable[str]` | `"all"` | 검토할 대상 언어 폴더입니다. 공백으로 구분된 문자열과 이터러블을 허용합니다. `"all"`은 발견된 모든 번역 언어를 검토합니다. |
| `root_dir` | `str` | `"."` | 단일 검토 대상의 프로젝트 루트입니다. `root_dirs` 또는 `groups`가 제공되면 무시됩니다. |
| `markdown` | `bool` | `False` | 마크다운 및 MDX 소스 파일을 포함합니다. |
| `notebook` | `bool` | `False` | Jupyter 노트북 소스 파일을 포함합니다. |
| `images` | `bool` | `False` | 번역 옵션과의 대응을 위해 예약되어 있습니다. 이미지에 대한 링크 참조는 마크다운에서 확인됩니다. |
| `translations_dir` | `str \| None` | `None` | 사용자 지정 텍스트 번역 출력 디렉터리. 상대 경로는 각 루트를 기준으로 해석됩니다. |
| `root_dirs` | `Iterable[str] \| None` | `None` | 동일한 출력 설정을 공유하는 여러 루트입니다. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | 명시적인 `(root_dir, translations_dir)` 쌍입니다. `root_dirs`보다 우선합니다. |
| `changed_from` | `str \| None` | `None` | 검토를 변경된 소스 파일로 제한하는 데 사용되는 Git 참조(ref)입니다. |
| `output_format` | `str` | `"text"` | 검토 출력 형식입니다. 지원되는 값은 `"text"` 및 `"github"`입니다. |
| `fail_on_warnings` | `bool` | `False` | 경고를 오류와 마찬가지로 실패로 처리합니다. |
| `debug` | `bool` | `False` | 디버그 로깅을 활성화합니다. |
| `save_logs` | `bool` | `False` | 루트의 `logs/` 디렉터리 아래에 DEBUG 수준의 로그 파일을 저장합니다. |

If none of `markdown`, `notebook`, or `images` are set, the API reviews Markdown, notebooks, and image link references where applicable. Review does not call an LLM provider and does not require API keys.

## 구성 요구 사항

프로바이더 기반 번역 API는 번역 전에 프로바이더 구성이 필요합니다:

- Markdown 및 노트북 번역에는 LLM 제공자가 필요합니다. Azure OpenAI 또는 OpenAI 중 하나를 구성하세요.
- 이미지 번역은 LLM 제공자 외에 Azure AI Vision이 필요합니다.
- `run_translation`은 프로젝트 번역이 시작되기 전에 경량 연결 검사를 실행합니다.
- 에이전트 지원 `start_*_agent_translation` 및 `finish_*_agent_translation` API는 Co-op Translator LLM 제공자를 호출하지 않습니다. 호스트 애플리케이션 또는 MCP 에이전트가 준비된 청크를 번역합니다.
- `rewrite_markdown_paths`, `rewrite_notebook_paths`, 및 `run_review`는 결정론적이며 제공자 자격 증명이 필요하지 않습니다.

Required Azure OpenAI variables:

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

필수 OpenAI 변수:

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

이미지 번역을 위한 필수 Azure AI Vision 변수:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

`run_review`는 결정론적이며 Azure OpenAI, OpenAI, 또는 Azure AI Vision 구성이 필요하지 않습니다.

## 동작 참고사항

- 콘텐츠 번역 API는 번역을 프로젝트 경로 재작성과 별도로 유지합니다. 번역된 콘텐츠에서 대상 위치에 맞게 프로젝트 상대 링크를 조정해야 하는 경우 `rewrite_markdown_paths` 또는 `rewrite_notebook_paths`를 명시적으로 호출하세요.
- 프로젝트 오케스트레이션 API는 파일 검색, 쓰기, 경로 재작성, 메타데이터, 정리 및 선택적 고지 사항을 포함하여 콘텐츠 번역 주변의 프로젝트 동작을 추가합니다.
- `run_translation`은 CLI 사용자 경험과 일치하도록 Click을 통해 진행 상황 및 추정 요약을 출력합니다.
- `dry_run=True`는 가상 README 업데이트를 사용하여 추정을 계산하지만 README나 번역 파일을 작성하지 않습니다.
- `groups`는 순차적으로 처리됩니다. 작업이 시작되기 전에 단일 집계 추정치가 출력됩니다.
- 이미지 번역이 선택된 경우, Vision 구성이 누락되면 번역 시작 전에 오류가 발생합니다.
- 기존 별칭 기반 언어 폴더는 감지되며 실행의 일부로 표준 언어 폴더 이름으로 마이그레이션될 수 있습니다.
- `run_review`는 번역된 파일 누락, 누락되었거나 오래된 번역 메타데이터, 잘못된 Markdown 프론트매터/코드 펜스, 및 유효하지 않은 번역된 노트북 JSON에서 실패합니다.
- `run_review`는 기본적으로 누락된 로컬 Markdown 및 이미지 링크 대상들을 경고로 보고합니다.

## 내부 호출 경로

API는 CLI에서 사용되는 동일한 코어 구현에 위임합니다:

번역:

1. `co_op_translator.api.translation.translate_markdown_content`, `translate_notebook_content`, or `translate_image_content` 메모리 내 번역을 위해.
2. `co_op_translator.api.translation.rewrite_markdown_paths` 또는 `rewrite_notebook_paths` 명시적 경로 후처리를 위해.
3. `co_op_translator.api.translation.run_translation` 전체 프로젝트 오케스트레이션을 위해.
4. `co_op_translator.config.Config`, `LLMConfig`, 및 `VisionConfig`.
5. `co_op_translator.core.project.ProjectTranslator`.
6. `co_op_translator.core.project.TranslationManager`.
7. Markdown, 노트북 및 이미지용 집중된 프로젝트 번역 믹스인.
8. `co_op_translator.core` 아래의 Markdown, 노트북, 텍스트 및 이미지 번역기.

검토:

1. `co_op_translator.api.review.run_review`
2. `co_op_translator.review.targets.build_review_targets`
3. `co_op_translator.review.runner.ReviewRunner`
4. `co_op_translator.review.checks` 아래의 결정론적 검사들

The following classes are useful for maintainers, but are not exported as the package-level stable API.

| 클래스 | 모듈 | 책임 |
| --- | --- | --- |
| `ProjectTranslator` | `co_op_translator.core.project.project_translator` | 프로젝트 수준 번역 조정, 디렉터리 관리, 언어별 메타데이터 정규화, 및 Markdown, 노트북, 이미지 번역기들에 대한 위임을 담당합니다. |
| `TranslationManager` | `co_op_translator.core.project.translation` | Markdown, 노트북, 이미지 처리, 오래된 항목 감지, 및 번역 메타데이터 업데이트를 위한 비동기 파일 처리 작업을 수행합니다. |
| `ProjectMarkdownTranslationMixin` | `co_op_translator.core.project.translation.project_markdown_translation` | Markdown 파일 읽기, 콘텐츠 번역, 경로 재작성, 메타데이터, 고지사항, 및 쓰기를 조율합니다. |
| `ProjectNotebookTranslationMixin` | `co_op_translator.core.project.translation.project_notebook_translation` | 노트북 파일 읽기, Markdown 셀 번역, 경로 재작성, 메타데이터, 고지사항, 및 쓰기를 조율합니다. |
| `ProjectImageTranslationMixin` | `co_op_translator.core.project.translation.project_image_translation` | 소스 이미지 검색, 이미지 번역, 출력 경로, 메타데이터, 및 쓰기를 조율합니다. |
| `ProjectEvaluator` | `co_op_translator.core.project.project_evaluator` | 번역된 Markdown 쌍을 찾고, 번역 품질을 평가하며, 낮은 신뢰도의 복구 워크플로를 위한 신뢰도 메타데이터를 읽습니다. |
| `ReviewRunner` | `co_op_translator.review.runner` | 소스 파일, 대상 언어 및 구성된 번역 루트 전반에 걸친 결정론적 검토 검사를 조정합니다. |
| `ReviewTarget` | `co_op_translator.review.targets` | 해당 루트에 대해 검토되는 소스 루트와 번역 출력 디렉터리를 설명합니다. |
| `LanguageFolderMigrator` | `co_op_translator.core.project.language_migrator` | 레거시 별칭 언어 폴더를 감지하고 정식 BCP 47 폴더 마이그레이션 계획을 준비합니다. |
| `Config` | `co_op_translator.config.base_config` | `.env` 파일을 로드하고 필수 LLM 및 선택적 Vision 제공자가 구성되어 있는지 확인합니다. |
| `LLMConfig` | `co_op_translator.config.llm_config.config` | Azure OpenAI 또는 OpenAI를 자동 감지하고, 필요한 환경 변수를 검증하며, 제공자 연결 검사를 실행합니다. |
| `VisionConfig` | `co_op_translator.config.vision_config.config` | Azure AI Vision 구성을 감지하고 이미지 번역을 위한 연결 검사를 실행합니다. |