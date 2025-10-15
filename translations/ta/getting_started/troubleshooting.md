<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6e626bef5ed78a1cc55b0dbf44f01d47",
  "translation_date": "2025-10-15T04:49:25+00:00",
  "source_file": "getting_started/troubleshooting.md",
  "language_code": "ta"
}
-->
# Microsoft Co-op Translator சிக்கல் தீர்வு வழிகாட்டி

## மேலோட்டம்
Microsoft Co-Op Translator என்பது Markdown ஆவணங்களை எளிதாக மொழிபெயர்க்கும் சக்திவாய்ந்த கருவி. இந்த வழிகாட்டி, இந்த கருவியை பயன்படுத்தும்போது ஏற்படும் பொதுவான சிக்கல்களை எளிதில் தீர்க்க உதவும்.

## பொதுவான சிக்கல்கள் மற்றும் தீர்வுகள்

### 1. Markdown Tag சிக்கல்
**சிக்கல்:** மொழிபெயர்க்கப்பட்ட Markdown ஆவணத்தின் மேல் பகுதியில் `markdown` tag இருப்பதால், சரியாக காண்பிக்க முடியவில்லை.

**தீர்வு:** இதை சரி செய்ய, ஆவணத்தின் மேல் உள்ள `markdown` tag-ஐ நீக்குங்கள். இதனால் Markdown ஆவணம் சரியாக காண்பிக்கப்படும்.

**படி:**
1. மொழிபெயர்க்கப்பட்ட Markdown (`.md`) கோப்பை திறக்கவும்.
2. ஆவணத்தின் மேல் பகுதியில் உள்ள `markdown` tag-ஐ கண்டறியவும்.
3. அந்த tag-ஐ நீக்கவும்.
4. கோப்பை சேமிக்கவும்.
5. மீண்டும் கோப்பை திறந்து சரியாக காண்பிக்கப்படுகிறதா என உறுதி செய்யவும்.

### 2. பட URL சிக்கல்
**சிக்கல்:** உட்பொதிக்கப்பட்ட பட URL-கள் மொழி locale-ஐ பொருந்தவில்லை; தவறான அல்லது காணாமல் போன படங்கள்.

**தீர்வு:** உட்பொதிக்கப்பட்ட பட URL-களை சரிபார்த்து, அவை மொழி locale-ஐ பொருந்துகிறதா என உறுதி செய்யவும். அனைத்து படங்களும் `translated_images` என்ற கோப்பகத்தில் உள்ளன; ஒவ்வொரு படத்திலும் மொழி locale tag உள்ளது.

**படி:**
1. மொழிபெயர்க்கப்பட்ட Markdown ஆவணத்தை திறக்கவும்.
2. உட்பொதிக்கப்பட்ட படங்கள் மற்றும் அவற்றின் URL-களை கண்டறியவும்.
3. பட கோப்பின் பெயரில் உள்ள மொழி locale ஆவணத்தின் மொழியுடன் பொருந்துகிறதா என உறுதி செய்யவும்.
4. தேவையானால் URL-களை புதுப்பிக்கவும்.
5. சேமித்து, மீண்டும் திறந்து படங்கள் சரியாக காண்பிக்கப்படுகிறதா என உறுதி செய்யவும்.

### 3. மொழிபெயர்ப்பு துல்லியம்
**சிக்கல்:** மொழிபெயர்க்கப்பட்ட உள்ளடக்கம் துல்லியமாக இல்லை அல்லது மேலும் திருத்தம் தேவை.

**தீர்வு:** மொழிபெயர்க்கப்பட்ட ஆவணத்தை கவனமாக பரிசீலித்து, தேவையான திருத்தங்களை செய்யவும்.

**படி:**
1. மொழிபெயர்க்கப்பட்ட ஆவணத்தை திறக்கவும்.
2. உள்ளடக்கத்தை கவனமாக பரிசீலிக்கவும்.
3. மொழிபெயர்ப்பு துல்லியத்தை மேம்படுத்த தேவையான திருத்தங்களை செய்யவும்.
4. சேமிக்கவும்.

## 4. அனுமதி பிழை Redacted அல்லது 404

