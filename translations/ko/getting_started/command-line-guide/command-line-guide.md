<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a5eb9b53c81804f04bc9456160e79940",
  "translation_date": "2025-05-07T13:57:37+00:00",
  "source_file": "getting_started/command-line-guide/command-line-guide.md",
  "language_code": "ko"
}
-->
# Co-op Translator 명령줄 인터페이스(CLI) 사용 방법

## 사전 준비 사항

- **Python 3.10 이상**: Co-op Translator 실행에 필요합니다.
- **언어 모델 리소스**:  
  - **Azure OpenAI** 또는 기타 LLM. 자세한 내용은 [지원되는 모델 및 서비스](../../../../README.md)에서 확인할 수 있습니다.
- **컴퓨터 비전 리소스** (선택 사항):  
  - 이미지 번역용입니다. 없으면 번역기는 [Markdown 전용 모드](../markdown-only-mode.md)로 동작합니다.  
  - **Azure Computer Vision**

## 목차

1. [루트 디렉터리에 '.env' 파일 생성하기](./create-env-file.md)  
   - 선택한 언어 모델 서비스에 필요한 키를 포함합니다.  
   - Azure Computer Vision 키가 없거나 `-md`가 지정되면 번역기는 Markdown 전용 모드로 동작합니다.  
1. [Co-op translator 패키지 설치하기](./install-package.md)  
1. [Co-op Translator로 프로젝트 번역하기](./translator-your-project.md)

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 노력하고 있으나, 자동 번역에는 오류나 부정확성이 포함될 수 있음을 유의해 주시기 바랍니다. 원본 문서의 원어 버전이 권위 있는 출처로 간주되어야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 본 번역의 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.