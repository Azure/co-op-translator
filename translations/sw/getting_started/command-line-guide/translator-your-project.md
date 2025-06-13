<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d238206c3503631e32774716d11d1868",
  "translation_date": "2025-06-12T18:53:51+00:00",
  "source_file": "getting_started/command-line-guide/translator-your-project.md",
  "language_code": "sw"
}
-->
# Tafsiri mradi wako kwa kutumia Co-op Translator

**Co-op Translator** ni chombo cha mstari wa amri (CLI) kinachokusaidia kutafsiri faili za markdown na picha katika mradi wako kwa lugha mbalimbali. Sehemu hii inaelezea jinsi ya kutumia chombo hiki, inafafanua chaguzi mbalimbali za CLI, na kutoa mifano kwa matumizi tofauti.

> [!NOTE]
> Kwa orodha kamili ya amri na maelezo yao ya kina, tafadhali rejea [Command reference](./command-reference.md).

---

## Mifano ya Matukio na Amri

Hapa kuna baadhi ya matumizi ya kawaida ya **Co-op Translator**, pamoja na amri zinazofaa kutekeleza.

### 1. Tafsiri ya Msingi (Lugha Moja)

Ili kutafsiri mradi wako mzima (faili za markdown na picha) kwa lugha moja, kama Kikorea, tumia amri ifuatayo:

```bash
translate -l "ko"
```

Amri hii itatafsiri faili zote za markdown na picha kwa Kikorea, ikiongeza tafsiri mpya bila kufuta zilizopo.

