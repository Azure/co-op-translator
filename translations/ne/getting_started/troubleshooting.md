<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6e626bef5ed78a1cc55b0dbf44f01d47",
  "translation_date": "2025-10-15T02:53:36+00:00",
  "source_file": "getting_started/troubleshooting.md",
  "language_code": "ne"
}
-->
# Microsoft Co-op Translator समस्या समाधान गाइड

## संक्षिप्त परिचय
Microsoft Co-Op Translator एक शक्तिशाली उपकरण हो जसले Markdown कागजातहरूलाई सजिलै अनुवाद गर्न मद्दत गर्छ। यो गाइडले तपाईंलाई उपकरण प्रयोग गर्दा देखिने सामान्य समस्याहरू समाधान गर्न सहयोग पुर्‍याउँछ।

## सामान्य समस्या र समाधानहरू

### १. Markdown ट्याग समस्या
**समस्या:** अनुवाद गरिएको Markdown कागजातको माथि `markdown` ट्याग देखिन्छ, जसले रेंडरिङमा समस्या ल्याउँछ।

**समाधान:** यसलाई समाधान गर्न, फाइलको माथिबाट `markdown` ट्याग हटाउनुहोस्। यसले Markdown फाइल सही रूपमा देखिन्छ।

**चरणहरू:**
1. अनुवाद गरिएको Markdown (`.md`) फाइल खोल्नुहोस्।
2. कागजातको माथि रहेको `markdown` ट्याग खोज्नुहोस्।
3. `markdown` ट्याग हटाउनुहोस्।
4. फाइल सेभ गर्नुहोस्।
5. फाइल पुन: खोल्नुहोस् र सही रूपमा देखिन्छ कि छैन जाँच गर्नुहोस्।

### २. Embedded Images URL समस्या
**समस्या:** Embedded images को URL भाषा locale सँग मेल खाँदैन, जसले गलत वा हराएका images देखिन्छ।

**समाधान:** Embedded images को URL जाँच गर्नुहोस् र भाषा locale मिलेको छ कि छैन हेर्नुहोस्। सबै images `translated_images` फोल्डरमा छन् र प्रत्येक image को फाइल नाममा भाषा locale ट्याग हुन्छ।

**चरणहरू:**
1. अनुवाद गरिएको Markdown कागजात खोल्नुहोस्।
2. Embedded images र तिनीहरूको URL पहिचान गर्नुहोस्।
3. Image फाइल नाममा भाषा locale कागजातको भाषा सँग मिलेको छ कि छैन जाँच गर्नुहोस्।
4. आवश्यक परे URL अपडेट गर्नुहोस्।
5. फाइल सेभ गरेर पुन: खोल्नुहोस् र images सही देखिन्छ कि छैन हेर्नुहोस्।

### ३. अनुवादको शुद्धता
**समस्या:** अनुवाद गरिएको सामग्री सही छैन वा थप सम्पादन आवश्यक छ।

**समाधान:** अनुवाद गरिएको कागजात समीक्षा गर्नुहोस् र आवश्यक सम्पादन गरेर शुद्धता सुधार गर्नुहोस्।

**चरणहरू:**
1. अनुवाद गरिएको कागजात खोल्नुहोस्।
2. सामग्री ध्यानपूर्वक समीक्षा गर्नुहोस्।
3. अनुवादको शुद्धता सुधार गर्न आवश्यक सम्पादन गर्नुहोस्।
4. फाइल सेभ गर्नुहोस्।

## ४. अनुमति त्रुटि Redacted वा 404

यदि images वा पाठ सही भाषामा अनुवाद भएको छैन र -d debug मोडमा चलाउँदा 401 त्रुटि देखिन्छ भने, यो authentication असफलता हो—शायद key अमान्य, सकिएको, वा endpoint को region सँग जोडिएको छैन।

