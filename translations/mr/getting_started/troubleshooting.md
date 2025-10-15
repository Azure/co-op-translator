<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6e626bef5ed78a1cc55b0dbf44f01d47",
  "translation_date": "2025-10-15T02:50:28+00:00",
  "source_file": "getting_started/troubleshooting.md",
  "language_code": "mr"
}
-->
# Microsoft Co-op Translator समस्या निवारण मार्गदर्शिका

## आढावा
Microsoft Co-Op Translator हे Markdown दस्तऐवज सहजपणे भाषांतर करण्यासाठी एक शक्तिशाली साधन आहे. हे मार्गदर्शक या साधनाचा वापर करताना येणाऱ्या सामान्य समस्यांचे निराकरण करण्यात मदत करेल.

## सामान्य समस्या आणि उपाय

### 1. Markdown टॅग समस्या
**समस्या:** भाषांतरित Markdown दस्तऐवजात वरती `markdown` टॅग दिसतो, ज्यामुळे दस्तऐवज योग्यरित्या दिसत नाही.

**उपाय:** हे सोडवण्यासाठी, फक्त फाईलच्या सुरुवातीला असलेला `markdown` टॅग काढून टाका. त्यामुळे Markdown फाईल योग्यरित्या दिसेल.

**पायऱ्या:**
1. भाषांतरित Markdown (`.md`) फाईल उघडा.
2. दस्तऐवजाच्या सुरुवातीला `markdown` टॅग शोधा.
3. तो टॅग काढून टाका.
4. फाईल सेव्ह करा.
5. फाईल पुन्हा उघडा आणि ती योग्यरित्या दिसते का ते तपासा.

### 2. एम्बेडेड इमेजेस URL समस्या
**समस्या:** एम्बेड केलेल्या इमेजेसचे URL भाषा लोकलशी जुळत नाहीत, त्यामुळे चुकीच्या किंवा गायब इमेजेस दिसतात.

**उपाय:** एम्बेड केलेल्या इमेजेसचे URL तपासा आणि ते भाषा लोकलशी जुळतात का ते पहा. सर्व इमेजेस `translated_images` फोल्डरमध्ये आहेत आणि प्रत्येक इमेजच्या नावात भाषा लोकल टॅग आहे.

**पायऱ्या:**
1. भाषांतरित Markdown दस्तऐवज उघडा.
2. एम्बेड केलेल्या इमेजेस आणि त्यांचे URL शोधा.
3. इमेज फाईलच्या नावातील भाषा लोकल दस्तऐवजाच्या भाषेशी जुळते का ते तपासा.
4. गरज असल्यास URL अपडेट करा.
5. फाईल सेव्ह करा आणि पुन्हा उघडा, इमेजेस योग्यरित्या दिसतात का ते पहा.

### 3. भाषांतर अचूकता
**समस्या:** भाषांतरित मजकूर अचूक नाही किंवा अजून संपादनाची गरज आहे.

**उपाय:** भाषांतरित दस्तऐवज तपासा आणि आवश्यक संपादन करा जेणेकरून अचूकता आणि वाचनीयता वाढेल.

**पायऱ्या:**
1. भाषांतरित दस्तऐवज उघडा.
2. मजकूर काळजीपूर्वक वाचा.
3. आवश्यक संपादन करा.
4. फाईल सेव्ह करा.

## 4. परवानगी त्रुटी Redacted किंवा 404

जर इमेजेस किंवा मजकूर योग्य भाषेत भाषांतरित होत नसेल आणि -d debug मोडमध्ये 401 त्रुटी येत असेल, तर ही ओळखीची प्रमाणीकरण अयशस्वी स्थिती आहे—किंवा की अवैध आहे, कालबाह्य झाली आहे, किंवा योग्य region शी लिंक केलेली नाही.

