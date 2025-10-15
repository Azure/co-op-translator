<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "bd4704f50c55da7d572b691484aa0b30",
  "translation_date": "2025-10-15T02:40:04+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "ko"
}
-->
# Co-op Translator 기여 가이드

이 프로젝트는 다양한 기여와 제안을 환영합니다. 대부분의 기여는 Contributor License Agreement (CLA)에 동의해야 하며, 이는 여러분이 해당 기여를 사용할 권리가 있음을 선언하는 것입니다. 자세한 내용은 https://cla.opensource.microsoft.com 을 참고하세요.

풀 리퀘스트(PR)를 제출하면 CLA 봇이 자동으로 CLA 필요 여부를 판단하고 PR에 상태 체크나 코멘트 등으로 표시합니다. 봇이 안내하는 절차를 따라주시면 됩니다. CLA는 한 번만 동의하면, CLA를 사용하는 모든 저장소에 적용됩니다.

## 개발 환경 설정

이 프로젝트의 개발 환경을 설정할 때는 Poetry를 사용해 의존성을 관리하는 것을 권장합니다. 프로젝트 의존성은 `pyproject.toml`로 관리하므로, 의존성 설치 시 Poetry를 사용해야 합니다.

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

#### pip과 Poetry 모두

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

### 패키지 및 필수 패키지 설치

#### Poetry 사용 (pyproject.toml 기준)

```bash
poetry install
```

### 수동 테스트

PR을 제출하기 전에 실제 문서를 번역해보며 기능을 테스트하는 것이 중요합니다:

1. 루트 디렉터리에 테스트 디렉터리를 만듭니다:
    ```bash
    mkdir test_docs
    ```

2. 번역하고 싶은 마크다운 문서와 이미지를 테스트 디렉터리에 복사합니다. 예시:
    ```bash
    cp /path/to/your/docs/*.md test_docs/
    cp /path/to/your/images/*.png test_docs/
    ```

3. 패키지를 로컬에 설치합니다:
    ```bash
    pip install -e .
    ```

4. 테스트 문서에 Co-op Translator를 실행합니다:
    ```bash
    python -m co_op_translator --language-codes ko --root-dir test_docs
    ```

5. `test_docs/translations`와 `test_docs/translated_images`에서 번역된 파일을 확인하여 아래 항목을 검증합니다:
   - 번역 품질
   - 메타데이터 주석이 올바른지
   - 원래 마크다운 구조가 유지되는지
   - 링크와 이미지가 정상적으로 동작하는지

이런 수동 테스트는 실제 환경에서 변경 사항이 잘 작동하는지 확인하는 데 도움이 됩니다.

### 환경 변수

1. 루트 디렉터리에 `.env.template` 파일을 복사해 `.env` 파일을 만듭니다.
1. 안내에 따라 환경 변수를 채워 넣습니다.

> [!TIP]
>
> ### 추가 개발 환경 옵션
>
> 로컬에서 프로젝트를 실행하는 것 외에도 GitHub Codespaces나 VS Code Dev Containers를 활용해 개발 환경을 구성할 수 있습니다.
>
> #### GitHub Codespaces
>
> GitHub Codespaces를 사용하면 별도의 설정 없이 샘플을 가상으로 실행할 수 있습니다.
>
> 아래 버튼을 클릭하면 브라우저에서 웹 기반 VS Code 인스턴스가 열립니다:
>
> 1. 템플릿을 엽니다 (몇 분 정도 소요될 수 있습니다):
>
>     <a href="https://codespaces.new/azure/co-op-translator"><img src="https://github.com/codespaces/badge.svg" alt="Open in GitHub Codespaces"></a>
>
> #### 로컬에서 VS Code Dev Containers 사용
>
> ⚠️ 이 옵션은 Docker Desktop에 최소 16GB RAM이 할당되어 있어야 작동합니다. 16GB 미만이라면 [GitHub Codespaces 옵션](../..)이나 [로컬 환경 설정](../..)을 시도해보세요.
>
> 관련 옵션으로 VS Code Dev Containers가 있으며, [Dev Containers 확장](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)을 통해 로컬 VS Code에서 프로젝트를 열 수 있습니다:
>
> 1. Docker Desktop을 실행합니다 (설치되어 있지 않다면 설치)
> 2. 프로젝트를 엽니다:
>
>    <a href="https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator"><img src="https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode" alt="Open in Dev Containers"></a>


### 코드 스타일

