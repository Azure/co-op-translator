<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b38d8f042530a4bc872def7cb2c141cd",
  "translation_date": "2025-08-10T12:12:08+00:00",
  "source_file": "getting_started/command-reference.md",
  "language_code": "ko"
}
-->
# 명령어 참조
**Co-op Translator** CLI는 번역 프로세스를 사용자 정의할 수 있는 여러 옵션을 제공합니다:

명령어                                       | 설명
----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"                 | 프로젝트를 지정된 언어로 번역합니다. 예: translate -l "es fr de"는 스페인어, 프랑스어, 독일어로 번역합니다. translate -l "all"을 사용하면 지원되는 모든 언어로 번역합니다.
translate -l "language_codes" -u              | 기존 번역을 삭제하고 다시 생성하여 번역을 업데이트합니다. 경고: 지정된 언어의 현재 번역이 모두 삭제됩니다.
translate -l "language_codes" -img            | 이미지 파일만 번역합니다.
translate -l "language_codes" -md             | Markdown 파일만 번역합니다.
translate -l "language_codes" -chk            | 번역된 파일을 오류가 있는지 확인하고 필요시 번역을 다시 시도합니다.
translate -l "language_codes" -d              | 자세한 로그를 위한 디버그 모드를 활성화합니다.
translate -l "language_codes" -r "root_dir"   | 프로젝트의 루트 디렉토리를 지정합니다.
translate -l "language_codes" -f              | 이미지 번역에 빠른 모드를 사용합니다 (품질과 정렬에 약간의 손실이 있지만 최대 3배 빠른 플로팅).
translate -l "language_codes" -y              | 모든 프롬프트를 자동으로 확인합니다 (CI/CD 파이프라인에 유용).
translate -l "language_codes" --help          | CLI 내에서 사용 가능한 명령어에 대한 도움말 세부 정보 표시

### 사용 예시:

  1. 기본 동작 (기존 번역을 삭제하지 않고 새 번역 추가):   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. 기존 번역을 삭제하지 않고 새로운 한국어 이미지 번역만 추가:    translate -l "ko" -img

  3. 모든 한국어 번역 업데이트 (경고: 기존 한국어 번역이 모두 삭제된 후 다시 번역):    translate -l "ko" -u

  4. 한국어 이미지만 업데이트 (경고: 기존 한국어 이미지가 모두 삭제된 후 다시 번역):    translate -l "ko" -img -u

  5. 다른 번역에 영향을 주지 않고 한국어에 대한 새로운 Markdown 번역 추가:    translate -l "ko" -md

  6. 번역된 파일을 오류가 있는지 확인하고 필요시 번역을 다시 시도: translate -l "ko" -chk

  7. 번역된 파일을 오류가 있는지 확인하고 번역을 다시 시도 (Markdown만): translate -l "ko" -chk -md

  8. 번역된 파일을 오류가 있는지 확인하고 번역을 다시 시도 (이미지만): translate -l "ko" -chk -img

  9. 이미지 번역에 빠른 모드 사용:    translate -l "ko" -img -f

  10. 디버그 모드 예시: - translate -l "ko" -d: 디버그 로깅 활성화.

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 노력하고 있지만, 자동 번역에는 오류나 부정확성이 있을 수 있음을 유의하시기 바랍니다. 원본 문서는 해당 언어로 작성된 것이 권위 있는 자료로 간주되어야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.