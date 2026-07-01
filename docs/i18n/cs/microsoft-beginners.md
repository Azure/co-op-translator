# Repozitáře Microsoftu pro začátečníky

Tato stránka je určena správcům repozitářů Microsoft "For Beginners", které používají sdílenou sekci README "Other Courses".

Většina uživatelů Co-op Translator tuto stránku nepotřebuje.

## Automatická synchronizace sekce "Other Courses"

Přidejte tyto značky kolem sekce "Other Courses" ve vašem README:

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

Pokaždé, když Co-op Translator spustíte přes CLI nebo GitHub Actions, nahradí obsah mezi značkami zabalenou šablonou.

## Aktualizujte sdílenou šablonu

Zdroj šablony se nachází na:

```text
src/co_op_translator/templates/other_courses.md
```

Chcete-li aktualizovat sdílený obsah:

1. Upravte šablonu.
2. Otevřete pull request do Co-op Translator.
3. Po vydání změny spusťte Co-op Translator v cílovém repozitáři.

## Upozornění k sparse checkoutu

Velké repozitáře kurzů mohou být náročné na klonování, pokud obsahují mnoho přeložených výstupů. Toto upozornění můžete zahrnout do generovaných jazykových sekcí:

```markdown
> **Prefer to Clone Locally?**
>
> This repository includes many language translations, which can significantly increase download size. To clone without translations, use sparse checkout:
>
> ```bash
> git clone --filter=blob:none --sparse https://github.com/org/repo.git
> cd repo
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
```