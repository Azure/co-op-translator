<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d8eec418d6325416b9fab19a2dfcbf41",
  "translation_date": "2025-05-06T17:51:41+00:00",
  "source_file": "getting_started/command-line-guide/command-line-guide.md",
  "language_code": "ko"
}
-->
# Co-op Translator 커맨드 라인 인터페이스(CLI) 사용법

## 사전 준비 사항

- **Python 3.10 이상**: Co-op Translator 실행에 필요합니다.
- **언어 모델 리소스**:  
  - **Azure OpenAI** 또는 기타 LLM. 자세한 내용은 [지원 모델 및 서비스](../../../../README.md)에서 확인할 수 있습니다.
- **컴퓨터 비전 리소스** (선택 사항):  
  - 이미지 번역에 사용됩니다. 없을 경우 번역기는 기본적으로 [Markdown 전용 모드](../markdown-only-mode.md)로 동작합니다.  
  - **Azure Computer Vision**

### 초기 설정

시작하기 전에 다음 리소스들을 반드시 설정하세요:

- [Azure OpenAI 설정](../set-up-resources/set-up-azure-openai.md)
- [Azure Computer Vision 설정](../set-up-resources/set-up-azure-computer-vision.md) (선택 사항)

## 목차

1. [루트 디렉터리에 '.env' 파일 생성하기](./create-env-file.md)  
   - 선택한 언어 모델 서비스에 필요한 키를 포함합니다.  
   - Azure Computer Vision 키를 생략하거나 `-md`를 지정하면 번역기는 Markdown 전용 모드로 작동합니다.  
3. [Co-op Translator 패키지 설치하기](./install-package.md)  
4. [Co-op Translator로 프로젝트 번역하기](./translator-your-project.md)

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 노력하고 있으나, 자동 번역에는 오류나 부정확한 내용이 포함될 수 있음을 유의하시기 바랍니다. 원본 문서의 원어본이 권위 있는 출처로 간주되어야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 본 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.