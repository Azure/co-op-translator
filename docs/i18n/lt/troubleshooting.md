# Trikčių šalinimas

Naudokite šį puslapį, kai vertimo paleidimas netikėtai pavyksta, nepavyksta konfigūracijos metu arba sukuria išvestį, kurią reikia peržiūrėti.

## Pradėkite čia

1. Pirmiausia paleiskite susitelktą komandą, pavyzdžiui `translate -l "ko" -md`.
2. Pridėkite `-d` konsolės derinimo žurnalui.
3. Pridėkite `-s`, kad išsaugotumėte derinimo žurnalus kataloge `<root-dir>/logs/`.
4. Paleiskite `co-op-review` po vertimo, kad patikrintumėte šviežumą, struktūrą ir vietines nuorodas.

```bash
translate -l "ko" -md -d -s
co-op-review -l "ko"
```

## Konfigūracijos klaidos

### Nėra kalbos modelio teikėjo

Klaida:

```text
No language model configuration found.
```

Sprendimas:

- Konfigūruokite Azure OpenAI arba OpenAI.
- Patikrinkite, ar kintamieji yra aplinkoje, kur paleidžiama komanda.
- Vietiniam naudojimui įdėkite juos į `.env` projekto šaknyje.

Žr. [Konfigūracija](configuration.md).

### Vaizdų vertimas be Azure AI Vision

Klaida:

```text
Image translation requested but Azure AI Service is not configured.
```

Sprendimas:

- Pridėkite `AZURE_AI_SERVICE_API_KEY`.
- Pridėkite `AZURE_AI_SERVICE_ENDPOINT`.
- Arba vykdykite tik tekstui skirtą komandą, pvz., `translate -l "ko" -md`.

### Neteisingas raktas arba galinio taško adresas

Simptomai gali apimti `401`, užmaskuotas leidimų klaidas arba prieigos prie galinio taško klaidas.

Sprendimas:

- Patvirtinkite, kad raktas priklauso tam pačiam Azure ištekliui kaip ir galinis taškas.
- Patvirtinkite, kad išteklius palaiko Vision naudojant `-img`.
- Patvirtinkite, kad Azure OpenAI diegimo pavadinimas ir API versija atitinka jūsų diegimą.
- Paleiskite su derinimo žurnalais: `translate -l "ko" -md -d -s`.

## Nei vienas failas nebuvo išverstas

Dažnos priežastys:

- Pasirinktos vėliavėlės neatitinka jūsų failų.
- Jau yra esami išversti failai.
- Šaltinio failai yra išimtų katalogų viduje.
- Komanda paleista ne iš projekto šaknies.

Patikrinimai:

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -nb --dry-run
translate -l "ko" -img --dry-run
```

Naudokite `--root-dir`, kai komanda paleidžiama ne iš projekto šaknies.

## Netikėtas nuorodų elgesys

Nuorodų perrašymas priklauso nuo pasirinktų turinio tipų:

- `-nb` įtraukta: užrašomos nuorodos į užrašytus (notebook) failus gali nukreipti į išverstus užrašus.
- `-nb` neįtraukta: užrašų nuorodos gali likti nukreiptos į šaltinio užrašus.
- `-img` įtraukta: paveikslėlių nuorodos gali nukreipti į išverstus paveikslėlius.
- `-img` neįtraukta: paveikslėlių nuorodos gali likti nukreiptos į šaltinio paveikslėlius.

Paleiskite pilną turinio vertimą, kai visos vidinės nuorodos turėtų teikti pirmenybę išverstoms išvestims:

```bash
translate -l "ko" -md -nb -img
```

Paleiskite nuorodų peržiūrą po vertimo:

```bash
co-op-review -l "ko"
```

## Markdown atvaizdavimo problemos

Jei išverstasis Markdown atvaizduojamas neteisingai:

- Patikrinkite, ar frontmatter prasideda ir baigiasi `---`.
- Patikrinkite, ar kodo blokų ribojimo žymų skaičius sutampa tarp šaltinio ir išverstų failų.
- Paleiskite `co-op-review`, kad aptiktumėte bendras struktūros problemas.
- Išversti tą konkretų failą iš naujo, jei išvestis buvo sugadinta.

```bash
co-op-review -l "ko" --format github
```

## GitHub Action paleistas, bet nebuvo sukurtas Pull Request

Jei `peter-evans/create-pull-request` praneša, kad šaka nėra priekyje lyginant su baze, darbo eiga nerado failų, kuriuos būtų galima įsipareigoti.

Tikėtinos priežastys:

- Vertimo paleidimas nepagamino pakeitimų.
- `.gitignore` ignoruoja `translations/`, `translated_images/` arba išverstus užrašus.
- `add-paths` neatitinka sugeneruotų išvesties katalogų.
- Vertimo žingsnis baigėsi anksti.

Sprendimai:

1. Patvirtinkite, kad sugeneruoti failai yra `translations/` arba `translated_images/`.
2. Patvirtinkite, kad `.gitignore` neignoruoti sugeneruotų išvestų.
3. Naudokite atitinkančius `add-paths`:

   ```yaml
   with:
     add-paths: |
       translations/
       translated_images/
   ```

4. Laikinai pridėkite derinimo vėliavėles prie translate komandos:

   ```bash
   translate -l "ko" -md -d -s
   ```

5. Patvirtinkite, kad darbo eigos leidimai apima:

   ```yaml
   permissions:
     contents: write
     pull-requests: write
   ```

## Vertimo kokybė

Mašinų vertimai gali reikalauti žmogaus peržiūros. Naudokite `evaluate` tik tada, kai norite eksperimentinio kokybės vertinimo ir mažos pasitikėjimo taisymo darbo eigos.

!!! warning "Experimental"
    `evaluate` gali naudoti taisyklių pagrindu ir LLM pagrindu veikiančius patikrinimus, o jo vertinimo modelis ir metaduomenų elgsena gali keistis. Laikykite jį už reikalaujamų CI vartų, nebent jūsų darbo eiga yra pasiruošusi pokyčiams.

Vietoj to, deterministiniams CI patikrinimams naudokite `co-op-review`.