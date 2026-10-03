# CLI nuoroda

Co-op Translator įdiegia šiuos komandų eilutės įvesties taškus:

- `translate`
- `evaluate`
- `migrate-links`
- `co-op-review`
- `co-op-translator-mcp`

Komandos `translate`, `evaluate`, `migrate-links` ir `co-op-review` perduodamos per `co_op_translator.__main__`, kuris parenka komandos įgyvendinimą pagal paleistos programos pavadinimą. MCP serveris naudoja `co_op_translator.mcp.server` tiesiogiai.

Jei renkatės tarp CLI, Python API ir MCP, pradėkite nuo [Pasirinkite savo darbo eigą](workflows.md).

## Konsolės išvestis

Interaktyvios terminalų sesijos naudoja Rich formatavimą komandų antraštėms, pažangai ir santraukoms. CI ir neinteraktyvi išvestis automatiškai grįžta prie paprasto teksto.

Nustatykite `CO_OP_TRANSLATOR_OUTPUT_STYLE=plain`, kad priverstinai gautumėte paprastą išvestį, arba `CO_OP_TRANSLATOR_OUTPUT_STYLE=rich`, kad priverstinai gautumėte Rich išvestį. Nustatykite `CO_OP_TRANSLATOR_NO_PROGRESS=1`, kad išsaugotumėte santraukas ir slopintumėte gyvus pažangos juostas.

Naudokite `translate --json-events progress.ndjson`, kai kita sistema reikalinga
mašiniškai skaitoma pažanga. CLI toliau pateikia žmogui skirtą išvestį, tuo tarpu
NDJSON faile rašomi versijuoti `co-op.translation.event.v1` įvykiai su
stabiliais laukais, tokiais kaip `type`, `stage_key`, `completed`, `total` ir
`current_path`.

## Pirmas CLI naudojimas

Pradėkite čia, jei naudojate Co-op Translator iš terminalo:

1. Sukonfigūruokite LLM teikėją, kaip aprašyta [Konfigūracija](configuration.md).
2. Pasirinkite turinio tipą, kurį norite išversti.
3. Pirmiausia paleiskite siaurą komandą, pavyzdžiui, tik Markdown vertimą.
4. Prieš didelius saugyklos pakeitimus naudokite `--dry-run`.
5. Po vertimo naudokite `co-op-review`, kad patikrintumėte struktūrą ir aktualumą.

| Tikslas | Komanda pradžiai |
| --- | --- |
| Versti Markdown dokumentus | `translate -l "ko" -md` |
| Versti užrašų knygeles | `translate -l "ko" -nb` |
| Versti vaizdų tekstą | `translate -l "ko" -img` |
| Peržiūrėti darbą nerašant failų | `translate -l "ko" -md --dry-run` |
| Peržiūrėti esamus vertimus | `co-op-review -l "ko"` |
| Atnaujinti užrašų knygelių ir Markdown nuorodas | `migrate-links -l "ko" --dry-run` |
| Eksponuoti įrankius MCP klientui | Sukonfigūruokite [MCP Server](mcp.md) vietoje tiesioginio CLI komandų paleidimo. |

## translate

Verčia Markdown failus, užrašų knygeles ir vaizdų tekstą į vieną arba kelias tikslines kalbas.

```bash
translate -l "ko ja fr"
```

### Dažni pavyzdžiai

Versti tik Markdown:

```bash
translate -l "de" -md
```

Versti tik užrašų knygeles:

```bash
translate -l "zh-CN" -nb
```

Versti Markdown ir vaizdus:

```bash
translate -l "pt-BR" -md -img
```

Atnaujinti esamus vertimus ištrynus ir sukūrus juos iš naujo:

```bash
translate -l "ko" -u
```

Paleisti be interaktyvių užklausų:

```bash
translate -l "ko ja" -md -y
```

Išsaugoti žurnalus:

```bash
translate -l "ko" -s
```

