<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "220341925e9a67a0e467d1ba94d3cf7d",
  "translation_date": "2025-05-07T14:17:51+00:00",
  "source_file": "getting_started/set-up-azure-ai.md",
  "language_code": "ko"
}
-->
# Set Up Azure AI for Co-op Translator (Azure OpneAI & Azure AI Vision)

이 가이드는 Azure AI Foundry 내에서 언어 번역을 위한 Azure OpenAI와 이미지 기반 번역에 사용할 수 있는 이미지 콘텐츠 분석을 위한 Azure Computer Vision 설정 방법을 안내합니다.

**필수 조건:**
- 활성 구독이 있는 Azure 계정.
- Azure 구독 내에서 리소스 및 배포를 생성할 수 있는 충분한 권한.

## Azure AI 프로젝트 생성

AI 리소스를 관리하는 중앙 허브 역할을 하는 Azure AI 프로젝트를 먼저 생성합니다.

1. [https://ai.azure.com](https://ai.azure.com)으로 이동하여 Azure 계정으로 로그인합니다.

1. **+Create**를 선택하여 새 프로젝트를 만듭니다.

1. 다음 작업을 수행합니다:
   - **Project name** 입력 (예: `CoopTranslator-Project`).
   - **AI hub** 선택 (예: `CoopTranslator-Hub`) (필요 시 새로 만듭니다).

1. "**Review and Create**"를 클릭하여 프로젝트를 설정합니다. 프로젝트 개요 페이지로 이동합니다.

## 언어 번역을 위한 Azure OpenAI 설정

프로젝트 내에서 텍스트 번역 백엔드로 사용할 Azure OpenAI 모델을 배포합니다.

### 프로젝트로 이동

아직 이동하지 않았다면, Azure AI Foundry에서 새로 만든 프로젝트(예: `CoopTranslator-Project`)를 엽니다.

### OpenAI 모델 배포

1. 프로젝트 왼쪽 메뉴에서 "My assets" 아래의 "**Models + endpoints**"를 선택합니다.

1. **+ Deploy model**을 선택합니다.

1. **Deploy Base Model**을 선택합니다.

1. 사용 가능한 모델 목록이 표시됩니다. 적절한 GPT 모델을 필터링하거나 검색하세요. 권장 모델은 `gpt-4o`입니다.

1. 원하는 모델을 선택하고 **Confirm**을 클릭합니다.

1. **Deploy**를 선택합니다.

### Azure OpenAI 구성

배포가 완료되면 "**Models + endpoints**" 페이지에서 배포를 선택하여 **REST endpoint URL**, **Key**, **Deployment name**, **Model name**, **API version**을 확인할 수 있습니다. 이 정보는 번역 모델을 애플리케이션에 통합할 때 필요합니다.

## 이미지 번역을 위한 Azure Computer Vision 설정

이미지 내 텍스트 번역을 활성화하려면 Azure AI Service API Key와 Endpoint를 찾아야 합니다.

1. Azure AI 프로젝트(예: `CoopTranslator-Project`)로 이동합니다. 프로젝트 개요 페이지에 있는지 확인하세요.

### Azure AI 서비스 구성

Azure AI 서비스에서 API Key와 Endpoint를 찾습니다.

1. Azure AI 프로젝트(예: `CoopTranslator-Project`)로 이동합니다. 프로젝트 개요 페이지에 있는지 확인하세요.

1. Azure AI Service 탭에서 **API Key**와 **Endpoint**를 찾습니다.

    ![Find API Key and Endpoint](../../../getting_started/imgs/find-azure-ai-info.png)

이 연결을 통해 연결된 Azure AI Services 리소스(이미지 분석 포함)의 기능을 AI Foundry 프로젝트에서 사용할 수 있습니다. 이를 통해 노트북이나 애플리케이션에서 이미지에서 텍스트를 추출하고, 추출된 텍스트를 Azure OpenAI 모델로 보내 번역할 수 있습니다.

## 자격 증명 통합

지금까지 다음 정보를 수집했을 것입니다:

**Azure OpenAI (텍스트 번역용):**
- Azure OpenAI Endpoint
- Azure OpenAI API Key
- Azure OpenAI Model Name (예: `gpt-4o`)
- Azure OpenAI Deployment Name (예: `cooptranslator-gpt4o`)
- Azure OpenAI API Version

**Azure AI Services (Vision을 통한 이미지 텍스트 추출용):**
- Azure AI Service Endpoint
- Azure AI Service API Key

### 예: 환경 변수 구성 (미리보기)

나중에 애플리케이션을 구축할 때 수집한 자격 증명을 사용하여 환경 변수로 설정할 가능성이 큽니다. 예시는 다음과 같습니다:

```bash
# Azure AI Service Credentials (Required for image translation)
AZURE_AI_SERVICE_API_KEY="your_azure_ai_service_api_key" # e.g., 21xasd...
AZURE_AI_SERVICE_ENDPOINT="https://your_azure_ai_service_endpoint.cognitiveservices.azure.com/"

# Azure OpenAI Credentials (Required for text translation)
AZURE_OPENAI_API_KEY="your_azure_openai_api_key" # e.g., 21xasd...
AZURE_OPENAI_ENDPOINT="https://your_azure_openai_endpoint.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="your_model_name" # e.g., gpt-4o
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="your_deployment_name" # e.g., cooptranslator-gpt4o
AZURE_OPENAI_API_VERSION="your_api_version" # e.g., 2024-02-01
```

---

### 추가 자료

- [How to Create a project in Azure AI Foundry](https://learn.microsoft.com/azure/ai-foundry/how-to/create-projects?tabs=ai-studio)
- [How to Create Azure AI resources](https://learn.microsoft.com/azure/ai-foundry/how-to/create-azure-ai-resource?tabs=portal)
- [How to Deploy OpenAI models in Azure AI Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/deploy-models-openai)

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있으나, 자동 번역에는 오류나 부정확한 부분이 있을 수 있음을 유의해 주시기 바랍니다. 원문 문서가 권위 있는 출처로 간주되어야 합니다. 중요한 정보의 경우 전문적인 인간 번역을 권장합니다. 본 번역 사용으로 인한 오해나 잘못된 해석에 대해서는 당사가 책임지지 않습니다.