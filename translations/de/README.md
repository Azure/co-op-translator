<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "dac6bc281667816537df51f724a0ff2c",
  "translation_date": "2025-11-30T09:48:28+00:00",
  "source_file": "README.md",
  "language_code": "de"
}
-->
# Co-op Translator

_Erleichtern Sie die automatische Übersetzung Ihrer Bildungsinhalte auf GitHub in mehrere Sprachen, um ein weltweites Publikum zu erreichen._

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

### 🌐 Mehrsprachige Unterstützung

#### Unterstützt von [Co-op Translator](https://github.com/Azure/Co-op-Translator)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabisch](../ar/README.md) | [Bengalisch](../bn/README.md) | [Bulgarisch](../bg/README.md) | [Birmanisch (Myanmar)](../my/README.md) | [Chinesisch (vereinfacht)](../zh/README.md) | [Chinesisch (traditionell, Hongkong)](../hk/README.md) | [Chinesisch (traditionell, Macau)](../mo/README.md) | [Chinesisch (traditionell, Taiwan)](../tw/README.md) | [Kroatisch](../hr/README.md) | [Tschechisch](../cs/README.md) | [Dänisch](../da/README.md) | [Niederländisch](../nl/README.md) | [Estnisch](../et/README.md) | [Finnisch](../fi/README.md) | [Französisch](../fr/README.md) | [Deutsch](./README.md) | [Griechisch](../el/README.md) | [Hebräisch](../he/README.md) | [Hindi](../hi/README.md) | [Ungarisch](../hu/README.md) | [Indonesisch](../id/README.md) | [Italienisch](../it/README.md) | [Japanisch](../ja/README.md) | [Kannada](../kn/README.md) | [Koreanisch](../ko/README.md) | [Litauisch](../lt/README.md) | [Malaiisch](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepalesisch](../ne/README.md) | [Nigerianisches Pidgin](../pcm/README.md) | [Norwegisch](../no/README.md) | [Persisch (Farsi)](../fa/README.md) | [Polnisch](../pl/README.md) | [Portugiesisch (Brasilien)](../br/README.md) | [Portugiesisch (Portugal)](../pt/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Rumänisch](../ro/README.md) | [Russisch](../ru/README.md) | [Serbisch (Kyrillisch)](../sr/README.md) | [Slowakisch](../sk/README.md) | [Slowenisch](../sl/README.md) | [Spanisch](../es/README.md) | [Suaheli](../sw/README.md) | [Schwedisch](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thailändisch](../th/README.md) | [Türkisch](../tr/README.md) | [Ukrainisch](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamesisch](../vi/README.md)
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## Überblick

**Co-op Translator** hilft Ihnen, Ihre Bildungsinhalte auf GitHub mühelos in mehrere Sprachen zu übersetzen.
Wenn Sie Ihre Markdown-Dateien, Bilder oder Notebooks aktualisieren, bleiben die Übersetzungen automatisch synchronisiert, sodass Ihre Inhalte für Lernende weltweit stets aktuell und korrekt sind.

Beispiel, wie übersetzte Inhalte organisiert sind:

![Beispiel](../../translated_images/translation-ex.0c8aa6a7ee0aad2b35cddcc110c719baf0afc640e8c5a45540e6c166b9907d91.de.png)

## Schnellstart

```bash
# Erstellen und aktivieren Sie eine virtuelle Umgebung (empfohlen)
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
# Installieren Sie das Paket
pip install co-op-translator
# Übersetzen
translate -l "ko ja fr" -md
```

Docker:

```bash
# Ziehen Sie das öffentliche Image von GHCR
docker pull ghcr.io/azure/co-op-translator:latest
# Führen Sie es mit dem aktuellen Ordner als Mount und bereitgestellter .env-Datei aus (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko ja fr" -md
```

## Minimale Einrichtung

1. Erstellen Sie eine `.env`-Datei anhand der Vorlage: [.env.template](../../.env.template)
2. Konfigurieren Sie einen LLM-Anbieter (Azure OpenAI oder OpenAI)
3. (Optional) Für Bildübersetzungen (`-img`) Azure AI Vision einrichten
4. (Empfohlen) Entfernen Sie vorherige Übersetzungen, um Konflikte zu vermeiden (z.B. `translations/`)
5. (Empfohlen) Fügen Sie einen Übersetzungsabschnitt zu Ihrem README mit der [README-Sprachvorlage](./getting_started/README_languages_template.md) hinzu
6. Siehe: [Azure AI einrichten](./getting_started/set-up-azure-ai.md)

