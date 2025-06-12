<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c64ba65e091e5d87385490fa63a8f574",
  "translation_date": "2025-06-12T12:34:31+00:00",
  "source_file": "getting_started/command-line-guide/command-line-guide.md",
  "language_code": "pa"
}
-->
# Co-op Translator ਕਮਾਂਡ ਲਾਈਨ ਇੰਟਰਫੇਸ (CLI) ਨੂੰ ਕਿਵੇਂ ਵਰਤਣਾ ਹੈ

## ਲੋੜੀਂਦੇ ਸਾਧਨ

- **Python 3.10 ਜਾਂ ਉਸ ਤੋਂ ਉੱਚਾ**: Co-op Translator ਚਲਾਉਣ ਲਈ ਜਰੂਰੀ।

## ਸਮੱਗਰੀ ਸੂਚੀ

1. [ਰੂਟ ਡਾਇਰੈਕਟਰੀ ਵਿੱਚ '.env' ਫਾਇਲ ਬਣਾਓ](./create-env-file.md)
   - ਚੁਣੇ ਹੋਏ ਭਾਸ਼ਾ ਮਾਡਲ ਸੇਵਾ ਲਈ ਲੋੜੀਂਦੇ ਕੁੰਜੀਆਂ ਸ਼ਾਮਲ ਕਰੋ।
   - ਜੇ Azure Computer Vision ਕੁੰਜੀਆਂ ਛੱਡ ਦਿੱਤੀਆਂ ਜਾਂ `-md` ਦਿੱਤਾ ਗਿਆ ਹੈ, ਤਾਂ translator ਸਿਰਫ Markdown ਮੋਡ ਵਿੱਚ ਕੰਮ ਕਰੇਗਾ।
1. [Co-op translator ਪੈਕੇਜ ਇੰਸਟਾਲ ਕਰੋ](./install-package.md)
1. [Co-op Translator ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਆਪਣਾ ਪ੍ਰੋਜੈਕਟ ਅਨੁਵਾਦ ਕਰੋ](./translator-your-project.md)

**ਅਸਵੀਕਾਰੋक्ति**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦਿਤ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਅਤ ਲਈ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਮਰੱਥਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਹੀ ਪ੍ਰਮਾਣਿਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਜ਼ਰੂਰੀ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫ਼ਾਰਿਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਨਾਲ ਪੈਦਾ ਹੋਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤਫਹਮੀਆਂ ਜਾਂ ਭ੍ਰਮਾਂ ਲਈ ਅਸੀਂ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।