# Kuchangia maboresho ya lugha

Ujuzi wako wa lugha unaweza kusaidia kuboresha Co-op Translator. Anza kwa mfano, marekebisho yaliyopendekezwa, na maelezo kwa kutumia [fomu ya maoni ya tafsiri](https://github.com/Azure/co-op-translator/issues/new?template=translation_feedback.yml). Huna haja ya kuandika msimbo au kulipa kwa uendeshaji wa modeli.

## Kutoka kwa ripoti hadi maboresho ya pamoja

1. Mchangiaji hutoa kifungu cha chanzo, tafsiri yake, na muktadha.
2. Mkaguzi wa lugha anakagua maana, uhalisia wa matumizi ya lugha, na kama pendekezo linategemea eneo fulani au kozi.
3. Msimamizi huamua ikiwa suluhisho linastahili kuwa kwenye kozi ya chanzo, maelekezo ya lugha ya pamoja, usanidi wa istilahi, au msimbo wa tafsiri.
4. Kwa sheria ya pamoja, msimamizi analinganisha matokeo kabla na baada ya mabadiliko kwenye mfano ulioripotiwa na mifano isiyohusiana. Wachangiaji wanaweza kupitia matokeo haya bila kuendesha zana wenyewe.
5. PR inayotokana inaunganisha ripoti na kutoa sifa kwa watu walio toa mifano na ukaguzi. Utekelezaji au kuzalisha upya katika hazina zinazotumia ni hatua tofauti.

Ripoti haiibadili moja kwa moja maagizo au kuanzisha upya tafsiri za kozi. Marekebisho maalum ya kozi yanapaswa kubaki kuunganishwa na hazina ya kozi. Usidhani mabadiliko ya mkono yataishi baada ya tafsiri upya baadaye; thibitisha mwenendo huo wa kazi.

## Mfano uliopo: Viungo vya Markdown vya Kijapani

The [Japanese instruction file](https://github.com/Azure/co-op-translator/blob/main/src/co_op_translator/templates/language/ja.md) inamwambia modeli kutafsiri maandishi ya kiungo huku ikihifadhi sintaksia ya Markdown na marudio ya kiungo. Kwa mfano, kiungo kilichoandikwa kama `[text](URL)` hakipaswi kuwa `「text」（URL）`.

Huu ni mfano uliolengwa wa sheria ya lugha unaothibitishwa na mchoro wa matokeo sahihi na yasiyo sahihi. Hii si ushahidi kwamba maagizo pekee yanahakikisha Markdown sahihi.

The [Markdown prompt builder](https://github.com/Azure/co-op-translator/blob/main/src/co_op_translator/utils/markdown/prompts.py) inachoma `templates/language/<language_code>.md` kwa kutumia nambari ya lugha iliyoandikwa kwa herufi ndogo na iliyokatwa sehemu zisizo za lazima. Ikiwa hakuna faili, inatumia maelekezo ya kawaida. Hii inaelezea njia ya prompt ya Markdown; usidhani kila picha au njia nyingine ya tafsiri inatumia maelekezo yale yale.

The [prompt tests](https://github.com/Azure/co-op-translator/blob/main/tests/co_op_translator/utils/markdown/test_prompts.py) huangalia kwamba maelekezo ya Kijapani yamejumuishwa. Hiyo inathibitisha uundaji wa prompt, si ubora wa tafsiri.

## Nini kinapaswa kuwa katika sheria ya lugha?

Pendekeza marekebisho nyembamba yanayoweza kurudiwa na mfano wa chanzo, tabia inayotarajiwa, na mfano wa kinyume ambapo sheria haipaswi kutumika. Hifadhi maana, placeholders, msimbo, URLs, na muundo wa hati. Epuka kubadilisha upendeleo wa mtindo wa mtu mmoja au istilahi ya kozi moja kuwa sheria ya ulimwengu.

The current [glossary implementation](https://github.com/Azure/co-op-translator/blob/main/src/co_op_translator/glossary.py) inalinda istilahi dhidi ya tafsiri. Sio kamusi ya istilahi kutoka chanzo hadi lengwa. Jadili tabia mpya ya istilahi kabla ya kuiahidi wachangiaji.

## Mfano wa jumuiya: ripoti ya jina la bidhaa ya Kijapani

Katika [ripoti #527](https://github.com/Azure/co-op-translator/issues/527), @hyoshioka0128 alitambua tafsiri ya Kijapani iliyobadilisha jina la bidhaa `Co-op Translator` kuwa `Co-op 翻訳`. Ripoti ilijumuisha kiungo kwa dokumenti iliyohusishwa na skrini, ikifanya tatizo liwe rahisi kupata.

Mchangiaji pia aliunganisha [PR ya kozi inayohusiana](https://github.com/microsoft/AZD-for-beginners/pull/109). Katika mjadala wa tatizo, msimamizi alikiri ripoti na kupendekeza kuchunguza kwa nini jina lilibadilika, ikiwa ni pamoja na ulinzi wa istilahi, tabia ya kamusi, na njia ya tafsiri.

Hii inaonyesha jinsi ripoti ndogo inaweza kusaidia uchunguzi zaidi ya marekebisho ya maneno ya mtu mmoja. Hii sio matokeo yaliyothibitishwa ya kabla/baada wala ushahidi kwamba maagizo ya viungo vya Markdown ya Kijapani yaliyo hapo juu yalitatua tatizo la jina la bidhaa.

Unaweza kuchangia kwa njia ile ile: shiriki maandishi ya awali, tafsiri ya sasa, marekebisho yaliyopendekezwa, na kwa nini ni muhimu. Ongeza kiungo cha dokumenti au skrini (screenshot) inapofaa. Huna haja ya kuchunguza chanzo au kuandika prompt kabla ya kuripoti.

## Uthibitishaji kabla ya kupitisha sheria

Tumia sampuli za chanzo zile zile, marekebisho ya mtafsiri, mtoa huduma/modeli, na mipangilio ya uzalishaji kwa mbio za msingi na za mgombea, ukibadilisha tu maagizo yaliyopendekezwa. Rekodi mabadiliko halisi ya prompt na matokeo; rudia mifano inapohitajika kutofautisha athari thabiti na mabadiliko ya matokeo. Jumuisha kosa lililoripotiwa, muktadha wa ulinganisho, na mifano ambayo tayari inatafsiriwa kwa usahihi.

| Sampuli | Chanzo/muktadha | Matokeo ya msingi | Matokeo ya mgombea | Tathmini ya mkaguzi |
| --- | --- | --- | --- | --- |
| Kosa lililoripotiwa | Kukusanywa | Haijakimbizwa | Haijakimbizwa | Inasubiri |
| Mfano wa kinyume | Kukusanywa | Haijakimbizwa | Haijakimbizwa | Inasubiri |
| Mfano usioathiriwa | Kukusanywa | Haijakimbizwa | Haijakimbizwa | Inasubiri |

Angalia uhakika wa miundo tofauti na maamuzi ya kielimu. Jaribio linalofaulu la kupakia prompt sio tathmini ya ubora, na sentensi moja inayotarajiwa sio tafsiri pekee sahihi. Ikiwa muktadha, mbio za modeli, au ukaguzi wa lugha vinakosekana, acha pendekezo likisubiri badala ya kudai kwamba suala limetatuliwa.