<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8f776df01855a3a659c8eb6f16a5de74",
  "translation_date": "2025-10-15T03:07:00+00:00",
  "source_file": "README.md",
  "language_code": "pl"
}
-->
# Co-op Translator

_Automatyzuj tłumaczenie swojej edukacyjnej zawartości na GitHubie na wiele języków i docieraj do odbiorców na całym świecie._

[![Python package](https://img.shields.io/pypi/v/co-op-translator?color=4BA3FF)](https://pypi.org/project/co-op-translator/)
[![License: MIT](https://img.shields.io/github/license/azure/co-op-translator?color=4BA3FF)](https://github.com/azure/co-op-translator/blob/main/LICENSE)
[![Downloads](https://static.pepy.tech/badge/co-op-translator)](https://pepy.tech/project/co-op-translator)
[![Downloads](https://static.pepy.tech/badge/co-op-translator/month)](https://pepy.tech/project/co-op-translator)
[![Container: GHCR](https://img.shields.io/badge/Container-GHCR-2496ED?logo=docker&logoColor=fff)](https://github.com/azure/co-op-translator/pkgs/container/co-op-translator)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[![GitHub contributors](https://img.shields.io/github/contributors/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/graphs/contributors/)
[![GitHub issues](https://img.shields.io/github/issues/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/issues/)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/pulls/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

### 🌐 Obsługa wielu języków

#### Obsługiwane przez [Co-op Translator](https://github.com/Azure/Co-op-Translator)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh/README.md) | [Chinese (Traditional, Hong Kong)](../hk/README.md) | [Chinese (Traditional, Macau)](../mo/README.md) | [Chinese (Traditional, Taiwan)](../tw/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](./README.md) | [Portuguese (Brazil)](../br/README.md) | [Portuguese (Portugal)](../pt/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Azure AI Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)
[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## Przegląd

**Co-op Translator** pozwala szybko tłumaczyć edukacyjne treści na GitHubie na wiele języków, dzięki czemu łatwo docierasz do odbiorców na całym świecie. Gdy aktualizujesz pliki Markdown, obrazy lub notatniki Jupyter, tłumaczenia są automatycznie synchronizowane, by Twoje materiały edukacyjne były zawsze aktualne i dostępne dla międzynarodowych użytkowników.

Zobacz, jak Co-op Translator organizuje przetłumaczone materiały edukacyjne na GitHubie:

![Przykład](../../translated_images/translation-ex.0c8aa6a7ee0aad2b35cddcc110c719baf0afc640e8c5a45540e6c166b9907d91.pl.png)

## Szybki start

```bash
# Create and activate a virtual environment (recommended)
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
# Install the package
pip install co-op-translator
# Translate
translate -l "ko ja fr" -md
```

Docker:

```bash
# Pull the public image from GHCR
docker pull ghcr.io/azure/co-op-translator:latest
# Run with current folder mounted and .env provided (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko ja fr" -md
```

## Minimalna konfiguracja

- Utwórz plik `.env` na podstawie szablonu: [.env.template](../../.env.template)
- Skonfiguruj jednego dostawcę LLM (Azure OpenAI lub OpenAI)
- Do tłumaczenia obrazów (`-img`) skonfiguruj także Azure AI Vision
- Zalecane: Jeśli masz tłumaczenia wygenerowane przez inne narzędzia, najpierw je usuń, aby uniknąć konfliktów (np. `translations/`).
- Zalecane: Dodaj sekcję tłumaczeń do swojego README, korzystając z [szablonu języków README](./README_languages_template.md)
- Zobacz: [Konfiguracja Azure AI](./getting_started/set-up-azure-ai.md)

## Użycie

Tłumaczenie wszystkich obsługiwanych typów:

```bash
translate -l "ko ja"
```

Tylko Markdown:

```bash
translate -l "de" -md
```

Markdown + obrazy:

```bash
translate -l "pt" -md -img
```

Tylko notatniki:

```bash
translate -l "zh" -nb
```

Więcej opcji: [Opis poleceń](./getting_started/command-reference.md)

## Funkcje

- Automatyczne tłumaczenie plików Markdown, notatników i obrazów
- Synchronizacja tłumaczeń z aktualizacjami źródła
- Działa lokalnie (CLI) lub w CI (GitHub Actions)
- Wykorzystuje Azure OpenAI lub OpenAI; opcjonalnie Azure AI Vision do obrazów
- Zachowuje formatowanie i strukturę Markdown

## Dokumentacja

- [Przewodnik po linii poleceń](./getting_started/command-line-guide/command-line-guide.md)
- [Przewodnik po GitHub Actions (repozytoria publiczne i standardowe sekrety)](./getting_started/github-actions-guide/github-actions-guide-public.md)
- [Przewodnik po GitHub Actions (repozytoria organizacji Microsoft i konfiguracje na poziomie organizacji)](./getting_started/github-actions-guide/github-actions-guide-org.md)
- [Obsługiwane języki](./getting_started/supported-languages.md)
- [Rozwiązywanie problemów](./getting_started/troubleshooting.md)

## Wesprzyj nas i wspieraj globalną edukację

Dołącz do nas i zmieniaj sposób udostępniania treści edukacyjnych na świecie! Daj [Co-op Translator](https://github.com/azure/co-op-translator) ⭐ na GitHubie i wesprzyj naszą misję przełamywania barier językowych w nauce i technologii. Twoje zainteresowanie i wkład mają ogromne znaczenie! Wszelkie propozycje funkcji i kontrybucje do kodu są mile widziane.

### Odkrywaj edukacyjne materiały Microsoft w swoim języku

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

Dowiedz się więcej o Co-op Translator z naszych prezentacji _(Kliknij obrazek poniżej, aby obejrzeć na YouTube.)_:

- **Open at Microsoft**: Krótkie 18-minutowe wprowadzenie i szybki przewodnik po użyciu Co-op Translator.

  [![Open at Microsoft](../../translated_images/open-ms-thumbnail.946b356b89bc5f0e33dcebb852f7926b98c33f54c1a49ce01c36ae7f35e2443a.pl.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## Współtworzenie

Ten projekt jest otwarty na kontrybucje i sugestie. Chcesz współtworzyć Azure Co-op Translator? Zajrzyj do [CONTRIBUTING.md](./CONTRIBUTING.md), aby dowiedzieć się, jak możesz pomóc uczynić Co-op Translator bardziej dostępnym.

## Współtwórcy

[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## Kodeks postępowania

Ten projekt przyjął [Kodeks postępowania Microsoft Open Source](https://opensource.microsoft.com/codeofconduct/).
Więcej informacji znajdziesz w [FAQ dotyczących kodeksu postępowania](https://opensource.microsoft.com/codeofconduct/faq/) lub
skontaktuj się z [opencode@microsoft.com](mailto:opencode@microsoft.com), jeśli masz dodatkowe pytania lub uwagi.

## Odpowiedzialna AI

Microsoft zobowiązuje się do wspierania klientów w odpowiedzialnym korzystaniu z naszych produktów AI, dzielenia się doświadczeniami i budowania relacji opartych na zaufaniu dzięki narzędziom takim jak Transparency Notes i Impact Assessments. Wiele z tych zasobów znajdziesz na [https://aka.ms/RAI](https://aka.ms/RAI).
Podejście Microsoft do odpowiedzialnej AI opiera się na zasadach: uczciwości, niezawodności i bezpieczeństwa, prywatności i ochrony, inkluzywności, przejrzystości oraz odpowiedzialności.

Modele językowe, obrazowe i głosowe na dużą skalę – takie jak te używane w tym projekcie – mogą czasem zachowywać się w sposób nieuczciwy, nieprzewidywalny lub obraźliwy, co może prowadzić do szkód. Zapoznaj się z [notą transparentności usługi Azure OpenAI](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text), aby poznać ryzyka i ograniczenia.

Zalecanym sposobem ograniczania tych ryzyk jest wdrożenie systemu bezpieczeństwa, który wykryje i zapobiegnie szkodliwym zachowaniom. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) zapewnia niezależną warstwę ochrony, wykrywając szkodliwe treści generowane przez użytkowników i AI w aplikacjach i usługach. Azure AI Content Safety oferuje API do tekstu i obrazów, które pozwalają wykrywać szkodliwe materiały. Dostępne jest także interaktywne Content Safety Studio, gdzie możesz przetestować przykładowy kod wykrywający szkodliwe treści w różnych formatach. [Dokumentacja szybkiego startu](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) przeprowadzi Cię przez wysyłanie zapytań do tej usługi.
Kolejnym aspektem, który warto wziąć pod uwagę, jest ogólna wydajność aplikacji. W przypadku aplikacji wielomodalnych i opartych na wielu modelach, wydajność oznacza, że system działa zgodnie z oczekiwaniami Twoimi i użytkowników, w tym nie generuje szkodliwych wyników. Ważne jest, aby ocenić wydajność całej aplikacji, korzystając z <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in">metryk jakości generowania oraz ryzyka i bezpieczeństwa</a>.

Możesz ocenić swoją aplikację AI w środowisku deweloperskim, korzystając z <a href="https://microsoft.github.io/promptflow/index.html">prompt flow SDK</a>. Na podstawie zbioru testowego lub wybranego celu, generacje Twojej aplikacji AI są mierzone ilościowo za pomocą wbudowanych lub własnych ewaluatorów. Aby rozpocząć pracę z prompt flow SDK i ocenić swój system, możesz skorzystać z <a href="https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk">przewodnika szybkiego startu</a>. Po przeprowadzeniu ewaluacji możesz <a href="https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results">zwizualizować wyniki w Azure AI Studio</a>.

## Znaki towarowe

Ten projekt może zawierać znaki towarowe lub logotypy projektów, produktów lub usług. Autoryzowane użycie znaków towarowych lub logotypów Microsoftu podlega i musi być zgodne z <a href="https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general">Wytycznymi dotyczącymi znaków towarowych i marki Microsoft</a>. Użycie znaków towarowych lub logotypów Microsoftu w zmodyfikowanych wersjach tego projektu nie może wprowadzać w błąd ani sugerować sponsorowania przez Microsoft. Wszelkie użycie znaków towarowych lub logotypów stron trzecich podlega zasadom tych stron.

## Uzyskiwanie pomocy

Jeśli utkniesz lub masz pytania dotyczące tworzenia aplikacji AI, dołącz do:

<a href="https://aka.ms/foundry/discord"><img src="https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff" alt="Azure AI Foundry Discord"></a>

Jeśli masz uwagi dotyczące produktu lub napotkasz błędy podczas tworzenia, odwiedź:

<a href="https://aka.ms/foundry/forum"><img src="https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff" alt="Azure AI Foundry Developer Forum"></a>

---

**Zastrzeżenie**:  
Ten dokument został przetłumaczony przy użyciu usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Dokładamy wszelkich starań, aby tłumaczenie było poprawne, jednak należy pamiętać, że tłumaczenia automatyczne mogą zawierać błędy lub nieścisłości. Za wiążące źródło należy uznać oryginalny dokument w jego języku ojczystym. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnych usług tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za wszelkie nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.