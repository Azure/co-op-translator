# 작은 프로젝트 번역·수정·검토하기

짧은 Markdown 파일 두 개와 대상 언어 하나로 시작하세요. 번역 결과가 저장되는 위치, 원문이 바뀔 때의 동작, 결과를 검사하는 방법을 확인할 수 있습니다.

## 실제 실행 결과

이 예제는 2026년 9월 19일 Co-op Translator 0.21.0과 Azure OpenAI의 `gpt-5-mini`로 실행했습니다. 빌드한 wheel과 기존 Python 의존성을 사용했고, 수정하지 않은 CLI 명령을 Click의 `CliRunner`로 호출했습니다.

| 단계 | 결과 |
| --- | --- |
| 미리보기 | 종료 코드 0, 모델 번역 요청 없음 |
| 최초 번역 | 종료 코드 0, 27.36초 |
| 최초 검토 | 종료 코드 0 |
| README 수정 후 검토 | 종료 코드 1, 오래된 번역 감지 |
| 번역 갱신 | 종료 코드 0, 22.17초 |
| 갱신 후 검토 | 종료 코드 0, 오류·경고 없음 |
| 수정하지 않은 guide | README 갱신 전후 바이트가 동일함 |
| 변경 없이 재실행 | 종료 코드 0, 모든 번역 파일 해시가 동일함 |

한 번의 실행에서 측정한 결과이며 성능을 보장하는 수치는 아닙니다. 설정 시간은 제외했고 제공자 비용은 측정하지 않았습니다. 변경이 없는 실행에서도 제공자 연결 검사를 수행할 수 있습니다.

[최초 번역](../../assets/demo/before.txt), [갱신된 번역](../../assets/demo/after.txt), [전체 diff](../../assets/demo/update.diff), [오래된 번역 검사 결과](../../assets/demo/review-stale.txt), [최종 검사 결과](../../assets/demo/review-after.txt), [실행 기록](../../assets/demo/results.json)을 확인하세요. 파일 전체를 다시 번역하면 diff에서 보이듯 다른 문장도 바뀔 수 있습니다. 두 번역 결과에는 생성된 면책 문구가 그대로 남아 있습니다.

사람의 검토도 필요합니다. 실제 갱신 결과의 `[사용 가이드](guide.md)을`은 `[사용 가이드](guide.md)를`로 고쳐야 합니다. 결과 파일은 모델 출력을 사후 수정하지 않고 그대로 보여 줍니다. 이 문장 오류가 있어도 구조 검사는 통과했습니다.

## 1. 작은 폴더 준비하기

Python 3.11–3.14와 [가상 환경 설정](configuration.md#local-runtime-setup)을 사용하세요. 기록된 예제의 버전을 설치합니다.

```bash
python -m pip install co-op-translator==0.21.0
mkdir translation-demo
cd translation-demo
git init
```

[README.txt](../../assets/demo/README.txt)와 [guide.txt](../../assets/demo/guide.txt)를 이 폴더에 내려받아 각각 `README.md`, `guide.md`로 저장하세요. 가상의 프로젝트 문서이므로 별도의 앱 설치는 필요하지 않습니다.

README에는 코드 블록과 `guide.md` 링크가 있으며 마지막 문장은 다음과 같습니다.

```text
Notes are saved locally.
```

이 폴더에는 원본 문서 두 개만 두세요. 이후 명령은 모두 `translation-demo` 안에서 실행하며 Bash와 PowerShell에서 사용할 수 있습니다.

## 2. 자격 증명 없이 미리보기

```bash
translate -l "ko" -md --dry-run
```

모델을 호출하거나 번역 파일을 쓰지 않고 작업량을 추정합니다. 토큰 추정치는 청구 금액이 아닙니다. 첫 실행에서는 두 Markdown 파일이 모두 새 작업으로 표시되어야 합니다.

## 3. 제공자를 선택하고 번역하기

[설정 안내](configuration.md)에 따라 Azure OpenAI, OpenAI, Anthropic 중 하나를 설정하세요. OpenAI와 Anthropic의 텍스트 번역에는 Azure 계정이 필요하지 않습니다. 이 예제에는 이미지 서비스도 필요하지 않습니다.

로컬 `.env` 파일을 사용한다면 이 폴더의 `.gitignore`에 `.env`를 추가하세요. 실제 번역 호출은 제공자 계정을 사용하므로 비용이 발생할 수 있습니다.

```bash
translate -l "ko" -md
co-op-review -l "ko"
```

`translations/ko/README.md`와 `translations/ko/guide.md`를 열어 문장, 코드 블록, 번역된 가이드로 이동하는 링크를 확인하세요. 문장은 모델마다 달라집니다.

`co-op-review`는 원문 변경 여부, 구조, 로컬 링크를 검사합니다. 통과했다고 언어적 정확성이 보장되는 것은 아닙니다. 오류가 있다면 다음 단계로 넘어가기 전에 해결하세요.

성공한 결과를 Git에 기록하세요. 필요한 경우 먼저 Git 사용자 정보를 설정합니다.

```bash
git add README.md guide.md translations
git commit -m "Record initial Korean translation"
```

## 4. 원문 바꾸기

`README.md`에서 `Notes are saved locally.`를 다음 문장으로 바꾸세요.

```text
Notes are saved locally as Markdown files.
```

`guide.md`는 수정하지 않은 상태로 다음을 실행하세요.

```bash
co-op-review -l "ko"
translate -l "ko" -md --dry-run
```

검토 명령은 README 번역이 오래되었다고 보고하며 실패 코드로 끝나야 합니다. 이 단계에서는 예상된 결과입니다. 미리보기에는 변경된 README의 번역 작업이 표시되어야 합니다.

## 5. 번역을 갱신하고 diff 확인하기

```bash
translate -l "ko" -md
git diff -- README.md translations/ko/README.md
git diff -- translations/ko/guide.md
co-op-review -l "ko"
```

실제 diff를 살펴보세요. 기본 CLI는 원문이 바뀐 파일 전체를 다시 번역하므로 그 파일의 다른 문장도 달라질 수 있습니다. 수정하지 않은 가이드에는 diff가 없어야 합니다. 검토에서 README가 오래되었다는 오류가 사라져야 하며, 다른 결과가 있다면 원인을 확인하세요.

직접 수정한 Markdown 문장을 블록 단위로 보존하려면 [Python API의 번역 상태 제공자(영문)](../../api.md#preserve-accepted-human-edits-with-a-translation-state-provider)를 별도로 연결해야 합니다. 위 CLI 명령에는 이 기능이 활성화되어 있지 않습니다.

## 6. 변경 없이 다시 실행하기

갱신된 원문과 번역문을 커밋하세요.

```bash
git add README.md translations
git commit -m "Update Korean translation after source edit"
translate -l "ko" -md
git diff --exit-code -- translations
```

번역이 최신이고 설정이 같다면 해당 파일을 건너뜁니다. 마지막 Git 명령은 diff 없이 성공해야 합니다.

## 다음 단계

- [README 하나를 번역해 PR 만들기](github-actions.md#your-first-readme-translation-pr)
- [CLI, Python API, MCP 선택하기](workflows.md)
- [코딩 없이 번역 문제 제보하기](https://github.com/Azure/co-op-translator/issues/new?template=translation_feedback.yml)
