# Python API

안정적인 공개 Python API는 `co_op_translator.api`에서 내보내집니다. 대부분의 통합은 다음 워크플로 중 하나를 사용합니다:

| 시나리오 | 사용 시 | 주요 API |
| --- | --- | --- |
| 개별 파일 또는 문서를 번역 | 애플리케이션이 소스 콘텐츠를 읽고, Co-op Translator에 번역을 요청하며, 결과를 저장할 위치를 결정합니다. | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| 호스트 에이전트 번역을 위해 콘텐츠 준비 | MCP 호스트나 애플리케이션 모델이 청크를 번역하고, Co-op Translator는 청크 분할 및 재구성을 처리합니다. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| 전체 리포지토리 번역 | Python API가 CLI처럼 동작하며 파일 검색, 출력 경로, 메타데이터, 정리 및 쓰기 작업을 처리하기를 원할 때. | `run_translation` |

`core`, `config`, `review`, `utils` 아래의 대부분의 저수준 모듈은 이러한 API 진입점에서 사용하는 구현 세부사항입니다.

MCP 클라이언트는 [MCP 서버](mcp.md)를 통해 동일한 공개 API를 사용합니다. Python을 직접 호출할 때는 이 페이지를 사용하고, Co-op Translator를 에이전트나 에디터에 노출할 때는 MCP 가이드를 사용하세요. CLI, Python API, MCP 중에서 결정해야 한다면 [워크플로 선택](workflows.md)에서 시작하세요.

## 처음 사용하는 API 흐름

Python 코드에서 Co-op Translator를 호출하는 경우 여기를 시작하세요:

1. 호스트 에이전트 번역을 위해 Markdown 또는 노트북 청크만 준비하는 경우가 아니라면 [Configuration](configuration.md)에 설명된 대로 LLM 제공자를 구성하세요.
2. 애플리케이션이 파일 입출력을 직접 관리할지 결정하세요.
3. 애플리케이션이 개별 파일을 읽고 쓸 경우 콘텐츠 API를 사용하세요.
4. Co-op Translator가 CLI처럼 리포지토리를 처리해야 하는 경우 `run_translation`을 사용하세요.
5. 자동화에서 결정적 검사가 필요하면 번역 후 `run_review`를 사용하세요.

| 목표 | 시작할 API |
| --- | --- |
| Markdown 문자열 또는 파일 하나 번역 | `translate_markdown_content` |
| 노트북 페이로드 하나 번역 | `translate_notebook_content` |
| 이미지 하나 번역 | `translate_image_content` |
| 호스트 에이전트에게 Markdown 또는 노트북 청크 번역을 맡기기 | `start_markdown_agent_translation` 또는 `start_notebook_agent_translation` |
| 출력 경로 선택 후 번역된 링크 재작성 | `rewrite_markdown_paths` 또는 `rewrite_notebook_paths` |
| 전체 리포지토리 번역 | `run_translation` |
| 번역된 출력 검토 | `run_review` |

## 시나리오 1: 개별 파일 또는 문서 번역

파일, 에디터 버퍼, 노트북 페이로드, MCP 요청 또는 사용자 지정 파이프라인 입력이 이미 있고 애플리케이션 코드가 파일 입출력을 관리하는 경우 이 워크플로를 사용하세요:

1. 소스 콘텐츠를 읽습니다.
2. 콘텐츠 번역 API를 호출합니다.
3. 번역된 콘텐츠를 프로젝트 번역 폴더에 기록할 경우 선택적으로 경로 재작성 API를 호출합니다.
4. 애플리케이션에서 결과를 저장하거나 반환합니다.

콘텐츠 번역 API는 프로젝트 검색을 수행하지 않으며, 메타데이터를 쓰지 않으며, 면책 조항을 추가하지 않으며, 링크를 자동으로 재작성하지 않습니다.

### Markdown 파일

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

번역된 Markdown이 Co-op Translator 프로젝트 레이아웃에 속하지 않을 경우 `rewrite_markdown_paths`를 건너뛰고 번역된 문자열을 직접 저장하세요.

### 노트북 파일

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

