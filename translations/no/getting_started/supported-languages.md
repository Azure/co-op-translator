<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d11fe2b5308a8752a994869658751533",
  "translation_date": "2025-11-30T11:30:53+00:00",
  "source_file": "getting_started/supported-languages.md",
  "language_code": "no"
}
-->
# Støttede språk

Tabellen nedenfor viser språkene som for øyeblikket støttes av **Co-op Translator**. Den inkluderer språkkoder, språknavn og eventuelle kjente problemer knyttet til hvert språk. Hvis du ønsker å legge til støtte for et nytt språk, vennligst legg til den tilsvarende språkkoden, navnet og passende font i filen `font_language_mappings.yml` som ligger i `src/co_op_translator/fonts/`, og send inn en pull request etter testing.

| Språkkode    | Språknavn            | Font                              | RTL-støtte | Kjente problemer |
|--------------|----------------------|----------------------------------|------------|------------------|
| en           | Engelsk              | NotoSans-Medium.ttf              | Nei        | Nei              |
| fr           | Fransk               | NotoSans-Medium.ttf              | Nei        | Nei              |
| es           | Spansk               | NotoSans-Medium.ttf              | Nei        | Nei              |
| de           | Tysk                 | NotoSans-Medium.ttf              | Nei        | Nei              |
| ru           | Russisk              | NotoSans-Medium.ttf              | Nei        | Nei              |
| ar           | Arabisk              | NotoSansArabic-Medium.ttf        | Ja         | Nei              |
| fa           | Persisk (Farsi)      | NotoSansArabic-Medium.ttf        | Ja         | Nei              |
| ur           | Urdu                 | NotoSansArabic-Medium.ttf        | Ja         | Nei              |
| zh           | Kinesisk (forenklet) | NotoSansCJK-Medium.ttc           | Nei        | Nei              |
| mo           | Kinesisk (tradisjonell, Macau) | NotoSansCJK-Medium.ttc  | Nei        | Nei              |
| hk           | Kinesisk (tradisjonell, Hong Kong) | NotoSansCJK-Medium.ttc | Nei        | Nei              |
| tw           | Kinesisk (tradisjonell, Taiwan) | NotoSansCJK-Medium.ttc   | Nei        | Nei              |
| ja           | Japansk              | NotoSansCJK-Medium.ttc           | Nei        | Nei              |
| ko           | Koreansk             | NotoSansCJK-Medium.ttc           | Nei        | Nei              |
| hi           | Hindi                | NotoSansDevanagari-Medium.ttf    | Nei        | Nei              |
| bn           | Bengalsk             | NotoSansBengali-Medium.ttf       | Nei        | Nei              |
| mr           | Marathi              | NotoSansDevanagari-Medium.ttf    | Nei        | Nei              |
| ne           | Nepali               | NotoSansDevanagari-Medium.ttf    | Nei        | Nei              |
| pa           | Punjabi (Gurmukhi)   | NotoSansGurmukhi-Medium.ttf      | Nei        | Nei              |
| pt           | Portugisisk (Portugal)| NotoSans-Medium.ttf             | Nei        | Nei              |
| br           | Portugisisk (Brasil) | NotoSans-Medium.ttf              | Nei        | Nei              |
| it           | Italiensk            | NotoSans-Medium.ttf              | Nei        | Nei              |
| lt           | Litauisk             | NotoSans-Medium.ttf              | Nei        | Nei              |
| pl           | Polsk                | NotoSans-Medium.ttf              | Nei        | Nei              |
| tr           | Tyrkisk              | NotoSans-Medium.ttf              | Nei        | Nei              |
| el           | Gresk                | NotoSans-Medium.ttf              | Nei        | Nei              |
| th           | Thai                 | NotoSansThai-Medium.ttf          | Nei        | Nei              |
| sv           | Svensk               | NotoSans-Medium.ttf              | Nei        | Nei              |
| da           | Dansk                | NotoSans-Medium.ttf              | Nei        | Nei              |
| no           | Norsk                | NotoSans-Medium.ttf              | Nei        | Nei              |
| fi           | Finsk                | NotoSans-Medium.ttf              | Nei        | Nei              |
| nl           | Nederlandsk          | NotoSans-Medium.ttf              | Nei        | Nei              |
| he           | Hebraisk             | NotoSansHebrew-Medium.ttf        | Ja         | Nei              |
| vi           | Vietnamesisk         | NotoSans-Medium.ttf              | Nei        | Nei              |
| id           | Indonesisk           | NotoSans-Medium.ttf              | Nei        | Nei              |
| ms           | Malayisk             | NotoSans-Medium.ttf              | Nei        | Nei              |
| tl           | Tagalog (Filippinsk) | NotoSans-Medium.ttf              | Nei        | Nei              |
| sw           | Swahili              | NotoSans-Medium.ttf              | Nei        | Nei              |
| hu           | Ungarsk              | NotoSans-Medium.ttf              | Nei        | Nei              |
| cs           | Tsjekkisk            | NotoSans-Medium.ttf              | Nei        | Nei              |
| sk           | Slovakisk            | NotoSans-Medium.ttf              | Nei        | Nei              |
| ro           | Rumensk              | NotoSans-Medium.ttf              | Nei        | Nei              |
| bg           | Bulgarsk             | NotoSans-Medium.ttf              | Nei        | Nei              |
| sr           | Serbisk (kyrillisk)  | NotoSans-Medium.ttf              | Nei        | Nei              |
| hr           | Kroatisk             | NotoSans-Medium.ttf              | Nei        | Nei              |
| sl           | Slovensk             | NotoSans-Medium.ttf              | Nei        | Nei              |
| uk           | Ukrainsk             | NotoSans-Medium.ttf              | Nei        | Nei              |
| my           | Burmesisk (Myanmar)  | NotoSansMyanmar-Medium.ttf       | Nei        | Nei              |
| ta           | Tamil                | NotoSansTamil-Medium.ttf         | Nei        | Nei              |
| et           | Estisk               | NotoSans-Medium.ttf              | Nei        | Nei              |
| pcm          | Nigeriansk pidgin    | NotoSans-Medium.ttf              | Nei        | Nei              |
| te           | Telugu               | NotoSans-Medium.ttf              | Nei        | Nei              |
| ml           | Malayalam            | NotoSans-Medium.ttf              | Nei        | Nei              |
| kn           | Kannada              | NotoSans-Medium.ttf              | Nei        | Nei              |

## Legge til et nytt språk

Interessert i å legge til et nytt språk? Vennligst følg bidragsveiledningen:

- Se Contributing: [Bidra med et nytt språk](../CONTRIBUTING.md#contribute-a-new-language)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vennligst vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->