## Verwendung

Übersetzen Sie alle unterstützten Typen:

```bash
translate -l "ko ja"
```

Nur Markdown:

```bash
translate -l "de" -md
```

Markdown + Bilder:

```bash
translate -l "pt" -md -img
```

Nur Notebooks:

```bash
translate -l "zh" -nb
```

Weitere Optionen: [Befehlsreferenz](./getting_started/command-reference.md)

## Funktionen

- Automatisierte Übersetzung von Markdown, Notebooks und Bildern
- Hält Übersetzungen synchron mit Quelländerungen
- Funktioniert lokal (CLI) oder in CI (GitHub Actions)
- Nutzt Azure OpenAI oder OpenAI; optional Azure AI Vision für Bilder
- Bewahrt Markdown-Formatierung und Struktur

## Dokumentation

- [Kommandozeilen-Anleitung](./getting_started/command-line-guide/command-line-guide.md)
- [GitHub Actions Anleitung (öffentliche Repositories & Standard-Secrets)](./getting_started/github-actions-guide/github-actions-guide-public.md)
- [GitHub Actions Anleitung (Microsoft Organisations-Repositories & Organisationseinstellungen)](./getting_started/github-actions-guide/github-actions-guide-org.md)
- [README-Sprachvorlage](./getting_started/README_languages_template.md)
- [Unterstützte Sprachen](./getting_started/supported-languages.md)
- [Mitwirken](./CONTRIBUTING.md)
- [Fehlerbehebung](./getting_started/troubleshooting.md)

### Microsoft-spezifische Anleitung
> [!NOTE]
> Nur für Maintainer der Microsoft „For Beginners“-Repositories.

- [Aktualisierung der „anderen Kurse“-Liste (nur für MS Beginners Repositories)](./getting_started/update-other-courses.md)

## Unterstützen Sie uns und fördern Sie globales Lernen

