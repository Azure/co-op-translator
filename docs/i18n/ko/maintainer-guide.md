# 유지보수자 가이드

이 페이지는 API, CLI, 및 문서 사이트가 어떻게 연결되어 있는지 요약합니다.

## 공개 API 경계

안정적인 Python API는 다음에서 내보내집니다:

```python
co_op_translator.api
```

공개 API는 콘텐츠 번역 도우미, 경로 재작성 도우미, 프로젝트 오케스트레이션 및 검토로 구성됩니다:

```python
from co_op_translator.api import (
    ImageTranslationOptions,
    MarkdownTranslationOptions,
    NotebookTranslationOptions,
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

새 공개 API를 추가할 때는 다음을 업데이트하세요:

- `src/co_op_translator/api/__init__.py`
- `docs/api.md`
- `tests/co_op_translator/` 아래의 관련 API 테스트(예: `test_api.py` 또는 `test_review_api.py`)

프로젝트가 직접 지원할 의도가 없는 한 하위 수준의 `core` 모듈을 안정적인 API로 문서화하지 마세요.

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

`src/co_op_translator/__main__.py`는 스크립트 이름으로 분기합니다:

- `translate`는 `co_op_translator.cli.translate.translate_command`를 호출합니다
- `evaluate`는 `co_op_translator.cli.evaluate.evaluate_command`를 호출합니다
- `migrate-links`는 `co_op_translator.cli.migrate_links.migrate_links_command`를 호출합니다
- `co-op-review`는 `co_op_translator.cli.review.review_command`를 호출합니다

`co-op-translator-mcp`는 `__main__.py`를 우회하여 `co_op_translator.mcp.server:main`을 직접 호출합니다.

CLI 옵션을 추가하거나 변경할 때는 다음을 업데이트하세요:

- 관련 `src/co_op_translator/cli/*.py` 명령
- `docs/cli.md`
- 동작이 변경되는 경우 CLI 관련 테스트

## MCP 서버

MCP 서버는 다음에 구현되어 있습니다:

```python
co_op_translator.mcp.server
```

서버는 의도적으로 하위 수준의 `core` 모듈을 호출하는 대신 공개 Python API를 래핑합니다. MCP 클라이언트, Python 호출자 및 CLI가 동일한 동작을 공유하도록 이 경계를 그대로 유지하세요.

MCP 도구를 추가하거나 변경할 때는 다음을 업데이트하세요:

- `src/co_op_translator/mcp/server.py`
- `tests/co_op_translator/test_mcp_server.py`
- `docs/mcp.md`
- 공개 API 표면이 변경되면 `docs/api.md`

저장소 번역 도구는 MCP를 통해 모델로 호출 가능하며 여러 파일을 쓸 수 있습니다. 기본값으로 `dry_run=True`를 유지하고 실제 쓰기(non-dry-run) 프로젝트 번역 전에 `confirm_write=True`를 요구하세요.

## 번역 흐름

프로젝트 번역의 상위 수준 흐름은 다음과 같습니다:

1. CLI 인수 또는 API 매개변수를 파싱합니다.
2. `LLMConfig`로 LLM 구성을 검증합니다.
3. 이미지 번역이 선택된 경우 Azure AI Vision을 검증합니다.
4. 언어 코드를 정규화합니다.
5. 레거시 언어 폴더 별칭을 감지합니다.
6. 번역량을 추정합니다.
7. 해당되는 경우 README의 언어/코스 섹션을 업데이트합니다.
8. 프로젝트 번역을 `ProjectTranslator`에 위임합니다.
9. `ProjectTranslator`는 파일 처리를 `TranslationManager`에 위임합니다.

`TranslationManager`는 파일 유형별 집중된 믹스인으로 구성됩니다:

- `ProjectMarkdownTranslationMixin`는 Markdown 파일 읽기, 콘텐츠 번역, 경로 재작성, 메타데이터, 면책조항 및 쓰기를 처리합니다.
- `ProjectNotebookTranslationMixin`는 노트북 파일 읽기, Markdown 셀 번역, 경로 재작성, 메타데이터, 면책조항 및 쓰기를 처리합니다.
- `ProjectImageTranslationMixin`는 이미지 탐색, 텍스트 추출/번역, 렌더된 이미지 쓰기 및 메타데이터를 처리합니다.

하위 수준의 콘텐츠 API는 프로젝트 워크플로를 건너뜁니다:

1. `translate_markdown_content` 및 `translate_notebook_content`는 메모리 내 콘텐츠만 번역합니다.
2. `translate_image_content`는 단일 이미지의 텍스트를 번역하고 렌더된 이미지 객체를 반환합니다.
3. `rewrite_markdown_paths` 및 `rewrite_notebook_paths`는 명시적인 후처리 도우미입니다. 이들은 번역도 수행하지 않고 프로젝트 쓰기도 수행하지 않습니다.

## 검토 흐름

결정적 검토 흐름은 다음과 같습니다:

1. CLI 인수 또는 API 매개변수를 파싱합니다.
2. 요청된 언어 코드를 정규화합니다.
3. `root_dir`, `root_dirs` 또는 `groups`에서 하나 이상의 검토 대상(target)을 빌드합니다.
4. 선택적으로 `--changed-from`으로 소스 파일을 제한합니다.
5. 구조, 번역 최신성, Markdown 무결성 및 로컬 링크/이미지 경로에 대해 결정적 검사를 실행합니다.
6. 텍스트 출력 또는 GitHub 형식의 Markdown 중 하나를 출력합니다.
7. 검토 오류가 발견되면 실패로 종료합니다.

검토 흐름은 API 키를 필요로 하지 않으며 풀 리퀘스트 CI에 적합해야 합니다. 풀 리퀘스트 워크플로우는 매 실행마다 체크 요약을 작성하며 `co-op-review`가 실패할 때만 PR 코멘트를 게시합니다.

## 문서 사이트

문서 사이트는 다음에 의해 구성됩니다:

```text
mkdocs.yml
requirements-docs.txt
docs/
```

`docs/` 디렉터리는 정식 문서 소스입니다. 프로젝트가 의도적으로 다른 게시 문서 표면을 도입하지 않는 한 이 디렉터리 외부에 새로운 최종 사용자 가이드를 추가하지 마세요.

로컬에서 빌드:

```bash
python -m pip install -r requirements-docs.txt
python -m mkdocs build --strict
```

로컬 미리보기:

```bash
python -m mkdocs serve
```

생성된 사이트는 git에서 무시되는 `site/`에 작성됩니다.

## GitHub Pages 워크플로

`.github/workflows/docs.yml`은 풀 리퀘스트에서 사이트를 빌드하고 `main`으로의 푸시에서 배포합니다.

워크플로우는 다음을 설치합니다:

```bash
pip install -r requirements-docs.txt
```

문서 워크플로우는 문서 도구체인만 설치합니다. `mkdocs.yml`은 `mkdocstrings`를 `src/`로 가리키므로 공개 API 페이지를 전체 런타임 의존성 세트를 설치하지 않고도 소스 트리에서 렌더링할 수 있습니다. 향후 API 문서가 빌드 중에 선택적 런타임 제공자를 가져오는 것을 요구한다면 `.github/workflows/docs.yml`과 이 가이드를 함께 업데이트하세요.

## 문서 품질 기준

문서 변경을 병합하기 전에 다음을 실행하세요:

```bash
python -m mkdocs build --strict
git diff --check
```

깨진 링크, 잘못된 네비게이션 항목 및 API 렌더링 문제들이 조기에 실패하도록 엄격한 빌드를 사용하세요.