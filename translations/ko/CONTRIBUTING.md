<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "758ca1c5ae0d32c52d2dd59132dcfbf0",
  "translation_date": "2025-11-30T10:27:20+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "ko"
}
-->
# Co-op Translator에 기여하기

이 프로젝트는 기여와 제안을 환영합니다. 대부분의 기여는 기여자가 자신의 기여물을 사용할 권리를 실제로 보유하고 있음을 선언하는 기여자 라이선스 계약(CLA)에 동의해야 합니다. 자세한 내용은 https://cla.opensource.microsoft.com 을 참조하세요.

풀 리퀘스트를 제출하면 CLA 봇이 자동으로 CLA 제출 필요 여부를 판단하고 PR에 적절한 상태 검사나 코멘트를 추가합니다. 봇의 안내에 따라 진행하면 되며, CLA는 모든 저장소에서 한 번만 제출하면 됩니다.

## 개발 환경 설정

이 프로젝트의 개발 환경 설정에는 의존성 관리를 위해 Poetry 사용을 권장합니다. 프로젝트 의존성 관리는 `pyproject.toml`을 사용하므로, 의존성 설치 시 Poetry를 사용해야 합니다.

### 가상 환경 생성

#### pip 사용 시

```bash
python -m venv .venv
```

#### Poetry 사용 시

```bash
poetry init
```

### 가상 환경 활성화

#### pip와 Poetry 모두에 해당

- Windows:

    ```bash
    .venv\Scripts\activate.bat
    ```

- Mac/Linux:

    ```bash
    source .venv/bin/activate
    ```

#### Poetry 사용 시

```bash
poetry shell
```

### 패키지 및 필수 패키지 설치

#### Poetry 사용 (pyproject.toml 기준)

```bash
poetry install
```

### 수동 테스트

PR 제출 전에 실제 문서로 번역 기능을 테스트하는 것이 중요합니다:

1. 루트 디렉터리에 테스트 디렉터리 생성:
    ```bash
    mkdir test_docs
    ```

2. 번역할 마크다운 문서와 이미지 일부를 테스트 디렉터리에 복사합니다. 예:
    ```bash
    cp /path/to/your/docs/*.md test_docs/
    cp /path/to/your/images/*.png test_docs/
    ```

3. 패키지를 로컬에 설치:
    ```bash
    pip install -e .
    ```

4. 테스트 문서에 대해 Co-op Translator 실행:
    ```bash
    python -m co_op_translator --language-codes ko --root-dir test_docs
    ```

5. `test_docs/translations`와 `test_docs/translated_images`에서 번역된 파일을 확인하여:
   - 번역 품질
   - 메타데이터 주석의 정확성
   - 원본 마크다운 구조 유지 여부
   - 링크와 이미지 정상 작동 여부

이 수동 테스트는 실제 환경에서 변경 사항이 잘 작동하는지 확인하는 데 도움이 됩니다.

### 환경 변수

1. 루트 디렉터리에 `.env.template` 파일을 복사하여 `.env` 파일 생성
2. 안내에 따라 환경 변수 값을 입력

> [!TIP]
>
> ### 추가 개발 환경 옵션
>
> 로컬 실행 외에도 GitHub Codespaces 또는 VS Code Dev Containers를 사용해 대체 개발 환경을 구성할 수 있습니다.
>
> #### GitHub Codespaces
>
> GitHub Codespaces를 사용하면 별도의 설정 없이 웹 기반 VS Code 인스턴스를 브라우저에서 바로 실행할 수 있습니다.
>
> 버튼을 클릭하면 웹 브라우저에서 VS Code가 열립니다:
>
> 1. 템플릿 열기 (몇 분 소요될 수 있음):
>
>     [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/azure/co-op-translator)
>
> #### VS Code Dev Containers를 사용한 로컬 실행
>
> ⚠️ 이 옵션은 Docker Desktop에 최소 16GB RAM이 할당되어 있어야 작동합니다. 16GB 미만인 경우 [GitHub Codespaces 옵션](../..)이나 [로컬 환경 설정](../..)을 시도하세요.
>
> VS Code Dev Containers는 [Dev Containers 확장](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)을 사용해 로컬 VS Code에서 프로젝트를 열어줍니다:
>
> 1. Docker Desktop 실행 (설치되어 있지 않으면 설치)
> 2. 프로젝트 열기:
>
>    [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator)


