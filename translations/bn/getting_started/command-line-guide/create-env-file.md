<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "66029e3b67a3eb980ab8740367e91283",
  "translation_date": "2025-06-12T12:40:54+00:00",
  "source_file": "getting_started/command-line-guide/create-env-file.md",
  "language_code": "bn"
}
-->
# রুট ডিরেক্টরিতে *.env* ফাইল তৈরি করুন

এই টিউটোরিয়ালে, আমরা আপনাকে Azure সার্ভিসের জন্য পরিবেশ ভেরিয়েবল সেটআপ করার প্রক্রিয়া দেখাবো একটি *.env* ফাইল ব্যবহার করে। পরিবেশ ভেরিয়েবলগুলি আপনাকে সংবেদনশীল ক্রেডেনশিয়াল যেমন API কী নিরাপদে পরিচালনা করতে সাহায্য করে, যা কোডবেসে সরাসরি লিখতে হয় না।

> [!IMPORTANT]
> - শুধুমাত্র একটি ভাষা মডেল সার্ভিস (Azure OpenAI বা OpenAI) কনফিগার করা প্রয়োজন। আপনার পছন্দসই সার্ভিসের পরিবেশ ভেরিয়েবল পূরণ করুন। যদি একাধিক ভাষা মডেলের পরিবেশ ভেরিয়েবল সেট করা থাকে, তাহলে কো-অপ অনুবাদক অগ্রাধিকারের ভিত্তিতে একটি নির্বাচন করবে।
> - যদি Computer Vision এর পরিবেশ ভেরিয়েবল সেট না করা থাকে, অনুবাদক স্বয়ংক্রিয়ভাবে [Markdown-only mode](./markdown-only-mode.md) এ স্যুইচ করবে।

> [!NOTE]
> এই গাইডটি মূলত Azure সার্ভিসের উপর কেন্দ্রীভূত, তবে আপনি [supported models and services list](../README.md#-supported-models-and-services) থেকে যেকোনো সমর্থিত ভাষা মডেল বেছে নিতে পারেন।

## *.env* ফাইল তৈরি করুন

আপনার প্রকল্পের রুট ডিরেক্টরিতে একটি *.env* নামের ফাইল তৈরি করুন। এই ফাইলে আপনার সব পরিবেশ ভেরিয়েবল সহজ ফরম্যাটে সংরক্ষিত থাকবে।

> [!WARNING]
> আপনার *.env* ফাইলটি গিটের মতো ভার্সন কন্ট্রোল সিস্টেমে কমিট করবেন না। দুর্ঘটনাজনিত কমিট থেকে রক্ষা পেতে *.env* ফাইলটি আপনার .gitignore ফাইলে যুক্ত করুন।

1. আপনার প্রকল্পের রুট ডিরেক্টরিতে যান।

1. রুট ডিরেক্টরিতে একটি *.env* ফাইল তৈরি করুন।

1. *.env* ফাইলটি খুলুন এবং নিম্নলিখিত টেমপ্লেট পেস্ট করুন:

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
> যদি আপনার API কী এবং এন্ডপয়েন্ট খুঁজে পেতে চান, তাহলে [set-up-azure-ai.md](../set-up-azure-ai.md) ফাইলটি দেখুন।

**দায়বদ্ধতা স্বীকার**:  
এই নথিটি AI অনুবাদ সেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। আমরা যথাসাধ্য সঠিকতার জন্য চেষ্টা করি, তবে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা ভুল থাকতে পারে। মূল নথিটি তার নিজস্ব ভাষায় সর্বোত্তম এবং কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচনা করা উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ গ্রহণ করার পরামর্শ দেওয়া হয়। এই অনুবাদের ব্যবহারে সৃষ্ট কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী নই।