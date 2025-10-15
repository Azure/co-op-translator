<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6e626bef5ed78a1cc55b0dbf44f01d47",
  "translation_date": "2025-10-15T03:27:22+00:00",
  "source_file": "getting_started/troubleshooting.md",
  "language_code": "fi"
}
-->
# Microsoft Co-op Translator - Vianmääritysohje

## Yleiskatsaus
Microsoft Co-Op Translator on tehokas työkalu Markdown-dokumenttien kääntämiseen vaivattomasti. Tämä ohje auttaa sinua ratkaisemaan yleisimmät ongelmat, joita työkalua käyttäessä voi tulla vastaan.

## Yleiset ongelmat ja ratkaisut

### 1. Markdown-tagin ongelma
**Ongelma:** Käännetyn Markdown-tiedoston alussa on `markdown`-tagi, joka aiheuttaa renderöintiongelmia.

**Ratkaisu:** Poista tiedoston alusta `markdown`-tagi. Tämän jälkeen Markdown-tiedosto näkyy oikein.

**Vaiheet:**
1. Avaa käännetty Markdown (`.md`)-tiedosto.
2. Etsi dokumentin alusta `markdown`-tagi.
3. Poista kyseinen tagi.
4. Tallenna tiedosto.
5. Avaa tiedosto uudelleen ja varmista, että se näkyy oikein.

### 2. Upotettujen kuvien URL-ongelma
**Ongelma:** Upotettujen kuvien URL-osoitteet eivät vastaa kielilokaalia, jolloin kuvat näkyvät väärin tai puuttuvat.

**Ratkaisu:** Tarkista upotettujen kuvien URL-osoitteet ja varmista, että ne vastaavat dokumentin kielilokaalia. Kaikki kuvat löytyvät `translated_images`-kansiosta, ja jokaisessa kuvatiedoston nimessä on kielilokaali.

**Vaiheet:**
1. Avaa käännetty Markdown-dokumentti.
2. Etsi upotetut kuvat ja niiden URL-osoitteet.
3. Varmista, että kuvatiedoston nimessä oleva kielilokaali vastaa dokumentin kieltä.
4. Päivitä URL-osoitteet tarvittaessa.
5. Tallenna muutokset ja avaa dokumentti uudelleen varmistaaksesi, että kuvat näkyvät oikein.

### 3. Käännöksen tarkkuus
**Ongelma:** Käännetty sisältö ei ole tarkka tai vaatii lisämuokkauksia.

**Ratkaisu:** Tarkista käännetty dokumentti ja tee tarvittavat muokkaukset, jotta käännös on tarkempi ja luettavampi.

**Vaiheet:**
1. Avaa käännetty dokumentti.
2. Lue sisältö huolellisesti läpi.
3. Tee tarvittavat muokkaukset käännöksen parantamiseksi.
4. Tallenna muutokset.

## 4. Lupaongelma: Redacted tai 404

Jos kuvat tai teksti eivät käänny oikealle kielelle ja debug-tilassa (-d) saat 401-virheen, kyseessä on tyypillinen tunnistautumisongelma—avain on joko virheellinen, vanhentunut tai ei liity oikeaan päätepisteen alueeseen.

