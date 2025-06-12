<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "66029e3b67a3eb980ab8740367e91283",
  "translation_date": "2025-06-12T12:40:32+00:00",
  "source_file": "getting_started/command-line-guide/create-env-file.md",
  "language_code": "ko"
}
-->
# 루트 디렉터리에 *.env* 파일 만들기

이 튜토리얼에서는 *.env* 파일을 사용해 Azure 서비스용 환경 변수를 설정하는 방법을 안내합니다. 환경 변수는 API 키와 같은 민감한 자격 증명을 코드에 직접 작성하지 않고도 안전하게 관리할 수 있게 해줍니다.

> [!IMPORTANT]
> - 하나의 언어 모델 서비스(Azure OpenAI 또는 OpenAI)만 설정하면 됩니다. 원하는 서비스에 맞는 환경 변수를 입력하세요. 여러 언어 모델의 환경 변수가 설정되어 있으면, 협업 번역기가 우선순위에 따라 하나를 선택합니다.
> - Computer Vision 환경 변수가 설정되어 있지 않으면, 번역기는 자동으로 [Markdown 전용 모드](./markdown-only-mode.md)로 전환됩니다.

> [!NOTE]
> 이 가이드는 주로 Azure 서비스를 다루지만, [지원되는 모델 및 서비스 목록](../README.md#-supported-models-and-services)에서 원하는 언어 모델을 선택할 수 있습니다.

## *.env* 파일 만들기

프로젝트 루트 디렉터리에 *.env*라는 파일을 만드세요. 이 파일은 모든 환경 변수를 간단한 형식으로 저장합니다.

> [!WARNING]
> *.env* 파일을 Git 같은 버전 관리 시스템에 커밋하지 마세요. 실수로 커밋되는 것을 방지하려면 .gitignore 파일에 *.env*를 추가하세요.

1. 프로젝트 루트 디렉터리로 이동합니다.

1. 프로젝트 루트 디렉터리에 *.env* 파일을 만듭니다.

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
> API 키와 엔드포인트를 찾고 싶다면 [set-up-azure-ai.md](../set-up-azure-ai.md)를 참고하세요.

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 노력하고 있으나, 자동 번역에는 오류나 부정확한 부분이 있을 수 있음을 유의해 주시기 바랍니다. 원문은 해당 언어의 원본 문서가 권위 있는 출처로 간주되어야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 본 번역의 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.