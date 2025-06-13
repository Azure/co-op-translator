<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9b1b247a8d0f1736459e0e9ede0d9c92",
  "translation_date": "2025-06-12T11:42:56+00:00",
  "source_file": "getting_started/markdown-only-mode.md",
  "language_code": "cs"
}
-->
# Markdown 전용 모드 사용하기

## 소개
Markdown 전용 모드는 프로젝트의 Markdown 콘텐츠만 번역하도록 설계되었습니다. 이 모드는 이미지 번역 과정을 건너뛰고 텍스트 콘텐츠에만 집중하여, 이미지 번역이 필요 없거나 Computer Vision 관련 환경 변수가 설정되어 있지 않은 경우에 적합합니다.

## 사용 시기
- Computer Vision 관련 환경 변수가 구성되어 있지 않을 때.
- 이미지 링크를 업데이트하지 않고 텍스트 콘텐츠만 번역하고 싶을 때.
- 사용자가 `-md` 명령줄 옵션을 명시적으로 지정했을 때.

## 활성화 방법
Markdown 전용 모드를 활성화하려면 명령어에 `-md` 옵션을 사용하세요. 예를 들어:
```
translate -l "ko" -md
```

또는 Computer Vision 관련 환경 변수가 구성되어 있지 않은 경우, `translate -l "ko"`를 실행하면 자동으로 Markdown 전용 모드로 전환됩니다.

```
translate -l "ko"
```

이 명령은 Markdown 콘텐츠를 한국어로 번역하며, 이미지 링크는 번역된 경로가 아닌 원본 경로로 유지합니다.

## 동작 방식
Markdown 전용 모드에서는:
- 번역 과정에서 이미지 번역 단계를 건너뜁니다.
- Markdown 내 이미지 링크는 변경되지 않고 원본 경로를 가리킵니다.

## 예시
### 이전
```markdown
![Image](../../../translated_images/image.aa98bae4d78871bb3b23ac9f938ff86539da4cd6fb4c52dafedc4665135c3d61.cs.png)
```
### Markdown 전용 모드 사용 후
```markdown
![Image](../../../translated_images/image.fc8708ffe1e1ca12c38822b1a382726da4b232025d1daa8a50ab75c8635d0c4a.cs.png)
```

## 문제 해결
- `-md` 옵션이 명령어에 올바르게 지정되었는지 확인하세요.
- Computer Vision 환경 변수가 번역 과정에 영향을 주지 않는지 점검하세요.

## 결론
Markdown 전용 모드는 이미지 링크를 변경하지 않고 텍스트 콘텐츠만 번역하는 간편한 방법을 제공합니다. 이미지 번역이 불필요하거나 Computer Vision 환경이 갖춰지지 않은 환경에서 특히 유용합니다.

**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné výklady vyplývající z použití tohoto překladu.