Rašyti struktūruotus pažangos įvykius:

```bash
translate -l "ko ja" -md --json-events progress.ndjson
```

### Parinktys

| Parinktis | Privaloma | Aprašymas |
| --- | --- | --- |
| `-l`, `--language-codes` | Yes | Tarpais atskirti kalbų kodai, pavyzdžiui, `"es fr de"`, arba `"all"`. |
| `-r`, `--root-dir` | No | Projekto šaknis. Pagal numatytuosius nustatymus dabartinis katalogas. |
| `-u`, `--update` | No | Ištrinti esamus pasirinktos kalbos vertimus ir sukurti juos iš naujo. |
| `-img`, `--images` | No | Versti tik vaizdų failus. |
| `-md`, `--markdown` | No | Versti tik Markdown failus. |
| `-nb`, `--notebook` | No | Versti tik Jupyter užrašų knygeles. |
| `-d`, `--debug` | No | Įjungti derinimo lygio žurnalavimą konsolėje. |
| `-s`, `--save-logs` | No | Išsaugoti DEBUG lygio žurnalus po `<root-dir>/logs/`. |
| `--json-events` | No | Rašyti mašinai skaitomus vertimo pažangos įvykius kaip NDJSON. |
| `-x`, `--fix` | No | Išversti iš naujo mažo pasitikėjimo Markdown failus remiantis ankstesniais įvertinimo rezultatais. |
| `-c`, `--min-confidence` | No | Pasitikėjimo slenkstis `--fix`. Pagal numatytuosius nustatymus `0.7`. |
| `--add-disclaimer`, `--no-disclaimer` | No | Pridėti arba slėpti mašininio vertimo atsisakymus. CLI pagal numatytuosius nustatymus įjungta. |
| `-f`, `--fast` | No | Nebenaudojamas greitas vaizdų režimas. |
| `-y`, `--yes` | No | Automatiškai patvirtinti užklausas, naudinga CI. |
| `--repo-url` | No | Saugyklos URL, naudojamas README kalbų lentelės sparse-checkout patarimui. |
| `--migrate-language-folders` | No | Pervardyti senas alias aplankus, pvz., `cn` arba `tw`, į kanoninius BCP 47 aplankus. |
| `--dry-run` | No | Peržiūrėti kalbų aplankų migraciją ir vertimo įverčius nerašant failų. |

Jei nebus nurodytas jokio tipo žymeklis, `translate` apdoros Markdown, užrašų knygeles ir vaizdus. Vaizdų vertimui reikalinga Azure AI Vision konfigūracija.

## evaluate

Įvertina išverstų Markdown kokybę vienai kalbai.

!!! warning "Eksperimentinis"
    `evaluate` yra eksperimentinė. Ji gali naudoti taisyklėmis pagrįstus ir LLM pagrįstus kokybės patikrinimus, rašo įvertinimo rezultatus į vertimo metaduomenis, o jos vertinimo modelis ir metaduomenų elgsena gali keistis.

```bash
evaluate -l "ko"
```

### Dažni pavyzdžiai

Naudokite griežtesnį mažo pasitikėjimo slenkstį:

```bash
evaluate -l "es" -c 0.8
```

Paleisti tik taisyklėmis pagrįstus patikrinimus:

```bash
evaluate -l "fr" -f
```

Paleisti tik LLM pagrįstus patikrinimus:

```bash
evaluate -l "ja" -D
```

### Parinktys

| Parinktis | Privaloma | Aprašymas |
| --- | --- | --- |
| `-l`, `--language-code` | Yes | Vienas kalbos kodas, kurį reikia įvertinti. Alias kodai normalizuojami. |
| `-r`, `--root-dir` | No | Projekto šaknis. Pagal numatytuosius nustatymus dabartinis katalogas. |
| `-c`, `--min-confidence` | No | Slenkstis, naudojamas kai išvardijami mažo pasitikėjimo vertimai. Pagal numatytuosius nustatymus `0.7`. |
| `-d`, `--debug` | No | Įjungti derinimo žurnalavimą. |
| `-s`, `--save-logs` | No | Išsaugoti DEBUG lygio žurnalus po `<root-dir>/logs/`. |
| `-f`, `--fast` | No | Tik taisyklėmis pagrįstas vertinimas. |
| `-D`, `--deep` | No | Tik LLM pagrįstas vertinimas. |

