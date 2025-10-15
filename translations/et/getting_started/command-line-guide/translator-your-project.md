<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "20943a46b11c6d74814f41a817a6db4c",
  "translation_date": "2025-10-15T05:00:56+00:00",
  "source_file": "getting_started/command-line-guide/translator-your-project.md",
  "language_code": "et"
}
-->
# Tõlgi oma projekt Co-op Translatoriga

**Co-op Translator** on käsurea tööriist (CLI), mis aitab sul tõlkida oma projekti markdown- ja pildifaile mitmesse keelde. Selles jaotises selgitatakse, kuidas tööriista kasutada, tutvustatakse erinevaid CLI valikuid ning tuuakse näiteid erinevate kasutusjuhtude kohta.

> [!NOTE]
> Kõigi käskude ja nende detailsete kirjelduste täieliku loendi leiad [Käsurea viitest](./command-reference.md).

---

## Näitesituatsioonid ja käsud

Siin on mõned levinumad kasutusviisid **Co-op Translatori** jaoks koos sobivate käskudega.

### 1. Põhitõlge (üks keel)

Kui soovid tõlkida kogu oma projekti (markdown-failid ja pildid) ühte keelde, näiteks korea keelde, kasuta järgmist käsku:

```bash
translate -l "ko"
```

See käsk tõlgib kõik markdown- ja pildifailid korea keelde, lisades uued tõlked ilma olemasolevaid kustutamata.