Begleiten Sie uns dabei, die Art und Weise zu revolutionieren, wie Bildungsinhalte weltweit geteilt werden! Geben Sie [Co-op Translator](https://github.com/azure/co-op-translator) einen ⭐ auf GitHub und unterstützen Sie unsere Mission, Sprachbarrieren im Lernen und in der Technologie abzubauen. Ihr Interesse und Ihre Beiträge haben großen Einfluss! Code-Beiträge und Feature-Vorschläge sind jederzeit willkommen.

### Entdecken Sie Microsoft-Bildungsinhalte in Ihrer Sprache

- [AZD für Anfänger](https://github.com/microsoft/AZD-for-beginners)
- [Edge AI für Anfänger](https://github.com/microsoft/edgeai-for-beginners)
- [Model Context Protocol (MCP) für Anfänger](https://github.com/microsoft/mcp-for-beginners)
- [AI Agents für Anfänger](https://github.com/microsoft/ai-agents-for-beginners)
- [Generative AI für Anfänger mit .NET](https://github.com/microsoft/Generative-AI-for-beginners-dotnet)
- [Generative AI für Anfänger](https://github.com/microsoft/generative-ai-for-beginners)
- [Generative AI für Anfänger mit Java](https://github.com/microsoft/generative-ai-for-beginners-java)
- [ML für Anfänger](https://aka.ms/ml-beginners)
- [Data Science für Anfänger](https://aka.ms/datascience-beginners)
- [AI für Anfänger](https://aka.ms/ai-beginners)
- [Cybersecurity für Anfänger](https://github.com/microsoft/Security-101)
- [Webentwicklung für Anfänger](https://aka.ms/webdev-beginners)
- [IoT für Anfänger](https://aka.ms/iot-beginners)
- [PhiCookBook](https://github.com/microsoft/PhiCookBook)

## Video-Präsentationen

👉 Klicken Sie auf das Bild unten, um das Video auf YouTube anzusehen.

- **Open at Microsoft**: Eine kurze 18-minütige Einführung und schnelle Anleitung zur Nutzung von Co-op Translator.

  [![Open at Microsoft](../../translated_images/open-ms-thumbnail.946b356b89bc5f0e33dcebb852f7926b98c33f54c1a49ce01c36ae7f35e2443a.de.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## Mitwirken

Dieses Projekt freut sich über Beiträge und Vorschläge. Möchten Sie zum Azure Co-op Translator beitragen? Bitte lesen Sie unsere [CONTRIBUTING.md](./CONTRIBUTING.md) für Richtlinien, wie Sie Co-op Translator zugänglicher machen können.

## Mitwirkende

[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## Verhaltenskodex

Dieses Projekt hat den [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/) übernommen.
Weitere Informationen finden Sie in den [FAQ zum Verhaltenskodex](https://opensource.microsoft.com/codeofconduct/faq/) oder kontaktieren Sie [opencode@microsoft.com](mailto:opencode@microsoft.com) bei weiteren Fragen oder Anmerkungen.

## Verantwortungsvolle KI

Microsoft verpflichtet sich, unseren Kunden zu helfen, unsere KI-Produkte verantwortungsvoll zu nutzen, unsere Erkenntnisse zu teilen und vertrauensbasierte Partnerschaften durch Werkzeuge wie Transparenznotizen und Wirkungsbewertungen aufzubauen. Viele dieser Ressourcen finden Sie unter [https://aka.ms/RAI](https://aka.ms/RAI).
Der Ansatz von Microsoft für verantwortungsvolle KI basiert auf unseren KI-Prinzipien: Fairness, Zuverlässigkeit und Sicherheit, Datenschutz und Sicherheit, Inklusivität, Transparenz und Verantwortlichkeit.

Groß angelegte Modelle für natürliche Sprache, Bilder und Sprache – wie die in diesem Beispiel verwendeten – können sich potenziell unfair, unzuverlässig oder anstößig verhalten und dadurch Schaden verursachen. Bitte konsultieren Sie die [Transparenznotiz des Azure OpenAI-Dienstes](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text), um über Risiken und Einschränkungen informiert zu sein.
Der empfohlene Ansatz zur Minderung dieser Risiken besteht darin, ein Sicherheitssystem in Ihre Architektur zu integrieren, das schädliches Verhalten erkennen und verhindern kann. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) bietet eine unabhängige Schutzschicht, die in der Lage ist, schädliche nutzergenerierte und KI-generierte Inhalte in Anwendungen und Diensten zu erkennen. Azure AI Content Safety umfasst Text- und Bild-APIs, mit denen Sie schädliches Material erkennen können. Außerdem gibt es ein interaktives Content Safety Studio, mit dem Sie Beispielcode zur Erkennung schädlicher Inhalte in verschiedenen Modalitäten ansehen, erkunden und ausprobieren können. Die folgende [Quickstart-Dokumentation](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) führt Sie durch die Anfragen an den Dienst.

Ein weiterer Aspekt, den Sie berücksichtigen sollten, ist die Gesamtleistung der Anwendung. Bei multimodalen und multimodellbasierten Anwendungen verstehen wir unter Leistung, dass das System so funktioniert, wie Sie und Ihre Nutzer es erwarten, einschließlich der Vermeidung schädlicher Ausgaben. Es ist wichtig, die Leistung Ihrer gesamten Anwendung anhand von [Generierungsqualität sowie Risiko- und Sicherheitsmetriken](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in) zu bewerten.

Sie können Ihre KI-Anwendung in Ihrer Entwicklungsumgebung mit dem [prompt flow SDK](https://microsoft.github.io/promptflow/index.html) evaluieren. Anhand eines Testdatensatzes oder eines Ziels werden die Generierungen Ihrer generativen KI-Anwendung quantitativ mit integrierten oder benutzerdefinierten Evaluatoren gemessen. Um mit dem prompt flow SDK zur Bewertung Ihres Systems zu starten, können Sie der [Quickstart-Anleitung](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk) folgen. Nach der Ausführung eines Evaluierungslaufs können Sie die Ergebnisse [im Azure AI Studio visualisieren](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Marken

Dieses Projekt kann Marken oder Logos von Projekten, Produkten oder Diensten enthalten. Die autorisierte Nutzung von Microsoft-Marken oder -Logos unterliegt den [Microsoft Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general) und muss diesen folgen. Die Verwendung von Microsoft-Marken oder -Logos in modifizierten Versionen dieses Projekts darf keine Verwirrung stiften oder eine Microsoft-Unterstützung suggerieren. Die Nutzung von Marken oder Logos Dritter unterliegt den jeweiligen Richtlinien dieser Dritten.

## Hilfe erhalten

Wenn Sie nicht weiterkommen oder Fragen zum Erstellen von KI-Anwendungen haben, treten Sie bei:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Wenn Sie Produktfeedback geben oder Fehler beim Erstellen melden möchten, besuchen Sie:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache ist als maßgebliche Quelle zu betrachten. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->