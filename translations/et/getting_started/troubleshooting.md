<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6e626bef5ed78a1cc55b0dbf44f01d47",
  "translation_date": "2025-10-15T04:49:54+00:00",
  "source_file": "getting_started/troubleshooting.md",
  "language_code": "et"
}
-->
# Microsoft Co-op Translatori tõrkeotsingu juhend

## Ülevaade
Microsoft Co-Op Translator on võimas tööriist Markdowni dokumentide sujuvaks tõlkimiseks. See juhend aitab sul lahendada levinud probleeme, mis võivad tööriista kasutamisel ette tulla.

## Levinumad probleemid ja lahendused

### 1. Markdowni sildi probleem
**Probleem:** Tõlgitud Markdowni dokumendi ülaosas on `markdown` silt, mis põhjustab kuvamisprobleeme.

**Lahendus:** Selle lahendamiseks kustuta lihtsalt faili ülaosast `markdown` silt. Nii kuvatakse Markdowni fail korrektselt.

**Sammud:**
1. Ava tõlgitud Markdowni (`.md`) fail.
2. Leia dokumendi ülaosast `markdown` silt.
3. Kustuta see silt.
4. Salvesta muudatused.
5. Ava fail uuesti, et veenduda, et see kuvatakse õigesti.

### 2. Manustatud piltide URL-i probleem
**Probleem:** Manustatud piltide URL-id ei vasta keele lokaadile, mistõttu pildid on valed või puuduvad.

**Lahendus:** Kontrolli manustatud piltide URL-e ja veendu, et need vastavad keele lokaadile. Kõik pildid asuvad kaustas `translated_images` ning igal pildil on failinimes keele lokaadi tähis.

**Sammud:**
1. Ava tõlgitud Markdowni dokument.
2. Otsi manustatud pildid ja nende URL-id.
3. Veendu, et pildi failinimes olev keele lokaadi tähis vastab dokumendi keelele.
4. Vajadusel uuenda URL-e.
5. Salvesta muudatused ja ava dokument uuesti, et kontrollida, kas pildid kuvatakse õigesti.

### 3. Tõlke täpsus
**Probleem:** Tõlgitud sisu pole täpne või vajab täiendavat toimetamist.

**Lahendus:** Vaata tõlgitud dokument üle ja tee vajalikud parandused, et tõlge oleks täpsem ja loetavam.

**Sammud:**
1. Ava tõlgitud dokument.
2. Vaata sisu hoolikalt üle.
3. Tee vajalikud parandused tõlke täpsuse parandamiseks.
4. Salvesta muudatused.

## 4. Õiguste viga Redacted või 404

Kui pildid või tekst ei tõlgita õigesse keelde ja -d debug režiimis ilmneb 401 viga, on tegemist klassikalise autentimise probleemiga—võti on kas vale, aegunud või pole seotud õige piirkonna lõpp-punktiga.

