# Configurare Azure AI

Utilizați acest ghid când doriți să configurați Azure OpenAI pentru traducerea textului și Azure AI Vision pentru extragerea textului din imagini.

## Cerințe prealabile

- Un abonament Azure.
- Permisiunea de a crea sau utiliza resurse Azure AI și implementări de modele.
- Un proiect în Azure AI Foundry sau acces echivalent la resursele Azure OpenAI și Azure AI Vision.

## Creați un proiect Azure AI

1. Deschideți [Azure AI Foundry](https://ai.azure.com).
2. Creați sau selectați un proiect.
3. Creați sau selectați un AI hub pentru proiect.
4. Deschideți prezentarea generală a proiectului după creare.

## Implementați un model Azure OpenAI

1. În proiect, deschideți **Models + endpoints**.
2. Selectați **Deploy model**.
3. Alegeți un model GPT, cum ar fi `gpt-4o`.
4. Implementați modelul.
5. Înregistrați endpoint-ul, numele implementării, numele modelului, cheia API și versiunea API-ului.

!!! note
    Versiunea API Azure OpenAI este separată de versiunea modelului afișată în Azure AI Foundry. Alegeți o versiune API acceptată pentru implementarea dvs.

## Configurați Azure AI Vision

Traducerea imaginilor folosește Azure AI Vision pentru a extrage textul din imaginile sursă înainte ca textul să fie tradus.

În proiectul dvs. Azure AI, găsiți cheia și endpoint-ul Azure AI Services.

![Găsiți informațiile serviciului Azure AI](../../assets/find-azure-ai-info.png)

Înregistrați:

- Endpoint-ul serviciului Azure AI
- Cheia API a serviciului Azure AI

## Variabile de mediu

Adăugați datele de autentificare în fișierul `.env` sau în secretele CI.

```bash
# Azure AI Vision, necesar pentru traducerea imaginilor
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"

# Azure OpenAI, necesar pentru traducerea textului
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Co-op Translator acceptă, de asemenea, seturi opționale de credențiale de rezervă. Duplicați un set complet de furnizor cu sufixe precum `_1` sau `_2`; toate variabilele dintr-un set de rezervă trebuie să aibă același sufix.

```bash
AZURE_OPENAI_API_KEY_1="..."
AZURE_OPENAI_ENDPOINT_1="https://<resource-1>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME_1="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME_1="<deployment-1>"
AZURE_OPENAI_API_VERSION_1="2024-12-01-preview"
```

## Pași următori

- Reveniți la [Configuration](configuration.md) pentru a configura variabilele de mediu locale sau ale CI.
- Folosiți [Referința CLI](cli.md) pentru comenzile de traducere.
- Folosiți [GitHub Actions](github-actions.md) pentru a automatiza pull request-urile de traducere.