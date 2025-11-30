<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "dac6bc281667816537df51f724a0ff2c",
  "translation_date": "2025-11-30T11:02:41+00:00",
  "source_file": "README.md",
  "language_code": "pl"
}
-->
# Co-op Translator

_Łatwo automatyzuj tłumaczenie edukacyjnych treści na GitHubie na wiele języków, aby dotrzeć do globalnej publiczności._

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

### 🌐 Wsparcie wielu języków

#### Obsługiwane przez [Co-op Translator](https://github.com/Azure/Co-op-Translator)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabski](../ar/README.md) | [Bengalski](../bn/README.md) | [Bułgarski](../bg/README.md) | [Birmański (Myanmar)](../my/README.md) | [Chiński (uproszczony)](../zh/README.md) | [Chiński (tradycyjny, Hongkong)](../hk/README.md) | [Chiński (tradycyjny, Makau)](../mo/README.md) | [Chiński (tradycyjny, Tajwan)](../tw/README.md) | [Chorwacki](../hr/README.md) | [Czeski](../cs/README.md) | [Duński](../da/README.md) | [Niderlandzki](../nl/README.md) | [Estoński](../et/README.md) | [Fiński](../fi/README.md) | [Francuski](../fr/README.md) | [Niemiecki](../de/README.md) | [Grecki](../el/README.md) | [Hebrajski](../he/README.md) | [Hindi](../hi/README.md) | [Węgierski](../hu/README.md) | [Indonezyjski](../id/README.md) | [Włoski](../it/README.md) | [Japoński](../ja/README.md) | [Kannada](../kn/README.md) | [Koreański](../ko/README.md) | [Litewski](../lt/README.md) | [Malajski](../ms/README.md) | [Malajalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepalski](../ne/README.md) | [Nigeryjski pidgin](../pcm/README.md) | [Norweski](../no/README.md) | [Perski (Farsi)](../fa/README.md) | [Polski](./README.md) | [Portugalski (Brazylia)](../br/README.md) | [Portugalski (Portugalia)](../pt/README.md) | [Pendżabski (Gurmukhi)](../pa/README.md) | [Rumuński](../ro/README.md) | [Rosyjski](../ru/README.md) | [Serbski (cyrylica)](../sr/README.md) | [Słowacki](../sk/README.md) | [Słoweński](../sl/README.md) | [Hiszpański](../es/README.md) | [Suahili](../sw/README.md) | [Szwedzki](../sv/README.md) | [Tagalog (Filipiński)](../tl/README.md) | [Tamilski](../ta/README.md) | [Telugu](../te/README.md) | [Tajski](../th/README.md) | [Turecki](../tr/README.md) | [Ukraiński](../uk/README.md) | [Urdu](../ur/README.md) | [Wietnamski](../vi/README.md)
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## Przegląd

**Co-op Translator** pomaga łatwo lokalizować edukacyjne treści na GitHubie na wiele języków.  
Gdy aktualizujesz pliki Markdown, obrazy lub notatniki, tłumaczenia są automatycznie synchronizowane, dzięki czemu Twoje materiały pozostają dokładne i aktualne dla uczących się na całym świecie.

Przykład organizacji przetłumaczonych treści:

![Przykład](../../translated_images/translation-ex.0c8aa6a7ee0aad2b35cddcc110c719baf0afc640e8c5a45540e6c166b9907d91.pl.png)

## Szybki start

```bash
# Utwórz i aktywuj środowisko wirtualne (zalecane)
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
# Zainstaluj pakiet
pip install co-op-translator
# Przetłumacz
translate -l "ko ja fr" -md
```

Docker:

```bash
# Pobierz publiczny obraz z GHCR
docker pull ghcr.io/azure/co-op-translator:latest
# Uruchom z zamontowanym bieżącym folderem i dostarczonym plikiem .env (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko ja fr" -md
```

## Minimalna konfiguracja

1. Utwórz plik `.env` korzystając z szablonu: [.env.template](../../.env.template)  
2. Skonfiguruj jednego dostawcę LLM (Azure OpenAI lub OpenAI)  
3. (Opcjonalnie) Dla tłumaczenia obrazów (`-img`) skonfiguruj Azure AI Vision  
4. (Zalecane) Wyczyść poprzednie tłumaczenia, aby uniknąć konfliktów (np. `translations/`)  
5. (Zalecane) Dodaj sekcję tłumaczeń do swojego README korzystając z [szablonu języków README](./getting_started/README_languages_template.md)  
6. Zobacz: [Konfiguracja Azure AI](./getting_started/set-up-azure-ai.md)  