`translate_notebook_content`는 Markdown 셀을 번역하고 비-Markdown 셀은 보존합니다. 경로 재작성은 Markdown 셀에만 적용됩니다.

### 이미지 파일

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

`translate_image_content`는 소스 이미지를 읽어 렌더된 `PIL.Image.Image`를 반환합니다. 번역된 이미지 메타데이터는 쓰지 않습니다.

## 시나리오 2: 전체 리포지토리 번역

Python API가 `translate` CLI처럼 동작하기를 원할 때 이 워크플로를 사용하세요. `run_translation`은 지원되는 파일을 검색하고, 선택된 콘텐츠 유형을 번역하며, 경로를 재작성하고, 출력 파일을 기록하고, 메타데이터를 업데이트하며, 정리와 같은 번역 유지 관리 작업을 수행합니다.

`run_translation`은 권장되는 프로젝트 오케스트레이션 진입점입니다. `translate_project`는 동일한 동작을 하는 호환성 별칭으로 내보내집니다.

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

통합을 위한 구조화된 진행 이벤트 기록:

```python
from co_op_translator.api import TranslationEvent, run_translation


def on_event(event: TranslationEvent) -> None:
    payload = event.to_dict()
    # 페이로드를 작업 이벤트 테이블에 저장하거나 UI로 스트리밍하세요.


run_translation(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
    progress_callback=on_event,
)
```

이벤트는 버전된 스키마 `co-op.translation.event.v1`을 사용합니다. 통합은
`type` 및 `stage_key`와 같은 안정적인 필드에 의존해야 하며, 사용자에게 표시되는
콘솔 텍스트나 `stage_label`에 의존해서는 안 됩니다.

여러 콘텐츠 루트를 한 번에 번역:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    root_dirs=["./docs", "./labs"],
)
```

번역을 명시적 출력 그룹에 기록:

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

언어별로 중첩된 하위 디렉터리가 필요한 경우 언어별 플레이스홀더를 사용하세요:

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

`markdown`, `notebook`, `images` 중 어느 것도 설정되지 않으면 API는 Markdown, 노트북, 이미지 등 지원되는 모든 유형을 번역합니다.

### 번역 상태 제공자로 승인된 사람의 편집 보존

기본적으로 Co-op Translator는 기존의 파일 단위 동작을 유지합니다:
Markdown 소스가 오래된 경우 전체 번역 파일이 재생성됩니다. 호스팅된
통합은 선택적으로 `TranslationStateProvider`를 전달하여 사람의
변경되지 않은 소스 블록에 대한 편집을 보존할 수 있습니다.

제공자는 마지막으로 승인된 소스/대상 쌍을 제공하고 각 새로운
후보를 기록합니다. 승인 여부는 통합의 책임으로 남아 있습니다—예를 들어,
번역 풀 리퀘스트가 병합된 후:

```python
from pathlib import Path

from co_op_translator.api import (
    TranslationBaseline,
    TranslationUpdate,
    run_translation,
)


class DatabaseTranslationState:
    def load_baseline(
        self,
        *,
        source_path: Path,
        translation_path: Path,
        language_code: str,
    ) -> TranslationBaseline | None:
        row = load_accepted_translation(
            source_path=source_path,
            translation_path=translation_path,
            language_code=language_code,
        )
        if row is None:
            return None
        return TranslationBaseline(
            source_text=row.source_text,
            target_text=row.target_text,
            revision=row.accepted_revision,
        )

    def record_candidate(
        self,
        *,
        source_path: Path,
        translation_path: Path,
        language_code: str,
        source_text: str,
        target_text: str,
        update: TranslationUpdate,
    ) -> None:
        save_translation_candidate(
            source_path=source_path,
            translation_path=translation_path,
            language_code=language_code,
            source_text=source_text,
            target_text=target_text,
            mode=update.mode,
            fallback_reason=update.fallback_reason,
        )


