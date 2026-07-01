# Co-op Translator

_Eenostavno avtomatizirajte in vzdržujte prevode vaših izobraževalnih GitHub vsebin v več jezikih, ko se vaš projekt razvija._

![Python 3.10–3.12](https://img.shields.io/badge/python-3.10--3.12-blue)
[![Python paket](https://img.shields.io/pypi/v/co-op-translator?color=4BA3FF)](https://pypi.org/project/co-op-translator/)
[![Licenca: MIT](https://img.shields.io/github/license/azure/co-op-translator?color=4BA3FF)](https://github.com/azure/co-op-translator/blob/main/LICENSE)
[![Prenosi](https://static.pepy.tech/badge/co-op-translator)](https://pepy.tech/project/co-op-translator)
[![Prenosi](https://static.pepy.tech/badge/co-op-translator/month)](https://pepy.tech/project/co-op-translator)
[![Kontejner: GHCR](https://img.shields.io/badge/Container-GHCR-2496ED?logo=docker&logoColor=fff)](https://github.com/azure/co-op-translator/pkgs/container/co-op-translator)
[![Slog kode: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[![GitHub prispevalci](https://img.shields.io/github/contributors/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/graphs/contributors/)
[![GitHub težave](https://img.shields.io/github/issues/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/issues/)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/pulls/)
[![PRs Dobrodošli](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

**Začnite tukaj:** [Izberite svoj potek dela](https://azure.github.io/co-op-translator/workflows/) | [Konfiguracija](https://azure.github.io/co-op-translator/configuration/) | [CLI](https://azure.github.io/co-op-translator/cli/) | [Python API](https://azure.github.io/co-op-translator/api/) | [MCP Server](https://azure.github.io/co-op-translator/mcp/)

### 🌐 Večjezična podpora

#### Podprto s strani [Co-op Translator](https://github.com/Azure/co-op-translator)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabščina](../ar/README.md) | [Bengalščina](../bn/README.md) | [Bolgarščina](../bg/README.md) | [Burmanščina (Myanmar)](../my/README.md) | [Kitajščina (poenostavljena)](../zh-CN/README.md) | [Kitajščina (tradicionalna, Hong Kong)](../zh-HK/README.md) | [Kitajščina (tradicionalna, Macau)](../zh-MO/README.md) | [Kitajščina (tradicionalna, Taiwan)](../zh-TW/README.md) | [Hrvaščina](../hr/README.md) | [Češčina](../cs/README.md) | [Danščina](../da/README.md) | [Nizozemščina](../nl/README.md) | [Estonščina](../et/README.md) | [Finščina](../fi/README.md) | [Francoščina](../fr/README.md) | [Nemščina](../de/README.md) | [Grščina](../el/README.md) | [Hebrejščina](../he/README.md) | [Hindijščina](../hi/README.md) | [Madžarščina](../hu/README.md) | [Indonezijščina](../id/README.md) | [Italijanščina](../it/README.md) | [Japonščina](../ja/README.md) | [Kannada](../kn/README.md) | [Kmerski (Khmer)](../km/README.md) | [Korejščina](../ko/README.md) | [Litovščina](../lt/README.md) | [Malajščina](../ms/README.md) | [Malajalščina](../ml/README.md) | [Maratščina](../mr/README.md) | [Nepalščina](../ne/README.md) | [Nigerijski pidžin](../pcm/README.md) | [Norveščina](../no/README.md) | [Perzijski (Farsi)](../fa/README.md) | [Poljščina](../pl/README.md) | [Portugalščina (Brazilija)](../pt-BR/README.md) | [Portugalščina (Portugalska)](../pt-PT/README.md) | [Pandžabščina (Gurmukhi)](../pa/README.md) | [Romunščina](../ro/README.md) | [Ruščina](../ru/README.md) | [Srbščina (cirilica)](../sr/README.md) | [Slovaščina](../sk/README.md) | [Slovenščina](./README.md) | [Španščina](../es/README.md) | [Svahili](../sw/README.md) | [Švedščina](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamilščina](../ta/README.md) | [Telugu](../te/README.md) | [Tajščina](../th/README.md) | [Turščina](../tr/README.md) | [Ukrajinščina](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamščina](../vi/README.md)

> **Raje klonirate lokalno?**
>
> Ta repozitorij vključuje več kot 50 prevodov, kar znatno poveča velikost prenosa. Za kloniranje brez prevodov uporabite sparse checkout:
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
> To vam zagotovi vse, kar potrebujete za dokončanje tečaja z veliko hitrejšim prenosom.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub opazovalci](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forki](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub zvezdice](https://img.shields.io/github/stars/azure/co-op-translator?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Odpri v GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## Pregled

**Co-op Translator** vam pomaga enostavno lokalizirati vaše izobraževalne GitHub vsebine v več jezikov.
Ko posodobite svoje Markdown datoteke, slike ali zvezke, so prevodi samodejno sinhronizirani, s čimer zagotovite, da je vaša vsebina natančna in posodobljena za učeče po vsem svetu.

Uporabite ga iz CLI za prevajanje repozitorijev, iz Python API za avtomatizacijo ali prek MCP strežnika za agentne in urejevalne poteke dela.

Primer, kako je prevedena vsebina organizirana:

![Primer](../../imgs/translation-ex.png)

## Zakaj Co-op Translator?

Prevesti eno datoteko je enostavno. Ohraniti celo dokumentacijsko repozitorij
preveden, povezan in ažuren pa je težava.

| Problem | Kako Co-op Translator pomaga |
| --- | --- |
| Dolgi dokumenti niso en sam poziv | Velike Markdown datoteke so razdeljene na kose, tako da dolg README ne temelji na enem krhkem odgovoru modela. Če kos ne uspe, lahko Co-op Translator poskusi znova in ponovno razdeli samo neuspešni del. |
| Nepopolni prevodi ne bi smeli biti označeni kot ažurni | Skrajšan prevod nikoli ne bi smel biti označen kot posodobljen. Co-op Translator preveri integriteto prevoda pred shranjevanjem in lahko zazna strukturalno nepopolne obstoječe prevode. |
| Povezave naj ustrezajo prevedeni strukturi repozitorija | Ročni prevodi pogosto pustijo relativne povezave, ki kažejo nazaj na izvorno drevo. Co-op Translator prepiše Markdown, zvezek, slikovne in README povezave, da ustrezajo strukturi `translations/<lang>/...`. |
| Prevajanje naj deluje po celotnem repozitoriju | Co-op Translator obravnava README datoteke, dokumentacijo, zvezke in besedilo na slikah kot del enotnega poteka dela repozitorija, namesto da bi prevajal datoteke eno za drugo. |
| Vzdrževanje prevodov je bolj pomembno kot njihovo enkratno ustvarjanje | Viri hash in metapodatki prevodov omogočajo Co-op Translatorju, da najde zastarele datoteke, preskoči nespremenjene datoteke in ohranja prevedeno vsebino sinhronizirano, ko se izvorni repozitorij spreminja. |

## Kako je upravljano stanje prevodov

Co-op Translator upravlja prevedeno vsebino kot **verzionirane programske artefakte**,  
ne kot statične datoteke.

Orodje spremlja stanje prevedenega Markdowna, slik in zvezkov
z uporabo **metapodatkov, specifičnih za jezik**.

Ta zasnova omogoča Co-op Translatorju, da:

- Zanesljivo zazna zastarele prevode
- Obravnava Markdown, slike in zvezke dosledno
- Varnostno širi na velike, hitro spreminjajoče se, večjezične repozitorije

Z modeliranjem prevodov kot upravljanih artefaktov,
se poteki dela za prevajanje naravno uskladijo s sodobnimi
praktikami upravljanja odvisnosti in artefaktov v programski opremi.

→ [Kako je upravljano stanje prevodov](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/rethinking-documentation-translation-treating-translations-as-versioned-software/4491755)

### Sorodni poglobljeni članki

- [Popravljanje pokvarjenega Markdowna pri AI prevodu: Ojačitev produkcijskega cevovoda](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/fixing-broken-markdown-in-ai-translation-hardening-a-production-pipeline/4511378)

## Začnite

Co-op Translator lahko uporabljate iz CLI, Python API ali MCP strežnika. Začnite z vodnikom poteka dela, če izbirate med lokalnim prevajanjem, avtomatizacijo, CI in integracijo agent/urejevalnik.

- [Izberite svoj potek dela](../../docs/workflows.md)
- [Konfigurirajte poverilnice](../../docs/configuration.md)
- [Prevajanje iz CLI](../../docs/cli.md)
- [Avtomatizirajte z Python API](../../docs/api.md)
- [Povežite se z MCP strežnikom](../../docs/mcp.md)
- [Zaženite v GitHub Actions](../../docs/github-actions.md)

Osnovni primer CLI po konfiguraciji:

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

Za prve zagon na velikih repozitorijih uporabite `--dry-run` pred zapisom prevedenih datotek. Oglejte si [CLI Reference](../../docs/cli.md) za zastavice tipov vsebine, dnevnike, pregled in migracijo povezav.

Hiter zagon v kontejnerju z Bash/Zsh:

```bash
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko" -md
```

Hiter zagon v kontejnerju z PowerShell:

```powershell
docker run --rm -it --env-file .env -v ${PWD}:/work ghcr.io/azure/co-op-translator:latest -l "ko" -md
```

## Funkcije

- Samodejno prevajanje za Markdown, zvezke in slike
- Ohranja prevode sinhronizirane z izvorne spremembe
- Deluje lokalno (CLI) ali v CI (GitHub Actions)
- Omogoča orodja za prevajanje Markdown, zvezkov, slik, pregledov in projektov preko MCP
- Uporablja Azure OpenAI ali OpenAI za prevajanje, podprto s ponudnikom
- Dovoli, da MCP gostuje agente, ki prevajajo kose Markdowna in zvezkov brez Co-op Translator LLM poverilnic
- Uporablja Azure AI Vision za izločanje besedila iz slik in prevod
- Pregleduje strukturo prevoda in njegovo ažurnost z determinističnimi preverjanji
- Ohranja oblikovanje in strukturo Markdowna

## Dokumentacija

- [Spletna dokumentacija](https://azure.github.io/co-op-translator/)
- [Izberite svoj potek dela](../../docs/workflows.md)
- [Konfiguracija](../../docs/configuration.md)
- [Nastavitev Azure AI](../../docs/azure-ai-setup.md)
- [CLI Reference](../../docs/cli.md)
- [Python API](../../docs/api.md)
- [MCP Server](../../docs/mcp.md)
- [GitHub Actions](../../docs/github-actions.md)
- [Predloga README jezikov](../../docs/readme-languages-template.md)
- [Podprti jeziki](../../docs/supported-languages.md)
- [Prispevanje](../../CONTRIBUTING.md)
- [Odpravljanje težav](../../docs/troubleshooting.md)

### Microsoft-specifičen vodnik
> [!NOTE]
> Za vzdrževalce Microsoftovih repozitorijev “For Beginners” samo.

- [Posodabljanje seznama 'other courses' (samo za MS Beginners repozitorije)](../../docs/microsoft-beginners.md)

## Podprite nas in spodbujajte globalno učenje

Pridružite se nam pri preoblikovanju načina deljenja izobraževalne vsebine po svetu! Nagradite [Co-op Translator](https://github.com/azure/co-op-translator) z ⭐ na GitHubu in podprite naše poslanstvo razbijanja jezikovnih ovir pri učenju in tehnologiji. Vaš interes in prispevki imajo velik vpliv! Prispevki kode in predlogi za funkcije so vedno dobrodošli.

### Raziščite Microsoftovo izobraževalno vsebino v vašem jeziku
- [LangChain4j za začetnike](https://github.com/microsoft/LangChain4j-for-Beginners)
- [AZD za začetnike](https://github.com/microsoft/AZD-for-beginners)
- [Edge AI za začetnike](https://github.com/microsoft/edgeai-for-beginners)
- [Model Context Protocol (MCP) za začetnike](https://github.com/microsoft/mcp-for-beginners)
- [AI agenti za začetnike](https://github.com/microsoft/ai-agents-for-beginners)
- [Generativna AI za začetnike z .NET](https://github.com/microsoft/Generative-AI-for-beginners-dotnet)
- [Generativna AI za začetnike](https://github.com/microsoft/generative-ai-for-beginners)
- [Generativna AI za začetnike z Javo](https://github.com/microsoft/generative-ai-for-beginners-java)
- [Strojno učenje za začetnike](https://aka.ms/ml-beginners)
- [Podatkovna znanost za začetnike](https://aka.ms/datascience-beginners)
- [Umetna inteligenca za začetnike](https://aka.ms/ai-beginners)
- [Kibernetska varnost za začetnike](https://github.com/microsoft/Security-101)
- [Spletni razvoj za začetnike](https://aka.ms/webdev-beginners)
- [IoT za začetnike](https://aka.ms/iot-beginners)
- [PhiCookBook](https://github.com/microsoft/PhiCookBook)

## Video predstavitve

👉 Kliknite sliko spodaj za ogled na YouTube.

- **Open at Microsoft**: Kratek 18-minutni uvod in hiter vodnik, kako uporabljati Co-op Translator.

  [![Open at Microsoft](../../imgs/open-ms-thumbnail.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## Prispevanje

Ta projekt sprejema prispevke in predloge. Želite prispevati k Azure Co-op Translator? Oglejte si naš [CONTRIBUTING.md](../../CONTRIBUTING.md) za smernice o tem, kako lahko pomagate narediti Co-op Translator bolj dostopen.

## Prispevalci

[![Prispevalci co-op-translator](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## Kodeks ravnanja

Projekt je sprejel [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
Za več informacij si oglejte [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) ali
kontaktirajte [opencode@microsoft.com](mailto:opencode@microsoft.com) za dodatna vprašanja ali pripombe.

## Odgovorna umetna inteligenca

Microsoft si prizadeva pomagati našim strankam pri odgovorni uporabi naših AI izdelkov, deliti pridobljena znanja in graditi partnerstva, ki temeljijo na zaupanju, z orodji, kot so Transparency Notes in Impact Assessments. Veliko teh virov najdete na [https://aka.ms/RAI](https://aka.ms/RAI).
Microsoftov pristop k odgovorni AI temelji na naših načelih AI: pravičnost, zanesljivost in varnost, zasebnost in zaščita, vključenost, preglednost in odgovornost.

Veliki modeli za naravni jezik, slike in govor — kot tisti, uporabljeni v tem vzorcu — se lahko obnašajo na načine, ki so nepravični, nezanesljivi ali žaljivi in lahko povzročijo škodo. Za informacije o tveganjih in omejitvah si oglejte [Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text).

Priporočeni pristop za ublažitev teh tveganj je vključitev varnostnega sistema v vašo arhitekturo, ki lahko zaznava in preprečuje škodljivo vedenje. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) zagotavlja neodvisno plast zaščite, sposobno zaznati škodljivo vsebino, ustvarjeno s strani uporabnikov in z AI, v aplikacijah in storitvah. Azure AI Content Safety vključuje API-je za besedilo in slike, ki omogočajo zaznavanje škodljivih vsebin. Imamo tudi interaktivni Content Safety Studio, ki vam omogoča ogled, raziskovanje in preizkus primerov kode za zaznavanje škodljive vsebine v različnih modalnostih. Naslednja [quickstart documentation](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) vas vodi skozi pošiljanje zahtevkov storitvi.

Drug vidik, ki ga je treba upoštevati, je splošna zmogljivost aplikacije. Pri aplikacijah z več modalnostmi in več modeli razumemo zmogljivost kot to, da sistem deluje tako, kot vi in vaši uporabniki pričakujete, vključno s tem, da ne ustvarja škodljivih izhodov. Pomembno je oceniti zmogljivost vaše celotne aplikacije z uporabo [generation quality and risk and safety metrics](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in).

Aplikacijo AI lahko ocenite v vašem razvojnem okolju z uporabo [prompt flow SDK](https://microsoft.github.io/promptflow/index.html). Glede na testni nabor podatkov ali cilj so generacije vaše generativne AI aplikacije kvantitativno merjene z vgrajenimi ocenjevalci ali s prilagojenimi ocenjevalci po vaši izbiri. Če želite začeti z prompt flow SDK za ocenjevanje vašega sistema, lahko sledite [quickstart guide](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Ko izvedete ocenitveni zagon, lahko [visualize the results in Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Blagovne znamke

Ta projekt lahko vsebuje blagovne znamke ali logotipe za projekte, izdelke ali storitve. Pooblaščena uporaba Microsoftovih blagovnih znamk ali logotipov je pogojevana in se mora izvajati v skladu z [Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
Uporaba Microsoftovih blagovnih znamk ali logotipov v spremenjenih različicah tega projekta ne sme povzročiti zmede ali nakazovati Microsoftovega sponzorstva.
Vsaka uporaba blagovnih znamk ali logotipov tretjih oseb je predmet politik teh tretjih oseb.

## Kako dobiti pomoč

Če se zataknete ali imate vprašanja o gradnji AI aplikacij, se pridružite:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Če imate povratne informacije o izdelku ali napake med izdelavo, obiščite:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)