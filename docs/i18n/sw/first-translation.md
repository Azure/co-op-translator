# Tafsiri, hariri, na hakiki mradi mdogo

Anza na mafaili mafupi mawili ya Markdown na lugha moja ya lengo. Utaona wapi tafsiri zinaandikwa, kinachotokea wakati chanzo kinabadilika, na jinsi ya kukagua matokeo.

## Matokeo yaliyorekodiwa

Mfano ulifanyika tarehe 19 Septemba, 2026 kwa kutumia Co-op Translator 0.21.0 na Azure OpenAI (`gpt-5-mini`). Amri za CLI zisizobadilishwa zilitumika kupitia Click's `CliRunner` kwa kutumia wheel iliyojengwa na utegemezi wa Python uliopo.

| Hatua | Matokeo |
| --- | --- |
| Mapitio | Exit 0; hakuna ombi la tafsiri la modeli |
| Tafsiri ya awali | Exit 0; 27.36 sekunde |
| Ukaguzi wa awali | Exit 0 |
| Hariri README na hakiki | Exit 1; Tafsiri iliyochakaa imegunduliwa |
| Sasisha tafsiri | Exit 0; 22.17 sekunde |
| Hakiki baada ya sasisho | Exit 0; hakuna makosa au onyo |
| Mwongozo usiobadilika | Bayti sawa kabla na baada ya sasisho la README |
| Endesha tena | Exit 0; hashi sawa kwa faili zote za tafsiri |

Hizi ni vipimo vya kila utekelezaji, si dhamana za utendaji. Muda wa usanidi haujumuishwi; malipo ya mtoa huduma hayakupimwa. Utekelezaji usiobadilika bado unaweza kufanya ukaguzi wa afya wa mtoa huduma.

Kagua [tafsiri ya awali](../../assets/demo/before.txt), [tafsiri iliyosasishwa](../../assets/demo/after.txt), [tofauti kamili ya tafsiri](../../assets/demo/update.diff), [mapitio ya zamani](../../assets/demo/review-stale.txt), [mapitio ya mwisho](../../assets/demo/review-after.txt), na [maelezo ya utekelezaji](../../assets/demo/results.json). Tafsiri ya faili nzima inaweza kubadilisha maneno mengine, kama tofauti iliyorekodiwa inavyoonyesha. Nakala za maandishi zote mbili zinahifadhi kukanusho lililotengenezwa.

Ukaguzi wa binadamu bado una umuhimu: sasisho lililorekodiwa linatumia `[사용 가이드](guide.md)을`; kiambishi cha Kikorea kinapaswa kuwa `[사용 가이드](guide.md)를`. Nakala za maandishi zinahifadhi matokeo haya bila kubadilishwa badala ya kuonyesha tafsiri iliyohaririwa kama matokeo ya modeli. Mapitio ya kimuundo yanapitisha licha ya tatizo hili la uandishi.

## 1. Andaa folda ndogo

