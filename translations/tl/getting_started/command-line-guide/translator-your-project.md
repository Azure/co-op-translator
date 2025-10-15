<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "20943a46b11c6d74814f41a817a6db4c",
  "translation_date": "2025-10-15T03:43:36+00:00",
  "source_file": "getting_started/command-line-guide/translator-your-project.md",
  "language_code": "tl"
}
-->
# Isalin ang iyong proyekto gamit ang Co-op Translator

Ang **Co-op Translator** ay isang command-line interface (CLI) tool na tumutulong sa iyo na isalin ang mga markdown at image file sa iyong proyekto sa iba’t ibang wika. Sa seksyong ito, ipapaliwanag kung paano gamitin ang tool, tatalakayin ang iba’t ibang CLI options, at magbibigay ng mga halimbawa para sa iba’t ibang sitwasyon.

> [!NOTE]
> Para sa kumpletong listahan ng mga command at detalyadong paliwanag, bisitahin ang [Command reference](./command-reference.md).

---

## Mga Halimbawa ng Sitwasyon at Command

Narito ang ilang karaniwang gamit ng **Co-op Translator** at ang tamang command para dito.

### 1. Pangunahing Pagsasalin (Isang Wika)

Para isalin ang buong proyekto mo (markdown files at images) sa isang wika, halimbawa Korean, gamitin ang command na ito:

```bash
translate -l "ko"
```

Ang command na ito ay magsasalin ng lahat ng markdown at image file sa Korean, at magdadagdag ng bagong salin nang hindi binubura ang mga dati nang salin.

