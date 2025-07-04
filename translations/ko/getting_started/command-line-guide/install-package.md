<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b6d85d887d2664539a438dae5d0dfa50",
  "translation_date": "2025-07-04T06:50:51+00:00",
  "source_file": "getting_started/command-line-guide/install-package.md",
  "language_code": "ko"
}
-->
# Co-op 번역기 패키지 설치

**Co-op 번역기**는 프로젝트의 모든 마크다운 파일과 이미지를 여러 언어로 번역하는 데 도움을 주기 위해 설계된 명령줄 인터페이스(CLI) 도구입니다. 이 튜토리얼은 번역기를 설정하고 다양한 사용 사례에 맞게 실행하는 방법을 안내합니다.

### 가상 환경 생성

`pip` 또는 `Poetry`를 사용하여 가상 환경을 생성할 수 있습니다. 터미널에 다음 명령 중 하나를 입력하세요.

#### pip 사용하기

```bash
python -m venv .venv
```

#### Poetry 사용하기

```bash
poetry init
```

### 가상 환경 활성화

가상 환경을 생성한 후에는 활성화해야 합니다. 운영 체제에 따라 단계가 다릅니다. 터미널에 다음 명령을 입력하세요.

#### pip 및 Poetry 모두 사용하기

- Windows:

    ```bash
    .venv\Scripts\activate
    ```

- Mac/Linux:

    ```bash
    source .venv/bin/activate
    ```

#### Poetry 사용하기

1. Poetry로 환경을 생성했다면, 터미널에 다음 명령을 입력하여 활성화하세요.

    ```bash
    poetry shell
    ```

### 패키지 및 필요한 패키지 설치

가상 환경이 설정되고 활성화되면, 다음 단계는 필요한 종속성을 설치하는 것입니다.

### 빠른 설치

Co-Op 번역기를 pip를 통해 설치

```
pip install co-op-translator
```
또는 

Poetry를 통해 설치
```
poetry add co-op-translator
```

#### 이 저장소를 복제한 경우 requirements.txt에서 pip 사용하기

![NOTE] 빠른 설치를 통해 co-op 번역기를 설치한 경우 이 작업을 수행하지 마세요.

1. pip를 사용하는 경우, 터미널에 다음 명령을 입력하세요. `requirements.txt` 파일에 지정된 필요한 패키지를 자동으로 설치합니다:

    ```bash
    pip install -r requirements.txt
    ```

#### pyproject.toml에서 Poetry 사용하기

1. Poetry를 사용하는 경우, 터미널에 다음 명령을 입력하세요. `pyproject.toml` 파일에 지정된 필요한 패키지를 자동으로 설치합니다:

    ```bash
    poetry install
    ```

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 우리는 정확성을 위해 노력하지만, 자동 번역에는 오류나 부정확성이 있을 수 있음을 유의하시기 바랍니다. 원본 문서는 해당 언어로 작성된 것이 권위 있는 출처로 간주되어야 합니다. 중요한 정보에 대해서는 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 책임을 지지 않습니다.