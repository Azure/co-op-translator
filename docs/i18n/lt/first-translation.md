# Versti, redaguoti ir peržiūrėti mažą projektą

Pradėkite su dviem trumpais Markdown failais ir viena tiksline kalba. Pamatysite, kur rašomi vertimai, kas nutinka, kai keičiasi šaltinis, ir kaip patikrinti rezultatą.

## Įrašyti rezultatai

Pavyzdys buvo vykdytas 2026 m. rugsėjo 19 d. su Co-op Translator 0.21.0 ir Azure OpenAI (`gpt-5-mini`). Nekeičiami CLI komandų iškvietimai buvo atlikti per Click's `CliRunner`, naudojant sukompiliuotą wheel ir esamus Python priklausomumus.

| Step | Result |
| --- | --- |
| Peržiūra | Išėjimo kodas 0; modelio vertimo neprašyta |
| Pradinis vertimas | Išėjimo kodas 0; 27.36 sekundės |
| Pradinė peržiūra | Išėjimo kodas 0 |
| README redagavimas ir peržiūra | Išėjimo kodas 1; aptiktas pasenęs vertimas |
| Atnaujinti vertimą | Išėjimo kodas 0; 22.17 sekundės |
| Peržiūra po atnaujinimo | Išėjimo kodas 0; jokių klaidų ar įspėjimų |
| Gidas nepasikeitė | Baitai identiški prieš ir po README atnaujinimo |
| Paleisti dar kartą | Išėjimo kodas 0; identiški hešai visiems vertimo failams |

Tai yra atskiri paleidimo matavimai, ne našumo garantijos. Paruošimo laikas neįskaičiuotas; tiekėjo apmokestinimas nebuvo matuojamas. Nepakeistas paleidimas vis tiek gali atlikti tiekėjo sveikatos patikrinimą.

Peržiūrėkite [pradinį vertimą](../../assets/demo/before.txt), [atnaujintą vertimą](../../assets/demo/after.txt), [pilną vertimo skirtumą](../../assets/demo/update.diff), [pasenusią peržiūrą](../../assets/demo/review-stale.txt), [galutinę peržiūrą](../../assets/demo/review-after.txt) ir [paleidimo detales](../../assets/demo/results.json). Visas failo vertimas gali pakeisti kitus žodinius pasirinkimus, kaip rodo užfiksuotas skirtumas. Abu tekstiniai artefaktai išlaiko sugeneruotą atsisakymą.

Žmogiška peržiūra vis dar svarbi: užfiksuotame atnaujinime naudojama `[사용 가이드](guide.md)을`; korėjietiška dalelytė turėtų būti `[사용 가이드](guide.md)를`. Tekstiniai artefaktai palieka šią išvestį nepakitusią vietoje to, kad pateiktų ištaisytą vertimą kaip modelio išvestį. Struktūrinė peržiūra praeina nepaisant šios formuluotės problemos.

## 1. Paruoškite mažą aplanką