मूळ कारण समजून घेण्यासाठी co-op translator [-d debug switch](https://github.com/Azure/co-op-translator/blob/main/getting_started/command-reference.md) सह चालवा.

- **त्रुटी संदेश:** `Access denied due to invalid subscription key or wrong API endpoint.`
- **संभाव्य कारणे:**
  - Subscription key विनंतीमध्ये चुकीची किंवा redacted आहे.
  - AI Services Key किंवा Subscription Key कदाचित Translator किंवा OpenAI सारख्या वेगळ्या Azure resource ची आहे, **Azure AI Vision** resource ची नाही.

 **Resource Type**
  - [Azure Portal](https://portal.azure.com) किंवा [Azure AI Foundry](https://ai.azure.com) वर जा आणि resource `Azure AI services` → `Vision` प्रकाराची आहे का ते तपासा.
  - की तपासा आणि योग्य की वापरली आहे का ते खात्री करा.

## 5. कॉन्फिगरेशन त्रुटी (नवीन त्रुटी हाताळणी)

नवीन selective translation प्रणालीपासून, Co-op Translator आता आवश्यक सेवा कॉन्फिगर नसल्यास स्पष्ट त्रुटी संदेश देतो.

### 5.1. इमेज भाषांतरासाठी Azure AI Service कॉन्फिगर नाही

**समस्या:** तुम्ही इमेज भाषांतर (`-img` flag) मागितले आहे पण Azure AI Service योग्यरित्या कॉन्फिगर केलेली नाही.

**त्रुटी संदेश:**
```
Error: Image translation requested but Azure AI Service is not configured.
Please add AZURE_AI_SERVICE_API_KEY and AZURE_AI_SERVICE_ENDPOINT to your .env file.
Check Azure AI Service availability and configuration.
```

**उपाय:**
1. **पर्याय 1:** Azure AI Service कॉन्फिगर करा
   - `AZURE_AI_SERVICE_API_KEY` तुमच्या `.env` फाईलमध्ये जोडा
   - `AZURE_AI_SERVICE_ENDPOINT` तुमच्या `.env` फाईलमध्ये जोडा
   - सेवा उपलब्ध आहे का ते तपासा

2. **पर्याय 2:** इमेज भाषांतराची विनंती काढून टाका
   ```bash
   # Instead of: translate -l "ko" -img
   # Use: translate -l "ko" -md
   ```

### 5.2. आवश्यक कॉन्फिगरेशन गायब

**समस्या:** आवश्यक LLM कॉन्फिगरेशन उपलब्ध नाही.

**त्रुटी संदेश:**
```
Error: No language model configuration found.
Please configure either Azure OpenAI or OpenAI in your .env file.
```

**उपाय:**
1. तुमच्या `.env` फाईलमध्ये खालीलपैकी किमान एक LLM कॉन्फिगरेशन आहे का ते तपासा:
   - **Azure OpenAI**: `AZURE_OPENAI_API_KEY` आणि `AZURE_OPENAI_ENDPOINT`
   - **OpenAI**: `OPENAI_API_KEY`
   
   तुम्हाला Azure OpenAI किंवा OpenAI यापैकी एकच कॉन्फिगर करावे लागेल, दोन्ही नाही.

### 5.3. Selective Translation गोंधळ

**समस्या:** कमांड यशस्वी झाली तरी कोणतीही फाईल भाषांतरित झाली नाही.

**संभाव्य कारणे:**
- चुकीचे फाईल टाईप फ्लॅग्स (`-md`, `-img`, `-nb`)
- प्रोजेक्टमध्ये जुळणाऱ्या फाईल्स नाहीत
- चुकीची डिरेक्टरी रचना

**उपाय:**
1. **Debug मोड वापरा** आणि काय घडतेय ते पहा:
   ```bash
   translate -l "ko" -md -d
   ```

2. **प्रोजेक्टमधील फाईल टाईप्स तपासा:**
   ```bash
   # For markdown files
   find . -name "*.md" -not -path "./translations/*"
   
   # For notebooks
   find . -name "*.ipynb" -not -path "./translations/*"
   
   # For images
   find . -name "*.png" -o -name "*.jpg" -o -name "*.jpeg" -not -path "./translations/*"
   ```

3. **फ्लॅग्सची योग्य कॉम्बिनेशन तपासा:**
   ```bash
   # Translate everything (default)
   translate -l "ko"
   
   # Translate specific types
   translate -l "ko" -md -img
   ```

## 6. जुन्या प्रणालीमधून स्थलांतर

### 6.1. Markdown-Only मोड बंद

**समस्या:** पूर्वी markdown-only fallback वर अवलंबून असलेल्या कमांड्स आता अपेक्षेप्रमाणे काम करत नाहीत.

**जुना वर्तन:**
```bash
# This used to automatically switch to markdown-only mode
translate -l "ko"  # (when Azure AI Vision was not configured)
```

**नवीन वर्तन:**
```bash
# This now produces an error if image translation is requested but not configured
translate -l "ko" -img
```

**उपाय:**
- **स्पष्टपणे सांगा** तुम्हाला काय भाषांतरित करायचे आहे:
  ```bash
  translate -l "ko" -md        # Only markdown
  translate -l "ko" -md -img   # Markdown and images
  translate -l "ko"            # Everything (if all services configured)
  ```

### 6.2. अनपेक्षित लिंक वर्तन

**समस्या:** भाषांतरित फाईल्समधील लिंक्स अनपेक्षित ठिकाणी दाखवतात.

**कारण:** निवडलेल्या फाईल टाईप्सनुसार डायनॅमिक लिंक प्रक्रिया बदलते.

**उपाय:**
1. **नवीन लिंक वर्तन समजून घ्या:**
   - `-nb` समाविष्ट: Notebook लिंक्स भाषांतरित आवृत्तीकडे दाखवतात
   - `-nb` वगळले: Notebook लिंक्स मूळ फाईल्सकडे दाखवतात
   - `-img` समाविष्ट: इमेज लिंक्स भाषांतरित आवृत्तीकडे दाखवतात
   - `-img` वगळले: इमेज लिंक्स मूळ फाईल्सकडे दाखवतात

2. **तुमच्या वापरासाठी योग्य कॉम्बिनेशन निवडा:**
   ```bash
   # All internal links point to translated versions
   translate -l "ko" -md -img -nb
   
   # Only markdown translated, other links point to originals
   translate -l "ko" -md
   ```

## 7. GitHub Action चालली पण Pull Request (PR) तयार झाला नाही

**लक्षण:** `peter-evans/create-pull-request` साठी workflow logs मध्ये दिसते:

> Branch 'update-translations' is not ahead of base 'main' and will not be created

**संभाव्य कारणे:**
- **कोणतेही बदल नाहीत:** भाषांतर स्टेपने कोणतेही फरक निर्माण केले नाहीत (repo आधीच अपडेट आहे).
- **outputs दुर्लक्षित:** `.gitignore` मध्ये तुम्हाला अपेक्षित असलेल्या फाईल्स वगळल्या आहेत (उदा. `*.ipynb`, `translations/`, `translated_images/`).
- **add-paths mismatch:** action ला दिलेले paths आणि प्रत्यक्ष output paths जुळत नाहीत.
- **Workflow logic/conditions:** भाषांतर स्टेप लवकर थांबली किंवा अनपेक्षित डिरेक्टरीमध्ये लिहिले.

**कसे दुरुस्त करावे / तपासावे:**
1. **outputs अस्तित्वात आहेत का ते तपासा:** भाषांतरानंतर, workspace मध्ये `translations/` आणि/किंवा `translated_images/` मध्ये नवीन/बदललेल्या फाईल्स आहेत का ते पहा.
   - Notebook चे भाषांतर करत असाल, तर `.ipynb` फाईल्स `translations/<lang>/...` मध्ये लिहिल्या आहेत का ते तपासा.
2. **`.gitignore` तपासा:** तयार झालेले outputs वगळू नका. हे वगळू नका:
   - `translations/`
   - `translated_images/`
   - `*.ipynb` (notebook चे भाषांतर करत असाल तर)
3. **add-paths outputs शी जुळतात का ते तपासा:** मल्टीलाइन value वापरा आणि दोन्ही फोल्डर्स समाविष्ट करा:
   ```yaml
   with:
     add-paths: |
       translations/
       translated_images/
   ```
4. **debug साठी PR जबरदस्तीने तयार करा:** wiring योग्य आहे का हे तपासण्यासाठी तात्पुरते रिकामे commits परवानगी द्या:
   ```yaml
   with:
     commit-empty: true
   ```
5. **debug सह चालवा:** translate कमांडला `-d` जोडा, कोणत्या फाईल्स सापडल्या आणि लिहिल्या हे पाहण्यासाठी.
6. **Permissions (GITHUB_TOKEN):** workflow ला commits आणि PR तयार करण्यासाठी write permissions आहेत का ते तपासा:
   ```yaml
   permissions:
     contents: write
     pull-requests: write
   ```


## जलद समस्या निवारण तपासणी

भाषांतराच्या समस्यांचे निराकरण करताना:

1. **debug मोड वापरा:** तपशीलवार logs पाहण्यासाठी `-d` फ्लॅग जोडा
2. **फ्लॅग्स तपासा:** `-md`, `-img`, `-nb` तुमच्या उद्देशाशी जुळतात का ते पहा
3. **कॉन्फिगरेशन तपासा:** तुमच्या `.env` फाईलमध्ये आवश्यक keys आहेत का ते पहा
4. **हळूहळू चाचणी करा:** फक्त `-md` ने सुरुवात करा, मग इतर टाईप्स जोडा
5. **फाईल स्ट्रक्चर तपासा:** स्रोत फाईल्स अस्तित्वात आहेत आणि उपलब्ध आहेत का ते पहा

अधिक तपशीलवार माहिती आणि कमांड्स/फ्लॅग्ससाठी [Command Reference](./command-reference.md) पहा.

---

**अस्वीकरण**:
हे दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून भाषांतरित केले आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी, कृपया लक्षात घ्या की स्वयंचलित भाषांतरांमध्ये चुका किंवा अपूर्णता असू शकतात. मूळ भाषेतील दस्तऐवज हा अधिकृत स्रोत मानावा. अत्यावश्यक माहितीसाठी, व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराचा वापर करून झालेल्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थासाठी आम्ही जबाबदार राहणार नाही.