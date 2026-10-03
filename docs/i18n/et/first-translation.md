# Tõlgi, redigeeri ja vaata üle väikest projekti

Alusta kahe lühikese Markdown-failiga ja ühe sihtkeelega. Näed, kuhu tõlked salvestatakse, mis juhtub, kui lähtefail muutub, ja kuidas tulemust kontrollida.

## Salvestatud tulemused

Näide käivitati 19. septembril 2026 Co-op Translator 0.21.0 ja Azure OpenAI (`gpt-5-mini`) abil. Muutmata CLI-käske kutsuti esile Click'i `CliRunner`i kaudu, kasutades ehitatud wheel'i ja olemasolevaid Python'i sõltuvusi.

| Samm | Tulemus |
| --- | --- |
| Eelvaade | Väljumiskood 0; mudeli tõlget ei taotletud |
| Algne tõlge | Väljumiskood 0; 27,36 sekundit |
| Algne ülevaatus | Väljumiskood 0 |
| Redigeeri README ja vaata üle | Väljumiskood 1; aegunud tõlge tuvastatud |
| Uuenda tõlget | Väljumiskood 0; 22,17 sekundit |
| Ülevaatus pärast uuendust | Väljumiskood 0; vigu ega hoiatusi ei ole |
| Muutmata juhend | Baitid identsed enne ja pärast README uuendust |
| Käivita uuesti | Väljumiskood 0; kõigi tõlkefailide hashid on identsed |

Need on üksikesituste mõõtmised, mitte jõudluse garantii. Seadistusaeg ei ole arvesse võetud; teenusepakkuja arveldamist ei mõõdetud. Muutmata käivitamine võib siiski sooritada teenusepakkuja tervisekontrolli.

Vaata [algset tõlget](../../assets/demo/before.txt), [uuendatud tõlget](../../assets/demo/after.txt), [täieliku tõlke diffi](../../assets/demo/update.diff), [aegunud ülevaadet](../../assets/demo/review-stale.txt), [lõplikku ülevaadet](../../assets/demo/review-after.txt) ja [käivituse üksikasju](../../assets/demo/results.json). Terve faili tõlge võib muuta teisi sõnastusi, nagu tabatud diff näitab. Mõlemad tekstiartefaktid säilitavad genereeritud vastutuseavalduse.

Inimese ülevaatus on endiselt oluline: tabatud uuenduses kasutatakse `[사용 가이드](guide.md)을`; korea partiklit peaks olema `[사용 가이드](guide.md)를`. Tekstilised artefaktid jätavad selle väljundi muutmatuks selle asemel, et esitada redigeeritud tõlget mudeli väljundina. Struktuurne ülevaatus läbib vaatamata sellele sõnastusprobleemile.

## 1. Valmista väike kaust

Kasuta Pythonit 3.11–3.14 ja [virtuaalse keskkonna seadistust](configuration.md#local-runtime-setup). Paigalda selle näite jaoks kasutatud versioon:

```bash
python -m pip install co-op-translator==0.21.0
mkdir translation-demo
cd translation-demo
git init
```

Laadi alla [README.txt](../../assets/demo/README.txt) ja [guide.txt](../../assets/demo/guide.txt) sellesse kausta, salvesta need kui `README.md` ja `guide.md`. Need on väikesed väljamõeldud projekti dokumendid; rakenduse paigaldamine ei ole vajalik.

README sisaldab koodiplokki ja linki `guide.md`. Selle viimane lause on:

```text
Notes are saved locally.
```

Hoia selles kaustas ainult neid kahte lähtefaili. Kõik järgnevad käsud käivitatakse kaustas `translation-demo` ja töötavad nii Bashis kui PowerShellis.

## 2. Eelvaade ilma volitusteta

```bash
translate -l "ko" -md --dry-run
```

Eelvaade hindab tõlketöö hulka ilma mudelit kutsumata või tõlkeid kirja panemata. Tokenite hinnang ei ole arve aluseks. Esimene käivitamine peaks tuvastama mõlemad Markdown-failid kui uue töö.

## 3. Vali teenusepakkuja ja tõlgi

Seadista üks teenusepakkuja vastavalt [konfiguratsiooni juhisele](configuration.md): Azure OpenAI, OpenAI või Anthropic. OpenAI ja Anthropic tekstide tõlkimiseks Azure'i kontot ei ole vaja. Selle näite jaoks pilditeenuseid ei vajata.

Kui kasutad kohalikku `.env` faili, lisa `.env` selle kausta `.gitignore`-i. Tõlkekõned kasutavad sinu teenusepakkuja kontot ja võivad kaasa tuua kulusid.

```bash
translate -l "ko" -md
co-op-review -l "ko"
```

Ava `translations/ko/README.md` ja `translations/ko/guide.md`. Kontrolli korea sõnastust, koodiplokki ja linki tõlgitud README-st tõlgitud juhendisse. Väljundi sõnastus võib mudeli lõikes erineda.

`co-op-review` kontrollib värskust, struktuuri ja kohalikke linke. Läbitud tulemus ei kinnita keelelist täpsust. Lahenda kõik raportitud vead enne jätkamist.

Salvesta edukas algseis Gitiga (vajadusel määra esmalt oma Git-identiteet):

```bash
git add README.md guide.md translations
git commit -m "Record initial Korean translation"
```

## 4. Muuda lähtefaili

Asenda failis `README.md` tekst `Notes are saved locally.` järgmisega:

```text
Notes are saved locally as Markdown files.
```

Jäta `guide.md` muutmata. Seejärel käivita:

```bash
co-op-review -l "ko"
translate -l "ko" -md --dry-run
```

Ülevaatus peaks teatama, et README tõlge on aegunud ja lõpetama ebaõnnestunult. See on oodatud vahe-olek. Eelvaade peaks tuvastama töö muutunud README jaoks.

## 5. Uuenda ja vaata diffi

```bash
translate -l "ko" -md
git diff -- README.md translations/ko/README.md
git diff -- translations/ko/guide.md
co-op-review -l "ko"
```

Vaata tegelikku diffi: vaikimisi CLI tõlgib muutunud faili uuesti, nii et mudel võib muuta ka muud sõnastust selles failis. Muutmata juhendil ei tohiks olla diffi. Ülevaatus ei tohiks enam teatada README aegumisest; uurige kõiki teisi leide, selle asemel et neid ignoreerida.

Plokitasemel inimeste Markdowni redaktsioonide säilitamine nõuab valikulist tõlkeoleku pakkujat [Python API](api.md)-s. Seda ei ole nende CLI-käskudega lubatud.

## 6. Käivita uuesti ilma muutusteta

Kinnita uuendatud lähtefail ja tõlge:

```bash
git add README.md translations
git commit -m "Update Korean translation after source edit"
translate -l "ko" -md
git diff --exit-code -- translations
```

Praeguste tõlgete ja muutmata konfiguratsiooni korral jätab tõlkija failid vahele. Viimane Git-käsk ei tohiks anda diffi ja peaks lõppema edukalt.

## Järgmised sammud

- [Tõlgi ainult README ja ava pull request](github-actions.md#your-first-readme-translation-pr).
- [Vali CLI, Python API või MCP](workflows.md).
- [Teata tõlkeprobleemist ilma kodeerimiseta](https://github.com/Azure/co-op-translator/issues/new?template=translation_feedback.yml).