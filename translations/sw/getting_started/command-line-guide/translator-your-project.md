<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "20943a46b11c6d74814f41a817a6db4c",
  "translation_date": "2025-10-15T03:46:23+00:00",
  "source_file": "getting_started/command-line-guide/translator-your-project.md",
  "language_code": "sw"
}
-->
# Tafsiri mradi wako kwa kutumia Co-op Translator

**Co-op Translator** ni zana ya mstari wa amri (CLI) inayokusaidia kutafsiri faili za markdown na picha kwenye mradi wako kwenda lugha mbalimbali. Sehemu hii inaelezea jinsi ya kutumia zana hii, inaeleza chaguzi mbalimbali za CLI, na inatoa mifano kwa matumizi tofauti.

> [!NOTE]
> Kwa orodha kamili ya amri na maelezo yake, tafadhali angalia [Command reference](./command-reference.md).

---

## Mifano ya Matumizi na Amri

Hapa kuna baadhi ya matumizi ya kawaida ya **Co-op Translator**, pamoja na amri zinazofaa kutumia.

### 1. Tafsiri ya Kawaida (Lugha Moja)

Ili kutafsiri mradi wako mzima (faili za markdown na picha) kwenda lugha moja, kama vile Kikorea, tumia amri ifuatayo:

```bash
translate -l "ko"
```

Amri hii itatafsiri faili zote za markdown na picha kwenda Kikorea, na kuongeza tafsiri mpya bila kufuta zilizopo.

