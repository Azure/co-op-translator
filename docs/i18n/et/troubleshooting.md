# Tõrkeotsing

Kasutage seda lehte, kui tõlkeprotsess õnnestub ootamatult, ebaõnnestub konfiguratsiooni ajal või annab väljundi, mis vajab ülevaatust.

## Alustage siit

1. Käivitage esmalt spetsiifiline käsk, näiteks `translate -l "ko" -md`.
2. Lisage `-d` konsooli silumislogide jaoks.
3. Lisage `-s`, et salvestada silumislogid asukohta `<root-dir>/logs/`.
4. Käivitage pärast tõlget `co-op-review`, et kontrollida ajakohasust, struktuuri ja kohalikke linke.

```bash
translate -l "ko" -md -d -s
co-op-review -l "ko"
```

## Konfiguratsiooni vead

### Keelemudeli pakkujat pole

Viga:

```text
No language model configuration found.
```

Lahendus:

- Konfigureerige Azure OpenAI, OpenAI või Anthropic.
- Kontrollige, et muutujad on keskkonnas, kus käsk käivitatakse.
- Kohalikuks kasutuseks pange need projekti juurkausta `.env`.

Vaadake [Konfiguratsiooni](configuration.md).

### Pildi tõlkimine ilma Azure AI Visionita

Viga:

```text
Image translation requested but Azure AI Service is not configured.
```

Lahendus:

- Lisage `AZURE_AI_SERVICE_API_KEY`.
- Lisage `AZURE_AI_SERVICE_ENDPOINT`.
- Või käivitage ainult teksti käsk, näiteks `translate -l "ko" -md`.

### Kehtetu võti või lõpp-punkt

Sümptomiteks võivad olla `401`, õiguste vead või lõpp-punkti ligipääsuvead.

Lahendus:

- Kinnitage, et võti kuulub samale Azure'i ressursile kui lõpp-punkt.
- Kinnitage, et ressurss toetab Vision-i, kui kasutate `-img`.
- Kinnitage, et Azure OpenAI juurutuse nimi ja API versioon vastavad teie juurutusele.
- Käivitage silumislogidega: `translate -l "ko" -md -d -s`.

## Ühtegi faili ei tõlgitud

Tavalised põhjused:

- Valitud lipud ei sobi teie failidega.
- Tõlgitud failid on juba olemas.
- Allika failid asuvad välistatud kataloogides.
- Käsk töötab vale projekti juurest.

Kontrollid:

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -nb --dry-run
translate -l "ko" -img --dry-run
```

Kasutage `--root-dir`, kui käsk käivitatakse väljaspool projekti juurkausta.

## Ootamatu linkide käitumine

Linkide ümberkirjutamine sõltub valitud sisutüüpidest:

- `-nb` lisatud: notebooki lingid võivad viidata tõlgitud märkmikutele.
- `-nb` välistatud: notebooki lingid võivad jääda viitama lähte-märkmikutele.
- `-img` lisatud: pildilingid võivad viidata tõlgitud piltidele.
- `-img` välistatud: pildilingid võivad jääda viitama lähtepiltidele.

Käivitage täielik sisu tõlge, kui kõik sisemised lingid peaksid eelistama tõlgitud väljundeid:

```bash
translate -l "ko" -md -nb -img
```

Käivitage linkide ülevaatus pärast tõlget:

```bash
co-op-review -l "ko"
```

## Markdowni renderdamise probleemid

Kui tõlgitud Markdown renderdub valesti:

- Kontrollige, et frontmatter algab ja lõpeb `---`.
- Kontrollige, et koodi tõkete arvu (```) oleks sama allika ja tõlgitud failide vahel.
- Käivitage `co-op-review`, et tuvastada levinud struktuuriprobleeme.
- Tõlkige konkreetne fail uuesti, kui väljund oli rikutud.

```bash
co-op-review -l "ko" --format github
```

## GitHub Action jooksis, kuid pull-päringut ei loodud

Kui `peter-evans/create-pull-request` teatab, et haru ei ole baasist ees, siis töövoog ei leidnud commiteerimiseks faile.

Tõenäolised põhjused:

- Tõlkejooks ei tootnud muudatusi.
- `.gitignore` välistab `translations/`, `translated_images/` või tõlgitud märkmikuid.
- `add-paths` ei vasta genereeritud väljundkataloogidele.
- Tõlkesamm lõpetas enneaegselt.

Lahendused:

1. Kinnitage, et genereeritud failid asuvad kaustades `translations/` või `translated_images/`.
2. Kinnitage, et `.gitignore` ei ignoreeri genereeritud väljundeid.
3. Kasutage vastavaid `add-paths`:

   ```yaml
   with:
     add-paths: |
       translations/
       translated_images/
   ```

4. Ajutiselt lisage translate-käsule silumislipud:

   ```bash
   translate -l "ko" -md -d -s
   ```

5. Kinnitage, et töövoo õigustes on lisatud:

   ```yaml
   permissions:
     contents: write
     pull-requests: write
   ```

## Tõlke kvaliteet

Masintõlkeid võib vaja minna inimlikku ülevaatust. Kasutage `evaluate` ainult siis, kui soovite eksperimentaalset kvaliteedi hindamist ja madala usaldusastmega paranduste töövooge.

!!! warning "Eksperimentaalne"
    `evaluate` võib kasutada reeglipõhiseid ja LLM-põhiseid kontrolle ning selle skoorimismudel ja metainfo käitumine võivad muutuda. Hoidke seda eemal nõutavatest CI-väravatest, kui teie töövoog ei ole muudatusteks valmis.

Deterministlike CI-kontrollide jaoks kasutage selle asemel `co-op-review`.