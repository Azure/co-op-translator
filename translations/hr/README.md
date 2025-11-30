<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "dac6bc281667816537df51f724a0ff2c",
  "translation_date": "2025-11-30T12:31:15+00:00",
  "source_file": "README.md",
  "language_code": "hr"
}
-->
# Co-op Translator

_Lako automatizirajte prijevod vašeg edukativnog GitHub sadržaja na više jezika kako biste dosegli globalnu publiku._

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

### 🌐 Podrška za više jezika

#### Podržano od strane [Co-op Translator](https://github.com/Azure/Co-op-Translator)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arapski](../ar/README.md) | [Bengalski](../bn/README.md) | [Bugarski](../bg/README.md) | [Burmanski (Myanmar)](../my/README.md) | [Kineski (pojednostavljeni)](../zh/README.md) | [Kineski (tradicionalni, Hong Kong)](../hk/README.md) | [Kineski (tradicionalni, Makao)](../mo/README.md) | [Kineski (tradicionalni, Tajvan)](../tw/README.md) | [Hrvatski](./README.md) | [Češki](../cs/README.md) | [Danski](../da/README.md) | [Nizozemski](../nl/README.md) | [Estonski](../et/README.md) | [Finski](../fi/README.md) | [Francuski](../fr/README.md) | [Njemački](../de/README.md) | [Grčki](../el/README.md) | [Hebrejski](../he/README.md) | [Hindi](../hi/README.md) | [Mađarski](../hu/README.md) | [Indonezijski](../id/README.md) | [Talijanski](../it/README.md) | [Japanski](../ja/README.md) | [Kannada](../kn/README.md) | [Korejski](../ko/README.md) | [Litvanski](../lt/README.md) | [Malajski](../ms/README.md) | [Malajalamski](../ml/README.md) | [Marathi](../mr/README.md) | [Nepalski](../ne/README.md) | [Nigerijski pidžin](../pcm/README.md) | [Norveški](../no/README.md) | [Perzijski (Farsi)](../fa/README.md) | [Poljski](../pl/README.md) | [Portugalski (Brazil)](../br/README.md) | [Portugalski (Portugal)](../pt/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Rumunjski](../ro/README.md) | [Ruski](../ru/README.md) | [Srpski (ćirilica)](../sr/README.md) | [Slovački](../sk/README.md) | [Slovenski](../sl/README.md) | [Španjolski](../es/README.md) | [Svahili](../sw/README.md) | [Švedski](../sv/README.md) | [Tagalog (Filipinski)](../tl/README.md) | [Tamilski](../ta/README.md) | [Telugu](../te/README.md) | [Tajlandski](../th/README.md) | [Turski](../tr/README.md) | [Ukrajinski](../uk/README.md) | [Urdu](../ur/README.md) | [Vijetnamski](../vi/README.md)
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## Pregled

**Co-op Translator** vam pomaže da lako lokalizirate vaš edukativni GitHub sadržaj na više jezika.
Kad ažurirate svoje Markdown datoteke, slike ili bilježnice, prijevodi se automatski sinkroniziraju, osiguravajući da vaš sadržaj ostane točan i ažuran za učenike širom svijeta.

Primjer kako je prevedeni sadržaj organiziran:

![Example](../../translated_images/translation-ex.0c8aa6a7ee0aad2b35cddcc110c719baf0afc640e8c5a45540e6c166b9907d91.hr.png)

## Brzi početak

```bash
# Kreirajte i aktivirajte virtualno okruženje (preporučeno)
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
# Instalirajte paket
pip install co-op-translator
# Prevedi
translate -l "ko ja fr" -md
```

Docker:

```bash
# Povucite javnu sliku s GHCR-a
docker pull ghcr.io/azure/co-op-translator:latest
# Pokrenite s montiranom trenutnom mapom i pruženom .env datotekom (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko ja fr" -md
```

## Minimalna postavka

1. Kreirajte `.env` datoteku koristeći predložak: [.env.template](../../.env.template)
2. Konfigurirajte jednog LLM pružatelja (Azure OpenAI ili OpenAI)
3. (Opcionalno) Za prijevod slika (`-img`), konfigurirajte Azure AI Vision
4. (Preporučeno) Očistite prethodne prijevode kako biste izbjegli sukobe (npr. `translations/`)
5. (Preporučeno) Dodajte odjeljak za prijevod u vaš README koristeći [README predložak za jezike](./getting_started/README_languages_template.md)
6. Pogledajte: [Postavljanje Azure AI](./getting_started/set-up-azure-ai.md)