run_translation(
    language_codes="ko",
    root_dir="./course",
    markdown=True,
    translation_state_provider=DatabaseTranslationState(),
)
```

유효한 승인 기준선이 있는 Markdown 파일의 경우 Co-op Translator는
최상위 Markdown 블록을 정렬합니다. 변경되지 않은 소스 블록은 현재 번역된
블록(사람이 수행한 편집 포함)을 재사용합니다; 변경되었거나 추가된 소스 블록은 번역을 위해 전송됩니다
번역됩니다; 삭제된 소스 블록은 제거됩니다. 정렬이 애매하거나
대상 구조가 변경되었거나 블록 번역이 유효하지 않거나 기준선이
없을 경우 Co-op Translator는 안전하게 기존의 전체 파일 번역 방식으로 대체합니다.


세그먼트 번역 메모리를 저장하지 않습니다. 현재는 Markdown 프로젝트
번역에 적용됩니다. 노트북 및 이미지 동작은 변경되지 않습니다. `update=True`를 전달하면
전체 재생성을 요청하게 됩니다.


프로젝트 워크플로가 종료된 후 `RuntimeError`를 발생시키며,
누락된 출력과 함께 성공한 실행으로 보고하지 않습니다. 통합은 이를 실패한
작업으로 처리하고 이전에 승인된 번역 상태를 유지해야 합니다.


## 번역된 출력 검토

`run_review`는 LLM이나 Vision 자격 증명 없이 결정론적 번역 검사를 수행합니다.

!!! note "Beta"
    `run_review`는 베타 버전의 결정론적 리뷰 API입니다. 모델 제공자를 호출하거나 파일을 쓰지 않지만, 검사 및 이슈 스키마는 변경될 수 있습니다.

```python
from co_op_translator.api import run_review

