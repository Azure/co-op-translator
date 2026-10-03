# 언어 개선 기여

귀하의 언어 지식은 Co-op Translator를 개선하는 데 도움이 될 수 있습니다. 예시, 제안된 수정안, 설명을 [번역 피드백 양식](https://github.com/Azure/co-op-translator/issues/new?template=translation_feedback.yml)으로 제출하세요. 코드 작성이나 모델 실행 비용은 필요하지 않습니다.

## 보고에서 공동 개선으로

1. 기여자는 원문 발췌, 번역본 및 맥락을 제공합니다.
2. 언어 검토자는 의미, 자연스러움, 그리고 제안이 특정 로케일 또는 과정에 의존하는지 여부를 확인합니다.
3. 유지 관리자는 수정 사항이 원본 과정, 공유 언어 지침, 용어 구성, 또는 번역 코드 중 어디에 속하는지 결정합니다.
4. 공유 규칙의 경우 유지 관리자는 보고된 예시와 관련 없는 예시들에 대해 변경 전후의 출력을 비교합니다. 기여자는 도구를 직접 실행하지 않고도 이 출력들을 검토할 수 있습니다.
5. 결과 PR은 보고서를 연결하고 예시와 검토를 제공한 사람들에게 공로를 표기합니다. 소비 저장소에서의 배포나 재생성은 별도의 단계입니다.

보고서는 자동으로 프롬프트를 변경하거나 과정 번역을 재생성하지 않습니다. 과정별 수정은 해당 과정 저장소와 연결된 상태로 남아 있어야 합니다. 수동 편집이 이후 재번역에서 유지될 것이라고 가정하지 말고 해당 워크플로우의 동작을 확인하세요.

## 기존 예시: 일본어 Markdown 링크

[일본어 지침 파일](https://github.com/Azure/co-op-translator/blob/main/src/co_op_translator/templates/language/ja.md)은 모델에게 링크 텍스트는 번역하되 Markdown 구문과 링크 목적지는 보존하도록 지시합니다. 예를 들어, `[text](URL)`로 작성된 링크는 `「text」（URL）`가 되어서는 안 됩니다.

이것은 올바른 출력과 잘못된 출력의 예로 뒷받침되는 언어 규칙의 집중된 예시입니다. 프롬프트 지침만으로 올바른 Markdown이 보장된다는 증거는 아닙니다.

[Markdown 프롬프트 빌더](https://github.com/Azure/co-op-translator/blob/main/src/co_op_translator/utils/markdown/prompts.py)는 소문자화하고 공백을 제거한 언어 코드를 사용하여 `templates/language/<language_code>.md`를 로드합니다. 파일이 없으면 공통 지침을 사용합니다. 이는 Markdown 프롬프트 경로를 설명하며 모든 이미지나 다른 번역 경로가 동일한 지침을 사용한다고 가정하지 마세요.

[프롬프트 테스트](https://github.com/Azure/co-op-translator/blob/main/tests/co_op_translator/utils/markdown/test_prompts.py)는 일본어 지침이 포함되어 있는지를 확인합니다. 이는 프롬프트 조립을 검증하는 것이며 번역 품질을 검증하는 것은 아닙니다.

## 언어 규칙에 포함되어야 할 것?

원문 예시, 기대 동작, 그리고 규칙이 적용되어서는 안 되는 반례를 포함한 좁고 반복 가능한 수정을 제안하세요. 의미, 플레이스홀더, 코드, URL, 문서 구조는 보존하세요. 한 사람의 스타일 선호나 특정 과정의 용어를 보편 규칙으로 만들지 마세요.

현재 [용어집 구현](https://github.com/Azure/co-op-translator/blob/main/src/co_op_translator/glossary.py)은 용어를 번역으로부터 보호합니다. 이는 소스-대상 용어 사전이 아닙니다. 기여자에게 약속하기 전에 새로운 용어 동작에 대해 논의하세요.

## 커뮤니티 예시: 일본어 제품명 보고서

[보고서 #527](https://github.com/Azure/co-op-translator/issues/527)에서 @hyoshioka0128은 제품명 `Co-op Translator`가 `Co-op 翻訳`로 변경된 일본어 번역을 확인했습니다. 보고서에는 영향받은 문서에 대한 링크와 스크린샷이 포함되어 있어 문제를 쉽게 찾아낼 수 있었습니다.

기여자는 또한 [관련 과정 PR](https://github.com/microsoft/AZD-for-beginners/pull/109)을 연결했습니다. 이슈 토론에서 유지 관리자는 보고서를 인정하고 용어 보호, 용어집 동작, 번역 경로 등을 포함하여 이름이 왜 변경되었는지 조사할 것을 제안했습니다.

이것은 작은 보고서 하나가 개별 문구 수정을 넘어 조사 지원을 어떻게 할 수 있는지를 보여줍니다. 이는 검증된 전후 결과나 위의 일본어 Markdown 링크 지침이 이 제품명 문제를 해결했다는 증거는 아닙니다.

같은 방식으로 기여할 수 있습니다: 원문, 현재 번역, 제안된 수정안, 그리고 왜 중요한지 공유하세요. 유용할 때 문서 링크나 스크린샷을 추가하세요. 보고하기 전에 원인 진단이나 프롬프트 작성은 필요하지 않습니다.

## 규칙 채택 전 검증

기준 실행과 후보 실행에 대해 동일한 원본 샘플, 번역기 수정본, 공급자/모델, 생성 설정을 사용하고 제안된 지침만 변경하세요. 실제 프롬프트 변경 사항과 출력을 기록하세요; 출력 변동성에서 일관된 효과를 구별하기 위해 필요하면 예시를 반복하세요. 보고된 실패, 대조되는 문맥, 이미 올바르게 번역되는 예시들을 포함하세요.

| Sample | Source/context | Baseline output | Candidate output | Reviewer assessment |
| --- | --- | --- | --- | --- |
| Reported failure | To collect | Not run | Not run | Pending |
| Counterexample | To collect | Not run | Not run | Pending |
| Unaffected example | To collect | Not run | Not run | Pending |

구조적 불변성은 언어적 판단과 별도로 확인하세요. 프롬프트 로딩 테스트의 성공은 품질 평가가 아니며, 하나의 정확한 예상 문장이 유일한 유효 번역은 아닙니다. 문맥, 모델 실행, 또는 언어 검토가 누락된 경우에는 문제가 해결되었다고 주장하기보다 제안을 보류 상태로 유지하세요.