## Użycie

Tłumacz wszystkie obsługiwane typy:

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

Więcej opcji: [Referencja poleceń](./getting_started/command-reference.md)

## Funkcje

- Automatyczne tłumaczenie Markdown, notatników i obrazów  
- Synchronizacja tłumaczeń z oryginalnymi zmianami  
- Działa lokalnie (CLI) lub w CI (GitHub Actions)  
- Wykorzystuje Azure OpenAI lub OpenAI; opcjonalnie Azure AI Vision dla obrazów  
- Zachowuje formatowanie i strukturę Markdown  

## Dokumentacja

- [Przewodnik po linii poleceń](./getting_started/command-line-guide/command-line-guide.md)  
- [Przewodnik GitHub Actions (repozytoria publiczne i standardowe sekrety)](./getting_started/github-actions-guide/github-actions-guide-public.md)  
- [Przewodnik GitHub Actions (repozytoria organizacji Microsoft i konfiguracje na poziomie organizacji)](./getting_started/github-actions-guide/github-actions-guide-org.md)  
- [Szablon języków README](./getting_started/README_languages_template.md)  
- [Obsługiwane języki](./getting_started/supported-languages.md)  
- [Wkład w projekt](./CONTRIBUTING.md)  
- [Rozwiązywanie problemów](./getting_started/troubleshooting.md)  

### Przewodnik specyficzny dla Microsoft  
> [!NOTE]  
> Tylko dla opiekunów repozytoriów Microsoft „Dla początkujących”.

- [Aktualizacja listy „innych kursów” (tylko dla repozytoriów MS Beginners)](./getting_started/update-other-courses.md)

## Wspieraj nas i wspieraj globalną edukację

