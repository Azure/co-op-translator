<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "527ca4d0a8d3f51087ec3317279e36ee",
  "translation_date": "2025-10-15T03:47:03+00:00",
  "source_file": "getting_started/github-actions-guide/github-actions-guide-public.md",
  "language_code": "sw"
}
-->
# Kutumia Co-op Translator GitHub Action (Usanidi wa Umma)

**Walengwa:** Mwongozo huu umeandaliwa kwa watumiaji wa miradi ya umma au binafsi ambapo ruhusa za kawaida za GitHub Actions zinatosha. Unatumia `GITHUB_TOKEN` iliyojengwa ndani.

Fanya mchakato wa kutafsiri nyaraka za mradi wako kiotomatiki kwa urahisi ukitumia Co-op Translator GitHub Action. Mwongozo huu utakuelekeza jinsi ya kusanidi action ili kuunda pull request zenye tafsiri mpya kila faili lako la chanzo la Markdown au picha linapobadilika.

> [!IMPORTANT]
>
> **Kuchagua Mwongozo Sahihi:**
>
> Mwongozo huu unaelezea **usanidi rahisi ukitumia `GITHUB_TOKEN` ya kawaida**. Hii ndiyo njia inayopendekezwa kwa watumiaji wengi kwani hauhitaji kusimamia funguo za siri za GitHub App.
>

## Mahitaji ya Awali

Kabla ya kusanidi GitHub Action, hakikisha una taarifa za kuingia kwenye huduma ya AI.

**1. Inahitajika: Taarifa za Modeli ya Lugha ya AI**
Unahitaji taarifa za kuingia kwa angalau moja ya Modeli zinazotumika:

- **Azure OpenAI**: Inahitaji Endpoint, API Key, Majina ya Modeli/Deployment, Toleo la API.
- **OpenAI**: Inahitaji API Key, (Hiari: Org ID, Base URL, Model ID).
- Tazama [Modeli na Huduma Zinazotumika](../../../../README.md) kwa maelezo zaidi.

**2. Hiari: Taarifa za AI Vision (kwa Tafsiri ya Picha)**

- Inahitajika tu kama unahitaji kutafsiri maandishi ndani ya picha.
- **Azure AI Vision**: Inahitaji Endpoint na Subscription Key.
- Kama hautatoa, action itatumia [Markdown-only mode](../markdown-only-mode.md) kama chaguo-msingi.

## Usanidi na Mpangilio

Fuata hatua hizi kusanidi Co-op Translator GitHub Action kwenye mradi wako ukitumia `GITHUB_TOKEN` ya kawaida.

### Hatua ya 1: Elewa Uthibitishaji (Kutumia `GITHUB_TOKEN`)

Workflow hii inatumia `GITHUB_TOKEN` iliyojengwa ndani na GitHub Actions. Token hii inatoa ruhusa kiotomatiki kwa workflow kuingiliana na mradi wako kulingana na mipangilio utakayoweka kwenye **Hatua ya 3**.

### Hatua ya 2: Sanidi Siri za Mradi

Unachotakiwa ni kuongeza **taarifa zako za huduma ya AI** kama siri zilizofichwa kwenye mipangilio ya mradi wako.

1.  Nenda kwenye mradi wako wa GitHub unaolengwa.
2.  Nenda kwenye **Settings** > **Secrets and variables** > **Actions**.
3.  Chini ya **Repository secrets**, bonyeza **New repository secret** kwa kila siri ya huduma ya AI inayohitajika kama ilivyoorodheshwa hapa chini.

    ![Chagua sehemu ya settings](../../../../translated_images/select-setting-action.3b95c915d60311592ca51ecb91b3a7bbe0ae45438a2ee872c1520dc90b677780.sw.png) *(Marejeo ya Picha: Inaonyesha mahali pa kuongeza siri)*

**Siri za Huduma ya AI Zinazohitajika (Ongeza ZOTE zinazohusika kulingana na Mahitaji yako):**

