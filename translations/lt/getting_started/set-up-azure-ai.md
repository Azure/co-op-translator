<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b58d7c3cb4210697a073d20eb3064945",
  "translation_date": "2025-10-15T04:47:23+00:00",
  "source_file": "getting_started/set-up-azure-ai.md",
  "language_code": "lt"
}
-->
# Azure AI paruošimas Co-op Translator (Azure OpenAI & Azure AI Vision)

Šiame vadove rasite, kaip paruošti Azure OpenAI kalbų vertimui ir Azure Computer Vision vaizdų turinio analizei (tai leidžia versti tekstą iš paveikslėlių) naudojant Azure AI Foundry.

**Reikalavimai:**
- Azure paskyra su aktyvia prenumerata.
- Pakankamos teisės kurti išteklius ir diegimus jūsų Azure prenumeratoje.

## Sukurkite Azure AI projektą

Pradėkite nuo Azure AI projekto sukūrimo – tai bus pagrindinė vieta, kur valdysite visus AI išteklius.

1. Eikite į [https://ai.azure.com](https://ai.azure.com) ir prisijunkite su savo Azure paskyra.

1. Pasirinkite **+Sukurti** naujam projektui sukurti.

1. Atlikite šiuos veiksmus:
   - Įveskite **Projekto pavadinimą** (pvz., `CoopTranslator-Project`).
   - Pasirinkite **AI centrą** (pvz., `CoopTranslator-Hub`) (prireikus sukurkite naują).

1. Spauskite "**Peržiūrėti ir sukurti**", kad užbaigtumėte projekto kūrimą. Būsite nukreipti į projekto apžvalgos puslapį.

## Azure OpenAI paruošimas kalbų vertimui

Projekte diegsite Azure OpenAI modelį, kuris bus naudojamas tekstų vertimui.

### Eikite į savo projektą

Jei dar nesate, atsidarykite naujai sukurtą projektą (pvz., `CoopTranslator-Project`) Azure AI Foundry.

### Diegti OpenAI modelį

1. Kairiajame projekto meniu, skiltyje "Mano ištekliai", pasirinkite "**Modeliai + galiniai taškai**".

1. Pasirinkite **+ Diegti modelį**.

1. Pasirinkite **Diegti bazinį modelį**.

1. Pamatysite galimų modelių sąrašą. Filtruokite arba ieškokite tinkamo GPT modelio. Rekomenduojame `gpt-4o`.

1. Pasirinkite norimą modelį ir spauskite **Patvirtinti**.

1. Pasirinkite **Diegti**.

### Azure OpenAI konfigūracija

Kai modelis bus įdiegtas, galite pasirinkti diegimą iš "**Modeliai + galiniai taškai**" puslapio ir rasti **REST galinio taško URL**, **Raktą**, **Diegimo pavadinimą**, **Modelio pavadinimą** ir **API versiją**. Šių duomenų reikės, kad integruotumėte vertimo modelį į savo programą.

> [!NOTE]
> API versijas galite pasirinkti iš [API versijų nutraukimo](https://learn.microsoft.com/azure/ai-services/openai/api-version-deprecation) puslapio pagal savo poreikius. Atkreipkite dėmesį, kad **API versija** skiriasi nuo **Modelio versijos**, kuri rodoma **Modeliai + galiniai taškai** puslapyje Azure AI Foundry.

## Azure Computer Vision paruošimas vaizdų vertimui

Norėdami versti tekstą iš paveikslėlių, turite rasti Azure AI Service API raktą ir galinio taško adresą.

1. Eikite į savo Azure AI projektą (pvz., `CoopTranslator-Project`). Įsitikinkite, kad esate projekto apžvalgos puslapyje.

### Azure AI Service konfigūracija

Raskite API raktą ir galinio taško adresą Azure AI Service.

1. Eikite į savo Azure AI projektą (pvz., `CoopTranslator-Project`). Įsitikinkite, kad esate projekto apžvalgos puslapyje.

1. Suraskite **API raktą** ir **Galinio taško adresą** Azure AI Service skiltyje.

    <img src="../../../translated_images/find-azure-ai-info.0e00140419c12517d2011ecdde3fafb9306d379b29d2c04a0d18063e56983559.lt.png" alt="Raskite API raktą ir galinio taško adresą">

Šis ryšys leidžia jūsų AI Foundry projektui naudotis susietų Azure AI Services galimybėmis (įskaitant vaizdų analizę). Tuomet šį ryšį galite naudoti savo užrašuose ar programose, kad išgautumėte tekstą iš paveikslėlių ir perduotumėte jį Azure OpenAI modeliui vertimui.

## Kredencialų sujungimas

Šiuo metu turėtumėte būti surinkę šiuos duomenis:

**Azure OpenAI (teksto vertimui):**
- Azure OpenAI galinio taško adresas
- Azure OpenAI API raktas
- Azure OpenAI modelio pavadinimas (pvz., `gpt-4o`)
- Azure OpenAI diegimo pavadinimas (pvz., `cooptranslator-gpt4o`)
- Azure OpenAI API versija

**Azure AI Services (vaizdo teksto išgavimui per Vision):**
- Azure AI Service galinio taško adresas
- Azure AI Service API raktas

### Pavyzdys: Aplinkos kintamųjų konfigūracija (Preview)

Vėliau, kurdami programą, greičiausiai naudosite šiuos kredencialus konfigūruodami aplinkos kintamuosius, pavyzdžiui:

```bash
# Azure AI Service Credentials (Required for image translation)
AZURE_AI_SERVICE_API_KEY="your_azure_ai_service_api_key" # e.g., 21xasd...
AZURE_AI_SERVICE_ENDPOINT="https://your_azure_ai_service_endpoint.cognitiveservices.azure.com/"

# Azure OpenAI Credentials (Required for text translation)
AZURE_OPENAI_API_KEY="your_azure_openai_api_key" # e.g., 21xasd...
AZURE_OPENAI_ENDPOINT="https://your_azure_openai_endpoint.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="your_model_name" # e.g., gpt-4o
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="your_deployment_name" # e.g., cooptranslator-gpt4o
AZURE_OPENAI_API_VERSION="your_api_version" # e.g., 2024-12-01-preview
```

---

### Daugiau informacijos

- [Kaip sukurti projektą Azure AI Foundry](https://learn.microsoft.com/azure/ai-foundry/how-to/create-projects?tabs=ai-studio)
- [Kaip sukurti Azure AI išteklius](https://learn.microsoft.com/azure/ai-foundry/how-to/create-azure-ai-resource?tabs=portal)
- [Kaip diegti OpenAI modelius Azure AI Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/deploy-models-openai)

---

**Atsakomybės atsisakymas**:  
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojame profesionalų žmogaus vertimą. Mes neatsakome už nesusipratimus ar neteisingą interpretavimą, kilusį dėl šio vertimo naudojimo.