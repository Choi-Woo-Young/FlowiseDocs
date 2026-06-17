# Slack MCP

## 1. 사전 필수 사항

Slack MCP Node를 사용하기 전에 다음이 필요합니다:

* **Slack 계정**: [https://slack.com/](https://slack.com/)에서 가입
* **Slack 워크스페이스**
* **OAuth 클라이언트 앱**: Slack 워크스페이스 내에서 생성됩니다. 이렇게 하면 **Client ID**와 **Client Secret**을 얻을 수 있습니다.

***

## 2. Slack 자격증명 설정

### 2.1 Slack에서 새 앱 생성

1. [https://api.slack.com/apps/new](https://api.slack.com/apps/new)으로 이동합니다
2. 매니페스트를 통해 또는 처음부터 새 앱을 생성합니다.

<figure><img src="../../../.gitbook/assets/image (174).png" alt=""><figcaption></figcaption></figure>

3. 앱이 생성된 후 Client ID와 Client Secret을 가져옵니다.

<figure><img src="../../../.gitbook/assets/image (310).png" alt=""><figcaption></figcaption></figure>

### 2.2 Flowise에 자격증명 추가

1. Flowise에서 사이드바의 **Credentials**로 이동합니다.
2. **Add Credential**을 클릭하고 **Slack User Token OAuth2**를 검색합니다.
3. 다음 필드를 채웁니다:

<table><thead><tr><th>필드</th><th>설명</th><th width="250">예시</th></tr></thead><tbody><tr><td><strong>Client ID</strong></td><td>Slack의 OAuth Client ID</td><td><code>wBSGhxxxx</code></td></tr><tr><td><strong>Client Secret</strong></td><td>OAuth Client Secret (안전하게 저장됨)</td><td><code>••••••••</code></td></tr><tr><td><strong>Scopes</strong></td><td><em>(선택사항)</em> 공백으로 구분된 Scope.</td><td><p><code>search:read.public search:read.private search:read.mpim search:read.im search:read.files search:read.users groups:history</code></p><p><code>mpim:history</code></p><p><code>im:history</code></p><p><code>channels:history</code></p><p><code>chat:write</code></p><p><code>canvases:read canvases:write</code></p><p><code>users:read</code></p><p><code>users:read.email</code></p></td></tr></tbody></table>

4. OAuth Redirect URL을 복사한 다음 **Save**를 클릭합니다.

<figure><img src="../../../.gitbook/assets/image (338).png" alt="" width="548"><figcaption></figcaption></figure>

**팁:** 프로덕션 환경의 경우 필요한 가장 좁은 Scope를 사용하세요. 사용 가능한 [Scope](https://docs.slack.dev/reference/scopes/)를 참조하세요.

### 2.3 Slack 앱에 Redirect URL 추가

1. 왼쪽 사이드 네비게이션 바에서 OAuth & Permissions를 선택합니다:

<figure><img src="../../../.gitbook/assets/image (340).png" alt=""><figcaption></figcaption></figure>

2. 아래로 스크롤하면 Redirect URLs 섹션이 보입니다. 이전 단계에서 복사한 Redirect URL을 추가합니다. 그런 다음 Save URLs를 클릭합니다.

<figure><img src="../../../.gitbook/assets/image (341).png" alt="" width="563"><figcaption></figcaption></figure>

***

## 3. Slack MCP 추가

1. Agent Node를 드래그 앤 드롭합니다.
2. 새로운 Slack MCP Tool을 추가합니다.

<figure><img src="../../../.gitbook/assets/image (345).png" alt="" width="500"><figcaption></figcaption></figure>

3. 사전 구성된 자격증명을 선택하고 편집 버튼을 클릭합니다. Authenticate를 클릭합니다.

<figure><img src="../../../.gitbook/assets/image (342).png" alt="" width="538"><figcaption></figcaption></figure>

3. Slack 팝업 창이 나타나면 권한을 검토하고 Allow를 클릭합니다.

<figure><img src="../../../.gitbook/assets/image (347).png" alt="" width="542"><figcaption></figcaption></figure>

4. 인증된 후 새로고침 버튼을 클릭하여 사용 가능한 작업을 로드합니다.

<figure><img src="../../../.gitbook/assets/image (348).png" alt=""><figcaption></figcaption></figure>

5. 작업을 선택합니다. _팁: Agent에 필요한 작업만 선택하세요. 더 적은 Tool은 LLM이 더 나은 결정을 내리고 Token 사용을 줄이는 데 도움이 됩니다._

<figure><img src="../../../.gitbook/assets/image (339).png" alt="" width="452"><figcaption></figcaption></figure>

6. 완료! Agent와 대화를 시작하고 Slack MCP Tool을 호출하는 방식을 볼 수 있습니다.

<figure><img src="../../../.gitbook/assets/image (349).png" alt=""><figcaption></figcaption></figure>