> [!TIP]
>
> Gusto mo bang malaman kung anong mga language code ang available sa **Co-op Translator**? Bisitahin ang [Supported Languages](https://github.com/Azure/co-op-translator#supported-languages) section sa repository para sa karagdagang detalye.

#### Halimbawa sa Phi-3 CookBook

Sa **Phi-3 CookBook**, ginamit ko ang pamamaraang ito para idagdag ang Korean translation sa mga existing na markdown files at images.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko"
Translating images: 100%|███████████████████████████████████████████████████| 276/276 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 153/153 [1:43:07<00:00, 241.31s/it]
```

### 2. Pagsasalin sa Maramihang Wika

Para isalin ang proyekto mo sa maraming wika (hal. Spanish, French, at German), gamitin ang command na ito:

```bash
translate -l "es fr de"
```

Ang command na ito ay magsasalin ng proyekto sa Spanish, French, at German, at magdadagdag ng bagong salin nang hindi pinapalitan ang mga dati nang salin.

#### Halimbawa sa Phi-3 CookBook

Sa **Phi-3 CookBook**, pagkatapos kunin ang pinakabagong update para makita ang mga bagong commit, ginamit ko ang pamamaraang ito para isalin ang mga bagong markdown files at images.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko ja zh tw es fr" -a
Translating images: 100%|███████████████████████████████████████████████████| 273/273 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 6/6 [24:07<00:00, 241.31s/it]
```

> [!NOTE]
> Bagama’t mas mainam na isalin ang isang wika sa bawat pagkakataon, sa mga sitwasyon tulad nito na may partikular na pagbabago, mas mabilis ang pagsasalin sa maraming wika nang sabay-sabay.

### 3. Pag-update ng Salin (Binubura ang Dating Salin)

Para i-update ang mga dating salin (ibig sabihin, burahin ang kasalukuyang salin at palitan ng bago), gamitin ang `-u` option. Buburahin nito ang lahat ng dating salin para sa mga tinukoy na wika at isasalin muli.

```bash
translate -l "ko" -u
```

Babala: Magpapakita ang command na ito ng kumpirmasyon bago magpatuloy sa pagbura ng mga dating salin.

#### Halimbawa sa Phi-3 CookBook

Sa **Phi-3 CookBook**, ginamit ko ang pamamaraang ito para i-update ang lahat ng translated files sa Spanish. Inirerekomenda ko ang pamamaraang ito kapag malaki ang pagbabago sa orihinal na content sa maraming markdown documents. Kung iilan lang ang kailangang i-update, mas mabilis na mano-manong burahin ang mga partikular na file at gamitin ang `-a` method para idagdag ang updated na salin.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "es" -u
Warning: The update command will delete all existing translations for 'es' and re-translate everything.
Do you want to continue? Type 'yes' to proceed: yes
Proceeding with update...
Translating images: 100%|████████████████████████████████████████████| 150/150 [43:46<00:00, 15.55s/it]
Translating markdown files: 100%|███████████████████████████████████| 95/95 [1:40:27<00:00, 125.62s/it]
```

### 5. Pagsasalin ng Images Lang

Para isalin lang ang mga image file sa iyong proyekto, gamitin ang `-img` option:

```bash
translate -l "ko" -img
```

Ang command na ito ay magsasalin lang ng mga images sa Korean, nang hindi naaapektuhan ang mga markdown file.

### 6. Pagsasalin ng Markdown Files Lang

Para isalin lang ang mga markdown file sa iyong proyekto, gamitin ang `-md` option:

```bash
translate -l "ko" -md
```

#### Halimbawa sa Phi-3 CookBook

Sa **Phi-3 CookBook**, ginamit ko ang pamamaraang ito para i-check ang mga error sa salin ng Korean files at awtomatikong subukan ulit ang pagsasalin sa mga file na may problema.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko" -chk 
Checking translated files for errors in ko...
Checking files for ko: 100%|██████████████████████████████████████████████████| 95/95 [00:01<00:00, 65.47file/s]
Retrying vsc-extension-quickstart.md for ko:   0%|                                     | 0/17 [00:00<?, ?file/s] 
```

Ang option na ito ay nagche-check ng mga error sa salin. Sa ngayon, kung ang pagkakaiba ng line breaks sa orihinal at salin ay higit sa anim, itinuturing na may error ang file. Plano kong gawing mas flexible pa ang criterion na ito sa hinaharap.

Halimbawa, magagamit ang pamamaraang ito para makita ang mga kulang na bahagi o sirang salin, at awtomatikong uulitin ang pagsasalin para sa mga file na iyon.

Pero kung alam mo na kung aling mga file ang may problema, mas mabilis na mano-manong burahin ang mga iyon at gamitin ang `-a` option para isalin ulit.

### 8. Debug Mode

Para makita ang mas detalyadong log para sa troubleshooting, gamitin ang `-d` option:

```bash
translate -l "ko" -d
```

Ang command na ito ay magpapatakbo ng pagsasalin sa debug mode, na magbibigay ng dagdag na impormasyon para matukoy ang mga isyu habang nagsasalin.

#### Halimbawa sa Phi-3 CookBook

Sa **Phi-3 CookBook**, naranasan ko ang isyu na kapag maraming links sa markdown files, nagkakaroon ng formatting errors tulad ng sirang salin at nawawalang line breaks. Para ma-diagnose ang problema, ginamit ko ang `-d` option para makita kung paano tumatakbo ang proseso ng pagsasalin.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "ko" -d
DEBUG:openai._base_client:Request options: {'method': 'post', 'url': '/chat/completions', 'headers': {'api-key': 'af04e0bea45747d8a7b8c131c1971044'}, 'files': None, 'json_data': {'messages': [{'role': 'user', 'content': "Translate the following text to ko. NEVER ADD ANY EXTRA CONTENT OUTSIDE THE TRANSLATION. TRANSLATE ONLY WHAT IS GIVEN TO YOU.. MAINTAIN MARKDOWN FORMAT\n\n# Phi-3 Cookbook: Hands-On Examples with Microsoft's Phi-3 Models [![Open and use the samples in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phi-3cookbook) [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%
...
```

### 9. Pagsasalin sa Lahat ng Wika

Kung gusto mong isalin ang proyekto sa lahat ng suportadong wika, gamitin ang all keyword.

> [!WARNING]
> Ang pagsasalin sa lahat ng wika nang sabay-sabay ay maaaring tumagal depende sa laki ng proyekto. Halimbawa, ang pagsasalin ng **Phi-3 CookBook** sa Spanish ay umabot ng halos 2 oras. Dahil sa dami, hindi praktikal para sa isang tao ang magsalin sa 20 wika. Mas mainam na hati-hatiin ang trabaho sa maraming contributors, bawat isa ay mag-manage ng isa o dalawang wika, at dahan-dahang i-update ang mga salin.

```bash
translate -l "all"
```

Ang command na ito ay magsasalin ng proyekto sa lahat ng available na wika. Kapag nagpatuloy ka, maaaring tumagal ang pagsasalin depende sa laki ng proyekto.

> [!TIP]
>
> ### Mano-manong Pagbura ng Translated Files (Opsyonal)
> Awtomatikong nade-detect at nililinis na ang mga translated files kapag may update sa source file.
>
> Pero kung gusto mong mano-manong i-update ang salin—halimbawa, para ulitin ang isang partikular na file o i-override ang system behavior—pwede mong gamitin ang command na ito para burahin ang lahat ng bersyon ng file sa mga language folder.
>
> ### Sa Windows:
> 1. **Gamit ang Command Prompt**:
>    - Buksan ang Command Prompt.
>    - Pumunta sa folder kung saan naroon ang mga file gamit ang `cd` command.
>    - Gamitin ang command na ito para burahin ang mga file:
>      ```
>      del /s *filename*
>      ```
>      Palitan ang `filename` ng partikular na bahagi ng pangalan ng file na hinahanap mo. Ang `/s` option ay maghahanap sa mga subdirectory.
>
> 2. **Gamit ang PowerShell**:
>    - Buksan ang PowerShell.
>    - Patakbuhin ang command na ito:
>      ```powershell
>      Get-ChildItem -Path "C:\YourPath" -Filter "*filename*" -Recurse | Remove-Item -Force
>      ```
>      Palitan ang `"C:\YourPath"` ng path ng folder at `filename` ng partikular na pangalan.
>
> ### Sa macOS/Linux:
> 1. **Gamit ang Terminal**:
>   - Buksan ang Terminal.
>   - Pumunta sa directory gamit ang `cd`.
>   - Gamitin ang `find` command:
>     ```bash
>     find . -type f -name "*filename*" -delete
>     ```
>     Palitan ang `filename` ng partikular na pangalan.
>
> Laging i-double check ang mga file bago burahin para maiwasan ang aksidenteng pagkawala.
>
> Kapag nabura mo na ang mga file na kailangang palitan, i-rerun lang ang iyong `translate -l` command para ma-update ang pinakabagong pagbabago sa file.

---

**Paunawa**:
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagaman nagsusumikap kami para sa katumpakan, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi eksaktong salin. Ang orihinal na dokumento sa kanyang sariling wika ang dapat ituring na pangunahing sanggunian. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaintindihan o maling interpretasyon na maaaring lumitaw mula sa paggamit ng pagsasaling ito.