Dołącz do nas w rewolucjonizowaniu sposobu, w jaki treści edukacyjne są udostępniane na całym świecie!  
Daj [Co-op Translator](https://github.com/azure/co-op-translator) ⭐ na GitHubie i wspieraj naszą misję przełamywania barier językowych w nauce i technologii. Twoje zainteresowanie i wkład mają ogromne znaczenie! Zachęcamy do zgłaszania kodu i propozycji funkcji.

### Odkrywaj edukacyjne treści Microsoft w swoim języku

- [AZD dla początkujących](https://github.com/microsoft/AZD-for-beginners)  
- [Edge AI dla początkujących](https://github.com/microsoft/edgeai-for-beginners)  
- [Model Context Protocol (MCP) dla początkujących](https://github.com/microsoft/mcp-for-beginners)  
- [AI Agents dla początkujących](https://github.com/microsoft/ai-agents-for-beginners)  
- [Generative AI dla początkujących z użyciem .NET](https://github.com/microsoft/Generative-AI-for-beginners-dotnet)  
- [Generative AI dla początkujących](https://github.com/microsoft/generative-ai-for-beginners)  
- [Generative AI dla początkujących z użyciem Java](https://github.com/microsoft/generative-ai-for-beginners-java)  
- [ML dla początkujących](https://aka.ms/ml-beginners)  
- [Data Science dla początkujących](https://aka.ms/datascience-beginners)  
- [AI dla początkujących](https://aka.ms/ai-beginners)  
- [Cyberbezpieczeństwo dla początkujących](https://github.com/microsoft/Security-101)  
- [Web Dev dla początkujących](https://aka.ms/webdev-beginners)  
- [IoT dla początkujących](https://aka.ms/iot-beginners)  
- [PhiCookBook](https://github.com/microsoft/PhiCookBook)  

## Prezentacje wideo

👉 Kliknij obraz poniżej, aby obejrzeć na YouTube.

- **Open at Microsoft**: Krótkie, 18-minutowe wprowadzenie i szybki przewodnik, jak korzystać z Co-op Translator.

  [![Open at Microsoft](../../translated_images/open-ms-thumbnail.946b356b89bc5f0e33dcebb852f7926b98c33f54c1a49ce01c36ae7f35e2443a.pl.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## Wkład w projekt

Projekt zaprasza do współpracy i sugestii. Chcesz pomóc w rozwoju Azure Co-op Translator? Zapoznaj się z naszym [CONTRIBUTING.md](./CONTRIBUTING.md), aby dowiedzieć się, jak możesz pomóc uczynić Co-op Translator bardziej dostępnym.

## Współtwórcy

[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## Kodeks postępowania

Projekt przyjął [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).  
Więcej informacji znajdziesz w [FAQ dotyczących Kodeksu postępowania](https://opensource.microsoft.com/codeofconduct/faq/) lub  
skontaktuj się pod adresem [opencode@microsoft.com](mailto:opencode@microsoft.com) w razie dodatkowych pytań lub uwag.

## Odpowiedzialna sztuczna inteligencja

Microsoft zobowiązuje się pomagać klientom w odpowiedzialnym korzystaniu z naszych produktów AI, dzielić się naszymi doświadczeniami oraz budować zaufanie poprzez narzędzia takie jak Transparency Notes i Impact Assessments. Wiele z tych zasobów znajdziesz pod adresem [https://aka.ms/RAI](https://aka.ms/RAI).  
Podejście Microsoft do odpowiedzialnej AI opiera się na naszych zasadach AI: uczciwość, niezawodność i bezpieczeństwo, prywatność i ochrona, inkluzywność, przejrzystość oraz odpowiedzialność.

Modele językowe, obrazowe i mowy na dużą skalę – takie jak te używane w tym przykładzie – mogą potencjalnie zachowywać się w sposób nieuczciwy, zawodny lub obraźliwy, co może powodować szkody. Prosimy zapoznać się z [Transparency note usługi Azure OpenAI](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text), aby być świadomym ryzyk i ograniczeń.
Zalecanym podejściem do ograniczania tych ryzyk jest włączenie do architektury systemu bezpieczeństwa, który potrafi wykrywać i zapobiegać szkodliwym zachowaniom. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) zapewnia niezależną warstwę ochrony, zdolną do wykrywania szkodliwych treści generowanych przez użytkowników i AI w aplikacjach i usługach. Azure AI Content Safety obejmuje API do analizy tekstu i obrazów, które pozwalają wykrywać materiały szkodliwe. Mamy również interaktywne Content Safety Studio, które umożliwia przeglądanie, eksplorowanie i wypróbowywanie przykładowego kodu do wykrywania szkodliwych treści w różnych modalnościach. Poniższa [dokumentacja szybkiego startu](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) przeprowadzi Cię przez proces wysyłania zapytań do usługi.

Kolejnym aspektem, który warto wziąć pod uwagę, jest ogólna wydajność aplikacji. W przypadku aplikacji multimodalnych i wielomodelowych, wydajność oznacza, że system działa zgodnie z oczekiwaniami Twoimi i użytkowników, w tym nie generuje szkodliwych wyników. Ważne jest, aby ocenić wydajność całej aplikacji, korzystając z [metryk jakości generowania oraz ryzyka i bezpieczeństwa](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in).

Możesz ocenić swoją aplikację AI w środowisku deweloperskim, używając [prompt flow SDK](https://microsoft.github.io/promptflow/index.html). Na podstawie zestawu testowego lub celu, generacje Twojej aplikacji generatywnej AI są ilościowo mierzone za pomocą wbudowanych lub własnych evaluatorów. Aby rozpocząć pracę z prompt flow sdk do oceny systemu, możesz skorzystać z [przewodnika szybkiego startu](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Po wykonaniu oceny możesz [wizualizować wyniki w Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Znaki towarowe

Ten projekt może zawierać znaki towarowe lub logotypy projektów, produktów lub usług. Autoryzowane użycie znaków towarowych lub logotypów Microsoft podlega i musi być zgodne z [Wytycznymi dotyczącymi znaków towarowych i marki Microsoft](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general). Użycie znaków towarowych lub logotypów Microsoft w zmodyfikowanych wersjach tego projektu nie może powodować nieporozumień ani sugerować sponsorowania przez Microsoft. Wszelkie użycie znaków towarowych lub logotypów stron trzecich podlega politykom tych stron trzecich.

## Uzyskanie pomocy

Jeśli utkniesz lub masz pytania dotyczące tworzenia aplikacji AI, dołącz do:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Jeśli masz uwagi dotyczące produktu lub napotkasz błędy podczas tworzenia, odwiedź:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mimo że dokładamy starań, aby tłumaczenie było jak najbardziej precyzyjne, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym powinien być uznawany za źródło autorytatywne. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->