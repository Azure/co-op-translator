<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d238206c3503631e32774716d11d1868",
  "translation_date": "2025-06-12T18:51:04+00:00",
  "source_file": "getting_started/command-line-guide/translator-your-project.md",
  "language_code": "fi"
}
-->
# Käännä projektisi Co-op Translatorilla

**Co-op Translator** on komentorivityökalu (CLI), joka auttaa sinua kääntämään projektisi markdown- ja kuv tiedostot useille kielille. Tässä osiossa selitetään, miten työkalua käytetään, käydään läpi eri CLI-vaihtoehdot ja annetaan esimerkkejä erilaisista käyttötapauksista.

> [!NOTE]
> Täydellisen komentoluettelon ja yksityiskohtaiset kuvaukset löydät kohdasta [Command reference](./command-reference.md).

---

## Esimerkkitilanteet ja komennot

Tässä muutamia yleisiä käyttötapauksia **Co-op Translatorille** sekä niihin sopivat komennot.

### 1. Peruskäännös (yksi kieli)

Kääntääksesi koko projektisi (markdown-tiedostot ja kuvat) yhdelle kielelle, esimerkiksi koreaksi, käytä seuraavaa komentoa:

```bash
translate -l "ko"
```

Tämä komento kääntää kaikki markdown- ja kuvatiedostot koreaksi lisäämällä uudet käännökset ilman, että olemassa olevia poistetaan.

