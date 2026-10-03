# 번역, 편집 및 작은 프로젝트 검토

짧은 Markdown 파일 두 개와 하나의 대상 언어로 시작하세요. 번역이 어디에 작성되는지, 소스가 변경될 때 어떤 일이 발생하는지, 결과를 확인하는 방법을 확인할 수 있습니다.

## 기록된 결과

이 예제는 2026년 9월 19일에 Co-op Translator 0.21.0과 Azure OpenAI (`gpt-5-mini`)로 실행되었습니다. 변경하지 않은 CLI 명령은 빌드된 wheel과 기존 Python 종속성을 사용하여 Click의 `CliRunner`를 통해 호출되었습니다.

| 단계 | 결과 |
| --- | --- |
| 미리보기 | Exit 0; 모델 번역 요청 없음 |
| 초기 번역 | Exit 0; 27.36초 |
| 초기 검토 | Exit 0 |
| README 편집 및 검토 | Exit 1; 오래된 번역 감지 |
| 번역 업데이트 | Exit 0; 22.17초 |
| 업데이트 후 검토 | Exit 0; 오류나 경고 없음 |
| 변경되지 않은 가이드 | README 업데이트 전후 바이트 동일함 |
| 다시 실행 | Exit 0; 모든 번역 파일의 해시 동일 |

이 수치는 개별 실행 측정값이며 성능 보증이 아닙니다. 설정 시간은 제외되었으며 제공자 비용 청구는 측정하지 않았습니다. 변경이 없는 실행도 제공자 상태 확인을 수행할 수 있습니다.

다음을 검사하세요: [초기 번역](../../assets/demo/before.txt), [업데이트된 번역](../../assets/demo/after.txt), [전체 번역 차이](../../assets/demo/update.diff), [오래된 검토](../../assets/demo/review-stale.txt), [최종 검토](../../assets/demo/review-after.txt), 및 [실행 세부정보](../../assets/demo/results.json). 전체 파일 번역은 캡처된 diff가 보여주듯 다른 문구를 변경할 수 있습니다. 두 텍스트 산출물 모두 생성된 면책 조항을 유지합니다.

사람의 검토는 여전히 중요합니다: 캡처된 업데이트에서는 `[사용 가이드](guide.md)을`로 표기되어 있는데, 한국어 조사로는 `[사용 가이드](guide.md)를`가 되어야 합니다. 텍스트 산출물은 이 출력을 그대로 유지하며 편집된 번역을 모델 출력으로 제시하지 않습니다. 구조적 검토는 이 문구 문제에도 불구하고 통과합니다.

## 1. 작은 폴더 준비하기

Python 3.11–3.14을 사용하고 [가상 환경 설정](configuration.md#local-runtime-setup)을 따르세요. 이 예제에서 사용된 버전을 설치하세요:

```bash
python -m pip install co-op-translator==0.21.0
mkdir translation-demo
cd translation-demo
git init
```

이 폴더에 [README.txt](../../assets/demo/README.txt)와 [guide.txt](../../assets/demo/guide.txt)를 다운로드하여 `README.md`와 `guide.md`로 저장하세요. 이것들은 작은 허구 프로젝트 문서이며 애플리케이션 설치는 필요하지 않습니다.

README에는 코드 블록과 `guide.md`로의 링크가 포함되어 있습니다. 마지막 문장은 다음과 같습니다:

```text
Notes are saved locally.
```

이 폴더에는 이 두 소스 문서만 남겨 두세요. 다음의 모든 명령은 `translation-demo` 내부에서 실행되며 Bash와 PowerShell에서 동작합니다.

## 2. 자격 증명 없이 미리보기

```bash
translate -l "ko" -md --dry-run
```

미리보기는 모델을 호출하거나 번역을 작성하지 않고 번역 작업량을 추정합니다. 토큰 추정치는 청구 견적이 아닙니다. 첫 실행에서는 두 Markdown 파일 모두를 새로운 작업으로 식별해야 합니다.

## 3. 제공자를 선택하고 번역하기

다음 [구성 가이드](configuration.md)를 사용하여 하나의 제공자를 구성하세요: Azure OpenAI, OpenAI, 또는 Anthropic. OpenAI와 Anthropic의 텍스트 번역은 Azure 계정이 필요하지 않습니다. 이 예제에는 이미지 서비스가 필요하지 않습니다.

로컬 `.env` 파일을 사용하는 경우 `.env`를 이 폴더의 `.gitignore`에 추가하세요. 번역 호출은 제공자 계정을 사용하며 요금이 발생할 수 있습니다.

```bash
translate -l "ko" -md
co-op-review -l "ko"
```

`translations/ko/README.md`와 `translations/ko/guide.md`를 엽니다. 한국어 표현, 코드 블록, 그리고 번역된 README에서 번역된 가이드로의 링크를 확인하세요. 출력 문구는 모델마다 다릅니다.

`co-op-review`는 최신성, 구조 및 로컬 링크를 검사합니다. 통과 결과가 언어적 정확성을 보증하지는 않습니다. 계속하기 전에 보고된 오류를 해결하세요.

필요한 경우 먼저 Git 정체성을 구성한 후 Git으로 성공한 기준 상태를 기록하세요:

```bash
git add README.md guide.md translations
git commit -m "Record initial Korean translation"
```

## 4. 소스 변경하기

`README.md`에서 `Notes are saved locally.`를 다음으로 바꾸세요:

```text
Notes are saved locally as Markdown files.
```

`guide.md`는 변경하지 마세요. 그런 다음 다음을 실행하세요:

```bash
co-op-review -l "ko"
translate -l "ko" -md --dry-run
```

검토는 README 번역이 오래되었다고 보고하고 비정상 종료해야 합니다. 이는 예상되는 중간 상태입니다. 미리보기는 변경된 README에 대한 작업을 식별해야 합니다.

## 5. 업데이트하고 차이를 검사하기

```bash
translate -l "ko" -md
git diff -- README.md translations/ko/README.md
git diff -- translations/ko/guide.md
co-op-review -l "ko"
```

실제 diff를 확인하세요: 기본 CLI는 변경된 파일을 재번역하므로 모델이 해당 파일의 다른 문구도 수정할 수 있습니다. 변경되지 않은 guide에는 차이가 없어야 합니다. 검토는 더 이상 README를 오래되었다고 보고하지 않아야 하며, 무시하지 말고 다른 발견 사항들을 조사하세요.

사람의 편집된 Markdown의 블록 수준 보존은 [Python API](api.md)에서 선택적 번역 상태 제공자가 필요합니다. 이는 이 CLI 명령들로 활성화되어 있지 않습니다.

## 6. 변경 없이 다시 실행하기

업데이트된 소스와 번역을 커밋하세요:

```bash
git add README.md translations
git commit -m "Update Korean translation after source edit"
translate -l "ko" -md
git diff --exit-code -- translations
```

현재 번역과 변경되지 않은 구성으로, 번역기는 파일을 건너뜁니다. 마지막 Git 명령은 차이를 생성하지 않고 정상 종료해야 합니다.

## 다음 단계

- [README만 번역하고 풀 리퀘스트 열기](github-actions.md#your-first-readme-translation-pr).
- [CLI, Python API, 또는 MCP 선택하기](workflows.md).
- [코딩 없이 번역 문제 보고하기](https://github.com/Azure/co-op-translator/issues/new?template=translation_feedback.yml).