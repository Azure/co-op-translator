<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b58d7c3cb4210697a073d20eb3064945",
  "translation_date": "2025-06-12T11:49:08+00:00",
  "source_file": "getting_started/set-up-azure-ai.md",
  "language_code": "ko"
}
-->
# Set Up Azure AI for Co-op Translator (Azure OpneAI & Azure AI Vision)

이 가이드는 Azure AI Foundry 내에서 언어 번역을 위한 Azure OpenAI와 이미지 기반 번역에 활용할 수 있는 이미지 콘텐츠 분석을 위한 Azure Computer Vision 설정 방법을 안내합니다.

**사전 준비 사항:**
- 활성 구독이 연결된 Azure 계정
- Azure 구독에서 리소스 및 배포를 생성할 수 있는 충분한 권한

## Azure AI 프로젝트 생성

AI 리소스를 관리할 중앙 허브 역할을 하는 Azure AI 프로젝트를 먼저 생성합니다.

1. [https://ai.azure.com](https://ai.azure.com)으로 이동하여 Azure 계정으로 로그인합니다.

1. **+Create**를 선택하여 새 프로젝트를 만듭니다.

1. 다음 작업을 수행합니다:
   - **Project name** 입력 (예: `CoopTranslator-Project`).
   - **AI hub** 선택 (예: `CoopTranslator-Hub`) (필요 시 새로 생성).

1. "**Review and Create**"를 클릭하여 프로젝트를 설정합니다. 프로젝트 개요 페이지로 이동합니다.

## 언어 번역을 위한 Azure OpenAI 설정

프로젝트 내에서 텍스트 번역 백엔드로 사용할 Azure OpenAI 모델을 배포합니다.

### 프로젝트로 이동

아직 이동하지 않았다면, Azure AI Foundry에서 새로 만든 프로젝트(예: `CoopTranslator-Project`)를 엽니다.

### OpenAI 모델 배포

1. 프로젝트 좌측 메뉴에서 "My assets" 아래의 "**Models + endpoints**"를 선택합니다.

1. **+ Deploy model**을 선택합니다.

1. **Deploy Base Model**을 선택합니다.

1. 사용 가능한 모델 목록이 표시됩니다. 적합한 GPT 모델을 검색하거나 필터링하세요. 추천 모델은 `gpt-4o`입니다.

1. 원하는 모델을 선택하고 **Confirm**을 클릭합니다.

1. **Deploy**를 선택합니다.

### Azure OpenAI 구성

배포가 완료되면 "**Models + endpoints**" 페이지에서 배포를 선택하여 **REST endpoint URL**, **Key**, **Deployment name**, **Model name**, **API version**을 확인할 수 있습니다. 이 정보는 번역 모델을 애플리케이션에 통합할 때 필요합니다.

> [!NOTE]
> 필요에 따라 [API version deprecation](https://learn.microsoft.com/azure/ai-services/openai/api-version-deprecation) 페이지에서 API 버전을 선택할 수 있습니다. **API version**은 Azure AI Foundry의 "**Models + endpoints**" 페이지에 표시된 **Model version**과 다르니 유의하세요.

## 이미지 번역을 위한 Azure Computer Vision 설정

이미지 내 텍스트 번역을 가능하게 하려면 Azure AI Service API Key와 Endpoint를 찾아야 합니다.

1. Azure AI 프로젝트(예: `CoopTranslator-Project`)로 이동하여 프로젝트 개요 페이지에 있는지 확인합니다.

### Azure AI 서비스 구성

Azure AI 서비스에서 API Key와 Endpoint를 찾습니다.

1. Azure AI 프로젝트(예: `CoopTranslator-Project`)로 이동하여 프로젝트 개요 페이지에 있는지 확인합니다.

1. Azure AI Service 탭에서 **API Key**와 **Endpoint**를 찾습니다.

    ![Find API Key and Endpoint](../../../translated_images/find-azure-ai-info.60f8299be786dd67e61e2c79b4b9ea1f7694e6c0923f17a90bc6abf9d5f1dbd7.ko.png)

이 연결을 통해 연결된 Azure AI Services 리소스(이미지 분석 포함)의 기능을 AI Foundry 프로젝트에서 사용할 수 있습니다. 이후 노트북이나 애플리케이션에서 이 연결을 활용해 이미지에서 텍스트를 추출하고, 추출된 텍스트를 Azure OpenAI 모델로 보내 번역할 수 있습니다.

## 자격 증명 정리

지금쯤 다음 항목들을 확보했을 것입니다:

**Azure OpenAI (텍스트 번역용):**
- Azure OpenAI Endpoint
- Azure OpenAI API Key
- Azure OpenAI Model Name (예: `gpt-4o`)
- Azure OpenAI Deployment Name (예: `cooptranslator-gpt4o`)
- Azure OpenAI API Version

**Azure AI Services (Vision을 통한 이미지 텍스트 추출용):**
- Azure AI Service Endpoint
- Azure AI Service API Key

### 예시: 환경 변수 구성 (미리보기)

애플리케이션을 구축할 때 위에서 수집한 자격 증명을 환경 변수로 설정하는 경우가 많습니다. 예를 들면 다음과 같습니다:

```bash
# Azure AI Service Credentials (Required for image translation)
AZURE_AI_SERVICE_API_KEY="your_azure_ai_service_api_key" # e.g., 21xasd...
AZURE_AI_SERVICE_ENDPOINT="https://your_azure_ai_service_endpoint.cognitiveservices.azure.com/"

# Azure OpenAI Credentials (Required for text translation)
AZURE_OPENAI_API_KEY="your_azure_openai_api_key" # e.g., 21xasd...
AZURE_OPENAI_ENDPOINT="https://your_azure_openai_endpoint.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="your_model_name" # e.g., gpt-4o
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="your_deployment_name" # e.g., cooptranslator-gpt4o
AZURE_OPENAI_API_VERSION="your_api_version" # e.g., 2024-12-01-preview
```

---

### 추가 자료

- [Azure AI Foundry에서 프로젝트 생성 방법](https://learn.microsoft.com/azure/ai-foundry/how-to/create-projects?tabs=ai-studio)
- [Azure AI 리소스 생성 방법](https://learn.microsoft.com/azure/ai-foundry/how-to/create-azure-ai-resource?tabs=portal)
- [Azure AI Foundry에서 OpenAI 모델 배포 방법](https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/deploy-models-openai)

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 노력하고 있으나, 자동 번역에는 오류나 부정확한 내용이 포함될 수 있음을 유의해 주시기 바랍니다. 원문은 해당 언어의 원본 문서가 권위 있는 자료로 간주되어야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 본 번역 사용으로 인한 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.