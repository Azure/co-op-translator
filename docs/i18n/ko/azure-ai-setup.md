# Azure AI 설정

이 가이드는 텍스트 번역을 위해 Azure OpenAI를 구성하고 이미지 텍스트 추출을 위해 Azure AI Vision을 구성하려는 경우에 사용하세요.

## 필수 조건

- Azure 구독.
- Azure AI 리소스 및 모델 배포를 생성하거나 사용할 수 있는 권한.
- Azure AI Foundry의 프로젝트 또는 Azure OpenAI 및 Azure AI Vision 리소스에 대한 동등한 접근 권한.

## Azure AI 프로젝트 생성

1. [Azure AI Foundry](https://ai.azure.com)를 엽니다.
2. 프로젝트를 생성하거나 선택합니다.
3. 프로젝트용 AI 허브를 생성하거나 선택합니다.
4. 생성 후 프로젝트 개요를 엽니다.

## Azure OpenAI 모델 배포

1. 프로젝트에서 <strong>Models + endpoints</strong>를 엽니다.
2. <strong>Deploy model</strong>을 선택합니다.
3. `gpt-4o`와 같은 GPT 모델을 선택합니다.
4. 모델을 배포합니다.
5. 엔드포인트, 배포 이름, 모델 이름, API 키 및 API 버전을 기록합니다.

!!! note
    Azure OpenAI API 버전은 Azure AI Foundry에 표시되는 모델 버전과 별개입니다. 배포에 지원되는 API 버전을 선택하세요.

## Azure AI Vision 구성

이미지 번역은 소스 이미지에서 텍스트를 추출하기 위해 Azure AI Vision을 사용합니다.

Azure AI 프로젝트에서 Azure AI Services 키와 엔드포인트를 찾습니다.

![Azure AI 서비스 정보 찾기](../../assets/find-azure-ai-info.png)

기록할 항목:

- Azure AI Service endpoint
- Azure AI Service API key

## 환경 변수

자격 증명을 `.env` 파일 또는 CI 시크릿에 추가하세요.

```bash
# 이미지 번역에 필요한 Azure AI Vision
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"

# 텍스트 번역에 필요한 Azure OpenAI
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Co-op Translator는 선택적 폴백 자격 증명 세트도 지원합니다. `_1` 또는 `_2`와 같은 접미사를 사용하여 전체 공급자 세트를 복제하세요. 폴백 세트의 모든 변수는 동일한 접미사를 공유해야 합니다.

```bash
AZURE_OPENAI_API_KEY_1="..."
AZURE_OPENAI_ENDPOINT_1="https://<resource-1>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME_1="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME_1="<deployment-1>"
AZURE_OPENAI_API_VERSION_1="2024-12-01-preview"
```

## 다음 단계

- 로컬 또는 CI 환경 변수를 설정하려면 [Configuration](configuration.md)로 돌아가세요.
- 번역 명령에 대한 자세한 내용은 [CLI Reference](cli.md)를 사용하세요.
- 번역 풀 리퀘스트를 자동화하려면 [GitHub Actions](github-actions.md)를 사용하세요.