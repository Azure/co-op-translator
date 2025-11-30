<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "93a7150216aa3c2d191135358fa6dd21",
  "translation_date": "2025-11-30T13:39:28+00:00",
  "source_file": "getting_started/update-other-courses.md",
  "language_code": "ko"
}
-->
# "기타 강좌" 섹션 업데이트 (Microsoft 초보자 저장소)

이 가이드는 Co-op Translator를 사용하여 "기타 강좌" 섹션을 자동 동기화하는 방법과 모든 저장소에 대한 전역 템플릿을 업데이트하는 방법을 설명합니다.

- 적용 대상: Microsoft 초보자 저장소만 해당
- 사용 도구: Co-op Translator CLI 및 GitHub Actions
- 템플릿 소스: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## 빠른 시작: 저장소에서 자동 동기화 활성화

README의 "기타 강좌" 섹션 주위에 다음 마커를 추가하세요. Co-op Translator는 이 마커 사이의 모든 내용을 실행할 때마다 교체합니다.

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

Co-op Translator가 CLI(예: `translate -l "<language codes>"`) 또는 GitHub Actions를 통해 실행될 때마다 이 마커로 감싼 "기타 강좌" 섹션이 자동으로 업데이트됩니다.

> [!NOTE]
> 기존 목록이 있다면 동일한 마커로 감싸기만 하면 됩니다. 다음 실행 시 최신 표준화된 내용으로 교체됩니다.

---

## 전역 콘텐츠 변경 방법

모든 초보자 저장소에 나타나는 표준화된 콘텐츠를 업데이트하려면:

1. 템플릿을 편집하세요: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)
2. 변경 사항을 포함한 풀 리퀘스트를 Co-op Translator 저장소에 오픈하세요
3. PR이 병합되면 Co-op Translator 버전이 업데이트됩니다
4. 대상 저장소에서 Co-op Translator가 다음에 실행될 때(CLI 또는 GitHub Action) 업데이트된 섹션이 자동으로 동기화됩니다

이렇게 하면 모든 초보자 저장소에서 "기타 강좌" 콘텐츠의 단일 진실 소스를 유지할 수 있습니다.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있으나, 자동 번역에는 오류나 부정확성이 포함될 수 있음을 유의하시기 바랍니다. 원문 문서가 권위 있는 출처로 간주되어야 합니다. 중요한 정보의 경우 전문적인 인간 번역을 권장합니다. 본 번역 사용으로 인한 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->