> [!TIP]
>
> Ungependa kujua ni nambari zipi za lugha zinapatikana kwenye **Co-op Translator**? Tembelea sehemu ya [Supported Languages](https://github.com/Azure/co-op-translator#supported-languages) kwenye hazina kwa maelezo zaidi.

#### Mfano kwenye Phi-3 CookBook

Katika **Phi-3 CookBook**, nilitumia njia hii kuongeza tafsiri ya Kikorea kwa faili za markdown na picha zilizopo.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko"
Translating images: 100%|███████████████████████████████████████████████████| 276/276 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 153/153 [1:43:07<00:00, 241.31s/it]
```

### 2. Kutafsiri Lugha Nyingi

Ili kutafsiri mradi wako kwenda lugha nyingi (mfano, Kihispania, Kifaransa, na Kijerumani), tumia amri hii:

```bash
translate -l "es fr de"
```

Amri hii itatafsiri mradi kwenda Kihispania, Kifaransa, na Kijerumani, na kuongeza tafsiri mpya bila kuandika upya zilizopo.

#### Mfano kwenye Phi-3 CookBook

Katika **Phi-3 CookBook**, baada ya kuvuta mabadiliko ya hivi karibuni ili kuonyesha marekebisho mapya, nilitumia njia hii kutafsiri faili mpya za markdown na picha.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko ja zh tw es fr" -a
Translating images: 100%|███████████████████████████████████████████████████| 273/273 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 6/6 [24:07<00:00, 241.31s/it]
```

> [!NOTE]
> Ingawa inashauriwa kutafsiri lugha moja kwa wakati, katika hali kama hii ambapo mabadiliko maalum yanahitaji kuongezwa, kutafsiri lugha nyingi kwa mara moja kunaweza kuwa haraka.

### 3. Kusasisha Tafsiri (Hufuta Tafsiri Zilizopo)

Ili kusasisha tafsiri zilizopo (yaani, kufuta tafsiri za sasa na kuzibadilisha na mpya), tumia chaguo la `-u`. Hii itafuta tafsiri zote zilizopo kwa lugha ulizochagua na kuzitafsiri upya.

```bash
translate -l "ko" -u
```

Tahadhari: Amri hii itakuuliza uthibitisho kabla ya kuendelea na kufuta tafsiri zilizopo.

#### Mfano kwenye Phi-3 CookBook

Katika **Phi-3 CookBook**, nilitumia njia hii kusasisha faili zote zilizotafsiriwa kwa Kihispania. Ninapendekeza kutumia njia hii pale ambapo kuna mabadiliko makubwa kwenye yaliyomo asili kwenye hati nyingi za markdown. Kama kuna faili chache tu za markdown zilizotafsiriwa zinazohitaji kusasishwa, ni bora kufuta faili hizo moja kwa moja na kisha kutumia njia ya `-a` kuongeza tafsiri mpya.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "es" -u
Warning: The update command will delete all existing translations for 'es' and re-translate everything.
Do you want to continue? Type 'yes' to proceed: yes
Proceeding with update...
Translating images: 100%|████████████████████████████████████████████| 150/150 [43:46<00:00, 15.55s/it]
Translating markdown files: 100%|███████████████████████████████████| 95/95 [1:40:27<00:00, 125.62s/it]
```

### 5. Kutafsiri Picha Pekee

Ili kutafsiri faili za picha pekee kwenye mradi wako, tumia chaguo la `-img`:

```bash
translate -l "ko" -img
```

Amri hii itatafsiri picha pekee kwenda Kikorea, bila kugusa faili za markdown.

### 6. Kutafsiri Faili za Markdown Pekee

Ili kutafsiri faili za markdown pekee kwenye mradi wako, tumia chaguo la `-md`:

```bash
translate -l "ko" -md
```

#### Mfano kwenye Phi-3 CookBook

Katika **Phi-3 CookBook**, nilitumia njia hii kukagua makosa ya tafsiri kwenye faili za Kikorea na kujaribu tena kutafsiri faili zozote zilizoonekana kuwa na matatizo.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko" -chk 
Checking translated files for errors in ko...
Checking files for ko: 100%|██████████████████████████████████████████████████| 95/95 [00:01<00:00, 65.47file/s]
Retrying vsc-extension-quickstart.md for ko:   0%|                                     | 0/17 [00:00<?, ?file/s] 
```

Chaguo hili hukagua makosa ya tafsiri. Kwa sasa, kama tofauti ya mapumziko ya mistari kati ya faili asili na iliyotafsiriwa ni zaidi ya sita, faili hiyo inaonekana ina tatizo la tafsiri. Ninapanga kuboresha kigezo hiki ili kiwe na ufanisi zaidi siku zijazo.

Kwa mfano, njia hii ni muhimu kugundua sehemu zilizokosekana au tafsiri zilizoharibika, na itajaribu tena kutafsiri faili hizo moja kwa moja.

Hata hivyo, kama tayari unajua ni faili zipi zina matatizo, ni bora kufuta faili hizo moja kwa moja na kutumia chaguo la `-a` kuzitafsiri upya.

### 8. Hali ya Utatuzi (Debug Mode)

Ili kuwezesha taarifa za kina za utatuzi, tumia chaguo la `-d`:

```bash
translate -l "ko" -d
```

Amri hii itaendesha tafsiri katika hali ya utatuzi, na kutoa taarifa zaidi za logi zitakazokusaidia kutambua matatizo wakati wa mchakato wa tafsiri.

#### Mfano kwenye Phi-3 CookBook

Katika **Phi-3 CookBook**, nilikutana na tatizo ambapo tafsiri zenye viungo vingi kwenye faili za markdown zilisababisha makosa ya muundo, kama vile tafsiri zilizovunjika na mapumziko ya mistari kupuuzwa. Ili kuchunguza tatizo hili, nilitumia chaguo la `-d` kuona jinsi mchakato wa tafsiri unavyofanya kazi.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "ko" -d
DEBUG:openai._base_client:Request options: {'method': 'post', 'url': '/chat/completions', 'headers': {'api-key': 'af04e0bea45747d8a7b8c131c1971044'}, 'files': None, 'json_data': {'messages': [{'role': 'user', 'content': "Translate the following text to ko. NEVER ADD ANY EXTRA CONTENT OUTSIDE THE TRANSLATION. TRANSLATE ONLY WHAT IS GIVEN TO YOU.. MAINTAIN MARKDOWN FORMAT\n\n# Phi-3 Cookbook: Hands-On Examples with Microsoft's Phi-3 Models [![Open and use the samples in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phi-3cookbook) [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%
...
```

### 9. Kutafsiri Lugha Zote

Kama unataka kutafsiri mradi kwenda lugha zote zinazopatikana, tumia neno all.

> [!WARNING]
> Kutafsiri lugha zote kwa mara moja kunaweza kuchukua muda mrefu kulingana na ukubwa wa mradi. Kwa mfano, kutafsiri **Phi-3 CookBook** kwenda Kihispania kulichukua takriban saa 2. Kwa ukubwa huu, si rahisi kwa mtu mmoja kushughulikia lugha 20. Inashauriwa kugawanya kazi kati ya wachangiaji wengi, kila mmoja akisimamia lugha moja au mbili, na kusasisha tafsiri kidogo kidogo.

```bash
translate -l "all"
```

Amri hii itatafsiri mradi kwenda lugha zote zinazopatikana. Ukichagua kuendelea, tafsiri inaweza kuchukua muda mrefu kulingana na ukubwa wa mradi.

> [!TIP]
>
> ### Kufuta Faili Zilizotafsiriwa kwa Mkono (Hiari)
> Faili zilizotafsiriwa sasa zinatambuliwa na kusafishwa moja kwa moja pale faili asili inaposasishwa.
>
> Hata hivyo, kama unataka kusasisha tafsiri kwa mkono - kwa mfano, kurudia faili maalum au kubadilisha tabia ya mfumo - unaweza kutumia amri ifuatayo kufuta matoleo yote ya faili kwenye folda za lugha.
>
> ### Kwenye Windows:
> 1. **Kutumia Command Prompt**:
>    - Fungua Command Prompt.
>    - Nenda kwenye folda yenye faili kwa kutumia amri ya `cd`.
>    - Tumia amri hii kufuta faili:
>      ```
>      del /s *filename*
>      ```
>      Badilisha `filename` na sehemu maalum ya jina la faili unayotafuta. Chaguo la `/s` linatafuta kwenye folda ndogo pia.
>
> 2. **Kutumia PowerShell**:
>    - Fungua PowerShell.
>    - Endesha amri hii:
>      ```powershell
>      Get-ChildItem -Path "C:\YourPath" -Filter "*filename*" -Recurse | Remove-Item -Force
>      ```
>      Badilisha `"C:\YourPath"` na njia ya folda na `filename` na jina maalum.
>
> ### Kwenye macOS/Linux:
> 1. **Kutumia Terminal**:
>   - Fungua Terminal.
>   - Nenda kwenye folda kwa kutumia `cd`.
>   - Tumia amri ya `find`:
>     ```bash
>     find . -type f -name "*filename*" -delete
>     ```
>     Badilisha `filename` na jina maalum.
>
> Hakikisha unakagua faili kabla ya kufuta ili kuepuka kupoteza data kwa bahati mbaya. 
>
> Baada ya kufuta faili unazotaka kubadilisha, endesha tena amri yako ya `translate -l` ili kusasisha mabadiliko ya faili za hivi karibuni.

---

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya kutafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuhakikisha usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati asili katika lugha yake ya awali inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, inashauriwa kutumia huduma ya utafsiri wa kibinadamu wa kitaalamu. Hatutawajibika kwa kutoelewana au tafsiri potofu zitakazotokana na matumizi ya tafsiri hii.