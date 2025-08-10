<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "66029e3b67a3eb980ab8740367e91283",
  "translation_date": "2025-08-10T12:16:27+00:00",
  "source_file": "getting_started/command-line-guide/create-env-file.md",
  "language_code": "ko"
}
-->
# 루트 디렉터리에 *.env* 파일 생성하기

이 튜토리얼에서는 *.env* 파일을 사용하여 Azure 서비스에 대한 환경 변수를 설정하는 방법을 안내합니다. 환경 변수는 API 키와 같은 민감한 자격 증명을 코드베이스에 하드코딩하지 않고 안전하게 관리할 수 있도록 해줍니다.

> [!IMPORTANT]
> - 하나의 언어 모델 서비스(Azure OpenAI 또는 OpenAI)만 설정하면 됩니다. 선호하는 서비스에 대한 환경 변수를 입력하세요. 여러 언어 모델에 대한 환경 변수가 설정된 경우, 협업 번역기는 우선순위에 따라 하나를 선택합니다.
> - Computer Vision 환경 변수가 설정되지 않은 경우, 번역기는 자동으로 [Markdown-only 모드](./markdown-only-mode.md)로 전환됩니다.

> [!NOTE]
> 이 가이드는 주로 Azure 서비스에 초점을 맞추고 있지만, [지원되는 모델 및 서비스 목록](../README.md#-supported-models-and-services)에서 지원되는 언어 모델을 선택할 수 있습니다.

## *.env* 파일 생성하기

프로젝트의 루트 디렉터리에 *.env*라는 이름의 파일을 생성하세요. 이 파일은 모든 환경 변수를 간단한 형식으로 저장합니다.

> [!WARNING]
> *.env* 파일을 Git과 같은 버전 관리 시스템에 커밋하지 마세요. 실수로 커밋되는 것을 방지하기 위해 *.env*를 .gitignore 파일에 추가하세요.

1. 프로젝트의 루트 디렉터리로 이동합니다.

1. 프로젝트의 루트 디렉터리에 *.env* 파일을 생성합니다.

1. *.env* 파일을 열고 다음 템플릿을 붙여넣습니다:

    ```plaintext
    # Azure Credentials
    AZURE_AI_SERVICE_API_KEY="your_azure_ai_service_api_key"
    AZURE_AI_SERVICE_ENDPOINT="https://your_azure_ai_service_endpoint"

    # Azure OpenAI Credentials
    AZURE_OPENAI_API_KEY="your_azure_openai_api_key"
    AZURE_OPENAI_ENDPOINT="https://your_azure_openai_endpoint"
    AZURE_OPENAI_MODEL_NAME="your_model_name"
    AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="your_deployment_name"
    AZURE_OPENAI_API_VERSION="your_api_version"

    # OpenAI Credentials
    OPENAI_API_KEY="your_openai_api_key"
    OPENAI_ORG_ID="your_openai_org_id"
    OPENAI_CHAT_MODEL_ID="your_chat_model_id(ex. gpt-4o)"
    OPENAI_BASE_URL="https://api.openai.com/v1 (If you don't have a custom base URL, you can delete this lin, then it will use the default base URL)"
    ```

> [!NOTE]
> API 키와 엔드포인트를 찾고 싶다면 [set-up-azure-ai.md](../set-up-azure-ai.md)를 참조하세요.

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 노력하고 있지만, 자동 번역에는 오류나 부정확성이 있을 수 있음을 유의하시기 바랍니다. 원본 문서는 해당 언어로 작성된 것이 권위 있는 자료로 간주되어야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.