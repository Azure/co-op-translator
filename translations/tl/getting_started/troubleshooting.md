<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6e626bef5ed78a1cc55b0dbf44f01d47",
  "translation_date": "2025-10-15T03:43:09+00:00",
  "source_file": "getting_started/troubleshooting.md",
  "language_code": "tl"
}
-->
# Gabay sa Pag-aayos ng Microsoft Co-op Translator

## Pangkalahatang-ideya
Ang Microsoft Co-Op Translator ay isang makapangyarihang tool para sa tuluy-tuloy na pagsasalin ng mga Markdown na dokumento. Ang gabay na ito ay tutulong sa iyo na ayusin ang mga karaniwang isyu na nararanasan kapag ginagamit ang tool.

## Karaniwang Isyu at Solusyon

### 1. Isyu sa Markdown Tag
**Problema:** May `markdown` tag sa itaas ng isinaling Markdown na dokumento na nagdudulot ng problema sa pag-render.

**Solusyon:** Upang ayusin ito, tanggalin lang ang `markdown` tag sa itaas ng file. Sa ganitong paraan, maayos na magre-render ang Markdown file.

**Mga Hakbang:**
1. Buksan ang isinaling Markdown (`.md`) file.
2. Hanapin ang `markdown` tag sa itaas ng dokumento.
3. Tanggalin ang `markdown` tag.
4. I-save ang mga pagbabago sa file.
5. Buksan muli ang file para tiyaking maayos ang pag-render.

### 2. Isyu sa URL ng Nakapaloob na Larawan
**Problema:** Hindi tumutugma ang URL ng mga nakapaloob na larawan sa language locale, kaya nagkakaroon ng maling larawan o nawawalang larawan.

**Solusyon:** Suriin ang URL ng mga nakapaloob na larawan at tiyaking tumutugma ito sa language locale. Lahat ng larawan ay nasa `translated_images` folder at bawat larawan ay may language locale tag sa pangalan ng file.

**Mga Hakbang:**
1. Buksan ang isinaling Markdown na dokumento.
2. Hanapin ang mga nakapaloob na larawan at ang kanilang mga URL.
3. Tiyaking tumutugma ang language locale sa pangalan ng file ng larawan sa wika ng dokumento.
4. I-update ang mga URL kung kinakailangan.
5. I-save ang mga pagbabago at buksan muli ang dokumento para tiyaking tama ang pag-render ng mga larawan.

### 3. Katumpakan ng Pagsasalin
**Problema:** Hindi tama o kailangan pang i-edit ang isinaling nilalaman.

**Solusyon:** Suriin ang isinaling dokumento at gawin ang kinakailangang pag-edit para mapabuti ang katumpakan at pagiging malinaw.

**Mga Hakbang:**
1. Buksan ang isinaling dokumento.
2. Suriin nang mabuti ang nilalaman.
3. Gawin ang kinakailangang pag-edit para mapabuti ang pagsasalin.
4. I-save ang mga pagbabago.

## 4. Permission Error Redacted o 404

Kung ang mga larawan o teksto ay hindi naisalin sa tamang wika at kapag nagpatakbo sa -d debug mode ay nakaranas ka ng 401 error. Ito ay karaniwang authentication failure—maaaring invalid, expired, o hindi naka-link ang key sa endpoint region.