படங்கள் அல்லது உரை சரியான மொழிக்கு மொழிபெயர்க்கப்படவில்லை மற்றும் -d debug mode-ல் இயக்கும்போது 401 பிழை வருகிறது. இது authentication failure—key தவறானது, காலாவதியானது, அல்லது endpoint-இன் region-க்கு இணைக்கப்படவில்லை.

[d debug switch](https://github.com/Azure/co-op-translator/blob/main/getting_started/command-reference.md) மூலம் co-op translator-ஐ இயக்கி, காரணத்தை மேலும் புரிந்து கொள்ளுங்கள்.

- **பிழை செய்தி**: `Access denied due to invalid subscription key or wrong API endpoint.`
- **சாத்தியமான காரணங்கள்**:
  - Subscription key redacted அல்லது தவறாக request-ல் உள்ளது.
  - AI Services Key அல்லது Subscription Key வேறு Azure resource-க்கு (Translator அல்லது OpenAI) சொந்தமானது, **Azure AI Vision** resource-க்கு அல்ல.

 **Resource வகை**
  - [Azure Portal](https://portal.azure.com) அல்லது [Azure AI Foundry](https://ai.azure.com) சென்று resource வகை `Azure AI services` → `Vision` என்பதை உறுதி செய்யவும்.
  - Key-களை சரிபார்த்து, சரியான key பயன்படுத்தப்படுகிறதா என உறுதி செய்யவும்.

## 5. அமைப்பு பிழைகள் (புதிய பிழை கையாளுதல்)

புதிய selective translation அமைப்பில், Co-op Translator தேவையான சேவைகள் அமைக்கப்படவில்லை என்றால் தெளிவான பிழை செய்திகளை வழங்குகிறது.

### 5.1. பட மொழிபெயர்ப்புக்கு Azure AI Service அமைக்கப்படவில்லை

**சிக்கல்:** பட மொழிபெயர்ப்பு (`-img` flag) கோரியுள்ளீர்கள், ஆனால் Azure AI Service சரியாக அமைக்கப்படவில்லை.

**பிழை செய்தி:**
```
Error: Image translation requested but Azure AI Service is not configured.
Please add AZURE_AI_SERVICE_API_KEY and AZURE_AI_SERVICE_ENDPOINT to your .env file.
Check Azure AI Service availability and configuration.
```

**தீர்வு:**
1. **விருப்பம் 1**: Azure AI Service-ஐ அமைக்கவும்
   - உங்கள் `.env` கோப்பில் `AZURE_AI_SERVICE_API_KEY` சேர்க்கவும்
   - உங்கள் `.env` கோப்பில் `AZURE_AI_SERVICE_ENDPOINT` சேர்க்கவும்
   - சேவை அணுகக்கூடியதா என உறுதி செய்யவும்

2. **விருப்பம் 2**: பட மொழிபெயர்ப்பு கோரிக்கையை நீக்கவும்
   ```bash
   # Instead of: translate -l "ko" -img
   # Use: translate -l "ko" -md
   ```

### 5.2. தேவையான அமைப்பு இல்லை

**சிக்கல்:** முக்கிய LLM அமைப்பு இல்லை.

**பிழை செய்தி:**
```
Error: No language model configuration found.
Please configure either Azure OpenAI or OpenAI in your .env file.
```

**தீர்வு:**
1. உங்கள் `.env` கோப்பில் குறைந்தது ஒரு LLM அமைப்பு உள்ளதா என உறுதி செய்யவும்:
   - **Azure OpenAI**: `AZURE_OPENAI_API_KEY` மற்றும் `AZURE_OPENAI_ENDPOINT`
   - **OpenAI**: `OPENAI_API_KEY`
   
   Azure OpenAI அல்லது OpenAI ஒன்று இருந்தால் போதும், இரண்டும் தேவையில்லை.

### 5.3. Selective Translation குழப்பம்

**சிக்கல்:** கட்டளை வெற்றிகரமாக இயங்கினாலும் எந்த கோப்பும் மொழிபெயர்க்கப்படவில்லை.

**சாத்தியமான காரணங்கள்:**
- தவறான file type flags (`-md`, `-img`, `-nb`)
- திட்டத்தில் பொருந்தும் கோப்புகள் இல்லை
- தவறான கோப்பக அமைப்பு

**தீர்வு:**
1. **Debug mode** பயன்படுத்தி என்ன நடக்கிறது என பார்க்கவும்:
   ```bash
   translate -l "ko" -md -d
   ```

2. **Project-இல் file types**-ஐ சரிபார்க்கவும்:
   ```bash
   # For markdown files
   find . -name "*.md" -not -path "./translations/*"
   
   # For notebooks
   find . -name "*.ipynb" -not -path "./translations/*"
   
   # For images
   find . -name "*.png" -o -name "*.jpg" -o -name "*.jpeg" -not -path "./translations/*"
   ```

3. **Flag சேர்க்கும் முறையை** உறுதி செய்யவும்:
   ```bash
   # Translate everything (default)
   translate -l "ko"
   
   # Translate specific types
   translate -l "ko" -md -img
   ```

## 6. பழைய அமைப்பிலிருந்து மாற்றம்

### 6.1. Markdown-Only Mode நீக்கப்பட்டது

**சிக்கல்:** Markdown-only fallback-ஐ நம்பிய கட்டளைகள் இனி எதிர்பார்த்தபடி வேலை செய்யாது.

**பழைய நடத்தை:**
```bash
# This used to automatically switch to markdown-only mode
translate -l "ko"  # (when Azure AI Vision was not configured)
```

**புதிய நடத்தை:**
```bash
# This now produces an error if image translation is requested but not configured
translate -l "ko" -img
```

**தீர்வு:**
- **நீங்கள் மொழிபெயர்க்க விரும்பும் வகையை தெளிவாக குறிப்பிடவும்:**
  ```bash
  translate -l "ko" -md        # Only markdown
  translate -l "ko" -md -img   # Markdown and images
  translate -l "ko"            # Everything (if all services configured)
  ```

### 6.2. எதிர்பாராத Link நடத்தை

**சிக்கல்:** மொழிபெயர்க்கப்பட்ட கோப்புகளில் உள்ள இணைப்புகள் எதிர்பாராத இடங்களை நோக்கி செல்கின்றன.

**காரணம்:** தேர்ந்தெடுத்த file types-ஐ பொறுத்து dynamic link processing மாறும்.

**தீர்வு:**
1. **புதிய link நடத்தை புரிந்து கொள்ளவும்:**
   - `-nb` சேர்க்கப்பட்டால்: Notebook links மொழிபெயர்க்கப்பட்ட பதிப்பை நோக்கி செல்கின்றன
   - `-nb` சேர்க்கப்படவில்லை: Notebook links மூல கோப்புகளை நோக்கி செல்கின்றன
   - `-img` சேர்க்கப்பட்டால்: Image links மொழிபெயர்க்கப்பட்ட பதிப்பை நோக்கி செல்கின்றன
   - `-img` சேர்க்கப்படவில்லை: Image links மூல கோப்புகளை நோக்கி செல்கின்றன

2. **உங்கள் தேவைக்கு சரியான சேர்க்கை தேர்வு செய்யவும்:**
   ```bash
   # All internal links point to translated versions
   translate -l "ko" -md -img -nb
   
   # Only markdown translated, other links point to originals
   translate -l "ko" -md
   ```

## 7. GitHub Action இயங்கியது ஆனால் Pull Request (PR) உருவாக்கப்படவில்லை

**அறிகுறி:** `peter-evans/create-pull-request`-இன் workflow logs-ல்:

> Branch 'update-translations' is not ahead of base 'main' and will not be created

**சாத்தியமான காரணங்கள்:**
- **மாற்றங்கள் இல்லை:** மொழிபெயர்ப்பு படி எந்த மாற்றமும் இல்லை (repo ஏற்கனவே update-ஆக உள்ளது).
- **புறக்கணிக்கப்பட்ட output-கள்:** `.gitignore` நீங்கள் commit செய்ய விரும்பும் கோப்புகளை புறக்கணிக்கிறது (உதா: `*.ipynb`, `translations/`, `translated_images/`).
- **add-paths பொருந்தவில்லை:** action-க்கு வழங்கப்பட்ட பாதைகள் output-இன் உண்மையான இடங்களை பொருந்தவில்லை.
- **Workflow logic/conditions:** மொழிபெயர்ப்பு படி விரைவில் முடிந்தது அல்லது எதிர்பாராத கோப்பகங்களில் எழுதப்பட்டது.

**எப்படி சரி செய்ய / உறுதி செய்ய:**
1. **Output-கள் உள்ளதா உறுதி செய்யவும்:** மொழிபெயர்ப்பு முடிந்ததும், workspace-இல் புதிய/மாற்றப்பட்ட கோப்புகள் `translations/` மற்றும்/அல்லது `translated_images/`-இல் உள்ளதா பார்க்கவும்.
   - Notebook-களை மொழிபெயர்க்கும் போது, `.ipynb` கோப்புகள் `translations/<lang>/...`-இல் எழுதப்பட்டுள்ளதா உறுதி செய்யவும்.
2. **`.gitignore`-ஐ பரிசீலிக்கவும்:** உருவாக்கப்பட்ட output-களை புறக்கணிக்க வேண்டாம். புறக்கணிக்கப்படக்கூடாதவை:
   - `translations/`
   - `translated_images/`
   - `*.ipynb` (notebook-களை மொழிபெயர்க்கும் போது)
3. **add-paths output-களை பொருந்துகிறதா உறுதி செய்யவும்:** multiline value பயன்படுத்தி இரு கோப்பகங்களையும் சேர்க்கவும்:
   ```yaml
   with:
     add-paths: |
       translations/
       translated_images/
   ```
4. **Debug-க்கு PR-ஐ கட்டாயப்படுத்தவும்:** wiring சரியாக உள்ளதா உறுதி செய்ய empty commits-ஐ தற்காலிகமாக அனுமதிக்கவும்:
   ```yaml
   with:
     commit-empty: true
   ```
5. **Debug-இல் இயக்கவும்:** translate command-க்கு `-d` சேர்த்து எந்த கோப்புகள் கண்டறியப்பட்டன, எழுதப்பட்டன என்பதை பார்க்கவும்.
6. **அனுமதிகள் (GITHUB_TOKEN):** commit மற்றும் PR உருவாக்க workflow-க்கு write permission உள்ளதா உறுதி செய்யவும்:
   ```yaml
   permissions:
     contents: write
     pull-requests: write
   ```


## விரைவான Debugging Checklist

மொழிபெயர்ப்பு சிக்கல்களை தீர்க்கும்போது:

1. **Debug mode** பயன்படுத்தவும்: விரிவான பதிவுகளை பார்க்க `-d` flag சேர்க்கவும்
2. **Flags-ஐ சரிபார்க்கவும்:** `-md`, `-img`, `-nb` உங்கள் நோக்கத்திற்கு பொருந்துகிறதா என உறுதி செய்யவும்
3. **அமைப்பை உறுதி செய்யவும்:** உங்கள் `.env` கோப்பில் தேவையான key-கள் உள்ளதா பார்க்கவும்
4. **மெல்ல மெல்ல சோதிக்கவும்:** முதலில் `-md` மட்டும், பிறகு மற்ற வகைகளை சேர்க்கவும்
5. **கோப்பக அமைப்பை பார்க்கவும்:** மூல கோப்புகள் உள்ளதா, அணுகக்கூடியதா என உறுதி செய்யவும்

கட்டளைகள் மற்றும் flags பற்றிய விரிவான தகவலுக்கு [Command Reference](./command-reference.md) பார்க்கவும்.

---

**பொறுப்புத் தவிர்ப்பு**:
இந்த ஆவணம் AI மொழிபெயர்ப்பு சேவையான [Co-op Translator](https://github.com/Azure/co-op-translator) மூலம் மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சி செய்தாலும், தானாக மொழிபெயர்க்கப்படும் மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கலாம் என்பதை தயவுசெய்து கவனிக்கவும். மூல ஆவணம் அதன் சொந்த மொழியில் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்தவொரு தவறான புரிதல் அல்லது தவறான விளக்கத்திற்கு நாங்கள் பொறுப்பல்ல.