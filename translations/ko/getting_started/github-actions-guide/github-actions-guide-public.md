<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "87bf95d45e684475ef1e67d8dae5f6eb",
  "translation_date": "2025-05-06T18:09:49+00:00",
  "source_file": "getting_started/github-actions-guide/github-actions-guide-public.md",
  "language_code": "ko"
}
-->
# Co-op Translator GitHub Action 사용법 (공개 설정)

**대상:** 이 가이드는 표준 GitHub Actions 권한으로 충분한 대부분의 공개 또는 비공개 저장소 사용자를 위한 것입니다. 내장된 `GITHUB_TOKEN`를 활용합니다.

Co-op Translator GitHub Action을 사용해 저장소 문서 번역을 자동화하세요. 이 가이드는 원본 Markdown 파일이나 이미지가 변경될 때마다 자동으로 번역된 내용을 포함한 풀 리퀘스트를 생성하도록 액션을 설정하는 방법을 안내합니다.

> [!IMPORTANT]
>
> **적합한 가이드 선택하기:**
>
> 이 가이드는 **표준 `GITHUB_TOKEN`를 이용한 더 간단한 설정** 방법을 설명합니다. 민감한 GitHub App Private Key를 관리할 필요가 없어 대부분 사용자에게 권장되는 방법입니다.
>

## 사전 준비 사항

GitHub Action을 설정하기 전에 필요한 AI 서비스 자격 증명이 준비되어 있는지 확인하세요.

**1. 필수: AI 언어 모델 자격 증명**  
지원하는 언어 모델 중 최소 하나에 대한 자격 증명이 필요합니다.

- **Azure OpenAI**: Endpoint, API Key, 모델/배포 이름, API 버전 필요  
- **OpenAI**: API Key, (선택 사항: 조직 ID, Base URL, 모델 ID)  
- 자세한 내용은 [Supported Models and Services](../../../../README.md) 참고  
- 설정 가이드: [Set up Azure OpenAI](../set-up-resources/set-up-azure-openai.md)

**2. 선택 사항: 컴퓨터 비전 자격 증명 (이미지 번역용)**

- 이미지 내 텍스트를 번역해야 할 경우에만 필요  
- **Azure Computer Vision**: Endpoint와 구독 키 필요  
- 제공하지 않으면 액션이 [Markdown 전용 모드](../markdown-only-mode.md)로 동작  
- 설정 가이드: [Set up Azure Computer Vision](../set-up-resources/set-up-azure-computer-vision.md)

## 설정 및 구성

표준 `GITHUB_TOKEN`를 사용해 저장소에서 Co-op Translator GitHub Action을 설정하는 절차는 다음과 같습니다.

### 1단계: 인증 방식 이해하기 (`GITHUB_TOKEN` 사용)

이 워크플로우는 GitHub Actions에서 제공하는 내장 `GITHUB_TOKEN`를 사용합니다. 이 토큰은 3단계에서 설정한 권한에 따라 워크플로우가 저장소와 상호작용할 수 있도록 자동으로 권한을 부여합니다.

### 2단계: 저장소 시크릿 구성하기

저장소 설정에서 **AI 서비스 자격 증명**을 암호화된 시크릿으로 추가하기만 하면 됩니다.

1. 대상 GitHub 저장소로 이동  
2. **Settings** > **Secrets and variables** > **Actions**로 이동  
3. **Repository secrets** 아래에서 필요한 AI 서비스 시크릿마다 **New repository secret** 클릭

![Select setting action](../../../../getting_started/github-actions-guide/imgs/select-setting-action.png) *(이미지 참고: 시크릿 추가 위치)*

**필수 AI 서비스 시크릿 (사전 준비 사항에 따라 해당되는 모든 항목 추가):**

| 시크릿 이름                         | 설명                                  | 값 출처                          |
| :---------------------------------- | :----------------------------------- | :------------------------------ |
| `AZURE_SUBSCRIPTION_KEY`            | Azure AI 서비스 (컴퓨터 비전) 키            | Azure AI Foundry                 |
| `AZURE_AI_SERVICE_ENDPOINT`         | Azure AI 서비스 (컴퓨터 비전) 엔드포인트      | Azure AI Foundry                 |
| `AZURE_OPENAI_API_KEY`              | Azure OpenAI 서비스 키                     | Azure AI Foundry                 |
| `AZURE_OPENAI_ENDPOINT`             | Azure OpenAI 서비스 엔드포인트               | Azure AI Foundry                 |
| `AZURE_OPENAI_MODEL_NAME`           | Azure OpenAI 모델 이름                      | Azure AI Foundry                 |
| `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` | Azure OpenAI 배포 이름                      | Azure AI Foundry                 |
| `AZURE_OPENAI_API_VERSION`          | Azure OpenAI API 버전                       | Azure AI Foundry                 |
| `OPENAI_API_KEY`                    | OpenAI API 키                           | OpenAI 플랫폼                   |
| `OPENAI_ORG_ID`                     | OpenAI 조직 ID (선택 사항)                 | OpenAI 플랫폼                   |
| `OPENAI_CHAT_MODEL_ID`              | 특정 OpenAI 모델 ID (선택 사항)              | OpenAI 플랫폼                   |
| `OPENAI_BASE_URL`                   | 맞춤 OpenAI API 기본 URL (선택 사항)         | OpenAI 플랫폼                   |