프로젝트의 일관된 코드 스타일 유지를 위해 [Black](https://github.com/psf/black) Python 코드 포매터를 사용합니다. Black은 타협 없는 코드 포매터로, Python 코드를 자동으로 Black 스타일에 맞게 재정렬합니다.

#### 설정

Black 설정은 `pyproject.toml`에 지정되어 있습니다:

```toml
[tool.black]
line-length = 88
target-version = ['py310']
include = '\.pyi?$'
```

#### Black 설치

Poetry(권장) 또는 pip으로 Black을 설치할 수 있습니다:

##### Poetry 사용

개발 환경을 설정하면 Black이 자동으로 설치됩니다:
```bash
poetry install
```

##### pip 사용

pip을 사용하는 경우 Black을 직접 설치할 수 있습니다:
```bash
pip install black
```

#### Black 사용법

##### Poetry로

1. 프로젝트 내 모든 Python 파일을 포맷:
    ```bash
    poetry run black .
    ```

2. 특정 파일이나 디렉터리만 포맷:
    ```bash
    poetry run black path/to/file_or_directory
    ```

##### pip으로

1. 프로젝트 내 모든 Python 파일을 포맷:
    ```bash
    black .
    ```

2. 특정 파일이나 디렉터리만 포맷:
    ```bash
    black path/to/file_or_directory
    ```

> [!TIP]
> 에디터에서 저장 시 자동으로 Black으로 코드 포맷팅 되도록 설정하는 것을 추천합니다. 대부분의 최신 에디터는 확장이나 플러그인을 통해 지원합니다.

## Co-op Translator 실행하기

Poetry 환경에서 Co-op Translator를 실행하려면 아래 절차를 따르세요:

1. 번역 테스트를 진행할 디렉터리로 이동하거나 테스트용 임시 폴더를 만듭니다.

2. 아래 명령어를 실행합니다. `-l ko`는 번역할 언어 코드로 원하는 언어로 변경할 수 있습니다. `-d` 플래그는 디버그 모드입니다.

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> [!NOTE]
> 명령어 실행 전 Poetry 환경(poetry shell)이 활성화되어 있는지 확인하세요.

## 새로운 언어 기여하기

새로운 언어 지원을 추가하는 기여를 환영합니다. PR을 열기 전에 아래 단계를 완료해주시면 원활한 리뷰가 가능합니다.

1. 폰트 매핑에 언어 추가
   - `src/co_op_translator/fonts/font_language_mappings.yml` 파일을 수정합니다.
   - 아래 항목을 추가합니다:
     - `code`: ISO 스타일 언어 코드 (예: `vi`)
     - `name`: 사람이 읽기 쉬운 언어 이름
     - `font`: 해당 스크립트를 지원하는 `src/co_op_translator/fonts/` 내 폰트
     - `rtl`: 오른쪽에서 왼쪽 언어면 `true`, 아니면 `false`

2. 필요한 폰트 파일 포함
   - 새 폰트가 필요하다면 오픈소스 배포 라이선스 호환성을 확인하세요
   - 폰트 파일을 `src/co_op_translator/fonts/`에 추가하세요

3. 로컬 검증
   - 샘플(마크다운, 이미지, 노트북 등)에 대해 번역을 실행합니다
   - 출력물이 올바르게 렌더링되는지, 폰트 및 RTL 레이아웃이 적용되는지 확인합니다

4. 문서 업데이트
   - `getting_started/supported-languages.md`에 언어가 나타나는지 확인합니다
   - `README_languages_template.md`는 지원 목록에서 자동 생성되므로 수정할 필요 없습니다

5. PR 열기
   - 추가한 언어와 폰트/라이선스 관련 사항을 설명합니다
   - 가능하다면 렌더링된 결과물의 스크린샷을 첨부합니다

예시 YAML 항목:

```yaml
new_lang(code):
  name: "New Language"
  font: "NotoSans-Medium.ttf"
  rtl: false
```


## 유지 관리자 안내

### 커밋 메시지 및 머지 전략

프로젝트의 커밋 히스토리 일관성과 명확성을 위해 **Squash and Merge** 전략을 사용할 때 **최종 커밋 메시지**에 특정 포맷을 적용합니다.

풀 리퀘스트(PR)가 머지될 때, 개별 커밋은 하나로 합쳐집니다. 최종 커밋 메시지는 아래 포맷을 따라야 하며, 깔끔하고 일관된 히스토리를 유지할 수 있습니다.

#### 커밋 메시지 포맷 (Squash and Merge용)

커밋 메시지는 아래 형식을 사용합니다:

```bash
<type>: <description> (#<PR number>)
```

- **type**: 커밋의 범주를 지정합니다. 아래 타입을 사용합니다:
  - `Docs`: 문서 업데이트
  - `Build`: 빌드 시스템이나 의존성 관련 변경, 설정 파일, CI 워크플로우, Dockerfile 등
  - `Core`: 프로젝트 핵심 기능이나 주요 기능 변경, 특히 `src/co_op_translator/core` 디렉터리 관련

- **description**: 변경 사항을 간결하게 요약
- **PR number**: 해당 커밋과 연결된 풀 리퀘스트 번호

**예시**:

- `Docs: 설치 안내 개선 (#50)`
- `Core: 이미지 번역 처리 개선 (#60)`

> [!NOTE]
> 현재 **`Docs`**, **`Core`**, **`Build`** 접두사는 수정된 소스 코드에 적용된 라벨을 기반으로 PR 제목에 자동으로 추가됩니다. 올바른 라벨만 적용되어 있으면 PR 제목을 직접 수정할 필요는 없습니다. 접두사가 제대로 생성되었는지 확인만 해주시면 됩니다.

#### 머지 전략

풀 리퀘스트에는 기본적으로 **Squash and Merge** 전략을 사용합니다. 이 전략은 개별 커밋 메시지가 다르더라도 최종 커밋 메시지가 포맷을 따르도록 보장합니다.

**이유**:

- 깔끔하고 선형적인 프로젝트 히스토리
- 커밋 메시지의 일관성
- 사소한 커밋(예: "오타 수정")으로 인한 노이즈 감소

머지 시, 최종 커밋 메시지가 위에서 설명한 포맷을 따르는지 확인하세요.

**Squash and Merge 예시**
PR에 아래와 같은 커밋이 있다면:

- `fix typo`
- `update README`
- `adjust formatting`

최종 커밋 메시지는 다음과 같이 합쳐집니다:
`Docs: Improve documentation clarity and formatting (#65)`

---

**면책 조항**:
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있지만, 자동 번역에는 오류나 부정확성이 포함될 수 있음을 유의하시기 바랍니다. 원본 문서의 해당 언어 버전이 공식적인 기준이 되어야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 본 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.