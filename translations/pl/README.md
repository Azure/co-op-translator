# Co-op Translator

_Easily automate and maintain translations for your educational GitHub content across multiple languages as your project evolves._

![Python 3.10–3.12](https://img.shields.io/badge/python-3.10--3.12-blue)
[![Pakiet Pythona](https://img.shields.io/pypi/v/co-op-translator?color=4BA3FF)](https://pypi.org/project/co-op-translator/)
[![Licencja: MIT](https://img.shields.io/github/license/azure/co-op-translator?color=4BA3FF)](https://github.com/azure/co-op-translator/blob/main/LICENSE)
[![Pobrania](https://static.pepy.tech/badge/co-op-translator)](https://pepy.tech/project/co-op-translator)
[![Pobrania](https://static.pepy.tech/badge/co-op-translator/month)](https://pepy.tech/project/co-op-translator)
[![Kontener: GHCR](https://img.shields.io/badge/Container-GHCR-2496ED?logo=docker&logoColor=fff)](https://github.com/azure/co-op-translator/pkgs/container/co-op-translator)
[![Styl kodu: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[![Współtwórcy GitHub](https://img.shields.io/github/contributors/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/graphs/contributors/)
[![Zgłoszenia GitHub](https://img.shields.io/github/issues/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/issues/)
[![Pull requesty GitHub](https://img.shields.io/github/issues-pr/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/pulls/)
[![PR-y mile widziane](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

**Zacznij tutaj:** [Wybierz swój przepływ pracy](https://azure.github.io/co-op-translator/workflows/) | [Konfiguracja](https://azure.github.io/co-op-translator/configuration/) | [CLI](https://azure.github.io/co-op-translator/cli/) | [Python API](https://azure.github.io/co-op-translator/api/) | [Serwer MCP](https://azure.github.io/co-op-translator/mcp/)

### 🌐 Wsparcie wielu języków

#### Obsługiwane przez [Co-op Translator](https://github.com/Azure/co-op-translator)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabski](../ar/README.md) | [Bengalski](../bn/README.md) | [Bułgarski](../bg/README.md) | [Birmański (Myanmar)](../my/README.md) | [Chiński (uproszczony)](../zh-CN/README.md) | [Chiński (tradycyjny, Hongkong)](../zh-HK/README.md) | [Chiński (tradycyjny, Makau)](../zh-MO/README.md) | [Chiński (tradycyjny, Tajwan)](../zh-TW/README.md) | [Chorwacki](../hr/README.md) | [Czeski](../cs/README.md) | [Duński](../da/README.md) | [Niderlandzki](../nl/README.md) | [Estoński](../et/README.md) | [Fiński](../fi/README.md) | [Francuski](../fr/README.md) | [Niemiecki](../de/README.md) | [Grecki](../el/README.md) | [Hebrajski](../he/README.md) | [Hindi](../hi/README.md) | [Węgierski](../hu/README.md) | [Indonezyjski](../id/README.md) | [Włoski](../it/README.md) | [Japoński](../ja/README.md) | [Kannada](../kn/README.md) | [Khmerski](../km/README.md) | [Koreański](../ko/README.md) | [Litewski](../lt/README.md) | [Malajski](../ms/README.md) | [Malajalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepalski](../ne/README.md) | [Pidgin nigeryjski](../pcm/README.md) | [Norweski](../no/README.md) | [Perski (Farsi)](../fa/README.md) | [Polski](./README.md) | [Portugalski (Brazylia)](../pt-BR/README.md) | [Portugalski (Portugalia)](../pt-PT/README.md) | [Pendżabski (Gurmukhi)](../pa/README.md) | [Rumuński](../ro/README.md) | [Rosyjski](../ru/README.md) | [Serbski (cyrylica)](../sr/README.md) | [Słowacki](../sk/README.md) | [Słoweński](../sl/README.md) | [Hiszpański](../es/README.md) | [Suahili](../sw/README.md) | [Szwedzki](../sv/README.md) | [Tagalog (filipiński)](../tl/README.md) | [Tamilski](../ta/README.md) | [Telugu](../te/README.md) | [Tajski](../th/README.md) | [Turecki](../tr/README.md) | [Ukraiński](../uk/README.md) | [Urdu](../ur/README.md) | [Wietnamski](../vi/README.md)

> **Wolisz klonować lokalnie?**
>
> To repozytorium zawiera tłumaczenia na ponad 50 języków, co znacząco zwiększa rozmiar pobierania. Aby sklonować bez tłumaczeń, użyj sparse checkout:
>
> **Bash / macOS / Linux:**
> ```bash
> git clone --filter=blob:none --sparse https://github.com/Azure/co-op-translator.git
> cd co-op-translator
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
>
> **CMD (Windows):**
> ```cmd
> git clone --filter=blob:none --sparse https://github.com/Azure/co-op-translator.git
> cd co-op-translator
> git sparse-checkout set --no-cone "/*" "!translations" "!translated_images"
> ```
>
> To daje wszystko, czego potrzebujesz, aby ukończyć kurs przy znacznie szybszym pobieraniu.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![Obserwatorzy GitHub](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![Forki GitHub](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![Gwiazdy GitHub](https://img.shields.io/github/stars/azure/co-op-translator.svg?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Otwórz w GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## Przegląd

**Co-op Translator** pomaga lokalizować treści edukacyjne na GitHub na wiele języków bez wysiłku.
Gdy aktualizujesz pliki Markdown, obrazy lub notebooki, tłumaczenia pozostają automatycznie zsynchronizowane, zapewniając, że Twoje materiały są dokładne i aktualne dla uczących się na całym świecie.

Używaj go z CLI do tłumaczenia repozytorium, z API Pythona do automatyzacji lub przez serwer MCP do przepływów pracy z agentami i edytorami.

Przykład organizacji przetłumaczonej zawartości:

![Przykład](../../imgs/translation-ex.png)

## Dlaczego Co-op Translator?

Tłumaczenie jednego pliku jest proste. Utrzymanie całego repozytorium dokumentacji
przetłumaczonego, powiązanego i aktualnego to trudne zadanie.

| Problem | Jak Co-op Translator pomaga |
| --- | --- |
| Long docs are not one prompt | Duże pliki Markdown są dzielone na fragmenty, dzięki czemu długi README nie zależy od jednej kruchej odpowiedzi modelu. Jeśli fragment się nie powiedzie, Co-op Translator może ponowić próbę i ponownie podzielić tylko nieudany fragment. |
| Incomplete translations should not be marked current | Ucięte tłumaczenie nigdy nie powinno być oznaczone jako aktualne. Co-op Translator sprawdza integralność tłumaczeń przed zapisaniem i potrafi wykryć strukturalnie niekompletne istniejące tłumaczenia. |
| Links should match the translated repo structure | Ręczne tłumaczenia często pozostawiają względne linki wskazujące z powrotem na drzewo źródłowe. Co-op Translator przepisuje linki do Markdown, notebooków, obrazów i README, aby pasowały do struktury `translations/<lang>/...`. |
| Translation should work across an entire repo | Co-op Translator obsługuje pliki README, dokumentację, notebooki i tekst na obrazach jako część jednego przepływu pracy repozytorium, zamiast tłumaczyć pliki pojedynczo. |
| Maintaining translations matters more than creating them once | Hash'e źródeł i metadane tłumaczeń pozwalają Co-op Translator znaleźć przestarzałe pliki, pominąć niezmienione pliki i utrzymać zsynchronizowaną zawartość tłumaczeń w miarę ewolucji repozytorium źródłowego. |

## Jak zarządzany jest stan tłumaczeń

Co-op Translator zarządza przetłumaczoną zawartością jako **wersjonowanymi artefaktami oprogramowania**,  
a nie jako statycznymi plikami.

Narzędzie śledzi stan przetłumaczonych Markdownów, obrazów i notebooków
przy użyciu **metadanych z zakresem języka**.

Takie podejście pozwala Co-op Translator:

- Niezawodnie wykrywać przestarzałe tłumaczenia
- Traktować Markdown, obrazy i notebooki spójnie
- Skalać bezpiecznie w dużych, szybko zmieniających się, wielojęzycznych repozytoriach

Modelując tłumaczenia jako zarządzane artefakty,
przepływy pracy tłumaczeń naturalnie dopasowują się do
nowoczesnych praktyk zarządzania zależnościami i artefaktami oprogramowania.

→ [Jak zarządzany jest stan tłumaczeń](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/rethinking-documentation-translation-treating-translations-as-versioned-software/4491755)

### Powiązane artykuły pogłębione

- [Naprawianie uszkodzonego Markdown w tłumaczeniach AI: Utwardzanie potoków produkcyjnych](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/fixing-broken-markdown-in-ai-translation-hardening-a-production-pipeline/4511378)

## Zaczynamy

Co-op Translator można używać z poziomu CLI, API Pythona lub serwera MCP. Zacznij od przewodnika po przepływach pracy, jeśli wybierasz między tłumaczeniem lokalnym, automatyzacją, CI i integracją agenta/edytora.

- [Wybierz swój przepływ pracy](../../docs/workflows.md)
- [Skonfiguruj poświadczenia](../../docs/configuration.md)
- [Tłumaczenie z CLI](../../docs/cli.md)
- [Automatyzuj za pomocą Python API](../../docs/api.md)
- [Połącz z serwerem MCP](../../docs/mcp.md)
- [Uruchamianie w GitHub Actions](../../docs/github-actions.md)

Minimalny przykład CLI po konfiguracji:

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

pip install co-op-translator
translate -l "ko" -md
co-op-review -l "ko"
```

Dla pierwszych uruchomień na dużych repozytoriach użyj `--dry-run` przed zapisaniem przetłumaczonych plików. Zobacz [Referencję CLI](../../docs/cli.md) dla flag typów zawartości, logów, przeglądu i migracji linków.

Szybkie uruchomienie kontenera z Bash/Zsh:

```bash
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko" -md
```

Szybkie uruchomienie kontenera z PowerShell:

```powershell
docker run --rm -it --env-file .env -v ${PWD}:/work ghcr.io/azure/co-op-translator:latest -l "ko" -md
```

## Funkcje

- Zautomatyzowane tłumaczenia dla Markdown, notebooków i obrazów
- Utrzymuje tłumaczenia w synchronizacji ze zmianami źródła
- Działa lokalnie (CLI) lub w CI (GitHub Actions)
- Udostępnia narzędzia do tłumaczenia Markdown, notebooków, obrazów, przeglądu i projektów przez MCP
- Wykorzystuje Azure OpenAI lub OpenAI do tłumaczeń wspieranych przez dostawcę
- Pozwala serwerowi MCP hostować agentów tłumaczących fragmenty Markdown i notebooków bez poświadczeń LLM Co-op Translator
- Używa Azure AI Vision do ekstrakcji tekstu z obrazów i tłumaczeń
- Przegląda strukturę i aktualność tłumaczeń za pomocą deterministycznych kontroli
- Zachowuje formatowanie i strukturę Markdown

## Dokumentacja

- [Strona dokumentacji](https://azure.github.io/co-op-translator/)
- [Wybierz swój przepływ pracy](../../docs/workflows.md)
- [Konfiguracja](../../docs/configuration.md)
- [Konfiguracja Azure AI](../../docs/azure-ai-setup.md)
- [Referencja CLI](../../docs/cli.md)
- [Python API](../../docs/api.md)
- [Serwer MCP](../../docs/mcp.md)
- [GitHub Actions](../../docs/github-actions.md)
- [Szablon README dla języków](../../docs/readme-languages-template.md)
- [Obsługiwane języki](../../docs/supported-languages.md)
- [Współtworzenie](../../CONTRIBUTING.md)
- [Rozwiązywanie problemów](../../docs/troubleshooting.md)

### Przewodnik specyficzny dla Microsoft
> [!NOTE]
> Tylko dla opiekunów repozytoriów Microsoft „For Beginners”.

- [Aktualizowanie listy „other courses” (tylko dla repozytoriów MS Beginners)](../../docs/microsoft-beginners.md)

## Wesprzyj nas i wspieraj globalne uczenie się

Dołącz do nas w rewolucjonizowaniu sposobu, w jaki treści edukacyjne są udostępniane globalnie! Daj [Co-op Translator](https://github.com/azure/co-op-translator) ⭐ na GitHub i wspieraj naszą misję przełamywania barier językowych w nauce i technologii. Twoje zainteresowanie i wkład mają znaczący wpływ! Wkłady do kodu i sugestie funkcji są zawsze mile widziane.

### Poznaj materiały edukacyjne Microsoft w swoim języku
- [LangChain4j-for-Beginners](https://github.com/microsoft/LangChain4j-for-Beginners)
- [AZD for Beginners](https://github.com/microsoft/AZD-for-beginners)
- [Edge AI for Beginners](https://github.com/microsoft/edgeai-for-beginners)
- [Model Context Protocol (MCP) For Beginners](https://github.com/microsoft/mcp-for-beginners)
- [AI Agents for Beginners](https://github.com/microsoft/ai-agents-for-beginners)
- [Generative AI for Beginners using .NET](https://github.com/microsoft/Generative-AI-for-beginners-dotnet)
- [Generative AI for Beginners](https://github.com/microsoft/generative-ai-for-beginners)
- [Generative AI for Beginners using Java](https://github.com/microsoft/generative-ai-for-beginners-java)
- [ML for Beginners](https://aka.ms/ml-beginners)
- [Data Science for Beginners](https://aka.ms/datascience-beginners)
- [AI for Beginners](https://aka.ms/ai-beginners)
- [Cybersecurity for Beginners](https://github.com/microsoft/Security-101)
- [Web Dev for Beginners](https://aka.ms/webdev-beginners)
- [IoT for Beginners](https://aka.ms/iot-beginners)
- [PhiCookBook](https://github.com/microsoft/PhiCookBook)

## Prezentacje wideo

👉 Kliknij obrazek poniżej, aby obejrzeć na YouTube.

- **Open at Microsoft**: Krótkie 18-minutowe wprowadzenie i szybki poradnik, jak korzystać z Co-op Translator.

  [![Open at Microsoft](../../imgs/open-ms-thumbnail.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## Wkład

Ten projekt zaprasza do wkładu i sugestii. Chcesz przyczynić się do Azure Co-op Translator? Zobacz nasz [CONTRIBUTING.md](../../CONTRIBUTING.md) z wytycznymi, jak możesz pomóc uczynić Co-op Translator bardziej dostępnym.

## Współtwórcy

[![współtwórcy co-op-translator](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## Kodeks postępowania

Ten projekt przyjął [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
Aby uzyskać więcej informacji, zobacz [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) lub
skontaktuj się z [opencode@microsoft.com](mailto:opencode@microsoft.com) w przypadku dodatkowych pytań lub uwag.

## Odpowiedzialna sztuczna inteligencja

Microsoft zobowiązuje się pomagać naszym klientom w odpowiedzialnym korzystaniu z naszych produktów AI, dzielić się naszymi doświadczeniami oraz budować partnerstwa oparte na zaufaniu za pomocą narzędzi takich jak Transparency Notes i Impact Assessments. Wiele z tych zasobów można znaleźć pod adresem [https://aka.ms/RAI](https://aka.ms/RAI).
Podejście Microsoftu do odpowiedzialnej AI opiera się na naszych zasadach dotyczących AI: uczciwości, niezawodności i bezpieczeństwa, prywatności i ochrony, inkluzywności, przejrzystości oraz odpowiedzialności.

Modele dużej skali przetwarzania języka naturalnego, obrazu i mowy — podobne do tych użytych w tym przykładzie — mogą potencjalnie zachowywać się w sposób niesprawiedliwy, zawodny lub obraźliwy, powodując w ten sposób szkody. Zapoznaj się z [Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text), aby uzyskać informacje o ryzykach i ograniczeniach.

Zalecanym podejściem do łagodzenia tych ryzyk jest uwzględnienie w architekturze systemu bezpieczeństwa, który może wykrywać i zapobiegać szkodliwemu zachowaniu. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) zapewnia niezależną warstwę ochrony, zdolną do wykrywania szkodliwych treści tworzonych przez użytkowników i przez AI w aplikacjach i usługach. Azure AI Content Safety obejmuje interfejsy API do analizy tekstu i obrazów, które pozwalają wykrywać materiały szkodliwe. Posiadamy również interaktywne Content Safety Studio, które pozwala przeglądać, badać i wypróbowywać przykładowy kod do wykrywania szkodliwych treści w różnych modalnościach. Następująca [dokumentacja szybkiego startu](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) poprowadzi Cię przez wysyłanie żądań do usługi.

Kolejnym aspektem, który należy wziąć pod uwagę, jest ogólna wydajność aplikacji. W przypadku aplikacji multimodalnych i wykorzystujących wiele modeli, wydajność oznacza zgodność działania systemu z oczekiwaniami Twoimi i Twoich użytkowników, w tym niewytwarzanie szkodliwych wyników. Ważne jest ocenianie wydajności całej aplikacji przy użyciu [generation quality and risk and safety metrics](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in).

Możesz ocenić swoją aplikację AI w środowisku deweloperskim, używając [prompt flow SDK](https://microsoft.github.io/promptflow/index.html). Mając dane testowe lub cel do osiągnięcia, wyniki generowania Twojej aplikacji generatywnej AI są mierzone ilościowo za pomocą wbudowanych ewaluatorów lub niestandardowych ewaluatorów według Twojego wyboru. Aby rozpocząć pracę z prompt flow SDK w celu oceny systemu, możesz skorzystać z [przewodnika szybkiego startu](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Po uruchomieniu oceny możesz [zwizualizować wyniki w Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Znaki towarowe

W tym projekcie mogą występować znaki towarowe lub logotypy projektów, produktów lub usług. Autoryzowane użycie znaków towarowych lub logotypów Microsoft podlega i musi być zgodne z [Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
Użycie znaków towarowych lub logotypów Microsoft w zmodyfikowanych wersjach tego projektu nie może wprowadzać w błąd ani sugerować sponsorowania przez Microsoft.
Każde użycie znaków towarowych lub logotypów podmiotów trzecich podlega zasadom tych podmiotów.

## Uzyskiwanie pomocy

Jeśli utkniesz lub masz pytania dotyczące tworzenia aplikacji AI, dołącz:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Jeśli masz uwagi dotyczące produktu lub napotkasz błędy podczas tworzenia, odwiedź:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)