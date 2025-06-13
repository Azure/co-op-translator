<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b6d85d887d2664539a438dae5d0dfa50",
  "translation_date": "2025-06-12T18:32:37+00:00",
  "source_file": "getting_started/command-line-guide/install-package.md",
  "language_code": "ko"
}
-->
# Co-op 번역기 패키지 설치하기

**Co-op Translator**는 프로젝트 내 모든 마크다운 파일과 이미지를 여러 언어로 번역할 수 있도록 도와주는 커맨드 라인 인터페이스(CLI) 도구입니다. 이 튜토리얼에서는 번역기를 설정하고 다양한 용도에 맞게 실행하는 방법을 안내합니다.

### 가상 환경 만들기

가상 환경은 `pip` 또는 `Poetry` 중 하나를 사용해 만들 수 있습니다. 터미널에 다음 명령어 중 하나를 입력하세요.

#### pip 사용하기

```bash
python -m venv .venv
```

#### Poetry 사용하기

```bash
poetry init
```

### 가상 환경 활성화하기

가상 환경을 만든 후에는 활성화해야 합니다. 운영체제에 따라 방법이 다릅니다. 터미널에 다음 명령어를 입력하세요.

#### pip와 Poetry 모두 해당

- Windows:

    ```bash
    .venv\Scripts\activate
    ```

- Mac/Linux:

    ```bash
    source .venv/bin/activate
    ```

#### Poetry 사용 시

1. Poetry로 가상 환경을 만들었다면, 다음 명령어를 터미널에 입력해 활성화하세요.

    ```bash
    poetry shell
    ```

### 패키지 및 필수 패키지 설치하기

가상 환경이 준비되고 활성화되면, 다음 단계는 필요한 의존성 패키지를 설치하는 것입니다.

### 빠른 설치

pip를 통해 Co-Op Translator 설치하기

```
pip install co-op-translator
```  
또는

Poetry를 통해 설치하기  
```
poetry add co-op-translator
```

#### 이 저장소를 클론한 경우 pip로 (requirements.txt 사용)

![NOTE] 빠른 설치 방식으로 co-op translator를 설치했다면 이 방법을 사용하지 마세요.

1. pip를 사용한다면, 터미널에 다음 명령어를 입력하세요. `requirements.txt`에 명시된 필수 패키지가 자동으로 설치됩니다:

    ```bash
    pip install -r requirements.txt
    ```

#### Poetry 사용 시 (pyproject.toml 사용)

1. Poetry를 사용한다면, 터미널에 다음 명령어를 입력하세요. `pyproject.toml`에 명시된 필수 패키지가 자동으로 설치됩니다:

    ```bash
    poetry install
    ```

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있으나, 자동 번역은 오류나 부정확한 내용이 포함될 수 있음을 유의하시기 바랍니다. 원문 문서가 권위 있는 출처로 간주되어야 합니다. 중요한 정보의 경우 전문 인간 번역을 권장합니다. 본 번역의 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.