<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "53c99ea0ead7a3500149d4bb96be5811",
  "translation_date": "2025-05-06T17:53:30+00:00",
  "source_file": "getting_started/command-line-guide/create-env-file.md",
  "language_code": "ko"
}
-->
# 루트 디렉터리에 *.env* 파일 생성하기

이 튜토리얼에서는 *.env* 파일을 사용하여 Azure 서비스용 환경 변수를 설정하는 방법을 안내합니다. 환경 변수는 API 키와 같은 민감한 자격 증명을 코드에 직접 작성하지 않고도 안전하게 관리할 수 있게 해줍니다.

> [!IMPORTANT]
> - 하나의 언어 모델 서비스(Azure OpenAI 또는 OpenAI)만 설정하면 됩니다. 선호하는 서비스에 맞게 환경 변수를 채워주세요. 여러 언어 모델용 환경 변수가 설정되어 있으면, co-op translator가 우선순위에 따라 하나를 선택합니다.
> - Computer Vision 환경 변수가 설정되지 않은 경우, 번역기는 자동으로 [Markdown-only 모드](./markdown-only-mode.md)로 전환됩니다.

> [!NOTE]
> 이 가이드는 주로 Azure 서비스에 초점을 맞추고 있지만, [지원되는 모델 및 서비스 목록](../README.md#-supported-models-and-services)에서 원하는 언어 모델을 선택할 수 있습니다.

## *.env* 파일 생성하기

프로젝트 루트 디렉터리에 *.env*라는 파일을 만듭니다. 이 파일은 모든 환경 변수를 간단한 형식으로 저장합니다.

> [!WARNING]
> *.env* 파일을 Git과 같은 버전 관리 시스템에 커밋하지 마세요. 실수로 커밋되는 것을 방지하려면 *.env*를 .gitignore 파일에 추가하세요.

1. 프로젝트 루트 디렉터리로 이동합니다.

1. 루트 디렉터리에 *.env* 파일을 생성합니다.

    ![Create *.env* file.](../../../../imgs/create-env.png)

1. *.env* 파일을 열고 다음 템플릿을 붙여넣습니다:

    ```plaintext
    # Azure Credentials
    AZURE_SUBSCRIPTION_KEY="your_azure_AIServices_api_key"
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

## Azure 자격 증명 준비하기

환경 변수를 설정하려면 다음 Azure 자격 증명이 필요합니다:

이 모든 정보는 [AI Foundry](https://ai.azure.com/build/overview) 내 프로젝트 개요 페이지에서 확인할 수 있습니다.

![Foundry-overview](../../../../imgs/foundry-overview.png)

### Azure AI Service용:

    - Azure Subscription Key: Azure AI 서비스에 접근할 수 있는 API 키입니다.
    - Azure AI Service Endpoint: 특정 Azure AI 서비스의 엔드포인트 URL입니다.

### Azure OpenAI Service용:

    - Azure OpenAI API Key: Azure OpenAI 서비스에 접근하기 위한 API 키입니다.
    - Azure OpenAI Endpoint: Azure OpenAI 서비스의 엔드포인트 URL입니다.

1. AI Services 키와 엔드포인트를 *.env* 파일에 복사하여 붙여넣습니다.
2. Azure OpenAI API 키와 엔드포인트를 *.env* 파일에 복사하여 붙여넣습니다.

### 모델 정보

왼쪽 메뉴에서 모델과 엔드포인트를 선택하세요.

![FoundryModels](../../../../imgs/gpt-models.png)

사용할 모델을 선택하여 모델 세부 정보를 확인합니다.

![ModelDetails](../../../../imgs/model-deployment-name.png)

*.env* 파일에 필요한 정보는 다음과 같습니다:

    - Azure OpenAI Model Name: 상호작용할 모델 이름입니다.
    - Azure OpenAI Name: Azure OpenAI 모델 배포 이름입니다.
    - Azure OpenAI API Version: URL 문자열 끝에서 확인할 수 있는 Azure OpenAI API 버전입니다.

이 정보를 얻으려면 모델 배포를 선택하세요.

![FoundryModelinfo](../../../../imgs/foundry-model-info.png)

### Azure 환경 변수 추가하기

3. Azure OpenAI **Name**과 모델 **Version**을 *.env* 파일에 복사하여 붙여넣습니다.
4. *.env* 파일을 저장합니다.
5. 이제 이 환경 변수를 사용하여 Azure 서비스와 함께 **Co-op Translator**를 사용할 수 있습니다.

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 노력하고 있으나, 자동 번역에는 오류나 부정확성이 포함될 수 있음을 유의하시기 바랍니다. 원문은 해당 언어의 원본 문서를 권위 있는 자료로 간주해야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 본 번역 사용으로 인한 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.