### 3단계: 워크플로우 권한 구성하기

GitHub Action이 코드 체크아웃 및 풀 리퀘스트 생성을 위해 `GITHUB_TOKEN`를 통해 권한을 부여받아야 합니다.

1. 저장소에서 **Settings** > **Actions** > **General**로 이동  
2. 아래로 스크롤하여 **Workflow permissions** 섹션 찾기  
3. **Read and write permissions** 선택 — 이로써 `GITHUB_TOKEN`에 필요한 `contents: write`와 `pull-requests: write` 권한이 부여됩니다  
4. **Allow GitHub Actions to create and approve pull requests** 체크박스가 선택되어 있는지 확인  
5. **Save** 클릭

![Permission setting](../../../../getting_started/github-actions-guide/imgs/permission-setting.png)

### 4단계: 워크플로우 파일 생성하기

마지막으로, `GITHUB_TOKEN`를 사용해 자동화된 워크플로우를 정의하는 YAML 파일을 만듭니다.

1. 저장소 루트 디렉터리에 `.github/workflows/` 폴더가 없으면 생성  
2. `.github/workflows/` 폴더 안에 `co-op-translator.yml` 파일 생성  
3. 다음 내용을 `co-op-translator.yml`에 붙여넣기

```yaml
name: Co-op Translator

on:
  push:
    branches:
      - main

jobs:
  co-op-translator:
    runs-on: ubuntu-latest

    permissions:
      contents: write
      pull-requests: write

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      - name: Install Co-op Translator
        run: |
          python -m pip install --upgrade pip
          pip install co-op-translator

      - name: Run Co-op Translator
        env:
          PYTHONIOENCODING: utf-8
          # === AI Service Credentials ===
          AZURE_SUBSCRIPTION_KEY: ${{ secrets.AZURE_SUBSCRIPTION_KEY }}
          AZURE_AI_SERVICE_ENDPOINT: ${{ secrets.AZURE_AI_SERVICE_ENDPOINT }}
          AZURE_OPENAI_API_KEY: ${{ secrets.AZURE_OPENAI_API_KEY }}
          AZURE_OPENAI_ENDPOINT: ${{ secrets.AZURE_OPENAI_ENDPOINT }}
          AZURE_OPENAI_MODEL_NAME: ${{ secrets.AZURE_OPENAI_MODEL_NAME }}
          AZURE_OPENAI_CHAT_DEPLOYMENT_NAME: ${{ secrets.AZURE_OPENAI_CHAT_DEPLOYMENT_NAME }}
          AZURE_OPENAI_API_VERSION: ${{ secrets.AZURE_OPENAI_API_VERSION }}
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
          OPENAI_ORG_ID: ${{ secrets.OPENAI_ORG_ID }}
          OPENAI_CHAT_MODEL_ID: ${{ secrets.OPENAI_CHAT_MODEL_ID }}
          OPENAI_BASE_URL: ${{ secrets.OPENAI_BASE_URL }}
        run: |
          # =====================================================================
          # IMPORTANT: Set your target languages here (REQUIRED CONFIGURATION)
          # =====================================================================
          # Example: Translate to Spanish, French, German. Add -y to auto-confirm.
          translate -l "es fr de" -y  # <--- MODIFY THIS LINE with your desired languages

      - name: Create Pull Request with translations
        uses: peter-evans/create-pull-request@v5
        with:
          token: ${{ secrets.GITHUB_TOKEN }}
          commit-message: "🌐 Update translations via Co-op Translator"
          title: "🌐 Update translations via Co-op Translator"
          body: |
            This PR updates translations for recent changes to the main branch.

            ### 📋 Changes included
            - Translated contents are available in the `translations/` directory
            - Translated images are available in the `translated_images/` directory

            ---
            🌐 Automatically generated by the [Co-op Translator](https://github.com/Azure/co-op-translator) GitHub Action.
          branch: update-translations
          base: main
          labels: translation, automated-pr
          delete-branch: true
          add-paths: |
            translations/
            translated_images/
```  
4. **워크플로우 맞춤 설정:**  
  - **[!IMPORTANT] 대상 언어:** `Run Co-op Translator` step, you **MUST review and modify the list of language codes** within the `translate -l "..." -y` command to match your project's requirements. The example list (`ar de es...`) needs to be replaced or adjusted.
  - **Trigger (`on:`):** The current trigger runs on every push to `main`. For large repositories, consider adding a `paths:` filter (see commented example in the YAML) to run the workflow only when relevant files (e.g., source documentation) change, saving runner minutes.
  - **PR Details:** Customize the `commit-message`, `title`, `body`, `branch` name, and `labels` in the `Create Pull Request` 단계에서 필요에 따라 조정하세요.

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 노력하고 있으나, 자동 번역에는 오류나 부정확한 부분이 있을 수 있음을 유의하시기 바랍니다. 원본 문서는 해당 언어의 원문이 권위 있는 자료로 간주되어야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 본 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.