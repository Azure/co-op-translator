<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "10d8cb07ad0d2ee6705439d4e382ecc9",
  "translation_date": "2025-05-06T18:15:43+00:00",
  "source_file": "getting_started/set-up-resources/set-up-azure-openai.md",
  "language_code": "hi"
}
-->
# भाषा अनुवाद के लिए Azure OpenAI सेटअप करें

## Azure AI Foundry में एक Azure OpenAI रिसोर्स बनाएं

Azure AI Foundry में Azure OpenAI सेटअप करने के लिए, इन चरणों का पालन करें:

### एक हब बनाना

1. [Azure AI Foundry पोर्टल](https://ai.azure.com) में साइन इन करें: सुनिश्चित करें कि आप अपने Azure अकाउंट से साइन इन हैं।

2. Management Center पर जाएं: होम पेज से, बाएं मेनू में "Management Center" चुनें।

3. नया हब बनाएं: "+ New hub" पर क्लिक करें और आवश्यक विवरण जैसे Subscription, Resource Group, और Hub Name दर्ज करें। हम सलाह देते हैं कि हब को East US क्षेत्र में डिप्लॉय करें क्योंकि यह क्षेत्र Cognitive vision और GPT मॉडल्स को सपोर्ट करता है।

4. विवरण की समीक्षा करें और बनाएं: विवरण की जाँच करें और हब सेटअप करने के लिए "Create" पर क्लिक करें।

### एक प्रोजेक्ट बनाना

1. होम पेज पर जाएं: यदि आप पहले से वहां नहीं हैं, तो पेज के ऊपर बाएं कोने में "Azure AI Foundry" चुनकर होम पेज पर जाएं।

2. प्रोजेक्ट बनाएं: "+ Create project" पर क्लिक करें और अपने प्रोजेक्ट के लिए एक नाम दर्ज करें।

3. एक हब चुनें: यदि आपके पास कई हब हैं, तो वह चुनें जिसे आप उपयोग करना चाहते हैं। यदि आप नया हब बनाना चाहते हैं, तो आप इसे इस चरण में कर सकते हैं।

4. प्रोजेक्ट कॉन्फ़िगर करें: अपनी जरूरतों के अनुसार प्रोजेक्ट सेटअप के निर्देशों का पालन करें।

5. प्रोजेक्ट बनाएं: सेटअप पूरा करने के लिए "Create" पर क्लिक करें।

### OpenAI मॉडल के लिए मॉडल और एंडपॉइंट डिप्लॉय करना

1. [Azure AI Foundry पोर्टल](https://ai.azure.com) में साइन इन करें: सुनिश्चित करें कि आप उस Azure सब्सक्रिप्शन से साइन इन हैं जिसमें आपका Azure OpenAI Service रिसोर्स है।

2. Models and Endpoints पर जाएं: Azure AI Foundry होम पेज से, उस टाइल को खोजें जिसमें "Let's go." लिखा हो या बाएं मेनू में Model and Endpoints चुनें।

3. यदि आपके पास पहले से GPT मॉडल डिप्लॉय नहीं है, तो मॉडल डिप्लॉय करें: GPT मॉडल चुनें, हम GPT-4o, GPT-4o-mini या o3-mini की सलाह देते हैं।

4. अपने रिसोर्सेस तक पहुँचें: आपको अपने मौजूदा Azure OpenAI Service रिसोर्सेस दिखेंगे। यदि आपके पास कई रिसोर्सेस हैं, तो उस रिसोर्स का चयन करें जिसके साथ आप काम करना चाहते हैं।

अधिक विस्तृत निर्देशों के लिए, आप आधिकारिक Azure AI Foundry डाक्यूमेंटेशन देख सकते हैं।

[प्रोजेक्ट कैसे बनाएं](https://learn.microsoft.com/azure/ai-studio/how-to/create-project)

[रिसोर्सेस कैसे बनाएं](https://learn.microsoft.com/azure/ai-studio/how-to/create-azure-ai-resource)

[AI Foundry में OpenAI मॉडल का उपयोग कैसे करें](https://learn.microsoft.com/azure/ai-studio/ai-services/how-to/connect-azure-openai)

[Azure AI Foundry में OpenAI सेवाएं](https://learn.microsoft.com/azure/ai-studio/azure-openai-in-ai-studio)

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनूदित किया गया है। जबकि हम सटीकता के लिए प्रयासरत हैं, कृपया ध्यान रखें कि स्वचालित अनुवाद में त्रुटियाँ या असंगतियाँ हो सकती हैं। मूल दस्तावेज़ उसकी मूल भाषा में ही प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सलाह दी जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम जिम्मेदार नहीं हैं।