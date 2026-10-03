# 유지관리자 안내서

이 페이지는 API, CLI, 문서 사이트가 어떻게 연결되어 있는지 요약합니다.

## 공개 API 경계

안정적인 Python API는 다음에서 내보냅니다:

```python
co_op_translator.api
```

공개 API는 콘텐츠 번역 도우미, 경로 재작성 도우미, 프로젝트 조정, 그리고 검토로 구성됩니다:

```python
from co_op_translator.api import (
    ImageTranslationOptions,
    MarkdownTranslationOptions,
    NotebookTranslationOptions,
    TranslationBaseline,
    TranslationStateProvider,
    TranslationUpdate,
    run_review,
    run_translation,
    rewrite_markdown_paths,
    rewrite_notebook_paths,
    translate_image_content,
    translate_markdown_content,
    translate_notebook_content,
    translate_project,
)
```

`TranslationStateProvider` 는 호스팅된 통합을 위한 지속성 경계입니다.
생성된 후보는 수락된 베이스라인과 분리되어야 하므로
병합되지 않은 번역이 진실의 출처가 되지 않도록 해야 합니다.

새로운 공개 API를 추가할 때는 다음을 업데이트하세요:

- `src/co_op_translator/api/__init__.py`
- `docs/api.md`
- `tests/co_op_translator/` 아래의 관련 API 테스트(예: `test_api.py` 또는 `test_review_api.py`)

프로젝트가 직접적으로 이를 지원할 의도가 없는 한 낮은 수준의 `core` 모듈을 안정적인 API로 문서화하는 것을 피하세요.

## CLI 진입점

패키지는 다음 Poetry 스크립트를 정의합니다:

```toml
[tool.poetry.scripts]
translate = "co_op_translator.__main__:main"
evaluate = "co_op_translator.__main__:main"
migrate-links = "co_op_translator.__main__:main"
co-op-review = "co_op_translator.__main__:main"
co-op-translator-mcp = "co_op_translator.mcp.server:main"
```

`src/co_op_translator/__main__.py`은 스크립트 이름으로 분기합니다:

- `translate` 는 `co_op_translator.cli.translate.translate_command` 를 호출합니다
- `evaluate` 는 `co_op_translator.cli.evaluate.evaluate_command` 를 호출합니다
- `migrate-links` 는 `co_op_translator.cli.migrate_links.migrate_links_command` 를 호출합니다
- `co-op-review` 는 `co_op_translator.cli.review.review_command` 를 호출합니다

`co-op-translator-mcp` 는 `__main__.py` 를 우회하고 `co_op_translator.mcp.server:main` 을 직접 호출합니다.

CLI 옵션을 추가하거나 변경할 때는 다음을 업데이트하세요:

- 관련된 `src/co_op_translator/cli/*.py` 명령
- `docs/cli.md`
- 동작이 변경될 경우 CLI 관련 테스트

## MCP 서버

MCP 서버는 다음에 구현되어 있습니다:

```python
co_op_translator.mcp.server
```

서버는 의도적으로 낮은 수준의 `core` 모듈을 호출하는 대신 공개 Python API를 래핑합니다. 이 경계를 유지하여 MCP 클라이언트, Python 호출자 및 CLI가 동일한 동작을 공유하도록 하세요.

MCP 도구를 추가하거나 변경할 때는 다음을 업데이트하세요:

- `src/co_op_translator/mcp/server.py`
- `tests/co_op_translator/test_mcp_server.py`
- `docs/mcp.md`
- 공개 API 표면이 변경되면 `docs/api.md`

리포지토리 번역 도구는 MCP를 통해 모델로 호출할 수 있으며 여러 파일을 작성할 수 있습니다. 기본값으로 `dry_run=True`를 유지하고 비-dry-run 프로젝트 번역을 수행하기 전에 `confirm_write=True` 를 요구하세요.

## 번역 흐름

상위 수준의 프로젝트 번역 흐름은 다음과 같습니다:

1. CLI 인자 또는 API 파라미터를 파싱합니다.
2. `LLMConfig` 로 LLM 구성을 검증합니다.
3. 이미지 번역이 선택된 경우 Azure AI Vision을 검증합니다.
4. 언어 코드를 정규화합니다.
5. 레거시 언어 폴더 별칭을 감지합니다.
6. 번역량을 추정합니다.
7. 해당되는 경우 README의 언어/과정 섹션을 업데이트합니다.
8. 프로젝트 번역을 `ProjectTranslator` 에 위임합니다.
9. `ProjectTranslator` 는 파일 처리를 `TranslationManager` 에 위임합니다.

