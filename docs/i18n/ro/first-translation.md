# Traduceți, editați și revizuiți un proiect mic

Începeți cu două fișiere scurte Markdown și o limbă țintă. Veți vedea unde sunt scrise traducerile, ce se întâmplă când sursa se schimbă și cum să verificați rezultatul.

## Rezultate înregistrate

Exemplul a fost rulat pe 19 septembrie 2026 cu Co-op Translator 0.21.0 și Azure OpenAI (`gpt-5-mini`). Comenzile CLI neatinse au fost apelate prin `CliRunner` din Click folosind pachetul construit și dependențele Python existente.

| Pas | Rezultat |
| --- | --- |
| Previzualizare | Ieșire 0; nicio solicitare de traducere a modelului |
| Traducerea inițială | Ieșire 0; 27.36 secunde |
| Revizuirea inițială | Ieșire 0 |
| Editare README și revizuire | Ieșire 1; traducere învechită detectată |
| Actualizare traducere | Ieșire 0; 22.17 secunde |
| Revizuire după actualizare | Ieșire 0; fără erori sau avertismente |
| Ghid neschimbat | Octeți identici înainte și după actualizarea README |
| Rulați din nou | Ieșire 0; hash-uri identice pentru toate fișierele de traducere |

Acestea sunt măsurători ale rulărilor individuale, nu garanții de performanță. Timpul de configurare este exclus; facturarea furnizorului nu a fost măsurată. O rulare neschimbată poate totuși efectua o verificare a stării furnizorului.

Examinați [traducerea inițială](../../assets/demo/before.txt), [traducerea actualizată](../../assets/demo/after.txt), [diferența completă a traducerii](../../assets/demo/update.diff), [revizuirea învechită](../../assets/demo/review-stale.txt), [revizuirea finală](../../assets/demo/review-after.txt) și [detalii despre rulare](../../assets/demo/results.json). Traducerea întregului fișier poate schimba alte formulări, așa cum arată diff-ul capturat. Ambele artefacte text păstrează declarația generată.

Revizuirea umană contează în continuare: actualizarea capturată folosește `[사용 가이드](guide.md)을`; particula coreeană ar trebui să fie `[사용 가이드](guide.md)를`. Artefactele text păstrează această ieșire neatinsă în loc să prezinte o traducere editată ca ieșire a modelului. Revizuirea structurală trece în ciuda acestei probleme de formulare.

## 1. Pregătiți un dosar mic

Folosiți Python 3.11–3.14 și [configurarea mediului virtual](configuration.md#local-runtime-setup). Instalați versiunea folosită pentru acest exemplu:

```bash
python -m pip install co-op-translator==0.21.0
mkdir translation-demo
cd translation-demo
git init
```

Descărcați [README.txt](../../assets/demo/README.txt) și [guide.txt](../../assets/demo/guide.txt) în acest dosar, salvându-le ca `README.md` și `guide.md`. Sunt documente mici fictive ale proiectului; nu este necesară instalarea unei aplicații.

README-ul include un bloc de cod și un link către `guide.md`. Ultima sa propoziție este:

```text
Notes are saved locally.
```

Păstrați numai aceste două documente sursă în acest dosar. Toate comenzile următoare rulează în interiorul `translation-demo` și funcționează în Bash și PowerShell.

## 2. Previzualizare fără credențiale

```bash
translate -l "ko" -md --dry-run
```

Previzualizarea estimează volumul de lucru pentru traducere fără a apela un model sau a scrie traducerile. Estimările de tokeni nu sunt o cotație de facturare. Prima rulare ar trebui să identifice ambele fișiere Markdown ca lucru nou.

## 3. Alegeți un furnizor și traduceți

Configurați un furnizor folosind [ghidul de configurare](configuration.md): Azure OpenAI, OpenAI sau Anthropic. Traducerea textului cu OpenAI și Anthropic nu necesită un cont Azure. Serviciile de imagine nu sunt necesare pentru acest exemplu.

Dacă folosiți un fișier local `.env`, adăugați `.env` în `.gitignore` al acestui dosar. Apelurile de traducere folosesc contul furnizorului dvs. și pot genera costuri.

```bash
translate -l "ko" -md
co-op-review -l "ko"
```

Deschideți `translations/ko/README.md` și `translations/ko/guide.md`. Verificați formularea în coreeană, blocul de cod și linkul din README-ul tradus către ghidul tradus. Formularea ieșirii variază în funcție de model.

`co-op-review` verifică prospețimea, structura și linkurile locale. Un rezultat pozitiv nu certifică acuratețea lingvistică. Remediați orice erori raportate înainte de a continua.

Înregistrați starea de bază reușită cu Git (configurați mai întâi identitatea Git dacă este necesar):

```bash
git add README.md guide.md translations
git commit -m "Record initial Korean translation"
```

## 4. Schimbați sursa

În `README.md`, înlocuiți `Notes are saved locally.` cu:

```text
Notes are saved locally as Markdown files.
```

Lăsați `guide.md` neschimbat. Apoi rulați:

```bash
co-op-review -l "ko"
translate -l "ko" -md --dry-run
```

Revizuirea ar trebui să raporteze traducerea README ca fiind învechită și să iasă cu eșec. Aceasta este starea intermediară așteptată. Previzualizarea ar trebui să identifice lucru pentru README-ul modificat.

## 5. Actualizați și inspectați diff-ul

```bash
translate -l "ko" -md
git diff -- README.md translations/ko/README.md
git diff -- translations/ko/guide.md
co-op-review -l "ko"
```

Examinați diff-ul real: CLI-ul implicit retranslează fișierul modificat, astfel încât modelul poate, de asemenea, să revizuiască alte formulări din acel fișier. Ghidul neschimbat nu ar trebui să aibă diff. Revizuirea nu ar trebui să mai raporteze README-ul ca învechit; investigați orice alte constatări în loc să le ignorați.

Păstrarea la nivel de bloc a editărilor umane în Markdown necesită un furnizor opțional de stare a traducerii în [Python API](api.md). Nu este activat de aceste comenzi CLI.

## 6. Rulați din nou fără modificări

Comiteți sursa și traducerea actualizate:

```bash
git add README.md translations
git commit -m "Update Korean translation after source edit"
translate -l "ko" -md
git diff --exit-code -- translations
```

Cu traducerile curente și configurația neschimbată, translatorul omite fișierele. Comanda Git finală nu ar trebui să producă diff și ar trebui să se încheie cu succes.

## Pașii următori

- [Traduceți doar un README și deschideți un pull request](github-actions.md#your-first-readme-translation-pr).
- [Alegeți CLI, Python API sau MCP](workflows.md).
- [Raportați o problemă de traducere fără a scrie cod](https://github.com/Azure/co-op-translator/issues/new?template=translation_feedback.yml).