Pagal numatytuosius nustatymus `evaluate` naudoja tiek taisyklėmis pagrįstą, tiek LLM pagrįstą vertinimą. Rezultatai rašomi į vertimo metaduomenis ir apibendrinami konsolėje.

## co-op-review

Paleisti deterministinius vertimo priežiūros patikrinimus be API kredencialų.

!!! note "Beta"
    `co-op-review` yra beta versijos deterministinių peržiūrų komanda. Ji nekvietina modelių tiekėjų ir nerašo failų, tačiau jos patikrinimai ir problemų išvesties schema gali keistis.

```bash
co-op-review -l "ko"
```

### Dažni pavyzdžiai

Peržiūrėti Korėjiečių ir Japonų vertimus iš dabartinio katalogo:

```bash
co-op-review -l "ko ja"
```

Peržiūrėti konkretų projekto šaknį:

```bash
co-op-review -l "fr" -r ./my-course
```

Peržiūrėti tik README po README tik vertimo:

```bash
translate -l "ko" --readme-only -y
co-op-review -l "ko" --readme-only --format github
```

`--readme-only` ignoruoja kitus dokumentus ir įdėtus README. Jis nepavyksta, jei trūksta šakninio
`README.md`. Kartu su `--changed-from` jis peržiūri tik README,
kai tas šaltinio failas pasikeitė. README tik vertimas palieka šaltinio README
nepakitusią, įskaitant bet kokius bendrų skyrių žymeklius.

Peržiūrėti tik šaltinio failus, kurie pasikeitė palyginus su pagrindiniu ref:

```bash
co-op-review -l "ko" --changed-from origin/main
```

Išspausdinti GitHub stiliaus Markdown išvestį CI santraukoms:

```bash
co-op-review -l "ko ja" --changed-from origin/main --format github
```

### Parinktys

| Parinktis | Privaloma | Aprašymas |
| --- | --- | --- |
| `-l`, `--language-code` | No | Kalbos kodas peržiūrai. Gali būti perduotas kelis kartus arba kaip tarpu atskirta reikšmė. Pagal numatytuosius nustatymus visos aptiktos vertimų kalbos. |
| `-r`, `--root-dir` | No | Projekto šaknis. Pagal numatytuosius nustatymus dabartinis katalogas. |
| `--changed-from` | No | Git ref, naudojamas peržiūrai apriboti iki pakeistų šaltinio failų. |
| `--readme-only` | No | Peržiūrėti tik šakninį `README.md` vertimą. |
| `--format` | No | Išvesties formatas: `text` arba `github`. Pagal numatytuosius nustatymus `text`. |

`co-op-review` šiuo metu tikrina trūkstamus išverstus failus, trūkstamus arba pasenusius vertimo metaduomenis, Markdown frontmatter ir kodo tvorų vientisumą, neteisingą išverstų užrašų knygelių JSON ir trūkstamas vietines Markdown arba vaizdų nuorodų paskirties vietas. Trūkstamos nuorodos pagal numatytuosius nustatymus yra įspėjimai; struktūrinės ir aktualumo problemos priverčia komandą nepavykti.

## co-op-translator-mcp

Paleisti Co-op Translator MCP serverį agentams, redaktoriams ir MCP suderinamiems klientams.

```bash
co-op-translator-mcp
```

Numatytoji transporto priemonė yra `stdio`. Žr. [MCP Server](mcp.md) vadovą dėl kliento konfigūracijos, įrankių, išteklių ir saugumo pastabų.

