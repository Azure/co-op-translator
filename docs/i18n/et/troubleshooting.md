# Tõrkeotsing

Kasutage seda lehte, kui tõlkerun õnnestub ootamatult, ebaõnnestub konfiguratsiooni ajal või genereerib väljundi, mida tuleb üle vaadata.

## Alustamiseks

1. Käivitage esmalt sihitud käsk, näiteks `translate -l "ko" -md`.
2. Lisage `-d` konsooli silumislogide jaoks.
3. Lisage `-s`, et salvestada silumislogid kataloogi `<root-dir>/logs/`.
4. Käivitage pärast tõlkimist `co-op-review`, et kontrollida ajakohasust, struktuuri ja kohalikke linke.

```bash
translate -l "ko" -md -d -s
co-op-review -l "ko"
```

## Konfiguratsiooni vead

### Keeltemudeli pakkujat pole

Viga:

```text
No language model configuration found.
```

Lahendus:

- Konfigureerige Azure OpenAI või OpenAI.
- Kontrollige, et muutujad oleksid keskkonnas, kus käsk käivitatakse.
- Kohalikuks kasutuseks lisage need projekti juurkausta faili `.env`.

Vaadake [Konfiguratsioon](configuration.md).

### Pildi tõlkimine ilma Azure AI Visionita

Viga:

```text
Image translation requested but Azure AI Service is not configured.
```

Lahendus:

- Lisage `AZURE_AI_SERVICE_API_KEY`.
- Lisage `AZURE_AI_SERVICE_ENDPOINT`.
- Või käivitage tekstipõhine käsk, näiteks `translate -l "ko" -md`.

### Vigane võti või lõpp-punkt

Sümptomiteks võivad olla `401`, loata seotud veateated või lõpp-punkti juurdepääsu vead.

Lahendus:

- Kinnitage, et võti kuulub samale Azure'i ressursile kui lõpp-punkt.
- Kinnitage, et ressurss toetab Visioni, kui kasutatakse `-img`.
- Kinnitage, et Azure OpenAI juurutuse nimi ja API-versioon vastavad teie seadistusele.
- Käivitage silumislogidega: `translate -l "ko" -md -d -s`.

## Ühtegi faili ei tõlgitud

Levinumad põhjused:

- Valitud lipud ei vasta teie failidele.
- Olemas on juba tõlgitud failid.
- Allikfailid asuvad välistatud kataloogides.
- Käsk käivitati valest projekti juurkaustast.

Kontrollid:

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -nb --dry-run
translate -l "ko" -img --dry-run
```

Kasutage `--root-dir`, kui käsk käivitatakse väljaspool projekti juurkausta.

## Ootamatu linkide käitumine

Linkide ümberkirjutamine sõltub valitud sisutüüpidest:

- `-nb` included: notebook links can point to translated notebooks.
- `-nb` excluded: notebook links can remain pointed at source notebooks.
- `-img` included: image links can point to translated images.
- `-img` excluded: image links can remain pointed at source images.

Käivitage täielik sisu tõlkimine, kui kõik sisemised lingid peaksid eelistama tõlgitud väljundeid:

```bash
translate -l "ko" -md -nb -img
```

Käivitage linkide ülevaatus pärast tõlkimist:

```bash
co-op-review -l "ko"
```

## Markdowni renderdamise probleemid

Kui tõlgitud Markdown renderdub valesti:

- Kontrollige, et frontmatter algab ja lõpeb `---`-ga.
- Kontrollige, et lähte- ja tõlgitud failide koodiplokkide piiritlejate arv (``` ) on sama.
- Käivitage `co-op-review`, et püüda tavalisi struktuuriprobleeme.
- Tõlkige konkreetne fail uuesti, kui väljund oli rikutud.

```bash
co-op-review -l "ko" --format github
```

## GitHub Action käivitus, kuid pull requesti ei loodud

Kui `peter-evans/create-pull-request` teatab, et haru ei ole baasist ees, ei leidnud töövoog commitimiseks faile.

Tõenäolised põhjused:

- Tõlkerun ei tekitanud muudatusi.
- `.gitignore` välistab `translations/`, `translated_images/` või tõlgitud märkmikud.
- `add-paths` ei vasta genereeritud väljundkataloogidele.
- Tõlkimise samm lõpetas enneaegselt.

Lahendused:

1. Kinnitage, et genereeritud failid eksisteerivad kataloogides `translations/` või `translated_images/`.
2. Kinnitage, et `.gitignore` ei ignoreeri genereeritud väljundeid.
3. Use matching `add-paths`:

   ```yaml
   with:
     add-paths: |
       translations/
       translated_images/
   ```

4. Temporarily add debug flags to the translate command:

   ```bash
   translate -l "ko" -md -d -s
   ```

5. Confirm workflow permissions include:

   ```yaml
   permissions:
     contents: write
     pull-requests: write
   ```

## Tõlke kvaliteet

Masintõlked võivad vajada inimlikku ülevaatust. Kasutage `evaluate` ainult siis, kui soovite eksperimentaalset kvaliteedihindamist ja madala usaldusväärsusega paranduste töövooge.

!!! warning "Experimental"
    `evaluate` võib kasutada reeglipõhiseid ja LLM-põhiseid kontrolle, ning selle hindamismudel ja metaandmete käitumine võivad muutuda. Ärge lisage seda nõutavatesse CI-väravatesse, kui teie töövoog ei ole muutusteks ette valmistatud.

Deterministlike CI-kontrollide jaoks kasutage selle asemel `co-op-review`.