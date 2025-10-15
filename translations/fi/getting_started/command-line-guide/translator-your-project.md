<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "20943a46b11c6d74814f41a817a6db4c",
  "translation_date": "2025-10-15T03:27:49+00:00",
  "source_file": "getting_started/command-line-guide/translator-your-project.md",
  "language_code": "fi"
}
-->
# Käännä projektisi Co-op Translatorilla

**Co-op Translator** on komentorivikäyttöliittymä (CLI) -työkalu, jonka avulla voit kääntää projektisi markdown- ja kuvatiedostot useille kielille. Tässä osiossa kerrotaan, miten työkalua käytetään, käydään läpi eri CLI-vaihtoehdot ja annetaan esimerkkejä eri käyttötapauksista.

> [!NOTE]
> Kaikki komennot ja niiden tarkat kuvaukset löydät [Komento-oppaasta](./command-reference.md).

---

## Esimerkkitilanteet ja komennot

Tässä muutamia yleisiä käyttötapauksia **Co-op Translatorille** sekä sopivat komennot niiden toteuttamiseen.

### 1. Peruskäännös (Yksi kieli)

Jos haluat kääntää koko projektisi (markdown-tiedostot ja kuvat) yhdelle kielelle, esimerkiksi koreaksi, käytä seuraavaa komentoa:

```bash
translate -l "ko"
```

Tämä komento kääntää kaikki markdown- ja kuvatiedostot koreaksi, lisäten uudet käännökset poistamatta olemassa olevia.

