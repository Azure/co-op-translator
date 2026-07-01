# Azure AI -määritys

Käytä tätä opasta, kun haluat määrittää Azure OpenAI:n tekstikäännöksiä varten ja Azure AI Visionin kuvatekstin poimintaa varten.

## Edellytykset

- Azure-tilaus.
- Oikeus luoda tai käyttää Azure AI -resursseja ja mallien käyttöönottoja.
- Projekti Azure AI Foundryssa tai vastaavat oikeudet Azure OpenAI- ja Azure AI Vision -resursseihin.

## Luo Azure AI -projekti

1. Avaa [Azure AI Foundry](https://ai.azure.com).
2. Luo tai valitse projekti.
3. Luo tai valitse projektille AI-hubi.
4. Avaa projektin yleiskatsaus luomisen jälkeen.

## Ota Azure OpenAI -malli käyttöön

1. Projektissa avaa **Models + endpoints**.
2. Valitse **Deploy model**.
3. Valitse GPT-malli, esimerkiksi `gpt-4o`.
4. Ota malli käyttöön.
5. Tallenna päätepiste, käyttöönoton nimi, mallin nimi, API-avain ja API-versio.

!!! note
    Azure OpenAI:n API-versio on erillinen Azure AI Foundryssa näytettävästä malliversiosta. Valitse käyttöönotolle tuettu API-versio.

## Määritä Azure AI Vision

Kuvakäännös käyttää Azure AI Visionia lähdekuvista löytyvän tekstin poimintaan ennen kääntämistä.

Etsi Azure AI -projektistasi Azure AI Services -avain ja päätepiste.

![Etsi Azure AI -palvelun tiedot](../../assets/find-azure-ai-info.png)

Tallenna:

- Azure AI Service -päätepiste
- Azure AI Service -API-avain

## Ympäristömuuttujat

Lisää tunnistetiedot `.env`-tiedostoosi tai CI-salaisuuksiin.

```bash
# Azure AI Vision, vaaditaan kuvien kääntämiseen
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"

# Azure OpenAI, vaaditaan tekstin kääntämiseen
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Co-op Translator tukee myös valinnaisia varatunnistetietosarjoja. Kopioi täydellinen tarjoajasarja ja lisää loppuliite, kuten `_1` tai `_2`; kaikilla varasarjan muuttujilla on oltava sama loppuliite.

```bash
AZURE_OPENAI_API_KEY_1="..."
AZURE_OPENAI_ENDPOINT_1="https://<resource-1>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME_1="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME_1="<deployment-1>"
AZURE_OPENAI_API_VERSION_1="2024-12-01-preview"
```

## Seuraavat vaiheet

- Palaa kohtaan [Määritys](configuration.md) asettaaksesi paikalliset tai CI-ympäristömuuttujat.
- Käytä [CLI-viite](cli.md) käännöskomentoihin.
- Käytä [GitHub Actions](github-actions.md) automatisoimaan käännöspyyntöjen luominen.