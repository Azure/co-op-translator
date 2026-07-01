# Microsoft 초보자용 리포지토리

이 페이지는 공유되는 "Other Courses" README 섹션을 사용하는 Microsoft "For Beginners" 리포지토리의 유지관리자를 위한 것입니다.

대부분의 Co-op Translator 사용자는 이 페이지가 필요하지 않습니다.

## Other Courses 섹션 자동 동기화

README의 "Other Courses" 섹션 주위에 다음 마커를 추가하세요:

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

Co-op Translator가 CLI나 GitHub Actions를 통해 실행될 때마다, 마커 사이의 내용을 패키지된 템플릿으로 대체합니다.

## 공유 템플릿 업데이트

템플릿 소스는 다음 위치에 있습니다:

```text
src/co_op_translator/templates/other_courses.md
```

공유 콘텐츠를 업데이트하려면:

1. 템플릿을 편집하세요.
2. Co-op Translator에 풀 리퀘스트를 엽니다.
3. 변경 사항이 릴리스된 후 대상 리포지토리에서 Co-op Translator를 실행하세요.

## Sparse Checkout 권고

번역 결과물이 많은 대형 코스 리포지토리는 복제(clone) 비용이 많이 들 수 있습니다. 생성된 언어 섹션에 이 권고문을 포함할 수 있습니다:

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