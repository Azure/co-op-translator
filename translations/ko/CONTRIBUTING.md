<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d95d7ec0097c5569ac16dd42840787a2",
  "translation_date": "2025-07-04T06:46:51+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "ko"
}
-->
# Co-op Translator에 기여하기

이 프로젝트는 기여와 제안을 환영합니다. 대부분의 기여는 기여자 라이선스 계약(CLA)에 동의해야 하며, 이를 통해 귀하가 기여할 권리가 있으며 실제로 기여를 사용할 권리를 우리에게 부여한다는 것을 선언해야 합니다. 자세한 내용은 https://cla.opensource.microsoft.com를 방문하세요.

풀 리퀘스트를 제출하면, CLA 봇이 자동으로 CLA 제공이 필요한지 여부를 결정하고 PR에 적절히 표시합니다(예: 상태 확인, 댓글). 봇이 제공하는 지침을 따르기만 하면 됩니다. CLA를 사용하는 모든 저장소에서 한 번만 이 작업을 수행하면 됩니다.

## 개발 환경 설정

이 프로젝트의 개발 환경을 설정하려면 의존성 관리를 위해 Poetry를 사용하는 것이 좋습니다. 우리는 `pyproject.toml`을 사용하여 프로젝트 의존성을 관리하므로, 의존성을 설치하려면 Poetry를 사용해야 합니다.

### 가상 환경 생성

#### pip 사용

```bash
python -m venv .venv
```

#### Poetry 사용

```bash
poetry init
```

### 가상 환경 활성화

#### pip 및 Poetry 모두에 해당

- Windows:

    ```bash
    .venv\Scripts\activate.bat
    ```

- Mac/Linux:

    ```bash
    source .venv/bin/activate
    ```

#### Poetry 사용

```bash
poetry shell
```

### 패키지 및 필요한 패키지 설치

#### Poetry 사용 (pyproject.toml에서)

```bash
poetry install
```

### 수동 테스트

PR을 제출하기 전에 실제 문서를 사용하여 번역 기능을 테스트하는 것이 중요합니다:

1. 루트 디렉터리에 테스트 디렉터리를 만듭니다:
    ```bash
    mkdir test_docs
    ```

2. 번역하고자 하는 일부 마크다운 문서와 이미지를 테스트 디렉터리에 복사합니다. 예를 들어:
    ```bash
    cp /path/to/your/docs/*.md test_docs/
    cp /path/to/your/images/*.png test_docs/
    ```

3. 패키지를 로컬에 설치합니다:
    ```bash
    pip install -e .
    ```

4. 테스트 문서에서 Co-op Translator를 실행합니다:
    ```bash
    python -m co_op_translator --language-codes ko --root-dir test_docs
    ```

5. `test_docs/translations` 및 `test_docs/translated_images`에서 번역된 파일을 확인하여 다음을 검증합니다:
   - 번역 품질
   - 메타데이터 주석이 올바른지
   - 원래의 마크다운 구조가 유지되는지
   - 링크와 이미지가 제대로 작동하는지

이 수동 테스트는 실제 시나리오에서 변경 사항이 잘 작동하는지 확인하는 데 도움이 됩니다.

### 환경 변수

1. 제공된 `.env.template` 파일을 복사하여 루트 디렉터리에 `.env` 파일을 만듭니다.
1. 안내에 따라 환경 변수를 채웁니다.

> [!TIP]
>
> ### 추가 개발 환경 옵션
>
> 프로젝트를 로컬에서 실행하는 것 외에도 GitHub Codespaces 또는 VS Code Dev Containers를 사용하여 대체 개발 환경을 설정할 수 있습니다.
>
> #### GitHub Codespaces
>
> GitHub Codespaces를 사용하여 이 샘플을 가상으로 실행할 수 있으며 추가 설정이나 설정이 필요하지 않습니다.
>
> 버튼을 클릭하면 브라우저에서 웹 기반 VS Code 인스턴스가 열립니다:
>
> 1. 템플릿을 엽니다(몇 분이 걸릴 수 있습니다):
>
>     [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/azure/co-op-translator)
>
> #### VS Code Dev Containers를 사용하여 로컬에서 실행
>
> ⚠️ 이 옵션은 Docker Desktop에 최소 16GB의 RAM이 할당된 경우에만 작동합니다. 16GB 미만의 RAM을 사용하는 경우 [GitHub Codespaces 옵션](../..) 또는 [로컬 설정](../..)을 시도할 수 있습니다.
>
> 관련 옵션은 VS Code Dev Containers로, [Dev Containers 확장](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)을 사용하여 로컬 VS Code에서 프로젝트를 엽니다:
>
> 1. Docker Desktop을 시작합니다(설치되어 있지 않다면 설치)
> 2. 프로젝트를 엽니다:
>
>    [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator)

### 코드 스타일

