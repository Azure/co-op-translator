<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6e626bef5ed78a1cc55b0dbf44f01d47",
  "translation_date": "2025-10-15T03:45:54+00:00",
  "source_file": "getting_started/troubleshooting.md",
  "language_code": "sw"
}
-->
# Mwongozo wa Kutatua Matatizo ya Microsoft Co-op Translator

## Muhtasari
Microsoft Co-Op Translator ni chombo chenye nguvu kinachosaidia kutafsiri hati za Markdown kwa urahisi. Mwongozo huu utakusaidia kutatua matatizo ya kawaida unayoweza kukutana nayo wakati wa kutumia chombo hiki.

## Matatizo ya Kawaida na Suluhisho Zake

### 1. Tatizo la Tag ya Markdown
**Tatizo:** Hati ya Markdown iliyotafsiriwa ina tag ya `markdown` juu, inasababisha matatizo ya kuonyesha.

**Suluhisho:** Ili kutatua hili, futa tu tag ya `markdown` iliyo juu ya faili. Hii itaruhusu faili ya Markdown kuonyesha vizuri.

**Hatua:**
1. Fungua faili ya Markdown (`.md`) iliyotafsiriwa.
2. Tafuta tag ya `markdown` juu ya hati.
3. Futa tag ya `markdown`.
4. Hifadhi mabadiliko kwenye faili.
5. Fungua tena faili ili kuhakikisha inaonyesha vizuri.

### 2. Tatizo la URL za Picha Zilizopachikwa
**Tatizo:** URL za picha zilizopachikwa hazilingani na lugha ya hati, hivyo picha zinaonekana vibaya au hazipo.

**Suluhisho:** Kagua URL za picha zilizopachikwa na hakikisha zinalingana na lugha ya hati. Picha zote zipo kwenye folda ya `translated_images` na kila picha ina tag ya lugha kwenye jina la faili.

**Hatua:**
1. Fungua hati ya Markdown iliyotafsiriwa.
2. Tambua picha zilizopachikwa na URL zake.
3. Hakikisha tag ya lugha kwenye jina la picha inalingana na lugha ya hati.
4. Badilisha URL kama inahitajika.
5. Hifadhi mabadiliko na fungua tena hati ili kuthibitisha picha zinaonekana vizuri.

### 3. Usahihi wa Tafsiri
**Tatizo:** Yaliyotafsiriwa si sahihi au yanahitaji uhariri zaidi.

**Suluhisho:** Pitia hati iliyotafsiriwa na fanya uhariri unaohitajika ili kuboresha usahihi na uelewa.

**Hatua:**
1. Fungua hati iliyotafsiriwa.
2. Pitia yaliyomo kwa makini.
3. Fanya uhariri unaohitajika kuboresha usahihi wa tafsiri.
4. Hifadhi mabadiliko.

## 4. Hitilafu ya Ruhusa Redacted au 404

Ikiwa picha au maandishi havitafsiriwi kwa lugha sahihi na ukiendesha kwa -d debug mode unapata hitilafu ya 401. Hii ni ishara ya kushindwa kuthibitisha utambulisho—labda key ni batili, imeisha muda, au haijaunganishwa na eneo la endpoint.

