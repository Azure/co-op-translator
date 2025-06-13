<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d238206c3503631e32774716d11d1868",
  "translation_date": "2025-06-12T18:43:52+00:00",
  "source_file": "getting_started/command-line-guide/translator-your-project.md",
  "language_code": "ko"
}
-->
# Co-op Translator로 프로젝트 번역하기

**Co-op Translator**는 프로젝트 내 마크다운과 이미지 파일을 여러 언어로 번역할 수 있도록 도와주는 커맨드라인 인터페이스(CLI) 도구입니다. 이 섹션에서는 도구 사용법, 다양한 CLI 옵션, 그리고 여러 사용 사례에 대한 예제를 설명합니다.

> [!NOTE]
> 명령어 전체 목록과 상세 설명은 [Command reference](./command-reference.md)를 참고하세요.

---

## 예제 시나리오 및 명령어

다음은 **Co-op Translator**의 일반적인 사용 사례와 실행할 적절한 명령어입니다.

### 1. 기본 번역 (단일 언어)

프로젝트 전체(마크다운 파일과 이미지)를 한 가지 언어, 예를 들어 한국어로 번역하려면 다음 명령어를 사용하세요:

```bash
translate -l "ko"
```

이 명령어는 모든 마크다운과 이미지 파일을 한국어로 번역하며, 기존 번역을 삭제하지 않고 새 번역을 추가합니다.