우리는 프로젝트 전반에 걸쳐 일관된 코드 스타일을 유지하기 위해 [Black](https://github.com/psf/black)을 Python 코드 포매터로 사용합니다. Black은 타협 없는 코드 포매터로, Python 코드를 Black 코드 스타일에 맞게 자동으로 재포맷합니다.

#### 설정

Black 설정은 `pyproject.toml`에 지정되어 있습니다:

```toml
[tool.black]
line-length = 88
target-version = ['py310']
include = '\.pyi?$'
```

#### Black 설치

Poetry(권장) 또는 pip을 사용하여 Black을 설치할 수 있습니다:

##### Poetry 사용

개발 환경을 설정할 때 Black이 자동으로 설치됩니다:
```bash
poetry install
```

##### pip 사용

pip을 사용하는 경우 Black을 직접 설치할 수 있습니다:
```bash
pip install black
```

#### Black 사용

##### Poetry 사용

1. 프로젝트의 모든 Python 파일을 포맷합니다:
    ```bash
    poetry run black .
    ```

2. 특정 파일이나 디렉터리를 포맷합니다:
    ```bash
    poetry run black path/to/file_or_directory
    ```

##### pip 사용

1. 프로젝트의 모든 Python 파일을 포맷합니다:
    ```bash
    black .
    ```

2. 특정 파일이나 디렉터리를 포맷합니다:
    ```bash
    black path/to/file_or_directory
    ```

> [!TIP]
> 코드를 저장할 때 Black으로 자동 포맷하도록 편집기를 설정하는 것이 좋습니다. 대부분의 현대적인 편집기는 확장이나 플러그인을 통해 이를 지원합니다.

## Co-op Translator 실행

환경에서 Poetry를 사용하여 Co-op Translator를 실행하려면 다음 단계를 따르세요:

1. 번역 테스트를 수행할 디렉터리로 이동하거나 테스트 목적으로 임시 폴더를 만듭니다.

2. 다음 명령을 실행합니다. `-l ko`를 번역하려는 언어 코드로 바꾸세요. `-d` 플래그는 디버그 모드를 나타냅니다.

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> [!NOTE]
> 명령을 실행하기 전에 Poetry 환경이 활성화되어 있는지(poetry shell) 확인하세요.

## 유지 관리자

### 커밋 메시지 및 병합 전략

프로젝트의 커밋 기록의 일관성과 명확성을 보장하기 위해 **Squash and Merge** 전략을 사용할 때 **최종 커밋 메시지**에 대해 특정 커밋 메시지 형식을 따릅니다.

풀 리퀘스트(PR)가 병합되면 개별 커밋이 하나의 커밋으로 압축됩니다. 최종 커밋 메시지는 깨끗하고 일관된 기록을 유지하기 위해 아래 형식을 따라야 합니다.

#### 커밋 메시지 형식 (Squash and Merge용)

커밋 메시지에 다음 형식을 사용합니다:

```bash
<type>: <description> (#<PR number>)
```

- **type**: 커밋의 범주를 지정합니다. 다음 유형을 사용합니다:
  - `Docs`: 문서 업데이트.
  - `Build`: 빌드 시스템 또는 의존성과 관련된 변경 사항, 구성 파일, CI 워크플로우, Dockerfile 업데이트 포함.
  - `Core`: 프로젝트의 핵심 기능 또는 기능 수정, 특히 `src/co_op_translator/core` 디렉터리의 파일과 관련된 것.

- **description**: 변경 사항에 대한 간결한 요약.
- **PR number**: 커밋과 관련된 풀 리퀘스트 번호.

**예시**:

- `Docs: 설치 지침을 명확하게 업데이트 (#50)`
- `Core: 이미지 번역 처리 개선 (#60)`

> [!NOTE]
> 현재 **`Docs`**, **`Core`**, **`Build`** 접두사는 수정된 소스 코드에 적용된 레이블을 기반으로 PR 제목에 자동으로 추가됩니다. 올바른 레이블이 적용된 경우, PR 제목을 수동으로 업데이트할 필요는 없습니다. 모든 것이 올바른지 확인하고 접두사가 적절하게 생성되었는지 확인하기만 하면 됩니다.

#### 병합 전략

우리는 풀 리퀘스트에 대해 **Squash and Merge**를 기본 전략으로 사용합니다. 이 전략은 개별 커밋이 그렇지 않더라도 커밋 메시지가 우리의 형식을 따르도록 보장합니다.

**이유**:

- 깨끗하고 선형적인 프로젝트 기록.
- 커밋 메시지의 일관성.
- 사소한 커밋(예: "오타 수정")으로 인한 소음 감소.

병합할 때, 최종 커밋 메시지가 위에서 설명한 커밋 메시지 형식을 따르는지 확인하세요.

**Squash and Merge 예시**
PR에 다음과 같은 커밋이 포함된 경우:

- `fix typo`
- `update README`
- `adjust formatting`

다음과 같이 압축되어야 합니다:
`Docs: 문서 명확성과 포맷 개선 (#65)`

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 우리는 정확성을 위해 노력하지만, 자동 번역에는 오류나 부정확성이 있을 수 있음을 유의하시기 바랍니다. 원본 문서는 해당 언어로 작성된 것이 권위 있는 출처로 간주되어야 합니다. 중요한 정보에 대해서는 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 책임을 지지 않습니다.