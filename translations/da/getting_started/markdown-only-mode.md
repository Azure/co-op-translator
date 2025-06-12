<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9b1b247a8d0f1736459e0e9ede0d9c92",
  "translation_date": "2025-06-12T11:40:56+00:00",
  "source_file": "getting_started/markdown-only-mode.md",
  "language_code": "da"
}
-->
# Brug af Markdown-Only Mode

## Introduktion
Markdown-only mode er designet til kun at oversætte Markdown-indholdet i dit projekt. Denne tilstand springer billedoversættelsesprocessen over og fokuserer udelukkende på tekstindholdet, hvilket gør den ideel i situationer, hvor billedoversættelse ikke er nødvendig, eller hvor de nødvendige miljøvariabler til Computer Vision ikke er sat.

## Hvornår skal det bruges
- Når Computer Vision-relaterede miljøvariabler ikke er konfigureret.
- Når du kun ønsker at oversætte tekstindholdet uden at opdatere billedlinks.
- Når det eksplicit er angivet af brugeren via `-md` kommandolinjeoptionen.

## Sådan aktiveres det
For at aktivere Markdown-only mode, brug `-md` optionen i din kommando. For eksempel:
```
translate -l "ko" -md
```

Eller hvis de Computer Vision-relaterede miljøvariabler ikke er konfigureret. At køre `translate -l "ko"` vil automatisk skifte til Markdown-only mode.

```
translate -l "ko"
```

Denne kommando oversætter Markdown-indholdet til koreansk og opdaterer billedlinks til deres originale stier i stedet for at ændre dem til oversatte billedstier.

## Adfærd
I Markdown-only mode:
- Oversættelsesprocessen springer billedoversættelsestrinnet over.
- Billedlinks i Markdown forbliver uændrede og peger på deres oprindelige stier.

## Eksempler
### Før
```markdown
![Image](../../../translated_images/image.aa98bae4d78871bb3b23ac9f938ff86539da4cd6fb4c52dafedc4665135c3d61.da.png)
```
### Efter brug af Markdown-only mode
```markdown
![Image](../../../translated_images/image.fc8708ffe1e1ca12c38822b1a382726da4b232025d1daa8a50ab75c8635d0c4a.da.png)
```

## Fejlfinding
- Sørg for, at `-md` optionen er korrekt angivet i kommandoen.
- Bekræft, at ingen Computer Vision miljøvariabler forstyrrer processen.

## Konklusion
Markdown-only mode giver en strømlinet måde at oversætte tekstindhold uden at ændre billedlinks. Det er især nyttigt, når billedoversættelse ikke er nødvendig, eller når man arbejder i miljøer uden opsætning til Computer Vision.

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det oprindelige dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.