Endesha co-op translator kwa [-d debug switch](https://github.com/Azure/co-op-translator/blob/main/getting_started/command-reference.md) ili kupata ufahamu zaidi wa chanzo cha tatizo.

- **Ujumbe wa Hitilafu**: `Access denied due to invalid subscription key or wrong API endpoint.`
- **Sababu Zinawezekana**:
  - Subscription key imefichwa au si sahihi kwenye ombi.
  - AI Services Key au Subscription Key inaweza kuwa ya rasilimali tofauti ya Azure (kama Translator au OpenAI) badala ya **Azure AI Vision**.

 **Aina ya Rasilimali**
  - Nenda kwenye [Azure Portal](https://portal.azure.com) au [Azure AI Foundry](https://ai.azure.com) na hakikisha rasilimali ni ya aina `Azure AI services` → `Vision`.
  - Thibitisha funguo na hakikisha unatumia funguo sahihi.

## 5. Hitilafu za Mpangilio (Error Handling Mpya)

Kuanzia mfumo mpya wa tafsiri ya kuchagua, Co-op Translator sasa inatoa ujumbe wa hitilafu wazi pale huduma zinazohitajika hazijapangwa.

### 5.1. Huduma ya Azure AI Haijapangwa kwa Tafsiri ya Picha

**Tatizo:** Umeomba tafsiri ya picha (`-img` flag) lakini huduma ya Azure AI haijapangwa vizuri.

**Ujumbe wa Hitilafu:**
```
Error: Image translation requested but Azure AI Service is not configured.
Please add AZURE_AI_SERVICE_API_KEY and AZURE_AI_SERVICE_ENDPOINT to your .env file.
Check Azure AI Service availability and configuration.
```

**Suluhisho:**
1. **Chaguo 1**: Panga huduma ya Azure AI
   - Ongeza `AZURE_AI_SERVICE_API_KEY` kwenye faili yako ya `.env`
   - Ongeza `AZURE_AI_SERVICE_ENDPOINT` kwenye faili yako ya `.env`
   - Hakikisha huduma inapatikana

2. **Chaguo 2**: Ondoa ombi la tafsiri ya picha
   ```bash
   # Instead of: translate -l "ko" -img
   # Use: translate -l "ko" -md
   ```

### 5.2. Mpangilio Muhimu Umekosekana

**Tatizo:** Mpangilio muhimu wa LLM umekosekana.

**Ujumbe wa Hitilafu:**
```
Error: No language model configuration found.
Please configure either Azure OpenAI or OpenAI in your .env file.
```

**Suluhisho:**
1. Hakikisha faili yako ya `.env` ina angalau moja ya mpangilio wa LLM ufuatao:
   - **Azure OpenAI**: `AZURE_OPENAI_API_KEY` na `AZURE_OPENAI_ENDPOINT`
   - **OpenAI**: `OPENAI_API_KEY`
   
   Unahitaji ama Azure OpenAI AU OpenAI imepangwa, si zote mbili.

### 5.3. Mkanganyiko wa Tafsiri ya Kuchagua

**Tatizo:** Hakuna faili zilizotafsiriwa ingawa amri imefanikiwa.

**Sababu Zinawezekana:**
- Bendera za aina ya faili si sahihi (`-md`, `-img`, `-nb`)
- Hakuna faili zinazolingana kwenye mradi
- Muundo wa folda si sahihi

**Suluhisho:**
1. **Tumia debug mode** kuona kinachoendelea:
   ```bash
   translate -l "ko" -md -d
   ```

2. **Kagua aina za faili** kwenye mradi wako:
   ```bash
   # For markdown files
   find . -name "*.md" -not -path "./translations/*"
   
   # For notebooks
   find . -name "*.ipynb" -not -path "./translations/*"
   
   # For images
   find . -name "*.png" -o -name "*.jpg" -o -name "*.jpeg" -not -path "./translations/*"
   ```

3. **Thibitisha mchanganyiko wa bendera**:
   ```bash
   # Translate everything (default)
   translate -l "ko"
   
   # Translate specific types
   translate -l "ko" -md -img
   ```

## 6. Uhamiaji kutoka Mfumo wa Zamani

### 6.1. Hali ya Markdown Pekee Imeondolewa

**Tatizo:** Amri zilizotegemea fallback ya Markdown pekee hazifanyi kazi kama ilivyotarajiwa.

**Tabia ya Zamani:**
```bash
# This used to automatically switch to markdown-only mode
translate -l "ko"  # (when Azure AI Vision was not configured)
```

**Tabia Mpya:**
```bash
# This now produces an error if image translation is requested but not configured
translate -l "ko" -img
```

**Suluhisho:**
- **Kuwa wazi** kuhusu unachotaka kutafsiri:
  ```bash
  translate -l "ko" -md        # Only markdown
  translate -l "ko" -md -img   # Markdown and images
  translate -l "ko"            # Everything (if all services configured)
  ```

### 6.2. Tabia Isiyotarajiwa ya Viungo

**Tatizo:** Viungo kwenye faili zilizotafsiriwa vinaelekeza sehemu zisizotarajiwa.

**Sababu:** Usindikaji wa viungo unabadilika kulingana na aina za faili zilizochaguliwa.

**Suluhisho:**
1. **Elewa tabia mpya ya viungo**:
   - `-nb` imejumuishwa: Viungo vya notebook vinaelekeza kwenye toleo lililotafsiriwa
   - `-nb` haijajumuishwa: Viungo vya notebook vinaelekeza kwenye faili asili
   - `-img` imejumuishwa: Viungo vya picha vinaelekeza kwenye toleo lililotafsiriwa
   - `-img` haijajumuishwa: Viungo vya picha vinaelekeza kwenye faili asili

2. **Chagua mchanganyiko sahihi** kwa matumizi yako:
   ```bash
   # All internal links point to translated versions
   translate -l "ko" -md -img -nb
   
   # Only markdown translated, other links point to originals
   translate -l "ko" -md
   ```

## 7. GitHub Action imekimbia lakini hakuna Pull Request (PR) iliyoundwa

**Dalili:** Logi za workflow kwa `peter-evans/create-pull-request` zinaonyesha:

> Branch 'update-translations' is not ahead of base 'main' and will not be created

**Sababu zinazowezekana:**
- **Hakuna mabadiliko yaliyogunduliwa:** Hatua ya tafsiri haijazalisha tofauti (repo tayari iko sawa).
- **Matokeo yamepuuzwa:** `.gitignore` inazuia faili unazotarajia kuwasilisha (mfano, `*.ipynb`, `translations/`, `translated_images/`).
- **add-paths haifanani:** Njia zilizotolewa kwa action hazifanani na maeneo halisi ya matokeo.
- **Mantiki/maelezo ya workflow:** Hatua ya tafsiri imekoma mapema au imeandika kwenye folda zisizotarajiwa.

**Jinsi ya kutatua / kuthibitisha:**
1. **Thibitisha matokeo yapo:** Baada ya tafsiri, angalia workspace ina faili mpya/zilizobadilishwa kwenye `translations/` na/au `translated_images/`.
   - Ikiwa unatafsiri notebooks, hakikisha faili za `.ipynb` zimeandikwa chini ya `translations/<lang>/...`.
2. **Kagua `.gitignore`:** Usizuie matokeo yaliyotengenezwa. Hakikisha HAUZUII:
   - `translations/`
   - `translated_images/`
   - `*.ipynb` (ukitafsiri notebooks)
3. **Hakikisha add-paths inafanana na matokeo:** Tumia thamani ya mistari mingi na jumuisha folda zote kama inahitajika:
   ```yaml
   with:
     add-paths: |
       translations/
       translated_images/
   ```
4. **Lazimisha PR kwa debugging:** Ruhusu muda mfupi commits tupu ili kuthibitisha wiring ni sahihi:
   ```yaml
   with:
     commit-empty: true
   ```
5. **Endesha kwa debug:** Ongeza `-d` kwenye amri ya tafsiri ili kuchapisha ni faili gani zimegunduliwa na kuandikwa.
6. **Ruhusa (GITHUB_TOKEN):** Hakikisha workflow ina ruhusa ya kuandika ili kuunda commits na PRs:
   ```yaml
   permissions:
     contents: write
     pull-requests: write
   ```


## Orodha ya Haraka ya Kutatua Matatizo

Unapotatua matatizo ya tafsiri:

1. **Tumia debug mode**: Ongeza bendera ya `-d` kuona logi za kina
2. **Kagua bendera zako**: Hakikisha `-md`, `-img`, `-nb` zinaendana na unachokusudia
3. **Thibitisha mpangilio**: Kagua faili yako ya `.env` ina funguo zinazohitajika
4. **Jaribu hatua kwa hatua**: Anza na `-md` pekee, kisha ongeza aina nyingine
5. **Kagua muundo wa faili**: Hakikisha faili za chanzo zipo na zinaweza kufikiwa

Kwa maelezo zaidi kuhusu amri na bendera zinazopatikana, angalia [Command Reference](./command-reference.md).

---

**Kanusho**:
Hati hii imetafsiriwa kwa kutumia huduma ya kutafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuhakikisha usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati asili katika lugha yake ya asili inapaswa kuchukuliwa kama chanzo rasmi. Kwa taarifa muhimu, inashauriwa kutumia huduma ya utafsiri wa kibinadamu wa kitaalamu. Hatuwajibiki kwa kutoelewana au kutafsiri vibaya kunakotokana na matumizi ya tafsiri hii.