> [!TIP]
>
> Haluatko nähdä, mitkä kielikoodit ovat käytettävissä **Co-op Translatorissa**? Katso lisätietoja [Tuetut kielet](https://github.com/Azure/co-op-translator#supported-languages) -osiosta projektin repossa.

#### Esimerkki Phi-3 CookBookissa

**Phi-3 CookBookissa** käytin seuraavaa tapaa lisätäkseni koreankielisen käännöksen olemassa oleville markdown-tiedostoille ja kuville.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko"
Translating images: 100%|███████████████████████████████████████████████████| 276/276 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 153/153 [1:43:07<00:00, 241.31s/it]
```

### 2. Käännös useille kielille

Jos haluat kääntää projektisi useille kielille (esim. espanja, ranska ja saksa), käytä tätä komentoa:

```bash
translate -l "es fr de"
```

Tämä komento kääntää projektin espanjaksi, ranskaksi ja saksaksi, lisäten uudet käännökset korvaamatta olemassa olevia.

#### Esimerkki Phi-3 CookBookissa

**Phi-3 CookBookissa**, kun olin hakenut uusimmat muutokset vastaamaan viimeisimpiä committeja, käytin seuraavaa tapaa kääntääkseni juuri lisätyt markdown-tiedostot ja kuvat.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko ja zh tw es fr" -a
Translating images: 100%|███████████████████████████████████████████████████| 273/273 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 6/6 [24:07<00:00, 241.31s/it]
```

> [!NOTE]
> Yleisesti ottaen on suositeltavaa kääntää yksi kieli kerrallaan, mutta tällaisissa tilanteissa, joissa tiettyjä muutoksia pitää lisätä, usean kielen kääntäminen kerralla voi olla tehokasta.

### 3. Käännösten päivittäminen (Poistaa olemassa olevat käännökset)

Jos haluat päivittää olemassa olevat käännökset (eli poistaa nykyiset käännökset ja korvata ne uusilla), käytä `-u`-vaihtoehtoa. Tämä poistaa kaikki valittujen kielten käännökset ja kääntää ne uudelleen.

```bash
translate -l "ko" -u
```

Varoitus: Tämä komento pyytää vahvistusta ennen kuin se poistaa olemassa olevat käännökset.

#### Esimerkki Phi-3 CookBookissa

**Phi-3 CookBookissa** käytin seuraavaa tapaa päivittääkseni kaikki espanjankieliset käännetyt tiedostot. Suosittelen tätä tapaa, kun alkuperäiseen sisältöön on tullut merkittäviä muutoksia useissa markdown-dokumenteissa. Jos päivitettäviä käännettyjä tiedostoja on vain muutama, on tehokkaampaa poistaa ne manuaalisesti ja käyttää sitten `-a`-tapaa lisätäksesi päivitetyt käännökset.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "es" -u
Warning: The update command will delete all existing translations for 'es' and re-translate everything.
Do you want to continue? Type 'yes' to proceed: yes
Proceeding with update...
Translating images: 100%|████████████████████████████████████████████| 150/150 [43:46<00:00, 15.55s/it]
Translating markdown files: 100%|███████████████████████████████████| 95/95 [1:40:27<00:00, 125.62s/it]
```

### 5. Vain kuvien kääntäminen

Jos haluat kääntää vain projektisi kuvatiedostot, käytä `-img`-vaihtoehtoa:

```bash
translate -l "ko" -img
```

Tämä komento kääntää vain kuvat koreaksi, eikä vaikuta markdown-tiedostoihin.

### 6. Vain markdown-tiedostojen kääntäminen

Jos haluat kääntää vain projektisi markdown-tiedostot, käytä `-md`-vaihtoehtoa:

```bash
translate -l "ko" -md
```

#### Esimerkki Phi-3 CookBookissa

**Phi-3 CookBookissa** käytin seuraavaa tapaa tarkistaakseni käännösvirheet koreankielisissä tiedostoissa ja automaattisesti yrittääkseni käännöstä uudelleen niille tiedostoille, joissa havaittiin ongelmia.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko" -chk 
Checking translated files for errors in ko...
Checking files for ko: 100%|██████████████████████████████████████████████████| 95/95 [00:01<00:00, 65.47file/s]
Retrying vsc-extension-quickstart.md for ko:   0%|                                     | 0/17 [00:00<?, ?file/s] 
```

Tämä vaihtoehto tarkistaa käännösvirheet. Tällä hetkellä, jos rivinvaihtojen ero alkuperäisen ja käännetyn tiedoston välillä on yli kuusi, tiedosto merkitään virheelliseksi. Aion parantaa tätä kriteeriä tulevaisuudessa joustavuuden lisäämiseksi.

Esimerkiksi tämä tapa on hyödyllinen puuttuvien osien tai vioittuneiden käännösten havaitsemiseen, ja se yrittää automaattisesti kääntää kyseiset tiedostot uudelleen.

Jos kuitenkin jo tiedät, mitkä tiedostot ovat ongelmallisia, on tehokkaampaa poistaa ne manuaalisesti ja käyttää `-a`-vaihtoehtoa niiden uudelleenkääntämiseen.

### 8. Debug-tila

Jos haluat ottaa käyttöön yksityiskohtaisen lokituksen vianetsintää varten, käytä `-d`-vaihtoehtoa:

```bash
translate -l "ko" -d
```

Tämä komento suorittaa käännöksen debug-tilassa, tarjoten lisätietoja lokiin, jotka auttavat tunnistamaan ongelmia käännösprosessin aikana.

#### Esimerkki Phi-3 CookBookissa

**Phi-3 CookBookissa** kohtasin ongelman, jossa markdown-tiedostoissa olevat lukuisat linkit aiheuttivat muotoiluvirheitä, kuten rikkoutuneita käännöksiä ja ohitettuja rivinvaihtoja. Tämän ongelman diagnosoimiseksi käytin `-d`-vaihtoehtoa nähdäkseni, miten käännösprosessi toimi.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "ko" -d
DEBUG:openai._base_client:Request options: {'method': 'post', 'url': '/chat/completions', 'headers': {'api-key': 'af04e0bea45747d8a7b8c131c1971044'}, 'files': None, 'json_data': {'messages': [{'role': 'user', 'content': "Translate the following text to ko. NEVER ADD ANY EXTRA CONTENT OUTSIDE THE TRANSLATION. TRANSLATE ONLY WHAT IS GIVEN TO YOU.. MAINTAIN MARKDOWN FORMAT\n\n# Phi-3 Cookbook: Hands-On Examples with Microsoft's Phi-3 Models [![Open and use the samples in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phi-3cookbook) [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%
...
```

### 9. Kaikkien kielten kääntäminen

Jos haluat kääntää projektin kaikille tuetuille kielille, käytä all-avainsanaa.

> [!WARNING]
> Kaikkien kielten kääntäminen kerralla voi viedä paljon aikaa projektin koosta riippuen. Esimerkiksi **Phi-3 CookBookin** kääntäminen espanjaksi vei noin 2 tuntia. Tämän mittakaavan vuoksi ei ole käytännöllistä, että yksi henkilö hoitaa 20 kieltä. Suositeltavaa on jakaa työ useiden tekijöiden kesken, kukin hoitaa yhden tai kaksi kieltä, ja päivittää käännöksiä vähitellen.

```bash
translate -l "all"
```

Tämä komento kääntää projektin kaikille saatavilla oleville kielille. Jos jatkat, käännös voi kestää kauan projektin koosta riippuen.

> [!TIP]
>
> ### Käännettyjen tiedostojen manuaalinen poistaminen (valinnainen)
> Käännetyt tiedostot tunnistetaan ja siivotaan nyt automaattisesti, kun lähdetiedosto päivittyy.
>
> Jos kuitenkin haluat päivittää käännöksen manuaalisesti – esimerkiksi tehdä tietyn tiedoston uudelleen tai ohittaa järjestelmän oletuskäytöksen – voit käyttää seuraavaa komentoa poistaaksesi kaikki tiedoston versiot kielikansioista.
>
> ### Windowsissa:
> 1. **Komentokehotteen käyttö**:
>    - Avaa komentokehote.
>    - Siirry kansioon, jossa tiedostot ovat, käyttämällä `cd`-komentoa.
>    - Käytä seuraavaa komentoa tiedostojen poistamiseen:
>      ```
>      del /s *filename*
>      ```
>      Korvaa `filename` tiedoston nimellä, jota etsit. `/s`-vaihtoehto etsii myös alikansioista.
>
> 2. **PowerShellin käyttö**:
>    - Avaa PowerShell.
>    - Suorita tämä komento:
>      ```powershell
>      Get-ChildItem -Path "C:\YourPath" -Filter "*filename*" -Recurse | Remove-Item -Force
>      ```
>      Korvaa `"C:\YourPath"` kansiopolulla ja `filename` tiedoston nimellä.
>
> ### macOS/Linuxissa:
> 1. **Terminaalin käyttö**:
>   - Avaa terminaali.
>   - Siirry hakemistoon `cd`-komennolla.
>   - Käytä `find`-komentoa:
>     ```bash
>     find . -type f -name "*filename*" -delete
>     ```
>     Korvaa `filename` tiedoston nimellä.
>
> Tarkista aina tiedostot ennen poistamista, jotta et vahingossa poista väärää sisältöä.
>
> Kun olet poistanut tiedostot, jotka haluat korvata, suorita uudelleen `translate -l`-komento päivittääksesi uusimmat tiedostomuutokset.

---

**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulee pitää ensisijaisena lähteenä. Kriittisissä tapauksissa suositellaan ammattimaista ihmiskääntäjää. Emme ole vastuussa tämän käännöksen käytöstä mahdollisesti aiheutuvista väärinkäsityksistä tai tulkintavirheistä.