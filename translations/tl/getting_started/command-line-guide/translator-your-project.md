<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d238206c3503631e32774716d11d1868",
  "translation_date": "2025-06-12T18:53:29+00:00",
  "source_file": "getting_started/command-line-guide/translator-your-project.md",
  "language_code": "tl"
}
-->
# Isalin ang iyong proyekto gamit ang Co-op Translator

Ang **Co-op Translator** ay isang command-line interface (CLI) na tool na tumutulong sa iyo na isalin ang mga markdown at image files sa iyong proyekto sa iba't ibang wika. Ipinaliwanag sa seksyong ito kung paano gamitin ang tool, mga iba't ibang opsyon ng CLI, at mga halimbawa para sa iba't ibang sitwasyon.

> [!NOTE]
> Para sa kumpletong listahan ng mga command at kanilang detalyadong paglalarawan, pakitingnan ang [Command reference](./command-reference.md).

---

## Mga Halimbawa ng Sitwasyon at Mga Command

Narito ang ilang karaniwang gamit ng **Co-op Translator**, kasama ang mga angkop na command na dapat patakbuhin.

### 1. Pangunahing Pagsasalin (Isang Wika)

Para isalin ang buong proyekto (mga markdown file at mga larawan) sa isang wika lamang, tulad ng Korean, gamitin ang sumusunod na command:

```bash
translate -l "ko"
```

Isasalin ng command na ito ang lahat ng markdown at image files sa Korean, magdadagdag ng mga bagong pagsasalin nang hindi binubura ang mga dati nang nasa sistema.

