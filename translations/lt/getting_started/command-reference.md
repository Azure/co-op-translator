<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a6cddf5e9648ef0bba0de7eb07e74cf1",
  "translation_date": "2025-10-15T04:46:31+00:00",
  "source_file": "getting_started/command-reference.md",
  "language_code": "lt"
}
-->
# Komandų nuoroda

**Co-op Translator** CLI siūlo įvairias parinktis, leidžiančias pritaikyti vertimo procesą:

Komanda                                       | Aprašymas
----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"                 | Išverčia jūsų projektą į nurodytas kalbas. Pavyzdys: translate -l "es fr de" išvers į ispanų, prancūzų ir vokiečių kalbas. Naudokite translate -l "all", kad išverstumėte į visas palaikomas kalbas.
translate -l "language_codes" -u              | Atnaujina vertimus ištrindamas esamus ir sukuriant juos iš naujo. Įspėjimas: tai ištrins visus dabartinius nurodytų kalbų vertimus.
translate -l "language_codes" -img            | Verčia tik paveikslėlių failus.
translate -l "language_codes" -md             | Verčia tik Markdown failus.
translate -l "language_codes" -nb             | Verčia tik Jupyter užrašų knygų failus (.ipynb).
translate -l "language_codes" --fix           | Iš naujo verčia failus, kurių pasitikėjimo balai yra žemi, remiantis ankstesnių vertinimų rezultatais.
translate -l "language_codes" -d              | Įjungia derinimo režimą detaliam žurnalo rašymui.
translate -l "language_codes" --save-logs, -s | Išsaugo DEBUG lygio žurnalus į failus <root_dir>/logs/ (konsolė lieka valdoma per -d)
translate -l "language_codes" -r "root_dir"   | Nurodo projekto šakninį katalogą
translate -l "language_codes" -f              | Naudoja greitą režimą paveikslėlių vertimui (iki 3 kartų greitesnis braižymas, šiek tiek prastesnė kokybė ir išdėstymas).
translate -l "language_codes" -y              | Automatiškai patvirtina visus užklausimus (naudinga CI/CD procesams)
translate -l "language_codes" --help          | Pagalbos informacija CLI viduje, rodanti galimas komandas
evaluate -l "language_code"                  | Įvertina vertimo kokybę konkrečiai kalbai ir pateikia pasitikėjimo balus
evaluate -l "language_code" -c 0.8           | Įvertina vertimus su pasirinktu pasitikėjimo slenksčiu
evaluate -l "language_code" -f               | Greitas vertinimo režimas (tik pagal taisykles, be LLM)
evaluate -l "language_code" -D               | Gilus vertinimo režimas (tik LLM pagrindu, išsamesnis, bet lėtesnis)
evaluate -l "language_code" --save-logs, -s  | Išsaugo DEBUG lygio žurnalus į failus <root_dir>/logs/
migrate-links -l "language_codes"             | Iš naujo apdoroja išverstus Markdown failus, kad atnaujintų nuorodas į užrašų knygas (.ipynb). Pirmenybė teikiama išverstoms užrašų knygoms, jei jos yra; kitaip gali būti naudojamos originalios.
migrate-links -l "language_codes" -r          | Nurodykite projekto šakninį katalogą (numatytas: dabartinis katalogas).
migrate-links -l "language_codes" --dry-run   | Parodo, kurie failai būtų pakeisti, bet nieko neįrašo.
migrate-links -l "language_codes" --no-fallback-to-original | Neperrašyti nuorodų į originalias užrašų knygas, kai išverstų nėra (atnaujinti tik kai išversta egzistuoja).
migrate-links -l "language_codes" -d          | Įjungti derinimo režimą detaliam žurnalo rašymui.
migrate-links -l "language_codes" --save-logs, -s | Išsaugo DEBUG lygio žurnalus į failus <root_dir>/logs/
migrate-links -l "all" -y                      | Apdoroja visas kalbas ir automatiškai patvirtina įspėjimo užklausą.

## Naudojimo pavyzdžiai

  1. Numatytoji elgsena (prideda naujus vertimus neištrindamas esamų):   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. Prideda tik naujus korėjiečių paveikslėlių vertimus (esami vertimai neištrinami):    translate -l "ko" -img

  3. Atnaujina visus korėjiečių vertimus (Įspėjimas: tai ištrins visus esamus korėjiečių vertimus prieš išverčiant iš naujo):    translate -l "ko" -u

  4. Atnaujina tik korėjiečių paveikslėlius (Įspėjimas: tai ištrins visus esamus korėjiečių paveikslėlius prieš išverčiant iš naujo):    translate -l "ko" -img -u

  5. Prideda naujus Markdown vertimus korėjiečių kalbai, nekeičiant kitų vertimų:    translate -l "ko" -md

  6. Taiso žemo pasitikėjimo vertimus pagal ankstesnių vertinimų rezultatus: translate -l "ko" --fix

  7. Taiso žemo pasitikėjimo vertimus tik tam tikriems failams (Markdown): translate -l "ko" --fix -md

  8. Taiso žemo pasitikėjimo vertimus tik tam tikriems failams (paveikslėliai): translate -l "ko" --fix -img

  9. Naudoja greitą režimą paveikslėlių vertimui:    translate -l "ko" -img -f

  10. Taiso žemo pasitikėjimo vertimus su pasirinktu slenksčiu: translate -l "ko" --fix -c 0.8

  11. Derinimo režimo pavyzdys: - translate -l "ko" -d: Įjungia derinimo žurnalus.
  12. Išsaugo žurnalus į failus: translate -l "ko" -s
  13. Konsolės DEBUG ir failo DEBUG: translate -l "ko" -d -s

  14. Migruoja užrašų knygų nuorodas korėjiečių vertimams (atnaujina nuorodas į išverstas užrašų knygas, jei yra):    migrate-links -l "ko"

  15. Migruoja nuorodas su „dry-run“ (be failų rašymo):    migrate-links -l "ko" --dry-run

  16. Atnaujina nuorodas tik kai išverstos užrašų knygos egzistuoja (negrįžta prie originalų):    migrate-links -l "ko" --no-fallback-to-original

  17. Apdoroja visas kalbas su patvirtinimo užklausa:    migrate-links -l "all"

  18. Apdoroja visas kalbas ir automatiškai patvirtina:    migrate-links -l "all" -y
  19. Išsaugo žurnalus į failus migrate-links komandai:    migrate-links -l "ko ja" -s

### Vertinimo pavyzdžiai

> [!WARNING]  
> **Beta funkcija**: Vertinimo funkcionalumas šiuo metu yra beta versijoje. Ši funkcija išleista vertintiems išverstus dokumentus, o vertinimo metodai ir detalus įgyvendinimas dar kuriami ir gali keistis.

  1. Įvertinti korėjiečių vertimus: evaluate -l "ko"

  2. Įvertinti su pasirinktu pasitikėjimo slenksčiu: evaluate -l "ko" -c 0.8

  3. Greitas vertinimas (tik pagal taisykles): evaluate -l "ko" -f

  4. Gilus vertinimas (tik LLM pagrindu): evaluate -l "ko" -D

---

**Atsakomybės atsisakymas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojame profesionalų žmogaus vertimą. Mes neatsakome už nesusipratimus ar neteisingą interpretavimą, kilusį naudojantis šiuo vertimu.