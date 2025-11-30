<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "93a7150216aa3c2d191135358fa6dd21",
  "translation_date": "2025-11-30T13:46:01+00:00",
  "source_file": "getting_started/update-other-courses.md",
  "language_code": "fi"
}
-->
# Päivitä "Muut kurssit" -osio (Microsoft Beginners -repositoriot)

Tämä ohje selittää, miten "Muut kurssit" -osio synkronoidaan automaattisesti Co-op Translatorin avulla ja miten päivitetään globaali malli kaikille repositorioille.

- Soveltuu: Vain Microsoft Beginners -repositorioihin
- Toimii: Co-op Translator CLI:n ja GitHub Actionsin kanssa
- Mallin lähde: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## Nopeasti alkuun: Ota automaattinen synkronointi käyttöön repositoriossasi

Lisää seuraavat merkit "Muut kurssit" -osion ympärille README-tiedostossasi. Co-op Translator korvaa kaiken näiden merkkien välissä jokaisella suorituskerralla.

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

Joka kerta kun Co-op Translator suoritetaan — joko CLI:n kautta (esim. `translate -l "<language codes>"`) tai GitHub Actionsissa — se päivittää automaattisesti "Muut kurssit" -osion, joka on kääritty näiden merkkien sisään.

> [!NOTE]
> Jos sinulla on jo olemassa oleva lista, kääri se vain samoilla merkeillä. Seuraava suoritus korvaa sen uusimmalla standardoidulla sisällöllä.

---

## Miten muuttaa globaalia sisältöä

Jos haluat päivittää standardoidun sisällön, joka näkyy kaikissa Beginners-repositorioissa:

1. Muokkaa mallia: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)
2. Avaa pull request Co-op Translator -repositorioon muutoksillasi
3. Kun PR on yhdistetty, Co-op Translatorin versio päivittyy
4. Seuraavan kerran kun Co-op Translator suoritetaan (CLI:llä tai GitHub Actionissa) kohderepositoriossa, se synkronoi automaattisesti päivitetyn osion

Tämä varmistaa yhden totuuden lähteen "Muut kurssit" -sisällölle kaikissa Beginners-repositorioissa.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattikäännöksissä saattaa esiintyä virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäiskielellä tulee pitää virallisena lähteenä. Tärkeissä tiedoissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->