> [!TIP]
>
> **Co-op Translator**에서 지원하는 언어 코드를 확인하고 싶다면 저장소의 [Supported Languages](https://github.com/Azure/co-op-translator#supported-languages) 섹션을 방문하세요.

#### Phi-3 CookBook 예제

**Phi-3 CookBook**에서는 기존 마크다운 파일과 이미지에 한국어 번역을 추가하기 위해 다음 방법을 사용했습니다.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko"
Translating images: 100%|███████████████████████████████████████████████████| 276/276 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 153/153 [1:43:07<00:00, 241.31s/it]
```

### 2. 여러 언어 번역

프로젝트를 여러 언어(예: 스페인어, 프랑스어, 독일어)로 번역하려면 다음 명령어를 사용하세요:

```bash
translate -l "es fr de"
```

이 명령어는 프로젝트를 스페인어, 프랑스어, 독일어로 번역하며 기존 번역을 덮어쓰지 않고 새 번역을 추가합니다.

#### Phi-3 CookBook 예제

**Phi-3 CookBook**에서는 최신 커밋을 반영하기 위해 변경 사항을 받은 후, 새로 추가된 마크다운 파일과 이미지를 번역하기 위해 다음 방법을 사용했습니다.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko ja zh tw es fr" -a
Translating images: 100%|███████████████████████████████████████████████████| 273/273 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 6/6 [24:07<00:00, 241.31s/it]
```

> [!NOTE]
> 일반적으로 한 번에 한 언어씩 번역하는 것이 권장되지만, 특정 변경 사항을 한꺼번에 반영해야 하는 경우 여러 언어를 동시에 번역하는 것이 효율적일 수 있습니다.

### 3. 번역 업데이트 (기존 번역 삭제)

기존 번역을 삭제하고 새 번역으로 교체하려면 `-u` 옵션을 사용하세요. 이 옵션은 지정한 언어의 모든 기존 번역을 삭제하고 다시 번역합니다.

```bash
translate -l "ko" -u
```

주의: 이 명령어는 기존 번역을 삭제하기 전에 확인을 요청합니다.

#### Phi-3 CookBook 예제

**Phi-3 CookBook**에서는 스페인어로 번역된 모든 파일을 업데이트하기 위해 다음 방법을 사용했습니다. 여러 마크다운 문서에서 원본 내용이 크게 변경된 경우 이 방법을 추천합니다. 번역된 마크다운 파일이 몇 개만 업데이트되어야 한다면, 해당 파일만 수동으로 삭제한 후 `-a` 옵션으로 새 번역을 추가하는 것이 더 효율적입니다.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "es" -u
Warning: The update command will delete all existing translations for 'es' and re-translate everything.
Do you want to continue? Type 'yes' to proceed: yes
Proceeding with update...
Translating images: 100%|████████████████████████████████████████████| 150/150 [43:46<00:00, 15.55s/it]
Translating markdown files: 100%|███████████████████████████████████| 95/95 [1:40:27<00:00, 125.62s/it]
```

### 5. 이미지 파일만 번역

프로젝트 내 이미지 파일만 번역하려면 `-img` 옵션을 사용하세요:

```bash
translate -l "ko" -img
```

이 명령어는 마크다운 파일에 영향을 주지 않고 이미지 파일만 한국어로 번역합니다.

### 6. 마크다운 파일만 번역

프로젝트 내 마크다운 파일만 번역하려면 `-md` 옵션을 사용하세요:

```bash
translate -l "ko" -md
```

### 7. 번역된 파일 오류 확인

번역된 파일의 오류를 확인하고 필요 시 번역을 다시 시도하려면 `-chk` 옵션을 사용하세요:

```bash
translate -l "ko" -chk
```

이 명령어는 번역된 마크다운 파일을 검사하고 오류가 있는 파일에 대해 번역을 재시도합니다.

#### Phi-3 CookBook 예제

**Phi-3 CookBook**에서는 한국어 파일의 번역 오류를 확인하고 문제가 있는 파일에 대해 자동으로 번역을 재시도하기 위해 다음 방법을 사용했습니다.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko" -chk 
Checking translated files for errors in ko...
Checking files for ko: 100%|██████████████████████████████████████████████████| 95/95 [00:01<00:00, 65.47file/s]
Retrying vsc-extension-quickstart.md for ko:   0%|                                     | 0/17 [00:00<?, ?file/s] 
```

이 옵션은 번역 오류를 검사합니다. 현재는 원본과 번역본의 줄바꿈 차이가 6줄 이상인 경우 해당 파일을 번역 오류로 간주합니다. 앞으로 더 유연한 기준으로 개선할 계획입니다.

예를 들어, 이 방법은 누락된 부분이나 손상된 번역을 찾아내는 데 유용하며, 해당 파일의 번역을 자동으로 재시도합니다.

하지만 문제가 있는 파일을 이미 알고 있다면, 해당 파일을 수동으로 삭제하고 `-a` option to re-translate them.

### 8. Debug Mode

To enable detailed logging for troubleshooting, use the `-d` 옵션을 사용하는 것이 더 효율적입니다:

```bash
translate -l "ko" -d
```

이 명령어는 디버그 모드로 번역을 실행하여, 번역 과정에서 문제를 파악하는 데 도움이 되는 추가 로그 정보를 제공합니다.

#### Phi-3 CookBook 예제

**Phi-3 CookBook**에서는 마크다운 파일 내 많은 링크가 포함된 번역이 형식 오류(번역이 깨지거나 줄바꿈이 무시되는 현상)를 일으키는 문제를 겪었습니다. 문제를 진단하기 위해 `-d` 옵션을 사용하여 번역 프로세스가 어떻게 동작하는지 확인했습니다.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "ko" -d
DEBUG:openai._base_client:Request options: {'method': 'post', 'url': '/chat/completions', 'headers': {'api-key': 'af04e0bea45747d8a7b8c131c1971044'}, 'files': None, 'json_data': {'messages': [{'role': 'user', 'content': "Translate the following text to ko. NEVER ADD ANY EXTRA CONTENT OUTSIDE THE TRANSLATION. TRANSLATE ONLY WHAT IS GIVEN TO YOU.. MAINTAIN MARKDOWN FORMAT\n\n# Phi-3 Cookbook: Hands-On Examples with Microsoft's Phi-3 Models [![Open and use the samples in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phi-3cookbook) [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%
...
```

### 9. 모든 언어 번역

프로젝트를 지원하는 모든 언어로 번역하려면 `all` 키워드를 사용하세요.

> [!WARNING]
> 모든 언어를 한 번에 번역하는 것은 프로젝트 크기에 따라 상당한 시간이 걸릴 수 있습니다. 예를 들어, **Phi-3 CookBook**을 스페인어로 번역하는 데 약 2시간이 소요되었습니다. 20개 언어를 한 사람이 처리하는 것은 현실적이지 않습니다. 여러 기여자가 각각 1~2개 언어를 맡아 번역을 점진적으로 업데이트하는 것을 권장합니다.

```bash
translate -l "all"
```

이 명령어는 프로젝트를 사용 가능한 모든 언어로 번역합니다. 진행 시 프로젝트 크기에 따라 시간이 많이 소요될 수 있습니다.

> [!TIP]
>
> ### 번역된 파일 수동 삭제 (선택 사항)
> 번역된 파일은 이제 소스 파일이 업데이트될 때 자동으로 감지되어 정리됩니다.
>
> 하지만 특정 파일을 다시 번역하거나 시스템 동작을 덮어쓰려면, 다음 명령어를 사용해 해당 파일의 모든 언어 버전을 삭제할 수 있습니다.
>
> ### Windows에서:
> 1. **명령 프롬프트 사용**:
>    - 명령 프롬프트를 엽니다.
>    - `cd` 명령어로 파일이 위치한 폴더로 이동합니다.
>    - 다음 명령어로 파일을 삭제합니다:
>      ```
>      del /s *filename*
>      ```
>      `filename` with the specific part of the file name you're looking for. The `/s` 옵션은 하위 디렉터리도 검색합니다.
>
> 2. **PowerShell 사용**:
>    - PowerShell을 엽니다.
>    - 다음 명령어를 실행합니다:
>      ```powershell
>      Get-ChildItem -Path "C:\YourPath" -Filter "*filename*" -Recurse | Remove-Item -Force
>      ```
>      `"C:\YourPath"` with the folder path and `filename` with the specific name.
>
> ### On macOS/Linux:
> 1. **Using Terminal**:
>   - Open Terminal.
>   - Navigate to the directory with `cd`.
>   - Use the `find` 명령어를 대체하세요:
>     ```bash
>     find . -type f -name "*filename*" -delete
>     ```
>     `filename` with the specific name.
>
> Always double-check the files before deleting to avoid accidental loss. 
>
> Once you have deleted the files which need to be replace simply rerun your `translate -l` 명령어로 최신 파일 변경 사항을 업데이트하세요.

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 노력하고 있으나, 자동 번역에는 오류나 부정확한 내용이 포함될 수 있음을 유의하시기 바랍니다. 원문 문서가 권위 있는 출처로 간주되어야 합니다. 중요한 정보의 경우 전문적인 인간 번역을 권장합니다. 본 번역의 사용으로 인한 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.