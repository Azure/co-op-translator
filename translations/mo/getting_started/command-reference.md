<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b38d8f042530a4bc872def7cb2c141cd",
  "translation_date": "2025-06-12T11:24:44+00:00",
  "source_file": "getting_started/command-reference.md",
  "language_code": "mo"
}
-->
# Command reference
The **Co-op Translator** CLI는 번역 과정을 맞춤 설정할 수 있는 여러 옵션을 제공합니다:

Command                                       | Description
----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"                 | 프로젝트를 지정한 언어들로 번역합니다. 예: translate -l "es fr de"는 스페인어, 프랑스어, 독일어로 번역합니다. translate -l "all"을 사용하면 지원하는 모든 언어로 번역합니다.
translate -l "language_codes" -u              | 기존 번역을 삭제하고 다시 생성하여 번역을 업데이트합니다. 주의: 지정한 언어의 모든 현재 번역이 삭제됩니다.
translate -l "language_codes" -img            | 이미지 파일만 번역합니다.
translate -l "language_codes" -md             | Markdown 파일만 번역합니다.
translate -l "language_codes" -chk            | 번역된 파일의 오류를 검사하고 필요 시 번역을 재시도합니다.
translate -l "language_codes" -d              | 자세한 로그를 위한 디버그 모드를 활성화합니다.
translate -l "language_codes" -r "root_dir"   | 프로젝트의 루트 디렉터리를 지정합니다.
translate -l "language_codes" -f              | 이미지 번역에 빠른 모드를 사용합니다 (품질과 정렬이 약간 희생되지만 최대 3배 빠른 처리 속도).
translate -l "language_codes" -y              | 모든 프롬프트를 자동으로 확인합니다 (CI/CD 파이프라인에 유용).
translate -l "language_codes" --help          | CLI 내에서 사용 가능한 명령어에 대한 도움말을 표시합니다.

### Usage examples:

  1. 기본 동작 (기존 번역을 삭제하지 않고 새 번역 추가):   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. 기존 번역을 삭제하지 않고 한국어 이미지 번역만 추가:    translate -l "ko" -img

  3. 모든 한국어 번역을 업데이트 (주의: 기존 한국어 번역이 모두 삭제된 후 재번역):    translate -l "ko" -u

  4. 한국어 이미지 번역만 업데이트 (주의: 기존 한국어 이미지가 모두 삭제된 후 재번역):    translate -l "ko" -img -u

  5. 다른 번역에 영향을 주지 않고 한국어 마크다운 번역만 새로 추가:    translate -l "ko" -md

  6. 번역된 파일에서 오류를 검사하고 필요 시 번역 재시도: translate -l "ko" -chk

  7. 오류 검사 및 재시도 (마크다운 파일만): translate -l "ko" -chk -md

  8. 오류 검사 및 재시도 (이미지 파일만): translate -l "ko" -chk -img

  9. 이미지 번역에 빠른 모드 사용:    translate -l "ko" -img -f

  10. 디버그 모드 예시: - translate -l "ko" -d: 디버그 로그 활성화.

**Disclaimer**:  
This document has been translated using AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we strive for accuracy, please be aware that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not liable for any misunderstandings or misinterpretations arising from the use of this translation.