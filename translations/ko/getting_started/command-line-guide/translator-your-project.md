<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "33db54f4f3ca9f0321be05374b591f2b",
  "translation_date": "2025-05-06T17:58:05+00:00",
  "source_file": "getting_started/command-line-guide/translator-your-project.md",
  "language_code": "ko"
}
-->
# Co-op Translator를 사용해 프로젝트 번역하기

**Co-op Translator**는 프로젝트 내 마크다운과 이미지 파일을 여러 언어로 번역할 수 있는 커맨드라인 인터페이스(CLI) 도구입니다. 이 섹션에서는 도구 사용법, 다양한 CLI 옵션, 그리고 여러 사용 사례에 대한 예시를 설명합니다.

> [!NOTE]
> 모든 명령어와 상세 설명은 [Command reference](./command-reference.md)를 참고하세요.

---

## 예시 시나리오 및 명령어

다음은 **Co-op Translator**의 일반적인 사용 사례와 실행할 명령어 예시입니다.

### 1. 기본 번역 (단일 언어)

프로젝트 전체(마크다운 파일과 이미지)를 단일 언어, 예를 들어 한국어로 번역하려면 다음 명령어를 사용하세요:

```bash
translate -l "ko"
```

이 명령어는 기존 번역을 삭제하지 않고 모든 마크다운과 이미지 파일을 한국어로 새로 번역해 추가합니다.

