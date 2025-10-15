<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "20943a46b11c6d74814f41a817a6db4c",
  "translation_date": "2025-10-15T05:00:13+00:00",
  "source_file": "getting_started/command-line-guide/translator-your-project.md",
  "language_code": "lt"
}
-->
# Išverskite savo projektą su Co-op Translator

**Co-op Translator** yra komandinės eilutės (CLI) įrankis, padedantis išversti jūsų projekto markdown ir paveikslėlių failus į kelias kalbas. Šiame skyriuje paaiškinama, kaip naudotis įrankiu, aptariamos įvairios CLI parinktys ir pateikiami pavyzdžiai skirtingiems naudojimo atvejams.

> [!NOTE]
> Visą komandų sąrašą ir jų išsamų aprašymą rasite [Komandų nuorodoje](./command-reference.md).

---

## Pavyzdinės situacijos ir komandos

Čia pateikiami keli dažni **Co-op Translator** naudojimo atvejai su tinkamomis komandomis.

### 1. Pagrindinis vertimas (viena kalba)

Norėdami išversti visą projektą (markdown failus ir paveikslėlius) į vieną kalbą, pavyzdžiui, korėjiečių, naudokite šią komandą:

```bash
translate -l "ko"
```

Ši komanda išvers visus markdown ir paveikslėlių failus į korėjiečių kalbą, pridės naujus vertimus, nepašalindama jau esamų.