run_review(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
)
```

README만 번역한 후에는 동일한 범위로 검토를 실행하세요:

```python
run_review(language_codes="ko", root_dir="./my-course", readme_only=True)
```

`readme_only=True`는 각 구성된 소스 루트 아래의 `README.md`만 검토합니다,
커스텀 `groups` 및 출력 디렉터리를 포함합니다. 다른 문서 및 중첩된
README는 제외됩니다. 소스 README가 없으면 `ValueError`가 발생하며; 실패한
번역 검사 실패는 `RuntimeError`를 발생시킵니다.

기준 ref와 비교해 변경된 파일만 검토하고 GitHub 형식의 출력을 출력:

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

## 복사-붙여넣기용 API 예제

파일 기록 없이 Markdown 콘텐츠 번역:

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
        "[Setup](../setup.md)\n\n![Hero](images/hero.png)",
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

용어집 용어 보존:

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

## 공개 진입점

```python
from co_op_translator.api import (
    ImageTranslationOptions,
    MarkdownTranslationOptions,
    NotebookTranslationOptions,
    TranslationBaseline,
    TranslationStateProvider,
    TranslationUpdate,
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

::: co_op_translator.api.TranslationBaseline

::: co_op_translator.api.TranslationStateProvider

::: co_op_translator.api.TranslationUpdate

::: co_op_translator.api.run_translation

::: co_op_translator.api.translate_project

::: co_op_translator.api.run_review

## 콘텐츠 번역 API

콘텐츠 번역 API는 에디터 확장, MCP 도구, 노트북 프로세서 또는 사용자 지정 파이프라인처럼 이미 메모리에 콘텐츠가 있는 통합을 위한 것입니다.

| 함수 | 입력 | 출력 | 파일 입출력 | 참고 |
| --- | --- | --- | --- | --- |
| `translate_markdown_content` | Markdown `str` | Markdown `str` | 아니요 | 비동기. Markdown 콘텐츠만 번역합니다. 링크 재작성, 메타데이터 기록, 면책 조항 추가는 수행하지 않습니다. |
| `translate_notebook_content` | Notebook JSON `str` or `dict` | Notebook JSON `str` | 아니요 | 비동기. Markdown 셀을 번역하고 비-Markdown 셀은 보존합니다. 링크 재작성, 메타데이터 기록, 면책 조항 추가는 수행하지 않습니다. |
| `translate_image_content` | 이미지 경로 | `PIL.Image.Image` | 소스 이미지만 읽음 | 동기식. 이미지 텍스트를 추출하고 번역한 다음 렌더된 이미지를 반환합니다. 번역된 이미지 메타데이터는 저장하지 않습니다. |

`translate_markdown_content`와 `translate_notebook_content`는 옵션을 통해 선택적 `source_path`를 허용합니다. 해당 경로는 번역기에 컨텍스트로 전달되며, 호출자는 번역 후 프로젝트 특정 경로 재작성에 대해 책임이 있습니다.

```python
from co_op_translator.api import MarkdownTranslationOptions, translate_markdown_content

translated = await translate_markdown_content(
    document,
    "ko",
    MarkdownTranslationOptions(source_path="docs/guide.md"),
)
```

동일한 옵션을 딕셔너리로 전달할 수도 있습니다:

```python
translated = await translate_markdown_content(
    document,
    "ko",
    {"source_path": "docs/guide.md"},
)
```

## 에이전트 지원 번역 API

에이전트 지원 API는 Co-op Translator에서 구성된 LLM 제공자를 호출하지 않습니다. 이들 API는 호스트 에이전트가 번역할 수 있도록 Markdown 또는 노트북 청크를 준비한 다음, 번역된 청크로부터 최종 콘텐츠를 재구성합니다.

| 함수 | 목적 |
| --- | --- |
| `start_markdown_agent_translation` | 청크, 프롬프트 및 재구성 상태가 포함된 자체 포함형 Markdown 작업을 반환합니다. |
| `finish_markdown_agent_translation` | 작업과 호스트 에이전트가 번역한 청크로부터 Markdown을 재구성합니다. |
| `start_notebook_agent_translation` | 호스트 에이전트 번역을 위한 Markdown 셀 청크가 포함된 노트북 작업을 반환합니다. |
| `finish_notebook_agent_translation` | 코드 셀, 출력 및 메타데이터를 보존하면서 노트북 JSON을 재구성합니다. |

이 워크플로는 주로 MCP 호스트를 위한 것입니다. Co-op Translator가 제공자 호출을 관리하는 프로덕션 리포지토리 번역이 필요하면 `translate_markdown_content`, `translate_notebook_content`, 또는 `run_translation`을 사용하세요.

## 경로 재작성 API

경로 재작성 API는 번역을 수행하지 않습니다. 호출자가 소스 경로, 번역된 대상 경로 및 프로젝트 레이아웃을 알게 된 후 링크와 frontmatter 경로를 업데이트합니다.

| 함수 | 범위 | 참고 |
| --- | --- | --- |
| `rewrite_markdown_paths` | Markdown 본문 및 frontmatter | 번역된 대상에 대해 Markdown 링크와 지원되는 frontmatter 경로 필드를 재작성합니다. |
| `rewrite_notebook_paths` | 노트북 JSON의 Markdown 셀 | 각 Markdown 셀에 Markdown 경로 재작성을 적용하고 비-Markdown 셀은 그대로 둡니다. |

`policy` 인수는 다음 필드를 가진 딕셔너리일 수 있습니다:

| 필드 | 필수 | 용도 |
| --- | --- | --- |
| `language_code` | 예 | 대상 언어 코드 (예: `"ko"` 또는 `"pt-BR"`). |
| `root_dir` | 아니요 | 소스 프로젝트 루트. 기본값은 `"."`입니다. |
| `translations_dir` | 아니요 | 텍스트 번역 출력 디렉터리. 기본값은 `root_dir` 아래의 `translations`입니다. |
| `translated_images_dir` | 아니요 | 번역된 이미지 출력 디렉터리. 기본값은 `root_dir` 아래의 `translated_images`입니다. |
| `translation_types` | 아니요 | 활성화된 번역 유형. 기본값은 Markdown, 노트북, 이미지입니다. |
| `lang_subdir` | 아니요 | 각 언어 폴더 아래의 선택적 하위 디렉터리입니다. |

## 프로젝트 번역 매개변수

| 매개변수 | 유형 | 기본값 | 용도 |
| --- | --- | --- | --- |
| `language_codes` | `str` | 필수 | 공백으로 구분된 대상 언어 코드(예: `"ko ja fr"` 또는 `"all"`). 별칭 코드는 표준 BCP 47 값으로 정규화됩니다. |
| `root_dir` | `str` | `"."` | 단일 번역 대상의 프로젝트 루트입니다. `root_dirs` 또는 `groups`가 제공되면 무시됩니다. |
| `update` | `bool` | `False` | 선택된 언어에 대해 기존 번역을 삭제하고 재생성합니다. |
| `images` | `bool` | `False` | 이미지 번역 포함. Azure AI Vision 구성이 필요합니다. |
| `markdown` | `bool` | `False` | Markdown 번역 포함. |
| `notebook` | `bool` | `False` | Jupyter 노트북 번역 포함. |
| `debug` | `bool` | `False` | 디버그 로깅 활성화. |
| `save_logs` | `bool` | `False` | 루트 `logs/` 디렉터리에 DEBUG 수준 로그 파일 저장. |
| `yes` | `bool` | `True` | 프로그램 및 CI 사용을 위해 프롬프트를 자동으로 확인합니다. |
| `add_disclaimer` | `bool` | `False` | 번역된 Markdown 및 노트북에 기계 번역 고지문을 추가합니다. |
| `translations_dir` | `str \| None` | `None` | 사용자 지정 텍스트 번역 출력 디렉터리입니다. 상대 경로는 각 루트에 대해 해석됩니다. |
| `image_dir` | `str \| None` | `None` | 번역된 이미지 출력 디렉터리를 사용자 지정합니다. 상대 경로는 각 루트에 대해 해석됩니다. |
| `root_dirs` | `Iterable[str] \| None` | `None` | 동일한 출력 설정을 공유하는 여러 루트입니다. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | 명시적인 `(root_dir, translations_dir)` 쌍입니다. `root_dirs`보다 우선합니다. |
| `repo_url` | `str \| None` | `None` | README 언어 표 안내를 렌더링할 때 사용되는 리포지토리 URL입니다. |
| `glossaries` | `Iterable[str] \| None` | `None` | 번역 중 보존할 용어집 용어입니다. 중복 및 빈 용어는 정규화됩니다. |
| `dry_run` | `bool` | `False` | 파일을 쓰지 않고 번역량을 추정하고 마이그레이션 동작을 미리 봅니다. |
| `translation_state_provider` | `TranslationStateProvider \| None` | `None` | 증분 Markdown 업데이트를 위한 선택적 수락-기준 및 후보 지속성 어댑터입니다. 이를 생략하면 기존 전체 파일 동작이 유지됩니다. |

## 검토 매개변수

`run_review`는 가능한 경우 `run_translation` 서명을 의도적으로 반영하여 자동화가 최소한의 분기로 번역 및 검토 워크플로 간 전환할 수 있게 합니다.

| 매개변수 | 유형 | 기본값 | 용도 |
| --- | --- | --- | --- |
| `language_codes` | `str \| Iterable[str]` | `"all"` | 검토할 대상 언어 폴더입니다. 공백으로 구분된 문자열과 반복 가능한 객체가 허용됩니다. `"all"`은 발견된 모든 번역 언어를 검토합니다. |
| `root_dir` | `str` | `"."` | 단일 검토 대상의 프로젝트 루트입니다. `root_dirs` 또는 `groups`가 제공되면 무시됩니다. |
| `markdown` | `bool` | `False` | Markdown 및 MDX 소스 파일을 포함합니다. |
| `notebook` | `bool` | `False` | Jupyter 노트북 소스 파일을 포함합니다. |
| `images` | `bool` | `False` | 번역 옵션과의 대응을 위해 예약되어 있습니다. 이미지에 대한 링크 참조는 Markdown에서 확인됩니다. |
| `translations_dir` | `str \| None` | `None` | 사용자 지정 텍스트 번역 출력 디렉터리입니다. 상대 경로는 각 루트에 대해 해석됩니다. |
| `root_dirs` | `Iterable[str] \| None` | `None` | 동일한 출력 설정을 공유하는 여러 루트입니다. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | 명시적인 `(root_dir, translations_dir)` 쌍입니다. `root_dirs`보다 우선합니다. |
| `changed_from` | `str \| None` | `None` | 검토를 변경된 소스 파일로 제한하는 데 사용되는 Git 참조입니다. |
| `readme_only` | `bool` | `False` | 각 소스 루트 아래의 `README.md`만 검토합니다. 소스 README가 없으면 `ValueError`를 발생시킵니다. |
| `output_format` | `str` | `"text"` | 검토 출력 형식입니다. 지원되는 값은 `"text"`와 `"github"`입니다. |
| `fail_on_warnings` | `bool` | `False` | 경고를 오류와 함께 실패로 간주합니다. |
| `debug` | `bool` | `False` | 디버그 로깅을 활성화합니다. |
| `save_logs` | `bool` | `False` | `logs/` 루트 디렉터리 아래에 DEBUG 레벨 로그 파일을 저장합니다. |

`markdown`, `notebook`, `images` 중 어느 것도 설정되지 않은 경우, API는 해당되는 경우 Markdown, 노트북 및 이미지 링크 참조를 검토합니다. Review는 LLM 제공자를 호출하지 않으며 API 키가 필요하지 않습니다.

## 구성 요구사항

제공자 지원 번역 API는 번역하기 전에 제공자 구성이 필요합니다:

- Markdown 및 노트북 번역에는 LLM 공급자가 필요합니다. Azure OpenAI, OpenAI 또는 Anthropic을 구성하세요.
- 이미지 번역은 LLM 제공자에 더해 Azure AI Vision이 필요합니다.
- `run_translation`는 프로젝트 번역이 시작되기 전에 가벼운 연결 확인을 수행합니다.
- 에이전트 지원 `start_*_agent_translation` 및 `finish_*_agent_translation` API는 Co-op Translator LLM 제공자를 호출하지 않습니다. 호스트 애플리케이션 또는 MCP 에이전트가 준비된 청크를 번역합니다.
- `rewrite_markdown_paths`, `rewrite_notebook_paths`, 및 `run_review`은 결정론적이며 공급자 자격증명을 필요로 하지 않습니다.

필수 Azure OpenAI 변수:

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

필수 Anthropic 변수:

```bash
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

`ANTHROPIC_BASE_URL` 및 `ANTHROPIC_MAX_TOKENS`는 선택 사항입니다. Microsoft Agent Framework는 Co-op Translator 0.22.0부터 모든 제공자에 대한 기본 모델 클라이언트입니다. Semantic Kernel은 여전히 `CO_OP_TRANSLATOR_MODEL_CLIENT="semantic-kernel"`로 일시적으로 선택할 수 있지만, 그렇게 하면 사용 중단 경고가 발생합니다; 단계적 제거 계획은 [구성](configuration.md#model-client-backend)을 참조하세요.

이미지 번역을 위한 필수 Azure AI Vision 변수:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

`run_review`는 결정론적이며 LLM 또는 Azure AI Vision 구성이 필요하지 않습니다.

## 동작 참고사항

- 콘텐츠 번역 API는 번역을 프로젝트 경로 재작성과 분리합니다. 번역된 콘텐츠의 프로젝트 상대 링크를 대상 위치에 맞게 조정해야 할 때는 `rewrite_markdown_paths` 또는 `rewrite_notebook_paths`를 명시적으로 호출하세요.
- 프로젝트 오케스트레이션 API는 파일 검색, 쓰기, 경로 재작성, 메타데이터, 정리 및 선택적 고지문 등 콘텐츠 번역 주변의 프로젝트 동작을 추가합니다.
- `run_translation`은 CLI에서 사용하는 동일한 Rich 기반 리포터를 통해 진행률 및 추정 요약을 출력합니다. 비대화형 출력은 일반 텍스트로 대체됩니다.
- `dry_run=True`는 가상 README 업데이트를 사용해 추정치를 계산하지만 README 또는 번역 파일을 쓰지 않습니다.
- `groups`는 순차적으로 처리됩니다. 작업이 시작되기 전에 하나의 총괄 추정치가 출력됩니다.
- 이미지 번역이 선택되면, Vision 구성이 없을 경우 번역 시작 전에 오류가 발생합니다.
- 기존 별칭 기반 언어 폴더가 감지되며 실행의 일환으로 정식 언어 폴더 이름으로 마이그레이션할 수 있습니다.
- `run_review`는 번역된 파일 누락, 누락되었거나 오래된 번역 메타데이터, 잘못된 Markdown frontmatter/코드 펜스, 및 잘못된 번역된 노트북 JSON에서 실패합니다.
- `run_review`는 기본적으로 로컬 Markdown 및 이미지 링크 대상의 누락을 경고로 보고합니다.

## 내부 호출 경로

API는 CLI에서 사용되는 동일한 핵심 구현에 위임합니다:

번역:

1. `co_op_translator.api.translation.translate_markdown_content`, `translate_notebook_content`, or `translate_image_content` for in-memory translation.
2. `co_op_translator.api.translation.rewrite_markdown_paths` or `rewrite_notebook_paths` for explicit path post-processing.
3. `co_op_translator.api.translation.run_translation` for full project orchestration.
4. `co_op_translator.config.Config`, `LLMConfig`, 및 `VisionConfig`.
5. `co_op_translator.core.project.ProjectTranslator`.
6. `co_op_translator.core.project.TranslationManager`.
7. Markdown, 노트북 및 이미지에 대한 집중된 프로젝트 번역 믹스인.
8. `co_op_translator.core` 아래의 Markdown, 노트북, 텍스트 및 이미지 번역기.

검토:

1. `co_op_translator.api.review.run_review`
2. `co_op_translator.review.targets.build_review_targets`
3. `co_op_translator.review.runner.ReviewRunner`
4. `co_op_translator.review.checks` 아래의 결정론적 검사

다음 클래스들은 유지관리자에게 유용하지만 패키지 수준의 안정된 API로 노출되지 않습니다.

| 클래스 | 모듈 | 책임 |
| --- | --- | --- |
| `ProjectTranslator` | `co_op_translator.core.project.project_translator` | 프로젝트 수준의 번역, 디렉터리 관리, 언어별 메타데이터 정규화 및 Markdown, 노트북, 이미지 번역기로의 위임을 조정합니다. |
| `TranslationManager` | `co_op_translator.core.project.translation` | Markdown, 노트북, 이미지, 오래된 항목 감지 및 번역 메타데이터 업데이트에 대한 비동기 파일 처리 작업을 수행합니다. |
| `ProjectMarkdownTranslationMixin` | `co_op_translator.core.project.translation.project_markdown_translation` | Markdown 파일 읽기, 콘텐츠 번역, 경로 재작성, 메타데이터, 고지문 및 쓰기를 조정합니다. |
| `ProjectNotebookTranslationMixin` | `co_op_translator.core.project.translation.project_notebook_translation` | 노트북 파일 읽기, Markdown 셀 번역, 경로 재작성, 메타데이터, 고지문 및 쓰기를 조정합니다. |
| `ProjectImageTranslationMixin` | `co_op_translator.core.project.translation.project_image_translation` | 소스 이미지 검색, 이미지 번역, 출력 경로, 메타데이터 및 쓰기를 조정합니다. |
| `ProjectEvaluator` | `co_op_translator.core.project.project_evaluator` | 번역된 Markdown 쌍을 찾고 번역 품질을 평가하며 낮은 신뢰도 수리 워크플로를 위한 신뢰도 메타데이터를 읽습니다. |
| `ReviewRunner` | `co_op_translator.review.runner` | 소스 파일, 대상 언어 및 구성된 번역 루트 전반에 걸친 결정론적 검토 검사를 조정합니다. |
| `ReviewTarget` | `co_op_translator.review.targets` | 해당 루트에 대해 검토되는 소스 루트와 번역 출력 디렉터리를 설명합니다. |
| `LanguageFolderMigrator` | `co_op_translator.core.project.language_migrator` | 레거시 별칭 언어 폴더를 감지하고 정식 BCP 47 폴더 마이그레이션 계획을 준비합니다. |
| `Config` | `co_op_translator.config.base_config` | `.env` 파일을 로드하고 필수 LLM 및 선택적 Vision 제공자가 구성되었는지 확인합니다. |
| `LLMConfig` | `co_op_translator.config.llm_config.config` | Azure OpenAI, OpenAI 또는 Anthropic을 자동 감지하고 필수 환경 변수를 검증하며 제공자 연결 검사를 실행합니다. |
| `VisionConfig` | `co_op_translator.config.vision_config.config` | Azure AI Vision 구성을 감지하고 이미지 번역을 위한 연결 검사를 실행합니다. |