> [!TIP]
>
> Haluatko nähdä, mitä kielikoodeja **Co-op Translator** tukee? Katso lisätietoja [Supported Languages](https://github.com/Azure/co-op-translator#supported-languages) -osiosta repositoriossa.

#### Esimerkki Phi-3 CookBookista

**Phi-3 CookBookissa** käytin seuraavaa menetelmää lisätäkseni koreankielisen käännöksen olemassa oleviin markdown-tiedostoihin ja kuviin.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko"
Translating images: 100%|███████████████████████████████████████████████████| 276/276 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 153/153 [1:43:07<00:00, 241.31s/it]
```

### 2. Useamman kielen kääntäminen

Kääntääksesi projektin usealle kielelle (esim. espanja, ranska ja saksa), käytä tätä komentoa:

```bash
translate -l "es fr de"
```

Tämä komento kääntää projektin espanjaksi, ranskaksi ja saksaksi, lisäten uudet käännökset ilman, että olemassa olevia ylikirjoitetaan.

#### Esimerkki Phi-3 CookBookista

**Phi-3 CookBookissa**, kun olin hakenut viimeisimmät muutokset heijastamaan uusimpia commiteja, käytin seuraavaa menetelmää kääntääkseni vastikään lisätyt markdown-tiedostot ja kuvat.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko ja zh tw es fr" -a
Translating images: 100%|███████████████████████████████████████████████████| 273/273 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 6/6 [24:07<00:00, 241.31s/it]
```

> [!NOTE]
> Yleisesti on suositeltavaa kääntää yksi kieli kerrallaan, mutta tilanteissa kuten tämä, joissa tiettyjä muutoksia pitää lisätä, useamman kielen kääntäminen kerralla voi olla tehokasta.

### 3. Käännösten päivittäminen (poistaa olemassa olevat käännökset)

Päivittääksesi olemassa olevat käännökset (eli poistaa nykyiset käännökset ja korvata ne uusilla), käytä `-u` -valitsinta. Tämä poistaa kaikki määritettyjen kielten nykyiset käännökset ja kääntää ne uudelleen.

```bash
translate -l "ko" -u
```

Varoitus: Tämä komento kysyy vahvistuksen ennen kuin poistaa olemassa olevat käännökset.

#### Esimerkki Phi-3 CookBookista

**Phi-3 CookBookissa** käytin seuraavaa tapaa päivittääkseni kaikki espanjankieliset käännetyt tiedostot. Suosittelen tätä menetelmää, kun alkuperäisessä sisällössä on merkittäviä muutoksia useissa markdown-tiedostoissa. Jos päivitettäviä käännettyjä tiedostoja on vain muutama, on tehokkaampaa poistaa ne manuaalisesti ja käyttää sitten `-a` -menetelmää lisätäksesi päivitetyt käännökset.

### 5. Vain kuvien kääntäminen

Kääntääksesi vain projektin kuvatiedostot, käytä `-img` -valitsinta:

```bash
translate -l "ko" -img
```

Tämä komento kääntää vain kuvat koreaksi vaikuttamatta markdown-tiedostoihin.

### 6. Vain markdown-tiedostojen kääntäminen

Kääntääksesi vain projektin markdown-tiedostot, käytä `-md` -valitsinta:

```bash
translate -l "ko" -md
```

### 7. Käännettyjen tiedostojen virheiden tarkistus

Jos haluat tarkistaa käännetyt tiedostot virheiden varalta ja yrittää käännöstä uudelleen tarvittaessa, käytä `-chk` -valitsinta:

```bash
translate -l "ko" -chk
```

Tämä komento skannaa käännetyt markdown-tiedostot ja yrittää kääntää uudelleen ne tiedostot, joissa on virheitä.

#### Esimerkki Phi-3 CookBookista

**Phi-3 CookBookissa** käytin seuraavaa menetelmää tarkistaakseni koreankielisissä tiedostoissa käännösvirheitä ja automaattisesti yrittääkseni käännöstä uudelleen, jos ongelmia löytyi.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko" -chk 
Checking translated files for errors in ko...
Checking files for ko: 100%|██████████████████████████████████████████████████| 95/95 [00:01<00:00, 65.47file/s]
Retrying vsc-extension-quickstart.md for ko:   0%|                                     | 0/17 [00:00<?, ?file/s] 
```

Tämä valinta tarkistaa käännösvirheet. Tällä hetkellä, jos rivinvaihtojen ero alkuperäisen ja käännetyn tiedoston välillä on yli kuusi, tiedosto merkitään käännösvirheelliseksi. Aion parantaa tätä kriteeriä tulevaisuudessa joustavamman tarkistuksen mahdollistamiseksi.

Esimerkiksi tämä menetelmä on hyödyllinen puuttuvien osien tai vioittuneiden käännösten havaitsemiseen, ja se yrittää automaattisesti kääntää ne tiedostot uudelleen.

Jos kuitenkin tiedät jo, mitkä tiedostot ovat ongelmallisia, on tehokkaampaa poistaa ne manuaalisesti ja käyttää `-a` option to re-translate them.

### 8. Debug Mode

To enable detailed logging for troubleshooting, use the `-d` -valitsinta:

```bash
translate -l "ko" -d
```

Tämä komento suorittaa käännöksen debug-tilassa, tarjoten lisälokitietoa, joka auttaa tunnistamaan ongelmia käännösprosessin aikana.

#### Esimerkki Phi-3 CookBookista

**Phi-3 CookBookissa** kohtasin ongelman, jossa paljon linkkejä sisältävät käännökset markdown-tiedostoissa aiheuttivat muotoiluvirheitä, kuten rikkoutuneita käännöksiä ja ohitettuja rivinvaihtoja. Tämän ongelman diagnosoimiseksi käytin `-d` -valitsinta nähdäkseni, miten käännösprosessi toimii.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "ko" -d
DEBUG:openai._base_client:Request options: {'method': 'post', 'url': '/chat/completions', 'headers': {'api-key': 'af04e0bea45747d8a7b8c131c1971044'}, 'files': None, 'json_data': {'messages': [{'role': 'user', 'content': "Translate the following text to ko. NEVER ADD ANY EXTRA CONTENT OUTSIDE THE TRANSLATION. TRANSLATE ONLY WHAT IS GIVEN TO YOU.. MAINTAIN MARKDOWN FORMAT\n\n# Phi-3 Cookbook: Hands-On Examples with Microsoft's Phi-3 Models [![Open and use the samples in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phi-3cookbook) [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%
...
```

### 9. Kaikkien kielten kääntäminen

Jos haluat kääntää projektin kaikille tuetuille kielille, käytä all-avainsanaa.

> [!WARNING]
> Kaikkien kielten kääntäminen kerralla voi viedä huomattavasti aikaa projektin koosta riippuen. Esimerkiksi **Phi-3 CookBookin** kääntäminen espanjaksi kesti noin 2 tuntia. Tämän mittakaavan vuoksi ei ole käytännöllistä, että yksi henkilö hoitaa 20 kieltä. On suositeltavaa jakaa työ useamman tekijän kesken, jokaisen hoitaessa yhtä tai kahta kieltä, ja päivittää käännökset vähitellen.

```bash
translate -l "all"
```

Tämä komento kääntää projektin kaikille saatavilla oleville kielille. Jos jatkat, kääntäminen voi viedä huomattavasti aikaa projektin koosta riippuen.

> [!TIP]
>
> ### Käännettyjen tiedostojen manuaalinen poistaminen (valinnainen)
> Käännetyt tiedostot tunnistetaan ja siivotaan nyt automaattisesti, kun lähdetiedostoa päivitetään.
>
> Jos kuitenkin haluat päivittää käännöksen manuaalisesti – esimerkiksi tehdä uudelleen tietyn tiedoston tai ohittaa järjestelmän toiminnan – voit käyttää seuraavaa komentoa poistaaksesi tiedoston kaikki versiot kielikansioista.
>
> ### Windowsissa:
> 1. **Komentokehotteen käyttäminen**:
>    - Avaa komentokehote.
>    - Siirry kansioon, jossa tiedostot sijaitsevat, käyttämällä `cd`-komentoa.
>    - Käytä seuraavaa komentoa tiedostojen poistamiseen:
>      ```
>      del /s *filename*
>      ```
>      Vaihtoehto `/s` hakee myös alikansiot.
>
> 2. **PowerShellin käyttäminen**:
>    - Avaa PowerShell.
>    - Suorita tämä komento:
>      ```powershell
>      Get-ChildItem -Path "C:\YourPath" -Filter "*filename*" -Recurse | Remove-Item -Force
>      ```
>      Korvaa `"C:\YourPath"` with the folder path and `filename` with the specific name.
>
> ### On macOS/Linux:
> 1. **Using Terminal**:
>   - Open Terminal.
>   - Navigate to the directory with `cd`.
>   - Use the `find` -komento:
>     ```bash
>     find . -type f -name "*filename*" -delete
>     ```
>     Korvaa `filename` with the specific name.
>
> Always double-check the files before deleting to avoid accidental loss. 
>
> Once you have deleted the files which need to be replace simply rerun your `translate -l` -komento päivittääksesi uusimmat tiedostomuutokset.

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Pyrimme tarkkuuteen, mutta huomioithan, että automaattikäännöksissä voi esiintyä virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä tiedoissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä johtuvista väärinymmärryksistä tai tulkinnoista.