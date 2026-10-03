# 문제 해결

번역 실행이 예기치 않게 성공하거나 구성 중 실패했거나 검토가 필요한 출력물을 생성할 때 이 페이지를 사용하세요.

## 여기에서 시작

1. 먼저 `translate -l "ko" -md` 같은 집중 명령을 실행하세요.
2. 콘솔 디버그 로그를 보려면 `-d`를 추가하세요.
3. 디버그 로그를 `<root-dir>/logs/` 아래에 저장하려면 `-s`를 추가하세요.
4. 번역 후 신선도, 구조 및 로컬 링크를 확인하려면 `co-op-review`를 실행하세요.

```bash
translate -l "ko" -md -d -s
co-op-review -l "ko"
```

## 구성 오류

### 언어 모델 공급자 없음

오류:

```text
No language model configuration found.
```

해결:

- Azure OpenAI, OpenAI 또는 Anthropic을 구성하세요.
- 명령이 실행되는 환경에 변수가 있는지 확인하세요.
- 로컬 사용의 경우 프로젝트 루트의 `.env`에 넣으세요.

자세한 내용은 [구성](configuration.md)을 참조하세요.

### Azure AI Vision 없이 이미지 번역

오류:

```text
Image translation requested but Azure AI Service is not configured.
```

해결:

- `AZURE_AI_SERVICE_API_KEY`를 추가하세요.
- `AZURE_AI_SERVICE_ENDPOINT`를 추가하세요.
- 또는 `translate -l "ko" -md` 같은 텍스트 전용 명령을 실행하세요.

### 잘못된 키 또는 엔드포인트

증상에는 `401`, 권한 오류가 가려짐, 또는 엔드포인트 접근 오류가 포함될 수 있습니다.

해결:

- 키가 엔드포인트와 동일한 Azure 리소스에 속하는지 확인하세요.
- `-img`를 사용할 때 리소스가 Vision을 지원하는지 확인하세요.
- Azure OpenAI 배포 이름과 API 버전이 배포와 일치하는지 확인하세요.
- 디버그 로그와 함께 실행하세요: `translate -l "ko" -md -d -s`.

## 번역된 파일이 없음

일반적인 원인:

- 선택된 플래그가 파일과 일치하지 않습니다.
- 이미 번역된 파일이 존재합니다.
- 소스 파일이 제외된 디렉터리 아래에 있습니다.
- 명령이 잘못된 프로젝트 루트에서 실행되고 있습니다.

확인 사항:

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -nb --dry-run
translate -l "ko" -img --dry-run
```

명령이 프로젝트 루트 외부에서 실행되는 경우 `--root-dir`를 사용하세요.

## 예상치 못한 링크 동작

링크 재작성은 선택한 콘텐츠 유형에 따라 달라집니다:

- `-nb` 포함: 노트북 링크가 번역된 노트북을 가리킬 수 있습니다.
- `-nb` 제외: 노트북 링크가 소스 노트북을 가리킨 상태로 남을 수 있습니다.
- `-img` 포함: 이미지 링크가 번역된 이미지를 가리킬 수 있습니다.
- `-img` 제외: 이미지 링크가 소스 이미지를 가리킨 상태로 남을 수 있습니다.

모든 내부 링크가 번역된 출력물을 우선하도록 하려면 전체 콘텐츠 번역을 실행하세요:

```bash
translate -l "ko" -md -nb -img
```

번역 후 링크 검토를 실행하세요:

```bash
co-op-review -l "ko"
```

## Markdown 렌더링 문제

번역된 Markdown이 올바르게 렌더링되지 않는 경우:

- 프론트매터가 `---`로 시작하고 끝나는지 확인하세요.
- 소스 파일과 번역된 파일 간에 코드 펜스의 개수가 일치하는지 확인하세요.
- 일반적인 구조 문제를 잡으려면 `co-op-review`를 실행하세요.
- 출력이 손상된 경우 특정 파일을 다시 번역하세요.

```bash
co-op-review -l "ko" --format github
```

## GitHub Action은 실행되었지만 풀 리퀘스트가 생성되지 않음

`peter-evans/create-pull-request`가 브랜치가 base보다 앞서 있지 않다고 보고하면, 워크플로우가 커밋할 파일을 찾지 못한 것입니다.

가능한 원인:

- 번역 실행이 변경을 생성하지 않았습니다.
- `.gitignore`가 `translations/`, `translated_images/` 또는 번역된 노트북을 제외합니다.
- `add-paths`가 생성된 출력 디렉터리와 일치하지 않습니다.
- 번역 단계가 조기에 종료되었습니다.

해결 방법:

1. 생성된 파일이 `translations/` 또는 `translated_images/`에 존재하는지 확인하세요.
2. `.gitignore`가 생성된 출력물을 무시하지 않는지 확인하세요.
3. 일치하는 `add-paths`를 사용하세요:

   ```yaml
   with:
     add-paths: |
       translations/
       translated_images/
   ```

4. 일시적으로 translate 명령에 디버그 플래그를 추가하세요:

   ```bash
   translate -l "ko" -md -d -s
   ```

5. 워크플로우 권한에 다음이 포함되어 있는지 확인하세요:

   ```yaml
   permissions:
     contents: write
     pull-requests: write
   ```

## 번역 품질

기계 번역은 사람의 검토가 필요할 수 있습니다. 실험적 품질 점수 평가와 낮은 신뢰도 수리 워크플로우가 필요할 때만 `evaluate`를 사용하세요.

!!! warning "실험적"
    `evaluate`는 규칙 기반 및 LLM 기반 검사를 사용할 수 있으며, 그 점수 모델과 메타데이터 동작은 변경될 수 있습니다. 변경에 대비한 워크플로우가 준비되어 있지 않다면 필수 CI 게이트에 포함하지 마세요.

결정론적 CI 검사를 위해서는 대신 `co-op-review`를 사용하세요.