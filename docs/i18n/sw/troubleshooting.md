# Utatuzi wa matatizo

Tumia ukurasa huu wakati mchakato wa tafsiri umefanikiwa bila kutarajiwa, umeanguka wakati wa usanidi, au umetengeneza matokeo yanayohitaji ukaguzi.

## Anza Hapa

1. Endesha amri maalum kwanza, kwa mfano `translate -l "ko" -md`.
2. Ongeza `-d` kwa kumbukumbu za utatuzi za konsole.
3. Ongeza `-s` ili kuhifadhi kumbukumbu za utatuzi chini ya `<root-dir>/logs/`.
4. Endesha `co-op-review` baada ya tafsiri ili kukagua kusasishwa, muundo, na viungo vya ndani.

```bash
translate -l "ko" -md -d -s
co-op-review -l "ko"
```

## Makosa ya Usanidi

### Hakuna Mtoaji wa Mfano wa Lugha

Hitilafu:

```text
No language model configuration found.
```

Suluhisho:

- Sanidi Azure OpenAI, OpenAI, au Anthropic.
- Thibitisha kuwa vigezo viko katika mazingira ambapo amri inaendeshwa.
- Kwa matumizi ya ndani, weka katika `.env` kwenye mizizi ya mradi.

Angalia [Usanidi](configuration.md).

### Tafsiri ya Picha Bila Azure AI Vision

Hitilafu:

```text
Image translation requested but Azure AI Service is not configured.
```

Suluhisho:

- Ongeza `AZURE_AI_SERVICE_API_KEY`.
- Ongeza `AZURE_AI_SERVICE_ENDPOINT`.
- Au endesha amri ya maandishi pekee kama `translate -l "ko" -md`.

### Funguo au Endpoint Isiyosahihi

Dalili zinaweza kujumuisha `401`, makosa ya ruhusa yaliyofichwa, au makosa ya upatikanaji wa endpoint.

Suluhisho:

- Thibitisha kuwa funguo ni ya rasilimali ile ile ya Azure kama endpoint.
- Thibitisha kuwa rasilimali inasaidia Vision wakati unatumia `-img`.
- Thibitisha jina la deployment la Azure OpenAI na toleo la API vinavyolingana na utekelezaji wako.
- Endesha na kumbukumbu za utatuzi: `translate -l "ko" -md -d -s`.

## Hakuna Faili Zilizotafsiriwa

Sababu za kawaida:

- Bendera zilizochaguliwa hazilingani na faili zako.
- Faili za tafsiri zilizokuwepo tayari zipo.
- Faili za chanzo ziko chini ya saraka zilizotengwa.
- Amri inaendeshwa kutoka mizizi ya mradi isiyo sahihi.

Ukaguzi:

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -nb --dry-run
translate -l "ko" -img --dry-run
```

Tumia `--root-dir` wakati amri inaendeshwa nje ya mizizi ya mradi.

## Tabia isiyotarajiwa ya Viungo

Kurekebisha viungo kunategemea aina za maudhui zilizochaguliwa:

- `-nb` imejumuishwa: viungo vya daftari vinaweza kuelekeza kwa daftari zilizotafsiriwa.
- `-nb` imeondolewa: viungo vya daftari vinaweza kubaki kuelekeza kwenye daftari za chanzo.
- `-img` imejumuishwa: viungo vya picha vinaweza kuelekeza kwa picha zilizotafsiriwa.
- `-img` imeondolewa: viungo vya picha vinaweza kubaki kuelekeza kwa picha za chanzo.

Endesha tafsiri kamili ya maudhui wakati viungo vyote vya ndani vinapaswa kuipa kipaumbele matokeo yaliyotafsiriwa:

```bash
translate -l "ko" -md -nb -img
```

Endesha ukaguzi wa viungo baada ya tafsiri:

```bash
co-op-review -l "ko"
```

## Masuala ya Uwasilishaji wa Markdown

Kama Markdown iliyotafsiriwa inaonekana vibaya:

- Angalia kwamba frontmatter inaanza na inamalizika na `---`.
- Hakiki kuwa idadi ya mipaka ya msimbo inalingana kati ya faili za chanzo na zilizotafsiriwa.
- Endesha `co-op-review` ili kugundua masuala ya kawaida ya muundo.
- Tafsiri tena faili husika ikiwa matokeo yaliharibika.

```bash
co-op-review -l "ko" --format github
```

## GitHub Action Imeendeshwa Lakini Hakukuwa na Ombi la Pull Liliundwa

Ikiwa `peter-evans/create-pull-request` inaripoti kuwa tawi halija mbele ya msingi, mtiririko wa kazi haukupata faili za kucommit.

Sababu zinazoweza kuwa za kweli:

- Uendeshaji wa tafsiri haukukusanya mabadiliko yoyote.
- `.gitignore` inatoa `translations/`, `translated_images/`, au daftari zilizotafsiriwa.
- `add-paths` haifanyi mechi na saraka za matokeo zilizotengenezwa.
- Hatua ya tafsiri ilitoka mapema.

Suluhisho:

1. Thibitisha kwamba faili zilizotengenezwa zipo katika `translations/` au `translated_images/`.
2. Thibitisha kuwa `.gitignore` haijapuuza matokeo yaliyotengenezwa.
3. Tumia `add-paths` inayolingana:

   ```yaml
   with:
     add-paths: |
       translations/
       translated_images/
   ```

4. Kwa muda mfupi ongeza bendera za utatuzi kwa amri ya translate:

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

Tafsiri za mashine zinaweza kuhitaji ukaguzi wa binadamu. Tumia `evaluate` tu unapotaka alama za ubora za majaribio na michakato ya ukarabati yenye uaminifu mdogo.

!!! warning "Experimental"
    `evaluate` inaweza kutumia ukaguzi unaotegemea sheria na ukaguzi unaotegemea LLM, na modeli yake ya upimaji na tabia ya metadata zinaweza kubadilika. Usiyoiweke katika vizingiti vinavyotakiwa vya CI isipokuwa mtiririko wako wa kazi uko tayari kwa mabadiliko.

Kwa ukaguzi thabiti wa CI, tumia `co-op-review` badala yake.