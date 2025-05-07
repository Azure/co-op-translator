<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b38d8f042530a4bc872def7cb2c141cd",
  "translation_date": "2025-05-06T17:40:27+00:00",
  "source_file": "getting_started/command-reference.md",
  "language_code": "ko"
}
-->
# 명령어 참고
**Co-op Translator** CLI는 번역 과정을 맞춤 설정할 수 있는 여러 옵션을 제공합니다:

명령어                                       | 설명
----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"                 | 프로젝트를 지정한 언어로 번역합니다. 예: translate -l "es fr de"는 스페인어, 프랑스어, 독일어로 번역합니다. translate -l "all"을 사용하면 지원하는 모든 언어로 번역합니다.
translate -l "language_codes" -u              | 기존 번역을 삭제하고 다시 생성하여 번역을 업데이트합니다. 경고: 지정한 언어의 모든 기존 번역이 삭제됩니다.
translate -l "language_codes" -img            | 이미지 파일만 번역합니다.
translate -l "language_codes" -md             | 마크다운 파일만 번역합니다.
translate -l "language_codes" -chk            | 번역된 파일에 오류가 있는지 검사하고 필요 시 번역을 다시 시도합니다.
translate -l "language_codes" -d              | 자세한 로그를 위한 디버그 모드를 활성화합니다.
translate -l "language_codes" -r "root_dir"   | 프로젝트의 루트 디렉터리를 지정합니다.
translate -l "language_codes" -f              | 이미지 번역에 빠른 모드를 사용합니다 (품질과 정렬에 약간 영향을 주지만 최대 3배 빠른 처리 속도).
translate -l "language_codes" -y              | 모든 프롬프트를 자동으로 승인합니다 (CI/CD 파이프라인에 유용).
translate -l "language_codes" --help          | 사용 가능한 명령어에 대한 도움말을 CLI 내에서 보여줍니다.

### 사용 예시:

  1. 기본 동작 (기존 번역을 삭제하지 않고 새 번역만 추가):   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. 새로운 한국어 이미지 번역만 추가 (기존 번역은 삭제하지 않음):    translate -l "ko" -img

  3. 모든 한국어 번역 업데이트 (경고: 기존 한국어 번역을 모두 삭제 후 다시 번역):    translate -l "ko" -u

  4. 한국어 이미지 업데이트만 (경고: 기존 한국어 이미지 모두 삭제 후 다시 번역):    translate -l "ko" -img -u

  5. 다른 번역에 영향을 주지 않고 한국어 마크다운 번역만 새로 추가:    translate -l "ko" -md

  6. 번역된 파일에 오류가 있는지 검사하고 필요하면 다시 번역: translate -l "ko" -chk

  7. 번역된 파일 오류 검사 및 재번역 (마크다운만): translate -l "ko" -chk -md

  8. 번역된 파일 오류 검사 및 재번역 (이미지만): translate -l "ko" -chk -img

  9. 이미지 번역에 빠른 모드 사용:    translate -l "ko" -img -f

  10. 디버그 모드 예시: - translate -l "ko" -d: 디버그 로그 활성화.

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 노력하고 있으나, 자동 번역에는 오류나 부정확한 부분이 있을 수 있음을 양지해 주시기 바랍니다. 원문 문서는 해당 언어의 원본이므로 권위 있는 출처로 간주되어야 합니다. 중요한 정보의 경우 전문적인 인간 번역을 권장합니다. 본 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.