Tumia Python 3.11–3.14 na [usanidi wa mazingira ya virtual](configuration.md#local-runtime-setup). Sakinisha toleo linalotumika kwa mfano huu:

```bash
python -m pip install co-op-translator==0.21.0
mkdir translation-demo
cd translation-demo
git init
```

Pakua [README.txt](../../assets/demo/README.txt) na [guide.txt](../../assets/demo/guide.txt) kwenye folda hii, ukiwahifadhi kama `README.md` na `guide.md`. Ni nyaraka ndogo za mradi wa kubuni tu; hakuna usakinishaji wa programu unahitajika.

README ina sehemu ya msimbo na kiungo kwa `guide.md`. Sentensi yake ya mwisho ni:

```text
Notes are saved locally.
```

Hifadhi tu nyaraka hizi mbili za chanzo kwenye folda hii. Amri zote zinazofuata zinatekelezwa ndani ya `translation-demo` na zinafanya kazi katika Bash na PowerShell.

## 2. Tazama bila nyaraka za utambulisho

```bash
translate -l "ko" -md --dry-run
```

Muonekano wa awali unakadiria kazi ya tafsiri bila kuita modeli au kuandika tafsiri. Makadirio ya tokeni si nukuu ya bili. Utekelezaji wa kwanza unapaswa kutambua mafaili yote ya Markdown kama kazi mpya.

## 3. Chagua mtoa huduma na tafsiri

Sanidi mtoa huduma mmoja kwa kutumia [mwongozo wa usanidi](configuration.md): Azure OpenAI, OpenAI, au Anthropic. Tafsiri za maandishi za OpenAI na Anthropic hazihitaji akaunti ya Azure. Huduma za picha hazihitajiki kwa mfano huu.

Ikiwa unatumia faili ya `.env` ya ndani, ongeza `.env` kwa `.gitignore` ya folda hii. Miito ya tafsiri hutumia akaunti yako ya mtoa huduma na inaweza kusababisha malipo.

```bash
translate -l "ko" -md
co-op-review -l "ko"
```

Fungua `translations/ko/README.md` na `translations/ko/guide.md`. Kagua matumizi ya maneno ya Kikorea, blok ya msimbo, na kiungo kutoka README iliyotafsiriwa kuelekea mwongozo uliotafsiriwa. Maneno ya matokeo yanatofautiana kwa kila modeli.

`co-op-review` inakagua ikiwa ni mpya, muundo, na viungo vya ndani. Matokeo yaliyofaulu hayahakikisha usahihi wa kitenzi. Rekebisha makosa yoyote yaliyoripotiwa kabla ya kuendelea.

Rekodi msingi uliofanikiwa kwa Git (sanidi utambulisho wako wa Git kwanza ikiwa inahitajika):

```bash
git add README.md guide.md translations
git commit -m "Record initial Korean translation"
```

## 4. Badilisha chanzo

Katika `README.md`, badilisha `Notes are saved locally.` kwa:

```text
Notes are saved locally as Markdown files.
```

Acha `guide.md` isivyobadilishwa. Kisha endesha:

```bash
co-op-review -l "ko"
translate -l "ko" -md --dry-run
```

Ukaguzi unapaswa kuripoti tafsiri ya README kama iliyochakaa na kuishia kwa kushindikana. Hili ndilo hali ya kati inayotarajiwa. Muonekano wa awali unapaswa kutambua kazi kwa README iliyobadilishwa.

## 5. Sasisha na kagua tofauti

```bash
translate -l "ko" -md
git diff -- README.md translations/ko/README.md
git diff -- translations/ko/guide.md
co-op-review -l "ko"
```

Kagua tofauti halisi: CLI ya chaguo-msingi inatafsiri tena faili iliyobadilishwa, hivyo modeli pia inaweza kusahihisha maneno mengine katika faili hiyo. Mwongozo usiobadilika haupaswi kuwa na tofauti. Ukaguzi haipaswi tena kuripoti README kama iliyochakaa; chunguza matokeo mengine yoyote badala ya kuyaacha.

Uhifadhi wa ngazi-ya-bloki wa uhariri wa Markdown unaofanywa na binadamu unahitaji mtoa hali ya tafsiri wa hiari katika the [Python API](api.md). Haijawezeshwa na amri hizi za CLI.

## 6. Endesha tena bila mabadiliko

Fanya commit kwa chanzo na tafsiri zilizosasishwa:

```bash
git add README.md translations
git commit -m "Update Korean translation after source edit"
translate -l "ko" -md
git diff --exit-code -- translations
```

Kwa tafsiri zilizopo na usanidi usiobadilika, mtafsiri atapuuza faili hizo. Amri ya mwisho ya Git inapaswa kutoa hakuna tofauti na kutoka kwa mafanikio.

## Hatua zinazofuata

- [Tafsiri README tu na fungua pull request](github-actions.md#your-first-readme-translation-pr).
- [Chagua CLI, Python API, au MCP](workflows.md).
- [Ripoti tatizo la tafsiri bila kuandika msimbo](https://github.com/Azure/co-op-translator/issues/new?template=translation_feedback.yml).