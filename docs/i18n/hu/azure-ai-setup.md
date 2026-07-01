# Azure AI beállítása

Használja ezt az útmutatót, amikor az Azure OpenAI-t szeretné konfigurálni szöveg fordításához és az Azure AI Vision-t képekből történő szövegkinyeréshez.

## Előfeltételek

- Egy Azure-előfizetés.
- Jogosultság Azure AI erőforrások és modelltelepítések létrehozásához vagy használatához.
- Egy projekt az Azure AI Foundry-ban, vagy egyenértékű hozzáférés az Azure OpenAI és Azure AI Vision erőforrásokhoz.

## Azure AI-projekt létrehozása

1. Nyissa meg az [Azure AI Foundry](https://ai.azure.com).
2. Hozzon létre vagy válasszon ki egy projektet.
3. Hozzon létre vagy válasszon ki egy AI hubot a projekthez.
4. A létrehozás után nyissa meg a projekt áttekintését.

## Azure OpenAI-modell telepítése

1. A projektben nyissa meg a **Modellek + végpontok** részt.
2. Válassza a **Model telepítése** lehetőséget.
3. Válasszon egy GPT-modellt, például a `gpt-4o`-t.
4. Telepítse a modellt.
5. Jegyezze fel a végpontot, a telepítés nevét, a modell nevét, az API-kulcsot és az API verzióját.

!!! note
    Az Azure OpenAI API-verzió különbözik az Azure AI Foundry-ban megjelenített modell verziójától. Válasszon a telepítéséhez támogatott API-verziót.

## Azure AI Vision konfigurálása

A képek fordítása során az Azure AI Vision-t használjuk a forrásképekből való szövegkinyerésre, mielőtt a szöveget lefordítanánk.

Az Azure AI projektjében keresse meg az Azure AI Services kulcsát és végpontját.

![Azure AI szolgáltatás információinak megkeresése](../../assets/find-azure-ai-info.png)

Rögzítse:

- Azure AI Service végpontja
- Azure AI Service API-kulcsa

## Környezeti változók

Adja hozzá a hitelesítő adatokat a `.env` fájlhoz vagy a CI titkokhoz.

```bash
# Azure AI Vision, szükséges a képek fordításához
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"

# Azure OpenAI, szükséges a szövegek fordításához
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

A Co-op Translator opcionális tartalék hitelesítőkészleteket is támogat. Ismételje meg a teljes szolgáltató-készletet olyan végződésekkel, mint `_1` vagy `_2`; egy tartalék készletbeli összes változónak ugyanazt a végződést kell használnia.

```bash
AZURE_OPENAI_API_KEY_1="..."
AZURE_OPENAI_ENDPOINT_1="https://<resource-1>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME_1="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME_1="<deployment-1>"
AZURE_OPENAI_API_VERSION_1="2024-12-01-preview"
```

## Következő lépések

- Térjen vissza a [Configuration](configuration.md) oldalra, hogy beállítsa a helyi vagy CI környezeti változókat.
- Használja a [CLI referencia](cli.md)-t a fordítási parancsokhoz.
- Használja a [GitHub Actions](github-actions.md)-t a fordítási pull requestek automatizálásához.