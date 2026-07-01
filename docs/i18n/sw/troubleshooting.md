# Utatuzi wa Matatizo

Tumia ukurasa huu wakati utekelezaji wa tafsiri unafanikisha bila kutarajiwa, unashindwa wakati wa usanidi, au unatengeneza matokeo yanayohitaji ukaguzi.

## Anza Hapa

1. Endesha amri maalum kwanza, kama `translate -l "ko" -md`.
2. Ongeza `-d` kwa logi za ufuatilizi za console.
3. Ongeza `-s` ili kuhifadhi logi za debug chini ya `<root-dir>/logs/`.
4. Endesha `co-op-review` baada ya tafsiri ili kukagua ubora, muundo, na viungo vya ndani.

```bash
translate -l "ko" -md -d -s
co-op-review -l "ko"
```

## Makosa ya Usanidi

### Hakuna Mtoaji wa Mfano wa Lugha

Kosa:

```text
No language model configuration found.
```

Suluhisho:

- Sanidi Azure OpenAI au OpenAI.
- Thibitisha kuwa vigezo vipo katika mazingira ambapo amri inatekelezwa.
- Kwa matumizi ya ndani, ziweke katika `.env` kwenye mzizi wa mradi.

Angalia [Usanidi](configuration.md).

### Tafsiri ya Picha Bila Azure AI Vision

Kosa:

```text
Image translation requested but Azure AI Service is not configured.
```

Suluhisho:

- Ongeza `AZURE_AI_SERVICE_API_KEY`.
- Ongeza `AZURE_AI_SERVICE_ENDPOINT`.
- Au endesha amri ya maandishi pekee kama `translate -l "ko" -md`.

### Ufunguo au Endpoint Batili

Dalili zinaweza kujumuisha `401`, makosa ya ruhusa yaliyofichwa, au makosa ya upatikanaji wa endpoint.

Suluhisho:

- Thibitisha kwamba ufunguo unahusiana na rasilimali ya Azure ile ile kama endpoint.
- Thibitisha rasilimali inasaidia Vision unapotumia `-img`.
- Thibitisha kwamba jina la utekelezaji la Azure OpenAI na toleo la API vinaendana na utekelezaji wako.
- Endesha kwa logi za debug: `translate -l "ko" -md -d -s`.

## Hakuna Faili Zilizotafsiriwa

Sababu za kawaida:

- Bendera zilizochaguliwa hazilingani na faili zako.
- Faili zilizotafsiriwa tayari zipo.
- Faili za chanzo ziko ndani ya saraka zilizotengwa.
- Amri inaendeshwa kutoka mzizi wa mradi usio sahihi.

Ukaguzi:

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -nb --dry-run
translate -l "ko" -img --dry-run
```

Tumia `--root-dir` wakati amri inaendeshwa nje ya mzizi wa mradi.

## Tabia Isiyotarajiwa ya Viungo

Urekebishaji wa viungo unategemea aina za yaliyomo zilizochaguliwa:

- `-nb` imejumuishwa: viungo vya daftari vinaweza kuelekeza kwa daftari zilizotafsiriwa.
- `-nb` haijajumuishwa: viungo vya daftari vinaweza kuendelea kuelekea daftari za chanzo.
- `-img` imejumuishwa: viungo vya picha vinaweza kuelekeza kwa picha zilizotafsiriwa.
- `-img` haijajumuishwa: viungo vya picha vinaweza kuendelea kuelekea picha za chanzo.

Endesha tafsiri kamili ya yaliyomo wakati viungo vyote vya ndani vinapaswa kuonyesha matokeo yaliyotafsiriwa:

```bash
translate -l "ko" -md -nb -img
```

Endesha ukaguzi wa viungo baada ya tafsiri:

```bash
co-op-review -l "ko"
```

## Masuala ya Uonyesho wa Markdown

Iwapo Markdown iliyotafsiriwa inaonekana vibaya:

- Angalia kwamba frontmatter inaanza na kumalizika na `---`.
- Angalia kwamba idadi ya fence za msimbo zinaendana kati ya faili ya chanzo na iliyotafsiriwa.
- Endesha `co-op-review` ili kugundua masuala ya muundo ya kawaida.
- Tafsiri tena faili husika ikiwa matokeo yaliharibika.

```bash
co-op-review -l "ko" --format github
```

## Kitendo cha GitHub kilitekelezwa lakini Hakukuwa na Ombi la Kuvuta (Pull Request) lililotengenezwa

Ikiwa `peter-evans/create-pull-request` inaripoti kwamba tawi halijaenda mbele ya base, mtiririko wa kazi haukupata faili za kujumuisha.

Sababu zinazowezekana:

- Utekelezaji wa tafsiri haukuza mabadiliko.
- `.gitignore` inaondoa `translations/`, `translated_images/`, au daftari zilizotafsiriwa.
- `add-paths` haifanyi muafaka na saraka za matokeo zilizotengenezwa.
- Hatua ya tafsiri ilitoka mapema.

Suluhisho:

1. Thibitisha kwamba faili zilizotengenezwa zipo katika `translations/` au `translated_images/`.
2. Thibitisha `.gitignore` haizuii matokeo yaliyotengenezwa.
3. Tumia `add-paths` inayolingana:

   ```yaml
   with:
     add-paths: |
       translations/
       translated_images/
   ```

4. Kwa muda ongeza bendera za debug kwenye amri ya translate:

   ```bash
   translate -l "ko" -md -d -s
   ```

5. Thibitisha ruhusa za mtiririko wa kazi zinajumuisha:

   ```yaml
   permissions:
     contents: write
     pull-requests: write
   ```

## Ubora wa Tafsiri

Tafsiri za mashine zinaweza kuhitaji ukaguzi wa binadamu. Tumia `evaluate` tu unapotaka upimaji wa ubora wa majaribio na mitiririko ya kazi ya urejesho wa uaminifu mdogo.

!!! warning "Experimental"
    `evaluate` inaweza kutumia ukaguzi wa msingi wa sheria na ukaguzi wa msingi wa LLM, na modeli yake ya alama na tabia ya metadata zinaweza kubadilika. Usituweke katika vizingiti vya CI vinavyohitajika isipokuwa mtiririko wako wa kazi uko tayari kwa mabadiliko.

Kwa ukaguzi uliothabiti wa CI, tumia `co-op-review` badala yake.