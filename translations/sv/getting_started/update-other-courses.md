<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "93a7150216aa3c2d191135358fa6dd21",
  "translation_date": "2025-11-30T13:44:56+00:00",
  "source_file": "getting_started/update-other-courses.md",
  "language_code": "sv"
}
-->
# Uppdatera avsnittet "Andra kurser" (Microsoft Beginners-repos)

Denna guide förklarar hur du gör så att avsnittet "Andra kurser" synkroniseras automatiskt med Co-op Translator, och hur du uppdaterar den globala mallen för alla repos.

- Gäller för: Endast Microsoft Beginners-repositorier
- Fungerar med: Co-op Translator CLI och GitHub Actions
- Mallkälla: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## Kom igång snabbt: Aktivera autosynk i ditt repo

Lägg till följande markörer runt avsnittet "Andra kurser" i din README. Co-op Translator kommer att ersätta allt mellan dessa markörer vid varje körning.

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

Varje gång Co-op Translator körs – via CLI (t.ex. `translate -l "<language codes>"`) eller GitHub Actions – uppdateras automatiskt avsnittet "Andra kurser" som är inneslutet av dessa markörer.

> [!NOTE]
> Om du redan har en lista, omslut den bara med samma markörer. Nästa körning ersätter den med det senaste standardiserade innehållet.

---

## Så här ändrar du det globala innehållet

Om du vill uppdatera det standardiserade innehållet som visas i alla Beginners-repos:

1. Redigera mallen: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)
2. Skapa en pull request till Co-op Translator-repot med dina ändringar
3. När PR:en har mergats uppdateras Co-op Translator-versionen
4. Nästa gång Co-op Translator körs (CLI eller GitHub Action) i ett målrepo, synkroniseras det uppdaterade avsnittet automatiskt

Detta säkerställer en enda sanningskälla för innehållet i "Andra kurser" över alla Beginners-repositorier.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, bör du vara medveten om att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål ska betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår vid användning av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->