Aja co-op translator [-d debug switch](https://github.com/Azure/co-op-translator/blob/main/getting_started/command-reference.md) -valinnalla saadaksesi lisätietoa ongelman syystä.

- **Virheilmoitus**: `Access denied due to invalid subscription key or wrong API endpoint.`
- **Mahdollisia syitä**:
  - Tilauksen avain on peitetty tai virheellinen pyynnössä.
  - AI Services Key tai Subscription Key kuuluu eri Azure-resurssiin (esim. Translator tai OpenAI) eikä **Azure AI Vision** -resurssiin.

 **Resurssityyppi**
  - Mene [Azure Portal](https://portal.azure.com) tai [Azure AI Foundry](https://ai.azure.com) ja varmista, että resurssityyppi on `Azure AI services` → `Vision`.
  - Varmista avaimet ja käytä oikeaa avainta.

## 5. Konfiguraatiovirheet (Uusi virheenkäsittely)

Uuden valikoivan käännösjärjestelmän myötä Co-op Translator antaa nyt selkeät virheilmoitukset, jos vaadittuja palveluita ei ole konfiguroitu.

### 5.1. Azure AI Service ei konfiguroitu kuvakäännökselle

**Ongelma:** Pyysit kuvakäännöstä (`-img`-lippu), mutta Azure AI Service ei ole kunnolla konfiguroitu.

**Virheilmoitus:**
```
Error: Image translation requested but Azure AI Service is not configured.
Please add AZURE_AI_SERVICE_API_KEY and AZURE_AI_SERVICE_ENDPOINT to your .env file.
Check Azure AI Service availability and configuration.
```

**Ratkaisu:**
1. **Vaihtoehto 1**: Konfiguroi Azure AI Service
   - Lisää `AZURE_AI_SERVICE_API_KEY` `.env`-tiedostoon
   - Lisää `AZURE_AI_SERVICE_ENDPOINT` `.env`-tiedostoon
   - Varmista, että palvelu on käytettävissä

2. **Vaihtoehto 2**: Poista kuvakäännöspyyntö
   ```bash
   # Instead of: translate -l "ko" -img
   # Use: translate -l "ko" -md
   ```

### 5.2. Vaadittu konfiguraatio puuttuu

**Ongelma:** Oleellinen LLM-konfiguraatio puuttuu.

**Virheilmoitus:**
```
Error: No language model configuration found.
Please configure either Azure OpenAI or OpenAI in your .env file.
```

**Ratkaisu:**
1. Varmista, että `.env`-tiedostossa on vähintään yksi seuraavista LLM-konfiguraatioista:
   - **Azure OpenAI**: `AZURE_OPENAI_API_KEY` ja `AZURE_OPENAI_ENDPOINT`
   - **OpenAI**: `OPENAI_API_KEY`
   
   Sinulla tulee olla joko Azure OpenAI TAI OpenAI konfiguroituna, ei molempia.

### 5.3. Valikoivan käännöksen hämmennys

**Ongelma:** Yhtään tiedostoa ei käännetty, vaikka komento onnistui.

**Mahdollisia syitä:**
- Väärät tiedostotyyppiliput (`-md`, `-img`, `-nb`)
- Projektissa ei ole sopivia tiedostoja
- Väärä hakemistorakenne

**Ratkaisu:**
1. **Käytä debug-tilaa** nähdäksesi, mitä tapahtuu:
   ```bash
   translate -l "ko" -md -d
   ```

2. **Tarkista tiedostotyypit** projektissasi:
   ```bash
   # For markdown files
   find . -name "*.md" -not -path "./translations/*"
   
   # For notebooks
   find . -name "*.ipynb" -not -path "./translations/*"
   
   # For images
   find . -name "*.png" -o -name "*.jpg" -o -name "*.jpeg" -not -path "./translations/*"
   ```

3. **Varmista lippuyhdistelmät**:
   ```bash
   # Translate everything (default)
   translate -l "ko"
   
   # Translate specific types
   translate -l "ko" -md -img
   ```

## 6. Siirtyminen vanhasta järjestelmästä

### 6.1. Markdown-only-tila poistettu käytöstä

**Ongelma:** Komennot, jotka perustuivat automaattiseen markdown-only-varmistukseen, eivät enää toimi odotetusti.

**Vanha toiminta:**
```bash
# This used to automatically switch to markdown-only mode
translate -l "ko"  # (when Azure AI Vision was not configured)
```

**Uusi toiminta:**
```bash
# This now produces an error if image translation is requested but not configured
translate -l "ko" -img
```

**Ratkaisu:**
- **Ole selkeä** siitä, mitä haluat kääntää:
  ```bash
  translate -l "ko" -md        # Only markdown
  translate -l "ko" -md -img   # Markdown and images
  translate -l "ko"            # Everything (if all services configured)
  ```

### 6.2. Odottamaton linkkien toiminta

**Ongelma:** Käännettyjen tiedostojen linkit osoittavat odottamattomiin paikkoihin.

**Syy:** Dynaaminen linkkien käsittely muuttuu valittujen tiedostotyyppien mukaan.

**Ratkaisu:**
1. **Ymmärrä uusi linkkien toiminta**:
   - `-nb` mukana: Notebook-linkit osoittavat käännettyihin versioihin
   - `-nb` pois: Notebook-linkit osoittavat alkuperäisiin tiedostoihin
   - `-img` mukana: Kuvien linkit osoittavat käännettyihin versioihin
   - `-img` pois: Kuvien linkit osoittavat alkuperäisiin tiedostoihin

2. **Valitse oikea yhdistelmä** käyttötarpeesi mukaan:
   ```bash
   # All internal links point to translated versions
   translate -l "ko" -md -img -nb
   
   # Only markdown translated, other links point to originals
   translate -l "ko" -md
   ```

## 7. GitHub Action suoritettiin, mutta Pull Requestia (PR) ei luotu

**Oire:** `peter-evans/create-pull-request`-työnkulun lokit näyttävät:

> Branch 'update-translations' is not ahead of base 'main' and will not be created

**Todennäköisiä syitä:**
- **Ei muutoksia havaittu:** Käännösvaihe ei tuottanut eroja (repo jo ajan tasalla).
- **Ohitetut tulosteet:** `.gitignore` sulkee pois tiedostoja, jotka haluaisit commitoida (esim. `*.ipynb`, `translations/`, `translated_images/`).
- **add-paths ei täsmää:** Actionille annetut polut eivät vastaa todellisia tulostepaikkoja.
- **Työnkulun logiikka/ehdot:** Käännösvaihe päättyi aikaisin tai kirjoitti odottamattomiin hakemistoihin.

**Näin korjaat / varmistat:**
1. **Varmista, että tulosteita on:** Käännöksen jälkeen workspace sisältää uusia/muuttuneita tiedostoja kansioissa `translations/` ja/tai `translated_images/`.
   - Jos käännät notebookeja, varmista että `.ipynb`-tiedostot kirjoitetaan polkuun `translations/<lang>/...`.
2. **Tarkista `.gitignore`:** Älä ohita generoituja tulosteita. Varmista, että ET ohita:
   - `translations/`
   - `translated_images/`
   - `*.ipynb` (jos käännät notebookeja)
3. **Varmista, että add-paths vastaa tulosteita:** Käytä monirivistä arvoa ja sisällytä molemmat kansiot tarvittaessa:
   ```yaml
   with:
     add-paths: |
       translations/
       translated_images/
   ```
4. **Pakota PR debuggausta varten:** Salli tilapäisesti tyhjät commitit varmistaaksesi, että kytkentä toimii:
   ```yaml
   with:
     commit-empty: true
   ```
5. **Aja debug-tilassa:** Lisää `-d` käännöskomentoon, jotta näet, mitkä tiedostot löydettiin ja kirjoitettiin.
6. **Oikeudet (GITHUB_TOKEN):** Varmista, että työnkululla on kirjoitusoikeudet commitien ja PR:ien luomiseen:
   ```yaml
   permissions:
     contents: write
     pull-requests: write
   ```

## Pikainen vianmäärityksen tarkistuslista

Kun selvität käännösongelmia:

1. **Käytä debug-tilaa:** Lisää `-d`-lippu nähdäksesi tarkemmat lokit
2. **Tarkista lippusi:** Varmista, että `-md`, `-img`, `-nb` vastaavat tarkoitustasi
3. **Varmista konfiguraatio:** Tarkista, että `.env`-tiedostossa on tarvittavat avaimet
4. **Testaa vaiheittain:** Aloita pelkällä `-md`:llä, lisää sitten muita tyyppejä
5. **Tarkista tiedostorakenne:** Varmista, että lähdetiedostot ovat olemassa ja käytettävissä

Lisätietoja komennoista ja lipuista löydät [Command Reference](./command-reference.md) -dokumentista.

---

**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulee pitää ensisijaisena lähteenä. Kriittisissä tapauksissa suositellaan ammattimaista ihmiskääntäjää. Emme ole vastuussa tämän käännöksen käytöstä mahdollisesti aiheutuvista väärinkäsityksistä tai tulkintavirheistä.