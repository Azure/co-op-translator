# ការកំណត់ Azure AI

ប្រើមគ្គុទេសក៍នេះនៅពេលអ្នកចង់កំណត់ Azure OpenAI សម្រាប់ការប្រែសម្រួលអត្ថបទ និង Azure AI Vision សម្រាប់ការដកអត្ថបទពីរូបភាព។

## តម្រូវការមុន

- ការជាវ Azure មួយ។
- សិទ្ធិក្នុងការបង្កើត ឬប្រើធនធាន Azure AI និងការដាក់ឲ្យដំណើរការម៉ូឌែល।
- គម្រោងមួយក្នុង Azure AI Foundry ឬការចូលដំណើរការដូចគ្នាទៅកាន់ Azure OpenAI និង Azure AI Vision។

## បង្កើតគម្រោង Azure AI

1. បើក [Azure AI Foundry](https://ai.azure.com)។
2. បង្កើត ឬជ្រើសគម្រោងមួយ។
3. បង្កើត ឬជ្រើស AI hub សម្រាប់គម្រោង។
4. បើកទិដ្ឋភាពទូទៅរបស់គម្រោងបន្ទាប់ពីការបង្កើត។

## ដាក់ឲ្យដំណើរការម៉ូឌែល Azure OpenAI

1. ក្នុងគម្រោង បើក **Models + endpoints**។
2. ជ្រើស **Deploy model**។
3. ជ្រើសម៉ូឌែល GPT ដូចជា `gpt-4o`។
4. ដាក់ឲ្យម៉ូឌែលដំណើរការ។
5. កត់ត្រា endpoint, deployment name, model name, API key, និង API version។

!!! note
    ជំនាន់ API របស់ Azure OpenAI ផ្សេងពីជំនាន់ម៉ូឌែលដែលបង្ហាញនៅក្នុង Azure AI Foundry។ ជ្រើសជំនាន់ API ដែលគាំទ្រសម្រាប់ការដាក់ឲ្យដំណើរការ។

## កំណត់ Azure AI Vision

ការប្រែរូបភាពប្រើ Azure AI Vision ដើម្បីដកអត្ថបទពីរូបភាពដើមមុនការប្រែអត្ថបទ។

នៅក្នុងគម្រោង Azure AI របស់អ្នក ស្វែងរកកូនសោ និង endpoint របស់ Azure AI Services។

![ស្វែងរកព័ត៌មានសេវាកម្ម Azure AI](../../assets/find-azure-ai-info.png)

កត់ត្រា៖

- endpoint របស់សេវាកម្ម Azure AI
- កូនសោ API របស់សេវាកម្ម Azure AI

## អថេរបរិស្ថាន

បន្ថែមព័ត៌មានសម្គាល់សម្រាប់ការចូល (credentials) ទៅក្នុងឯកសារ `.env` របស់អ្នក ឬ CI secrets។

```bash
# Azure AI Vision, ចាំបាច់សម្រាប់ការប្រែសម្រួលរូបភាព
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"

# Azure OpenAI, ចាំបាច់សម្រាប់ការបកប្រែអត្ថបទ
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Co-op Translator ក៏គាំទ្រសំណុំគណនីជំនួសជាជម្រើសផងដែរ។ ចម្លងសំណុំអ្នកផ្តល់សេវាមួយទាំងស្រុងជាមួយនឹងបុព្វបទដូចជា `_1` ឬ `_2`; អថេរទាំងអស់ក្នុងសំណុំជំនួសត្រូវមានបុព្វបទដូចគ្នា។

```bash
AZURE_OPENAI_API_KEY_1="..."
AZURE_OPENAI_ENDPOINT_1="https://<resource-1>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME_1="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME_1="<deployment-1>"
AZURE_OPENAI_API_VERSION_1="2024-12-01-preview"
```

## ជំហានបន្ទាប់

- ត្រឡប់ទៅ [Configuration](configuration.md) ដើម្បីកំណត់អថេរបរិស្ថានសម្រាប់ម៉ាស៊ីនក្នុងស្រុក ឬ CI។
- ប្រើ [CLI Reference](cli.md) សម្រាប់ពាក្យបញ្ជាប្រែសម្រួល។
- ប្រើ [GitHub Actions](github-actions.md) ដើម្បីស្វ័យប្រវត្តិកម្មការដាក់សំណើ pull requests សម្រាប់ការប្រែសម្រួល។