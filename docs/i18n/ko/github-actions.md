# GitHub Actions

원문이 변경되면 자동으로 문서를 번역하고 결과를 풀 리퀘스트(PR)로 검토하려면 GitHub Actions를 사용하세요.

조직 정책에서 허용한다면 조직 저장소도 기본 `GITHUB_TOKEN`으로 시작할 수 있습니다. 조직에서 앱 ID를 요구하거나 후속 CI를 자동 실행해야 한다면 [GitHub App 설정](#github-app-setup)을 참고하세요.

**사람이 수정한 번역문:** 이 워크플로는 원문이 변경된 파일 전체를 다시 번역하므로 직접 다듬은 문장이 덮어써질 수 있습니다. PR을 병합하기 전에 변경 내용을 검토하세요. 변경되지 않은 Markdown 블록의 수정 사항을 보존하려면 [Python API의 번역 상태 제공자(영문)](../../api.md#preserve-accepted-human-edits-with-a-translation-state-provider)를 연결한 별도 통합이 필요합니다.

<a id="your-first-readme-translation-pr"></a>

## 첫 README 번역 PR 만들기

루트의 `README.md` 하나와 대상 언어 하나로 시작하세요. Markdown만 번역하므로 Azure AI Vision은 필요하지 않습니다.

1. [translate-readme.yml](../../assets/workflows/translate-readme.yml)을 번역할 저장소의 `.github/workflows/translate-readme.yml`에 복사하고 기본 브랜치에 커밋하세요. 다운로드가 어려우면 [GitHub에서 템플릿 보기](https://github.com/Azure/co-op-translator/blob/main/docs/assets/workflows/translate-readme.yml)를 사용하세요. 템플릿은 `Azure/co-op-translator@main`의 루트 Action을 사용하고 같은 소스 ref에서 CLI를 설치합니다. 재현 가능한 실행에는 검토한 커밋을 고정하세요.
2. **Actions > Translate README > Run workflow**에서 언어를 선택하고 **Preview only**를 체크한 상태로 실행하세요. 미리보기 단계에서 토큰 추정치를 확인합니다. 이 단계는 제공자를 호출하거나 번역 파일과 PR을 만들지 않습니다.
3. [텍스트 제공자 하나의 시크릿](#prerequisites)을 추가하고, **Settings > Actions > General**에서 **Allow GitHub Actions to create and approve pull requests**를 켜세요. 템플릿은 작업에 `contents: write`, `pull-requests: write`를 명시하므로 저장소 전체의 기본 워크플로 권한을 바꿀 필요는 없습니다. 조직 정책에서 막혀 있다면 관리자에게 승인된 [GitHub App](#github-app-setup)을 문의하세요.
4. **Preview only**를 해제하고 다시 실행하세요. 미리보기, 번역, `co-op-review --readme-only` 검사를 진행하고, 번역과 검토가 성공한 경우에만 PR을 만들거나 갱신합니다. 실행 요약에서 PR 링크를 확인할 수 있습니다.
5. PR의 문장과 파일 변경을 검토한 뒤 준비되면 병합하세요. 자동 병합은 하지 않습니다.

PR에는 `translations/<language>/README.md`와 해당 언어의 메타데이터 파일만 포함됩니다. 원본 README는 유지되며 다른 문서의 링크는 원본 문서를 가리킵니다. PR 본문에서 변경 파일과 구조 검사 결과를 확인하세요. 번역이나 검토가 실패하면 PR을 만들지 않으므로 실행 요약과 실패한 단계의 로그를 확인하세요. 변경 내용이 없다면 새 PR은 필요하지 않습니다.

**조직과 CI:** 조직 소유 저장소라는 이유만으로 GitHub App이 필요한 것은 아닙니다. `GITHUB_TOKEN`으로 생성·갱신·재개한 PR의 워크플로는 쓰기 권한이 있는 사용자가 **Approve workflows to run**을 선택해야 실행됩니다. 이 토큰의 push는 push 워크플로를 실행하지 않습니다. 무인 후속 CI가 필요하다면 [GitHub App 설정](#github-app-setup)과 GitHub의 [워크플로 실행 규칙](https://docs.github.com/en/actions/how-tos/writing-workflows/choosing-when-your-workflow-runs/triggering-a-workflow)을 참고하세요.

<a id="prerequisites"></a>

## 준비 사항

텍스트 번역에는 아래 제공자 중 하나의 시크릿이 필요합니다.

- Azure OpenAI: `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_MODEL_NAME`, `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME`, `AZURE_OPENAI_API_VERSION`
- OpenAI: `OPENAI_API_KEY`, `OPENAI_CHAT_MODEL_ID`. `OPENAI_ORG_ID`, `OPENAI_BASE_URL`은 필요한 경우에만 추가합니다.
- Anthropic: `ANTHROPIC_API_KEY`, `ANTHROPIC_MODEL`. `ANTHROPIC_BASE_URL`은 필요한 경우에만 추가합니다.

이미지 번역을 추가할 때만 `AZURE_AI_SERVICE_API_KEY`, `AZURE_AI_SERVICE_ENDPOINT`가 필요합니다. 자세한 설정은 [설정 안내](configuration.md)와 [Azure AI 설정](azure-ai-setup.md)을 참고하세요.

<a id="standard-setup"></a>

## 표준 설정

README 워크플로를 시도한 뒤 저장소의 Markdown 파일을 여러 언어로 번역할 때 사용하세요. PR 생성 전에 Markdown 검토를 실행하며 Azure AI Vision은 필요하지 않습니다.

### 1. 저장소 시크릿 추가

대상 저장소의 **Settings > Secrets and variables > Actions**에서 사용할 제공자의 시크릿을 추가하세요.

![Actions 시크릿 선택](../../assets/github-actions/select-setting-action.png)

### 2. PR 생성 허용

**Settings > Actions > General**의 **Workflow permissions**에서 **Allow GitHub Actions to create and approve pull requests**를 켜고 저장하세요.

아래 작업은 `contents: write`, `pull-requests: write`를 명시합니다. 저장소의 기본 워크플로 권한은 그대로 두세요. 조직 정책으로 PR 생성이 제한되어 있다면 관리자에게 승인된 [GitHub App](#github-app-setup)을 문의하세요.

### 3. 워크플로 추가

`.github/workflows/co-op-translator.yml`을 만드세요.

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

`TARGET_LANGUAGES`를 원하는 언어로 바꾸세요. 검토 단계는 번역 범위에 맞춰 Python API로 Markdown만 검사합니다. 번역이나 검토에 오류가 있으면 PR 생성 전에 작업이 중단됩니다. PR은 자동 병합되지 않습니다. 큰 저장소는 `on.push` 아래에 `paths:` 필터를 추가해 문서 변경 시에만 실행되도록 설정할 수 있습니다.

### 선택 사항: 노트북과 이미지

노트북은 번역 명령에 `-nb`를 추가하고 검토 단계에 `notebook=True`를 설정하세요. 이미지 안의 텍스트는 [Azure AI Vision 시크릿](#prerequisites) 두 개를 설정하고 번역 단계의 `env`에 전달한 뒤, 명령에 `-img`, PR의 `add-paths`에 `translated_images/`를 추가하세요. 이미지와 문장 품질은 사람이 직접 확인해야 합니다. 결정적 검사는 번역의 언어적 정확성을 보장하지 않습니다.

<a id="github-app-setup"></a>

## GitHub App 설정

조직에서 앱 ID를 요구하거나 생성한 PR의 후속 CI를 `GITHUB_TOKEN` 승인 단계 없이 실행해야 할 때 승인된 GitHub App을 사용하세요. 앱 설치와 권한은 조직 관리자의 정책을 따릅니다.

### 1. 앱 생성 또는 설치

가능하면 조직에서 제공하는 앱을 사용하세요. 새 앱은 **Contents**와 **Pull requests**의 읽기/쓰기 권한이 필요합니다. 대상 저장소에 앱을 설치하고 필요한 조직 승인을 받으세요. 앱 ID와 개인 키 내용을 각각 `GH_APP_ID`, `GH_APP_PRIVATE_KEY` 저장소 시크릿에 저장합니다.

### 2. 앱 토큰 생성

기존 PR 생성 단계 바로 앞에 다음 단계를 추가하세요. README 템플릿에서는 같은 성공 조건을 적용해 미리보기나 실패한 실행에서 앱 토큰을 요청하지 않도록 합니다.

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

기존 PR 생성 단계의 `token`만 `${{ steps.generate_token.outputs.token }}`으로 바꾸세요. 성공 조건, 브랜치, PR 본문, `add-paths`는 유지합니다. 토큰은 기본적으로 현재 저장소에 한정됩니다. 표준 설정에 적용할 때는 위의 `if`를 생략하세요. 표준 설정은 기본 성공 조건으로 동작하므로 번역과 검토가 성공한 뒤에만 토큰과 PR을 생성합니다.

자세한 권한은 [create-github-app-token Action](https://github.com/actions/create-github-app-token/tree/v2)을 참고하세요.

## 실행 시간 제한

GitHub 호스팅 실행기에는 최대 작업 시간이 있습니다. 큰 저장소나 많은 언어를 처리하면 제한을 넘을 수 있습니다.

- 실행당 언어 수를 줄이세요.
- `-md`, `-nb`, `-img`로 콘텐츠 유형을 지정하세요.
- 저장소 크기나 모델 응답 시간 때문에 작업이 자주 중단된다면 자체 실행기를 고려하세요.

## CI에서 검토

제공자 호출 없이 PR의 번역 결과를 검사하려면 `co-op-review`를 사용하세요.

```yaml
      - name: Review translated outputs
        run: |
          co-op-review --changed-from "origin/${{ github.base_ref }}" --format github
```

`co-op-review`는 베타 단계의 결정적 검사 명령입니다. 검사 항목과 출력 형식은 변경될 수 있지만 파일을 쓰거나 LLM·Vision 제공자를 호출하지 않습니다.
