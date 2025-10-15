<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "20943a46b11c6d74814f41a817a6db4c",
  "translation_date": "2025-10-15T02:41:43+00:00",
  "source_file": "getting_started/command-line-guide/translator-your-project.md",
  "language_code": "ko"
}
-->
# Co-op Translator로 프로젝트 번역하기

**Co-op Translator**는 프로젝트 내의 마크다운 파일과 이미지 파일을 여러 언어로 번역할 수 있도록 도와주는 커맨드라인 인터페이스(CLI) 도구입니다. 이 섹션에서는 도구 사용 방법, 다양한 CLI 옵션, 그리고 여러 상황에 맞는 예시를 설명합니다.

> [!NOTE]
> 모든 명령어와 자세한 설명은 [Command reference](./command-reference.md)에서 확인할 수 있습니다.

---

## 예시 시나리오 및 명령어

여기 **Co-op Translator**의 대표적인 사용 예시와 그에 맞는 명령어를 소개합니다.

### 1. 기본 번역 (단일 언어)

프로젝트 전체(마크다운 파일과 이미지)를 한 가지 언어(예: 한국어)로 번역하려면 다음 명령어를 사용하세요.

```bash
translate -l "ko"
```

이 명령어는 모든 마크다운 및 이미지 파일을 한국어로 번역하며, 기존 번역을 삭제하지 않고 새 번역만 추가합니다.