> [!TIP]
>
> Unataka kuona ni vipi nambari za lugha zinavyopatikana katika **Co-op Translator**? Tembelea sehemu ya [Supported Languages](https://github.com/Azure/co-op-translator#supported-languages) kwenye hifadhidata kwa maelezo zaidi.

#### Mfano kwenye Phi-3 CookBook

Katika **Phi-3 CookBook**, nilitumia njia ifuatayo kuongeza tafsiri ya Kikorea kwa faili zilizopo za markdown na picha.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko"
Translating images: 100%|███████████████████████████████████████████████████| 276/276 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 153/153 [1:43:07<00:00, 241.31s/it]
```

### 2. Kutafsiri Lugha Nyingi

Ili kutafsiri mradi wako kwa lugha nyingi (mfano, Kihispania, Kifaransa, na Kijerumani), tumia amri hii:

```bash
translate -l "es fr de"
```

Amri hii itatafsiri mradi kwa Kihispania, Kifaransa, na Kijerumani, ikiongeza tafsiri mpya bila kuandika juu zilizopo.

#### Mfano kwenye Phi-3 CookBook

Katika **Phi-3 CookBook**, baada ya kuvuta mabadiliko ya hivi karibuni ili kuonyesha marekebisho ya hivi punde, nilitumia njia ifuatayo kutafsiri faili mpya za markdown na picha.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko ja zh tw es fr" -a
Translating images: 100%|███████████████████████████████████████████████████| 273/273 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 6/6 [24:07<00:00, 241.31s/it]
```

> [!NOTE]
> Ingawa kwa kawaida inapendekezwa kutafsiri lugha moja kwa wakati, katika hali kama hii ambapo mabadiliko maalum yanahitajika, kutafsiri lugha nyingi kwa pamoja kunaweza kuwa na ufanisi zaidi.

### 3. Kusasisha Tafsiri (Hufuta Tafsiri Zilizopo)

Ili kusasisha tafsiri zilizopo (yaani, kufuta tafsiri za sasa na kuzibadilisha na mpya), tumia chaguo la `-u`. Hii itafuta tafsiri zote zilizopo kwa lugha zilizotajwa na kuzitafsiri upya.

```bash
translate -l "ko" -u
```

Onyo: Amri hii itakuomba uthibitisho kabla ya kuendelea na kufuta tafsiri zilizopo.

#### Mfano kwenye Phi-3 CookBook

Katika **Phi-3 CookBook**, nilitumia njia ifuatayo kusasisha faili zote zilizotafsiriwa kwa Kihispania. Ninapendekeza kutumia njia hii wakati kuna mabadiliko makubwa katika maudhui ya asili kwenye nyaraka nyingi za markdown. Ikiwa kuna faili chache tu za markdown zilizotafsiriwa kusasisha, ni bora kufuta faili hizo kwa mkono kisha kutumia njia ya `-a` kuongeza tafsiri zilizosasishwa.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "es" -u
Warning: The update command will delete all existing translations for 'es' and re-translate everything.
Do you want to continue? Type 'yes' to proceed: yes
Proceeding with update...
Translating images: 100%|████████████████████████████████████████████| 150/150 [43:46<00:00, 15.55s/it]
Translating markdown files: 100%|███████████████████████████████████| 95/95 [1:40:27<00:00, 125.62s/it]
```

### 5. Kutafsiri Picha Pekee

Ili kutafsiri picha pekee katika mradi wako, tumia chaguo la `-img`:

```bash
translate -l "ko" -img
```

Amri hii itatafsiri picha pekee kwa Kikorea, bila kuathiri faili zozote za markdown.

### 6. Kutafsiri Faili za Markdown Pekee

Ili kutafsiri faili za markdown pekee katika mradi wako, tumia chaguo la `-md`:

```bash
translate -l "ko" -md
```

### 7. Kukagua Makosa katika Faili Zilizotafsiriwa

Kama unataka kukagua faili zilizotafsiriwa kwa makosa na kujaribu kutafsiri tena ikiwa inahitajika, tumia chaguo la `-chk`:

```bash
translate -l "ko" -chk
```

Amri hii itapitia faili za markdown zilizotafsiriwa na kujaribu tena kutafsiri faili zozote zenye makosa.

#### Mfano kwenye Phi-3 CookBook

Katika **Phi-3 CookBook**, nilitumia njia ifuatayo kukagua makosa ya tafsiri katika faili za Kikorea na kujaribu tena kutafsiri kwa otomatiki faili zozote zilizo na matatizo.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko" -chk 
Checking translated files for errors in ko...
Checking files for ko: 100%|██████████████████████████████████████████████████| 95/95 [00:01<00:00, 65.47file/s]
Retrying vsc-extension-quickstart.md for ko:   0%|                                     | 0/17 [00:00<?, ?file/s] 
```

Chaguo hili linakagua makosa ya tafsiri. Kwa sasa, kama tofauti ya mapumziko ya mistari kati ya faili ya asili na ile iliyotafsiriwa ni zaidi ya sita, faili hiyo huwekwa kama yenye hitilafu ya tafsiri. Ninapanga kuboresha kigezo hiki ili kuwa na ufanisi zaidi siku za usoni.

Kwa mfano, njia hii ni muhimu kugundua sehemu zilizokosekana au tafsiri zilizoharibika, na itajaribu tena kutafsiri faili hizo moja kwa moja.

Hata hivyo, kama tayari unajua faili gani zina matatizo, ni bora kufuta faili hizo kwa mkono na kutumia chaguo la `-a` option to re-translate them.

### 8. Debug Mode

To enable detailed logging for troubleshooting, use the `-d`:

```bash
translate -l "ko" -d
```

Amri hii itafanya tafsiri katika hali ya ufuatiliaji wa makosa (debug mode), ikitoa taarifa za ziada za kumbukumbu zinazoweza kusaidia kugundua matatizo wakati wa mchakato wa tafsiri.

#### Mfano kwenye Phi-3 CookBook

Katika **Phi-3 CookBook**, nilikumbana na tatizo ambapo tafsiri zilizo na viungo vingi katika faili za markdown zilisababisha makosa ya muundo, kama tafsiri zilizovunjika na kupuuzwa kwa mapumziko ya mistari. Ili kuchunguza tatizo hili, nilitumia chaguo la `-d` kuona jinsi mchakato wa tafsiri unavyofanya kazi.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "ko" -d
DEBUG:openai._base_client:Request options: {'method': 'post', 'url': '/chat/completions', 'headers': {'api-key': 'af04e0bea45747d8a7b8c131c1971044'}, 'files': None, 'json_data': {'messages': [{'role': 'user', 'content': "Translate the following text to ko. NEVER ADD ANY EXTRA CONTENT OUTSIDE THE TRANSLATION. TRANSLATE ONLY WHAT IS GIVEN TO YOU.. MAINTAIN MARKDOWN FORMAT\n\n# Phi-3 Cookbook: Hands-On Examples with Microsoft's Phi-3 Models [![Open and use the samples in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phi-3cookbook) [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%
...
```

### 9. Kutafsiri Lugha Zote

Ikiwa unataka kutafsiri mradi kwa lugha zote zinazounga mkono, tumia neno kuu all.

> [!WARNING]
> Kutafsiri lugha zote kwa pamoja kunaweza kuchukua muda mrefu kulingana na ukubwa wa mradi. Kwa mfano, kutafsiri **Phi-3 CookBook** kwa Kihispania kulichukua takriban saa 2. Kwa wingi huu, si rahisi mtu mmoja kushughulikia lugha 20. Inapendekezwa kugawanya kazi kwa washiriki wengi, kila mmoja akisimamia lugha moja au mbili, na kusasisha tafsiri polepole.

```bash
translate -l "all"
```

Amri hii itatafsiri mradi kwa lugha zote zinazopatikana. Ikiwa utaendelea, tafsiri inaweza kuchukua muda mrefu kulingana na ukubwa wa mradi.

> [!TIP]
>
> ### Kufuta Faili Zilizotafsiriwa kwa Mkono (Hiari)
> Faili zilizotafsiriwa sasa hutambuliwa na kusafishwa moja kwa moja wakati faili ya chanzo inaposasishwa.
>
> Hata hivyo, kama unataka kusasisha tafsiri kwa mkono - kwa mfano, kufanya upya faili fulani au kubadili tabia ya mfumo - unaweza kutumia amri ifuatayo kufuta matoleo yote ya faili hiyo katika folda za lugha.
>
> ### Kwenye Windows:
> 1. **Kutumia Command Prompt**:
>    - Fungua Command Prompt.
>    - Elekea kwenye folda inayohifadhi faili kwa kutumia amri ya `cd`.
>    - Tumia amri ifuatayo kufuta faili:
>      ```
>      del /s *filename*
>      ```
>      Chaguo `filename` with the specific part of the file name you're looking for. The `/s` kinatafuta pia katika saraka ndogo.
>
> 2. **Kutumia PowerShell**:
>    - Fungua PowerShell.
>    - Endesha amri hii:
>      ```powershell
>      Get-ChildItem -Path "C:\YourPath" -Filter "*filename*" -Recurse | Remove-Item -Force
>      ```
>      Badilisha `"C:\YourPath"` with the folder path and `filename` with the specific name.
>
> ### On macOS/Linux:
> 1. **Using Terminal**:
>   - Open Terminal.
>   - Navigate to the directory with `cd`.
>   - Use the `find` kwa amri ifuatayo:
>     ```bash
>     find . -type f -name "*filename*" -delete
>     ```
>     Badilisha `filename` with the specific name.
>
> Always double-check the files before deleting to avoid accidental loss. 
>
> Once you have deleted the files which need to be replace simply rerun your `translate -l` ili kusasisha mabadiliko ya faili za hivi karibuni.

**Kiasi cha majibu**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kwamba tafsiri za moja kwa moja zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake ya asili inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inashauriwa. Hatubeba dhima yoyote kwa kutoelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.