Käivita co-op translator [-d debug lülitiga](https://github.com/Azure/co-op-translator/blob/main/getting_started/command-reference.md), et saada rohkem infot vea põhjuste kohta.

- **Veateade:** `Access denied due to invalid subscription key or wrong API endpoint.`
- **Võimalikud põhjused:**
  - Tellimuse võti on taotluses redigeeritud või vale.
  - AI Services Key või Subscription Key kuulub mõnele teisele Azure ressursile (nt Translator või OpenAI), mitte **Azure AI Vision** ressursile.

 **Ressursi tüüp**
  - Mine [Azure Portali](https://portal.azure.com) või [Azure AI Foundry](https://ai.azure.com) ja veendu, et ressurss on tüübiga `Azure AI services` → `Vision`.
  - Kontrolli võtmeid ja veendu, et kasutad õiget võtit.

## 5. Seadistuse vead (Uus veahaldus)

Alates uuest selektiivsest tõlkesüsteemist annab Co-op Translator nüüd selgeid veateateid, kui vajalikud teenused pole seadistatud.

### 5.1. Azure AI Service pole pilditõlkeks seadistatud

**Probleem:** Soovisid pilditõlget (`-img` lipp), kuid Azure AI Service pole korrektselt seadistatud.

**Veateade:**
```
Error: Image translation requested but Azure AI Service is not configured.
Please add AZURE_AI_SERVICE_API_KEY and AZURE_AI_SERVICE_ENDPOINT to your .env file.
Check Azure AI Service availability and configuration.
```

**Lahendus:**
1. **Variant 1**: Seadista Azure AI Service
   - Lisa `.env` faili `AZURE_AI_SERVICE_API_KEY`
   - Lisa `.env` faili `AZURE_AI_SERVICE_ENDPOINT`
   - Veendu, et teenus on ligipääsetav

2. **Variant 2**: Eemalda pilditõlke päring
   ```bash
   # Instead of: translate -l "ko" -img
   # Use: translate -l "ko" -md
   ```

### 5.2. Puuduv vajalik seadistus

**Probleem:** Oluline LLM-i seadistus puudub.

**Veateade:**
```
Error: No language model configuration found.
Please configure either Azure OpenAI or OpenAI in your .env file.
```

**Lahendus:**
1. Veendu, et sinu `.env` failis on vähemalt üks järgmistest LLM-i seadistustest:
   - **Azure OpenAI**: `AZURE_OPENAI_API_KEY` ja `AZURE_OPENAI_ENDPOINT`
   - **OpenAI**: `OPENAI_API_KEY`
   
   Vaja on kas Azure OpenAI või OpenAI seadistust, mitte mõlemat.

### 5.3. Selektiivse tõlke segadus

**Probleem:** Ühtegi faili ei tõlgitud, kuigi käsk õnnestus.

**Võimalikud põhjused:**
- Vale failitüübi lipud (`-md`, `-img`, `-nb`)
- Projektis pole sobivaid faile
- Vale kataloogistruktuur

**Lahendus:**
1. **Kasuta debug režiimi**, et näha, mis toimub:
   ```bash
   translate -l "ko" -md -d
   ```

2. **Kontrolli failitüüpe** oma projektis:
   ```bash
   # For markdown files
   find . -name "*.md" -not -path "./translations/*"
   
   # For notebooks
   find . -name "*.ipynb" -not -path "./translations/*"
   
   # For images
   find . -name "*.png" -o -name "*.jpg" -o -name "*.jpeg" -not -path "./translations/*"
   ```

3. **Kontrolli lippude kombinatsioone**:
   ```bash
   # Translate everything (default)
   translate -l "ko"
   
   # Translate specific types
   translate -l "ko" -md -img
   ```

## 6. Üleminek vanalt süsteemilt

### 6.1. Ainult-markdown režiim on aegunud

**Probleem:** Käsklused, mis tuginesid automaatsele markdown-only režiimile, enam ei tööta ootuspäraselt.

**Vana käitumine:**
```bash
# This used to automatically switch to markdown-only mode
translate -l "ko"  # (when Azure AI Vision was not configured)
```

**Uus käitumine:**
```bash
# This now produces an error if image translation is requested but not configured
translate -l "ko" -img
```

**Lahendus:**
- **Ole konkreetne**, mida soovid tõlkida:
  ```bash
  translate -l "ko" -md        # Only markdown
  translate -l "ko" -md -img   # Markdown and images
  translate -l "ko"            # Everything (if all services configured)
  ```

### 6.2. Ootamatu linkide käitumine

**Probleem:** Tõlgitud failide lingid viitavad ootamatutele asukohtadele.

**Põhjus:** Dünaamiline linkide töötlemine muutub vastavalt valitud failitüüpidele.

**Lahendus:**
1. **Mõista uut linkide käitumist**:
   - Kui `-nb` on kaasatud: märkmiku lingid viitavad tõlgitud versioonidele
   - Kui `-nb` pole kaasatud: märkmiku lingid viitavad originaalfailidele
   - Kui `-img` on kaasatud: pildilingid viitavad tõlgitud versioonidele
   - Kui `-img` pole kaasatud: pildilingid viitavad originaalfailidele

2. **Vali õige kombinatsioon** vastavalt oma vajadusele:
   ```bash
   # All internal links point to translated versions
   translate -l "ko" -md -img -nb
   
   # Only markdown translated, other links point to originals
   translate -l "ko" -md
   ```

## 7. GitHub Action käivitus, kuid Pull Requesti (PR) ei loodud

**Sümptom:** Töövoo logides `peter-evans/create-pull-request` näidatakse:

> Branch 'update-translations' is not ahead of base 'main' and will not be created

**Tõenäolised põhjused:**
- **Muudatusi ei tuvastatud:** Tõlkeetapp ei tekitanud erinevusi (repo juba ajakohane).
- **Väljundid ignoreeritud:** `.gitignore` välistab failid, mida soovid commit'ida (nt `*.ipynb`, `translations/`, `translated_images/`).
- **add-paths ei klapi:** Actionile antud teed ei vasta tegelikele väljundite asukohtadele.
- **Töövoo loogika/tingimused:** Tõlkeetapp lõpetas varem või kirjutas ootamatutesse kataloogidesse.

**Kuidas parandada / kontrollida:**
1. **Veendu, et väljundid on olemas:** Pärast tõlkimist kontrolli, et tööruumis on uusi/muudetud faile kaustades `translations/` ja/või `translated_images/`.
   - Kui tõlgid märkmikke, veendu, et `.ipynb` failid on kirjutatud kausta `translations/<lang>/...`.
2. **Vaata üle `.gitignore`:** Ära ignoreeri genereeritud väljundeid. Veendu, et EI ignoreeri:
   - `translations/`
   - `translated_images/`
   - `*.ipynb` (kui tõlgid märkmikke)
3. **Veendu, et add-paths klapib väljunditega:** Kasuta mitmerealist väärtust ja lisa mõlemad kaustad, kui vaja:
   ```yaml
   with:
     add-paths: |
       translations/
       translated_images/
   ```
4. **Sunni PR-i loomine silumiseks:** Luba ajutiselt tühjad commit'id, et kontrollida ühendusi:
   ```yaml
   with:
     commit-empty: true
   ```
5. **Käivita debug režiimis:** Lisa tõlke käsule `-d`, et näha, millised failid leiti ja kirjutati.
6. **Õigused (GITHUB_TOKEN):** Veendu, et töövoog lubab kirjutada commit'e ja PR-e:
   ```yaml
   permissions:
     contents: write
     pull-requests: write
   ```


## Kiire tõrkeotsingu kontrollnimekiri

Tõlkeprobleemide lahendamisel:

1. **Kasuta debug režiimi:** Lisa `-d` lipp, et näha detailseid logisid
2. **Kontrolli oma lippe:** Veendu, et `-md`, `-img`, `-nb` vastavad sinu soovile
3. **Kontrolli seadistust:** Veendu, et `.env` failis on vajalikud võtmed
4. **Testi järk-järgult:** Alusta ainult `-md`-ga, lisa hiljem teised tüübid
5. **Kontrolli failistruktuuri:** Veendu, et allikafailid on olemas ja ligipääsetavad

Lisainfo käskude ja lippude kohta leiad [Command Reference](./command-reference.md) lehelt.

---

**Vastutusest loobumine**:  
See dokument on tõlgitud tehisintellekti tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, tuleb arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Originaaldokumenti selle algses keeles tuleks pidada autoriteetseks allikaks. Kriitilise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgendamise eest.