> [!TIP]
>
> Soovid teada, millised keelekoodid on **Co-op Translatoris** saadaval? Vaata [Toetatud keeled](https://github.com/Azure/co-op-translator#supported-languages) jaotist repo lehel.

#### Näide Phi-3 CookBookis

**Phi-3 CookBookis** kasutasin järgmist meetodit, et lisada olemasolevatele markdown-failidele ja piltidele korea tõlge.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko"
Translating images: 100%|███████████████████████████████████████████████████| 276/276 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 153/153 [1:43:07<00:00, 241.31s/it]
```

### 2. Tõlkimine mitmesse keelde

Kui soovid tõlkida projekti mitmesse keelde (nt hispaania, prantsuse ja saksa), kasuta seda käsku:

```bash
translate -l "es fr de"
```

See käsk tõlgib projekti hispaania, prantsuse ja saksa keelde, lisades uued tõlked ilma olemasolevaid üle kirjutamata.

#### Näide Phi-3 CookBookis

**Phi-3 CookBookis** tõmbasin kõigepealt viimased muudatused, et kajastada värskeid committe, ja kasutasin seejärel järgmist meetodit, et tõlkida hiljuti lisatud markdown-failid ja pildid.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko ja zh tw es fr" -a
Translating images: 100%|███████████████████████████████████████████████████| 273/273 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 6/6 [24:07<00:00, 241.31s/it]
```

> [!NOTE]
> Üldiselt on soovitatav tõlkida üks keel korraga, kuid sellistes olukordades, kus on vaja lisada kindlaid muudatusi, võib mitme keele korraga tõlkimine olla tõhus.

### 3. Tõlgete uuendamine (kustutab olemasolevad tõlked)

Olemasolevate tõlgete uuendamiseks (ehk kustutab praegused tõlked ja asendab need uutega) kasuta `-u` valikut. See kustutab kõik valitud keelte tõlked ja tõlgib need uuesti.

```bash
translate -l "ko" -u
```

Hoiatus: See käsk küsib enne olemasolevate tõlgete kustutamist kinnitust.

#### Näide Phi-3 CookBookis

**Phi-3 CookBookis** kasutasin järgmist meetodit, et uuendada kõiki hispaaniakeelseid tõlgitud faile. Soovitan seda meetodit kasutada, kui originaalsisu on oluliselt muutunud mitmes markdown-dokumendis. Kui vaja uuendada vaid mõnda tõlgitud markdown-faili, on tõhusam need käsitsi kustutada ja kasutada `-a` meetodit, et lisada uuendatud tõlked.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "es" -u
Warning: The update command will delete all existing translations for 'es' and re-translate everything.
Do you want to continue? Type 'yes' to proceed: yes
Proceeding with update...
Translating images: 100%|████████████████████████████████████████████| 150/150 [43:46<00:00, 15.55s/it]
Translating markdown files: 100%|███████████████████████████████████| 95/95 [1:40:27<00:00, 125.62s/it]
```

### 5. Ainult piltide tõlkimine

Kui soovid tõlkida ainult projekti pildifaile, kasuta `-img` valikut:

```bash
translate -l "ko" -img
```

See käsk tõlgib ainult pildid korea keelde, mõjutamata markdown-faile.

### 6. Ainult markdown-failide tõlkimine

Kui soovid tõlkida ainult projekti markdown-faile, kasuta `-md` valikut:

```bash
translate -l "ko" -md
```

#### Näide Phi-3 CookBookis

**Phi-3 CookBookis** kasutasin järgmist meetodit, et kontrollida tõlkevigu korea failides ja automaatselt proovida uuesti tõlkida faile, kus tuvastati vigu.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko" -chk 
Checking translated files for errors in ko...
Checking files for ko: 100%|██████████████████████████████████████████████████| 95/95 [00:01<00:00, 65.47file/s]
Retrying vsc-extension-quickstart.md for ko:   0%|                                     | 0/17 [00:00<?, ?file/s] 
```

See valik kontrollib tõlkevigu. Praegu, kui originaali ja tõlgitud faili reavahede erinevus on üle kuue, märgitakse fail tõlkeveaga. Plaanin seda kriteeriumi tulevikus paindlikumaks muuta.

Näiteks on see meetod kasulik puuduva sisu või rikutud tõlgete tuvastamiseks ning tõlge tehakse automaatselt uuesti nende failide jaoks.

Kui aga tead juba, millised failid on probleemsed, on tõhusam need käsitsi kustutada ja kasutada `-a` valikut, et need uuesti tõlkida.

### 8. Silumisrežiim

Detailse logimise lubamiseks veaotsingul kasuta `-d` valikut:

```bash
translate -l "ko" -d
```

See käsk käivitab tõlkimise silumisrežiimis, pakkudes lisalogisid, mis aitavad tõlkeprotsessi käigus vigu tuvastada.

#### Näide Phi-3 CookBookis

**Phi-3 CookBookis** tekkis mul probleem, kus paljude linkidega markdown-failide tõlkimisel esines vormindusvigu, näiteks katkenud tõlked ja eiratud reavahed. Selle probleemi diagnoosimiseks kasutasin `-d` valikut, et näha, kuidas tõlkeprotsess toimib.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "ko" -d
DEBUG:openai._base_client:Request options: {'method': 'post', 'url': '/chat/completions', 'headers': {'api-key': 'af04e0bea45747d8a7b8c131c1971044'}, 'files': None, 'json_data': {'messages': [{'role': 'user', 'content': "Translate the following text to ko. NEVER ADD ANY EXTRA CONTENT OUTSIDE THE TRANSLATION. TRANSLATE ONLY WHAT IS GIVEN TO YOU.. MAINTAIN MARKDOWN FORMAT\n\n# Phi-3 Cookbook: Hands-On Examples with Microsoft's Phi-3 Models [![Open and use the samples in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phi-3cookbook) [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%
...
```

### 9. Kõikide keelte tõlkimine

Kui soovid tõlkida projekti kõikidesse toetatud keeltesse, kasuta märksõna all.

> [!WARNING]
> Kõikide keelte korraga tõlkimine võib võtta palju aega, sõltuvalt projekti suurusest. Näiteks **Phi-3 CookBooki** tõlkimine hispaania keelde võttis umbes 2 tundi. Sellise mahuga pole mõistlik, et üks inimene haldab 20 keelt. Soovitatav on töö jagada mitme panustaja vahel, igaüks haldab ühte või kahte keelt, ja tõlked uuendatakse järk-järgult.

```bash
translate -l "all"
```

See käsk tõlgib projekti kõikidesse saadaolevatesse keeltesse. Kui jätkad, võib tõlkimine võtta palju aega, sõltuvalt projekti suurusest.

> [!TIP]
>
> ### Tõlgitud failide käsitsi kustutamine (valikuline)
> Tõlgitud failid tuvastatakse ja puhastatakse nüüd automaatselt, kui lähtefaili uuendatakse.
>
> Kui soovid siiski tõlget käsitsi uuendada – näiteks konkreetse faili uuesti tõlkimiseks või süsteemi käitumise ülekirjutamiseks – saad kasutada järgmist käsku, et kustutada kõik selle faili versioonid keelekaustadest.
>
> ### Windowsis:
> 1. **Command Prompti kasutamine**:
>    - Ava Command Prompt.
>    - Liigu kausta, kus failid asuvad, kasutades `cd` käsku.
>    - Kasuta järgmist käsku failide kustutamiseks:
>      ```
>      del /s *filename*
>      ```
>      Asenda `filename` selle failinime osaga, mida otsid. `/s` valik otsib ka alamkaustadest.
>
> 2. **PowerShelli kasutamine**:
>    - Ava PowerShell.
>    - Käivita see käsk:
>      ```powershell
>      Get-ChildItem -Path "C:\YourPath" -Filter "*filename*" -Recurse | Remove-Item -Force
>      ```
>      Asenda `"C:\YourPath"` kausta teega ja `filename` konkreetse nimega.
>
> ### macOS/Linuxis:
> 1. **Terminali kasutamine**:
>   - Ava Terminal.
>   - Liigu kataloogi `cd` abil.
>   - Kasuta `find` käsku:
>     ```bash
>     find . -type f -name "*filename*" -delete
>     ```
>     Asenda `filename` konkreetse nimega.
>
> Kontrolli alati faile enne kustutamist, et vältida juhuslikku kaotust.
>
> Kui vajalikud failid on kustutatud, käivita lihtsalt uuesti oma `translate -l` käsk, et uuendada viimased failimuudatused.

---

**Vastutusest loobumine**:  
See dokument on tõlgitud tehisintellekti tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Originaaldokumenti selle algses keeles tuleks pidada autoriteetseks allikaks. Kriitilise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgendamise eest.