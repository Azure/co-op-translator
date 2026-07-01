# Konfiguracja Azure AI

Skorzystaj z tego przewodnika, gdy chcesz skonfigurować Azure OpenAI do tłumaczenia tekstu i Azure AI Vision do ekstrakcji tekstu z obrazów.

## Wymagania wstępne

- Subskrypcja Azure.
- Uprawnienia do tworzenia lub używania zasobów Azure AI i wdrożeń modeli.
- Projekt w Azure AI Foundry lub równoważny dostęp do zasobów Azure OpenAI i Azure AI Vision.

## Utwórz projekt Azure AI

1. Otwórz [Azure AI Foundry](https://ai.azure.com).
2. Utwórz lub wybierz projekt.
3. Utwórz lub wybierz centrum AI dla projektu.
4. Otwórz przegląd projektu po jego utworzeniu.

## Wdróż model Azure OpenAI

1. W projekcie otwórz **Modele + punkty końcowe**.
2. Wybierz **Wdróż model**.
3. Wybierz model GPT, na przykład `gpt-4o`.
4. Wdróż model.
5. Zapisz punkt końcowy, nazwę wdrożenia, nazwę modelu, klucz API oraz wersję API.

!!! note
    Wersja Azure OpenAI API jest odrębna od wersji modelu wyświetlanej w Azure AI Foundry. Wybierz obsługiwaną wersję API dla swojego wdrożenia.

## Skonfiguruj Azure AI Vision

Tłumaczenie obrazów wykorzystuje Azure AI Vision do wyodrębniania tekstu z obrazów źródłowych przed ich tłumaczeniem.

W swoim projekcie Azure AI znajdź klucz i punkt końcowy usługi Azure AI Services.

![Znajdź informacje o usłudze Azure AI](../../assets/find-azure-ai-info.png)

Zapisz:

- Punkt końcowy usługi Azure AI Service
- Klucz API usługi Azure AI Service

## Zmienne środowiskowe

Dodaj poświadczenia do pliku `.env` lub sekretów CI.

```bash
# Azure AI Vision, wymagany do tłumaczenia obrazów
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"

# Azure OpenAI, wymagany do tłumaczenia tekstu
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Co-op Translator obsługuje także opcjonalne zestawy poświadczeń zapasowych. Zduplikuj pełny zestaw dostawcy z przyrostkami takimi jak `_1` lub `_2`; wszystkie zmienne w zestawie zapasowym muszą mieć ten sam przyrostek.

```bash
AZURE_OPENAI_API_KEY_1="..."
AZURE_OPENAI_ENDPOINT_1="https://<resource-1>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME_1="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME_1="<deployment-1>"
AZURE_OPENAI_API_VERSION_1="2024-12-01-preview"
```

## Kolejne kroki

- Wróć do [Konfiguracja](configuration.md), aby skonfigurować zmienne środowiskowe lokalnie lub w CI.
- Użyj [CLI Reference](cli.md) do poleceń tłumaczenia.
- Użyj [GitHub Actions](github-actions.md), aby zautomatyzować pull requesty tłumaczeń.