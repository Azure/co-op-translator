# 문제 해결

번역 실행이 예기치 않게 성공했거나 구성 중 실패했거나 검토가 필요한 출력이 생성된 경우 이 페이지를 사용하세요.

## 시작하기

1. 먼저 다음과 같은 특정 명령을 실행하세요: `translate -l "ko" -md`.
2. 콘솔 디버그 로그를 위해 `-d`를 추가하세요.
3. 디버그 로그를 `<root-dir>/logs/`에 저장하려면 `-s`를 추가하세요.
4. 번역 후 신선도, 구조, 로컬 링크를 확인하려면 `co-op-review`를 실행하세요.

```bash
translate -l "ko" -md -d -s
co-op-review -l "ko"
```

## 구성 오류

### 언어 모델 제공자 없음

오류:

```text
No language model configuration found.
```

해결:

- Azure OpenAI 또는 OpenAI를 구성하세요.
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

증상으로는 `401`, 권한 오류(비공개 처리됨) 또는 엔드포인트 접근 오류 등이 있을 수 있습니다.

해결:

- 키가 엔드포인트와 동일한 Azure 리소스에 속하는지 확인하세요.
- `-img`를 사용할 때 리소스가 Vision을 지원하는지 확인하세요.
- Azure OpenAI 배포 이름과 API 버전이 배포와 일치하는지 확인하세요.
- 디버그 로그와 함께 실행하세요: `translate -l "ko" -md -d -s`.

## 번역된 파일이 없음

일반적인 원인:

- 선택한 플래그가 파일과 일치하지 않습니다.
- 이미 번역된 파일이 존재합니다.
- 소스 파일이 제외된 디렉터리 아래에 있습니다.
- 명령이 잘못된 프로젝트 루트에서 실행되고 있습니다.

확인 사항:

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -nb --dry-run
translate -l "ko" -img --dry-run
```

명령을 프로젝트 루트 밖에서 실행할 때는 `--root-dir`를 사용하세요.

## 예기치 않은 링크 동작

링크 재작성은 선택한 콘텐츠 유형에 따라 달라집니다:

- `-nb` 포함: 노트북 링크가 번역된 노트북을 가리킬 수 있습니다.
- `-nb` 제외: 노트북 링크가 원본 노트북을 가리킬 수 있습니다.
- `-img` 포함: 이미지 링크가 번역된 이미지를 가리킬 수 있습니다.
- `-img` 제외: 이미지 링크가 원본 이미지를 가리킬 수 있습니다.

모든 내부 링크가 번역된 출력을 우선하도록 하려면 전체 콘텐츠 번역을 실행하세요:

```bash
translate -l "ko" -md -nb -img
```

번역 후 링크 검토를 실행하세요:

```bash
co-op-review -l "ko"
```

## 마크다운 렌더링 문제

번역된 마크다운이 올바르게 렌더링되지 않는 경우:

- 프론트매터가 `---`로 시작하고 끝나는지 확인하세요.
- 소스 파일과 번역된 파일 간에 코드 펜스의 개수가 일치하는지 확인하세요.
- `co-op-review`를 실행하여 일반적인 구조 문제를 잡아내세요.
- 출력이 손상된 경우 해당 파일만 다시 번역하세요.

```bash
co-op-review -l "ko" --format github
```

## GitHub 액션이 실행되었지만 풀 리퀘스트가 생성되지 않음

`peter-evans/create-pull-request`가 브랜치가 기준보다 앞서지 않는다고 보고하면 워크플로가 커밋할 파일을 찾지 못한 것입니다.

가능한 원인:

- 번역 실행으로 변경 사항이 생성되지 않았습니다.
- `.gitignore`가 `translations/`, `translated_images/` 또는 번역된 노트북을 제외합니다.
- `add-paths`가 생성된 출력 디렉터리와 일치하지 않습니다.
- 번역 단계가 조기에 종료되었습니다.

해결 방법:

1. 생성된 파일이 `translations/` 또는 `translated_images/`에 있는지 확인하세요.
2. `.gitignore`가 생성된 출력을 무시하지 않는지 확인하세요.
3. 일치하는 `add-paths`를 사용하세요:

   ```yaml
   with:
     add-paths: |
       translations/
       translated_images/
   ```

4. 일시적으로 번역 명령에 디버그 플래그를 추가하세요:

   ```bash
   translate -l "ko" -md -d -s
   ```

5. 워크플로 권한에 다음이 포함되어 있는지 확인하세요:

   ```yaml
   permissions:
     contents: write
     pull-requests: write
   ```

## 번역 품질

기계 번역은 인간의 검토가 필요할 수 있습니다. 실험적인 품질 점수 산정 및 낮은 신뢰도 수리 워크플로를 원할 때만 `evaluate`를 사용하세요.

!!! warning "Experimental"
    `evaluate`는 규칙 기반 및 LLM 기반 검사들을 사용할 수 있으며, 그 점수 모델과 메타데이터 동작은 변경될 수 있습니다. 워크플로가 이러한 변경에 대비되어 있지 않다면 필수 CI 관문에서 제외하세요.

결정론적 CI 검사에는 대신 `co-op-review`를 사용하세요.