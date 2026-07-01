# Microsoft ਸ਼ੁਰੂਆਤੀ ਰਿਪੋਜ਼ਿਟਰੀਜ਼

ਇਹ ਪੰਨਾ Microsoft ਦੇ 'ਸ਼ੁਰੂਆਤ ਕਰਨ ਵਾਲਿਆਂ ਲਈ' ਰਿਪੋਜ਼ਿਟਰੀਜ਼ ਦੇ ਰਖ-ਰਖਾਅ ਕਰਨ ਵਾਲਿਆਂ ਲਈ ਹੈ ਜੋ ਸਾਂਝੇ 'ਹੋਰ ਕੋਰਸ' README ਸੈਕਸ਼ਨ ਨੂੰ ਵਰਤਦੇ ਹਨ।

ਜ਼ਿਆਦਾਤਰ Co-op Translator ਉਪਭੋਗਤਾਵਾਂ ਨੂੰ ਇਸ ਪੰਨੇ ਦੀ ਲੋੜ ਨਹੀਂ ਹੁੰਦੀ।

## 'ਹੋਰ ਕੋਰਸ' ਸੈਕਸ਼ਨ ਦੀ ਆਟੋ-ਸਿੰਕ

ਆਪਣੇ README ਵਿੱਚ 'ਹੋਰ ਕੋਰਸ' ਸੈਕਸ਼ਨ ਦੇ ਆਲੇ-ਦੁਆਲੇ ਇਹ ਨਿਸ਼ਾਨ ਲਗਾਓ:

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

ਜਦੋਂ ਵੀ Co-op Translator CLI ਜਾਂ GitHub Actions ਰਾਹੀਂ ਚਲਾਇਆ ਜਾਂਦਾ ਹੈ, ਇਹ ਨਿਸ਼ਾਨਾਂ ਦੇ ਦਰਮਿਆਨ ਦੀ ਸਮੱਗਰੀ ਨੂੰ ਪੈਕੇਜ ਕੀਤੇ ਗਏ ਟੈਂਪਲੇਟ ਨਾਲ ਬਦਲ ਦਿੰਦਾ ਹੈ।

## ਸਾਂਝੇ ਟੈਂਪਲੇਟ ਨੂੰ ਅਪਡੇਟ ਕਰੋ

ਟੈਂਪਲੇਟ ਸੋਰਸ ਇੱਥੇ ਹੈ:

```text
src/co_op_translator/templates/other_courses.md
```

ਸਾਂਝੀ ਸਮੱਗਰੀ ਨੂੰ ਅਪਡੇਟ ਕਰਨ ਲਈ:

1. ਟੈਂਪਲੇਟ ਨੂੰ ਸੰਪਾਦਿਤ ਕਰੋ।
2. Co-op Translator ਲਈ ਇੱਕ pull request ਖੋਲ੍ਹੋ।
3. ਬਦਲਾਅ ਜਾਰੀ ਹੋਣ ਤੋਂ ਬਾਅਦ, ਟਾਰਗਿਟ ਰਿਪੋਜ਼ਿਟਰੀ ਵਿੱਚ Co-op Translator ਚਲਾਓ।

## Sparse Checkout ਸਲਾਹ

ਜਦੋਂ ਵੱਡੇ ਕੋਰਸ ਰਿਪੋਜ਼ਿਟਰੀਜ਼ ਵਿੱਚ ਬਹੁਤ ਸਾਰੇ ਅਨੁਵਾਦਿਤ ਨਤੀਜੇ ਸ਼ਾਮਲ ਹੁੰਦੇ ਹਨ, ਤਾਂ ਉਹਨਾਂ ਨੂੰ clone ਕਰਨਾ ਮਹਿੰਗਾ ਹੋ ਸਕਦਾ ਹੈ। ਤੁਸੀਂ ਇਹ ਸਲਾਹ ਜਨਰੇਟ ਕੀਤੇ ਭਾਸ਼ਾ ਸੈਕਸ਼ਨਾਂ ਵਿੱਚ ਸ਼ਾਮਲ ਕਰ ਸਕਦੇ ਹੋ:

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