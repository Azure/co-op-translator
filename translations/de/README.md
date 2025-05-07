<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "18318279bb851dc2c709bfc6a26f6e1d",
  "translation_date": "2025-05-07T14:06:21+00:00",
  "source_file": "README.md",
  "language_code": "de"
}
-->
![Logo](../../imgs/logo.png)

# Co-op Translator: Automatisieren Sie mühelos die Übersetzung von Bildungsdokumentationen

_Automatisieren Sie ganz einfach die Übersetzung Ihrer Dokumentation in mehrere Sprachen, um ein globales Publikum zu erreichen._

[![Python package](https://img.shields.io/pypi/v/co-op-translator?color=4BA3FF)](https://pypi.org/project/co-op-translator/)
[![License: MIT](https://img.shields.io/github/license/azure/co-op-translator?color=4BA3FF)](https://github.com/azure/co-op-translator/blob/main/LICENSE)
[![Downloads](https://static.pepy.tech/badge/co-op-translator)](https://pepy.tech/project/co-op-translator)
[![Downloads](https://static.pepy.tech/badge/co-op-translator/month)](https://pepy.tech/project/co-op-translator)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[![GitHub contributors](https://img.shields.io/github/contributors/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/graphs/contributors/)
[![GitHub issues](https://img.shields.io/github/issues/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/issues/)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/pulls/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

### Sprachunterstützung powered by Co-op Translator

[Koreanisch](../ko/README.md) | [Japanisch](../ja/README.md) | [Chinesisch (vereinfacht)](../zh/README.md) | [Chinesisch (traditionell, Taiwan)](../tw/README.md) | [Spanisch](../es/README.md) | [Französisch](../fr/README.md) | [Deutsch](./README.md) | [Portugiesisch (Brasilien)](../br/README.md) | [Hindi](../hi/README.md) | [Russisch](../ru/README.md) | [Türkisch](../tr/README.md) | [Arabisch](../ar/README.md) | [Indonesisch](../id/README.md) | [Vietnamesisch](../vi/README.md)

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Azure AI Community Discord](https://dcbadge.vercel.app/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)
[![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=VS%20Code%20Dev%20Containers&message=Open&color=007ACC&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator)

> [!TIP]
> **Leistungsstarke Automatisierung**: Jetzt mit Unterstützung für GitHub Actions! Übersetzen Sie Ihre Dokumentation automatisch, sobald Änderungen in Ihrem Repository vorgenommen werden, und halten Sie alles mühelos auf dem neuesten Stand. [Mehr erfahren](../..).

## Unterstützte Modelle und Dienste

| Typ                   | Name                           |
|-----------------------|--------------------------------|
| Language Model        | ![Azure OpenAI](https://img.shields.io/badge/Azure_OpenAI-blue?style=flat-square) ![OpenAI](https://img.shields.io/badge/OpenAI-green?style=flat-square&logo=openai) |
| Computer Vision       | ![Azure Computer Vision](https://img.shields.io/badge/Azure_Computer_Vision-blue?style=flat-square) |

> [!NOTE]
> Wenn ein Computer-Vision-Dienst nicht verfügbar ist, wechselt der co-op translator in den [Markdown-Only-Modus](./getting_started/markdown-only-mode.md).

## Überblick: Optimieren Sie die Übersetzung Ihrer Bildungsinhalte

Sprachbarrieren erschweren den Zugang zu wertvollen Bildungsressourcen und technischem Wissen für Lernende und Entwickler weltweit erheblich. Das schränkt die Teilnahme ein und verlangsamt den globalen Innovations- und Lernprozess.

**Co-op Translator** entstand aus dem Bedarf, den ineffizienten manuellen Übersetzungsprozess für Microsofts eigene umfangreiche Bildungsreihe (wie die "For Beginners"-Anleitungen) zu verbessern. Daraus entwickelte sich ein benutzerfreundliches, leistungsstarkes Tool, das diese Barrieren für alle abbaut. Durch hochwertige automatisierte Übersetzungen per CLI und GitHub Actions ermöglicht Co-op Translator Lehrkräften, Studierenden, Forschern und Entwicklern weltweit den Austausch und Zugriff auf Wissen ohne Sprachhürden.

So organisiert Co-op Translator übersetzte Bildungsinhalte:

![Example](../../imgs/translation-ex.png)

Markdown-Dateien und Bildtexte werden automatisch übersetzt und übersichtlich in sprachspezifischen Ordnern abgelegt.

**Ermöglichen Sie noch heute globalen Zugang zu Ihren Bildungsinhalten mit Co-op Translator!**

## Unterstützung des globalen Zugangs zu Microsofts Lernressourcen

Co-op Translator hilft, die Sprachbarriere bei wichtigen Microsoft-Bildungsinitiativen zu überbrücken, indem er den Übersetzungsprozess für Repositories automatisiert, die eine globale Entwickler-Community bedienen. Beispiele für Projekte, die derzeit Co-op Translator nutzen:

[![ML-For-Beginners](https://github-readme-stats.vercel.app/api/pin/?username=microsoft&repo=ML-For-Beginners&bg_color=ffffff&title_color=0078D4&text_color=333333&border_color=c0d8f0&border_radius=10)](https://github.com/microsoft/ML-For-Beginners)
[![Generative-AI-for-beginners-dotnet](https://github-readme-stats.vercel.app/api/pin/?username=microsoft&repo=Generative-AI-for-beginners-dotnet&bg_color=ffffff&title_color=0078D4&text_color=333333&border_color=c0d8f0&border_radius=10)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet)
[![AI-For-Beginners](https://github-readme-stats.vercel.app/api/pin/?username=microsoft&repo=AI-For-Beginners&bg_color=ffffff&title_color=0078D4&text_color=333333&border_color=c0d8f0&border_radius=10)](https://github.com/microsoft/AI-For-Beginners)
[![ai-agents-for-beginners](https://github-readme-stats.vercel.app/api/pin/?username=microsoft&repo=ai-agents-for-beginners&bg_color=ffffff&title_color=0078D4&text_color=333333&border_color=c0d8f0&border_radius=10)](https://github.com/microsoft/ai-agents-for-beginners)
[![PhiCookBook](https://github-readme-stats.vercel.app/api/pin/?username=microsoft&repo=PhiCookBook&bg_color=ffffff&title_color=0078D4&text_color=333333&border_color=c0d8f0&border_radius=10)](https://github.com/microsoft/PhiCookBook)

## Hauptfunktionen

- **Automatisierte Übersetzungen**: Texte mühelos in mehrere Sprachen übersetzen.
- **GitHub Actions Integration**: Übersetzungen als Teil Ihrer CI/CD-Pipeline automatisieren.
- **Markdown-Erhaltung**: Korrekte Markdown-Syntax während der Übersetzung beibehalten.
- **Bildtextübersetzung**: Text in Bildern extrahieren und übersetzen.
- **Fortschrittliche LLM-Technologie**: Modernste Sprachmodelle für hochwertige Übersetzungen nutzen.
- **Einfache Integration**: Nahtlose Einbindung in Ihre bestehende Projektstruktur.
- **Lokalisierung vereinfachen**: Den Prozess der Internationalisierung Ihres Projekts optimieren.

## Funktionsweise

![Architecture](../../imgs/architecture_241019.png)

Co-op Translator nimmt Markdown-Dateien und Bilder aus Ihrem Projektordner und verarbeitet sie folgendermaßen:

1. **Textextraktion**: Extrahiert Text aus Markdown-Dateien und, falls konfiguriert (z. B. mit Azure Computer Vision), auch aus Bildern.
1. **KI-Übersetzung**: Sendet den extrahierten Text an das konfigurierte LLM (Azure OpenAI, OpenAI usw.) zur Übersetzung.
1. **Speicherung der Ergebnisse**: Speichert die übersetzten Markdown-Dateien und Bilder (mit übersetztem Text) in sprachspezifischen Ordnern und bewahrt dabei das ursprüngliche Format.

## Erste Schritte

> [!NOTE]
> Während dieses Tutorial sich auf Azure-Ressourcen konzentriert, können Sie jedes unterstützte Sprachmodell aus der Liste der [supported models and services](../..) verwenden.

Starten Sie schnell mit der CLI oder richten Sie eine vollständige Automatisierung mit GitHub Actions ein.

### Erste Einrichtung

- [Azure AI einrichten](./getting_started/set-up-azure-ai.md)

### Schnellstart: Kommandozeile

Für einen schnellen Einstieg über die Kommandozeile:

1. Paket installieren:
    ```bash
    pip install co-op-translator
    ```
2. Anmeldedaten konfigurieren:
  - Erstellen Sie eine `.env` file in your project's root directory.
  - Copy the contents from the [.env.template](../../.env.template) file into your new `.env` file.
  - Fill in the required API keys and endpoint information in your `.env` file.
3. Run Translation:
  - Navigate to your project's root directory in your terminal.
  - Execute the translate command, specifying target languages with the `-l`-Datei:
    ```bash
    translate -l "ko ja fr"
    ```
    *(Ersetzen Sie `"ko ja fr"` with your desired space-separated language codes)*

### Detailed Usage Guides

Choose the approach that best fits your workflow:

#### 1. Using the Command Line (CLI)

- Best for: One-time translations, manual control, or integration into custom scripts.
- Requires: Local installation of Python and the `co-op-translator` package.
- Guide: [Command Line Guide](./getting_started/command-line-guide/command-line-guide.md)

#### 2. Using GitHub Actions (Automation)

- Best for: Automatically translating content whenever changes are pushed to your repository. Keeps translations consistently up-to-date.
- Requires: Setting up a workflow file (`.github/workflows`) in Ihrem Repository. Keine lokale Installation erforderlich.
- Anleitungen:
  - [GitHub Actions Guide (öffentliche Repositories & Standard-Secrets)](./getting_started/github-actions-guide/github-actions-guide-public.md) - Für die meisten öffentlichen oder persönlichen Repositories, die auf Standard-Repository-Geheimnisse angewiesen sind.
  - [GitHub Actions Guide (Microsoft Organization Repos & Organisationsebene)](./getting_started/github-actions-guide/github-actions-guide-org.md) - Für die Arbeit innerhalb der Microsoft GitHub-Organisation oder wenn organisationseigene Secrets oder Runner genutzt werden sollen.

### Fehlerbehebung und Tipps

- [Fehlerbehebungsanleitung](./getting_started/troubleshooting.md)

### Weitere Ressourcen

- [Befehlsreferenz](./getting_started/command-reference.md): Ausführliche Anleitung zu allen verfügbaren Befehlen und Optionen.
- [Mehrsprachige Unterstützung einrichten](./getting_started/multi-language-support.md): So fügen Sie eine Tabelle mit Links zu den übersetzten Versionen in Ihrer README hinzu.
- [Unterstützte Sprachen](./getting_started/supported-languages.md): Liste der unterstützten Sprachen und Anleitungen zum Hinzufügen neuer Sprachen.
- [Markdown-Only-Modus](./getting_started/markdown-only-mode.md): Wie Sie nur Text übersetzen, ohne Bildübersetzung.

## Video-Präsentationen

Erfahren Sie mehr über Co-op Translator in unseren Präsentationen _(Klicken Sie auf das Bild unten, um das Video auf YouTube anzusehen.)_:

- **Open at Microsoft**: Eine kurze 18-minütige Einführung und Schnellstart-Anleitung zur Nutzung von Co-op Translator.

  [![Open at Microsoft](../../imgs/open-ms-thumbnail.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

- **Microsoft Reactor**: Eine einstündige, detaillierte Schritt-für-Schritt-Anleitung, die alles abdeckt – von der Erklärung, was Co-op Translator ist, über die Einrichtung und effektive Nutzung bis hin zu einer Live-Demo, die die Funktionen in Aktion zeigt.

  [![Microsoft Reactor](../../imgs/reactor-thumbnail.jpg)](https://www.youtube.com/watch?v=boTtKVPBLAc)

## Unterstützen Sie uns und fördern Sie globales Lernen

Seien Sie Teil der Revolution, wie Bildungsinhalte weltweit geteilt werden! Geben Sie [Co-op Translator](https://github.com/azure/co-op-translator) einen ⭐ auf GitHub und unterstützen Sie unsere Mission, Sprachbarrieren im Lernen und in der Technologie abzubauen. Ihr Interesse und Ihre Beiträge bewirken viel! Code-Beiträge und Feature-Vorschläge sind jederzeit willkommen.

## Mitwirken

Dieses Projekt freut sich über Beiträge und Vorschläge. Möchten Sie Azure Co-op Translator unterstützen? Bitte lesen Sie unsere [CONTRIBUTING.md](./CONTRIBUTING.md) für Richtlinien, wie Sie helfen können, Co-op Translator zugänglicher zu machen.

## Mitwirkende

[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## Verhaltenskodex

Dieses Projekt hat den [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/) übernommen.
Weitere Informationen finden Sie in den [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) oder kontaktieren Sie [opencode@microsoft.com](mailto:opencode@microsoft.com) bei weiteren Fragen oder Anmerkungen.

## Verantwortungsvolle KI

Microsoft verpflichtet sich, Kunden bei der verantwortungsvollen Nutzung unserer KI-Produkte zu unterstützen, unsere Erkenntnisse zu teilen und vertrauensbasierte Partnerschaften durch Tools wie Transparency Notes und Impact Assessments aufzubauen. Viele dieser Ressourcen finden Sie unter [https://aka.ms/RAI](https://aka.ms/RAI).
Der Ansatz von Microsoft für verantwortungsvolle KI basiert auf unseren KI-Prinzipien zu Fairness, Zuverlässigkeit und Sicherheit, Datenschutz und Sicherheit, Inklusivität, Transparenz und Verantwortlichkeit.
Groß angelegte Modelle für natürliche Sprache, Bilder und Sprache – wie die in diesem Beispiel verwendeten – können sich potenziell unfair, unzuverlässig oder anstößig verhalten und dadurch Schäden verursachen. Bitte konsultieren Sie die [Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text), um über Risiken und Einschränkungen informiert zu sein.

Der empfohlene Ansatz zur Minderung dieser Risiken besteht darin, ein Sicherheitssystem in Ihre Architektur zu integrieren, das schädliches Verhalten erkennen und verhindern kann. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) bietet eine unabhängige Schutzschicht, die in der Lage ist, schädliche nutzergenerierte und KI-generierte Inhalte in Anwendungen und Diensten zu erkennen. Azure AI Content Safety umfasst Text- und Bild-APIs, mit denen Sie schädliches Material identifizieren können. Außerdem steht ein interaktives Content Safety Studio zur Verfügung, mit dem Sie Beispielcode zur Erkennung schädlicher Inhalte in verschiedenen Modalitäten ansehen, erkunden und ausprobieren können. Die folgende [Quickstart-Dokumentation](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) führt Sie durch das Stellen von Anfragen an den Dienst.

Ein weiterer Aspekt, der berücksichtigt werden sollte, ist die Gesamtleistung der Anwendung. Bei multimodalen und multimodellbasierten Anwendungen verstehen wir unter Leistung, dass das System so funktioniert, wie Sie und Ihre Nutzer es erwarten, einschließlich der Vermeidung schädlicher Ausgaben. Es ist wichtig, die Leistung Ihrer gesamten Anwendung anhand von [Qualitäts- sowie Risiko- und Sicherheitsmetriken für die Generierung](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in) zu bewerten.

Sie können Ihre KI-Anwendung in Ihrer Entwicklungsumgebung mit dem [prompt flow SDK](https://microsoft.github.io/promptflow/index.html) evaluieren. Anhand eines Testdatensatzes oder eines Ziels werden die Generierungen Ihrer generativen KI-Anwendung quantitativ mit integrierten oder benutzerdefinierten Evaluatoren Ihrer Wahl gemessen. Um mit dem prompt flow sdk zur Bewertung Ihres Systems zu beginnen, können Sie der [Quickstart-Anleitung](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk) folgen. Nach der Ausführung eines Evaluierungslaufs können Sie die Ergebnisse [im Azure AI Studio visualisieren](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Trademarks

Dieses Projekt kann Marken oder Logos von Projekten, Produkten oder Diensten enthalten. Die autorisierte Nutzung von Microsoft-Marken oder -Logos unterliegt den [Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general) und muss diesen entsprechen. Die Verwendung von Microsoft-Marken oder -Logos in modifizierten Versionen dieses Projekts darf nicht zu Verwechslungen führen oder eine Microsoft-Unterstützung suggerieren. Die Nutzung von Marken oder Logos Dritter unterliegt den jeweiligen Richtlinien dieser Dritten.

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache gilt als maßgebliche Quelle. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.