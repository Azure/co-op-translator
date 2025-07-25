<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d238206c3503631e32774716d11d1868",
  "translation_date": "2025-06-12T18:45:50+00:00",
  "source_file": "getting_started/command-line-guide/translator-your-project.md",
  "language_code": "ne"
}
-->
# Co-op Translator प्रयोग गरेर आफ्नो परियोजना अनुवाद गर्नुहोस्

**Co-op Translator** एउटा कमाण्ड-लाइन इन्टरफेस (CLI) उपकरण हो जसले तपाईंलाई आफ्नो परियोजनाका markdown र छवि फाइलहरू विभिन्न भाषामा अनुवाद गर्न मद्दत गर्छ। यो भागले उपकरण कसरी प्रयोग गर्ने, विभिन्न CLI विकल्पहरू, र विभिन्न प्रयोगका उदाहरणहरू व्याख्या गर्दछ।

> [!NOTE]
> कमाण्डहरूको पूर्ण सूची र तिनीहरूको विस्तृत विवरणका लागि, कृपया [Command reference](./command-reference.md) हेर्नुहोस्।

---

## उदाहरण परिदृश्य र कमाण्डहरू

यहाँ **Co-op Translator** का केही सामान्य प्रयोगहरू र तिनीहरूका लागि उपयुक्त कमाण्डहरू प्रस्तुत छन्।

### १. आधारभूत अनुवाद (एकल भाषा)

तपाईंको सम्पूर्ण परियोजना (markdown फाइलहरू र छविहरू) लाई एउटा मात्र भाषामा, जस्तै कोरियनमा अनुवाद गर्न, तलको कमाण्ड प्रयोग गर्नुहोस्:

```bash
translate -l "ko"
```

यो कमाण्डले सबै markdown र छवि फाइलहरू कोरियनमा अनुवाद गर्नेछ, र नयाँ अनुवाद थप्नेछ तर पहिलेका अनुवादहरू मेट्ने छैन।