Naudokite Python 3.11–3.14 ir [virtualios aplinkos nustatymą](configuration.md#local-runtime-setup). Įdiekite šios demonstracijos naudotą versiją:

```bash
python -m pip install co-op-translator==0.21.0
mkdir translation-demo
cd translation-demo
git init
```

Atsisiųskite [README.txt](../../assets/demo/README.txt) ir [guide.txt](../../assets/demo/guide.txt) į šį aplanką, išsaugodami juos kaip `README.md` ir `guide.md`. Tai yra maži išgalvoti projekto dokumentai; programos diegti nereikia.

README faile yra kodo blokas ir nuoroda į `guide.md`. Jo paskutinis sakinys yra:

```text
Notes are saved locally.
```

Palikite šiame aplanke tik šiuos du šaltinius. Visos tolesnės komandos vykdomos kataloge `translation-demo` ir veiks Bash ir PowerShell.

## 2. Peržiūra be kredencialų

```bash
translate -l "ko" -md --dry-run
```

Peržiūra įvertina vertimo darbą nekviečiant modelio ir neįrašant vertimų. Tokenų įverčiai nėra sąskaitos pasiūlymas. Pirmasis paleidimas turėtų nustatyti abu Markdown failus kaip naują darbą.

## 3. Pasirinkite paslaugų teikėją ir atlikite vertimą

Sukonfigūruokite vieną teikėją naudodami [konfigūracijos gaires](configuration.md): Azure OpenAI, OpenAI arba Anthropic. OpenAI ir Anthropic teksto vertimui nereikia Azure paskyros. Vaizdų paslaugos šiam pavyzdžiui nėra reikalingos.

Jei naudojate vietinį `.env` failą, pridėkite `.env` prie šio aplanko `.gitignore`. Vertimo užklausos naudoja jūsų teikėjo paskyrą ir gali sukelti mokesčius.

```bash
translate -l "ko" -md
co-op-review -l "ko"
```

Atidarykite `translations/ko/README.md` ir `translations/ko/guide.md`. Patikrinkite korėjietišką formuluotę, kodo bloką ir nuorodą iš išversto `README` į išverstą `guide.md`. Išvesties formuluotė keičiasi priklausomai nuo modelio.

`co-op-review` tikrina šviežumą, struktūrą ir vietines nuorodas. Praeitas rezultatas negarantuoja lingvistinio tikslumo. Išspręskite visas praneštas klaidas prieš tęsdami.

Užfiksuokite sėkmingą bazinę būseną su Gitu (pirmiausia sukonfigūruokite savo Git identitetą, jei reikia):

```bash
git add README.md guide.md translations
git commit -m "Record initial Korean translation"
```

## 4. Pakeiskite šaltinį

Faile `README.md` pakeiskite `Notes are saved locally.` į:

```text
Notes are saved locally as Markdown files.
```

Palikite `guide.md` nepakitusį. Tada vykdykite:

```bash
co-op-review -l "ko"
translate -l "ko" -md --dry-run
```

Peržiūra turėtų pranešti, kad README vertimas pasenęs ir baigtis nesėkmingai. Tai yra tikėtina tarpinė būsena. Peržiūra turėtų identifikuoti užduotį dėl pakeisto README.

## 5. Atnaujinkite ir patikrinkite skirtumą

```bash
translate -l "ko" -md
git diff -- README.md translations/ko/README.md
git diff -- translations/ko/guide.md
co-op-review -l "ko"
```

Patikrinkite tikrąjį skirtumą: numatytasis CLI iš naujo išverčia pakeistą failą, todėl modelis taip pat gali pakeisti ir kitus to failo formulavimus. Nepakeistas `guide.md` neturėtų turėti skirtumų. Peržiūra neturėtų daugiau nurodyti README kaip pasenusio; ištirkite kitus radinius, o ne ignoruokite juos.

Žmogaus Markdown pakeitimų bloko lygmens išsaugojimui reikalingas pasirenkamas vertimo būsenos tiekėjas [Python API](api.md). Tai nėra įjungta šių CLI komandų.

## 6. Paleiskite dar kartą be pakeitimų

Įrašykite atnaujintą šaltinį ir vertimą į Git:

```bash
git add README.md translations
git commit -m "Update Korean translation after source edit"
translate -l "ko" -md
git diff --exit-code -- translations
```

Turint esamus vertimus ir nepakitusią konfigūraciją, vertėjas praleidžia failus. Galutinė Git komanda neturėtų sukurti skirtumo ir turėtų baigtis sėkmingai.

## Tolimesni žingsniai

- [Išversti tik README ir atidaryti pull request'ą](github-actions.md#your-first-readme-translation-pr).
- [Pasirinkite CLI, Python API arba MCP](workflows.md).
- [Praneškite apie vertimo problemą be programavimo](https://github.com/Azure/co-op-translator/issues/new?template=translation_feedback.yml).