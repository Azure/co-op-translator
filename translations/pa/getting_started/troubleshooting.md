<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6e626bef5ed78a1cc55b0dbf44f01d47",
  "translation_date": "2025-10-15T02:56:53+00:00",
  "source_file": "getting_started/troubleshooting.md",
  "language_code": "pa"
}
-->
# ਮਾਈਕਰੋਸਾਫਟ ਕੋ-ਓਪ ਟ੍ਰਾਂਸਲੇਟਰ ਟਰਬਲਸ਼ੂਟਿੰਗ ਗਾਈਡ

## ਝਲਕ
ਮਾਈਕਰੋਸਾਫਟ ਕੋ-ਓਪ ਟ੍ਰਾਂਸਲੇਟਰ ਇੱਕ ਸ਼ਕਤੀਸ਼ਾਲੀ ਟੂਲ ਹੈ ਜੋ ਮਾਰਕਡਾਊਨ ਡੌਕੂਮੈਂਟਾਂ ਨੂੰ ਆਸਾਨੀ ਨਾਲ ਅਨੁਵਾਦ ਕਰਨ ਲਈ ਵਰਤਿਆ ਜਾਂਦਾ ਹੈ। ਇਹ ਗਾਈਡ ਤੁਹਾਨੂੰ ਟੂਲ ਵਰਤਣ ਦੌਰਾਨ ਆਉਣ ਵਾਲੀਆਂ ਆਮ ਸਮੱਸਿਆਵਾਂ ਨੂੰ ਹੱਲ ਕਰਨ ਵਿੱਚ ਮਦਦ ਕਰੇਗੀ।

## ਆਮ ਸਮੱਸਿਆਵਾਂ ਅਤੇ ਹੱਲ

### 1. ਮਾਰਕਡਾਊਨ ਟੈਗ ਸਮੱਸਿਆ
**ਸਮੱਸਿਆ:** ਅਨੁਵਾਦ ਕੀਤੇ ਮਾਰਕਡਾਊਨ ਡੌਕੂਮੈਂਟ ਦੇ ਸ਼ੁਰੂ 'ਤੇ `markdown` ਟੈਗ ਆ ਜਾਂਦੀ ਹੈ, ਜਿਸ ਨਾਲ ਰੈਂਡਰਿੰਗ ਸਮੱਸਿਆ ਆਉਂਦੀ ਹੈ।

**ਹੱਲ:** ਇਸਨੂੰ ਹੱਲ ਕਰਨ ਲਈ, ਫਾਇਲ ਦੇ ਸ਼ੁਰੂ 'ਤੇ ਆਈ `markdown` ਟੈਗ ਨੂੰ ਹਟਾ ਦਿਓ। ਇਸ ਨਾਲ ਮਾਰਕਡਾਊਨ ਫਾਇਲ ਠੀਕ ਤਰੀਕੇ ਨਾਲ ਰੈਂਡਰ ਹੋਵੇਗੀ।

**ਕਦਮ:**
1. ਅਨੁਵਾਦ ਕੀਤੀ ਮਾਰਕਡਾਊਨ (`.md`) ਫਾਇਲ ਖੋਲ੍ਹੋ।
2. ਡੌਕੂਮੈਂਟ ਦੇ ਸ਼ੁਰੂ 'ਤੇ `markdown` ਟੈਗ ਲੱਭੋ।
3. `markdown` ਟੈਗ ਨੂੰ ਹਟਾ ਦਿਓ।
4. ਫਾਇਲ ਨੂੰ ਸੇਵ ਕਰੋ।
5. ਫਾਇਲ ਮੁੜ ਖੋਲ੍ਹੋ ਅਤੇ ਵੇਖੋ ਕਿ ਠੀਕ ਰੈਂਡਰ ਹੋ ਰਹੀ ਹੈ ਜਾਂ ਨਹੀਂ।

