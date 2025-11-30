<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "93a7150216aa3c2d191135358fa6dd21",
  "translation_date": "2025-11-30T13:41:38+00:00",
  "source_file": "getting_started/update-other-courses.md",
  "language_code": "pa"
}
-->
# "ਹੋਰ ਕੋਰਸ" ਸੈਕਸ਼ਨ ਨੂੰ ਅੱਪਡੇਟ ਕਰੋ (Microsoft Beginners ਰਿਪੋਜ਼)

ਇਹ ਗਾਈਡ ਦੱਸਦੀ ਹੈ ਕਿ ਕਿਵੇਂ "ਹੋਰ ਕੋਰਸ" ਸੈਕਸ਼ਨ ਨੂੰ Co-op Translator ਦੀ ਵਰਤੋਂ ਨਾਲ ਆਟੋ-ਸਿੰਕ੍ਰੋਨਾਈਜ਼ ਕੀਤਾ ਜਾ ਸਕਦਾ ਹੈ, ਅਤੇ ਸਾਰੇ ਰਿਪੋਜ਼ ਲਈ ਗਲੋਬਲ ਟੈਮਪਲੇਟ ਨੂੰ ਕਿਵੇਂ ਅੱਪਡੇਟ ਕਰਨਾ ਹੈ।

- ਲਾਗੂ ਹੁੰਦਾ ਹੈ: ਸਿਰਫ Microsoft Beginners ਰਿਪੋਜ਼ ਲਈ
- ਕੰਮ ਕਰਦਾ ਹੈ: Co-op Translator CLI ਅਤੇ GitHub Actions ਨਾਲ
- ਟੈਮਪਲੇਟ ਸਰੋਤ: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## ਤੇਜ਼ ਸ਼ੁਰੂਆਤ: ਆਪਣੇ ਰਿਪੋ ਵਿੱਚ ਆਟੋ-ਸਿੰਕ ਚਾਲੂ ਕਰੋ

ਆਪਣੇ README ਵਿੱਚ "ਹੋਰ ਕੋਰਸ" ਸੈਕਸ਼ਨ ਦੇ ਆਲੇ-ਦੁਆਲੇ ਹੇਠਾਂ ਦਿੱਤੇ ਮਾਰਕਰ ਜੋੜੋ। Co-op Translator ਹਰ ਚਲਾਉਣ 'ਤੇ ਇਨ੍ਹਾਂ ਮਾਰਕਰਾਂ ਦੇ ਵਿਚਕਾਰ ਦੀ ਸਾਰੀ ਸਮੱਗਰੀ ਬਦਲ ਦੇਵੇਗਾ।

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

ਜਦੋਂ ਵੀ Co-op Translator ਚਲਾਇਆ ਜਾਂਦਾ ਹੈ—CLI ਰਾਹੀਂ (ਜਿਵੇਂ ਕਿ `translate -l "<language codes>"`) ਜਾਂ GitHub Actions ਰਾਹੀਂ—ਇਹ ਆਪਣੇ ਆਪ "ਹੋਰ ਕੋਰਸ" ਸੈਕਸ਼ਨ ਨੂੰ ਜੋ ਇਨ੍ਹਾਂ ਮਾਰਕਰਾਂ ਨਾਲ ਘਿਰਿਆ ਹੋਇਆ ਹੈ, ਅੱਪਡੇਟ ਕਰਦਾ ਹੈ।

> [!NOTE]
> ਜੇ ਤੁਹਾਡੇ ਕੋਲ ਪਹਿਲਾਂ ਹੀ ਕੋਈ ਸੂਚੀ ਹੈ, ਤਾਂ ਸਿਰਫ ਉਸਨੂੰ ਉਹੀ ਮਾਰਕਰਾਂ ਨਾਲ ਘੇਰ ਦਿਓ। ਅਗਲੀ ਵਾਰੀ ਚਲਾਉਣ 'ਤੇ ਇਹ ਉਸਨੂੰ ਨਵੀਂ ਮਿਆਰੀ ਸਮੱਗਰੀ ਨਾਲ ਬਦਲ ਦੇਵੇਗਾ।

---

## ਗਲੋਬਲ ਸਮੱਗਰੀ ਕਿਵੇਂ ਬਦਲਣੀ ਹੈ

ਜੇ ਤੁਸੀਂ ਉਹ ਮਿਆਰੀ ਸਮੱਗਰੀ ਅੱਪਡੇਟ ਕਰਨੀ ਚਾਹੁੰਦੇ ਹੋ ਜੋ ਸਾਰੇ Beginners ਰਿਪੋਜ਼ ਵਿੱਚ ਦਿਖਾਈ ਦਿੰਦੀ ਹੈ:

1. ਟੈਮਪਲੇਟ ਨੂੰ ਸੋਧੋ: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)
2. ਆਪਣੇ ਬਦਲਾਅ ਨਾਲ Co-op Translator ਰਿਪੋ ਵਿੱਚ ਇੱਕ ਪੁਲ ਰਿਕਵੇਸਟ ਖੋਲ੍ਹੋ
3. ਜਦੋਂ PR ਮਰਜ ਹੋ ਜਾਵੇ, Co-op Translator ਦਾ ਵਰਜਨ ਅੱਪਡੇਟ ਹੋ ਜਾਵੇਗਾ
4. ਅਗਲੀ ਵਾਰੀ ਜਦੋਂ Co-op Translator (CLI ਜਾਂ GitHub Action) ਕਿਸੇ ਟਾਰਗੇਟ ਰਿਪੋ ਵਿੱਚ ਚਲਾਇਆ ਜਾਵੇਗਾ, ਇਹ ਆਪਣੇ ਆਪ ਅੱਪਡੇਟ ਕੀਤਾ ਸੈਕਸ਼ਨ ਸਿੰਕ ਕਰ ਦੇਵੇਗਾ

ਇਸ ਨਾਲ ਸਾਰੇ Beginners ਰਿਪੋਜ਼ ਵਿੱਚ "ਹੋਰ ਕੋਰਸ" ਸਮੱਗਰੀ ਲਈ ਇੱਕ ਸਿੰਗਲ ਸੱਚਾਈ ਦਾ ਸਰੋਤ ਯਕੀਨੀ ਬਣਦਾ ਹੈ।

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ਅਸਵੀਕਾਰੋਪੱਤਰ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਤਾ ਲਈ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਵਿੱਚ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਮਰਥਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਪ੍ਰਮਾਣਿਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਉਤਪੰਨ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆ ਲਈ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->