# Microsoft தொடக்கர்களுக்கான ரெப்போசிடரிகள்

இந்த பக்கம் பொதுவாக பகிரப்படும் "Other Courses" README பகுதியைப் பயன்படுத்தும் Microsoft "For Beginners" ரெப்போசிடரிகளை பராமரிப்பவர்களுக்கு арналғанது.

பெரும்பாலான Co-op Translator பயனர்களுக்கு இந்தப் பக்கம் தேவையில்லை.

## "Other Courses" பகுதியின் தானாக ஒத்திசை

உங்கள் README இல் உள்ள "Other Courses" பகுதியைச் சுற்றி இந்த குறிகளை இணைக்கவும்:

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

Co-op Translator CLI அல்லது GitHub Actions மூலம் இயங்கும் ஒவ்வொரு முறையும், அது குறிகளுக்கிடையிலுள்ள உள்ளடக்கத்தை தொகுக்கப்பட்ட டெம்ப்ளேட்டுடன் மாற்றும்.

## பகிரப்பட்ட டெம்ப்ளேட்டை புதுப்பித்தல்

டெம்ப்ளேட் மூலத்தளம் அமைந்துள்ளது:

```text
src/co_op_translator/templates/other_courses.md
```

பகிரப்பட்ட உள்ளடக்கத்தை புதுப்பிக்க:

1. டெம்ப்ளேட்டை தொகுக்கவும்.
2. Co-op Translator-க்கு ஒரு pull request திறக்கவும்.
3. மாற்றம் வெளியிடப்பட்ட பிறகு, இலக்கு ரெப்போசிடரியில் Co-op Translator-ஐ இயக்கவும்.

## Sparse Checkout அறிவுரை

பல மொழிகளில் மொழியாக்கப்பட்ட பல அவுட்புட்கள் இடம்பெற்றால், பெரிய பாட ரெப்போசிடரிகளை கிளோன் செய்வது செலவு அதிகமாகிவிடும். நீங்கள் உருவாக்கப்படும் மொழி பிரிவுகளில் இந்த அறிவுறுத்தலை சேர்க்கலாம்:

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