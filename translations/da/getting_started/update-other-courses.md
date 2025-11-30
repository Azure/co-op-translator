<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "93a7150216aa3c2d191135358fa6dd21",
  "translation_date": "2025-11-30T13:45:17+00:00",
  "source_file": "getting_started/update-other-courses.md",
  "language_code": "da"
}
-->
# Opdater sektionen "Andre kurser" (Microsoft Beginners-repositorier)

Denne vejledning forklarer, hvordan du får sektionen "Andre kurser" til at synkronisere automatisk ved hjælp af Co-op Translator, og hvordan du opdaterer den globale skabelon for alle repositorier.

- Gælder for: Kun Microsoft Beginners-repositorier
- Fungerer med: Co-op Translator CLI og GitHub Actions
- Skabelonkilde: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## Hurtig start: Aktiver auto-synk i dit repo

Tilføj følgende markører omkring sektionen "Andre kurser" i din README. Co-op Translator vil erstatte alt mellem disse markører ved hver kørsel.

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

Hver gang Co-op Translator kører – via CLI (f.eks. `translate -l "<language codes>"`) eller GitHub Actions – opdateres sektionen "Andre kurser" automatisk inden for disse markører.

> [!NOTE]
> Hvis du allerede har en liste, skal du blot pakke den ind med de samme markører. Næste kørsel vil erstatte den med det nyeste standardiserede indhold.

---

## Sådan ændrer du det globale indhold

Hvis du vil opdatere det standardiserede indhold, der vises i alle Beginners-repositorier:

1. Rediger skabelonen: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)
2. Opret en pull request til Co-op Translator-repoet med dine ændringer
3. Når PR’en er flettet, opdateres Co-op Translator-versionen
4. Næste gang Co-op Translator kører (CLI eller GitHub Action) i et målrepo, synkroniseres den opdaterede sektion automatisk

Dette sikrer en enkelt sandhedskilde for indholdet i "Andre kurser" på tværs af alle Beginners-repositorier.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, bedes du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det oprindelige dokument på dets modersmål bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->