# Microsoft Beginners Repositories

Diese Seite richtet sich an Maintainer von Microsoft "For Beginners" Repositorys, die den gemeinsamen README-Bereich "Other Courses" verwenden.

Die meisten Co-op Translator-Benutzer benötigen diese Seite nicht.

## Auto-Sync the Other Courses Section

Fügen Sie diese Marker um den "Other Courses"-Abschnitt in Ihrem README ein:

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

Jedes Mal, wenn Co-op Translator über die CLI oder GitHub Actions ausgeführt wird, ersetzt er den Inhalt zwischen den Markern durch die gepackte Vorlage.

## Update the Shared Template

Die Vorlage befindet sich unter:

```text
src/co_op_translator/templates/other_courses.md
```

Um den gemeinsamen Inhalt zu aktualisieren:

1. Bearbeiten Sie die Vorlage.
2. Öffnen Sie einen Pull Request bei Co-op Translator.
3. Nachdem die Änderung veröffentlicht wurde, führen Sie Co-op Translator im Ziel-Repository aus.

## Sparse Checkout Advisory

Große Kurs-Repositorys können beim Klonen kostspielig werden, wenn sie viele übersetzte Ausgaben enthalten. Sie können diesen Hinweis in generierten Sprachabschnitten aufnehmen:

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