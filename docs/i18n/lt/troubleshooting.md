# Trikčių šalinimas

Naudokite šį puslapį, jei vertimo vykdymas netikėtai pavyksta, nepavyksta konfigūracijos metu arba sukuria rezultatą, kurį reikia peržiūrėti.

## Pradžia

1. Pirmiausia paleiskite konkrečią komandą, pvz., `translate -l "ko" -md`.
2. Pridėkite `-d` konsolės derinimo žurnalams.
3. Pridėkite `-s`, kad išsaugotumėte derinimo žurnalus kataloge `<root-dir>/logs/`.
4. Po vertimo paleiskite `co-op-review`, kad patikrintumėte šviežumą, struktūrą ir vietinius saitus.

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

- Konfigūruokite Azure OpenAI, OpenAI arba Anthropic.
- Patikrinkite, ar kintamieji yra aplinkoje, iš kurios vykdoma komanda.
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
- Arba paleiskite tik teksto komandą, pvz., `translate -l "ko" -md`.

### Neteisingas raktas arba galinis taškas

Simptomai gali būti `401`, užmaskuotos leidimų klaidos arba galinio taško prieigos klaidos.

Sprendimas:

- Patikrinkite, ar raktas priklauso tam pačiam Azure ištekliui kaip ir galinis taškas.
- Patikrinkite, ar išteklius palaiko Vision, kai naudojamas `-img`.
- Patikrinkite, ar Azure OpenAI diegimo pavadinimas ir API versija atitinka jūsų diegimą.
- Paleiskite su derinimo žurnalais: `translate -l "ko" -md -d -s`.

## Nėra išverstų failų

Dažnos priežastys:

- Pasirinkti parametrai neatitinka jūsų failų.
- Išverstų failų jau yra.
- Šaltinio failai yra pašalintuose kataloguose.
- Komanda paleista iš neteisingos projekto šaknies.

Patikrinimai:

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -nb --dry-run
translate -l "ko" -img --dry-run
```

Naudokite `--root-dir`, kai komanda vykdoma ne iš projekto šaknies.

## Netikėtas nuorodų elgesys

Nuorodų perrašymas priklauso nuo pasirinktų turinio tipų:

- `-nb` įtraukta: užrašų (notebook) nuorodos gali rodyti į išverstus užrašus.
- `-nb` neįtraukta: užrašų nuorodos gali likti nukreiptos į originalius užrašus.
- `-img` įtraukta: vaizdų nuorodos gali rodyti į išverstus vaizdus.
- `-img` neįtraukta: vaizdų nuorodos gali likti nukreiptos į originalius vaizdus.

Vykdykite pilną turinio vertimą, kai visos vidinės nuorodos turėtų pirmenybę teikti išverstiems rezultatams:

```bash
translate -l "ko" -md -nb -img
```

Paleiskite nuorodų peržiūrą po vertimo:

```bash
co-op-review -l "ko"
```

## Markdown atvaizdavimo problemos

Jei išverstas Markdown atvaizduojamas neteisingai:

- Patikrinkite, ar frontmatter prasideda ir baigiasi su `---`.
- Patikrinkite, ar kodo skyriklių skaičius sutampa tarp šaltinio ir išverstų failų.
- Paleiskite `co-op-review`, kad aptiktumėte dažnas struktūros problemas.
- Išverskite konkretų failą iš naujo, jei rezultatas buvo sugadintas.

```bash
co-op-review -l "ko" --format github
```

## GitHub veiksmas paleistas, bet nebuvo sukurtas Pull Request

Jei `peter-evans/create-pull-request` praneša, kad šaka nėra pažengusi prieš pagrindinę, darbo eiga nerado failų, kuriuos būtų galima įsipareigoti.

Tikėtinos priežastys:

- Vertimo vykdymas nepagamino jokių pakeitimų.
- `.gitignore` išskiria `translations/`, `translated_images/` arba išverstus užrašus.
- `add-paths` neatitinka sugeneruotų išvesties katalogų.
- Vertimo žingsnis baigėsi anksčiau nei planuota.

Sprendimai:

1. Patvirtinkite, kad sugeneruoti failai egzistuoja `translations/` arba `translated_images/`.
2. Patikrinkite, kad `.gitignore` neignoruotų sugeneruotų išvestinių failų.
3. Naudokite atitinkančius `add-paths`:

   ```yaml
   with:
     add-paths: |
       translations/
       translated_images/
   ```

4. Laikinai pridėkite derinimo parinktis prie translate komandos:

   ```bash
   translate -l "ko" -md -d -s
   ```

5. Patikrinkite, ar darbo eigos leidimai apima:

   ```yaml
   permissions:
     contents: write
     pull-requests: write
   ```

## Vertimo kokybė

Mašininiai vertimai gali reikalauti žmogaus peržiūros. Naudokite `evaluate` tik tada, kai norite eksperimentinio kokybės vertinimo ir mažos pasitikėjimo taisymo darbo eigos.

!!! warning "Eksperimentinė"
    `evaluate` gali naudoti taisyklėmis ir LLM pagrįstus tikrinimus, o jo vertinimo modelis bei metaduomenų elgsena gali keistis. Neįtraukite jo į privalomus CI vartus, nebent jūsų darbo eiga yra pasirengusi pokyčiams.

Deterministiniams CI patikrinimams vietoj to naudokite `co-op-review`.