`TranslationManager` 는 특정 파일 유형의 믹스인들로 구성됩니다:

- `ProjectMarkdownTranslationMixin` 는 Markdown 파일 읽기, 콘텐츠 번역, 경로 재작성, 메타데이터, 면책 조항 및 쓰기를 처리합니다.
- `ProjectNotebookTranslationMixin` 는 노트북 파일 읽기, Markdown 셀 번역, 경로 재작성, 메타데이터, 면책 조항 및 쓰기를 처리합니다.
- `ProjectImageTranslationMixin` 는 이미지 검색, 텍스트 추출/번역, 렌더된 이미지 쓰기 및 메타데이터를 처리합니다.

하위 수준의 콘텐츠 API는 프로젝트 워크플로우를 건너뜁니다:

1. `translate_markdown_content` 및 `translate_notebook_content` 는 메모리 내의 콘텐츠만 번역합니다.
2. `translate_image_content` 는 단일 이미지의 텍스트를 번역하고 렌더된 이미지 객체를 반환합니다.
3. `rewrite_markdown_paths` 및 `rewrite_notebook_paths` 는 명시적인 후처리 헬퍼입니다. 이들은 번역이나 프로젝트 쓰기를 수행하지 않습니다.

## 검토 흐름

결정론적 검토 흐름은 다음과 같습니다:

1. CLI 인자 또는 API 파라미터를 파싱합니다.
2. 요청된 언어 코드를 정규화합니다.
3. `root_dir`, `root_dirs` 또는 `groups` 에서 하나 이상의 검토 대상을 구성합니다.
4. 선택적으로 `--changed-from` 로 소스 파일을 제한합니다.
5. 구조, 번역 최신성, Markdown 무결성, 로컬 링크/이미지 경로에 대한 결정론적 검사를 실행합니다.
6. 텍스트 출력 또는 GitHub 형식의 Markdown 중 하나를 출력합니다.
7. 검토 오류가 발견되면 실패 상태로 종료합니다.

검토 흐름은 API 키를 필요로 하지 않으며 로컬 검사나 선택적 소비자 CI에서 사용할 수 있습니다. 이 저장소는 모든 풀 리퀘스트에 대해 `co-op-review` 를 자동으로 실행하지 않습니다.

## 문서 사이트

문서 사이트는 다음에 의해 구성됩니다:

```text
mkdocs.yml
requirements-docs.txt
docs/
```

`docs/` 디렉터리는 표준 문서 소스입니다. 프로젝트가 의도적으로 다른 공개 문서 표면을 도입하지 않는 한 이 디렉터리 외부에 새로운 최종 사용자 가이드를 추가하지 마세요.

로컬에서 빌드:

```bash
python -m pip install -r requirements-docs.txt
python -m mkdocs build --strict
```

로컬에서 미리보기:

```bash
python -m mkdocs serve
```

생성된 사이트는 git에서 무시되는 `site/` 에 작성됩니다.

## GitHub Pages 워크플로우

`.github/workflows/docs.yml` 은 풀 리퀘스트에서 사이트를 빌드하고 `main` 에 푸시될 때 배포합니다.

워크플로우는 다음을 설치합니다:

```bash
pip install -r requirements-docs.txt
```

문서 워크플로우는 문서 툴체인만 설치합니다. `mkdocs.yml` 은 `mkdocstrings` 를 `src/` 로 가리키므로 공개 API 페이지를 전체 런타임 의존성을 설치하지 않고도 소스 트리에서 렌더링할 수 있습니다. 향후 API 문서가 빌드 중에 선택적 런타임 제공자를 임포트해야 하는 경우, `.github/workflows/docs.yml` 과 이 안내서를 함께 업데이트하세요.

## 문서 품질 기준

문서 변경 사항을 머지하기 전에 다음을 실행하세요:

```bash
python -m mkdocs build --strict
git diff --check
```

깨진 링크, 잘못된 내비게이션 항목 및 API 렌더링 문제를 조기에 탐지하도록 엄격한 빌드를 사용하세요.