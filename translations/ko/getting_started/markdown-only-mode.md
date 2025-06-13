<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9b1b247a8d0f1736459e0e9ede0d9c92",
  "translation_date": "2025-06-12T11:38:11+00:00",
  "source_file": "getting_started/markdown-only-mode.md",
  "language_code": "ko"
}
-->
# Markdown 전용 모드 사용하기

## 소개  
Markdown 전용 모드는 프로젝트의 Markdown 내용만 번역하도록 설계되었습니다. 이 모드는 이미지 번역 과정을 건너뛰고 텍스트 내용에만 집중하기 때문에, 이미지 번역이 필요 없거나 Computer Vision 관련 환경 변수가 설정되어 있지 않은 상황에 적합합니다.

## 사용 시기  
- Computer Vision 관련 환경 변수가 설정되어 있지 않을 때  
- 이미지 링크를 변경하지 않고 텍스트 내용만 번역하고 싶을 때  
- 사용자가 `-md` 명령줄 옵션을 명시적으로 지정했을 때  

## 활성화 방법  
Markdown 전용 모드를 활성화하려면 명령어에 `-md` 옵션을 사용하세요. 예를 들어:  
```
translate -l "ko" -md
```

또는 Computer Vision 관련 환경 변수가 설정되어 있지 않은 경우, `translate -l "ko"` 명령어를 실행하면 자동으로 Markdown 전용 모드로 전환됩니다.

```
translate -l "ko"
```

이 명령은 Markdown 내용을 한국어로 번역하며, 이미지 링크는 번역된 이미지 경로로 변경하지 않고 원래 경로를 유지합니다.

## 동작 방식  
Markdown 전용 모드에서는:  
- 이미지 번역 단계가 생략됩니다.  
- Markdown 내 이미지 링크는 변경되지 않고 원래 경로를 가리킵니다.

## 예시  
### 이전  
```markdown
![Image](../../../translated_images/image.aa98bae4d78871bb3b23ac9f938ff86539da4cd6fb4c52dafedc4665135c3d61.ko.png)
```  
### Markdown 전용 모드 사용 후  
```markdown
![Image](../../../translated_images/image.fc8708ffe1e1ca12c38822b1a382726da4b232025d1daa8a50ab75c8635d0c4a.ko.png)
```

## 문제 해결  
- 명령어에 `-md` 옵션이 정확히 지정되었는지 확인하세요.  
- Computer Vision 환경 변수가 번역 과정에 영향을 주지 않는지 점검하세요.

## 결론  
Markdown 전용 모드는 이미지 링크를 변경하지 않고 텍스트 내용만 간편하게 번역할 수 있는 방법입니다. 이미지 번역이 필요 없거나 Computer Vision 환경이 갖춰지지 않은 경우에 특히 유용합니다.

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 노력하고 있으나, 자동 번역에는 오류나 부정확한 부분이 있을 수 있음을 양지해 주시기 바랍니다. 원본 문서는 해당 언어의 원문이 권위 있는 출처로 간주되어야 합니다. 중요한 정보의 경우 전문적인 인간 번역을 권장합니다. 본 번역 사용으로 인한 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.