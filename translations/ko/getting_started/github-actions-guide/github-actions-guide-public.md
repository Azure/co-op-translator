<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a52587a512e667f70d92db853d3c61d5",
  "translation_date": "2025-07-03T07:13:08+00:00",
  "source_file": "getting_started/github-actions-guide/github-actions-guide-public.md",
  "language_code": "ko"
}
-->
# Co-op Translator GitHub Action 사용하기 (공개 설정)

**대상 독자:** 이 가이드는 표준 GitHub Actions 권한이 충분한 대부분의 공개 또는 비공개 저장소의 사용자를 위한 것입니다. 내장된 `GITHUB_TOKEN`을 사용합니다.

Co-op Translator GitHub Action을 사용하여 저장소의 문서를 자동으로 번역하세요. 이 가이드는 소스 Markdown 파일이나 이미지가 변경될 때마다 업데이트된 번역으로 자동으로 풀 요청을 생성하는 액션 설정 방법을 안내합니다.

> [!IMPORTANT]
>
> **올바른 가이드 선택:**
>
> 이 가이드는 **표준 `GITHUB_TOKEN`을 사용하는 간단한 설정**을 설명합니다. 이는 민감한 GitHub App Private Keys를 관리할 필요가 없기 때문에 대부분의 사용자에게 권장되는 방법입니다.
>

## 사전 준비

GitHub Action을 구성하기 전에 필요한 AI 서비스 자격 증명을 준비하세요.

**1. 필수: AI 언어 모델 자격 증명**
지원되는 언어 모델에 대한 자격 증명이 필요합니다:

- **Azure OpenAI**: Endpoint, API Key, 모델/배포 이름, API 버전이 필요합니다.
- **OpenAI**: API Key가 필요합니다. (선택 사항: Org ID, Base URL, 모델 ID)
- 자세한 내용은 [지원되는 모델 및 서비스](../../../../README.md)를 참조하세요.

**2. 선택 사항: AI Vision 자격 증명 (이미지 번역용)**

- 이미지 내 텍스트를 번역해야 하는 경우에만 필요합니다.
- **Azure AI Vision**: Endpoint와 Subscription Key가 필요합니다.
- 제공되지 않으면 액션은 [Markdown-only 모드](../markdown-only-mode.md)로 기본 설정됩니다.

## 설정 및 구성

표준 `GITHUB_TOKEN`을 사용하여 저장소에서 Co-op Translator GitHub Action을 구성하는 단계를 따르세요.

### Step 1: 인증 이해하기 (`GITHUB_TOKEN` 사용)

이 워크플로는 GitHub Actions에서 제공하는 내장된 `GITHUB_TOKEN`을 사용합니다. 이 토큰은 **Step 3**에서 구성된 설정에 따라 저장소와 상호작용할 수 있는 권한을 워크플로에 자동으로 부여합니다.

### Step 2: 저장소 비밀 구성

저장소 설정에서 암호화된 비밀로 **AI 서비스 자격 증명**만 추가하면 됩니다.

1.  대상 GitHub 저장소로 이동합니다.
2.  **Settings** > **Secrets and variables** > **Actions**로 이동합니다.
3.  **Repository secrets** 아래에서 아래에 나열된 각 필수 AI 서비스 비밀에 대해 **New repository secret**을 클릭합니다.

    ![Select setting action](../../../../translated_images/select-setting-action.3b95c915d60311592ca51ecb91b3a7bbe0ae45438a2ee872c1520dc90b677780.ko.png) *(이미지 참조: 비밀을 추가하는 위치를 보여줌)*

**필수 AI 서비스 비밀 (사전 준비에 따라 적용되는 모든 항목 추가):**