| Jina la Siri                         | Maelezo                               | Chanzo cha Thamani                     |
| :---------------------------------- | :---------------------------------------- | :------------------------------- |
| `AZURE_AI_SERVICE_API_KEY`            | Key ya Azure AI Service (Computer Vision)  | Azure AI Foundry yako               |
| `AZURE_AI_SERVICE_ENDPOINT`         | Endpoint ya Azure AI Service (Computer Vision) | Azure AI Foundry yako               |
| `AZURE_OPENAI_API_KEY`              | Key ya huduma ya Azure OpenAI              | Azure AI Foundry yako               |
| `AZURE_OPENAI_ENDPOINT`             | Endpoint ya huduma ya Azure OpenAI         | Azure AI Foundry yako               |
| `AZURE_OPENAI_MODEL_NAME`           | Jina la Modeli ya Azure OpenAI              | Azure AI Foundry yako               |
| `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` | Jina la Deployment ya Azure OpenAI         | Azure AI Foundry yako               |
| `AZURE_OPENAI_API_VERSION`          | Toleo la API la Azure OpenAI              | Azure AI Foundry yako               |
| `OPENAI_API_KEY`                    | API Key ya OpenAI                        | OpenAI Platform yako              |
| `OPENAI_ORG_ID`                     | OpenAI Organization ID (Hiari)         | OpenAI Platform yako              |
| `OPENAI_CHAT_MODEL_ID`              | Model ID maalum ya OpenAI (Hiari)       | OpenAI Platform yako              |
| `OPENAI_BASE_URL`                   | Base URL ya API ya OpenAI (Hiari)     | OpenAI Platform yako              |

### Hatua ya 3: Sanidi Ruhusa za Workflow

GitHub Action inahitaji ruhusa kupitia `GITHUB_TOKEN` ili kuchukua code na kuunda pull request.

1.  Kwenye mradi wako, nenda kwenye **Settings** > **Actions** > **General**.
2.  Shuka chini kwenye sehemu ya **Workflow permissions**.
3.  Chagua **Read and write permissions**. Hii inampa `GITHUB_TOKEN` ruhusa za `contents: write` na `pull-requests: write` kwa workflow hii.
4.  Hakikisha kisanduku cha **Allow GitHub Actions to create and approve pull requests** kimewekwa alama ya tiki.
5.  Bonyeza **Save**.

![Mpangilio wa ruhusa](../../../../translated_images/permission-setting.ae2f02748b0579e7dc3633f14dad67005b533ea8f69890818857de058089a7f5.sw.png)

### Hatua ya 4: Tengeneza Faili la Workflow

Hatimaye, tengeneza faili la YAML linaloelezea workflow ya kiotomatiki ukitumia `GITHUB_TOKEN`.

1.  Kwenye mzizi wa mradi wako, tengeneza `.github/workflows/` kama haipo.
2.  Ndani ya `.github/workflows/`, tengeneza faili liitwalo `co-op-translator.yml`.
3.  Bandika yaliyomo yafuatayo kwenye `co-op-translator.yml`.

