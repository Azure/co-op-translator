<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "93a7150216aa3c2d191135358fa6dd21",
  "translation_date": "2025-11-30T13:46:25+00:00",
  "source_file": "getting_started/update-other-courses.md",
  "language_code": "nl"
}
-->
# Update de sectie "Andere Cursussen" (Microsoft Beginners repositories)

Deze gids legt uit hoe je de sectie "Andere Cursussen" automatisch laat synchroniseren met Co-op Translator, en hoe je de globale template voor alle repositories bijwerkt.

- Van toepassing op: alleen Microsoft Beginners repositories
- Werkt met: Co-op Translator CLI en GitHub Actions
- Template bron: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## Snelstart: Schakel auto-sync in je repository in

Voeg de volgende markers toe rond de sectie "Andere Cursussen" in je README. Co-op Translator vervangt alles tussen deze markers bij elke uitvoering.

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

Elke keer dat Co-op Translator draait—via CLI (bijv. `translate -l "<language codes>"`) of GitHub Actions—wordt de sectie "Andere Cursussen" die tussen deze markers staat automatisch bijgewerkt.

> [!NOTE]
> Als je al een bestaande lijst hebt, wikkel die dan gewoon in met dezelfde markers. De volgende run vervangt deze dan door de nieuwste gestandaardiseerde inhoud.

---

## Hoe je de globale inhoud aanpast

Als je de gestandaardiseerde inhoud wilt bijwerken die in alle Beginners repositories verschijnt:

1. Bewerk de template: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)
2. Open een pull request naar de Co-op Translator repository met je wijzigingen
3. Nadat de PR is gemerged, wordt de Co-op Translator versie bijgewerkt
4. De volgende keer dat Co-op Translator draait (CLI of GitHub Action) in een doelrepository, wordt de bijgewerkte sectie automatisch gesynchroniseerd

Dit zorgt voor één enkele bron van waarheid voor de inhoud van "Andere Cursussen" in alle Beginners repositories.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet als de gezaghebbende bron worden beschouwd. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->