> [!TIP]
>
> **Co-op Translator**에서 지원하는 언어 코드를 확인하고 싶으신가요? 저장소의 [Supported Languages](https://github.com/Azure/co-op-translator#supported-languages) 섹션에서 자세한 정보를 확인할 수 있습니다.

#### Phi-3 CookBook 예시

**Phi-3 CookBook**에서는 기존 마크다운 파일과 이미지에 대해 한국어 번역을 추가할 때 다음 방법을 사용했습니다.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko"
Translating images: 100%|███████████████████████████████████████████████████| 276/276 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 153/153 [1:43:07<00:00, 241.31s/it]
```

### 2. 다국어 번역

프로젝트를 여러 언어(예: 스페인어, 프랑스어, 독일어)로 번역하려면 다음 명령어를 사용하세요.

```bash
translate -l "es fr de"
```

이 명령어는 프로젝트를 스페인어, 프랑스어, 독일어로 번역하며, 기존 번역을 덮어쓰지 않고 새 번역만 추가합니다.

#### Phi-3 CookBook 예시

**Phi-3 CookBook**에서는 최신 커밋을 반영한 후, 새로 추가된 마크다운 파일과 이미지를 번역할 때 다음 방법을 사용했습니다.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko ja zh tw es fr" -a
Translating images: 100%|███████████████████████████████████████████████████| 273/273 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 6/6 [24:07<00:00, 241.31s/it]
```

> [!NOTE]
> 일반적으로는 한 번에 한 언어씩 번역하는 것이 권장되지만, 이처럼 특정 변경 사항을 여러 언어에 추가해야 할 때는 여러 언어를 동시에 번역하는 것이 효율적일 수 있습니다.

### 3. 번역 업데이트 (기존 번역 삭제)

기존 번역을 업데이트하려면(즉, 현재 번역을 삭제하고 새로 번역하려면) `-u` 옵션을 사용하세요. 이 옵션은 지정한 언어의 기존 번역을 모두 삭제하고 다시 번역합니다.

```bash
translate -l "ko" -u
```

경고: 이 명령어는 기존 번역을 삭제하기 전에 확인 메시지를 표시합니다.

#### Phi-3 CookBook 예시

**Phi-3 CookBook**에서는 스페인어로 번역된 모든 파일을 업데이트할 때 다음 방법을 사용했습니다. 원본 내용이 여러 마크다운 문서에서 크게 변경된 경우 이 방법을 추천합니다. 단, 업데이트할 번역 파일이 몇 개뿐이라면 해당 파일만 직접 삭제한 후 `-a` 옵션으로 새 번역을 추가하는 것이 더 효율적입니다.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "es" -u
Warning: The update command will delete all existing translations for 'es' and re-translate everything.
Do you want to continue? Type 'yes' to proceed: yes
Proceeding with update...
Translating images: 100%|████████████████████████████████████████████| 150/150 [43:46<00:00, 15.55s/it]
Translating markdown files: 100%|███████████████████████████████████| 95/95 [1:40:27<00:00, 125.62s/it]
```

### 5. 이미지 파일만 번역

프로젝트 내 이미지 파일만 번역하려면 `-img` 옵션을 사용하세요.

```bash
translate -l "ko" -img
```

이 명령어는 마크다운 파일에는 영향을 주지 않고 이미지 파일만 한국어로 번역합니다.

### 6. 마크다운 파일만 번역

프로젝트 내 마크다운 파일만 번역하려면 `-md` 옵션을 사용하세요.

```bash
translate -l "ko" -md
```

#### Phi-3 CookBook 예시

**Phi-3 CookBook**에서는 한국어 파일의 번역 오류를 점검하고, 오류가 감지된 파일을 자동으로 재번역할 때 다음 방법을 사용했습니다.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko" -chk 
Checking translated files for errors in ko...
Checking files for ko: 100%|██████████████████████████████████████████████████| 95/95 [00:01<00:00, 65.47file/s]
Retrying vsc-extension-quickstart.md for ko:   0%|                                     | 0/17 [00:00<?, ?file/s] 
```

이 옵션은 번역 오류를 점검합니다. 현재는 원본과 번역 파일의 줄바꿈 차이가 6줄 이상일 경우 번역 오류로 간주합니다. 앞으로 더 유연하게 기준을 개선할 예정입니다.

예를 들어, 이 방법은 누락된 부분이나 손상된 번역을 감지하는 데 유용하며, 해당 파일을 자동으로 재번역합니다.

하지만 이미 문제가 있는 파일을 알고 있다면, 해당 파일만 직접 삭제한 후 `-a` 옵션으로 재번역하는 것이 더 효율적입니다.

### 8. 디버그 모드

문제 해결을 위해 상세 로그를 활성화하려면 `-d` 옵션을 사용하세요.

```bash
translate -l "ko" -d
```

이 명령어는 번역을 디버그 모드로 실행하여, 번역 과정에서 발생하는 문제를 파악하는 데 도움이 되는 추가 로그 정보를 제공합니다.

#### Phi-3 CookBook 예시

**Phi-3 CookBook**에서는 마크다운 파일에 링크가 많을 때 번역이 깨지거나 줄바꿈이 무시되는 등 포맷 오류가 발생하는 문제를 겪었습니다. 이 문제를 진단하기 위해 `-d` 옵션을 사용해 번역 과정을 확인했습니다.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "ko" -d
DEBUG:openai._base_client:Request options: {'method': 'post', 'url': '/chat/completions', 'headers': {'api-key': 'af04e0bea45747d8a7b8c131c1971044'}, 'files': None, 'json_data': {'messages': [{'role': 'user', 'content': "Translate the following text to ko. NEVER ADD ANY EXTRA CONTENT OUTSIDE THE TRANSLATION. TRANSLATE ONLY WHAT IS GIVEN TO YOU.. MAINTAIN MARKDOWN FORMAT\n\n# Phi-3 Cookbook: Hands-On Examples with Microsoft's Phi-3 Models [![Open and use the samples in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phi-3cookbook) [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%
...
```

### 9. 모든 언어로 번역

프로젝트를 지원되는 모든 언어로 번역하려면 all 키워드를 사용하세요.

> [!WARNING]
> 모든 언어로 한 번에 번역하면 프로젝트 크기에 따라 상당한 시간이 소요될 수 있습니다. 예를 들어, **Phi-3 CookBook**을 스페인어로 번역하는 데 약 2시간이 걸렸습니다. 규모를 고려하면 한 사람이 20개 언어를 모두 처리하는 것은 비현실적입니다. 여러 기여자가 각자 1~2개 언어씩 맡아 번역을 점진적으로 업데이트하는 것이 좋습니다.

```bash
translate -l "all"
```

이 명령어는 프로젝트를 지원되는 모든 언어로 번역합니다. 진행할 경우, 프로젝트 크기에 따라 번역에 상당한 시간이 걸릴 수 있습니다.

> [!TIP]
>
> ### 번역 파일 수동 삭제 (선택 사항)
> 이제 번역 파일은 원본 파일이 업데이트되면 자동으로 감지되어 정리됩니다.
>
> 하지만 특정 파일을 다시 번역하거나 시스템 동작을 무시하고 직접 업데이트하고 싶다면, 다음 명령어로 언어 폴더 전체에서 해당 파일을 삭제할 수 있습니다.
>
> ### Windows에서:
> 1. **명령 프롬프트 사용**:
>    - 명령 프롬프트를 엽니다.
>    - `cd` 명령어로 파일이 있는 폴더로 이동합니다.
>    - 다음 명령어로 파일을 삭제합니다:
>      ```
>      del /s *filename*
>      ```
>      `filename`을 찾고자 하는 파일명 일부로 바꿔주세요. `/s` 옵션은 하위 폴더도 검색합니다.
>
> 2. **PowerShell 사용**:
>    - PowerShell을 엽니다.
>    - 다음 명령어를 실행합니다:
>      ```powershell
>      Get-ChildItem -Path "C:\YourPath" -Filter "*filename*" -Recurse | Remove-Item -Force
>      ```
>      `"C:\YourPath"`를 폴더 경로로, `filename`을 파일명으로 바꿔주세요.
>
> ### macOS/Linux에서:
> 1. **터미널 사용**:
>   - 터미널을 엽니다.
>   - `cd`로 해당 디렉터리로 이동합니다.
>   - `find` 명령어를 사용합니다:
>     ```bash
>     find . -type f -name "*filename*" -delete
>     ```
>     `filename`을 파일명으로 바꿔주세요.
>
> 파일을 삭제하기 전에 항상 한 번 더 확인하여 실수로 파일이 삭제되지 않도록 주의하세요.
>
> 삭제가 필요한 파일을 지운 후, `translate -l` 명령어를 다시 실행하면 최신 파일 변경 사항이 반영됩니다.

---

**면책 조항**:
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있지만, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서(원어)가 권위 있는 자료로 간주되어야 합니다. 중요한 정보의 경우 전문적인 인간 번역을 권장합니다. 이 번역의 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.