> [!TIP]
>
> Norite sužinoti, kokie kalbų kodai galimi **Co-op Translator**? Daugiau informacijos rasite [Supported Languages](https://github.com/Azure/co-op-translator#supported-languages) skiltyje repozitorijoje.

#### Pavyzdys su Phi-3 CookBook

**Phi-3 CookBook** projekte naudojau šį metodą, kad pridėčiau korėjiečių vertimą esamiems markdown failams ir paveikslėliams.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko"
Translating images: 100%|███████████████████████████████████████████████████| 276/276 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 153/153 [1:43:07<00:00, 241.31s/it]
```

### 2. Vertimas į kelias kalbas

Norėdami išversti projektą į kelias kalbas (pvz., ispanų, prancūzų ir vokiečių), naudokite šią komandą:

```bash
translate -l "es fr de"
```

Ši komanda išvers projektą į ispanų, prancūzų ir vokiečių kalbas, pridės naujus vertimus, neperrašydama jau esamų.

#### Pavyzdys su Phi-3 CookBook

**Phi-3 CookBook** projekte, po naujausių pakeitimų atsiuntimo, naudojau šį metodą, kad išversčiau naujai pridėtus markdown failus ir paveikslėlius.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko ja zh tw es fr" -a
Translating images: 100%|███████████████████████████████████████████████████| 273/273 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 6/6 [24:07<00:00, 241.31s/it]
```

> [!NOTE]
> Nors paprastai rekomenduojama versti po vieną kalbą, tokiose situacijose, kai reikia pridėti konkrečius pakeitimus, versti kelias kalbas vienu metu gali būti efektyvu.

### 3. Vertimų atnaujinimas (pašalina esamus vertimus)

Norėdami atnaujinti esamus vertimus (t. y. ištrinti dabartinius vertimus ir juos pakeisti naujais), naudokite `-u` parinktį. Ji ištrins visus nurodytų kalbų vertimus ir išvers iš naujo.

```bash
translate -l "ko" -u
```

Įspėjimas: Ši komanda prieš tęsiant paprašys patvirtinimo dėl esamų vertimų ištrynimo.

#### Pavyzdys su Phi-3 CookBook

**Phi-3 CookBook** projekte naudojau šį metodą, kad atnaujinčiau visus išverstus failus ispanų kalba. Rekomenduoju šį metodą, kai originaliame turinyje yra daug pakeitimų keliuose markdown dokumentuose. Jei reikia atnaujinti tik kelis išverstus markdown failus, efektyviau juos ištrinti rankiniu būdu ir tada naudoti `-a` metodą, kad pridėtumėte atnaujintus vertimus.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "es" -u
Warning: The update command will delete all existing translations for 'es' and re-translate everything.
Do you want to continue? Type 'yes' to proceed: yes
Proceeding with update...
Translating images: 100%|████████████████████████████████████████████| 150/150 [43:46<00:00, 15.55s/it]
Translating markdown files: 100%|███████████████████████████████████| 95/95 [1:40:27<00:00, 125.62s/it]
```

### 5. Tik paveikslėlių vertimas

Norėdami išversti tik paveikslėlių failus projekte, naudokite `-img` parinktį:

```bash
translate -l "ko" -img
```

Ši komanda išvers tik paveikslėlius į korėjiečių kalbą, nepaliesdama markdown failų.

### 6. Tik markdown failų vertimas

Norėdami išversti tik markdown failus projekte, naudokite `-md` parinktį:

```bash
translate -l "ko" -md
```

#### Pavyzdys su Phi-3 CookBook

**Phi-3 CookBook** projekte naudojau šį metodą, kad patikrinčiau vertimo klaidas korėjiečių failuose ir automatiškai pakartotinai išversčiau tuos failus, kuriuose aptikta problemų.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko" -chk 
Checking translated files for errors in ko...
Checking files for ko: 100%|██████████████████████████████████████████████████| 95/95 [00:01<00:00, 65.47file/s]
Retrying vsc-extension-quickstart.md for ko:   0%|                                     | 0/17 [00:00<?, ?file/s] 
```

Ši parinktis tikrina vertimo klaidas. Šiuo metu, jei skirtumas tarp originalo ir vertimo eilučių lūžių yra didesnis nei šeši, failas pažymimas kaip turintis vertimo klaidą. Ateityje planuoju patobulinti šį kriterijų, kad būtų lankstesnis.

Pavyzdžiui, šis metodas naudingas aptikti trūkstamas dalis ar sugadintus vertimus ir automatiškai pakartotinai išverčia tuos failus.

Tačiau, jei jau žinote, kurie failai yra probleminiai, efektyviau juos ištrinti rankiniu būdu ir naudoti `-a` parinktį, kad išverstumėte iš naujo.

### 8. Derinimo režimas

Norėdami įjungti išsamesnį žurnalavimą problemų sprendimui, naudokite `-d` parinktį:

```bash
translate -l "ko" -d
```

Ši komanda paleis vertimą derinimo režimu ir pateiks papildomą žurnalo informaciją, kuri gali padėti nustatyti problemas vertimo metu.

#### Pavyzdys su Phi-3 CookBook

**Phi-3 CookBook** projekte susidūriau su problema, kai vertimai su daug nuorodų markdown failuose sukeldavo formatavimo klaidas, pavyzdžiui, sugadintus vertimus ir ignoruojamus eilučių lūžius. Norėdamas diagnozuoti šią problemą, naudojau `-d` parinktį, kad pamatyčiau, kaip vyksta vertimo procesas.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "ko" -d
DEBUG:openai._base_client:Request options: {'method': 'post', 'url': '/chat/completions', 'headers': {'api-key': 'af04e0bea45747d8a7b8c131c1971044'}, 'files': None, 'json_data': {'messages': [{'role': 'user', 'content': "Translate the following text to ko. NEVER ADD ANY EXTRA CONTENT OUTSIDE THE TRANSLATION. TRANSLATE ONLY WHAT IS GIVEN TO YOU.. MAINTAIN MARKDOWN FORMAT\n\n# Phi-3 Cookbook: Hands-On Examples with Microsoft's Phi-3 Models [![Open and use the samples in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phi-3cookbook) [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%
...
```

### 9. Vertimas į visas kalbas

Jei norite išversti projektą į visas palaikomas kalbas, naudokite all raktinį žodį.

> [!WARNING]
> Vertimas į visas kalbas vienu metu gali užtrukti labai ilgai, priklausomai nuo projekto dydžio. Pavyzdžiui, **Phi-3 CookBook** vertimas į ispanų kalbą užtruko apie 2 valandas. Atsižvelgiant į mastą, nepatogu vienam žmogui tvarkyti 20 kalbų. Rekomenduojama darbą paskirstyti keliems bendradarbiams, kad kiekvienas tvarkytų po vieną ar dvi kalbas ir vertimai būtų atnaujinami palaipsniui.

```bash
translate -l "all"
```

Ši komanda išvers projektą į visas galimas kalbas. Jei tęsite, vertimas gali užtrukti ilgai, priklausomai nuo projekto dydžio.

> [!TIP]
>
> ### Rankinis išverstų failų ištrynimas (pasirinktinai)
> Išversti failai dabar automatiškai aptinkami ir išvalomi, kai atnaujinamas šaltinio failas.
>
> Tačiau, jei norite rankiniu būdu atnaujinti vertimą – pavyzdžiui, iš naujo išversti konkretų failą ar pakeisti sistemos elgseną – galite naudoti šią komandą, kad ištrintumėte visus failo variantus kalbų aplankuose.
>
> ### Windows sistemoje:
> 1. **Naudojant Command Prompt**:
>    - Atidarykite Command Prompt.
>    - Pereikite į aplanką, kuriame yra failai, naudodami `cd` komandą.
>    - Naudokite šią komandą failams ištrinti:
>      ```
>      del /s *filename*
>      ```
>      Pakeiskite `filename` į konkrečią failo dalį, kurios ieškote. `/s` parinktis ieško poaplankiuose.
>
> 2. **Naudojant PowerShell**:
>    - Atidarykite PowerShell.
>    - Paleiskite šią komandą:
>      ```powershell
>      Get-ChildItem -Path "C:\YourPath" -Filter "*filename*" -Recurse | Remove-Item -Force
>      ```
>      Pakeiskite `"C:\YourPath"` į aplanko kelią ir `filename` į konkretų pavadinimą.
>
> ### macOS/Linux sistemoje:
> 1. **Naudojant Terminal**:
>   - Atidarykite Terminal.
>   - Pereikite į katalogą su `cd`.
>   - Naudokite `find` komandą:
>     ```bash
>     find . -type f -name "*filename*" -delete
>     ```
>     Pakeiskite `filename` į konkretų pavadinimą.
>
> Visada atidžiai patikrinkite failus prieš ištrindami, kad išvengtumėte netyčinio praradimo. 
>
> Kai ištrinsite failus, kuriuos reikia pakeisti, tiesiog iš naujo paleiskite savo `translate -l` komandą, kad atnaujintumėte naujausius failų pakeitimus.

---

**Atsakomybės atsisakymas**:
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojame profesionalų žmogaus vertimą. Mes neatsakome už nesusipratimus ar neteisingą interpretavimą, kilusį naudojantis šiuo vertimu.