### 코드 스타일

프로젝트 전반에 일관된 코드 스타일 유지를 위해 [Black](https://github.com/psf/black)을 Python 코드 포매터로 사용합니다. Black은 자동으로 코드를 Black 스타일에 맞게 재포맷하는 엄격한 포매터입니다.

#### 설정

Black 설정은 `pyproject.toml`에 명시되어 있습니다:

```toml
[tool.black]
line-length = 88
target-version = ['py310']
include = '\.pyi?$'
```

#### Black 설치

Poetry(권장) 또는 pip를 사용해 Black을 설치할 수 있습니다:

##### Poetry 사용 시

개발 환경 설정 시 Black이 자동으로 설치됩니다:
```bash
poetry install
```

##### pip 사용 시

pip를 사용하는 경우 직접 설치할 수 있습니다:
```bash
pip install black
```

#### Black 사용법

##### Poetry 사용 시

1. 프로젝트 내 모든 Python 파일 포맷:
    ```bash
    poetry run black .
    ```

2. 특정 파일 또는 디렉터리 포맷:
    ```bash
    poetry run black path/to/file_or_directory
    ```

##### pip 사용 시

1. 프로젝트 내 모든 Python 파일 포맷:
    ```bash
    black .
    ```

2. 특정 파일 또는 디렉터리 포맷:
    ```bash
    black path/to/file_or_directory
    ```

> [!TIP]
> 대부분의 최신 에디터는 저장 시 Black으로 자동 포맷하는 확장이나 플러그인을 지원하므로, 이를 설정하는 것을 권장합니다.

## Co-op Translator 실행하기

Poetry 환경에서 Co-op Translator를 실행하려면 다음 단계를 따르세요:

1. 번역 테스트를 수행할 디렉터리로 이동하거나 임시 폴더를 만듭니다.

2. 다음 명령어를 실행합니다. `-l ko` 부분을 원하는 번역 언어 코드로 바꾸세요. `-d` 플래그는 디버그 모드입니다.

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> [!NOTE]
> 명령 실행 전에 Poetry 환경이 활성화(poetry shell)되어 있는지 확인하세요.

## 새로운 언어 기여하기

새로운 언어 지원 추가 기여를 환영합니다. PR을 열기 전에 원활한 검토를 위해 아래 단계를 완료하세요.

1. 폰트 매핑에 언어 추가
   - `src/co_op_translator/fonts/font_language_mappings.yml` 편집
   - 다음 항목 추가:
     - `code`: ISO 유사 언어 코드 (예: `vi`)
     - `name`: 사람이 읽기 쉬운 표시 이름
     - `font`: `src/co_op_translator/fonts/`에 포함된 해당 스크립트를 지원하는 폰트
     - `rtl`: 오른쪽에서 왼쪽 방향이면 `true`, 아니면 `false`

2. 필요한 폰트 파일 포함 (필요한 경우)
   - 새 폰트가 필요한 경우 오픈 소스 배포에 적합한 라이선스인지 확인
   - 폰트 파일을 `src/co_op_translator/fonts/`에 추가

3. 로컬 검증
   - 작은 샘플(마크다운, 이미지, 노트북 등)에 대해 번역 실행
   - 출력이 올바르게 렌더링되는지, 폰트 및 RTL 레이아웃이 정상인지 확인

4. 문서 업데이트
   - `getting_started/supported-languages.md`에 언어 추가 확인
   - `getting_started/README_languages_template.md`는 지원 목록에서 자동 생성되므로 변경 불필요

5. PR 열기
   - 추가한 언어와 폰트/라이선스 관련 사항 설명
   - 가능하면 렌더링 결과 스크린샷 첨부

예시 YAML 항목:

```yaml
new_lang(code):
  name: "New Language"
  font: "NotoSans-Medium.ttf"
  rtl: false
```

### 새 언어 테스트

다음 명령어로 새 언어를 테스트할 수 있습니다:

```bash
# 가상 환경 생성 및 활성화
python -m venv .venv
# 윈도우
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
# 개발 패키지 설치
pip install -e .
# 번역 실행
translate -l "new_lang"
```

## 유지보수자

### 커밋 메시지 및 병합 전략

프로젝트 커밋 기록의 일관성과 명확성을 위해, **Squash and Merge** 전략을 사용할 때 **최종 커밋 메시지**는 아래 형식을 따릅니다.

풀 리퀘스트가 병합되면 개별 커밋들이 하나로 합쳐지며, 최종 커밋 메시지는 깔끔하고 일관된 기록 유지를 위해 아래 형식을 따라야 합니다.

#### 커밋 메시지 형식 (Squash and Merge용)

커밋 메시지는 다음 형식을 사용합니다:

```bash
<type>: <description> (#<PR 번호>)
```

- **type**: 커밋 유형을 지정합니다. 다음 유형을 사용합니다:
  - `Docs`: 문서 업데이트
  - `Build`: 빌드 시스템 또는 의존성 관련 변경 (설정 파일, CI 워크플로, Dockerfile 포함)
  - `Core`: 프로젝트 핵심 기능 또는 `src/co_op_translator/core` 디렉터리 내 파일 관련 변경

- **description**: 변경 사항 간결 요약
- **PR 번호**: 해당 풀 리퀘스트 번호

**예시**:

- `Docs: 설치 지침 명확화 (#50)`
- `Core: 이미지 번역 처리 개선 (#60)`

> [!NOTE]
> 현재 **`Docs`**, **`Core`**, **`Build`** 접두사는 수정된 소스 코드에 적용된 라벨에 따라 PR 제목에 자동으로 추가됩니다. 올바른 라벨이 붙어 있으면 PR 제목을 수동으로 수정할 필요는 없으며, 접두사가 제대로 생성되었는지만 확인하면 됩니다.

#### 병합 전략

풀 리퀘스트 병합 시 기본 전략은 **Squash and Merge**입니다. 이 전략은 개별 커밋 메시지와 상관없이 커밋 메시지 형식을 보장합니다.

**이유**:

- 깔끔하고 선형적인 프로젝트 기록 유지
- 커밋 메시지 일관성 확보
- 사소한 커밋(예: 오타 수정)으로 인한 기록 잡음 감소

병합 시 최종 커밋 메시지가 위 형식을 따르는지 확인하세요.

**Squash and Merge 예시**
PR에 다음 커밋이 있을 때:

- `fix typo`
- `update README`
- `adjust formatting`

이들은 다음과 같이 합쳐집니다:
`Docs: 문서 명확화 및 포맷 개선 (#65)`

### 릴리스 프로세스

유지보수자가 Co-op Translator 새 릴리스를 가장 간단히 배포하는 방법을 설명합니다.

#### 1. `pyproject.toml`에서 버전 올리기

1. 다음 버전 번호 결정 (Semantic Versioning: `MAJOR.MINOR.PATCH` 준수)
2. `pyproject.toml`의 `[tool.poetry]` 아래 `version` 필드 수정
3. 버전만 변경하는 전용 풀 리퀘스트 생성 (자동 업데이트된 lock/메타데이터 파일 포함 가능)
4. 리뷰 후 **Squash and Merge** 사용, 최종 커밋 메시지는 위 형식 준수

#### 2. GitHub 릴리스 생성

1. GitHub 저장소 페이지에서 **Releases** → **Draft a new release** 열기
2. `main` 브랜치에서 새 태그 생성 (예: `v0.13.0`)
3. 릴리스 제목을 버전과 동일하게 설정 (예: `v0.13.0`)
4. **Generate release notes** 클릭해 변경 로그 자동 생성
5. 필요 시 텍스트 편집 (예: 새로 지원하는 언어나 주요 변경 사항 강조)
6. 릴리스 게시하기

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있으나, 자동 번역에는 오류나 부정확성이 포함될 수 있음을 유의하시기 바랍니다. 원문 문서가 권위 있는 출처로 간주되어야 합니다. 중요한 정보의 경우 전문적인 인간 번역을 권장합니다. 본 번역 사용으로 인한 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->