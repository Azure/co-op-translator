<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "822238e4451d04bb152cebb1be6f13c2",
  "translation_date": "2025-11-30T12:53:22+00:00",
  "source_file": "getting_started/command-reference.md",
  "language_code": "lt"
}
-->
# Komandų nuoroda

**Co-op Translator** CLI siūlo keletą parinkčių, leidžiančių pritaikyti vertimo procesą:

Komanda                                      | Aprašymas
---------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"                 | Išverčia jūsų projektą į nurodytas kalbas. Pavyzdys: translate -l "es fr de" išvers į ispanų, prancūzų ir vokiečių kalbas. Naudokite translate -l "all", kad išverstų į visas palaikomas kalbas.
translate -l "language_codes" -u              | Atnaujina vertimus, ištrindama esamus ir juos sukurdama iš naujo. Įspėjimas: tai ištrins visus esamus vertimus nurodytoms kalboms.
translate -l "language_codes" -img            | Verčia tik paveikslėlių failus.
translate -l "language_codes" -md             | Verčia tik Markdown failus.
translate -l "language_codes" -nb             | Verčia tik Jupyter užrašų knygeles (.ipynb).
translate -l "language_codes" --fix           | Pakartoja vertimą failams, kurių vertimo kokybė buvo žema pagal ankstesnius vertinimo rezultatus.
translate -l "language_codes" -d              | Įjungia derinimo režimą detaliam žurnalo fiksavimui.
translate -l "language_codes" --save-logs, -s | Išsaugo DEBUG lygio žurnalus failuose <root_dir>/logs/ kataloge (konsolės išvestis valdoma per -d).
translate -l "language_codes" -r "root_dir"   | Nurodo projekto šaknies katalogą.
translate -l "language_codes" -f              | Naudoja greitą režimą paveikslėlių vertimui (iki 3 kartų greitesnis braižymas, šiek tiek prarandant kokybę ir išlyginimą).
translate -l "language_codes" -y              | Automatiškai patvirtina visus raginimus (naudinga CI/CD procesuose).
translate -l "language_codes" --add-disclaimer/--no-disclaimer | Įjungia arba išjungia mašininio vertimo atsakomybės atsisakymo skilties pridėjimą prie išverstų markdown ir užrašų knygelių (numatyta: įjungta).
translate -l "language_codes" --help          | Rodo pagalbos informaciją CLI su galimomis komandomis.
evaluate -l "language_code"                  | Įvertina vertimo kokybę konkrečioje kalboje ir pateikia pasitikėjimo balus.
evaluate -l "language_code" -c 0.8           | Įvertina vertimus su pasirinktu pasitikėjimo slenksčiu.
evaluate -l "language_code" -f               | Greitas vertinimo režimas (tik taisyklėmis pagrįstas, be LLM).
evaluate -l "language_code" -D               | Gilus vertinimo režimas (tik LLM pagrindu, išsamesnis, bet lėtesnis).
evaluate -l "language_code" --save-logs, -s  | Išsaugo DEBUG lygio žurnalus failuose <root_dir>/logs/ kataloge.
migrate-links -l "language_codes"             | Perdirba išverstus Markdown failus, atnaujindama nuorodas į užrašų knygeles (.ipynb). Pirmenybė teikiama išverstoms užrašų knygelėms, jei jų nėra – gali naudoti originalias.
migrate-links -l "language_codes" -r          | Nurodo projekto šaknies katalogą (numatyta: dabartinis katalogas).
migrate-links -l "language_codes" --dry-run   | Parodo, kurie failai būtų pakeisti, bet nekeičia failų.
migrate-links -l "language_codes" --no-fallback-to-original | Nekeičia nuorodų į originalias užrašų knygeles, jei nėra išverstų (atnaujina tik, kai yra išverstos).
migrate-links -l "language_codes" -d          | Įjungia derinimo režimą detaliam žurnalo fiksavimui.
migrate-links -l "language_codes" --save-logs, -s | Išsaugo DEBUG lygio žurnalus failuose <root_dir>/logs/ kataloge.
migrate-links -l "all" -y                      | Apdoroja visas kalbas ir automatiškai patvirtina įspėjimo raginimą.

## Naudojimo pavyzdžiai

  1. Numatytoji elgsena (prideda naujus vertimus, neištrindama esamų):   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. Prideda tik naujus korėjiečių paveikslėlių vertimus (esami vertimai neištrinami):    translate -l "ko" -img

  3. Atnaujina visus korėjiečių vertimus (Įspėjimas: tai ištrins visus esamus korėjiečių vertimus prieš pakartotinį vertimą):    translate -l "ko" -u

  4. Atnaujina tik korėjiečių paveikslėlius (Įspėjimas: tai ištrins visus esamus korėjiečių paveikslėlius prieš pakartotinį vertimą):    translate -l "ko" -img -u

  5. Prideda naujus korėjiečių markdown vertimus, nepaveikdama kitų vertimų:    translate -l "ko" -md

  6. Taiso žemos kokybės vertimus pagal ankstesnius vertinimo rezultatus: translate -l "ko" --fix

  7. Taiso žemos kokybės vertimus tik tam tikriems failams (markdown): translate -l "ko" --fix -md

  8. Taiso žemos kokybės vertimus tik tam tikriems failams (paveikslėliai): translate -l "ko" --fix -img

  9. Naudoja greitą režimą paveikslėlių vertimui:    translate -l "ko" -img -f

  10. Taiso žemos kokybės vertimus su pasirinktu slenksčiu: translate -l "ko" --fix -c 0.8

  11. Derinimo režimo pavyzdys: - translate -l "ko" -d: Įjungia derinimo žurnalų fiksavimą.
  12. Išsaugo žurnalus į failus: translate -l "ko" -s
  13. Konsolės DEBUG ir failų DEBUG: translate -l "ko" -d -s
  14. Verčia nenaudojant mašininio vertimo atsakomybės atsisakymo pranešimų: translate -l "ko" --no-disclaimer

  15. Migracija nuorodų į užrašų knygeles korėjiečių vertimams (atnaujina nuorodas į išverstus užrašų knygeles, jei yra):    migrate-links -l "ko"

  15. Migracija su sausuoju paleidimu (failai nekeičiasi):    migrate-links -l "ko" --dry-run

  16. Atnaujina nuorodas tik, kai yra išverstos užrašų knygelės (negrįžta prie originalių):    migrate-links -l "ko" --no-fallback-to-original

  17. Apdoroja visas kalbas su patvirtinimo raginimu:    migrate-links -l "all"

  18. Apdoroja visas kalbas ir automatiškai patvirtina:    migrate-links -l "all" -y
  19. Išsaugo žurnalus failuose migrate-links komandai:    migrate-links -l "ko ja" -s

### Vertinimo pavyzdžiai

> [!WARNING]  
> **Beta funkcija**: Vertinimo funkcionalumas šiuo metu yra beta stadijoje. Ši funkcija išleista vertinant išverstus dokumentus, o vertinimo metodai ir detalus įgyvendinimas dar yra kuriami ir gali keistis.

  1. Įvertina korėjiečių vertimus: evaluate -l "ko"

  2. Įvertina su pasirinktu pasitikėjimo slenksčiu: evaluate -l "ko" -c 0.8

  3. Greitas vertinimas (tik taisyklėmis pagrįstas): evaluate -l "ko" -f

  4. Gilus vertinimas (tik LLM pagrindu): evaluate -l "ko" -D

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors stengiamės užtikrinti tikslumą, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neatsakome už bet kokius nesusipratimus ar neteisingus aiškinimus, kylančius dėl šio vertimo naudojimo.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->