<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "822238e4451d04bb152cebb1be6f13c2",
  "translation_date": "2025-11-30T10:29:19+00:00",
  "source_file": "getting_started/command-reference.md",
  "language_code": "ko"
}
-->
# 명령어 참조

**Co-op Translator** CLI는 번역 과정을 사용자 정의할 수 있는 여러 옵션을 제공합니다:

명령어                                       | 설명
----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"                 | 프로젝트를 지정한 언어로 번역합니다. 예: translate -l "es fr de"는 스페인어, 프랑스어, 독일어로 번역합니다. translate -l "all"을 사용하면 지원하는 모든 언어로 번역합니다.
translate -l "language_codes" -u              | 기존 번역을 삭제하고 다시 생성하여 번역을 업데이트합니다. 주의: 지정한 언어의 모든 현재 번역이 삭제됩니다.
translate -l "language_codes" -img            | 이미지 파일만 번역합니다.
translate -l "language_codes" -md             | 마크다운 파일만 번역합니다.
translate -l "language_codes" -nb             | Jupyter 노트북 파일(.ipynb)만 번역합니다.
translate -l "language_codes" --fix           | 이전 평가 결과를 기반으로 신뢰도가 낮은 파일을 재번역합니다.
translate -l "language_codes" -d              | 자세한 로그 출력을 위한 디버그 모드를 활성화합니다.
translate -l "language_codes" --save-logs, -s | DEBUG 레벨 로그를 <root_dir>/logs/ 폴더에 저장합니다 (콘솔 출력은 -d 옵션에 의해 제어됨).
translate -l "language_codes" -r "root_dir"   | 프로젝트의 루트 디렉터리를 지정합니다.
translate -l "language_codes" -f              | 이미지 번역에 빠른 모드를 사용합니다 (품질과 정렬에 약간의 손해를 보면서 최대 3배 빠른 처리).
translate -l "language_codes" -y              | 모든 프롬프트를 자동으로 확인합니다 (CI/CD 파이프라인에 유용).
translate -l "language_codes" --add-disclaimer/--no-disclaimer | 번역된 마크다운과 노트북에 기계 번역 면책 조항 섹션을 추가할지 여부를 설정합니다 (기본값: 활성화).
translate -l "language_codes" --help          | CLI 내에서 사용 가능한 명령어에 대한 도움말을 표시합니다.
evaluate -l "language_code"                  | 특정 언어에 대한 번역 품질을 평가하고 신뢰도 점수를 제공합니다.
evaluate -l "language_code" -c 0.8           | 사용자 지정 신뢰도 임계값으로 번역을 평가합니다.
evaluate -l "language_code" -f               | 빠른 평가 모드 (규칙 기반, LLM 미사용).
evaluate -l "language_code" -D               | 심층 평가 모드 (LLM 기반, 더 철저하지만 느림).
evaluate -l "language_code" --save-logs, -s  | DEBUG 레벨 로그를 <root_dir>/logs/ 폴더에 저장합니다.
migrate-links -l "language_codes"             | 번역된 마크다운 파일을 다시 처리하여 노트북(.ipynb) 링크를 업데이트합니다. 번역된 노트북이 있으면 우선 사용하며, 없으면 원본 노트북으로 대체할 수 있습니다.
migrate-links -l "language_codes" -r          | 프로젝트 루트 디렉터리를 지정합니다 (기본값: 현재 디렉터리).
migrate-links -l "language_codes" --dry-run   | 변경될 파일을 보여주지만 실제로는 파일을 수정하지 않습니다.
migrate-links -l "language_codes" --no-fallback-to-original | 번역된 노트북이 없을 때 원본 노트북 링크로 되돌리지 않습니다 (번역된 노트북이 있을 때만 업데이트).
migrate-links -l "language_codes" -d          | 자세한 로그 출력을 위한 디버그 모드를 활성화합니다.
migrate-links -l "language_codes" --save-logs, -s | DEBUG 레벨 로그를 <root_dir>/logs/ 폴더에 저장합니다.
migrate-links -l "all" -y                      | 모든 언어를 처리하고 경고 프롬프트를 자동으로 확인합니다.

## 사용 예시

  1. 기본 동작 (기존 번역을 삭제하지 않고 새 번역만 추가):   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. 한국어 이미지 번역만 새로 추가 (기존 번역은 삭제하지 않음):    translate -l "ko" -img

  3. 모든 한국어 번역 업데이트 (주의: 기존 한국어 번역이 모두 삭제된 후 재번역):    translate -l "ko" -u

  4. 한국어 이미지 번역만 업데이트 (주의: 기존 한국어 이미지가 모두 삭제된 후 재번역):    translate -l "ko" -img -u

  5. 다른 번역에 영향을 주지 않고 한국어 마크다운 번역만 새로 추가:    translate -l "ko" -md

  6. 이전 평가 결과를 기반으로 신뢰도가 낮은 번역 수정: translate -l "ko" --fix

  7. 특정 파일만 신뢰도 낮은 번역 수정 (마크다운): translate -l "ko" --fix -md

  8. 특정 파일만 신뢰도 낮은 번역 수정 (이미지): translate -l "ko" --fix -img

  9. 이미지 번역에 빠른 모드 사용:    translate -l "ko" -img -f

  10. 사용자 지정 임계값으로 신뢰도 낮은 번역 수정: translate -l "ko" --fix -c 0.8

  11. 디버그 모드 예시: - translate -l "ko" -d: 디버그 로그 활성화.
  12. 로그를 파일로 저장: translate -l "ko" -s
  13. 콘솔과 파일 모두 DEBUG 레벨 로그: translate -l "ko" -d -s
  14. 출력에 기계 번역 면책 조항을 추가하지 않고 번역: translate -l "ko" --no-disclaimer

  15. 한국어 번역에 대한 노트북 링크 마이그레이션 (번역된 노트북 링크로 업데이트):    migrate-links -l "ko"

  15. 변경 사항을 파일에 쓰지 않고 확인만:    migrate-links -l "ko" --dry-run

  16. 번역된 노트북이 있을 때만 링크 업데이트 (원본으로 되돌리지 않음):    migrate-links -l "ko" --no-fallback-to-original

  17. 모든 언어에 대해 확인 프롬프트와 함께 처리:    migrate-links -l "all"

  18. 모든 언어를 처리하고 자동으로 확인:    migrate-links -l "all" -y
  19. migrate-links 로그를 파일로 저장:    migrate-links -l "ko ja" -s

### 평가 예시

> [!WARNING]  
> **베타 기능**: 평가 기능은 현재 베타 단계입니다. 이 기능은 번역된 문서를 평가하기 위해 출시되었으며, 평가 방법과 세부 구현은 아직 개발 중이며 변경될 수 있습니다.

  1. 한국어 번역 평가: evaluate -l "ko"

  2. 사용자 지정 신뢰도 임계값으로 평가: evaluate -l "ko" -c 0.8

  3. 빠른 평가 (규칙 기반만): evaluate -l "ko" -f

  4. 심층 평가 (LLM 기반만): evaluate -l "ko" -D

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있으나, 자동 번역에는 오류나 부정확한 부분이 있을 수 있음을 유의해 주시기 바랍니다. 원문 문서는 해당 언어의 권위 있는 자료로 간주되어야 합니다. 중요한 정보의 경우 전문적인 인간 번역을 권장합니다. 본 번역 사용으로 인한 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->