> [!TIP]
>
> के तपाईं जान्न चाहनुहुन्छ कि **Co-op Translator** मा कुन भाषा कोडहरू उपलब्ध छन्? थप विवरणका लागि रिपोजिटोरीमा रहेको [Supported Languages](https://github.com/Azure/co-op-translator#supported-languages) सेक्सन हेर्नुहोस्।

#### Phi-3 CookBook मा उदाहरण

**Phi-3 CookBook** मा मैले पहिलेका markdown फाइलहरू र छविहरूको कोरियन अनुवाद थप्न निम्न विधि प्रयोग गरेको थिएँ।

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko"
Translating images: 100%|███████████████████████████████████████████████████| 276/276 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 153/153 [1:43:07<00:00, 241.31s/it]
```

### २. बहुभाषी अनुवाद

तपाईंको परियोजनालाई स्पेनिश, फ्रेन्च, र जर्मन जस्ता धेरै भाषामा अनुवाद गर्न यो कमाण्ड प्रयोग गर्नुहोस्:

```bash
translate -l "es fr de"
```

यो कमाण्डले परियोजनालाई स्पेनिश, फ्रेन्च, र जर्मनमा अनुवाद गर्नेछ, नयाँ अनुवाद थप्नेछ तर पहिलेका अनुवादहरू मेट्ने छैन।

#### Phi-3 CookBook मा उदाहरण

**Phi-3 CookBook** मा मैले सबैभन्दा नयाँ कमिटहरू प्रतिबिम्बित गर्न पछिल्लो परिवर्तनहरू तानिसकेपछि, नयाँ थपिएका markdown फाइलहरू र छविहरू अनुवाद गर्न निम्न विधि प्रयोग गरेको थिएँ।

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko ja zh tw es fr" -a
Translating images: 100%|███████████████████████████████████████████████████| 273/273 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 6/6 [24:07<00:00, 241.31s/it]
```

> [!NOTE]
> सामान्यतया एकै पटक एक भाषा अनुवाद गर्नु सिफारिस गरिन्छ, तर यस्तो अवस्थामा जहाँ विशेष परिवर्तनहरू थप्नुपर्छ, धेरै भाषाहरू एकै पटक अनुवाद गर्नु प्रभावकारी हुन सक्छ।

### ३. अनुवाद अपडेट गर्नुहोस् (पहिलेका अनुवादहरू मेटिन्छ)

पहिलेका अनुवादहरू हटाएर नयाँ अनुवाद राख्न `-u` विकल्प प्रयोग गर्नुहोस्। यसले निर्दिष्ट भाषाका सबै अनुवादहरू मेट्ने र पुन: अनुवाद गर्नेछ।

```bash
translate -l "ko" -u
```

सावधान: यो कमाण्डले पहिलेका अनुवादहरू मेट्न अघि तपाईंलाई पुष्टिकरण सोध्नेछ।

#### Phi-3 CookBook मा उदाहरण

**Phi-3 CookBook** मा मैले स्पेनिशमा सबै अनुवादित फाइलहरू अपडेट गर्न निम्न विधि प्रयोग गरेको थिएँ। मूल सामग्रीमा धेरै महत्वपूर्ण परिवर्तनहरू हुँदा यो विधि सिफारिस गरिन्छ। यदि केवल केही अनुवादित markdown फाइलहरू मात्र अपडेट गर्नुपर्ने हो भने, ती फाइलहरू म्यानुअली मेटेर `-a` विधि प्रयोग गर्नु बढी प्रभावकारी हुन्छ।

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "es" -u
Warning: The update command will delete all existing translations for 'es' and re-translate everything.
Do you want to continue? Type 'yes' to proceed: yes
Proceeding with update...
Translating images: 100%|████████████████████████████████████████████| 150/150 [43:46<00:00, 15.55s/it]
Translating markdown files: 100%|███████████████████████████████████| 95/95 [1:40:27<00:00, 125.62s/it]
```

### ५. केवल छविहरू अनुवाद गर्नुहोस्

परियोजनाका केवल छवि फाइलहरू अनुवाद गर्न `-img` विकल्प प्रयोग गर्नुहोस्:

```bash
translate -l "ko" -img
```

यो कमाण्डले केवल छविहरूलाई कोरियनमा अनुवाद गर्नेछ, markdown फाइलहरूलाई असर नगरी।

### ६. केवल Markdown फाइलहरू अनुवाद गर्नुहोस्

परियोजनाका केवल markdown फाइलहरू अनुवाद गर्न `-md` विकल्प प्रयोग गर्नुहोस्:

```bash
translate -l "ko" -md
```

### ७. अनुवादित फाइलहरूमा त्रुटि जाँच गर्नुहोस्

अनुवादित फाइलहरूमा त्रुटि छ कि छैन जाँच्न र आवश्यक परे पुनः अनुवाद प्रयास गर्न `-chk` विकल्प प्रयोग गर्नुहोस्:

```bash
translate -l "ko" -chk
```

यो कमाण्डले अनुवादित markdown फाइलहरू स्क्यान गर्नेछ र त्रुटि भएका फाइलहरूको पुनः अनुवाद गर्नेछ।

#### Phi-3 CookBook मा उदाहरण

**Phi-3 CookBook** मा मैले कोरियन फाइलहरूमा अनुवाद त्रुटि जाँच गर्न र कुनै समस्या देखिएमा स्वतः पुनः अनुवाद प्रयास गर्न निम्न विधि प्रयोग गरेको थिएँ।

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko" -chk 
Checking translated files for errors in ko...
Checking files for ko: 100%|██████████████████████████████████████████████████| 95/95 [00:01<00:00, 65.47file/s]
Retrying vsc-extension-quickstart.md for ko:   0%|                                     | 0/17 [00:00<?, ?file/s] 
```

यो विकल्प अनुवाद त्रुटिहरू जाँच गर्छ। हालको अवस्थामा, मूल र अनुवादित फाइलबीच लाइन ब्रेकहरूको भिन्नता ६ भन्दा बढी भएमा फाइललाई अनुवाद त्रुटि भएको मानिन्छ। भविष्यमा यो मापदण्डलाई अझ लचिलो बनाउन योजना छ।

उदाहरणका लागि, यो विधि हराएका खण्ड वा बिग्रिएका अनुवाद पत्ता लगाउन उपयोगी छ र ती फाइलहरूको स्वतः पुनः अनुवाद गर्छ।

तर यदि तपाईंलाई पहिले नै कुन फाइलहरू समस्या भएको थाहा छ भने, ती फाइलहरू म्यानुअली मेटेर `-a` option to re-translate them.

### 8. Debug Mode

To enable detailed logging for troubleshooting, use the `-d` विकल्प प्रयोग गर्नु बढी प्रभावकारी हुन्छ:

```bash
translate -l "ko" -d
```

यो कमाण्डले डिबग मोडमा अनुवाद चलाउनेछ, जसले थप लगिङ जानकारी प्रदान गर्छ र अनुवाद प्रक्रियामा समस्या पत्ता लगाउन मद्दत गर्छ।

#### Phi-3 CookBook मा उदाहरण

**Phi-3 CookBook** मा मैले यस्तो समस्या देखेँ जहाँ धेरै लिंक भएका markdown फाइलहरूमा अनुवाद गर्दा फर्म्याटिङ त्रुटि आउँथ्यो, जस्तै टुटेका अनुवाद र नजरअन्दाज गरिएका लाइन ब्रेकहरू। यो समस्या पत्ता लगाउन मैले `-d` विकल्प प्रयोग गरेर अनुवाद प्रक्रिया कसरी काम गर्छ हेरेँ।

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "ko" -d
DEBUG:openai._base_client:Request options: {'method': 'post', 'url': '/chat/completions', 'headers': {'api-key': 'af04e0bea45747d8a7b8c131c1971044'}, 'files': None, 'json_data': {'messages': [{'role': 'user', 'content': "Translate the following text to ko. NEVER ADD ANY EXTRA CONTENT OUTSIDE THE TRANSLATION. TRANSLATE ONLY WHAT IS GIVEN TO YOU.. MAINTAIN MARKDOWN FORMAT\n\n# Phi-3 Cookbook: Hands-On Examples with Microsoft's Phi-3 Models [![Open and use the samples in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phi-3cookbook) [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%
...
```

### ९. सबै भाषाहरू अनुवाद गर्नुहोस्

परियोजनालाई उपलब्ध सबै भाषामा अनुवाद गर्न `all` कीवर्ड प्रयोग गर्नुहोस्।

> [!WARNING]
> सबै भाषाहरू एकै पटक अनुवाद गर्दा परियोजनाको आकारअनुसार धेरै समय लाग्न सक्छ। उदाहरणका लागि, **Phi-3 CookBook** लाई स्पेनिशमा अनुवाद गर्न लगभग २ घण्टा लागेको थियो। यति ठूलो परिमाणका लागि एकै व्यक्तिले २० भाषाहरू सम्हाल्नु व्यवहारिक छैन। यसकारण, धेरै सहभागीहरूबीच काम बाँडफाँड गरेर प्रत्येकले एक वा दुई भाषा सम्हाल्ने र क्रमशः अनुवाद अपडेट गर्ने सिफारिस गरिन्छ।

```bash
translate -l "all"
```

यो कमाण्डले परियोजनालाई उपलब्ध सबै भाषामा अनुवाद गर्नेछ। यदि तपाईं अघि बढ्नुभयो भने, परियोजनाको आकार अनुसार अनुवादमा धेरै समय लाग्न सक्छ।

> [!TIP]
>
> ### अनुवादित फाइलहरू म्यानुअली मेट्ने (वैकल्पिक)
> स्रोत फाइल अपडेट हुँदा अनुवादित फाइलहरू स्वतः पत्ता लगाइ सफा गरिन्छ।
>
> तर यदि तपाईंले म्यानुअली अनुवाद अपडेट गर्न चाहनुहुन्छ — उदाहरणका लागि, कुनै विशेष फाइल पुनः गर्न वा सिस्टम व्यवहारलाई ओभरराइड गर्न — तपाईंले तलको कमाण्ड प्रयोग गरेर सबै भाषाका फोल्डरहरूमा फाइलका सबै संस्करणहरू मेट्न सक्नुहुन्छ।
>
> ### Windows मा:
> १. **Command Prompt प्रयोग गरेर**:
>    - Command Prompt खोल्नुहोस्।
>    - `cd` कमाण्ड प्रयोग गरी फाइलहरू रहेको फोल्डरमा जानुहोस्।
>    - फाइलहरू मेट्न तलको कमाण्ड प्रयोग गर्नुहोस्:
>      ```
>      del /s *filename*
>      ```
>      यहाँ `filename` with the specific part of the file name you're looking for. The `/s` विकल्पले सबडिरेक्टोरीहरू पनि खोज्छ।
>
> २. **PowerShell प्रयोग गरेर**:
>    - PowerShell खोल्नुहोस्।
>    - यो कमाण्ड चलाउनुहोस्:
>      ```powershell
>      Get-ChildItem -Path "C:\YourPath" -Filter "*filename*" -Recurse | Remove-Item -Force
>      ```
>      यहाँ `"C:\YourPath"` with the folder path and `filename` with the specific name.
>
> ### On macOS/Linux:
> 1. **Using Terminal**:
>   - Open Terminal.
>   - Navigate to the directory with `cd`.
>   - Use the `find` कमाण्ड प्रयोग गरेर फाइल खोजिन्छ:
>     ```bash
>     find . -type f -name "*filename*" -delete
>     ```
>     यहाँ `filename` with the specific name.
>
> Always double-check the files before deleting to avoid accidental loss. 
>
> Once you have deleted the files which need to be replace simply rerun your `translate -l` कमाण्ड प्रयोग गरेर सबैभन्दा नयाँ फाइल परिवर्तनहरू अपडेट गर्न सकिन्छ।

**अस्वीकरण**:  
यो दस्तावेज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरेर अनुवाद गरिएको हो। हामी शुद्धताको लागि प्रयासरत छौं, तर कृपया जानकार रहनुहोस् कि स्वचालित अनुवादमा त्रुटिहरू वा अशुद्धता हुन सक्छ। मूल दस्तावेज यसको मातृ भाषामा अधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीको लागि व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलतफहमी वा गलत व्याख्याको लागि हामी जिम्मेवार छैनौं।