## Korištenje

Prevedite sve podržane tipove:

```bash
translate -l "ko ja"
```

Samo Markdown:

```bash
translate -l "de" -md
```

Markdown + slike:

```bash
translate -l "pt" -md -img
```

Samo bilježnice:

```bash
translate -l "zh" -nb
```

Više opcija: [Referenca naredbi](./getting_started/command-reference.md)

## Značajke

- Automatski prijevod za Markdown, bilježnice i slike
- Održava prijevode sinkroniziranima sa izvorom
- Radi lokalno (CLI) ili u CI (GitHub Actions)
- Koristi Azure OpenAI ili OpenAI; opcionalno Azure AI Vision za slike
- Čuva formatiranje i strukturu Markdowna

## Dokumentacija

- [Vodič za naredbeni redak](./getting_started/command-line-guide/command-line-guide.md)
- [Vodič za GitHub Actions (javni repozitoriji i standardni tajni ključevi)](./getting_started/github-actions-guide/github-actions-guide-public.md)
- [Vodič za GitHub Actions (Microsoft organizacijski repozitoriji i postavke na razini organizacije)](./getting_started/github-actions-guide/github-actions-guide-org.md)
- [README predložak za jezike](./getting_started/README_languages_template.md)
- [Podržani jezici](./getting_started/supported-languages.md)
- [Doprinosi](./CONTRIBUTING.md)
- [Rješavanje problema](./getting_started/troubleshooting.md)

### Microsoft-specifični vodič
> [!NOTE]
> Samo za održavatelje Microsoft “For Beginners” repozitorija.

- [Ažuriranje popisa “ostalih tečajeva” (samo za MS Beginners repozitorije)](./getting_started/update-other-courses.md)

## Podržite nas i potaknite globalno učenje

