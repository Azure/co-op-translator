<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6e626bef5ed78a1cc55b0dbf44f01d47",
  "translation_date": "2025-10-15T04:48:53+00:00",
  "source_file": "getting_started/troubleshooting.md",
  "language_code": "lt"
}
-->
# Microsoft Co-op Translator trikčių šalinimo vadovas

## Apžvalga
Microsoft Co-Op Translator – tai galingas įrankis, skirtas sklandžiai versti Markdown dokumentus. Šis vadovas padės išspręsti dažniausiai pasitaikančias problemas, su kuriomis galite susidurti naudojant šį įrankį.

## Dažniausios problemos ir sprendimai

### 1. Markdown žymos problema
**Problema:** Išverstas Markdown dokumentas turi `markdown` žymą viršuje, dėl ko kyla atvaizdavimo problemų.

**Sprendimas:** Norėdami tai ištaisyti, tiesiog ištrinkite `markdown` žymą dokumento viršuje. Taip Markdown failas bus tinkamai atvaizduojamas.

**Veiksmai:**
1. Atidarykite išverstą Markdown (`.md`) failą.
2. Suraskite `markdown` žymą dokumento viršuje.
3. Ištrinkite šią žymą.
4. Išsaugokite pakeitimus.
5. Vėl atidarykite failą ir patikrinkite, ar jis tinkamai atvaizduojamas.

### 2. Įterptų paveikslėlių URL problema
**Problema:** Įterptų paveikslėlių URL neatitinka kalbos lokalės, todėl paveikslėliai rodomi neteisingai arba visai nerodomi.

**Sprendimas:** Patikrinkite paveikslėlių URL ir įsitikinkite, kad jie atitinka dokumento kalbos lokalę. Visi paveikslėliai saugomi `translated_images` aplanke, o kiekvieno paveikslėlio pavadinime yra kalbos lokalės žyma.

**Veiksmai:**
1. Atidarykite išverstą Markdown dokumentą.
2. Suraskite įterptus paveikslėlius ir jų URL.
3. Patikrinkite, ar paveikslėlio pavadinime esanti kalbos lokalė sutampa su dokumento kalba.
4. Jei reikia, atnaujinkite URL.
5. Išsaugokite pakeitimus ir vėl atidarykite dokumentą, kad įsitikintumėte, jog paveikslėliai rodomi teisingai.

### 3. Vertimo tikslumas
**Problema:** Išverstas turinys nėra tikslus arba reikia papildomo redagavimo.

**Sprendimas:** Peržiūrėkite išverstą dokumentą ir atlikite reikiamus pakeitimus, kad pagerintumėte vertimo tikslumą ir skaitomumą.

**Veiksmai:**
1. Atidarykite išverstą dokumentą.
2. Kruopščiai peržiūrėkite turinį.
3. Atlikite reikiamus pakeitimus, kad vertimas būtų tikslesnis.
4. Išsaugokite pakeitimus.

## 4. Leidimų klaida Redacted arba 404

Jei paveikslėliai ar tekstas neverčiami į reikiamą kalbą ir naudojant -d debug režimą gaunate 401 klaidą, tai reiškia, kad autentifikacija nepavyko – raktas neteisingas, pasibaigęs arba nesusietas su tinkamu regionu.