| 비밀 이름                           | 설명                                     | 값 출처                          |
| :---------------------------------- | :---------------------------------------- | :------------------------------- |
| `AZURE_SUBSCRIPTION_KEY`            | Azure AI 서비스 (Computer Vision) 키      | Azure AI Foundry                 |
| `AZURE_AI_SERVICE_ENDPOINT`         | Azure AI 서비스 (Computer Vision) 엔드포인트 | Azure AI Foundry                 |
| `AZURE_OPENAI_API_KEY`              | Azure OpenAI 서비스 키                   | Azure AI Foundry                 |
| `AZURE_OPENAI_ENDPOINT`             | Azure OpenAI 서비스 엔드포인트           | Azure AI Foundry                 |
| `AZURE_OPENAI_MODEL_NAME`           | Azure OpenAI 모델 이름                   | Azure AI Foundry                 |
| `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` | Azure OpenAI 배포 이름                   | Azure AI Foundry                 |
| `AZURE_OPENAI_API_VERSION`          | Azure OpenAI API 버전                    | Azure AI Foundry                 |
| `OPENAI_API_KEY`                    | OpenAI API 키                            | OpenAI Platform                  |
| `OPENAI_ORG_ID`                     | OpenAI 조직 ID (선택 사항)               | OpenAI Platform                  |
| `OPENAI_CHAT_MODEL_ID`              | 특정 OpenAI 모델 ID (선택 사항)          | OpenAI Platform                  |
| `OPENAI_BASE_URL`                   | 사용자 정의 OpenAI API 기본 URL (선택 사항) | OpenAI Platform                  |

### Step 3: 워크플로 권한 구성

GitHub Action은 코드 체크아웃 및 풀 요청 생성을 위해 `GITHUB_TOKEN`을 통해 권한이 필요합니다.

1.  저장소에서 **Settings** > **Actions** > **General**로 이동합니다.
2.  **Workflow permissions** 섹션으로 스크롤합니다.
3.  **Read and write permissions**을 선택합니다. 이는 이 워크플로에 필요한 `contents: write` 및 `pull-requests: write` 권한을 `GITHUB_TOKEN`에 부여합니다.
4.  **Allow GitHub Actions to create and approve pull requests** 체크박스가 **체크됨**을 확인합니다.
5.  **Save**를 선택합니다.

![Permission setting](../../../../translated_images/permission-setting.ae2f02748b0579e7dc3633f14dad67005b533ea8f69890818857de058089a7f5.ko.png)

### Step 4: 워크플로 파일 생성

마지막으로, `GITHUB_TOKEN`을 사용하여 자동화된 워크플로를 정의하는 YAML 파일을 생성합니다.

1.  저장소의 루트 디렉토리에 `.github/workflows/` 디렉토리를 생성합니다. 존재하지 않는 경우.
2.  `.github/workflows/` 내에 `co-op-translator.yml`이라는 파일을 생성합니다.
3.  아래 내용을 `co-op-translator.yml`에 붙여넣습니다.

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
4.  **워크플로 맞춤화:**
  - **[!IMPORTANT] 대상 언어:** `Run Co-op Translator` 단계에서 `translate -l "..." -y` 명령어 내의 언어 코드 목록을 검토하고 프로젝트 요구 사항에 맞게 수정해야 합니다. 예제 목록 (`ar de es...`)은 교체하거나 조정해야 합니다.
  - **트리거 (`on:`):** 현재 트리거는 `main`에 대한 모든 푸시에서 실행됩니다. 대규모 저장소의 경우 관련 파일(예: 소스 문서)이 변경될 때만 워크플로가 실행되도록 `paths:` 필터를 추가하여 러너 시간을 절약하는 것을 고려하세요.
  - **PR 세부사항:** 필요에 따라 `Create Pull Request` 단계에서 `commit-message`, `title`, `body`, `branch` 이름 및 `labels`를 맞춤화하세요.

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 우리는 정확성을 위해 노력하지만, 자동 번역에는 오류나 부정확성이 있을 수 있음을 유의하시기 바랍니다. 원본 문서는 해당 언어로 작성된 것이 권위 있는 출처로 간주되어야 합니다. 중요한 정보에 대해서는 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 책임을 지지 않습니다.