```yaml
name: Co-op Translator

on:
  push:
    branches:
      - main

jobs:
  co-op-translator:
    runs-on: ubuntu-latest

    permissions:
      contents: write
      pull-requests: write

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      - name: Install Co-op Translator
        run: |
          python -m pip install --upgrade pip
          pip install co-op-translator

      - name: Run Co-op Translator
        env:
          PYTHONIOENCODING: utf-8
          # === AI Service Credentials ===
          AZURE_AI_SERVICE_API_KEY: ${{ secrets.AZURE_AI_SERVICE_API_KEY }}
          AZURE_AI_SERVICE_ENDPOINT: ${{ secrets.AZURE_AI_SERVICE_ENDPOINT }}
          AZURE_OPENAI_API_KEY: ${{ secrets.AZURE_OPENAI_API_KEY }}
          AZURE_OPENAI_ENDPOINT: ${{ secrets.AZURE_OPENAI_ENDPOINT }}
          AZURE_OPENAI_MODEL_NAME: ${{ secrets.AZURE_OPENAI_MODEL_NAME }}
          AZURE_OPENAI_CHAT_DEPLOYMENT_NAME: ${{ secrets.AZURE_OPENAI_CHAT_DEPLOYMENT_NAME }}
          AZURE_OPENAI_API_VERSION: ${{ secrets.AZURE_OPENAI_API_VERSION }}
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
          OPENAI_ORG_ID: ${{ secrets.OPENAI_ORG_ID }}
          OPENAI_CHAT_MODEL_ID: ${{ secrets.OPENAI_CHAT_MODEL_ID }}
          OPENAI_BASE_URL: ${{ secrets.OPENAI_BASE_URL }}
        run: |
          # =====================================================================
          # IMPORTANT: Set your target languages here (REQUIRED CONFIGURATION)
          # =====================================================================
          # Example: Translate to Spanish, French, German. Add -y to auto-confirm.
          translate -l "es fr de" -y  # <--- MODIFY THIS LINE with your desired languages

      - name: Create Pull Request with translations
        uses: peter-evans/create-pull-request@v5
        with:
          token: ${{ secrets.GITHUB_TOKEN }}
          commit-message: "🌐 Update translations via Co-op Translator"
          title: "🌐 Update translations via Co-op Translator"
          body: |
            This PR updates translations for recent changes to the main branch.

            ### 📋 Changes included
            - Translated contents are available in the `translations/` directory
            - Translated images are available in the `translated_images/` directory

            ---
            🌐 Automatically generated by the [Co-op Translator](https://github.com/Azure/co-op-translator) GitHub Action.
          branch: update-translations
          base: main
          labels: translation, automated-pr
          delete-branch: true
          add-paths: |
            translations/
            translated_images/
```
4.  **Badilisha Workflow kulingana na mahitaji yako:**
  - **[!IMPORTANT] Lugha Lengwa:** Katika hatua ya `Run Co-op Translator`, **LAZIMA ukague na kubadilisha orodha ya nambari za lugha** ndani ya amri `translate -l "..." -y` ili ziendane na mahitaji ya mradi wako. Orodha ya mfano (`ar de es...`) inapaswa kubadilishwa au kurekebishwa.
  - **Trigger (`on:`):** Trigger ya sasa inaendesha kila push kwenye `main`. Kwa miradi mikubwa, fikiria kuongeza kigezo cha `paths:` (tazama mfano ulioandikwa maoni kwenye YAML) ili workflow iendeshe tu pale faili husika (kama vile nyaraka za chanzo) zinapobadilika, hivyo kuokoa muda wa runner.
  - **Maelezo ya PR:** Badilisha `commit-message`, `title`, `body`, jina la `branch`, na `labels` kwenye hatua ya `Create Pull Request` kama inahitajika.

## Kuendesha Workflow

> [!WARNING]  
> **Muda wa Kuendesha GitHub-hosted Runner:**  
> Runners wa GitHub-hosted kama `ubuntu-latest` wana **muda wa juu wa kuendesha wa masaa 6**.  
> Kwa miradi mikubwa ya nyaraka, kama mchakato wa tafsiri utazidi masaa 6, workflow itakatizwa kiotomatiki.  
> Ili kuepuka hili, fikiria:  
> - Kutumia **self-hosted runner** (hakuna kikomo cha muda)  
> - Kupunguza idadi ya lugha lengwa kwa kila mzunguko

Mara faili la `co-op-translator.yml` litakapounganishwa kwenye tawi lako kuu (au tawi lililobainishwa kwenye trigger ya `on:`), workflow itaendeshwa kiotomatiki kila mabadiliko yanaposukumwa kwenye tawi hilo (na yanalingana na kigezo cha `paths` kama kimewekwa).

---

**Kanusho**:
Hati hii imetafsiriwa kwa kutumia huduma ya kutafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati asili katika lugha yake ya asili inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, inashauriwa kutumia huduma ya utafsiri wa kibinadamu wa kitaalamu. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zitakazotokana na matumizi ya tafsiri hii.