Paleiskite co-op translator su [-d debug jungikliu](https://github.com/Azure/co-op-translator/blob/main/getting_started/command-reference.md), kad geriau suprastumėte problemos priežastį.

- **Klaidos pranešimas**: `Access denied due to invalid subscription key or wrong API endpoint.`
- **Galimos priežastys**:
  - Prenumeratos raktas buvo paslėptas arba neteisingas užklausoje.
  - AI Services Key arba Subscription Key priklauso kitam Azure resursui (pvz., Translator ar OpenAI), o ne **Azure AI Vision** resursui.

 **Resurso tipas**
  - Eikite į [Azure Portal](https://portal.azure.com) arba [Azure AI Foundry](https://ai.azure.com) ir įsitikinkite, kad resurso tipas yra `Azure AI services` → `Vision`.
  - Patikrinkite raktus ir įsitikinkite, kad naudojate teisingą raktą.

## 5. Konfigūracijos klaidos (naujas klaidų apdorojimas)

Nuo naujos selektyvaus vertimo sistemos Co-op Translator aiškiai praneša apie klaidas, kai reikiamos paslaugos nėra sukonfigūruotos.

### 5.1. Azure AI Service nesukonfigūruota paveikslėlių vertimui

**Problema:** Paprašėte paveikslėlių vertimo (`-img` vėliava), bet Azure AI Service nėra tinkamai sukonfigūruota.

**Klaidos pranešimas:**
```
Error: Image translation requested but Azure AI Service is not configured.
Please add AZURE_AI_SERVICE_API_KEY and AZURE_AI_SERVICE_ENDPOINT to your .env file.
Check Azure AI Service availability and configuration.
```

**Sprendimas:**
1. **1 variantas**: Sukonfigūruokite Azure AI Service
   - Pridėkite `AZURE_AI_SERVICE_API_KEY` į savo `.env` failą
   - Pridėkite `AZURE_AI_SERVICE_ENDPOINT` į savo `.env` failą
   - Patikrinkite, ar paslauga pasiekiama

2. **2 variantas**: Pašalinkite paveikslėlių vertimo užklausą
   ```bash
   # Instead of: translate -l "ko" -img
   # Use: translate -l "ko" -md
   ```

### 5.2. Trūksta būtinos konfigūracijos

**Problema:** Trūksta esminės LLM konfigūracijos.

**Klaidos pranešimas:**
```
Error: No language model configuration found.
Please configure either Azure OpenAI or OpenAI in your .env file.
```

**Sprendimas:**
1. Patikrinkite, ar jūsų `.env` faile yra bent viena iš šių LLM konfigūracijų:
   - **Azure OpenAI**: `AZURE_OPENAI_API_KEY` ir `AZURE_OPENAI_ENDPOINT`
   - **OpenAI**: `OPENAI_API_KEY`
   
   Reikia sukonfigūruoti arba Azure OpenAI, arba OpenAI – ne abu.

### 5.3. Selektyvaus vertimo painiava

**Problema:** Nė vienas failas nebuvo išverstas, nors komanda įvykdyta sėkmingai.

**Galimos priežastys:**
- Netinkamos failų tipų vėliavos (`-md`, `-img`, `-nb`)
- Projekte nėra atitinkančių failų
- Netinkama katalogų struktūra

**Sprendimas:**
1. **Naudokite debug režimą**, kad pamatytumėte, kas vyksta:
   ```bash
   translate -l "ko" -md -d
   ```

2. **Patikrinkite failų tipus** savo projekte:
   ```bash
   # For markdown files
   find . -name "*.md" -not -path "./translations/*"
   
   # For notebooks
   find . -name "*.ipynb" -not -path "./translations/*"
   
   # For images
   find . -name "*.png" -o -name "*.jpg" -o -name "*.jpeg" -not -path "./translations/*"
   ```

3. **Patikrinkite vėliavų derinius**:
   ```bash
   # Translate everything (default)
   translate -l "ko"
   
   # Translate specific types
   translate -l "ko" -md -img
   ```

## 6. Migracija iš senos sistemos

### 6.1. Tik Markdown režimas panaikintas

**Problema:** Komandos, kurios automatiškai veikė tik su Markdown, nebeveikia kaip anksčiau.

**Senas elgesys:**
```bash
# This used to automatically switch to markdown-only mode
translate -l "ko"  # (when Azure AI Vision was not configured)
```

**Naujas elgesys:**
```bash
# This now produces an error if image translation is requested but not configured
translate -l "ko" -img
```

**Sprendimas:**
- **Būkite aiškūs**, ką norite versti:
  ```bash
  translate -l "ko" -md        # Only markdown
  translate -l "ko" -md -img   # Markdown and images
  translate -l "ko"            # Everything (if all services configured)
  ```

### 6.2. Netikėtas nuorodų elgesys

**Problema:** Nuorodos išverstame faile nukreipia į netikėtas vietas.

**Priežastis:** Dinaminis nuorodų apdorojimas keičiasi priklausomai nuo pasirinktų failų tipų.

**Sprendimas:**
1. **Supraskite naują nuorodų elgesį**:
   - Įtraukus `-nb`: užrašų knygelių nuorodos nukreipia į išverstus failus
   - Neįtraukus `-nb`: užrašų knygelių nuorodos nukreipia į originalius failus
   - Įtraukus `-img`: paveikslėlių nuorodos nukreipia į išverstus failus
   - Neįtraukus `-img`: paveikslėlių nuorodos nukreipia į originalius failus

2. **Pasirinkite tinkamą derinį** pagal savo poreikius:
   ```bash
   # All internal links point to translated versions
   translate -l "ko" -md -img -nb
   
   # Only markdown translated, other links point to originals
   translate -l "ko" -md
   ```

## 7. GitHub Action įvykdyta, bet Pull Request (PR) nesukurta

**Simptomas:** Darbo eigos žurnale `peter-evans/create-pull-request` matote:

> Branch 'update-translations' is not ahead of base 'main' and will not be created

**Galimos priežastys:**
- **Nėra pakeitimų:** Vertimo žingsnis nesukūrė skirtumų (repo jau atnaujintas).
- **Ignoruojami rezultatai:** `.gitignore` ignoruoja failus, kuriuos norite įtraukti (pvz., `*.ipynb`, `translations/`, `translated_images/`).
- **add-paths neatitikimas:** Veiksmo nurodyti keliai nesutampa su tikrais rezultatais.
- **Darbo eigos logika/sąlygos:** Vertimo žingsnis baigėsi anksčiau arba rašė į netikėtus katalogus.

**Kaip ištaisyti / patikrinti:**
1. **Patvirtinkite, kad rezultatai egzistuoja:** Po vertimo patikrinkite, ar darbo aplinkoje yra naujų/pakeistų failų `translations/` ir/arba `translated_images/`.
   - Jei verčiate užrašų knygeles, įsitikinkite, kad `.ipynb` failai tikrai parašyti į `translations/<lang>/...`.
2. **Peržiūrėkite `.gitignore`:** Neignoruokite sugeneruotų rezultatų. Įsitikinkite, kad NEignoruojate:
   - `translations/`
   - `translated_images/`
   - `*.ipynb` (jei verčiate užrašų knygeles)
3. **Įsitikinkite, kad add-paths atitinka rezultatus:** Naudokite kelių eilučių reikšmę ir įtraukite abu aplankus, jei reikia:
   ```yaml
   with:
     add-paths: |
       translations/
       translated_images/
   ```
4. **Priverstinai sukurkite PR derinimui:** Laikinai leiskite tuščius commit’us, kad patikrintumėte, ar viskas sujungta teisingai:
   ```yaml
   with:
     commit-empty: true
   ```
5. **Paleiskite su debug:** Pridėkite `-d` prie vertimo komandos, kad matytumėte, kokie failai buvo rasti ir parašyti.
6. **Leidimai (GITHUB_TOKEN):** Įsitikinkite, kad darbo eiga turi rašymo leidimus commit’ams ir PR kūrimui:
   ```yaml
   permissions:
     contents: write
     pull-requests: write
   ```

## Greitas trikčių šalinimo kontrolinis sąrašas

Sprendžiant vertimo problemas:

1. **Naudokite debug režimą:** Pridėkite `-d` vėliavą, kad matytumėte išsamius žurnalus
2. **Patikrinkite vėliavas:** Įsitikinkite, kad `-md`, `-img`, `-nb` atitinka jūsų tikslą
3. **Patikrinkite konfigūraciją:** Patikrinkite, ar jūsų `.env` faile yra reikalingi raktai
4. **Testuokite palaipsniui:** Pradėkite nuo `-md`, tada pridėkite kitus tipus
5. **Patikrinkite failų struktūrą:** Įsitikinkite, kad šaltinio failai egzistuoja ir yra pasiekiami

Daugiau informacijos apie galimas komandas ir vėliavas rasite [Komandų nuorodoje](./command-reference.md).

---

**Atsakomybės atsisakymas**:  
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojame profesionalų žmogaus vertimą. Mes neatsakome už nesusipratimus ar neteisingą interpretavimą, kilusį dėl šio vertimo naudojimo.