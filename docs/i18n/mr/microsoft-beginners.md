# Microsoft सुरुवातीसाठी रिपॉझिटरीज

ही पृष्ठ Microsoft "For Beginners" रिपॉझिटरीजच्या देखभाल करणाऱ्यांसाठी आहे जे सामायिक "Other Courses" README विभाग वापरतात.

बहुतेक Co-op Translator वापरकर्त्यांना या पानाची आवश्यकता नाही.

## Other Courses विभागाचे आपोआप समक्रमण

आपल्या README मध्ये "Other Courses" विभागाच्या आसपास हे मार्कर जोडा:

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

प्रत्येक वेळी Co-op Translator CLI किंवा GitHub Actions द्वारे चालवल्यावर, तो मार्करदरम्यानचा मजकूर पॅक केलेल्या टेम्पलेटने बदलतो.

## सामायिक टेम्पलेट अपडेट करा

The template source lives at:

```text
src/co_op_translator/templates/other_courses.md
```

To update the shared content:

1. Edit the template.
2. Co-op Translator कडे एक pull request उघडा.
3. बदल रिलीज केल्यानंतर, लक्ष्य रिपॉझिटरीमध्ये Co-op Translator चालवा.

## Sparse Checkout सल्ला

बरीच अनुवादित आउटपुट्स असतील तर मोठ्या कोर्स रिपॉझिटरीज क्लोन करण्यासाठी महाग होऊ शकतात. आपण तयार करण्यात आलेल्या भाषा विभागांमध्ये हा सल्ला समाविष्ट करू शकता:

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