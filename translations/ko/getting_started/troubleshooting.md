<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6e626bef5ed78a1cc55b0dbf44f01d47",
  "translation_date": "2025-10-15T02:41:22+00:00",
  "source_file": "getting_started/troubleshooting.md",
  "language_code": "ko"
}
-->
# Microsoft Co-op Translator 문제 해결 가이드

## 개요
Microsoft Co-Op Translator는 Markdown 문서를 손쉽게 번역할 수 있는 강력한 도구입니다. 이 가이드에서는 도구 사용 중 자주 발생하는 문제를 해결하는 방법을 안내합니다.

## 자주 발생하는 문제와 해결 방법

### 1. Markdown 태그 문제
**문제:** 번역된 Markdown 문서 상단에 `markdown` 태그가 포함되어 있어 렌더링에 문제가 생깁니다.

**해결 방법:** 상단의 `markdown` 태그를 삭제하면 Markdown 파일이 정상적으로 렌더링됩니다.

**단계:**
1. 번역된 Markdown(`.md`) 파일을 엽니다.
2. 문서 맨 위에 있는 `markdown` 태그를 찾습니다.
3. 해당 태그를 삭제합니다.
4. 파일을 저장합니다.
5. 파일을 다시 열어 정상적으로 렌더링되는지 확인합니다.

### 2. 이미지 URL 문제
**문제:** 삽입된 이미지의 URL이 언어 로케일과 맞지 않아 이미지가 잘못 표시되거나 누락됩니다.

**해결 방법:** 이미지의 URL을 확인하고 언어 로케일이 문서와 일치하는지 확인하세요. 모든 이미지는 `translated_images` 폴더에 있으며, 각 이미지 파일명에 언어 로케일 태그가 포함되어 있습니다.

**단계:**
1. 번역된 Markdown 문서를 엽니다.
2. 삽입된 이미지와 URL을 확인합니다.
3. 이미지 파일명에 포함된 언어 로케일이 문서 언어와 일치하는지 검토합니다.
4. 필요하다면 URL을 수정합니다.
5. 변경 후 저장하고 이미지를 정상적으로 볼 수 있는지 확인합니다.

### 3. 번역 정확도
**문제:** 번역된 내용이 정확하지 않거나 추가 편집이 필요합니다.

**해결 방법:** 번역된 문서를 검토하고 정확성과 가독성을 높이기 위해 필요한 수정을 합니다.

**단계:**
1. 번역된 문서를 엽니다.
2. 내용을 꼼꼼히 검토합니다.
3. 번역 정확도를 높이기 위해 필요한 부분을 수정합니다.
4. 변경 사항을 저장합니다.

## 4. 권한 오류, Redacted 또는 404

이미지나 텍스트가 올바른 언어로 번역되지 않고, -d 디버그 모드에서 401 오류가 발생한다면 인증 실패일 가능성이 높습니다. 키가 잘못되었거나 만료되었거나, 엔드포인트의 리전에 연결되어 있지 않을 수 있습니다.