### Parinktys

| Parinktis | Privaloma | Aprašymas |
| --- | --- | --- |
| `--transport` | No | MCP transportas: `stdio`, `streamable-http`, arba `sse`. Pagal numatytuosius nustatymus `stdio`. |

## migrate-links

Perapdoroti išverstus Markdown failus ir atnaujinti užrašų knygelių nuorodas, kad jos nukreiptų į išverstus užrašų knygeles, kai jos yra prieinamos.

```bash
migrate-links -l "ko ja"
```

### Dažni pavyzdžiai

Peržiūrėti nuorodų atnaujinimus:

```bash
migrate-links -l "ko" --dry-run
```

Apdoroti visas palaikomas kalbas be patvirtinimo:

```bash
migrate-links -l "all" -y
```

Perrašyti nuorodas tik tada, kai egzistuoja išverstos užrašų knygelės:

```bash
migrate-links -l "ko" --no-fallback-to-original
```

### Parinktys

| Parinktis | Privaloma | Aprašymas |
| --- | --- | --- |
| `-l`, `--language-codes` | Yes | Tarpais atskirti kalbų kodai arba `"all"`. |
| `-r`, `--root-dir` | No | Projekto šaknis. Pagal numatytuosius nustatymus dabartinis katalogas. |
| `--image-dir` | No | Išverstų vaizdų katalogas, santykinis šakniniam katalogui. Pagal numatytuosius nustatymus `translated_images`. |
| `--dry-run` | No | Rodyti failus, kurie pasikeistų, nerašant atnaujinimų. |
| `--fallback-to-original`, `--no-fallback-to-original` | No | Naudoti originalias užrašų knygelių nuorodas, kai trūksta išverstų užrašų knygelių. Pagal numatytuosius nustatymus įjungta. |
| `-d`, `--debug` | No | Įjungti derinimo žurnalavimą. |
| `-s`, `--save-logs` | No | Išsaugoti DEBUG lygio žurnalus po `<root-dir>/logs/`. |
| `-y`, `--yes` | No | Automatiškai patvirtinti užklausas apdorojant visas kalbas. |

## Aplinka

Kai komandai reikalingi teikėjo kredencialai, sukonfigūruokite vieną iš šių teikėjų rinkinių. `translate --dry-run` ir `co-op-review` nereikalauja teikėjo kredencialų:

```bash
# Azure OpenAI
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"

# Arba OpenAI
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"

# Arba Anthropic
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

Vaizdų vertimui papildomai reikalinga Azure AI Vision:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

## Išvesties struktūra

Teksto vertimai rašomi į:

```text
translations/<language-code>/<original-path>
```

Išverstos vaizdų išvestys rašomos į:

```text
translated_images/<language-code>/<original-path>
```

Pavyzdžiui, išvertus `README.md` ir `docs/setup.md` į korėjiečių kalbą gaunama:

```text
translations/ko/README.md
translations/ko/docs/setup.md
```

## Kopijuoti ir įklijuoti CLI pavyzdžiai

Versti Markdown į tris kalbas:

```bash
translate -l "ko ja fr" -md
```

Versti užrašų knygeles tik:

```bash
translate -l "zh-CN" -nb
```

Versti vaizdus tik:

```bash
translate -l "pt-BR" -img
```

Peržiūrėti Markdown vertimą nerašant failų:

```bash
translate -l "de es" -md --dry-run
```

Sutaisyti mažo pasitikėjimo Markdown vertimus:

```bash
evaluate -l "ko" -c 0.8
translate -l "ko" --fix -c 0.8 -md
```

Paleisti CI draugišką Markdown vertimą:

```bash
translate -l "ko ja" -md -y -s
```

Peržiūrėti išverstą išvestį:

```bash
co-op-review -l "ko ja"
```

Peržiūrėti nuorodų migraciją:

```bash
migrate-links -l "ko" --dry-run
```