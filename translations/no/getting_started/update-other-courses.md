<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "93a7150216aa3c2d191135358fa6dd21",
  "translation_date": "2025-11-30T13:45:38+00:00",
  "source_file": "getting_started/update-other-courses.md",
  "language_code": "no"
}
-->
# Oppdater seksjonen "Andre kurs" (Microsoft Beginners-repositorier)

Denne veiledningen forklarer hvordan du kan få seksjonen "Andre kurs" til å synkronisere automatisk ved hjelp av Co-op Translator, og hvordan du oppdaterer den globale malen for alle repositorier.

- Gjelder for: Kun Microsoft Beginners-repositorier
- Fungerer med: Co-op Translator CLI og GitHub Actions
- Mal-kilde: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## Kom i gang raskt: Aktiver automatisk synkronisering i ditt repo

Legg til følgende markører rundt seksjonen "Andre kurs" i README-filen din. Co-op Translator vil erstatte alt mellom disse markørene ved hver kjøring.

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

Hver gang Co-op Translator kjører—via CLI (f.eks. `translate -l "<language codes>"`) eller GitHub Actions—oppdateres automatisk seksjonen "Andre kurs" som er omsluttet av disse markørene.

> [!NOTE]
> Hvis du allerede har en liste, pakk den bare inn med de samme markørene. Neste kjøring vil erstatte den med det nyeste standardiserte innholdet.

---

## Hvordan endre det globale innholdet

Hvis du ønsker å oppdatere det standardiserte innholdet som vises i alle Beginners-repositorier:

1. Rediger malen: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)
2. Åpne en pull request til Co-op Translator-repoet med endringene dine
3. Når PR-en er slått sammen, vil versjonen av Co-op Translator bli oppdatert
4. Neste gang Co-op Translator kjører (CLI eller GitHub Action) i et målrepo, vil den automatisk synkronisere den oppdaterte seksjonen

Dette sikrer en enkelt sannhetskilde for innholdet i "Andre kurs" på tvers av alle Beginners-repositorier.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vennligst vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->