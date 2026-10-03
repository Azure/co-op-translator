# GitHub Actions

Sử dụng GitHub Actions khi bạn muốn một kho lưu trữ tự động dịch tài liệu đã thay đổi và mở một pull request với các kết quả đã tạo.

Bắt đầu với cài đặt `GITHUB_TOKEN` tiêu chuẩn, kể cả đối với các kho thuộc tổ chức nơi chính sách cho phép. Xem [Cài đặt GitHub App](#github-app-setup) khi tổ chức của bạn yêu cầu một định danh App hoặc bạn cần chạy workflow hạ nguồn tự động.

**Human edits:** các workflow này sẽ dịch lại toàn bộ các tệp nguồn đã thay đổi và có thể ghi đè nội dung đã được chỉnh sửa trong bản dịch. Xem xét từng PR trước khi hợp nhất. Việc giữ nguyên cấp khối Markdown của các chỉnh sửa được chấp nhận đòi hỏi tích hợp tùy chỉnh với [Python API translation state provider](api.md#preserve-accepted-human-edits-with-a-translation-state-provider).

## PR dịch README đầu tiên của bạn

Bắt đầu với một tệp gốc `README.md` và một ngôn ngữ đích. Workflow này chỉ dịch Markdown, vì vậy không cần Azure AI Vision.

1. Sao chép [translate-readme.yml](../../assets/workflows/translate-readme.yml) ([xem mẫu trên GitHub](https://github.com/Azure/co-op-translator/blob/main/docs/assets/workflows/translate-readme.yml)) vào `.github/workflows/translate-readme.yml` trong kho bạn muốn dịch, và commit nó vào nhánh mặc định của kho đó. Mẫu sử dụng Action gốc trong `Azure/co-op-translator@main`, vốn cài đặt CLI từ cùng ref nguồn. Khóa một commit đã được duyệt để chạy có thể tái tạo.
2. Mở **Actions > Translate README > Run workflow**, chọn một ngôn ngữ, và để **Chỉ xem trước** được chọn. Xem lại ước tính token trong bước xem trước. Chế độ xem trước không gọi nhà cung cấp mô hình, không ghi bản dịch, và không tạo PR.
3. Thêm các bí mật cho một [nhà cung cấp văn bản](#prerequisites), và bật **Cho phép GitHub Actions tạo và phê duyệt pull requests** trong **Settings > Actions > General**. Mẫu yêu cầu `contents: write` và `pull-requests: write` cho job của nó; bạn không cần thay đổi quyền mặc định cho mỗi workflow. Nếu chính sách tổ chức chặn các quyền hoặc cài đặt này, hãy hỏi quản trị viên về một [GitHub App](#github-app-setup) được phê duyệt.
4. Chạy workflow một lần nữa với **Chỉ xem trước** không được chọn. Nó sẽ xem trước, dịch, chạy `co-op-review --readme-only`, và chỉ tạo hoặc cập nhật một PR dịch sau khi việc dịch và xem xét thành công. Tóm tắt workflow liên kết tới PR.
5. Xem xét cách diễn đạt và các thay đổi tệp trong PR, sau đó hợp nhất khi sẵn sàng. Workflow không tự động hợp nhất.

PR chỉ chứa `translations/<language>/README.md` và tệp metadata ngôn ngữ của nó. README nguồn vẫn không thay đổi, và các liên kết tới tài liệu khác tiếp tục trỏ tới các tài liệu nguồn. Nội dung PR liệt kê các tệp đã thay đổi và kết quả kiểm tra cấu trúc. Nếu dịch hoặc duyệt thất bại, kiểm tra tóm tắt workflow và nhật ký bước thất bại; không có PR nào được tạo. Nếu không có thay đổi, không cần PR mới.

**Lưu ý về Tổ chức và CI:** Một GitHub App là tùy chọn, không phải là yêu cầu của quyền sở hữu tổ chức. Với `GITHUB_TOKEN`, các workflow pull-request để mở, cập nhật hoặc mở lại PR yêu cầu một người dùng có quyền ghi chọn **Approve workflows to run**. Các workflow push không được kích hoạt bởi token này. Đối với CI hạ nguồn không giám sát, xem [GitHub App Setup](#github-app-setup) và GitHub's [workflow triggering rules](https://docs.github.com/en/actions/how-tos/writing-workflows/choosing-when-your-workflow-runs/triggering-a-workflow).

## Yêu cầu trước

Trước khi tạo workflow, cấu hình các bí mật dịch vụ AI mà quá trình dịch của bạn cần.

Dịch văn bản yêu cầu một nhà cung cấp mô hình ngôn ngữ:

- Azure OpenAI: `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_MODEL_NAME`, `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME`, `AZURE_OPENAI_API_VERSION`
- OpenAI: `OPENAI_API_KEY`, `OPENAI_CHAT_MODEL_ID`, cùng với tùy chọn `OPENAI_ORG_ID` và `OPENAI_BASE_URL`
- Anthropic: `ANTHROPIC_API_KEY`, `ANTHROPIC_MODEL`, cùng với tùy chọn `ANTHROPIC_BASE_URL`

Dịch hình ảnh còn yêu cầu Azure AI Vision:

- `AZURE_AI_SERVICE_API_KEY`
- `AZURE_AI_SERVICE_ENDPOINT`

Xem [Cấu hình](configuration.md) và [Thiết lập Azure AI](azure-ai-setup.md) để biết chi tiết cấu hình cục bộ.

## Cài đặt tiêu chuẩn

Sau khi thử workflow README, sử dụng cài đặt này để dịch các tệp Markdown của một kho sang nhiều ngôn ngữ. Nó chạy kiểm tra Markdown trước khi mở PR và không yêu cầu Azure AI Vision.

### Bước 1: Thêm bí mật của kho

Trong kho đích của bạn, mở **Settings** > **Secrets and variables** > **Actions**, sau đó thêm các bí mật nhà cung cấp mà workflow của bạn sẽ sử dụng.

![Chọn bí mật Actions](../../assets/github-actions/select-setting-action.png)

### Bước 2: Bật quyền Workflow

Mở **Settings** > **Actions** > **General**.

Trong **Workflow permissions**:

1. Bật **Cho phép GitHub Actions tạo và phê duyệt pull requests**.
2. Save the setting.

Job dưới đây yêu cầu `contents: write` và `pull-requests: write` một cách rõ ràng. Giữ quyền workflow mặc định của kho không đổi. Nếu chính sách tổ chức chặn việc tạo PR, hỏi quản trị viên về một [GitHub App](#github-app-setup) được phê duyệt.

### Bước 3: Thêm Workflow

Tạo `.github/workflows/co-op-translator.yml`:

```yaml
name: Co-op Translator

on:
  push:
    branches:
      - main

jobs:
  co-op-translator:
    runs-on: ubuntu-latest
    env:
      TARGET_LANGUAGES: "es fr de"

    permissions:
      contents: write
      pull-requests: write

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Set up Python
        uses: actions/setup-python@v7
        with:
          python-version: "3.11"

      - name: Install Co-op Translator
        run: |
          python -m pip install --upgrade pip
          pip install co-op-translator

      - name: Run Co-op Translator
        env:
          PYTHONIOENCODING: utf-8
          AZURE_OPENAI_API_KEY: ${{ secrets.AZURE_OPENAI_API_KEY }}
          AZURE_OPENAI_ENDPOINT: ${{ secrets.AZURE_OPENAI_ENDPOINT }}
          AZURE_OPENAI_MODEL_NAME: ${{ secrets.AZURE_OPENAI_MODEL_NAME }}
          AZURE_OPENAI_CHAT_DEPLOYMENT_NAME: ${{ secrets.AZURE_OPENAI_CHAT_DEPLOYMENT_NAME }}
          AZURE_OPENAI_API_VERSION: ${{ secrets.AZURE_OPENAI_API_VERSION }}
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
          OPENAI_ORG_ID: ${{ secrets.OPENAI_ORG_ID }}
          OPENAI_CHAT_MODEL_ID: ${{ secrets.OPENAI_CHAT_MODEL_ID }}
          OPENAI_BASE_URL: ${{ secrets.OPENAI_BASE_URL }}
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
          ANTHROPIC_MODEL: ${{ secrets.ANTHROPIC_MODEL }}
          ANTHROPIC_BASE_URL: ${{ secrets.ANTHROPIC_BASE_URL }}
        run: |
          translate -l "$TARGET_LANGUAGES" -md -y

      - name: Review Markdown translations
        run: |
          python - <<'PY'
          import os
          from co_op_translator.api import run_review

          run_review(
              language_codes=os.environ["TARGET_LANGUAGES"].split(),
              markdown=True,
              notebook=False,
              output_format="github",
          )
          PY

      - name: Create Pull Request with translations
        uses: peter-evans/create-pull-request@v5
        with:
          token: ${{ secrets.GITHUB_TOKEN }}
          commit-message: "Update translations via Co-op Translator"
          title: "Update translations via Co-op Translator"
          body: |
            This PR updates translations for recent changes to the main branch.
            Markdown structure, freshness, and local links were reviewed.
            Review translation wording before merging.

            Generated by Co-op Translator.
          branch: update-translations
          base: main
          labels: translation, automated-pr
          delete-branch: true
          add-paths: |
            translations/
```

Thay `TARGET_LANGUAGES` thành các ngôn ngữ mà dự án của bạn cần. Việc duyệt sử dụng Python API để chỉ kiểm tra Markdown, phù hợp với bước dịch. Lỗi dịch hoặc duyệt sẽ dừng job trước khi tạo PR. Workflow không tự động hợp nhất PR. Đối với các kho lớn, thêm bộ lọc `paths:` dưới `on.push` để workflow chỉ chạy khi có thay đổi tài liệu.

### Tùy chọn: notebooks và hình ảnh

Đối với notebooks, thêm `-nb` vào lệnh dịch và đặt `notebook=True` trong bước duyệt. Đối với văn bản trong hình ảnh, cấu hình hai [Azure AI Vision secrets](#prerequisites), truyền chúng trong `env` của bước dịch, thêm `-img` vào lệnh, và thêm `translated_images/` vào `add-paths` của bước PR. Xem lại các hình ảnh đã dịch bằng mắt; bước duyệt xác định không chứng nhận độ chính xác văn bản hình ảnh hoặc ngôn ngữ.

## Cài đặt GitHub App

Sử dụng một GitHub App được phê duyệt khi tổ chức của bạn yêu cầu một định danh App, hoặc khi PR sinh ra cần kích hoạt CI hạ nguồn mà không qua bước phê duyệt `GITHUB_TOKEN`. App không bỏ qua chính sách tổ chức; quản trị viên vẫn kiểm soát việc cài đặt và quyền của nó.

### Bước 1: Tạo hoặc Cài đặt một GitHub App

Sử dụng App do tổ chức cung cấp nếu có, hoặc tạo một App có quyền đọc/ghi tới **Contents** và **Pull requests**. Cài đặt nó lên kho đích với mọi phê duyệt tổ chức cần thiết.

Ghi lại:

- App ID
- Nội dung private key

Lưu chúng làm bí mật của kho:

- `GH_APP_ID`
- `GH_APP_PRIVATE_KEY`

### Bước 2: Tạo Token của App

Thêm bước này ngay trước bước pull request hiện có. Đối với mẫu README, sử dụng cùng điều kiện thành công để các xem trước và dịch thất bại không yêu cầu token App:

```yaml
      - name: Authenticate GitHub App
        id: generate_token
        if: ${{ !inputs.preview && steps.translate.outcome == 'success' && steps.review.outcome == 'success' }}
        uses: actions/create-github-app-token@v2
        with:
          app-id: ${{ secrets.GH_APP_ID }}
          private-key: ${{ secrets.GH_APP_PRIVATE_KEY }}
          permission-contents: write
          permission-pull-requests: write
```

Sau đó chỉ thay đổi input `token` của bước pull request hiện có thành `${{ steps.generate_token.outputs.token }}`. Giữ nguyên điều kiện thành công, nhánh, nội dung PR và `add-paths`. Token mặc định được giới hạn cho kho hiện tại. Khi điều chỉnh cài đặt tiêu chuẩn thay vì mẫu README, bỏ `if` ở trên: workflow đó sử dụng điều kiện thành công mặc định, vì vậy việc tạo token và tạo PR chỉ chạy sau khi dịch và duyệt thành công.

Xem [create-github-app-token Action](https://github.com/actions/create-github-app-token/tree/v2) chính thức để biết cài đặt và quyền token.

## Giới hạn Runner

Các runner do GitHub-hosted cung cấp có thời lượng job tối đa. Các kho lớn hoặc nhiều ngôn ngữ đích có thể vượt quá giới hạn đó.

Đối với khối lượng dịch lớn:

- Dịch ít ngôn ngữ hơn cho mỗi lần chạy.
- Sử dụng các cờ nội dung như `-md`, `-nb`, hoặc `-img`.
- Sử dụng runner tự lưu trữ khi kích thước kho hoặc độ trễ mô hình khiến các runner được host trở nên không đáng tin cậy.

## Duyệt trong CI

Sử dụng `co-op-review` khi một pull request cần xác minh các bản dịch được tạo ra mà không gọi nhà cung cấp LLM hoặc Vision.

```yaml
      - name: Review translated outputs
        run: |
          co-op-review --changed-from "origin/${{ github.base_ref }}" --format github
```

`co-op-review` là một lệnh duyệt xác định (beta). Các kiểm tra và schema đầu ra của nó có thể thay đổi, nhưng nó được thiết kế an toàn cho CI vì nó không ghi tệp hoặc gọi nhà cung cấp mô hình.