Patakbuhin ang co-op translator gamit ang [-d debug switch](https://github.com/Azure/co-op-translator/blob/main/getting_started/command-reference.md) para mas maintindihan ang ugat ng problema.

- **Error Message**: `Access denied due to invalid subscription key or wrong API endpoint.`
- **Mga Posibleng Sanhi**:
  - Redacted o mali ang subscription key sa request.
  - Ang AI Services Key o Subscription Key ay maaaring para sa ibang Azure resource (tulad ng Translator o OpenAI) imbes na **Azure AI Vision** resource.

 **Uri ng Resource**
  - Pumunta sa [Azure Portal](https://portal.azure.com) o [Azure AI Foundry](https://ai.azure.com) at tiyaking ang resource ay may type na `Azure AI services` → `Vision`.
  - I-validate ang mga key at tiyaking tama ang ginagamit na key.

## 5. Mga Error sa Configuration (Bagong Error Handling)

Simula sa bagong selective translation system, nagbibigay na ang Co-op Translator ng malinaw na error message kapag hindi naka-configure ang mga kinakailangang serbisyo.

### 5.1. Hindi Naka-configure ang Azure AI Service para sa Image Translation

**Problema:** Humiling ka ng image translation (`-img` flag) pero hindi maayos ang configuration ng Azure AI Service.

**Error Message:**
```
Error: Image translation requested but Azure AI Service is not configured.
Please add AZURE_AI_SERVICE_API_KEY and AZURE_AI_SERVICE_ENDPOINT to your .env file.
Check Azure AI Service availability and configuration.
```

**Solusyon:**
1. **Opsyon 1**: I-configure ang Azure AI Service
   - Idagdag ang `AZURE_AI_SERVICE_API_KEY` sa iyong `.env` file
   - Idagdag ang `AZURE_AI_SERVICE_ENDPOINT` sa iyong `.env` file
   - Tiyaking accessible ang service

2. **Opsyon 2**: Alisin ang request para sa image translation
   ```bash
   # Instead of: translate -l "ko" -img
   # Use: translate -l "ko" -md
   ```

### 5.2. Kulang na Kinakailangang Configuration

**Problema:** Kulang ang mahalagang LLM configuration.

**Error Message:**
```
Error: No language model configuration found.
Please configure either Azure OpenAI or OpenAI in your .env file.
```

**Solusyon:**
1. Tiyaking may isa sa mga sumusunod na LLM configuration sa iyong `.env` file:
   - **Azure OpenAI**: `AZURE_OPENAI_API_KEY` at `AZURE_OPENAI_ENDPOINT`
   - **OpenAI**: `OPENAI_API_KEY`
   
   Kailangan mo ng Azure OpenAI O OpenAI na naka-configure, hindi pareho.

### 5.3. Kalituhan sa Selective Translation

**Problema:** Walang na-translate na file kahit nagtagumpay ang command.

**Mga Posibleng Sanhi:**
- Mali ang file type flags (`-md`, `-img`, `-nb`)
- Walang tumutugmang file sa project
- Mali ang directory structure

**Solusyon:**
1. **Gamitin ang debug mode** para makita ang nangyayari:
   ```bash
   translate -l "ko" -md -d
   ```

2. **Suriin ang mga file type** sa iyong project:
   ```bash
   # For markdown files
   find . -name "*.md" -not -path "./translations/*"
   
   # For notebooks
   find . -name "*.ipynb" -not -path "./translations/*"
   
   # For images
   find . -name "*.png" -o -name "*.jpg" -o -name "*.jpeg" -not -path "./translations/*"
   ```

3. **I-verify ang kombinasyon ng mga flag**:
   ```bash
   # Translate everything (default)
   translate -l "ko"
   
   # Translate specific types
   translate -l "ko" -md -img
   ```

## 6. Paglipat mula sa Lumang Sistema

### 6.1. Deprecated na Markdown-Only Mode

**Problema:** Ang mga command na umaasa sa automatic markdown-only fallback ay hindi na gumagana gaya ng dati.

**Lumang Ugali:**
```bash
# This used to automatically switch to markdown-only mode
translate -l "ko"  # (when Azure AI Vision was not configured)
```

**Bagong Ugali:**
```bash
# This now produces an error if image translation is requested but not configured
translate -l "ko" -img
```

**Solusyon:**
- **Maging malinaw** sa gusto mong i-translate:
  ```bash
  translate -l "ko" -md        # Only markdown
  translate -l "ko" -md -img   # Markdown and images
  translate -l "ko"            # Everything (if all services configured)
  ```

### 6.2. Hindi Inaasahang Ugali ng Link

**Problema:** Ang mga link sa isinaling file ay tumuturo sa hindi inaasahang lokasyon.

**Sanhi:** Nagbabago ang dynamic link processing depende sa napiling file types.

**Solusyon:**
1. **Unawain ang bagong ugali ng link**:
   - Kapag kasama ang `-nb`: Ang notebook links ay tumuturo sa isinaling bersyon
   - Kapag hindi kasama ang `-nb`: Ang notebook links ay tumuturo sa orihinal na file
   - Kapag kasama ang `-img`: Ang image links ay tumuturo sa isinaling bersyon
   - Kapag hindi kasama ang `-img`: Ang image links ay tumuturo sa orihinal na file

2. **Piliin ang tamang kombinasyon** para sa iyong gamit:
   ```bash
   # All internal links point to translated versions
   translate -l "ko" -md -img -nb
   
   # Only markdown translated, other links point to originals
   translate -l "ko" -md
   ```

## 7. Tumakbo ang GitHub Action pero walang Pull Request (PR) na nagawa

**Sintomas:** Ang workflow logs para sa `peter-evans/create-pull-request` ay nagpapakita ng:

> Branch 'update-translations' is not ahead of base 'main' and will not be created

**Mga Posibleng Sanhi:**
- **Walang nakitang pagbabago:** Walang nagawang diff ang translation step (up to date na ang repo).
- **Ignored outputs:** Naka-`.gitignore` ang mga file na inaasahan mong i-commit (hal. `*.ipynb`, `translations/`, `translated_images/`).
- **Hindi tugma ang add-paths:** Hindi tumutugma ang mga path na ibinigay sa action sa aktwal na output locations.
- **Workflow logic/conditions:** Maagang nag-exit ang translation step o nagsulat sa hindi inaasahang directory.

**Paano ayusin / i-verify:**
1. **Tiyaking may outputs:** Pagkatapos ng translation, suriin kung may bago/nabago na file sa `translations/` at/o `translated_images/`.
   - Kung nagta-translate ng notebook, tiyaking may `.ipynb` files sa `translations/<lang>/...`.
2. **Suriin ang `.gitignore`:** Huwag i-ignore ang mga generated outputs. Tiyaking HINDI mo ini-ignore ang:
   - `translations/`
   - `translated_images/`
   - `*.ipynb` (kung nagta-translate ng notebook)
3. **Tiyaking tugma ang add-paths sa outputs:** Gumamit ng multiline value at isama ang parehong folder kung kinakailangan:
   ```yaml
   with:
     add-paths: |
       translations/
       translated_images/
   ```
4. **I-force ang PR para sa debugging:** Pansamantalang payagan ang empty commits para matiyak na tama ang wiring:
   ```yaml
   with:
     commit-empty: true
   ```
5. **Patakbuhin sa debug:** Idagdag ang `-d` sa translate command para makita kung anong files ang natuklasan at naisulat.
6. **Permissions (GITHUB_TOKEN):** Tiyaking may write permissions ang workflow para makagawa ng commits at PRs:
   ```yaml
   permissions:
     contents: write
     pull-requests: write
   ```


## Mabilisang Checklist sa Pag-debug

Kapag nag-aayos ng isyu sa pagsasalin:

1. **Gamitin ang debug mode**: Idagdag ang `-d` flag para makita ang detalyadong logs
2. **Suriin ang iyong mga flag**: Tiyaking tumutugma ang `-md`, `-img`, `-nb` sa iyong layunin
3. **I-verify ang configuration**: Suriin kung may mga kinakailangang key sa iyong `.env` file
4. **Subukan nang paunti-unti**: Simulan sa `-md` lang, saka idagdag ang ibang types
5. **Suriin ang file structure**: Tiyaking may source files at accessible ang mga ito

Para sa mas detalyadong impormasyon tungkol sa mga available na command at flag, tingnan ang [Command Reference](./command-reference.md).

---

**Paunawa**:
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagaman nagsusumikap kami para sa katumpakan, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatumpak. Ang orihinal na dokumento sa kanyang sariling wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring lumitaw mula sa paggamit ng pagsasaling ito.