[-d 디버그 스위치](https://github.com/Azure/co-op-translator/blob/main/getting_started/command-reference.md)를 사용해 원인을 더 자세히 파악하세요.

- **오류 메시지:** `Access denied due to invalid subscription key or wrong API endpoint.`
- **가능한 원인:**
  - 요청에 사용된 구독 키가 잘못되었거나 삭제됨.
  - AI Services Key 또는 Subscription Key가 **Azure AI Vision** 리소스가 아닌 Translator나 OpenAI 등 다른 Azure 리소스에 속함.

 **리소스 유형**
  - [Azure Portal](https://portal.azure.com) 또는 [Azure AI Foundry](https://ai.azure.com)에서 리소스 유형이 `Azure AI services` → `Vision`인지 확인하세요.
  - 키가 올바른지 검증하고, 올바른 키를 사용하고 있는지 확인하세요.

## 5. 구성 오류 (새로운 오류 처리)

선택적 번역 시스템이 도입되면서, Co-op Translator는 필수 서비스가 구성되지 않았을 때 명확한 오류 메시지를 제공합니다.

### 5.1. 이미지 번역을 위한 Azure AI 서비스 미구성

**문제:** 이미지 번역(`-img` 플래그)을 요청했지만 Azure AI 서비스가 제대로 구성되지 않았습니다.

**오류 메시지:**
```
Error: Image translation requested but Azure AI Service is not configured.
Please add AZURE_AI_SERVICE_API_KEY and AZURE_AI_SERVICE_ENDPOINT to your .env file.
Check Azure AI Service availability and configuration.
```

**해결 방법:**
1. **옵션 1:** Azure AI 서비스 구성
   - `.env` 파일에 `AZURE_AI_SERVICE_API_KEY` 추가
   - `.env` 파일에 `AZURE_AI_SERVICE_ENDPOINT` 추가
   - 서비스 접근 가능 여부 확인

2. **옵션 2:** 이미지 번역 요청 제거
   ```bash
   # Instead of: translate -l "ko" -img
   # Use: translate -l "ko" -md
   ```

### 5.2. 필수 구성 누락

**문제:** 필수 LLM 구성값이 누락되었습니다.

**오류 메시지:**
```
Error: No language model configuration found.
Please configure either Azure OpenAI or OpenAI in your .env file.
```

**해결 방법:**
1. `.env` 파일에 아래 LLM 구성 중 하나 이상이 있는지 확인하세요:
   - **Azure OpenAI**: `AZURE_OPENAI_API_KEY`와 `AZURE_OPENAI_ENDPOINT`
   - **OpenAI**: `OPENAI_API_KEY`
   
   Azure OpenAI 또는 OpenAI 중 하나만 구성하면 됩니다.

### 5.3. 선택적 번역 혼동

**문제:** 명령이 성공했지만 번역된 파일이 없습니다.

**가능한 원인:**
- 잘못된 파일 유형 플래그(`-md`, `-img`, `-nb`)
- 프로젝트에 일치하는 파일 없음
- 디렉터리 구조 오류

**해결 방법:**
1. **디버그 모드 사용**: 실제 동작을 확인하세요.
   ```bash
   translate -l "ko" -md -d
   ```

2. **프로젝트 내 파일 유형 확인**:
   ```bash
   # For markdown files
   find . -name "*.md" -not -path "./translations/*"
   
   # For notebooks
   find . -name "*.ipynb" -not -path "./translations/*"
   
   # For images
   find . -name "*.png" -o -name "*.jpg" -o -name "*.jpeg" -not -path "./translations/*"
   ```

3. **플래그 조합 검증**:
   ```bash
   # Translate everything (default)
   translate -l "ko"
   
   # Translate specific types
   translate -l "ko" -md -img
   ```

## 6. 구 시스템에서의 마이그레이션

### 6.1. Markdown 전용 모드 폐지

**문제:** 자동 markdown-only fallback에 의존하던 명령이 더 이상 기대대로 동작하지 않습니다.

**이전 동작:**
```bash
# This used to automatically switch to markdown-only mode
translate -l "ko"  # (when Azure AI Vision was not configured)
```

**새 동작:**
```bash
# This now produces an error if image translation is requested but not configured
translate -l "ko" -img
```

**해결 방법:**
- **명확하게 번역 대상을 지정하세요:**
  ```bash
  translate -l "ko" -md        # Only markdown
  translate -l "ko" -md -img   # Markdown and images
  translate -l "ko"            # Everything (if all services configured)
  ```

### 6.2. 예상치 못한 링크 동작

**문제:** 번역된 파일의 링크가 예상과 다른 위치를 가리킵니다.

**원인:** 선택한 파일 유형에 따라 동적으로 링크 처리 방식이 달라집니다.

**해결 방법:**
1. **새로운 링크 동작 이해하기**:
   - `-nb` 포함: 노트북 링크가 번역된 버전을 가리킴
   - `-nb` 미포함: 노트북 링크가 원본 파일을 가리킴
   - `-img` 포함: 이미지 링크가 번역된 버전을 가리킴
   - `-img` 미포함: 이미지 링크가 원본 파일을 가리킴

2. **사용 목적에 맞는 조합 선택**:
   ```bash
   # All internal links point to translated versions
   translate -l "ko" -md -img -nb
   
   # Only markdown translated, other links point to originals
   translate -l "ko" -md
   ```

## 7. GitHub Action은 실행됐지만 Pull Request(PR)이 생성되지 않음

**증상:** `peter-evans/create-pull-request` 워크플로 로그에 다음과 같이 표시됨:

> Branch 'update-translations' is not ahead of base 'main' and will not be created

**가능한 원인:**
- **변경 사항 없음:** 번역 단계에서 차이가 발생하지 않아(이미 최신 상태) PR이 생성되지 않음.
- **출력 무시됨:** `.gitignore`가 커밋하려는 파일을 제외함(예: `*.ipynb`, `translations/`, `translated_images/`).
- **add-paths 불일치:** 액션에 제공한 경로가 실제 출력 위치와 다름.
- **워크플로 논리/조건:** 번역 단계가 일찍 종료되거나 예상치 못한 디렉터리에 파일을 씀.

**해결/확인 방법:**
1. **출력 파일 확인:** 번역 후 작업 공간에 `translations/` 또는 `translated_images/`에 새 파일이나 변경된 파일이 있는지 확인하세요.
   - 노트북 번역 시, `.ipynb` 파일이 실제로 `translations/<lang>/...`에 작성되는지 확인하세요.
2. **`.gitignore` 검토:** 생성된 출력 파일을 무시하지 않도록 하세요. 다음 항목을 무시하지 않아야 합니다:
   - `translations/`
   - `translated_images/`
   - `*.ipynb` (노트북 번역 시)
3. **add-paths가 출력과 일치하는지 확인:** 여러 폴더를 모두 포함하도록 멀티라인 값 사용:
   ```yaml
   with:
     add-paths: |
       translations/
       translated_images/
   ```
4. **디버깅용 PR 강제 생성:** 빈 커밋을 임시로 허용해 연결이 올바른지 확인:
   ```yaml
   with:
     commit-empty: true
   ```
5. **디버그 모드로 실행:** translate 명령에 `-d`를 추가해 발견된 파일과 작성된 파일을 출력하세요.
6. **권한(GITHUB_TOKEN):** 커밋 및 PR 생성을 위해 워크플로에 쓰기 권한이 있는지 확인하세요:
   ```yaml
   permissions:
     contents: write
     pull-requests: write
   ```

## 빠른 디버깅 체크리스트

번역 문제를 해결할 때:

1. **디버그 모드 사용:** 상세 로그를 보려면 `-d` 플래그 추가
2. **플래그 확인:** `-md`, `-img`, `-nb`가 의도와 일치하는지 확인
3. **구성 검증:** `.env` 파일에 필요한 키가 있는지 확인
4. **점진적 테스트:** 먼저 `-md`만 사용해보고, 이후 다른 유형 추가
5. **파일 구조 확인:** 소스 파일이 존재하고 접근 가능한지 확인

사용 가능한 명령과 플래그에 대한 자세한 정보는 [Command Reference](./command-reference.md)를 참고하세요.

---

**면책 조항**:
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있지만, 자동 번역에는 오류나 부정확성이 포함될 수 있음을 유의하시기 바랍니다. 원본 문서의 해당 언어 버전이 공식적인 기준이 되어야 합니다. 중요한 정보의 경우 전문 번역가의 번역을 권장합니다. 본 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.