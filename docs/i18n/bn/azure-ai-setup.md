# Azure AI সেটআপ

এই নির্দেশিকাটি ব্যবহার করুন যখন আপনি টেক্সট অনুবাদের জন্য Azure OpenAI এবং চিত্র-টেক্সট নিষ্কাশনের জন্য Azure AI Vision কনফিগার করতে চান।

## পূর্বশর্ত

- একটি Azure সাবস্ক্রিপশন.
- Azure AI রিসোর্স এবং মডেল ডিপ্লয়মেন্ট তৈরি বা ব্যবহার করার অনুমতি.
- Azure AI Foundry-এ একটি প্রকল্প বা Azure OpenAI এবং Azure AI Vision রিসোর্সগুলোর সমমানের অ্যাক্সেস.

## একটি Azure AI প্রকল্প তৈরি করুন

1. Open [Azure AI Foundry](https://ai.azure.com).
2. একটি প্রকল্প তৈরি করুন বা নির্বাচন করুন.
3. প্রকল্পের জন্য একটি AI হাব তৈরি করুন বা নির্বাচন করুন.
4. তৈরি হওয়ার পরে প্রকল্প ওভারভিউ খুলুন.

## একটি Azure OpenAI মডেল ডিপ্লয় করুন

1. প্রকল্পে, **Models + endpoints** খুলুন.
2. **Deploy model** নির্বাচন করুন.
3. একটি GPT মডেল নির্বাচন করুন যেমন `gpt-4o`.
4. মডেলটি ডিপ্লয় করুন.
5. এন্ডপয়েন্ট, ডিপ্লয়মেন্ট নাম, মডেল নাম, API কী এবং API ভার্সন নোট করুন.

!!! note
    Azure OpenAI API সংস্করণটি Azure AI Foundry-এ প্রদর্শিত মডেল সংস্করণ থেকে আলাদা। আপনার ডিপ্লয়মেন্টের জন্য একটি সমর্থিত API সংস্করণ নির্বাচন করুন।

## Azure AI Vision কনফিগার করুন

ইমেজ অনুবাদে টেক্সট অনুবাদিত হওয়ার আগে উৎস চিত্র থেকে টেক্সট বের করতে Azure AI Vision ব্যবহার করা হয়।

আপনার Azure AI প্রকল্পে Azure AI Services কী এবং এন্ডপয়েন্ট খুঁজুন।

![Azure AI সার্ভিসের তথ্য খুঁজুন](../../assets/find-azure-ai-info.png)

নোট করুন:

- Azure AI Service এন্ডপয়েন্ট
- Azure AI Service API কী

## পরিবেশ ভেরিয়েবল

আপনার `.env` ফাইল বা CI সিক্রেটসে ক্রেডেনশিয়ালগুলো যোগ করুন।

```bash
# Azure AI Vision, চিত্র অনুবাদের জন্য প্রয়োজনীয়
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"

# Azure OpenAI, টেক্সট অনুবাদের জন্য প্রয়োজনীয়
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Co-op Translator এছাড়াও ঐচ্ছিক ফ্যালব্যাক ক্রেডেনশিয়াল সেটগুলিকে সমর্থন করে। `_1` বা `_2` এর মতো সাফিক্স সহ একটি সম্পূর্ণ প্রোভাইডার সেট নকল করুন; ফ্যালব্যাক সেটের সকল ভেরিয়েবল একই সাফিক্স শেয়ার করতে হবে।

```bash
AZURE_OPENAI_API_KEY_1="..."
AZURE_OPENAI_ENDPOINT_1="https://<resource-1>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME_1="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME_1="<deployment-1>"
AZURE_OPENAI_API_VERSION_1="2024-12-01-preview"
```

## পরবর্তী ধাপ

- [Configuration](configuration.md)-এ ফিরে যান এবং লোকাল বা CI পরিবেশ ভেরিয়েবল সেট আপ করুন.
- অনুবাদ কমান্ডের জন্য [CLI Reference](cli.md) ব্যবহার করুন.
- অনুবাদ পুল রিকোয়েস্টগুলো স্বয়ংক্রিয় করার জন্য [GitHub Actions](github-actions.md) ব্যবহার করুন.