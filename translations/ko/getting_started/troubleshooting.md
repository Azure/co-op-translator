<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0788d7ebe4876c9be89132f48e09b26d",
  "translation_date": "2025-07-04T06:50:25+00:00",
  "source_file": "getting_started/troubleshooting.md",
  "language_code": "ko"
}
-->
# Microsoft Co-op Translator 문제 해결 가이드

## 개요
Microsoft Co-Op Translator는 Markdown 문서를 원활하게 번역할 수 있는 강력한 도구입니다. 이 가이드는 도구 사용 시 발생할 수 있는 일반적인 문제를 해결하는 데 도움을 줍니다.

## 일반적인 문제와 해결책

### 1. Markdown 태그 문제
**문제:** 번역된 Markdown 문서 상단에 `markdown` 태그가 포함되어 있어 렌더링 문제가 발생합니다.

**해결책:** 이를 해결하려면 파일 상단의 `markdown` 태그를 삭제하십시오. 이렇게 하면 Markdown 파일이 올바르게 렌더링됩니다.

**단계:**
1. 번역된 Markdown (`.md`) 파일을 엽니다.
2. 문서 상단의 `markdown` 태그를 찾습니다.
3. `markdown` 태그를 삭제합니다.
4. 파일에 변경 사항을 저장합니다.
5. 파일을 다시 열어 올바르게 렌더링되는지 확인합니다.

### 2. 내장 이미지 URL 문제
**문제:** 내장 이미지의 URL이 언어 로케일과 일치하지 않아 잘못된 이미지가 표시되거나 이미지가 누락됩니다.

**해결책:** 내장 이미지의 URL을 확인하고 언어 로케일과 일치하는지 확인하십시오. 모든 이미지는 `translated_images` 폴더에 있으며 각 이미지 파일 이름에 언어 로케일 태그가 포함되어 있습니다.

**단계:**
1. 번역된 Markdown 문서를 엽니다.
2. 내장 이미지와 그 URL을 식별합니다.
3. 이미지 파일 이름의 언어 로케일이 문서의 언어와 일치하는지 확인합니다.
4. 필요에 따라 URL을 업데이트합니다.
5. 변경 사항을 저장하고 문서를 다시 열어 이미지가 올바르게 렌더링되는지 확인합니다.

### 3. 번역 정확성
**문제:** 번역된 내용이 정확하지 않거나 추가 편집이 필요합니다.

**해결책:** 번역된 문서를 검토하고 정확성과 가독성을 높이기 위해 필요한 편집을 수행하십시오.

**단계:**
1. 번역된 문서를 엽니다.
2. 내용을 주의 깊게 검토합니다.
3. 번역 정확성을 높이기 위해 필요한 편집을 수행합니다.
4. 변경 사항을 저장합니다.

### 4. 파일 형식 문제
**문제:** 번역된 문서의 형식이 잘못되었습니다. 이는 표에서 발생할 수 있으며 추가적인 ``` are added.

**Solution:** Adjust the formatting of the document to match the original structure. Simply deleting the ```가 표 문제를 해결할 것입니다.

**단계:**
1. 번역된 문서를 엽니다.
2. 원본 문서와 비교하여 형식 문제를 식별합니다.
3. 원본 문서와 일치하도록 형식을 조정합니다.
4. 변경 사항을 저장합니다.

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 우리는 정확성을 위해 노력하지만, 자동 번역에는 오류나 부정확성이 있을 수 있음을 유의하시기 바랍니다. 원본 문서는 해당 언어로 작성된 것이 권위 있는 출처로 간주되어야 합니다. 중요한 정보에 대해서는 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 책임을 지지 않습니다.