<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "10d8cb07ad0d2ee6705439d4e382ecc9",
  "translation_date": "2025-05-06T18:14:42+00:00",
  "source_file": "getting_started/set-up-resources/set-up-azure-openai.md",
  "language_code": "ko"
}
-->
# Azure OpenAI를 이용한 언어 번역 설정

## Azure AI Foundry에서 Azure OpenAI 리소스 생성하기

Azure AI Foundry에서 Azure OpenAI를 설정하려면 다음 단계를 따르세요:

### 허브 생성하기

1. [Azure AI Foundry 포털](https://ai.azure.com)에 로그인: Azure 계정으로 로그인되어 있는지 확인하세요.

2. 관리 센터로 이동: 홈 화면에서 왼쪽 메뉴의 "Management Center"를 선택하세요.

3. 새 허브 만들기: "+ New hub"를 클릭하고 구독, 리소스 그룹, 허브 이름 등 필요한 정보를 입력하세요. Cognitive vision과 GPT 모델을 지원하는 East US 지역에 허브를 배포하는 것을 권장합니다.

4. 검토 후 생성: 정보를 확인한 후 "Create"를 클릭하여 허브를 만드세요.

### 프로젝트 생성하기

1. 홈 페이지로 이동: 아직 홈 페이지에 없다면 페이지 왼쪽 상단의 "Azure AI Foundry"를 선택해 홈으로 이동하세요.

2. 프로젝트 생성: "+ Create project"를 클릭하고 프로젝트 이름을 입력하세요.

3. 허브 선택: 여러 허브가 있다면 사용할 허브를 선택하세요. 새 허브를 만들고 싶다면 이 단계에서 생성할 수 있습니다.

4. 프로젝트 구성: 안내에 따라 필요에 맞게 프로젝트를 설정하세요.

5. 프로젝트 생성 완료: "Create"를 클릭하여 프로젝트 생성을 마무리하세요.

### OpenAI 모델 배포 및 엔드포인트 설정

1. [Azure AI Foundry 포털](https://ai.azure.com)에 로그인: Azure OpenAI Service 리소스가 포함된 Azure 구독으로 로그인되어 있는지 확인하세요.

2. 모델 및 엔드포인트로 이동: Azure AI Foundry 홈 페이지에서 해당 타일을 찾거나 왼쪽 메뉴에서 "Model and Endpoints"를 선택하세요.

3. GPT 모델이 아직 배포되지 않았다면 모델 배포 선택: GPT-4o, GPT-4o-mini 또는 o3-mini 모델을 추천합니다.

4. 리소스 접근: 기존 Azure OpenAI Service 리소스가 보일 것입니다. 여러 리소스가 있다면 작업할 리소스를 선택하세요.

자세한 내용은 공식 Azure AI Foundry 문서를 참고하세요.

[프로젝트 생성 방법](https://learn.microsoft.com/azure/ai-studio/how-to/create-project)

[리소스 생성 방법](https://learn.microsoft.com/azure/ai-studio/how-to/create-azure-ai-resource)

[AI Foundry에서 OpenAI 모델 사용법](https://learn.microsoft.com/azure/ai-studio/ai-services/how-to/connect-azure-openai)

[Azure AI Foundry의 OpenAI 서비스](https://learn.microsoft.com/azure/ai-studio/azure-openai-in-ai-studio)

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 노력하고 있으나, 자동 번역에는 오류나 부정확성이 포함될 수 있음을 유의하시기 바랍니다. 원문은 해당 언어의 원본 문서가 권위 있는 출처로 간주되어야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 본 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해서는 책임을 지지 않습니다.