Root cause बुझ्न [-d debug switch](https://github.com/Azure/co-op-translator/blob/main/getting_started/command-reference.md) प्रयोग गरेर co-op translator चलाउनुहोस्।

- **त्रुटि सन्देश**: `Access denied due to invalid subscription key or wrong API endpoint.`
- **सम्भावित कारणहरू**:
  - Subscription key अनुरोधमा redacted वा गलत छ।
  - AI Services Key वा Subscription Key फरक Azure resource (जस्तै Translator वा OpenAI) को हुन सक्छ, **Azure AI Vision** resource को सट्टा।

 **Resource Type**
  - [Azure Portal](https://portal.azure.com) वा [Azure AI Foundry](https://ai.azure.com) मा जानुहोस् र resource को प्रकार `Azure AI services` → `Vision` छ कि छैन हेर्नुहोस्।
  - Key हरू प्रमाणित गर्नुहोस् र सही key प्रयोग भएको छ कि छैन जाँच गर्नुहोस्।

## ५. कन्फिगरेसन त्रुटिहरू (नयाँ Error Handling)

नयाँ selective translation प्रणालीबाट, Co-op Translator ले आवश्यक सेवा कन्फिगर नभएको अवस्थामा स्पष्ट त्रुटि सन्देश दिन्छ।

### ५.१. Image Translation का लागि Azure AI Service कन्फिगर छैन

**समस्या:** तपाईंले image translation (`-img` flag) माग्नुभयो तर Azure AI Service सही रूपमा कन्फिगर छैन।

**त्रुटि सन्देश:**
```
Error: Image translation requested but Azure AI Service is not configured.
Please add AZURE_AI_SERVICE_API_KEY and AZURE_AI_SERVICE_ENDPOINT to your .env file.
Check Azure AI Service availability and configuration.
```

**समाधान:**
1. **विकल्प १**: Azure AI Service कन्फिगर गर्नुहोस्
   - आफ्नो `.env` फाइलमा `AZURE_AI_SERVICE_API_KEY` थप्नुहोस्
   - आफ्नो `.env` फाइलमा `AZURE_AI_SERVICE_ENDPOINT` थप्नुहोस्
   - सेवा पहुँचयोग्य छ कि छैन जाँच गर्नुहोस्

2. **विकल्प २**: Image translation अनुरोध हटाउनुहोस्
   ```bash
   # Instead of: translate -l "ko" -img
   # Use: translate -l "ko" -md
   ```

### ५.२. आवश्यक कन्फिगरेसन हराइरहेको

**समस्या:** आवश्यक LLM कन्फिगरेसन छैन।

**त्रुटि सन्देश:**
```
Error: No language model configuration found.
Please configure either Azure OpenAI or OpenAI in your .env file.
```

**समाधान:**
1. आफ्नो `.env` फाइलमा कम्तिमा एउटा LLM कन्फिगरेसन छ कि छैन जाँच गर्नुहोस्:
   - **Azure OpenAI**: `AZURE_OPENAI_API_KEY` र `AZURE_OPENAI_ENDPOINT`
   - **OpenAI**: `OPENAI_API_KEY`
   
   तपाईंलाई Azure OpenAI वा OpenAI मध्ये एक कन्फिगर गर्नुपर्छ, दुवै होइन।

### ५.३. Selective Translation भ्रम

**समस्या:** आदेश सफल भए पनि कुनै फाइल अनुवाद भएन।

**सम्भावित कारणहरू:**
- गलत फाइल प्रकार flags (`-md`, `-img`, `-nb`)
- प्रोजेक्टमा मिल्ने फाइल छैन
- गलत directory संरचना

**समाधान:**
1. **Debug मोड प्रयोग गर्नुहोस्** के भइरहेको छ हेर्न:
   ```bash
   translate -l "ko" -md -d
   ```

2. **प्रोजेक्टमा फाइल प्रकारहरू जाँच गर्नुहोस्**:
   ```bash
   # For markdown files
   find . -name "*.md" -not -path "./translations/*"
   
   # For notebooks
   find . -name "*.ipynb" -not -path "./translations/*"
   
   # For images
   find . -name "*.png" -o -name "*.jpg" -o -name "*.jpeg" -not -path "./translations/*"
   ```

3. **Flag संयोजनहरू प्रमाणित गर्नुहोस्**:
   ```bash
   # Translate everything (default)
   translate -l "ko"
   
   # Translate specific types
   translate -l "ko" -md -img
   ```

## ६. पुरानो प्रणालीबाट माइग्रेशन

### ६.१. Markdown-Only मोड हटाइएको

**समस्या:** Markdown मात्र fallback मा निर्भर आदेशहरू अब पहिले जस्तो काम गर्दैन।

**पुरानो व्यवहार:**
```bash
# This used to automatically switch to markdown-only mode
translate -l "ko"  # (when Azure AI Vision was not configured)
```

**नयाँ व्यवहार:**
```bash
# This now produces an error if image translation is requested but not configured
translate -l "ko" -img
```

**समाधान:**
- **स्पष्ट हुनुहोस्** के अनुवाद गर्न चाहनुहुन्छ:
  ```bash
  translate -l "ko" -md        # Only markdown
  translate -l "ko" -md -img   # Markdown and images
  translate -l "ko"            # Everything (if all services configured)
  ```

### ६.२. अप्रत्याशित लिंक व्यवहार

**समस्या:** अनुवाद गरिएको फाइलका लिंकहरू अप्रत्याशित स्थानमा देखिन्छ।

**कारण:** चयन गरिएको फाइल प्रकार अनुसार dynamic link processing परिवर्तन हुन्छ।

**समाधान:**
1. **नयाँ लिंक व्यवहार बुझ्नुहोस्**:
   - `-nb` समावेश: Notebook लिंकहरू अनुवादित संस्करणमा देखिन्छ
   - `-nb` बाहिर: Notebook लिंकहरू मूल फाइलमा देखिन्छ
   - `-img` समावेश: Image लिंकहरू अनुवादित संस्करणमा देखिन्छ
   - `-img` बाहिर: Image लिंकहरू मूल फाइलमा देखिन्छ

2. **आफ्नो प्रयोगका लागि सही संयोजन छान्नुहोस्**:
   ```bash
   # All internal links point to translated versions
   translate -l "ko" -md -img -nb
   
   # Only markdown translated, other links point to originals
   translate -l "ko" -md
   ```

## ७. GitHub Action चल्यो तर Pull Request (PR) बनेन

**लक्षण:** `peter-evans/create-pull-request` को workflow logs मा देखिन्छ:

> Branch 'update-translations' is not ahead of base 'main' and will not be created

**सम्भावित कारणहरू:**
- **कुनै परिवर्तन छैन:** Translation चरणले कुनै फरक ल्याएन (repo पहिले नै अपडेट छ)।
- **Ignored outputs:** `.gitignore` ले तपाईंले commit गर्न चाहेको फाइलहरूलाई exclude गर्छ (जस्तै, `*.ipynb`, `translations/`, `translated_images/`)।
- **add-paths mismatch:** Action मा दिइएको paths वास्तविक output स्थानसँग मेल खाँदैन।
- **Workflow logic/conditions:** Translation चरण चाँडै सकियो वा अप्रत्याशित directory मा लेखियो।

**कसरी समाधान गर्ने / प्रमाणित गर्ने:**
1. **Outputs छन् कि छैन जाँच गर्नुहोस्:** Translation पछि workspace मा `translations/` र/वा `translated_images/` मा नयाँ/परिवर्तित फाइल छन् कि छैन हेर्नुहोस्।
   - यदि notebook अनुवाद गर्दै हुनुहुन्छ भने, `.ipynb` फाइलहरू `translations/<lang>/...` मा लेखिएको छ कि छैन हेर्नुहोस्।
2. **`.gitignore` समीक्षा गर्नुहोस्:** Generated outputs ignore नगर्नुहोस्। सुनिश्चित गर्नुहोस् कि तपाईंले ignore गर्नुभएको छैन:
   - `translations/`
   - `translated_images/`
   - `*.ipynb` (notebook अनुवाद गर्दा)
3. **add-paths outputs सँग मेल खानुहोस्:** Multiline value प्रयोग गर्नुहोस् र दुबै फोल्डर समावेश गर्नुहोस्:
   ```yaml
   with:
     add-paths: |
       translations/
       translated_images/
   ```
4. **Debugging का लागि PR force गर्नुहोस्:** Wiring सही छ कि छैन पुष्टि गर्न अस्थायी रूपमा empty commits अनुमति दिनुहोस्:
   ```yaml
   with:
     commit-empty: true
   ```
5. **Debug मोडमा चलाउनुहोस्:** Translate command मा `-d` थप्नुहोस् जसले कुन फाइल पत्ता लाग्यो र लेखियो देखाउँछ।
6. **Permissions (GITHUB_TOKEN):** Workflow मा commits र PR बनाउन लेख्ने अनुमति छ कि छैन सुनिश्चित गर्नुहोस्:
   ```yaml
   permissions:
     contents: write
     pull-requests: write
   ```


## छिटो Debugging Checklist

Translation समस्या समाधान गर्दा:

1. **Debug मोड प्रयोग गर्नुहोस्:** विस्तृत logs हेर्न `-d` flag थप्नुहोस्
2. **आफ्नो flags जाँच गर्नुहोस्:** `-md`, `-img`, `-nb` तपाईंको उद्देश्यसँग मेल खानुहोस्
3. **कन्फिगरेसन प्रमाणित गर्नुहोस्:** आफ्नो `.env` फाइलमा आवश्यक keys छन् कि छैन हेर्नुहोस्
4. **क्रमशः परीक्षण गर्नुहोस्:** सुरुमा `-md` मात्र, त्यसपछि अन्य प्रकार थप्नुहोस्
5. **फाइल संरचना जाँच गर्नुहोस्:** स्रोत फाइलहरू छन् र पहुँचयोग्य छन् कि छैन हेर्नुहोस्

उपलब्ध आदेश र flags को विस्तृत जानकारीका लागि [Command Reference](./command-reference.md) हेर्नुहोस्।

---

**अस्वीकरण**:
यो दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरेर अनुवाद गरिएको हो। हामी शुद्धताको लागि प्रयास गर्छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादमा त्रुटि वा अशुद्धता हुन सक्छ। मूल भाषामा रहेको दस्तावेज़लाई नै अधिकारिक स्रोत मान्नुपर्छ। महत्वपूर्ण जानकारीको लागि, पेशेवर मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न हुने कुनै पनि गलतफहमी वा गलत व्याख्याको लागि हामी जिम्मेवार हुने छैनौं।