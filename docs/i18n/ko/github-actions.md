# GitHub Actions

저장소가 변경된 문서를 자동으로 번역하고 생성된 결과물로 풀 리퀘스트를 열도록 하려면 GitHub Actions를 사용하세요.

표준 `GITHUB_TOKEN` 설정으로 시작하세요(정책이 허용되는 조직 저장소의 경우도 포함). 조직에서 App 식별이 필요하거나 자동 하위 워크플로 실행이 필요한 경우 [GitHub App Setup](#github-app-setup)를 참조하세요.

**수동 편집:** 이 워크플로는 변경된 원본 파일을 전체 재번역하므로 번역에서 사람이 편집한 문구를 덮어쓸 수 있습니다. 병합 전에 각 PR을 검토하세요. 수락된 편집의 Markdown 블록 수준 보존은 [Python API translation state provider](api.md#preserve-accepted-human-edits-with-a-translation-state-provider)와의 맞춤 통합이 필요합니다.

## 첫 README 번역 PR

루트 `README.md` 하나와 대상 언어 하나로 시작하세요. 이 워크플로는 Markdown만 번역하므로 Azure AI Vision은 필요하지 않습니다.

1. 번역하려는 저장소의 `.github/workflows/translate-readme.yml`에 [translate-readme.yml](../../assets/workflows/translate-readme.yml) ([템플릿을 GitHub에서 보기](https://github.com/Azure/co-op-translator/blob/main/docs/assets/workflows/translate-readme.yml))을 복사하고 해당 저장소의 기본 브랜치에 커밋하세요. 템플릿은 `Azure/co-op-translator@main`의 루트 Action을 사용하며, 동일한 소스 ref에서 CLI를 설치합니다. 재현 가능한 실행을 위해 검토된 커밋을 고정하세요.
2. <strong>Actions > Translate README > Run workflow</strong>를 열고 언어를 선택한 다음 <strong>Preview only</strong>를 체크된 상태로 두세요. 미리 보기 단계에서 토큰 추정치를 검토하세요. 미리보기는 모델 제공자를 호출하지 않으며 번역을 기록하거나 PR을 생성하지 않습니다.
3. 하나의 [텍스트 제공자](#prerequisites)에 대한 시크릿을 추가하고 <strong>설정 > 작업 > 일반</strong>에서 <strong>GitHub Actions가 풀 리퀘스트를 생성하고 승인하도록 허용</strong>을 활성화하세요. 템플릿은 작업에 대해 `contents: write` 및 `pull-requests: write`를 요청하며, 모든 워크플로의 기본 권한을 변경할 필요는 없습니다. 조직 정책이 이러한 권한이나 설정을 차단하는 경우 승인된 [GitHub 앱](#github-app-setup)에 대해 관리자에게 문의하세요.
4. <strong>Preview only</strong>의 체크를 해제하고 워크플로를 다시 실행하세요. 그러면 미리보기, 번역, `co-op-review --readme-only` 실행을 거쳐 번역 및 검토가 성공한 경우에만 번역 PR을 생성하거나 업데이트합니다. 워크플로 요약에는 PR 링크가 포함됩니다.
5. PR에서 문구와 파일 변경 사항을 검토한 후 준비되면 병합하세요. 이 워크플로는 자동으로 병합하지 않습니다.

PR에는 `translations/<language>/README.md`와 해당 언어 메타데이터 파일만 포함됩니다. 원본 README는 변경되지 않으며 다른 문서로의 링크는 계속 원본 문서를 가리킵니다. PR 본문에는 변경된 파일과 구조적 검토 결과가 나열됩니다. 번역이나 검토가 실패하면 워크플로 요약과 실패한 단계의 로그를 확인하세요; PR은 생성되지 않습니다. 변경 사항이 없으면 새 PR이 필요하지 않습니다.

**Organization and CI note:** GitHub App은 선택 사항이며 조직 소유의 필수 조건이 아닙니다. `GITHUB_TOKEN`을 사용하는 경우 PR을 열거나 업데이트하거나 다시 열기 위한 풀 리퀘스트 워크플로는 쓰기 권한이 있는 사용자가 <strong>Approve workflows to run</strong>를 선택해야 합니다. 푸시 워크플로는 이 토큰으로 트리거되지 않습니다. 무인 하위 CI에 대해서는 [GitHub App Setup](#github-app-setup) 및 GitHub의 [workflow triggering rules](https://docs.github.com/en/actions/how-tos/writing-workflows/choosing-when-your-workflow-runs/triggering-a-workflow)을 참조하세요.

## Prerequisites

워크플로를 생성하기 전에 번역 실행에 필요한 AI 서비스 시크릿을 구성하세요.

텍스트 번역에는 하나의 언어 모델 공급자가 필요합니다:

- Azure OpenAI: `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_MODEL_NAME`, `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME`, `AZURE_OPENAI_API_VERSION`
- OpenAI: `OPENAI_API_KEY`, `OPENAI_CHAT_MODEL_ID`, plus optional `OPENAI_ORG_ID` and `OPENAI_BASE_URL`
- Anthropic: `ANTHROPIC_API_KEY`, `ANTHROPIC_MODEL`, plus optional `ANTHROPIC_BASE_URL`

이미지 번역에는 추가로 Azure AI Vision이 필요합니다:

- `AZURE_AI_SERVICE_API_KEY`
- `AZURE_AI_SERVICE_ENDPOINT`

로컬 구성 세부정보는 [Configuration](configuration.md) 및 [Azure AI Setup](azure-ai-setup.md)을 참조하세요.

## 표준 설정

README 워크플로를 시도한 후, 이 설정을 사용하여 저장소의 Markdown 파일을 여러 언어로 번역하세요. PR을 열기 전에 Markdown 검토를 실행하며 Azure AI Vision은 필요하지 않습니다.

### 1단계: 리포지토리 시크릿 추가

대상 저장소에서 **Settings** > **Secrets and variables** > <strong>Actions</strong>를 열고 워크플로가 사용할 제공자 시크릿을 추가하세요.

![Actions 시크릿 선택](../../assets/github-actions/select-setting-action.png)

### 2단계: 워크플로 권한 활성화

**Settings** > **Actions** > <strong>General</strong>를 여세요.

Under **Workflow permissions**:

1. <strong>GitHub Actions가 풀 리퀘스트를 생성하고 승인하도록 허용</strong>을 활성화하세요.
2. 설정을 저장하세요.

아래 작업은 `contents: write` 및 `pull-requests: write`를 명시적으로 요청합니다. 저장소의 기본 워크플로 권한은 변경하지 마세요. 조직 정책이 PR 생성을 차단하면 승인된 [GitHub App](#github-app-setup)에 대해 관리자에게 문의하세요.

### 3단계: 워크플로 추가

Create `.github/workflows/co-op-translator.yml`:

```yaml
name: Co-op Translator

on:
  push:
    branches:
      - main

jobs:
  co-op-translator:
    runs-on: ubuntu-latest
    env:
      TARGET_LANGUAGES: "es fr de"

    permissions:
      contents: write
      pull-requests: write

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Set up Python
        uses: actions/setup-python@v7
        with:
          python-version: "3.11"

      - name: Install Co-op Translator
        run: |
          python -m pip install --upgrade pip
          pip install co-op-translator

      - name: Run Co-op Translator
        env:
          PYTHONIOENCODING: utf-8
          AZURE_OPENAI_API_KEY: ${{ secrets.AZURE_OPENAI_API_KEY }}
          AZURE_OPENAI_ENDPOINT: ${{ secrets.AZURE_OPENAI_ENDPOINT }}
          AZURE_OPENAI_MODEL_NAME: ${{ secrets.AZURE_OPENAI_MODEL_NAME }}
          AZURE_OPENAI_CHAT_DEPLOYMENT_NAME: ${{ secrets.AZURE_OPENAI_CHAT_DEPLOYMENT_NAME }}
          AZURE_OPENAI_API_VERSION: ${{ secrets.AZURE_OPENAI_API_VERSION }}
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
          OPENAI_ORG_ID: ${{ secrets.OPENAI_ORG_ID }}
          OPENAI_CHAT_MODEL_ID: ${{ secrets.OPENAI_CHAT_MODEL_ID }}
          OPENAI_BASE_URL: ${{ secrets.OPENAI_BASE_URL }}
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
          ANTHROPIC_MODEL: ${{ secrets.ANTHROPIC_MODEL }}
          ANTHROPIC_BASE_URL: ${{ secrets.ANTHROPIC_BASE_URL }}
        run: |
          translate -l "$TARGET_LANGUAGES" -md -y

      - name: Review Markdown translations
        run: |
          python - <<'PY'
          import os
          from co_op_translator.api import run_review

          run_review(
              language_codes=os.environ["TARGET_LANGUAGES"].split(),
              markdown=True,
              notebook=False,
              output_format="github",
          )
          PY

      - name: Create Pull Request with translations
        uses: peter-evans/create-pull-request@v5
        with:
          token: ${{ secrets.GITHUB_TOKEN }}
          commit-message: "Update translations via Co-op Translator"
          title: "Update translations via Co-op Translator"
          body: |
            This PR updates translations for recent changes to the main branch.
            Markdown structure, freshness, and local links were reviewed.
            Review translation wording before merging.

            Generated by Co-op Translator.
          branch: update-translations
          base: main
          labels: translation, automated-pr
          delete-branch: true
          add-paths: |
            translations/
```

프로젝트에 필요한 언어로 `TARGET_LANGUAGES`를 변경하세요. 검토는 번역 단계와 일치하게 Markdown만 확인하도록 Python API를 사용합니다. 번역 또는 검토 오류는 PR 생성 전에 작업을 중단합니다. 이 워크플로는 PR을 자동으로 병합하지 않습니다. 대규모 저장소의 경우 `on.push` 아래에 `paths:` 필터를 추가하여 문서가 변경될 때만 워크플로가 실행되도록 하세요.

### 선택 사항: 노트북 및 이미지

노트북의 경우 번역 명령에 `-nb`를 추가하고 검토 단계에서 `notebook=True`로 설정하세요. 이미지 텍스트의 경우 두 개의 [Azure AI Vision 시크릿](#prerequisites)을 구성하고 번역 단계의 `env`에 전달하며 명령에 `-img`를 추가하고 PR 단계의 `add-paths`에 `translated_images/`를 추가하세요. 번역된 이미지는 시각적으로 검토하세요; 결정론적 리뷰는 이미지 텍스트나 언어적 정확성을 보증하지 않습니다.

## GitHub 앱 설정

조직에서 App 식별이 필요하거나 생성된 PR이 `GITHUB_TOKEN` 승인 단계 없이 하위 CI를 트리거해야 하는 경우 승인된 GitHub App을 사용하세요. App이 조직 정책을 우회하지는 않으며 설치 및 권한은 여전히 관리자에 의해 제어됩니다.

### 1단계: GitHub 앱 생성 또는 설치

가능하면 기존 조직에서 제공한 App을 사용하거나 <strong>Contents</strong>와 <strong>Pull requests</strong>에 대한 읽기/쓰기 액세스 권한을 가진 App을 생성하세요. 필요한 조직 승인을 받아 대상 저장소에 설치하세요.

Record:

- 앱 ID
- 개인 키 내용

이를 저장소 시크릿으로 저장하세요:

- `GH_APP_ID`
- `GH_APP_PRIVATE_KEY`

### 2단계: 앱 토큰 생성

기존 풀 리퀘스트 단계 바로 전에 이 단계를 추가하세요. README 템플릿의 경우 동일한 성공 조건을 사용하여 미리보기와 실패한 번역이 App 토큰을 요청하지 않도록 하세요:

```yaml
      - name: Authenticate GitHub App
        id: generate_token
        if: ${{ !inputs.preview && steps.translate.outcome == 'success' && steps.review.outcome == 'success' }}
        uses: actions/create-github-app-token@v2
        with:
          app-id: ${{ secrets.GH_APP_ID }}
          private-key: ${{ secrets.GH_APP_PRIVATE_KEY }}
          permission-contents: write
          permission-pull-requests: write
```

그런 다음 기존 풀 리퀘스트 단계의 `token` 입력만 `${{ steps.generate_token.outputs.token }}`로 변경하세요. 성공 조건, 브랜치, PR 본문 및 `add-paths`는 변경하지 마세요. 토큰은 기본적으로 현재 저장소로 범위가 지정됩니다. README 템플릿 대신 표준 설정을 적용할 때는 위의 `if`를 생략하세요: 해당 워크플로는 기본 성공 조건을 사용하므로 토큰 생성과 PR 생성은 번역 및 검토가 성공한 후에만 실행됩니다.

설치 및 토큰 권한에 대해서는 공식 [create-github-app-token Action](https://github.com/actions/create-github-app-token/tree/v2)을 참조하세요.

## 러너 제한

GitHub 호스팅 러너에는 작업 최대 실행 시간이 있습니다. 대규모 저장소나 대상 언어가 많으면 해당 한도를 초과할 수 있습니다.

For large translation workloads:

- 한 실행당 번역하는 언어 수를 줄이세요.
- `-md`, `-nb`, 또는 `-img`와 같은 콘텐츠 플래그를 사용하세요.
- 저장소 크기나 모델 지연으로 호스팅 러너가 신뢰할 수 없는 경우 self-hosted 러너를 사용하세요.

## CI에서 검토

풀 리퀘스트가 LLM 또는 Vision 제공자를 호출하지 않고 생성된 번역을 검증해야 할 때 `co-op-review`를 사용하세요.

```yaml
      - name: Review translated outputs
        run: |
          co-op-review --changed-from "origin/${{ github.base_ref }}" --format github
```

`co-op-review`는 베타 결정론적 검토 명령입니다. 그 검사와 출력 스키마는 변경될 수 있지만, 파일을 쓰거나 모델 제공자를 호출하지 않기 때문에 CI에 안전하도록 설계되었습니다.