### 2. ਇੰਬੈੱਡ ਕੀਤੀਆਂ ਇਮੇਜਾਂ ਦੀ URL ਸਮੱਸਿਆ
**ਸਮੱਸਿਆ:** ਇੰਬੈੱਡ ਕੀਤੀਆਂ ਇਮੇਜਾਂ ਦੀਆਂ URL ਭਾਸ਼ਾ ਲੋਕੇਲ ਨਾਲ ਮੇਲ ਨਹੀਂ ਖਾਂਦੀਆਂ, ਜਿਸ ਕਰਕੇ ਗਲਤ ਜਾਂ ਗੁੰਮ ਹੋਈਆਂ ਇਮੇਜਾਂ ਆਉਂਦੀਆਂ ਹਨ।

**ਹੱਲ:** ਇੰਬੈੱਡ ਕੀਤੀਆਂ ਇਮੇਜਾਂ ਦੀ URL ਚੈੱਕ ਕਰੋ ਅਤੇ ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਉਹ ਭਾਸ਼ਾ ਲੋਕੇਲ ਨਾਲ ਮੇਲ ਖਾਂਦੀਆਂ ਹਨ। ਸਾਰੀਆਂ ਇਮੇਜਾਂ `translated_images` ਫੋਲਡਰ ਵਿੱਚ ਹਨ ਅਤੇ ਹਰ ਇਮੇਜ ਦੇ ਫਾਇਲ ਨਾਂ ਵਿੱਚ ਭਾਸ਼ਾ ਲੋਕੇਲ ਟੈਗ ਹੁੰਦਾ ਹੈ।

**ਕਦਮ:**
1. ਅਨੁਵਾਦ ਕੀਤੀ ਮਾਰਕਡਾਊਨ ਡੌਕੂਮੈਂਟ ਖੋਲ੍ਹੋ।
2. ਇੰਬੈੱਡ ਕੀਤੀਆਂ ਇਮੇਜਾਂ ਅਤੇ ਉਨ੍ਹਾਂ ਦੀਆਂ URL ਪਛਾਣੋ।
3. ਵੇਖੋ ਕਿ ਇਮੇਜ ਫਾਇਲ ਨਾਂ ਵਿੱਚ ਲੋਕੇਲ ਡੌਕੂਮੈਂਟ ਦੀ ਭਾਸ਼ਾ ਨਾਲ ਮੇਲ ਖਾਂਦੀ ਹੈ।
4. ਜੇ ਲੋੜ ਹੋਵੇ ਤਾਂ URL ਅੱਪਡੇਟ ਕਰੋ।
5. ਫਾਇਲ ਸੇਵ ਕਰੋ ਅਤੇ ਮੁੜ ਖੋਲ੍ਹੋ ਕਿ ਇਮੇਜਾਂ ਠੀਕ ਆ ਰਹੀਆਂ ਹਨ ਜਾਂ ਨਹੀਂ।

### 3. ਅਨੁਵਾਦ ਦੀ ਸਹੀਤਾ
**ਸਮੱਸਿਆ:** ਅਨੁਵਾਦ ਕੀਤਾ ਸਮੱਗਰੀ ਠੀਕ ਨਹੀਂ ਜਾਂ ਹੋਰ ਸੋਧ ਦੀ ਲੋੜ ਹੈ।

**ਹੱਲ:** ਅਨੁਵਾਦ ਕੀਤੇ ਡੌਕੂਮੈਂਟ ਨੂੰ ਧਿਆਨ ਨਾਲ ਵੇਖੋ ਅਤੇ ਜਿੱਥੇ ਲੋੜ ਹੋਵੇ ਸੋਧ ਕਰੋ ਤਾਂ ਜੋ ਸਹੀਤਾ ਅਤੇ ਪੜ੍ਹਨਯੋਗਤਾ ਵਧੇ।

**ਕਦਮ:**
1. ਅਨੁਵਾਦ ਕੀਤਾ ਡੌਕੂਮੈਂਟ ਖੋਲ੍ਹੋ।
2. ਸਮੱਗਰੀ ਧਿਆਨ ਨਾਲ ਵੇਖੋ।
3. ਜਿੱਥੇ ਲੋੜ ਹੋਵੇ ਸੋਧ ਕਰੋ।
4. ਫਾਇਲ ਸੇਵ ਕਰੋ।

## 4. ਪਰਮਿਸ਼ਨ ਐਰਰ ਰੀਡੈਕਟ ਜਾਂ 404