> [!TIP]
>
> Gusto mo bang malaman kung anong mga language code ang available sa **Co-op Translator**? Bisitahin ang seksyong [Supported Languages](https://github.com/Azure/co-op-translator#supported-languages) sa repository para sa karagdagang detalye.

#### Halimbawa sa Phi-3 CookBook

Sa **Phi-3 CookBook**, ginamit ko ang sumusunod na paraan para idagdag ang pagsasalin sa Korean para sa mga umiiral na markdown file at mga larawan.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko"
Translating images: 100%|███████████████████████████████████████████████████| 276/276 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 153/153 [1:43:07<00:00, 241.31s/it]
```

### 2. Pagsasalin sa Maramihang Wika

Para isalin ang proyekto sa maramihang wika (halimbawa, Spanish, French, at German), gamitin ang command na ito:

```bash
translate -l "es fr de"
```

Isasalin ng command na ito ang proyekto sa Spanish, French, at German, magdadagdag ng mga bagong pagsasalin nang hindi nire-replace ang mga dati nang nasa sistema.

#### Halimbawa sa Phi-3 CookBook

Sa **Phi-3 CookBook**, pagkatapos i-pull ang mga pinakabagong pagbabago para maipakita ang mga pinaka-sariwang commit, ginamit ko ang sumusunod na paraan para isalin ang mga bagong idinagdag na markdown file at mga larawan.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko ja zh tw es fr" -a
Translating images: 100%|███████████████████████████████████████████████████| 273/273 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 6/6 [24:07<00:00, 241.31s/it]
```

> [!NOTE]
> Bagamat karaniwang inirerekomenda na isang wika lang ang isalin sa isang pagkakataon, sa mga sitwasyon tulad nito kung saan kailangang idagdag ang mga tiyak na pagbabago, mas epektibo ang pagsasalin ng maramihang wika nang sabay-sabay.

### 3. Pag-update ng mga Pagsasalin (Binubura ang Umiiral na mga Pagsasalin)

Para i-update ang mga umiiral na pagsasalin (ibig sabihin, burahin ang kasalukuyang mga pagsasalin at palitan ng bago), gamitin ang opsyong `-u`. Buburahin nito lahat ng umiiral na pagsasalin para sa mga tinukoy na wika at isasalin muli.

```bash
translate -l "ko" -u
```

Babala: Hihingin ng command na ito ang iyong kumpirmasyon bago tuluyang burahin ang mga umiiral na pagsasalin.

#### Halimbawa sa Phi-3 CookBook

Sa **Phi-3 CookBook**, ginamit ko ang sumusunod na paraan para i-update ang lahat ng isinaling file sa Spanish. Inirerekomenda kong gamitin ang pamamaraang ito kapag may malalaking pagbabago sa orihinal na nilalaman sa maraming markdown na dokumento. Kung iilan lang naman ang kailangang i-update na isinaling markdown file, mas mabilis na manu-manong burahin ang mga partikular na file at pagkatapos ay gamitin ang `-a` na paraan para idagdag ang mga na-update na pagsasalin.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "es" -u
Warning: The update command will delete all existing translations for 'es' and re-translate everything.
Do you want to continue? Type 'yes' to proceed: yes
Proceeding with update...
Translating images: 100%|████████████████████████████████████████████| 150/150 [43:46<00:00, 15.55s/it]
Translating markdown files: 100%|███████████████████████████████████| 95/95 [1:40:27<00:00, 125.62s/it]
```

### 5. Pagsasalin ng Mga Larawan Lamang

Para isalin lamang ang mga image file sa iyong proyekto, gamitin ang opsyong `-img`:

```bash
translate -l "ko" -img
```

Isasalin lamang ng command na ito ang mga larawan sa Korean, nang hindi naaapektuhan ang mga markdown file.

### 6. Pagsasalin ng Mga Markdown File Lamang

Para isalin lamang ang mga markdown file sa iyong proyekto, gamitin ang opsyong `-md`:

```bash
translate -l "ko" -md
```

### 7. Pagsusuri ng Mga Mali sa Isinaling Mga File

Kung nais mong suriin ang mga isinaling file para sa mga error at subukang muli ang pagsasalin kung kinakailangan, gamitin ang opsyong `-chk`:

```bash
translate -l "ko" -chk
```

Susuriin ng command na ito ang mga isinaling markdown file at muling isasalin ang anumang file na may mga error.

#### Halimbawa sa Phi-3 CookBook

Sa **Phi-3 CookBook**, ginamit ko ang sumusunod na paraan para suriin ang mga error sa pagsasalin ng mga Korean na file at awtomatikong subukang muli ang pagsasalin para sa anumang file na may natukoy na problema.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko" -chk 
Checking translated files for errors in ko...
Checking files for ko: 100%|██████████████████████████████████████████████████| 95/95 [00:01<00:00, 65.47file/s]
Retrying vsc-extension-quickstart.md for ko:   0%|                                     | 0/17 [00:00<?, ?file/s] 
```

Sinusuri ng opsyong ito ang mga error sa pagsasalin. Sa kasalukuyan, kung ang pagkakaiba sa mga line break sa pagitan ng orihinal at isinaling file ay higit sa anim, itinuturing na may error ang file sa pagsasalin. Plano kong pagbutihin ang pamantayang ito para sa mas malawak na kakayahang umangkop sa hinaharap.

Halimbawa, kapaki-pakinabang ang pamamaraang ito para matukoy ang mga nawawalang bahagi o sirang pagsasalin, at awtomatikong susubukan muli ang pagsasalin para sa mga file na iyon.

Gayunpaman, kung alam mo na kung alin ang mga problemadong file, mas mabilis na manu-manong burahin ang mga ito at gamitin ang opsyong `-a` option to re-translate them.

### 8. Debug Mode

To enable detailed logging for troubleshooting, use the `-d`:

```bash
translate -l "ko" -d
```

Patatakbuhin ng command na ito ang pagsasalin sa debug mode, na nagbibigay ng karagdagang impormasyon sa pag-log na makakatulong sa iyo na tuklasin ang mga isyu habang isinasagawa ang pagsasalin.

#### Halimbawa sa Phi-3 CookBook

Sa **Phi-3 CookBook**, nakaranas ako ng isyu kung saan ang mga pagsasalin na maraming link sa mga markdown file ay nagdulot ng mga error sa format, tulad ng sirang pagsasalin at hindi pinapansin na mga line break. Para ma-diagnose ang problemang ito, ginamit ko ang opsyong `-d` para makita kung paano gumagana ang proseso ng pagsasalin.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "ko" -d
DEBUG:openai._base_client:Request options: {'method': 'post', 'url': '/chat/completions', 'headers': {'api-key': 'af04e0bea45747d8a7b8c131c1971044'}, 'files': None, 'json_data': {'messages': [{'role': 'user', 'content': "Translate the following text to ko. NEVER ADD ANY EXTRA CONTENT OUTSIDE THE TRANSLATION. TRANSLATE ONLY WHAT IS GIVEN TO YOU.. MAINTAIN MARKDOWN FORMAT\n\n# Phi-3 Cookbook: Hands-On Examples with Microsoft's Phi-3 Models [![Open and use the samples in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phi-3cookbook) [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%
...
```

### 9. Pagsasalin sa Lahat ng Wika

Kung nais mong isalin ang proyekto sa lahat ng suportadong wika, gamitin ang keyword na all.

> [!WARNING]
> Ang pagsasalin sa lahat ng wika nang sabay-sabay ay maaaring tumagal ng malaking oras depende sa laki ng proyekto. Halimbawa, ang pagsasalin ng **Phi-3 CookBook** sa Spanish ay tumagal ng halos 2 oras. Dahil sa lawak nito, hindi praktikal na isang tao lang ang humawak ng 20 wika. Inirerekomenda na hatiin ang trabaho sa maraming contributor, bawat isa ay namamahala ng isa o dalawang wika, at unti-unting ina-update ang mga pagsasalin.

```bash
translate -l "all"
```

Isasalin ng command na ito ang proyekto sa lahat ng available na wika. Kapag nagpursige ka, maaaring tumagal nang matagal ang pagsasalin depende sa laki ng proyekto.

> [!TIP]
>
> ### Manu-manong Pagbura ng Mga Isinaling File (Opsyonal)
> Awtomatikong natutukoy at nililinis ang mga isinaling file kapag na-update ang source file.
>
> Gayunpaman, kung gusto mong manu-manong i-update ang isang pagsasalin — halimbawa, upang ulitin ang isang partikular na file o i-override ang sistema — maaari mong gamitin ang sumusunod na command para burahin ang lahat ng bersyon ng file sa iba't ibang language folder.
>
> ### Sa Windows:
> 1. **Gamit ang Command Prompt**:
>    - Buksan ang Command Prompt.
>    - Pumunta sa folder kung saan naroroon ang mga file gamit ang command na `cd`.
>    - Gamitin ang sumusunod na command para burahin ang mga file:
>      ```
>      del /s *filename*
>      ```
>      Ang opsyong `/s` ay naghahanap din sa mga subdirectory.
>
> 2. **Gamit ang PowerShell**:
>    - Buksan ang PowerShell.
>    - Patakbuhin ang command na ito:
>      ```powershell
>      Get-ChildItem -Path "C:\YourPath" -Filter "*filename*" -Recurse | Remove-Item -Force
>      ```
>      Palitan ang `"C:\YourPath"` with the folder path and `filename` with the specific name.
>
> ### On macOS/Linux:
> 1. **Using Terminal**:
>   - Open Terminal.
>   - Navigate to the directory with `cd`.
>   - Use the `find` command:
>     ```bash
>     find . -type f -name "*filename*" -delete
>     ```
>     Palitan ang `filename` with the specific name.
>
> Always double-check the files before deleting to avoid accidental loss. 
>
> Once you have deleted the files which need to be replace simply rerun your `translate -l` command para i-update ang pinakabagong mga pagbabago sa file.

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat nagsusumikap kami para sa katumpakan, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mga mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.