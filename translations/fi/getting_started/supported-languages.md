<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d11fe2b5308a8752a994869658751533",
  "translation_date": "2025-11-30T11:34:48+00:00",
  "source_file": "getting_started/supported-languages.md",
  "language_code": "fi"
}
-->
# Tuetut kielet

Alla oleva taulukko listaa kielet, joita **Co-op Translator** tukee tällä hetkellä. Siinä on kielikoodit, kielten nimet sekä tunnetut ongelmat kunkin kielen kohdalla. Jos haluat lisätä tuen uudelle kielelle, lisää vastaava kielikoodi, nimi ja sopiva fontti tiedostoon `font_language_mappings.yml`, joka löytyy kansiosta `src/co_op_translator/fonts/`, ja tee pull request testauksen jälkeen.

| Kielikoodi    | Kielen nimi          | Fontti                           | RTL-tuki    | Tunnetut ongelmat |
|---------------|----------------------|---------------------------------|-------------|-------------------|
| en            | Englanti             | NotoSans-Medium.ttf             | Ei          | Ei                |
| fr            | Ranska               | NotoSans-Medium.ttf             | Ei          | Ei                |
| es            | Espanja              | NotoSans-Medium.ttf             | Ei          | Ei                |
| de            | Saksa                | NotoSans-Medium.ttf             | Ei          | Ei                |
| ru            | Venäjä               | NotoSans-Medium.ttf             | Ei          | Ei                |
| ar            | Arabia               | NotoSansArabic-Medium.ttf       | Kyllä       | Ei                |
| fa            | Persia (Farsi)       | NotoSansArabic-Medium.ttf       | Kyllä       | Ei                |
| ur            | Urdu                 | NotoSansArabic-Medium.ttf       | Kyllä       | Ei                |
| zh            | Kiina (yksinkertaistettu) | NotoSansCJK-Medium.ttc      | Ei          | Ei                |
| mo            | Kiina (perinteinen, Macao) | NotoSansCJK-Medium.ttc     | Ei          | Ei                |
| hk            | Kiina (perinteinen, Hong Kong) | NotoSansCJK-Medium.ttc | Ei          | Ei                |
| tw            | Kiina (perinteinen, Taiwan) | NotoSansCJK-Medium.ttc      | Ei          | Ei                |
| ja            | Japani               | NotoSansCJK-Medium.ttc          | Ei          | Ei                |
| ko            | Korea                | NotoSansCJK-Medium.ttc          | Ei          | Ei                |
| hi            | Hindi                | NotoSansDevanagari-Medium.ttf   | Ei          | Ei                |
| bn            | Bengali              | NotoSansBengali-Medium.ttf      | Ei          | Ei                |
| mr            | Marathi              | NotoSansDevanagari-Medium.ttf   | Ei          | Ei                |
| ne            | Nepali               | NotoSansDevanagari-Medium.ttf   | Ei          | Ei                |
| pa            | Punjabi (Gurmukhi)   | NotoSansGurmukhi-Medium.ttf     | Ei          | Ei                |
| pt            | Portugali (Portugali)| NotoSans-Medium.ttf             | Ei          | Ei                |
| br            | Portugali (Brasilia) | NotoSans-Medium.ttf             | Ei          | Ei                |
| it            | Italia               | NotoSans-Medium.ttf             | Ei          | Ei                |
| lt            | Liettua              | NotoSans-Medium.ttf             | Ei          | Ei                |
| pl            | Puola                | NotoSans-Medium.ttf             | Ei          | Ei                |
| tr            | Turkki               | NotoSans-Medium.ttf             | Ei          | Ei                |
| el            | Kreikka              | NotoSans-Medium.ttf             | Ei          | Ei                |
| th            | Thai                 | NotoSansThai-Medium.ttf         | Ei          | Ei                |
| sv            | Ruotsi               | NotoSans-Medium.ttf             | Ei          | Ei                |
| da            | Tanska               | NotoSans-Medium.ttf             | Ei          | Ei                |
| no            | Norja                | NotoSans-Medium.ttf             | Ei          | Ei                |
| fi            | Suomi                | NotoSans-Medium.ttf             | Ei          | Ei                |
| nl            | Hollanti             | NotoSans-Medium.ttf             | Ei          | Ei                |
| he            | Heprea               | NotoSansHebrew-Medium.ttf       | Kyllä       | Ei                |
| vi            | Vietnami             | NotoSans-Medium.ttf             | Ei          | Ei                |
| id            | Indonesia            | NotoSans-Medium.ttf             | Ei          | Ei                |
| ms            | Malaiji              | NotoSans-Medium.ttf             | Ei          | Ei                |
| tl            | Tagalog (Filippiinit)| NotoSans-Medium.ttf             | Ei          | Ei                |
| sw            | Swahili              | NotoSans-Medium.ttf             | Ei          | Ei                |
| hu            | Unkari               | NotoSans-Medium.ttf             | Ei          | Ei                |
| cs            | Tšekki               | NotoSans-Medium.ttf             | Ei          | Ei                |
| sk            | Slovakia             | NotoSans-Medium.ttf             | Ei          | Ei                |
| ro            | Romania              | NotoSans-Medium.ttf             | Ei          | Ei                |
| bg            | Bulgaria             | NotoSans-Medium.ttf             | Ei          | Ei                |
| sr            | Serbia (kyrillinen)  | NotoSans-Medium.ttf             | Ei          | Ei                |
| hr            | Kroatia              | NotoSans-Medium.ttf             | Ei          | Ei                |
| sl            | Slovenia             | NotoSans-Medium.ttf             | Ei          | Ei                |
| uk            | Ukraina              | NotoSans-Medium.ttf             | Ei          | Ei                |
| my            | Burman (Myanmar)     | NotoSansMyanmar-Medium.ttf      | Ei          | Ei                |
| ta            | Tamili               | NotoSansTamil-Medium.ttf        | Ei          | Ei                |
| et            | Viro                 | NotoSans-Medium.ttf             | Ei          | Ei                |
| pcm           | Nigerian Pidgin      | NotoSans-Medium.ttf             | Ei          | Ei                |
| te            | Telugu               | NotoSans-Medium.ttf             | Ei          | Ei                |
| ml            | Malayalam            | NotoSans-Medium.ttf             | Ei          | Ei                |
| kn            | Kannada              | NotoSans-Medium.ttf             | Ei          | Ei                |

## Uuden kielen lisääminen

Haluatko lisätä uuden kielen? Noudata seuraavia ohjeita:

- Katso ohjeet kohdasta Contributing: [Contribute a new language](../CONTRIBUTING.md#contribute-a-new-language)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattikäännöksissä saattaa esiintyä virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->