ਜੇ ਇਮੇਜ ਜਾਂ ਟੈਕਸਟ ਠੀਕ ਭਾਸ਼ਾ ਵਿੱਚ ਅਨੁਵਾਦ ਨਹੀਂ ਹੋ ਰਹੇ ਅਤੇ -d ਡੀਬੱਗ ਮੋਡ ਦੌਰਾਨ 401 ਐਰਰ ਆਉਂਦੀ ਹੈ। ਇਹ ਆਮ ਤੌਰ 'ਤੇ ਆਥੈਂਟੀਕੇਸ਼ਨ ਫੇਲ ਹੈ—ਕੁੰਜੀ ਗਲਤ, ਮਿਆਦ ਪੁੱਗੀ ਜਾਂ ਐਂਡਪੌਇੰਟ ਦੇ ਰੀਜਨ ਨਾਲ ਨਹੀਂ ਮਿਲਦੀ।

ਹੋਰ ਜਾਣਕਾਰੀ ਲਈ co-op translator ਨੂੰ [-d debug switch](https://github.com/Azure/co-op-translator/blob/main/getting_started/command-reference.md) ਨਾਲ ਚਲਾਓ।

- **ਐਰਰ ਮੈਸੇਜ**: `Access denied due to invalid subscription key or wrong API endpoint.`
- **ਸੰਭਾਵਤ ਕਾਰਨ:**
  - ਸਬਸਕ੍ਰਿਪਸ਼ਨ ਕੁੰਜੀ ਰੀਡੈਕਟ ਜਾਂ ਗਲਤ ਸੀ।
  - AI Services Key ਜਾਂ Subscription Key ਕਿਸੇ ਹੋਰ Azure resource (ਜਿਵੇਂ Translator ਜਾਂ OpenAI) ਦੀ ਹੈ, ਨਾ ਕਿ **Azure AI Vision** ਦੀ।

 **Resource Type**
  - [Azure Portal](https://portal.azure.com) ਜਾਂ [Azure AI Foundry](https://ai.azure.com) 'ਤੇ ਜਾਓ ਅਤੇ ਯਕੀਨੀ ਬਣਾਓ ਕਿ resource ਦੀ ਕਿਸਮ `Azure AI services` → `Vision` ਹੈ।
  - ਕੁੰਜੀਆਂ ਦੀ ਜਾਂਚ ਕਰੋ ਅਤੇ ਠੀਕ ਕੁੰਜੀ ਵਰਤੋ।

## 5. ਕੰਫਿਗਰੇਸ਼ਨ ਐਰਰ (ਨਵਾਂ ਐਰਰ ਹੈਂਡਲਿੰਗ)

ਨਵੇਂ selective translation system ਨਾਲ, Co-op Translator ਹੁਣ explicit ਐਰਰ ਮੈਸੇਜ ਦਿੰਦਾ ਹੈ ਜਦੋਂ ਲੋੜੀਂਦੇ ਸਰਵਿਸ ਕੰਫਿਗਰ ਨਹੀਂ ਹੁੰਦੇ।

### 5.1. ਇਮੇਜ ਅਨੁਵਾਦ ਲਈ Azure AI Service ਕੰਫਿਗਰ ਨਹੀਂ

**ਸਮੱਸਿਆ:** ਤੁਸੀਂ ਇਮੇਜ ਅਨੁਵਾਦ (`-img` flag) ਮੰਗਿਆ ਪਰ Azure AI Service ਠੀਕ ਤਰੀਕੇ ਨਾਲ ਕੰਫਿਗਰ ਨਹੀਂ।

**ਐਰਰ ਮੈਸੇਜ:**
```
Error: Image translation requested but Azure AI Service is not configured.
Please add AZURE_AI_SERVICE_API_KEY and AZURE_AI_SERVICE_ENDPOINT to your .env file.
Check Azure AI Service availability and configuration.
```

**ਹੱਲ:**
1. **ਵਿਕਲਪ 1**: Azure AI Service ਕੰਫਿਗਰ ਕਰੋ
   - ਆਪਣੇ `.env` ਫਾਇਲ ਵਿੱਚ `AZURE_AI_SERVICE_API_KEY` ਜੋੜੋ
   - ਆਪਣੇ `.env` ਫਾਇਲ ਵਿੱਚ `AZURE_AI_SERVICE_ENDPOINT` ਜੋੜੋ
   - ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਸਰਵਿਸ ਐਕਸੈਸ ਹੋ ਸਕਦੀ ਹੈ

2. **ਵਿਕਲਪ 2**: ਇਮੇਜ ਅਨੁਵਾਦ ਦੀ ਮੰਗ ਹਟਾਓ
   ```bash
   # Instead of: translate -l "ko" -img
   # Use: translate -l "ko" -md
   ```

### 5.2. ਲੋੜੀਂਦੀ ਕੰਫਿਗਰੇਸ਼ਨ ਗੁੰਮ

**ਸਮੱਸਿਆ:** ਜਰੂਰੀ LLM ਕੰਫਿਗਰੇਸ਼ਨ ਨਹੀਂ ਮਿਲੀ।

**ਐਰਰ ਮੈਸੇਜ:**
```
Error: No language model configuration found.
Please configure either Azure OpenAI or OpenAI in your .env file.
```

**ਹੱਲ:**
1. ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਤੁਹਾਡੇ `.env` ਫਾਇਲ ਵਿੱਚ ਘੱਟੋ-ਘੱਟ ਹੇਠਾਂ ਦਿੱਤੀਆਂ LLM ਕੰਫਿਗਰੇਸ਼ਨਾਂ ਵਿੱਚੋਂ ਇੱਕ ਹੈ:
   - **Azure OpenAI**: `AZURE_OPENAI_API_KEY` ਅਤੇ `AZURE_OPENAI_ENDPOINT`
   - **OpenAI**: `OPENAI_API_KEY`
   
   ਤੁਹਾਨੂੰ Azure OpenAI ਜਾਂ OpenAI ਵਿੱਚੋਂ ਇੱਕ ਦੀ ਲੋੜ ਹੈ, ਦੋਵੇਂ ਦੀ ਨਹੀਂ।

### 5.3. ਚੋਣਵੀਂ ਅਨੁਵਾਦ ਗੜਬੜ

**ਸਮੱਸਿਆ:** ਕੋਈ ਵੀ ਫਾਇਲ ਅਨੁਵਾਦ ਨਹੀਂ ਹੋਈ, ਹਾਲਾਂਕਿ ਕਮਾਂਡ ਸਫਲ ਹੋਈ।

**ਸੰਭਾਵਤ ਕਾਰਨ:**
- ਗਲਤ ਫਾਇਲ ਟਾਈਪ ਫਲੈਗ (`-md`, `-img`, `-nb`)
- ਪ੍ਰੋਜੈਕਟ ਵਿੱਚ ਕੋਈ ਮੇਲ ਖਾਂਦੀਆਂ ਫਾਇਲਾਂ ਨਹੀਂ
- ਗਲਤ ਡਾਇਰੈਕਟਰੀ ਬਣਤਰ

**ਹੱਲ:**
1. **ਡਿਬੱਗ ਮੋਡ ਵਰਤੋ** ਤਾਂ ਜੋ ਪਤਾ ਲੱਗੇ ਕੀ ਹੋ ਰਿਹਾ:
   ```bash
   translate -l "ko" -md -d
   ```

2. **ਫਾਇਲ ਟਾਈਪ ਚੈੱਕ ਕਰੋ** ਆਪਣੇ ਪ੍ਰੋਜੈਕਟ ਵਿੱਚ:
   ```bash
   # For markdown files
   find . -name "*.md" -not -path "./translations/*"
   
   # For notebooks
   find . -name "*.ipynb" -not -path "./translations/*"
   
   # For images
   find . -name "*.png" -o -name "*.jpg" -o -name "*.jpeg" -not -path "./translations/*"
   ```

3. **ਫਲੈਗ ਕੰਬੀਨੇਸ਼ਨ ਜਾਂਚੋ**:
   ```bash
   # Translate everything (default)
   translate -l "ko"
   
   # Translate specific types
   translate -l "ko" -md -img
   ```

## 6. ਪੁਰਾਣੇ ਸਿਸਟਮ ਤੋਂ ਮਾਈਗ੍ਰੇਸ਼ਨ

### 6.1. ਸਿਰਫ ਮਾਰਕਡਾਊਨ ਮੋਡ ਹਟਾਇਆ ਗਿਆ

**ਸਮੱਸਿਆ:** ਉਹ ਕਮਾਂਡਾਂ ਜੋ ਆਟੋਮੈਟਿਕ ਮਾਰਕਡਾਊਨ-ਕੇਵਲ fallback 'ਤੇ ਨਿਰਭਰ ਸੀ, ਹੁਣ ਉਮੀਦ ਮੁਤਾਬਕ ਨਹੀਂ ਚੱਲਦੀਆਂ।

**ਪੁਰਾਣਾ ਵਿਹਾਰ:**
```bash
# This used to automatically switch to markdown-only mode
translate -l "ko"  # (when Azure AI Vision was not configured)
```

**ਨਵਾਂ ਵਿਹਾਰ:**
```bash
# This now produces an error if image translation is requested but not configured
translate -l "ko" -img
```

**ਹੱਲ:**
- **ਸਪੱਸ਼ਟ ਹੋਵੋ** ਕਿ ਤੁਸੀਂ ਕੀ ਅਨੁਵਾਦ ਕਰਨਾ ਚਾਹੁੰਦੇ ਹੋ:
  ```bash
  translate -l "ko" -md        # Only markdown
  translate -l "ko" -md -img   # Markdown and images
  translate -l "ko"            # Everything (if all services configured)
  ```

### 6.2. ਅਣਉਮੀਦ ਲਿੰਕ ਵਿਹਾਰ

**ਸਮੱਸਿਆ:** ਅਨੁਵਾਦ ਕੀਤੀਆਂ ਫਾਇਲਾਂ ਵਿੱਚ ਲਿੰਕ ਅਣਉਮੀਦ ਥਾਵਾਂ 'ਤੇ ਜਾਂਦੇ ਹਨ।

**ਕਾਰਨ:** ਚੁਣੇ ਹੋਏ ਫਾਇਲ ਟਾਈਪਾਂ ਦੇ ਆਧਾਰ 'ਤੇ ਲਿੰਕ ਪ੍ਰੋਸੈਸਿੰਗ ਵਿਹਾਰ ਬਦਲ ਜਾਂਦਾ ਹੈ।

**ਹੱਲ:**
1. **ਨਵੇਂ ਲਿੰਕ ਵਿਹਾਰ ਨੂੰ ਸਮਝੋ**:
   - `-nb` ਸ਼ਾਮਲ: ਨੋਟਬੁੱਕ ਲਿੰਕ ਅਨੁਵਾਦ ਕੀਤੀਆਂ ਵਰਜਨਾਂ ਵੱਲ ਜਾਂਦੇ ਹਨ
   - `-nb` ਨਾ ਹੋਣ 'ਤੇ: ਨੋਟਬੁੱਕ ਲਿੰਕ ਮੂਲ ਫਾਇਲਾਂ ਵੱਲ ਜਾਂਦੇ ਹਨ
   - `-img` ਸ਼ਾਮਲ: ਇਮੇਜ ਲਿੰਕ ਅਨੁਵਾਦ ਕੀਤੀਆਂ ਵਰਜਨਾਂ ਵੱਲ ਜਾਂਦੇ ਹਨ
   - `-img` ਨਾ ਹੋਣ 'ਤੇ: ਇਮੇਜ ਲਿੰਕ ਮੂਲ ਫਾਇਲਾਂ ਵੱਲ ਜਾਂਦੇ ਹਨ

2. **ਆਪਣੀ ਲੋੜ ਮੁਤਾਬਕ ਠੀਕ ਕੰਬੀਨੇਸ਼ਨ ਚੁਣੋ**:
   ```bash
   # All internal links point to translated versions
   translate -l "ko" -md -img -nb
   
   # Only markdown translated, other links point to originals
   translate -l "ko" -md
   ```

## 7. GitHub Action ਚੱਲੀ ਪਰ Pull Request (PR) ਨਹੀਂ ਬਣੀ

**ਲੱਛਣ:** `peter-evans/create-pull-request` ਲਈ workflow ਲੌਗ ਵਿੱਚ ਆਉਂਦਾ ਹੈ:

> Branch 'update-translations' is not ahead of base 'main' and will not be created

**ਸੰਭਾਵਤ ਕਾਰਨ:**
- **ਕੋਈ ਤਬਦੀਲੀ ਨਹੀਂ ਮਿਲੀ:** ਅਨੁਵਾਦ ਕਦਮ ਨੇ ਕੋਈ ਫਰਕ ਨਹੀਂ ਕੀਤਾ (repo ਪਹਿਲਾਂ ਹੀ ਅੱਪ-ਟੂ-ਡੇਟ ਹੈ)।
- **ਆਉਟਪੁੱਟ ਇਗਨੋਰ ਹੋ ਗਈ:** `.gitignore` ਉਹ ਫਾਇਲਾਂ ਇਗਨੋਰ ਕਰ ਰਿਹਾ ਹੈ ਜੋ ਤੁਸੀਂ commit ਕਰਨਾ ਚਾਹੁੰਦੇ ਹੋ (ਜਿਵੇਂ `*.ipynb`, `translations/`, `translated_images/`)।
- **add-paths ਗਲਤ:** ਐਕਸ਼ਨ ਨੂੰ ਦਿੱਤੇ ਪਾਥ ਅਸਲ ਆਉਟਪੁੱਟ ਥਾਵਾਂ ਨਾਲ ਮੇਲ ਨਹੀਂ ਖਾਂਦੇ।
- **Workflow ਲੌਜਿਕ/ਸ਼ਰਤਾਂ:** ਅਨੁਵਾਦ ਕਦਮ ਜਲਦੀ ਖਤਮ ਹੋ ਗਿਆ ਜਾਂ ਗਲਤ ਡਾਇਰੈਕਟਰੀ ਵਿੱਚ ਲਿਖਿਆ।

**ਕਿਵੇਂ ਠੀਕ ਕਰੀਏ / ਜਾਂਚੀਏ:**
1. **ਆਉਟਪੁੱਟ ਮੌਜੂਦਗੀ ਦੀ ਪੁਸ਼ਟੀ ਕਰੋ:** ਅਨੁਵਾਦ ਤੋਂ ਬਾਅਦ, ਵੇਖੋ ਕਿ `translations/` ਅਤੇ/ਜਾਂ `translated_images/` ਵਿੱਚ ਨਵੀਆਂ/ਤਬਦੀਲ ਫਾਇਲਾਂ ਹਨ।
   - ਜੇ ਨੋਟਬੁੱਕ ਅਨੁਵਾਦ ਕਰ ਰਹੇ ਹੋ, ਯਕੀਨੀ ਬਣਾਓ ਕਿ `.ipynb` ਫਾਇਲਾਂ `translations/<lang>/...` ਹੇਠ ਲਿਖੀਆਂ ਗਈਆਂ ਹਨ।
2. **`.gitignore` ਵੇਖੋ:** ਬਣੀਆਂ ਆਉਟਪੁੱਟ ਫਾਇਲਾਂ ਨੂੰ ਇਗਨੋਰ ਨਾ ਕਰੋ। ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਤੁਸੀਂ ਹੇਠਾਂ ਦਿੱਤੀਆਂ ਨੂੰ ਇਗਨੋਰ ਨਹੀਂ ਕਰ ਰਹੇ:
   - `translations/`
   - `translated_images/`
   - `*.ipynb` (ਜੇ ਨੋਟਬੁੱਕ ਅਨੁਵਾਦ ਕਰ ਰਹੇ ਹੋ)
3. **add-paths ਆਉਟਪੁੱਟ ਨਾਲ ਮੇਲ ਖਾਂਦੇ ਹਨ:** ਬਹੁ-ਲਾਈਨ ਮੁੱਲ ਵਰਤੋ ਅਤੇ ਦੋਵੇਂ ਫੋਲਡਰ ਸ਼ਾਮਲ ਕਰੋ ਜੇ ਲੋੜ ਹੋਵੇ:
   ```yaml
   with:
     add-paths: |
       translations/
       translated_images/
   ```
4. **ਡਿਬੱਗ ਲਈ PR ਫੋਰਸ ਕਰੋ:** ਅਸਥਾਈ ਤੌਰ 'ਤੇ ਖਾਲੀ commit ਮਨਜ਼ੂਰ ਕਰੋ ਤਾਂ ਜੋ ਵਾਇਰਿੰਗ ਠੀਕ ਹੈ ਜਾਂ ਨਹੀਂ ਪਤਾ ਲੱਗੇ:
   ```yaml
   with:
     commit-empty: true
   ```
5. **ਡਿਬੱਗ ਨਾਲ ਚਲਾਓ:** translate ਕਮਾਂਡ ਵਿੱਚ `-d` ਜੋੜੋ ਤਾਂ ਜੋ ਪਤਾ ਲੱਗੇ ਕਿਹੜੀਆਂ ਫਾਇਲਾਂ ਮਿਲੀਆਂ ਤੇ ਲਿਖੀਆਂ।
6. **ਪਰਮਿਸ਼ਨ (GITHUB_TOKEN):** ਯਕੀਨੀ ਬਣਾਓ ਕਿ workflow ਕੋਲ commit ਤੇ PR ਬਣਾਉਣ ਲਈ ਲਿਖਣ ਦੀ ਇਜਾਜ਼ਤ ਹੈ:
   ```yaml
   permissions:
     contents: write
     pull-requests: write
   ```


## ਤੇਜ਼ ਡਿਬੱਗਿੰਗ ਚੈੱਕਲਿਸਟ

ਅਨੁਵਾਦ ਸਮੱਸਿਆਵਾਂ ਹੱਲ ਕਰਦੇ ਸਮੇਂ:

1. **ਡਿਬੱਗ ਮੋਡ ਵਰਤੋ**: `-d` ਫਲੈਗ ਜੋੜੋ ਤਾਂ ਜੋ ਵਿਸਥਾਰ ਨਾਲ ਲੌਗ ਮਿਲਣ
2. **ਆਪਣੇ ਫਲੈਗ ਚੈੱਕ ਕਰੋ**: ਯਕੀਨੀ ਬਣਾਓ `-md`, `-img`, `-nb` ਤੁਹਾਡੀ ਮੁਰਾਦ ਨਾਲ ਮੇਲ ਖਾਂਦੇ ਹਨ
3. **ਕੰਫਿਗਰੇਸ਼ਨ ਵੇਖੋ**: ਆਪਣੇ `.env` ਫਾਇਲ ਵਿੱਚ ਲੋੜੀਂਦੀਆਂ ਕੁੰਜੀਆਂ ਹਨ ਜਾਂ ਨਹੀਂ
4. **ਇੱਕ-ਇੱਕ ਕਰਕੇ ਟੈਸਟ ਕਰੋ**: ਪਹਿਲਾਂ ਸਿਰਫ `-md` ਨਾਲ ਸ਼ੁਰੂ ਕਰੋ, ਫਿਰ ਹੋਰ ਟਾਈਪ ਜੋੜੋ
5. **ਫਾਇਲ ਬਣਤਰ ਵੇਖੋ**: ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਸਰੋਤ ਫਾਇਲਾਂ ਮੌਜੂਦ ਤੇ ਐਕਸੈਸ ਹੋ ਸਕਦੀਆਂ ਹਨ

ਹੋਰ ਵਿਸਥਾਰ ਲਈ ਉਪਲਬਧ ਕਮਾਂਡਾਂ ਅਤੇ ਫਲੈਗਾਂ ਬਾਰੇ ਜਾਣਕਾਰੀ ਲਈ [Command Reference](./command-reference.md) ਵੇਖੋ।

---

**ਅਸਵੀਕਰਨ**:
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਅਸੀਂ ਯਥਾਸੰਭਵ ਸਹੀ ਅਨੁਵਾਦ ਕਰਨ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਪਰ ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਵਿੱਚ ਰੱਖੋ ਕਿ ਆਟੋਮੈਟਿਕ ਅਨੁਵਾਦ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਣਪਛਾਤੀਆਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼, ਜਿਸ ਭਾਸ਼ਾ ਵਿੱਚ ਉਹ ਲਿਖਿਆ ਗਿਆ ਹੈ, ਨੂੰ ਹੀ ਅਧਿਕਾਰਤ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਜਰੂਰੀ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਹੋਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀਆਂ ਜਾਂ ਗਲਤ ਅਰਥ ਲਗਾਉਣ ਲਈ ਅਸੀਂ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।