> [!TIP]
>
> **Co-op Translator**에서 지원하는 언어 코드를 확인하고 싶다면 저장소의 [Supported Languages](https://github.com/Azure/co-op-translator#supported-languages) 섹션을 방문하세요.

#### Phi-3 CookBook 예시

**Phi-3 CookBook**에서는 기존 마크다운 파일과 이미지를 한국어로 추가 번역할 때 다음 방법을 사용했습니다.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko"
Translating images: 100%|███████████████████████████████████████████████████| 276/276 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 153/153 [1:43:07<00:00, 241.31s/it]
```

### 2. 여러 언어 번역하기

스페인어, 프랑스어, 독일어 등 여러 언어로 프로젝트를 번역하려면 다음 명령어를 사용하세요:

```bash
translate -l "es fr de"
```

이 명령어는 기존 번역을 덮어쓰지 않고 스페인어, 프랑스어, 독일어로 새 번역을 추가합니다.

#### Phi-3 CookBook 예시

**Phi-3 CookBook**에서는 최신 커밋을 반영하기 위해 변경사항을 가져온 후, 새로 추가된 마크다운 파일과 이미지를 번역할 때 다음 방법을 사용했습니다.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko ja zh tw es fr" -a
Translating images: 100%|███████████████████████████████████████████████████| 273/273 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 6/6 [24:07<00:00, 241.31s/it]
```

> [!NOTE]
> 일반적으로 한 번에 한 언어씩 번역하는 것이 권장되지만, 특정 변경사항을 한꺼번에 적용해야 하는 경우 여러 언어를 동시에 번역하는 것이 효율적일 수 있습니다.

### 3. 루트 디렉터리 지정하기

기본적으로 번역기는 현재 작업 디렉터리를 사용합니다. 프로젝트가 다른 위치에 있다면 `-r` 옵션으로 루트 디렉터리를 지정하세요:

```bash
translate -l "es fr de" -r "./my_project"
```

이 명령어는 `./my_project` into Spanish, French, and German.

### 4. Updating Translations (Deletes Existing Translations)

To update existing translations (i.e., delete the current translations and replace them with new ones), use the `-u` 옵션과 함께 사용합니다. 이 옵션은 지정한 언어의 기존 번역을 모두 삭제하고 다시 번역합니다.

```bash
translate -l "ko" -u
```

주의: 이 명령어는 기존 번역 삭제 전에 확인을 요청합니다.

#### Phi-3 CookBook 예시

**Phi-3 CookBook**에서는 스페인어로 번역된 모든 파일을 업데이트할 때 다음 방법을 사용했습니다. 여러 마크다운 문서에서 원본 내용에 큰 변경이 있을 경우 이 방법을 추천합니다. 만약 업데이트할 번역 파일이 몇 개뿐이라면, 해당 파일만 수동으로 삭제한 뒤 `-a` 옵션을 사용해 번역을 추가하는 것이 더 효율적입니다.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "es" -u
Warning: The update command will delete all existing translations for 'es' and re-translate everything.
Do you want to continue? Type 'yes' to proceed: yes
Proceeding with update...
Translating images: 100%|████████████████████████████████████████████| 150/150 [43:46<00:00, 15.55s/it]
Translating markdown files: 100%|███████████████████████████████████| 95/95 [1:40:27<00:00, 125.62s/it]
```

### 6. 이미지 파일만 번역하기

프로젝트 내 이미지 파일만 번역하려면 `-img` 옵션을 사용하세요:

```bash
translate -l "ko" -img
```

이 명령어는 마크다운 파일에는 영향을 주지 않고 이미지 파일만 한국어로 번역합니다.

### 7. 마크다운 파일만 번역하기

마크다운 파일만 번역하려면 `-md` 옵션을 사용하세요:

```bash
translate -l "ko" -md
```

### 8. 번역된 파일 오류 확인하기

번역된 파일의 오류를 확인하고 필요 시 재번역하려면 `-chk` 옵션을 사용하세요:

```bash
translate -l "ko" -chk
```

이 명령어는 번역된 마크다운 파일을 검사하고 오류가 있는 파일에 대해 번역을 재시도합니다.

#### Phi-3 CookBook 예시

**Phi-3 CookBook**에서는 한국어 파일의 번역 오류를 확인하고, 문제 있는 파일을 자동으로 재번역할 때 다음 방법을 사용했습니다.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko" -chk 
Checking translated files for errors in ko...
Checking files for ko: 100%|██████████████████████████████████████████████████| 95/95 [00:01<00:00, 65.47file/s]
Retrying vsc-extension-quickstart.md for ko:   0%|                                     | 0/17 [00:00<?, ?file/s] 
```

이 옵션은 번역 오류를 감지합니다. 현재는 원본과 번역 파일 간 줄바꿈 차이가 6줄 이상일 경우 번역 오류로 간주합니다. 앞으로 더 유연한 기준으로 개선할 계획입니다.

예를 들어, 누락된 덩어리나 손상된 번역을 감지하는 데 유용하며, 해당 파일을 자동으로 재번역합니다.

하지만 문제 있는 파일을 이미 알고 있다면, 해당 파일을 수동으로 삭제한 뒤 `-a` option to re-translate them.

### 9. Debug Mode

To enable detailed logging for troubleshooting, use the `-d` 옵션을 사용하는 것이 더 효율적입니다:

```bash
translate -l "ko" -d
```

이 명령어는 디버그 모드로 번역을 실행하여, 번역 과정에서 발생하는 문제를 파악할 수 있는 추가 로그 정보를 제공합니다.

#### Phi-3 CookBook 예시

**Phi-3 CookBook**에서는 마크다운 파일 내 링크가 많을 경우 번역 과정에서 포맷 오류, 번역 누락, 줄바꿈 무시 현상이 발생하는 문제를 겪었습니다. 이 문제를 진단하기 위해 `-d` 옵션을 사용해 번역 과정을 확인했습니다.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "ko" -d
DEBUG:openai._base_client:Request options: {'method': 'post', 'url': '/chat/completions', 'headers': {'api-key': 'af04e0bea45747d8a7b8c131c1971044'}, 'files': None, 'json_data': {'messages': [{'role': 'user', 'content': "Translate the following text to ko. NEVER ADD ANY EXTRA CONTENT OUTSIDE THE TRANSLATION. TRANSLATE ONLY WHAT IS GIVEN TO YOU.. MAINTAIN MARKDOWN FORMAT\n\n# Phi-3 Cookbook: Hands-On Examples with Microsoft's Phi-3 Models [![Open and use the samples in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phi-3cookbook) [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%
...
```

### 10. 모든 언어 번역하기

프로젝트를 지원하는 모든 언어로 번역하려면 `all` 키워드를 사용하세요.

> [!WARNING]
> 모든 언어를 한꺼번에 번역하면 프로젝트 크기에 따라 상당한 시간이 소요될 수 있습니다. 예를 들어, **Phi-3 CookBook**을 스페인어로 번역하는 데 약 2시간이 걸렸습니다. 20개 언어를 한 사람이 모두 처리하는 것은 현실적이지 않으므로, 여러 기여자가 각각 1~2개 언어씩 나눠서 작업하고 번역을 점진적으로 업데이트하는 것이 좋습니다.

```bash
translate -l "all"
```

이 명령어는 프로젝트를 지원하는 모든 언어로 번역합니다. 진행할 경우 프로젝트 크기에 따라 시간이 오래 걸릴 수 있습니다.

> [!TIP]
>
> ### 업데이트가 필요한 파일 삭제하기
> Pull Request에서 최근 변경된 파일을 업데이트하려면, 먼저 해당 파일명과 일치하는 기존 번역본을 모든 언어 폴더에서 삭제해야 합니다. 다음 명령어를 사용하면 번역 폴더 내 특정 이름의 파일을 한꺼번에 삭제할 수 있습니다.
>
> ### Windows에서:
> 1. **명령 프롬프트 사용하기**:
>    - 명령 프롬프트를 엽니다.
>    - `cd` 명령어로 파일이 위치한 폴더로 이동합니다.
>    - 다음 명령어를 사용해 파일을 삭제합니다:
>      ```
>      del /s *filename*
>      ```
>      `/s` 옵션은 하위 디렉터리도 검색합니다.
>
> 2. **PowerShell 사용하기**:
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
>   - Use the `find` 명령어:
>     ```bash
>     find . -type f -name "*filename*" -delete
>     ```
>     `filename` with the specific name.
>
> Always double-check the files before deleting to avoid accidental loss. 
>
> Once you have deleted the files which need to be replace simply rerun your `translate -l` 명령어로 최신 파일 변경사항을 업데이트하세요.

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 노력하고 있으나, 자동 번역에는 오류나 부정확한 내용이 포함될 수 있음을 유의해 주시기 바랍니다. 원본 문서의 원어 버전이 권위 있는 출처로 간주되어야 합니다. 중요한 정보의 경우 전문적인 인간 번역을 권장합니다. 본 번역 사용으로 인한 오해나 잘못된 해석에 대해서는 책임을 지지 않습니다.