Pridružite nam se u revoluciji dijeljenja edukativnog sadržaja širom svijeta! Dajte [Co-op Translator](https://github.com/azure/co-op-translator) ⭐ na GitHubu i podržite našu misiju uklanjanja jezičnih barijera u učenju i tehnologiji. Vaš interes i doprinosi imaju veliki utjecaj! Kodni doprinosi i prijedlozi za nove značajke su uvijek dobrodošli.

### Istražite Microsoft edukativni sadržaj na svom jeziku

- [AZD za početnike](https://github.com/microsoft/AZD-for-beginners)
- [Edge AI za početnike](https://github.com/microsoft/edgeai-for-beginners)
- [Model Context Protocol (MCP) za početnike](https://github.com/microsoft/mcp-for-beginners)
- [AI agenti za početnike](https://github.com/microsoft/ai-agents-for-beginners)
- [Generativna AI za početnike koristeći .NET](https://github.com/microsoft/Generative-AI-for-beginners-dotnet)
- [Generativna AI za početnike](https://github.com/microsoft/generative-ai-for-beginners)
- [Generativna AI za početnike koristeći Java](https://github.com/microsoft/generative-ai-for-beginners-java)
- [ML za početnike](https://aka.ms/ml-beginners)
- [Data Science za početnike](https://aka.ms/datascience-beginners)
- [AI za početnike](https://aka.ms/ai-beginners)
- [Cybersecurity za početnike](https://github.com/microsoft/Security-101)
- [Web razvoj za početnike](https://aka.ms/webdev-beginners)
- [IoT za početnike](https://aka.ms/iot-beginners)
- [PhiCookBook](https://github.com/microsoft/PhiCookBook)

## Video prezentacije

👉 Kliknite na sliku ispod za gledanje na YouTubeu.

- **Open at Microsoft**: Kratki 18-minutni uvod i brzi vodič kako koristiti Co-op Translator.

  [![Open at Microsoft](../../translated_images/open-ms-thumbnail.946b356b89bc5f0e33dcebb852f7926b98c33f54c1a49ce01c36ae7f35e2443a.hr.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## Doprinosi

Ovaj projekt poziva na doprinose i prijedloge. Zainteresirani ste za doprinos Azure Co-op Translatoru? Molimo pogledajte naš [CONTRIBUTING.md](./CONTRIBUTING.md) za smjernice kako možete pomoći da Co-op Translator postane pristupačniji.

## Suradnici

[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## Kodeks ponašanja

Ovaj projekt je usvojio [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
Za više informacija pogledajte [Često postavljana pitanja o kodeksu ponašanja](https://opensource.microsoft.com/codeofconduct/faq/) ili
kontaktirajte [opencode@microsoft.com](mailto:opencode@microsoft.com) za dodatna pitanja ili komentare.

## Odgovorni AI

Microsoft je predan pomoći našim korisnicima da odgovorno koriste naše AI proizvode, dijeleći svoja iskustva i gradeći partnerstva temeljena na povjerenju kroz alate poput Transparency Notes i Impact Assessments. Mnogi od ovih resursa dostupni su na [https://aka.ms/RAI](https://aka.ms/RAI).
Microsoftov pristup odgovornom AI temelji se na našim AI principima: pravičnost, pouzdanost i sigurnost, privatnost i sigurnost, uključivost, transparentnost i odgovornost.

Veliki modeli za prirodni jezik, slike i govor - poput onih korištenih u ovom primjeru - mogu se potencijalno ponašati na načine koji nisu pravični, pouzdani ili mogu biti uvredljivi, što može uzrokovati štetu. Molimo konzultirajte [Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) kako biste bili informirani o rizicima i ograničenjima.
Preporučeni pristup za ublažavanje ovih rizika je uključivanje sigurnosnog sustava u vašu arhitekturu koji može otkriti i spriječiti štetno ponašanje. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) pruža neovisni sloj zaštite, sposoban otkriti štetni sadržaj koji generiraju korisnici i AI u aplikacijama i uslugama. Azure AI Content Safety uključuje tekstualne i slikovne API-je koji vam omogućuju otkrivanje štetnog materijala. Također imamo interaktivni Content Safety Studio koji vam omogućuje pregled, istraživanje i isprobavanje primjera koda za otkrivanje štetnog sadržaja u različitim modalitetima. Sljedeća [dokumentacija za brzi početak](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) vodi vas kroz slanje zahtjeva prema usluzi.

Još jedan aspekt koji treba uzeti u obzir je ukupna izvedba aplikacije. Kod višemodalnih i višemodelskih aplikacija, izvedba znači da sustav radi onako kako vi i vaši korisnici očekujete, uključujući i to da ne generira štetne rezultate. Važno je procijeniti izvedbu vaše cjelokupne aplikacije koristeći [metrike kvalitete generiranja te rizika i sigurnosti](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in).

Svoju AI aplikaciju možete evaluirati u razvojnom okruženju koristeći [prompt flow SDK](https://microsoft.github.io/promptflow/index.html). Bilo da imate testni skup podataka ili cilj, generacije vaše generativne AI aplikacije kvantitativno se mjere ugrađenim evaluatorima ili prilagođenim evaluatorima po vašem izboru. Za početak rada s prompt flow SDK-om za evaluaciju vašeg sustava, možete slijediti [vodič za brzi početak](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Nakon što izvršite evaluacijsko pokretanje, možete [vizualizirati rezultate u Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Zaštićeni znakovi

Ovaj projekt može sadržavati zaštićene znakove ili logotipe projekata, proizvoda ili usluga. Ovlaštena upotreba Microsoftovih
zaštićenih znakova ili logotipa podliježe i mora slijediti
[Microsoftove smjernice za zaštitne znakove i brend](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
Upotreba Microsoftovih zaštićenih znakova ili logotipa u izmijenjenim verzijama ovog projekta ne smije izazvati zabunu niti implicirati sponzorstvo Microsofta.
Svaka upotreba zaštićenih znakova ili logotipa trećih strana podliježe pravilima tih trećih strana.

## Dobivanje pomoći

Ako zapnete ili imate pitanja o izradi AI aplikacija, pridružite se:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Ako imate povratne informacije o proizvodu ili prijavite greške tijekom izrade, posjetite:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Odricanje od odgovornosti**:
Ovaj dokument preveden je pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo postići točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakva nesporazuma ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->